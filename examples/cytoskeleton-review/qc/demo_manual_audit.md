# Demo Manual Audit

Audit date: 2026-06-20

## Scope

Reviewed `examples/cytoskeleton-review/output/cytoskeleton_review_demo.md` for title, abstract, keywords, body length, theme map, figure placement, table placement, references, formatting, privacy, and manuscript cleanliness.

## Checks Passed

- Title is concise and topic-forward: 13 words.
- Abstract is in the expected range: 178 words.
- Keywords are present: 8 terms.
- Body length is within the 6,000-9,000 word target for 5-8 theme reviews: 6,610 counted words by repository validator.
- Theme map has 8 themes in the public QC file.
- Figures: 6 linked figures, all repository-relative.
- Captions: 6 captions, each placed below the figure.
- References: 58 numbered references counted after the References heading.
- References normalized to a Nature-family numbered style: surname-initial authors, `et al.` for long author lists, bold volume, page or article number, and year in parentheses.
- No absolute local paths in the demo output.
- No mojibake or replacement-character hits in the demo output.
- No workflow notes, claim-boundary labels, prompt traces, or internal QC notes in the formal manuscript.

## Fixes Applied

- Moved Table 1 from the end matter to the introduction, immediately after the evidence-boundary paragraph.
- Moved Table 2 from the end matter to the conceptual-definition section.
- Kept Table 3 near the special-division section where it is discussed.
- Changed table titles from `## Table` headings to bold table titles so tables are not misread as main sections.
- Updated the default full-review word range from "about 7,000 words" to 6,000-9,000 words.
- Updated the validator to reject `## Table` headings and enforce the 6,000-9,000 word range.
- Normalized the demo reference list from `year;volume:pages` formatting to a Nature-family numbered style.

## Remaining Release Notes

- If a target journal is selected later, rerun reference normalization against that journal's current author instructions.
- The demo topic is plant cell division because it is the current exemplar, but the skill itself is general scientific-review writing.
