# Plant Review Style Synthesis

Corpus: 250 source-balanced high-citation plant-related reviews from 2020-2026 in Cell, Nature, Science, Nature Biotechnology, Nature Plants, The Plant Cell, Annual Review of Plant Biology, and Trends in Plant Science. Source records are in `plant_review_corpus_2020_2026_source_balanced250.tsv`.

## Corpus Composition

- Trends in Plant Science: 111 articles
- Annual Review of Plant Biology: 50 articles
- Nature Plants: 30 articles
- The Plant Cell: 30 articles
- Science: 20 articles
- Cell: 5 articles
- Nature: 3 articles
- Nature Biotechnology: 1 articles

## Title Patterns

- colon title: 87
- forward-looking title: 19
- question title: 9
- from-to title: 8
- How-title: 7
- mechanism title: 5

Common title vocabulary (after stopword removal): crop (19), stress (17), signaling (15), development (14), interactions (13), immunity (11), crops (10), environmental (9), metabolism (9), challenges (9), agriculture (9), future (8), response (8), cell (8), molecular (8), climate (7), how (7), responses (7), breeding (7), soil (7), microbiome (7), growth (7), sustainable (7), role (7), photosynthesis (7), biology (7), root (6), regulatory (6), genome (6), through (6), acid (5), hormone (5), resistance (5), carbon (5), mycorrhizal (5)

Common title bigrams: climate change (4), salicylic acid (4), abiotic stress (4), soil carbon (4), stress responses (3), carbon sequestration (3), arbuscular mycorrhizal (3), sustainable agriculture (3), genome editing (3), tree mortality (3), environmental impacts (3), crop improvement (3), crop yield (3), molecular mechanisms (3), salt stress (2), stress resistance (2), root exudates (2), transcriptional regulatory (2), regulatory network (2), mycorrhizal fungi (2), calcium signaling (2), stress memory (2), growth development (2), microbiome interactions (2), crispr cas-mediated (2)

## Observed Writing Moves

- Titles are usually compact nouns or noun phrases, often naming a process plus a mechanism, tension, or application domain.
- TIPS-style titles often use active conceptual framing: stress combinations, hormone mediation, future crops, root exudates, or regulatory networks.
- Annual Review titles are more taxonomic and durable: mechanism/process names, signaling modules, nutrient pathways, organ systems, or stress classes.
- Nature/Science/Cell reviews tend to foreground a broad problem or conceptual synthesis, then use the abstract to narrow to mechanisms or implications.
- Strong abstracts move from field problem to recent shift, then to a structured synthesis and a concrete unresolved bottleneck.
- Paragraphs rarely start with generic praise. They begin with a claim, boundary, or tension, then cite evidence near the claim.
- Forward-looking sections work best when they name tractable bottlenecks, testable hypotheses, or implementation barriers.

## Useful Lexical Habits

- Prefer precise process verbs: mediates, constrains, buffers, couples, rewires, partitions, coordinates, tunes, decouples, prioritizes, nominates.
- Use cautious evidence verbs: supports, is consistent with, suggests, points to, nominates, was associated with, remains unresolved.
- Use tradeoff language when biology has competing outputs: resilience versus growth, dormancy versus emergence, storage stability versus rapid repair.
- Avoid inflated review phrases unless the evidence supports them: comprehensive, unprecedented, groundbreaking, lays a foundation, great significance.

## Figure Design Habits

- High-level figures are usually mechanism maps, lifecycle continua, stress-response axes, or pipeline diagrams.
- Strong figures separate phases or compartments with pale background fields, use restrained color semantics, and keep labels short.
- Review figures work best when each panel has one cognitive job: timeline, mechanism, tradeoff, or translation pipeline.
- Avoid decorative stock-like scenes; use organism-accurate morphology and biology-specific icons.

## Copyright And Access Note

The corpus stores metadata, abstracts, DOI links, and open full-text entry points where available. Do not copy article prose. Use the corpus to infer structure, rhetoric, and design conventions; cite original papers for scientific claims.
