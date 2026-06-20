---
name: plant-review-writer
description: Use when planning, drafting, revising, or quality-controlling plant-science review manuscripts, especially figure-rich reviews that need literature intake, evidence-ranked synthesis, citation integrity, journal-style structure, scientific figures, DOCX-ready outputs, or release-grade manuscript QC.
license: CC-BY-NC-4.0
---

# Plant Review Writer

## Purpose

This skill turns a plant-science review topic and evidence base into a formal review manuscript. It is built for high-level plant biology, crop science, breeding, cell biology, genetics, stress physiology, and plant biotechnology reviews that need synthesis rather than a list of papers.

Use genre conventions from strong review articles without copying source wording. The output should make a thesis, define evidence boundaries, place citations near claims, integrate figures with the text, and pass a recorded QC process before delivery.

## First Moves

1. State the review thesis in one sentence: the biological process, unresolved tension, and why the synthesis changes interpretation or practice.
2. Default to English unless the user requests another language.
3. Identify the target venue or style. If the user says Nature, Nature Plants, Cell, Trends in Plant Science, Annual Review, The Plant Cell, or another venue, load the closest formatting and structure rules from `references/`.
4. Before drafting a full review, run two learning gates:
   - Style gate: learn from at least 200 relevant high-level review records or approved review exemplars.
   - Topic gate: search and learn from at least 200 topic-relevant literature records before drafting.
5. Select a smaller core evidence set for close reading and citation. Prioritize high-quality mechanistic papers, classics, representative crop or species papers, and recent work from roughly the last five years.
6. State access limits. Do not claim full-text review of subscription-only papers unless the full text was actually available.
7. Build a section map and figure map together before writing the full manuscript.
8. Run five QC rounds before delivery for substantial manuscripts or major revisions.

## Required References

Load only the files needed for the task:

- `references/review_workflow.md`: full manuscript and revision workflow.
- `references/evidence_and_citation_integrity.md`: literature gates, evidence registry, citation placement, and access boundaries.
- `references/structure_and_style.md`: title, abstract, keywords, section rhythm, outlook, and outstanding questions.
- `references/figure_and_table_integration.md`: figure roles, section-derived prompts, captions, and display-item QC.
- `references/nature_reference_style.md`: Nature-family numeric reference expectations.
- `references/five_round_qc.md`: final manuscript audit before delivery.

## Manuscript Defaults

For a full plant-science review, unless the target venue or user specifies otherwise:

- Abstract: about 180-250 words.
- Keywords: 5-7 terms.
- Introduction or background: usually 800-1200 words for broad reviews.
- References: normally at least 30; use 35-60 for full figure-rich reviews when the topic warrants it.
- Figures: normally 4-6 main figures; each must answer a specific conceptual question.
- Outstanding Questions: 6-8 specific, answerable questions.
- Formal manuscript only: do not include workflow notes, claim-boundary labels, prompt traces, internal QC comments, or explanation of how the text was generated.

## Writing Rules

- Open sections with a claim, tension, or boundary problem rather than a generic topic sentence.
- Organize mechanism sections by causal gates, tissues, developmental phases, compartments, environmental filters, or threshold transitions.
- Keep direct evidence, comparative evidence, and speculation distinct.
- Place citations at the knowledge point they support.
- Avoid broad self-praise and formulaic claims such as "comprehensive," "of great significance," "lays a foundation," "fills a gap," and "provides a reference" unless the target text genuinely requires the wording.
- Use cautious evidence-ranked verbs: shows, demonstrates, supports, suggests, is consistent with, nominates, constrains, couples, tunes, buffers, rewires.
- End with named bottlenecks, testable models, decision frameworks, or specific validation designs.

## Figure Rules

Figures must be paired with the manuscript logic.

1. Draft or revise the section first.
2. Define the conceptual job of the figure.
3. Extract required labels, biological entities, causal arrows, and unsupported elements to avoid from the section and caption.
4. Generate or revise the figure only after the text logic is stable.
5. Cite the figure in the text and place the caption below the figure.
6. Inspect label spelling, line weight, morphology, color consistency, and caption-text agreement.

Do not make a figure only because it looks polished. If the figure does not show what the data or synthesis supports, replace it.

## Five-Round QC

Before delivering a substantial manuscript, record:

1. Literature and citation integrity: record counts, queries, access boundaries, core references, citation parity.
2. Structure and thesis: title, abstract, headings, figures, outlook, and questions point to the same thesis.
3. Language and evidence wording: formal manuscript style, no workflow notes, no unsupported certainty.
4. Figures and tables: every display item is cited, captioned, readable, and matched to text.
5. Final package and privacy: target formatting, DOCX or Markdown integrity, local paths removed, no credentials or private notes.

## Optional Scripts

Use the validation script when testing the packaged demo:

```bash
python scripts/validate_review_demo.py
```

For DOCX outputs in active projects, inspect the final document for embedded figure count, figure placement, captions, reference parity, and obvious layout errors before delivery.

