---
name: scientific-review-writer
description: Use when planning, drafting, revising, polishing, or quality-controlling scientific review articles across disciplines. Triggers include literature review, review manuscript, narrative review, mechanistic review, scholarly review, citation audit, figure-rich review, DOCX-ready review, Nature-style references, multi-round QC, and publication-ready review writing.
license: CC-BY-NC-4.0
---

# Scientific Review Writer

## Purpose

This skill helps produce high-level scientific review manuscripts across disciplines. It is a generalized successor to the original local review-writing skill: the plant-specific rules have been removed, while the strongest workflow elements remain.

The default output language is English. Use another language only when the user explicitly requests it.

## Operating Principles

1. Human-in-the-loop, not full automation: ask for approval when scope, outline, evidence boundary, target journal, or final release status materially affects the manuscript.
2. Evidence first: never draft a full review before the keyword search, literature intake, and available full-text learning gates are complete or the user provides a verified source set.
3. Claim-evidence parity: every substantive literature-dependent claim needs a nearby citation or must be softened.
4. Figures follow content: write or revise the relevant section before generating or accepting figures.
5. Final manuscripts are formal outputs: remove workflow notes, prompt traces, claim-boundary labels, internal QC comments, and generation explanations.

## First Moves

1. Define the review thesis in one sentence: field, unresolved tension, synthesis angle, and why it matters.
2. Record the target discipline, target journal or style, output format, expected word count, figure count, reference style, and whether the user wants a full review or a revision.
3. Default to the cytoskeleton-case full-review standard when the user asks for a finished, figure-rich review and gives no stricter target:
   - English manuscript.
   - Abstract about 180-220 words.
   - 6-8 keywords.
   - Body about 7,000 words before references.
   - 6 main figures.
   - At least 58 references.
   - 8 outstanding questions for future work when appropriate.
4. Draft 3-6 concise title candidates before the outline. Titles should foreground the core topic and synthesis angle, usually 8-16 words, without broad filler such as "comprehensive review" unless the target venue requires it.
5. Run two intake gates before drafting a full review:
   - Style gate: learn from at least 200 relevant high-level review records or user-approved exemplar reviews.
   - Topic gate: search topic keywords and ingest at least 200 topic-relevant records. For deep reviews, learning from available full texts is mandatory where lawful and accessible; record full-text IDs, counts, and access limits. Do not begin main drafting until this log exists or the user explicitly provides a verified corpus.
6. Select a smaller core evidence set for close reading and citation. Prioritize classics, high-quality mechanistic studies, representative methods or systems, recent work, and field-defining controversies.
7. Distill 5-8 synthesis themes before drafting. The first themes should provide broad, detailed coverage of the field; later themes should analyze core features, characteristics, distinctive strengths, bottlenecks, exceptions, or viewpoint-level insights.
8. Build and confirm an outline before drafting: section roles, word allocation, theme mapping, figure roles, table roles, and expected reference density.
9. Run five QC rounds before delivery for substantial manuscripts.

## Required References

Load only what the task needs:

- `references/review_workflow.md`: phase-by-phase review pipeline and checkpoints.
- `references/review_output_standard.md`: default full-review length, structure, figures, and formal output rules.
- `references/cytoskeleton_case_standard.md`: latest cytoskeleton-review case standard used for default scale.
- `references/evidence_and_citation_integrity.md`: literature gates, access boundaries, claim-evidence mapping, citation audit.
- `references/structure_and_style.md`: abstract, keywords, section rhythm, outlook, and final prose style.
- `references/style_calibration_and_quality.md`: user-voice calibration and writing quality checks.
- `references/theme_distillation.md`: title compression, keyword/full-text gate, and 5-8 theme synthesis rules.
- `references/figure_and_table_integration.md`: section-derived figure workflow and display-item QC.
- `references/nature_reference_style.md`: Nature-family numeric reference expectations.
- `references/five_round_qc.md`: final release-grade manuscript audit.

## Workflow

For a new full review:

1. Intake: discipline, thesis, journal style, output format, source availability, constraints, and expected depth.
2. Research: build keyword strategy, source corpus, available full-text learning log, evidence hierarchy, and access-boundary note.
3. Theme distillation: condense the evidence into 5-8 synthesis themes and a concise title set.
4. Architecture: produce outline, word allocation, theme-to-section map, figure plan, tables, and claim map; confirm before drafting when the project is large.
5. Argumentation: convert the evidence map into section-level claims, caveats, unresolved questions, and synthesis transitions.
6. Drafting: write section by section in English by default; keep citations close to claims.
7. Figures and tables: generate, revise, or accept display items only when they match the written section and data.
8. Citation and reference audit: normalize reference style and verify citation/reference parity.
9. Review and revision: run internal review, fix critical issues, then rerun QC.
10. Finalization: export Markdown and, when requested or feasible, DOCX/PDF with embedded figures.

For revising an existing review:

1. Diagnose the weakness: scope, evidence, argument, citation, figure, language, formatting, or target-journal mismatch.
2. Refresh literature when the weakness exposes a missing axis.
3. Revise the manuscript arc, not only isolated sentences.
4. Update figures, tables, captions, references, and outlook when the thesis changes.
5. Run the five-round QC again.

## Output Expectations

Deliver a formal review manuscript or revision package with, as appropriate:

- title,
- abstract,
- keywords,
- main text,
- figures and captions,
- tables where they do synthesis work,
- outlook or conclusion,
- outstanding questions,
- references,
- QC note for the user when the task includes final delivery.

The manuscript itself must not contain internal QC notes or generation-process explanations.

## Optional Scripts

Use scripts when they improve repeatability:

```bash
node scripts/build_review_docx.js --md <manuscript.md> --out <manuscript.docx>
python scripts/audit_review_docx.py --docx <manuscript.docx> --expect-figures <n> --min-references <n>
python scripts/validate_review_demo.py
```

When a script fails because of missing runtime dependencies, report that directly and continue with the best available validation.
