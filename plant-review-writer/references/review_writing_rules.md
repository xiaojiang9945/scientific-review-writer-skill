# Plant Review Writing Rules

Use these rules when drafting or revising a plant-science review manuscript.

## Title

- Prefer compact titles that name the biological process and the conceptual frame.
- Effective patterns include: process plus mechanism, process plus tradeoff, organism plus transition, or "from X to Y" when the review genuinely spans scales.
- Avoid titles that only promise coverage, such as "A review of..." or "Research progress on...".
- Use question titles sparingly; they work only when the manuscript answers the question with a structured synthesis.

## Abstract

Build the abstract in four or five moves:

1. State the field problem without exaggeration.
2. Name the recent conceptual or technical shift.
3. Define the scope and evidence hierarchy.
4. Synthesize the main mechanism, tradeoff, or pipeline.
5. End with a concrete bottleneck or decision point.

Keep abstracts dense but readable. Prefer "Here we synthesize..." only when needed; often a direct declarative sentence is stronger.

For full manuscript tasks, set an abstract target before drafting, commonly 180-230 words unless a journal limit is supplied. Check the final abstract length after revisions.

## Introduction And Background

- Start from a biological or agronomic tension, not from generic importance.
- Define terms where confusion affects interpretation, especially for composite traits, stress categories, developmental stages, and assay readouts.
- Move quickly from context to the review thesis.
- Use background to set up decisions the reader must make later: what counts as evidence, what scales are linked, and where current methods fail.
- For crop and trait reviews, state expression contexts early. A trait such as vigor, tolerance, quality, dormancy, or utilization should not be reduced to one laboratory assay, one stress, one organ, or one molecular readout unless the title explicitly says so.

## Pre-draft Evidence Work

- For a full high-level review, learn style from at least 200 relevant plant review records before drafting. Use this only for structure, vocabulary, logic, and figure habits; do not mimic source prose.
- Then run a topic-keyword literature-learning step before drafting. Search topic keywords and learn from at least 200 topic-relevant literature records. Include high-citation classics, high-quality mechanistic papers, representative crop/species studies, and recent progress from roughly the last five years.
- Use NCBI/PubMed, DOI or publisher pages, Google Scholar-like keyword searches, and available full-text or metadata sources. Record access limits clearly.
- Record query strings, databases or search sources, inclusion logic, and the number of records learned. If fewer than 200 topic-relevant records can be found, broaden synonyms, organisms, mechanisms, and date windows before drafting; if the topic genuinely has fewer than 200 records, document that limitation explicitly.
- Create an evidence table before drafting. Separate direct species/crop evidence, closely related comparative evidence, model-system evidence, and application or management evidence. Distinguish the 200+ learned topic corpus from the smaller core set that will actually be cited.
- For crop-breeding, germplasm, introgression, cultivar, or pre-breeding reviews, create a material-level evidence registry before drafting. Include cultivars, founder parents, lines, populations, chromosome segments, genes/loci, official variety records, institutional pages, public reports, classic non-English literature, and peer-reviewed mechanistic evidence when relevant. Do not let English-only database results erase important Chinese or other non-English crop-breeding achievements.
- Build a length plan before drafting so the abstract, background, mechanism, crop/species, breeding/application, outlook, figures, and references have visible proportions.
- During substantial revision, run a targeted literature-refresh step for any missing conceptual axis identified by the user. Record query themes, public sources used, core added evidence, and access limits. Use the refresh to revise the manuscript arc, tables, figures, and outlook, not only to add a paragraph.

## Main Text

- Open sections with a claim, boundary, or tension.
- Put citations close to the claim they support.
- Distinguish observation from mechanism and mechanism from application.
- Use direct evidence first. Comparative evidence should be labelled by organism or system.
- Where evidence conflicts, state the reason if known: genotype, developmental stage, assay, tissue, environment, or statistical design.
- Prefer short synthesis paragraphs over long lists of studies.
- When the title promises a crop-wide or species-wide review, audit the text for one-species drift. A dominant evidence crop can be frequent, but the review's thesis, abstract, headings, figures, and conclusions must preserve the stated scope.
- Mechanism sections should not be shallow gene catalogues. Organize mechanisms by phase, tissue, compartment, signal layer, causal gate, or threshold transition, then place genes and papers within that framework.
- For crop physiology and breeding mechanisms, connect the evidence to the organ, tissue, or management context that expresses the trait: roots, coleoptiles, leaves, spikes, endosperm, seed coat, vascular tissues, canopy temperature, seedbed condition, pathogen spectrum, processing class, or regional deployment.
- Separate phenotype, mechanism, and application. A measured association should not be written as a causal mechanism; a causal mechanism should not be written as breeding value until target-environment or product validation is discussed.
- Include interpretation and outlook in proportion: summarize the current state, but also name bottlenecks, testable models, and practical consequences without turning the review into speculation.
- Use historical order as a paragraph-ordering tool when it clarifies achievements or breeding routes, but do not turn user instructions such as "write by historical order" into headings. Headings should be content-derived and compact.
- Table columns should synthesize decisions. Avoid decorative "question" columns unless the review genuinely uses them as outstanding questions; for breeding/application tables, prefer decision columns such as evidence class, deployment status, conversion bottleneck, validation threshold, or failure mode.
- Check italics before delivery: species and genera, gene/locus names, and project-specified material/cultivar names should be italicized; chromosome arms and cytogenetic labels normally remain roman unless target style requires otherwise.

## Wording

Use precise integrative verbs:

- coordinates, couples, constrains, buffers, tunes, partitions, rewires, decouples, prioritizes, nominates, resolves.

Use evidence-calibrated verbs:

- demonstrates: direct and strong evidence.
- supports or is consistent with: convergent but not definitive evidence.
- suggests or points to: plausible inference.
- was associated with or mapped near: statistical or positional evidence.
- remains unresolved: genuine gap, not a decorative phrase.

Avoid:

- "comprehensive," "great significance," "lays a foundation," "fills a gap," "provides a theoretical basis," "worthy of further study," and broad unsupported causal claims.
- Reviewer-response phrasing such as "according to the reviewer's suggestion" or "we have added a section."
- Paragraphs that end with a block of citations detached from specific claims.

## Outlook

End with named bottlenecks rather than generic calls. A good outlook names:

- a measurement bottleneck,
- a mechanistic bottleneck,
- a translation or breeding/engineering bottleneck,
- and one or more testable questions.

For Trends-style manuscripts, add "Outstanding Questions" with concise, answerable questions. For Annual Review-style manuscripts, pair broader coverage with explicit unresolved axes.

Make outlooks bold only when they remain testable. Strong patterns include environment-specific ideotypes, predictive passports, validation networks, deployment filters, and decision frameworks. Each should map to an assay, dataset, field validation design, breeding decision, or management context.

Outstanding Questions should be answerable enough to imply an experiment, dataset, or selection pipeline. Avoid broad questions that only restate the topic.

## Final File Expectations

- For full manuscript deliverables, write the article in English unless instructed otherwise.
- Produce a Word/DOCX file when the user asks for a finished review manuscript, especially if figures are included.
- Follow `review_output_standard.md` for the accepted full-review form: 4-5 conceptual figures, roughly 35-45 references, section-level length balance, and a DOCX with embedded figures.
- Use `scripts/build_review_docx.js` when a Markdown manuscript with local image links needs to be converted into a consistent Word document.
- Maintain a short QC or methods note documenting the review-style learning step, topic-specific searches, length plan, figure plan, and final checks.
- For major revisions, record at least three QC rounds: citation/format, logic/language, and figure/DOCX integrity.
