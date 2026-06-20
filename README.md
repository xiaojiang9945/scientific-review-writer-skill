# Scientific Review Writer Skill

Private iteration repository for the `scientific-review-writer` Codex skill.

This repository is the generalized successor to the original local review-writing skill. It is no longer limited to plant science. The skill now targets scientific review manuscripts across disciplines, with English as the default output language.

## Current Status

- Repository state: private iteration.
- Public release version: not assigned.
- Target public release tag: `v1.0.0`, only after manual approval.
- License intent: non-commercial use with attribution, within lawful and ethical research use.

## What Changed

- Generalized from plant-specific review writing to scientific review writing.
- Default output language is English.
- Full-review default scale now follows the latest cytoskeleton/cell-division review case: 6,000-9,000 body words, 6 figures, at least 58 references, and 5 QC rounds.
- Added concise title rules and a hard keyword/full-text learning gate before drafting.
- Added a 5-8 theme distillation gate before the outline.
- Added staged pipeline design, checkpoint gates, claim-evidence integrity, optional style calibration, writing quality checks, and figure verification.
- Added Codex-oriented validation and repository safeguards.

## External Lessons Adapted

The skill borrows workflow ideas, not text, from:

- `Imbad0202/academic-research-skills`: staged research-to-write pipeline, integrity gates, style calibration, writing quality checks, and figure verification.
- OpenAI Codex Best Practices: reusable skills, practical `AGENTS.md`, scoped workflows, validation, and review-before-accept loops.

See `scientific-review-writer/references/codex_and_ars_lessons.md`.

## Demo

The demo uses the latest cell-division/cytoskeleton review standard:

- Source draft: `examples/cytoskeleton-review/input/source_review_en_final.md`
- Demo output: `examples/cytoskeleton-review/output/cytoskeleton_review_demo.md`
- Figures: `examples/cytoskeleton-review/output/figures/`
- Demo QC: `examples/cytoskeleton-review/qc/demo_qc_public.md`

The demo intentionally excludes raw downloaded full texts, large literature metadata exports, local absolute paths, private credentials, and private workspace notes not needed to evaluate the skill.

## Local Validation

Run from the repository root:

```bash
python scientific-review-writer/scripts/validate_review_demo.py
python <skill-creator>/scripts/quick_validate.py scientific-review-writer
```

Package locally for Codex testing:

```bash
python <skill-creator>/scripts/package_skill.py scientific-review-writer dist
```

## Public Release Checklist

Before changing this repository to public:

- Confirm the demo manuscript and generated figures may be shared.
- Confirm references are normalized to the chosen target style.
- Confirm no local paths, account names, credentials, raw full texts, or private project notes remain.
- Run the validation script and the skill quick validator.
- Create a clean `v1.0.0` tag only after approval.
