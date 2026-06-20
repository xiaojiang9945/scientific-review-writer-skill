# Release Checklist

Use this checklist before any public release.

## Versioning

- [ ] Repository is still private during iteration.
- [ ] Public release approval is recorded by the owner.
- [ ] First public release is tagged `v1.0.0`.
- [ ] Private iteration commits are not described as public releases.

## Skill Validation

- [ ] `python scientific-review-writer/scripts/validate_review_demo.py`
- [ ] `python <skill-creator>/scripts/quick_validate.py scientific-review-writer`
- [ ] Local package builds successfully.
- [ ] Skill can be installed and triggered in a fresh Codex session.

## Demo

- [ ] Demo source, output, figures, and QC file are present.
- [ ] Demo manuscript is English by default.
- [ ] Demo manuscript has abstract, keywords, figure citations, captions, and at least 58 references.
- [ ] Demo has 6 figures and about 7,000 body words.
- [ ] Demo references are normalized to the chosen target style.
- [ ] Demo figures are manuscript-linked, not decorative.
- [ ] Demo does not include raw full-text archives or large literature exports.

## Privacy

- [ ] No local absolute paths.
- [ ] No account names.
- [ ] No tokens, API keys, passwords, cookies, SSH keys, or `.env` files.
- [ ] No private project notes outside the approved demo.

## Manuscript Quality

- [ ] No claim-boundary labels or intermediate-generation notes in the manuscript.
- [ ] No reviewer-response phrasing in the manuscript.
- [ ] No unsupported broad claims.
- [ ] Citation and reference lists match.
- [ ] Figures and captions match the text.

