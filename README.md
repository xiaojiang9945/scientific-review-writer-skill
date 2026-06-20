# Plant Review Writer Skill

Private iteration repository for the `plant-review-writer` Codex skill.

This skill helps draft, revise, and quality-control figure-rich plant-science review manuscripts. It is designed for review articles that need a real literature intake step, evidence-ranked synthesis, citation integrity, publication-style figures, and multi-round manuscript QC.

## Current Status

- Repository state: private iteration.
- Public release version: not assigned.
- Target public release tag: `v1.0.0`, only after manual approval.
- License intent: non-commercial use with attribution, within lawful and ethical research use.

## What The Skill Enforces

- Style learning from at least 200 relevant high-level review records before full manuscript drafting.
- Topic literature learning from at least 200 topic-relevant records before full manuscript drafting.
- A smaller core evidence set chosen from the 200+ topic records for close reading and citation.
- Nearby citation placement at the supported knowledge point.
- Figure planning from the written section, not decorative topic art.
- Five QC rounds covering literature/citations, structure, language, figures/tables, and final privacy/export checks.
- Formal manuscripts that exclude workflow notes, claim-boundary labels, and intermediate generation explanations.

## Demo

The demo uses the plant kinetochore review from the local `Seed_Vigor_Review` project:

- Source draft: `examples/plant-kinetochore-review/input/source_review_en_strict.md`
- Demo output: `examples/plant-kinetochore-review/output/plant_kinetochore_review_demo.md`
- Figures: `examples/plant-kinetochore-review/output/figures/`
- Demo QC: `examples/plant-kinetochore-review/qc/demo_qc_public.md`

The demo intentionally does not include raw downloaded full texts, local workspace paths, private credentials, or large literature metadata exports.

## Local Validation

Run from the repository root:

```bash
python plant-review-writer/scripts/validate_review_demo.py
python <skill-creator>/scripts/quick_validate.py plant-review-writer
```

Package locally for Codex testing:

```bash
python <skill-creator>/scripts/package_skill.py plant-review-writer dist
```

## Install For Local Testing

Copy the `plant-review-writer/` directory into your Codex skills directory, then start a new Codex session and ask for a plant-science review manuscript or revision.

## Public Release Checklist

Before changing this repository to public:

- Confirm the demo manuscript and generated figures may be shared.
- Confirm references are normalized to the chosen target style.
- Confirm no local paths, account names, credentials, or private project notes remain.
- Run the validation script and the skill quick validator.
- Create a clean `v1.0.0` tag only after approval.
