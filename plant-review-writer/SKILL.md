---
name: plant-review-writer
description: Use when writing, planning, revising, or polishing plant-science review articles, especially high-level reviews modeled on Trends in Plant Science, Annual Review of Plant Biology, Nature Plants, The Plant Cell, Cell, Nature, Science, or Nature Biotechnology. Trigger for plant review manuscripts, titles, abstracts, backgrounds, main-text style, citation placement, review logic, figure schemes, graphical abstracts, mechanism figures, DOCX/Word outputs, image2 raster figures, and manuscript QC.
license: CC-BY-NC-4.0
---

# Plant Review Writer

## Overview

This skill helps draft and revise plant-science review articles with evidence-ranked claims, high-level review structure, disciplined citation placement, and publication-grade figure planning. It is derived from the original local `plant-review-writer` skill and a 2020-2026 plant-review style synthesis across Trends in Plant Science, Annual Review of Plant Biology, Nature Plants, The Plant Cell, Cell, Nature, Science, and Nature Biotechnology. This public-ready export keeps general writing rules and scripts, but excludes private project briefs, raw full texts, and large redistributed corpus tables.

Use it to turn a topic and evidence base into a review-style manuscript, not to mimic source wording. Borrow genre conventions only: compact topic sentences, mechanism-to-application logic, clear caveats, restrained language, and figures that do conceptual work.

## First Moves

1. Define the review thesis in one sentence: the biological process, the unresolved tension, and why the synthesis changes how readers think or work.
2. Default to English for the manuscript unless the user explicitly requests another language.
3. Identify the target venue or style. If the user requests Nature-family formatting, load `references/nature_reference_style.md` before final reference cleanup.
4. Before drafting a full review, run and document two mandatory learning steps: a style-learning step from at least 200 relevant/high-level plant review records, and a topic-keyword literature-learning step from at least 200 topic-relevant literature records found by keyword searches. The topic set should include high-citation classics, high-quality mechanistic papers, representative crop/species papers, and recent papers from roughly the last five years.
5. For crop-breeding, germplasm, introgression, or cultivar-utilization reviews, build an evidence registry before drafting. Include peer-reviewed literature, classic non-English literature when relevant, official variety records, institutional variety pages, public reports, and material/cultivar/gene/segment-level evidence; state access limits.
6. Set the evidence hierarchy before drafting: direct species evidence first, closely related cereals/crops second, model-system evidence only where it clarifies a conserved mechanism.
7. Build a section map and length plan that moves from measurable phenotype to mechanism, perturbation, genetics or tools, breeding/application, and outlook.
8. Include 5-7 keywords below the abstract for full manuscripts unless the target venue forbids keywords.
9. Place citations at the knowledge point they support. Avoid paragraph-end citation pools.
10. Plan figure roles alongside the text, but generate each image only after the corresponding manuscript section is drafted or revised. Derive the image2 prompt from that section's claims, entities, causal relationships, labels, and caption. Final figures must be generated directly with image2/raster generation; do not use SVG, HTML canvas, Python drawing, or vector stand-ins as intermediates.
11. If the user expects a finished manuscript, generate a DOCX/Word file and inspect embedded figures, captions, references, and layout before delivery.
12. For major revisions, check whether the user's criticism exposes a scope error, such as reducing a broad trait to one assay or one evidence axis. Refresh the literature for that missing axis, revise the manuscript arc, and update tables, figures, outlook, and questions together.
13. Run quality control before delivery: citation parity, title/abstract alignment, evidence wording, figure-label consistency, crop/species balance, depth of mechanism, evidence-registry coverage, italics for biological names, removal of generic or reviewer-response phrasing, and removal of workflow narration. For substantial manuscript or figure revisions, run five QC rounds covering literature/citations, structure/thesis, language/evidence wording, figures/tables, and final package/privacy.

## Style Defaults

Prefer a Trends in Plant Science-like rhythm for concise manuscripts: active conceptual framing, short section openings, explicit bottlenecks, and "Outstanding Questions." Use Annual Review-style coverage when the topic needs durable background or a broader taxonomy of mechanisms.

Use cautious, evidence-ranked verbs:

- Direct evidence: shows, demonstrates, resolves, quantifies, maps.
- Strong but not definitive evidence: supports, is consistent with, suggests, points to, nominates.
- Integrative synthesis: couples, constrains, buffers, coordinates, tunes, partitions, rewires, decouples, prioritizes.

Avoid inflated or self-validating phrasing such as "comprehensive," "of great significance," "lays a foundation," "fills a gap," "provides a reference," or "this review aims to" unless there is a precise reason.

## Required References

Load only the reference files needed for the current task:

- `references/plant_review_style_synthesis.md`: corpus-derived patterns in titles, abstracts, paragraph logic, vocabulary, and figure habits.
- `references/review_output_standard.md`: accepted full-manuscript standard for structure, section lengths, paragraph rhythm, figure count/style, DOCX formatting, and final QC.
- `references/review_writing_rules.md`: practical drafting rules for high-level plant reviews.
- `references/figure_design_rules.md`: figure design language, panel logic, palette, and morphology checks.
- `references/citation_qc_checklist.md`: final manuscript checks for citations, references, claims, and display items.
- `references/workspace_review_lessons.md`: reusable lessons from local review projects, including scope discipline, mechanism depth, revision evidence updates, image2 figure QC, bold but testable outlooks, and multi-round final QC.
- `references/corpus_summary.md`: corpus counts, source balance, and link-status caveats.
- `references/nature_reference_style.md`: Nature-family numeric reference expectations.
- `references/five_round_qc.md`: five-pass release-grade manuscript audit.

This repository intentionally does not include private project briefs, raw full-text archives, or large redistributed corpus TSV files. Use user-provided files or regenerate public metadata locally when those resources are needed.

## Optional Scripts

Use scripts when the corpus needs to be refreshed or re-summarized:

```bash
python scripts/collect_plant_review_corpus.py --out-dir <output_dir>
python scripts/analyze_plant_review_style.py --corpus <corpus.tsv> --out <style_synthesis.md>
```

Use these scripts for repeatable full-manuscript delivery:

```bash
node scripts/build_review_docx.js --md <manuscript.md> --out <manuscript.docx>
python scripts/audit_review_docx.py --docx <manuscript.docx> --expect-figures <n> --min-references <n>
```

The collector uses OpenAlex and public metadata/open-access links. Do not claim that paywalled databases or subscription-only full texts were fully searched unless the user provides exports or access.

## Manuscript Workflow

For a new plant review:

1. Learn review style from at least 200 plant review records where the task asks for a full high-level review; summarize the learned title, abstract, paragraph, vocabulary, figure, and logic habits.
2. Search topic keywords and learn from at least 200 topic-relevant literature records before drafting. Use NCBI/PubMed, DOI/publisher pages, Google Scholar-like keyword searches, and available full text/metadata. Record query strings, source databases, inclusion logic, and access limits. Do not claim subscription-only full-text coverage unless actually available.
3. For topics with important Chinese, Japanese, Russian, Spanish, or other non-English literature or official crop-variety records, search those evidence streams explicitly and include them in the registry when they change the synthesis.
4. From the 200+ topic records, identify a smaller core evidence set for citation and close reading: high-citation classics, high-quality mechanistic papers, representative crop/species papers, cultivar/material deployment records, and recent papers from roughly the last five years.
5. Separate direct evidence from comparative evidence in the notes and in the wording of the manuscript.
6. Draft title options before the abstract. Strong review titles often name a process plus a mechanism, tension, or translational frame. Do not turn user instructions such as "use historical order" or "compare mechanisms" into section headings; headings must be condensed from the content.
7. Plan component lengths before drafting: abstract, introduction, main mechanism sections, crop/species sections, breeding/application, outlook, questions, figures, tables, and references.
8. Write the abstract as: field problem, recent conceptual shift, synthesis scope, key mechanism or tool axis, and concrete bottleneck.
9. Open each section with a claim or tension, then move through evidence, mechanism, limits, and implication. Historical order can guide the order of evidence inside a section, but should not appear as meta-heading language unless the section is genuinely about history.
10. Add figures where the reader needs a conceptual map, not where the text merely needs decoration. For each figure, first write or revise the related section, then extract a section-derived image2 prompt and directly generate a bitmap figure.
11. End with named bottlenecks, synthesis, and actionable questions rather than a generic call for more research.
12. For figure-rich manuscripts, follow `references/review_output_standard.md`. If private project-specific standards are available in the user's local workspace, use them only for that private task and do not copy them into public release artifacts.

For revising an existing review:

1. Check whether the title, abstract, section headings, and figures carry the same thesis.
2. Replace vague claims with evidence-ranked wording.
3. Move citations from paragraph ends to the exact claims they support.
4. Remove response-to-reviewer phrases and broad claims that are not anchored to references.
5. Check whether the manuscript accidentally narrows the topic to one model or crop when the title promises a broader crop/species synthesis.
6. Check whether the manuscript accidentally narrows a broad trait to one assay, stress, stage, or readout. If so, add the missing expression contexts and mechanisms in the main arc, not only in a late caveat.
7. Deepen mechanism sections by organizing evidence into phases, tissues, organs, causal layers, environmental filters, or threshold gates instead of listing genes or papers.
8. Reconsider whether table columns are doing synthesis work. Avoid decorative "unresolved question" columns; when useful, convert them to decision columns such as evidence class, deployment status, conversion bottleneck, or validation threshold.
9. Verify italics for species names, named materials/cultivars when required by the project, and gene/locus names. Preserve chromosome arms, cytogenetic stocks, and structural labels in roman type unless the target journal specifies otherwise.
10. Verify every figure against the text, captions, organism morphology, and visual style requirements. If the image does not match the written section, revise the prompt and regenerate the bitmap image directly with image2 rather than patching it with SVG or vector edits. Inspect for stray panel letters, thick line weights, misspelled labels, extra legends, and crop-inaccurate morphology.

## Output Expectations

Deliver a formal manuscript or revision note that includes, as appropriate, title, abstract, 5-7 keywords, main text, conclusion or outlook, outstanding questions, figure/table proposals, and a numbered reference list. For full review-manuscript tasks, prefer producing both Markdown and DOCX/Word outputs, with generated figure files stored in the workspace. When working on a DOCX, update the document and then inspect the final file for embedded image count, figure placement, caption numbering, reference parity, and obvious layout errors. The final manuscript must not contain claim-boundary labels, prompt traces, workflow notes, or intermediate generation explanations.
