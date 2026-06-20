# Citation And Manuscript QC Checklist

Use this checklist before delivering a plant review manuscript or DOCX.

## Evidence And Citations

- For full high-level reviews, confirm that a style-learning step from at least 200 relevant plant review records was completed and documented.
- Confirm that a topic-keyword literature-learning step from at least 200 topic-relevant records was completed before drafting and documented with query strings, search sources, inclusion logic, and record count.
- Confirm that the 200+ topic records were narrowed into a core evidence set containing high-citation/high-quality representative papers and recent papers from roughly the last five years.
- For substantial revisions, confirm that any newly identified conceptual weakness triggered a targeted literature refresh and a short evidence note with query themes, public sources, core added evidence, and access limits.
- Every scientific claim that depends on literature has a nearby citation.
- References are cited at the knowledge point, not pooled at paragraph ends.
- The reference list and in-text citations match one-to-one.
- Numbered citations appear in order of first appearance unless the target style requires otherwise.
- Direct species evidence is labelled clearly, for example "in wheat," "in rice," "in Arabidopsis," or "in cereals."
- Model-system evidence is not written as if it has been directly shown in the focal crop.
- If the title promises a broad crop/species scope, check that the abstract, headings, mechanism section, figures, and outlook do not collapse into a single-species review.
- DOI, title, year, and journal metadata are checked for core papers.
- Unverified or inaccessible subscription records are not described as fully searched.

## Manuscript Logic

- Title, abstract, section headings, figures, and conclusion point to the same thesis.
- The introduction distinguishes key terms that could otherwise be conflated.
- The manuscript has not reduced a broad trait, crop use case, or biological process to one convenient assay, species, organ, stage, or stress unless the title explicitly narrows the scope.
- Each major section has a visible role in the review arc.
- Transitions explain why the next section follows, rather than merely listing topics.
- Mechanism sections are organized by causal layers, phases, tissues, or thresholds rather than only as lists of genes or studies.
- Mechanism sections connect phenotype, organ or tissue context, causal process, and application boundary; associations are not overstated as causal mechanisms.
- A length plan exists and the final abstract, background, mechanism, crop/species, breeding/application, outlook, questions, figures, and references remain within the intended proportions.
- The outlook names concrete bottlenecks and answerable questions.
- The outlook is bold enough to state decision frameworks, ideotypes, predictive tools, or validation designs where supported, but each forward-looking claim remains testable.

## Language

- Remove inflated phrases: "comprehensive," "great significance," "lays a foundation," "fills a gap," and similar formulaic claims.
- Replace unsupported causality with evidence-calibrated wording.
- Remove reviewer-response phrasing.
- Avoid "more research is needed" unless followed by a specific research design, method, or uncertainty.

## Figures And Tables

- Every figure and table is cited in the text.
- Each generated figure is based on the corresponding written section and caption, not on a generic topic prompt.
- Each image2 prompt records the section claim, required biological elements, causal relationships, allowed labels, and unsupported elements to avoid.
- Captions are numbered and match the embedded display items.
- Figure vocabulary matches the manuscript sections.
- Figures do not contain stray panel letters, inconsistent line weights, or organism-incorrect icons.
- Figures do not contain unnecessary in-figure titles, auto-added legends, bullet lists, or explanatory sentences when captions provide titles and interpretation.
- Figure labels are spelled correctly, readable after Word/PDF export, and do not introduce unsupported claims.
- If image2/raster figures were requested, final figures are bitmap PNG/JPEG files generated directly with image generation, not SVG/vector stand-ins or SVG-derived exports.
- Tables state what each row/column measures, not only what it is called.

## DOCX Or Final File

- Confirm embedded image count and table count.
- Open or inspect the final document after generation.
- Use `scripts/audit_review_docx.py` for a repeatable DOCX audit when available.
- Check abstract length if the target journal has a limit.
- Check that reference numbering did not change after edits.
- Confirm figure files are stored in the workspace with stable paths and embedded into the DOCX.
- Confirm embedded figures preserve their aspect ratios and are not stretched by fixed export dimensions.
- Confirm that all required sections are present: title, abstract, keywords if needed, main text, conclusion/outlook, outstanding questions if requested, display items, and reference list.

## Three-Round Revision Audit

For major revisions or figure-rich final manuscripts, run and record at least three passes:

1. Citation and format: abstract length, citation/reference parity, first-appearance order, figure/table count, all image paths resolved.
2. Logic and language: title/abstract/heading/figure/outlook alignment, evidence wording, scope balance, mechanism depth, no placeholders or reviewer-response phrasing.
3. Figure and DOCX integrity: organism morphology, label spelling, line weight, stray panel letters, figure count, table count, media embedding, captions, references heading, and image aspect ratios.
