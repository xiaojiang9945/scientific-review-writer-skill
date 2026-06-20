# Exemplar Review Output Standard

Use this standard when the user asks for a full, figure-rich plant-science review manuscript. It records the reusable quality, structure, writing rhythm, figure system, and DOCX form extracted from the accepted Word exemplar on crop pre-harvest sprouting. Do not copy topic-specific content; reproduce the form, depth, and quality control.

## Exemplar DOCX Record

Observed from the final Word manuscript:

| Feature | Standard to reproduce |
|---|---:|
| Text paragraphs | about 118 |
| Embedded image paragraphs | 5 |
| Figure captions | 5 |
| Embedded media | 5 PNG figures |
| References | about 35-45 core references |
| Citation markers | about 50-60 in-text citation markers |
| Paragraphs with citations | about 20-30 |
| Image display size in DOCX | about 6.5 x 3.7 inches each |
| Main font | Arial |
| Normal text | about 11 pt |
| Reference text | smaller, about 9 pt, hanging indent |
| Title | centered, bold, dark teal |
| Section headings | bold, dark teal |
| Page margins | about 1 inch |
| Footer | centered page number |

## Manuscript Shape

Use this order unless the topic clearly requires a different structure:

1. Title.
2. Abstract.
3. Keywords.
4. Introduction/background with term boundaries and the thesis.
5. Environmental, developmental, phenotypic, or measurement architecture.
6. Deep mechanism section organized by tissues, phases, compartments, thresholds, or causal layers.
7. Crop/species/system-specific genetic or mechanistic solutions.
8. Breeding, engineering, management, or translational pipeline.
9. Outlook with named bottlenecks.
10. Outstanding Questions.
11. References.

For cultivar, germplasm, introgression, or breeding-utilization reviews, add a material-level evidence map before drafting and consider a table that links materials or modules to donor route, breeding value, and conversion/deployment bottleneck.

Default length targets:

| Component | Target length |
|---|---:|
| Abstract | 180-230 words |
| Introduction/background | 700-900 words |
| Phenotype/environment/measurement architecture | 750-900 words |
| Mechanism section | 1100-1300 words |
| Crop/species/system-specific section | 800-950 words |
| Breeding/application/translation | 750-900 words |
| Outlook | 450-650 words |
| Outstanding Questions | 6-8 questions |
| Figures | 4-5 main figures |
| References | 35-45 core references |

The accepted exemplar used about 5400-5500 body words and 42 references. It felt substantial because the mechanism section was the longest section and because each figure had a conceptual role.

For revision tasks, preserve this shape but audit whether the user's criticism reveals a missing axis. If so, update the manuscript structure, tables, figures, and outlook together. Examples include adding field stress-emergence to a seed-vigor review, adding product-quality validation to a breeding review, or adding tissue/organ mechanisms to a molecular review.

## Writing Rhythm

Write in English unless the user explicitly requests another language.

Paragraph pattern:

- Open sections with a claim or tension, not a generic topic sentence.
- Define terms when confusion changes interpretation.
- Move from measurable phenotype to mechanism, then to crop/species differences, then to decisions.
- Use synthesis paragraphs that explain what evidence means, rather than strings of paper summaries.
- Put citations next to the specific claim they support.
- Use cautious evidence-ranked wording: direct crop evidence "shows" or "demonstrates"; comparative evidence "supports", "is consistent with", or "nominates".
- Avoid broad promises such as "comprehensive", "of great significance", "lays a foundation", "fills a gap", and "provides a reference".

Mechanism depth:

- Do not write a shallow gene catalogue.
- Organize mechanism by causal gates, tissues, phases, signal layers, or threshold transitions.
- Connect gene names to biological function, tissue context, field phenotype, and application limits.
- When the trait is expressed through an organ or management context, make that organ or context visible in the mechanism section and at least one figure.
- Include what remains unresolved and why it matters for measurement or breeding.

Scope control:

- If the title promises a broad crop/species/system review, audit the manuscript for drift toward one dominant model.
- A well-studied organism can be frequent, but the abstract, headings, figures, and outlook must preserve the stated scope.

## Figure System

A full review should normally include 4-5 figures. Complex breeding, germplasm, or multi-route crop-improvement reviews may need 6-8 figures if each figure answers a distinct conceptual question and is generated directly from the relevant section and caption. Each figure must answer one conceptual question.

Reusable figure roles:

1. Boundary figure: separates the target concept from related concepts and defines the problem.
2. Cascade or architecture figure: links environment/development/phenotype to mechanism and outcome.
3. Tissue-resolved or process-resolved mechanism figure: shows where causal gates occur.
4. Molecular or regulatory module figure: synthesizes signals, genes, and pathways without overclaiming.
5. Pipeline figure: connects phenotyping, omics, genetics, modelling, validation, and field decisions.

Figure rules:

- Plan figure roles alongside the text, but generate final images only after the corresponding manuscript section has been written.
- Derive each image2 prompt from the written section and caption. The prompt must encode the section's core claim, biological elements, causal relationships, allowed labels, and unsupported elements to avoid.
- Use captions for titles and interpretation; do not put large manuscript-style titles inside images.
- Keep in-image labels short and readable.
- Use image2/raster generation directly when the user requests image2 or bitmap figures. Do not create SVG, HTML canvas, Python-drawn, or other vector stand-ins unless explicitly requested.
- Copy generated image files into the workspace and embed from stable paths.

Preferred figure style:

- Plain white or very pale background.
- Flat fills with restrained pastel colors.
- Black or dark gray outlines.
- Thin arrows and light borders.
- Minimal or no gradients.
- No glossy highlights, no drop shadows, no 3D rendering.
- Scientific schematic feel, similar to clean plant-review figures.

## DOCX Output Standard

For a finished manuscript, produce both Markdown and DOCX/Word outputs when feasible.

DOCX build expectations:

- Title centered, bold, dark teal.
- Heading 1 in dark teal, bold.
- Normal text in Arial, about 11 pt.
- Captions slightly smaller than body text.
- References smaller, with hanging indent.
- Images centered, displayed at about 630 x 354 px or 6.5 x 3.7 inches in Word.
- Use page numbers in the footer.
- Embed images, do not merely link to external paths.
- Preserve source-image aspect ratios when embedding figures. Avoid fixed-height export logic that stretches wide or tall generated figures.

The bundled `scripts/build_review_docx.js` can build a Word file from Markdown with local image links using this style.

## Required QC Before Delivery

Run and record:

- style-learning source count: at least 200 relevant plant review records for full reviews,
- topic-keyword literature-learning source count: at least 200 topic-relevant literature records before drafting,
- topic-specific literature-search summary with query strings, search sources, inclusion logic, access boundaries, and the smaller core evidence set selected for citation,
- length plan versus actual section word counts,
- figure plan and final figure count,
- image file existence and embedded image count in DOCX,
- image aspect-ratio preservation in DOCX,
- citation/reference parity,
- numbered citation order,
- broad-scope balance check if the title is crop/species/system-wide,
- mechanism-depth check,
- abstract length,
- residual banned phrase check,
- final file paths.

If any check fails, revise before delivery.

For substantial manuscript updates, split QC into three recorded passes: citation/format, logic/language, and figure/DOCX integrity.
