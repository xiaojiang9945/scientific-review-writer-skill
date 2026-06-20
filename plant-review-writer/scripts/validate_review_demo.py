#!/usr/bin/env python3
"""Validate the packaged plant-review-writer demo and repository hygiene."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = ROOT / "plant-review-writer"
DEMO_DIR = ROOT / "examples" / "plant-kinetochore-review"
DEMO_OUTPUT = DEMO_DIR / "output" / "plant_kinetochore_review_demo.md"
DEMO_INPUT = DEMO_DIR / "input" / "source_review_en_strict.md"
DEMO_QC = DEMO_DIR / "qc" / "demo_qc_public.md"

PRIVACY_PATTERNS = [
    re.compile(r"[A-Za-z]:\\"),
    re.compile(r"(?i)\bUsers\\"),
    re.compile(r"(?i)\bOneDrive\b"),
    re.compile(r"(?i)\bxiaoj\b"),
    re.compile(r"ghp_[A-Za-z0-9_]+"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"(?i)OPENAI_API_KEY\s*="),
    re.compile(r"(?i)api[_-]?key\s*[:=]"),
    re.compile(r"(?i)password\s*[:=]"),
    re.compile(r"(?i)token\s*[:=]"),
]

FORMAL_MANUSCRIPT_BANS = [
    "claim boundary",
    "prompt trace",
    "intermediate generation",
    "as requested",
    "workflow note",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z][A-Za-z0-9'-]*", text))


def section_between(text: str, start_pattern: str, end_pattern: str) -> str:
    start = re.search(start_pattern, text, re.IGNORECASE | re.MULTILINE)
    if not start:
        return ""
    end = re.search(end_pattern, text[start.end() :], re.IGNORECASE | re.MULTILINE)
    if not end:
        return text[start.end() :]
    return text[start.end() : start.end() + end.start()]


def scan_privacy() -> list[str]:
    hits: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or path.is_dir():
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".docx", ".skill"}:
            continue
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            continue
        for pattern in PRIVACY_PATTERNS:
            for match in pattern.finditer(text):
                rel = path.relative_to(ROOT).as_posix()
                hits.append(f"{rel}: {pattern.pattern}: {match.group(0)[:80]}")
    return hits


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    required = [
        SKILL_DIR / "SKILL.md",
        SKILL_DIR / "references" / "review_workflow.md",
        SKILL_DIR / "references" / "evidence_and_citation_integrity.md",
        SKILL_DIR / "references" / "structure_and_style.md",
        SKILL_DIR / "references" / "figure_and_table_integration.md",
        SKILL_DIR / "references" / "nature_reference_style.md",
        SKILL_DIR / "references" / "five_round_qc.md",
        DEMO_INPUT,
        DEMO_OUTPUT,
        DEMO_QC,
    ]
    for path in required:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT).as_posix()}")

    if errors:
        print(json.dumps({"status": "failed", "errors": errors}, indent=2))
        return 1

    output = read_text(DEMO_OUTPUT)
    qc = read_text(DEMO_QC)

    if not re.search(r"^#\s+.+", output, re.MULTILINE):
        errors.append("Demo output is missing a title heading.")

    abstract = section_between(output, r"^\*\*Abstract\*\*\s*$", r"^\*\*Keywords")
    abstract_words = word_count(abstract)
    if abstract_words < 150 or abstract_words > 280:
        errors.append(f"Abstract length outside expected demo range: {abstract_words} words.")

    keywords_match = re.search(r"^\*\*Keywords:\*\*\s*(.+)$", output, re.MULTILINE)
    keyword_count = 0
    if not keywords_match:
        errors.append("Demo output is missing a Keywords line.")
    else:
        keyword_count = len([k.strip() for k in keywords_match.group(1).split(";") if k.strip()])
        if keyword_count < 5 or keyword_count > 7:
            errors.append(f"Expected 5-7 keywords, found {keyword_count}.")

    figure_links = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", output)
    if len(figure_links) < 4:
        errors.append(f"Expected at least 4 figure links, found {len(figure_links)}.")
    for link in figure_links:
        if re.match(r"^[a-z]+://", link):
            errors.append(f"External figure link is not allowed in demo output: {link}")
            continue
        fig_path = DEMO_OUTPUT.parent / link
        if not fig_path.exists():
            errors.append(f"Figure link does not resolve: {link}")

    caption_count = len(re.findall(r"\*\*Figure\s+\d+\.", output))
    if caption_count < len(figure_links):
        errors.append(f"Figure captions fewer than figure links: {caption_count} captions for {len(figure_links)} links.")

    reference_count = len(re.findall(r"^\d+\.\s+", output, re.MULTILINE))
    if reference_count < 30:
        errors.append(f"Expected at least 30 references, found {reference_count}.")

    lower_output = output.lower()
    for phrase in FORMAL_MANUSCRIPT_BANS:
        if phrase in lower_output:
            errors.append(f"Formal manuscript contains banned workflow phrase: {phrase}")

    for round_no in range(1, 6):
        if f"Round {round_no}" not in qc:
            errors.append(f"QC file missing Round {round_no}.")

    privacy_hits = scan_privacy()
    if privacy_hits:
        errors.extend([f"Privacy scan hit: {hit}" for hit in privacy_hits[:20]])
        if len(privacy_hits) > 20:
            errors.append(f"Privacy scan has {len(privacy_hits) - 20} additional hits.")

    if "v1.0.0" in read_text(ROOT / "README.md") and "private iteration" not in read_text(ROOT / "README.md").lower():
        warnings.append("README mentions v1.0.0 without private-iteration context.")

    summary = {
        "status": "passed" if not errors else "failed",
        "abstract_words": abstract_words,
        "keywords": keyword_count,
        "figures": len(figure_links),
        "captions": caption_count,
        "references": reference_count,
        "warnings": warnings,
        "errors": errors,
    }
    print(json.dumps(summary, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
