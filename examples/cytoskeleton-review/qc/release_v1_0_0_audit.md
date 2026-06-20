# v1.0.0 Release Audit

Audit date: 2026-06-20

## Text And Language

- Read `output/cytoskeleton_review_demo.md` section by section.
- Removed process-language from the formal manuscript, including references to full-text intake as a drafting step.
- Removed or softened meta-review phrasing that sounded like writing-process commentary.
- Confirmed no remaining prompt traces, workflow notes, claim-boundary labels, reviewer-response phrasing, or intermediate-generation statements in the formal output.
- Confirmed title, abstract, keywords, section headings, figures, tables, outlook, outstanding questions, and references are present.

## Figures

- Manually inspected all six PNG figures.
- Confirmed white or near-white backgrounds, no obvious overlap, readable visual marks, and consistent manuscript style.
- Confirmed figures are manuscript-linked and captions appear below the image links.
- Confirmed image dimensions are suitable for demo display: five figures at 1672 x 941 pixels and one at 1536 x 1024 pixels.

## Tables

- Confirmed three tables are present in the manuscript body.
- Confirmed table titles use bold text rather than second-level headings.
- Confirmed table placements match the sections where they are discussed.
- Confirmed DOCX preview contains three tables.

## References And Citations

- Confirmed 58 numbered references after the References heading.
- Confirmed Nature-family reference normalization.
- Confirmed no `year;volume:pages` entries remain.
- Confirmed DOCX citation/reference parity audit passed.

## Validation Commands

```bash
python scientific-review-writer/scripts/validate_review_demo.py
python scientific-review-writer/scripts/audit_review_docx.py --docx dist/cytoskeleton_review_demo_v1_preview.docx --expect-figures 6 --expect-tables 3 --min-references 58
python <skill-creator>/scripts/quick_validate.py scientific-review-writer
python <skill-creator>/scripts/quick_validate.py <local-skill-root>/scientific-review-writer
python <skill-creator>/scripts/package_skill.py scientific-review-writer dist
```

## Release Decision

- Release package version: `v1.0.0`.
- Repository visibility: public after owner approval.
