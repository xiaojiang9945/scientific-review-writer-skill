import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


IN = Path("outputs/plant_review_skill_work/plant_review_corpus_2020_2026_source_balanced250.tsv")
OUT = Path("outputs/plant_review_skill_work/plant_review_style_synthesis.md")

STOP = {
    "the", "and", "of", "in", "to", "for", "a", "an", "on", "with", "from",
    "by", "as", "at", "into", "under", "their", "its", "is", "are", "new",
    "review", "plant", "plants",
}


def words(s):
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]+", s) if w.lower() not in STOP]


def first_sentence(s):
    s = s.strip()
    if not s:
        return ""
    m = re.split(r"(?<=[.!?])\s+", s, maxsplit=1)
    return m[0]


rows = list(csv.DictReader(IN.open(encoding="utf-8"), delimiter="\t"))

title_tokens = Counter()
title_bigrams = Counter()
patterns = Counter()
by_journal = defaultdict(list)
first_verbs = Counter()

for r in rows:
    title = r["title"]
    ws = words(title)
    title_tokens.update(ws)
    title_bigrams.update(zip(ws, ws[1:]))
    by_journal[r["journal"]].append(r)
    if ":" in title:
        patterns["colon title"] += 1
    if "?" in title:
        patterns["question title"] += 1
    if re.search(r"\bhow\b", title, re.I):
        patterns["How-title"] += 1
    if re.search(r"\bfrom\b.+\bto\b", title, re.I):
        patterns["from-to title"] += 1
    if re.search(r"\bmechanism", title, re.I):
        patterns["mechanism title"] += 1
    if re.search(r"\bfuture|toward|towards|frontier|challenge|opportunit", title, re.I):
        patterns["forward-looking title"] += 1
    fs = first_sentence(r["abstract"])
    m = re.search(r"\b(is|are|has|have|plays|play|controls|regulates|underpins|requires|faces|threatens)\b", fs, re.I)
    if m:
        first_verbs[m.group(1).lower()] += 1


with OUT.open("w", encoding="utf-8") as f:
    f.write("# Plant Review Style Synthesis\n\n")
    f.write("Corpus: 250 source-balanced high-citation plant-related reviews from 2020-2026 in Cell, Nature, Science, Nature Biotechnology, Nature Plants, The Plant Cell, Annual Review of Plant Biology, and Trends in Plant Science. Source records are in `plant_review_corpus_2020_2026_source_balanced250.tsv`.\n\n")
    f.write("## Corpus Composition\n\n")
    for journal, js in sorted(by_journal.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        f.write(f"- {journal}: {len(js)} articles\n")
    f.write("\n## Title Patterns\n\n")
    for k, v in patterns.most_common():
        f.write(f"- {k}: {v}\n")
    f.write("\nCommon title vocabulary (after stopword removal): ")
    f.write(", ".join(f"{w} ({c})" for w, c in title_tokens.most_common(35)))
    f.write("\n\nCommon title bigrams: ")
    f.write(", ".join(f"{a} {b} ({c})" for (a, b), c in title_bigrams.most_common(25)))
    f.write("\n\n## Observed Writing Moves\n\n")
    f.write("- Titles are usually compact nouns or noun phrases, often naming a process plus a mechanism, tension, or application domain.\n")
    f.write("- TIPS-style titles often use active conceptual framing: stress combinations, hormone mediation, future crops, root exudates, or regulatory networks.\n")
    f.write("- Annual Review titles are more taxonomic and durable: mechanism/process names, signaling modules, nutrient pathways, organ systems, or stress classes.\n")
    f.write("- Nature/Science/Cell reviews tend to foreground a broad problem or conceptual synthesis, then use the abstract to narrow to mechanisms or implications.\n")
    f.write("- Strong abstracts move from field problem to recent shift, then to a structured synthesis and a concrete unresolved bottleneck.\n")
    f.write("- Paragraphs rarely start with generic praise. They begin with a claim, boundary, or tension, then cite evidence near the claim.\n")
    f.write("- Forward-looking sections work best when they name tractable bottlenecks, testable hypotheses, or implementation barriers.\n")
    f.write("\n## Useful Lexical Habits\n\n")
    f.write("- Prefer precise process verbs: mediates, constrains, buffers, couples, rewires, partitions, coordinates, tunes, decouples, prioritizes, nominates.\n")
    f.write("- Use cautious evidence verbs: supports, is consistent with, suggests, points to, nominates, was associated with, remains unresolved.\n")
    f.write("- Use tradeoff language when biology has competing outputs: resilience versus growth, dormancy versus emergence, storage stability versus rapid repair.\n")
    f.write("- Avoid inflated review phrases unless the evidence supports them: comprehensive, unprecedented, groundbreaking, lays a foundation, great significance.\n")
    f.write("\n## Figure Design Habits\n\n")
    f.write("- High-level figures are usually mechanism maps, lifecycle continua, stress-response axes, or pipeline diagrams.\n")
    f.write("- Strong figures separate phases or compartments with pale background fields, use restrained color semantics, and keep labels short.\n")
    f.write("- Review figures work best when each panel has one cognitive job: timeline, mechanism, tradeoff, or translation pipeline.\n")
    f.write("- Avoid decorative stock-like scenes; use organism-accurate morphology and biology-specific icons.\n")
    f.write("\n## Copyright And Access Note\n\n")
    f.write("The corpus stores metadata, abstracts, DOI links, and open full-text entry points where available. Do not copy article prose. Use the corpus to infer structure, rhetoric, and design conventions; cite original papers for scientific claims.\n")
