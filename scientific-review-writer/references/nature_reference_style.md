# Nature-Family Reference Style

Use the target journal's current author instructions when available. If the user requests Nature-family style and no more specific guide is provided, apply these defaults.

## In Text

- Use numbered citations.
- Number references in the order they first appear.
- Place citation numbers close to the supported claim.
- Do not pool unrelated citations at paragraph ends.

## Reference List

Journal article pattern:

```text
1. Author, A. B., Author, C. D. & Author, E. F. Article title. Journal Name volume, page-page (year).
```

Markdown manuscript pattern:

```text
1. Author, A. B. & Author, C. D. Article title. *Journal Name* **volume**, page-page (year).
```

Online-first or web-only article pattern when volume and pages/article number are unavailable:

```text
1. Author, A. B. Article title. *Journal Name* https://doi.org/xx.xxxx/xxxxx (year).
```

Book pattern:

```text
1. Author, A. B. Book Title (Publisher, year).
```

Chapter pattern:

```text
1. Author, A. B. Chapter title. In Book Title (eds Editor, C. D. & Editor, E. F.) page-page (Publisher, year).
```

## QC

- Number entries in first-citation order.
- List authors surname first with initials. For Nature-family style, include all authors up to five; for more than five authors, use the first author followed by `et al.` unless the target journal says otherwise.
- Check title spelling and preserve article-title capitalization as published.
- Italicize journal titles; use approved journal abbreviations when the target venue requires them.
- Bold volume numbers in Markdown when representing Nature-family style.
- Use `volume, page-page (year)` or `volume, article-number (year)` for standard articles.
- Use DOI or full URL before the year only for online-first, web-only, data, preprint, or other records without stable volume/page metadata, or when the target venue requests DOI display.
- Do not leave mixed styles such as `2019;70:239-267` in the final manuscript.
- Keep the final style consistent across all references.
