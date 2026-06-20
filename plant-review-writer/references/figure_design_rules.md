# Plant Review Figure Design Rules

Use these rules when planning or generating figures for plant-science reviews.

## Figure Roles

Choose the figure type by the cognitive job:

- Lifecycle continuum: connects developmental stages, environments, storage, field performance, or feedback loops.
- Mechanism map: links compartments, pathways, signals, damage, repair, or regulation.
- Tradeoff diagram: shows competing outputs such as growth versus defense, dormancy versus emergence, or yield versus resilience.
- Pipeline figure: connects phenotyping, omics, genetics, modelling, selection, and validation.
- Assay table or matrix: clarifies what each test measures and what it cannot measure.

Do not use a figure only as decoration.

## Section-Derived Image2 Workflow

Use this workflow for manuscript figures:

1. Plan the figure role early, but do not generate the final image from a generic topic idea.
2. First write or revise the manuscript section where the figure will be cited.
3. Extract the image prompt from that section and its caption:
   - conceptual question the figure answers,
   - core claims in the section,
   - required organs, tissues, cells, molecules, genes, taxa, treatments, or outputs,
   - causal arrows, sequence, gates, feedbacks, or contrasts,
   - exact short labels that may appear in the image,
   - elements to avoid because the section does not support them.
4. Convert those notes into an image2 prompt and directly generate a bitmap image.
5. Inspect the image against the section text and caption. If it drifts, regenerate with a more constrained prompt. Do not accept a figure only because it looks polished; verify that it represents the revised manuscript logic.

Do not use SVG, HTML canvas, Python drawing, or other vector stand-ins as an intermediate when the user requested image2/raster generation. Planning diagrams can be textual, but final figures must be generated directly as image files. Renaming or lightly re-captioning an old figure is not enough after the manuscript logic changes; either verify that the existing bitmap still matches the revised section or regenerate it directly from the revised section and caption.

Prompt template:

```text
Use case: infographic-diagram.
Asset type: scientific review figure for Section: <section heading>.
Source content: based on the written section, show <core section claim>.
Required visual structure: <panels/layout/sequence>.
Required biological elements: <organs/tissues/molecules/species>.
Required relationships: <arrows/causal gates/feedbacks/contrasts>.
Allowed labels only: <short labels>.
Caption will explain: <details not shown inside image>.
Style: simple scientific plant-review schematic, white or pale background, flat fills, black outlines, sparse labels, low-to-moderate saturation, minimal or no gradients, no highlights, no shadows, no 3D.
Avoid: unsupported pathways, generic decorations, manuscript title inside image, watermark, logo, SVG/vector look if the user asked for raster image2 output.
```

## Panel Logic

- Give each panel one job.
- Use short labels and avoid full-sentence labels inside the figure.
- Use captions for interpretation; use the figure for structure.
- Do not put manuscript-style titles inside figures unless the user or target journal explicitly asks for them. Put titles and detailed interpretation in captions.
- Avoid panel letters unless the target journal or user requests them. If panel letters are used, verify there are no stray letters from regenerated images.
- Keep mechanism maps readable by grouping signals into phases, compartments, or causal layers.
- Avoid auto-generated bottom legends, bullet lists, or explanatory sentences inside the image unless the figure design explicitly needs them. Captions should carry interpretation.

## Visual Language

Preferred review style:

- Adobe Illustrator-like flat vector rendering.
- Pale background fields to separate phases or domains.
- Muted accent palette: magenta, lavender, teal, sage green, wheat gold, slate blue, restrained orange.
- Thin black or dark slate outlines.
- Thin arrows, light borders, and dashed dividers where useful.
- Minimal shading; no heavy 3D or stock-photo effects.
- For users who request image2 or raster generation, generate bitmap figures directly with image2/image generation. Do not create SVG intermediate figures unless explicitly requested.
- For scientific review figures, prefer a simple, lightly rendered style: plain white or pale backgrounds, flat fills, black outlines, sparse labels, few or no gradients, no glossy highlights, no drop shadows, no 3D.

Avoid:

- decorative gradients, generic hero art, stock-like scenes, thick linework, cluttered icons, and unlabeled arrows.
- organism-incorrect icons, especially broadleaf seedlings when cereals are discussed.
- unrelated molecular symbols that imply evidence not discussed in the text.
- misspelled labels, microscopic text, unrequested panel letters, inconsistent line weights, and automatically generated legend keys that repeat information already in the caption.

## Plant Accuracy

Match morphology to the topic:

- Wheat and cereals: narrow leaves, fibrous roots, cereal grains, spikes or spikelets when mature organs are needed.
- Wheat seedling figures should show grass-like leaves, a pale tiller or coleoptile base when relevant, cereal grains, soil blocks only when seedbed context is needed, and fibrous or seminal roots. Broadleaf "sprout" icons are incorrect for wheat-centered figures.
- Arabidopsis: rosette, siliques, small seeds.
- Rice: narrow leaves, panicles, flooded or paddy context only when relevant.
- Maize: broad leaves and ears only when maize evidence is discussed.

If a figure generalizes across species, use abstract plant modules or clearly labelled species-specific icons.

## Mechanism Figure Depth

- A mechanism figure should synthesize a causal model, not only list genes.
- For crop physiology traits, consider organizing mechanism figures by tissue, organ, phase, threshold gate, or signal-to-phenotype transition.
- Where tissue specificity matters, include the relevant tissue context, such as embryo, aleurone, endosperm, seed coat/pericarp, glume, panicle, spike, root, leaf, or vascular tissue.
- For crop traits with environmental expression, include the relevant field or management filter when it is part of the mechanism: seedbed condition, salinity, drought, cold, heat, pathogen pressure, soil impedance, sowing depth, processing class, or target region.
- Use captions to explain gene names and evidence boundaries; keep in-figure text short enough to survive DOCX/PDF export.

## Text Integration

- Cite the figure in the section where its conceptual work is needed.
- Captions should state what the figure synthesizes, not claim the figure is original experimental evidence.
- Make figure terminology match section headings and table vocabulary.
- If the manuscript uses numbered references, do not put literature claims in figure captions unless those references are included and numbered consistently.
- For breeding and germplasm reviews, figures should carry material-level or mechanism-level work. Avoid purely macro-level pipelines when the text discusses named cultivars, translocations, genes, causal gates, or deployment decisions.

## Final Visual QC

Check:

- no stray panel letters,
- no unwanted in-figure titles when captions provide the title,
- line weights consistent across figures,
- organism morphology correct,
- labels fit inside shapes,
- labels are spelled correctly and do not introduce unsupported claims,
- any image2-added extra legends, checkmarks, or explanatory notes are necessary; otherwise regenerate or crop cleanly if the rest of the bitmap is correct,
- text is legible after DOCX/PDF export,
- figure colors are consistent with the manuscript set,
- image aspect ratios are preserved in DOCX and not stretched by fixed-width or fixed-height export scripts,
- generated bitmap images are copied into the workspace and embedded from stable paths,
- all figures are cited in the text and captioned in order.
