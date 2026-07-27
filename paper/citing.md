# Citing in this repository

Manuscript prose uses **pandoc-citeproc** keys that resolve against
[`references.bib`](references.bib).

## In Markdown

```markdown
Direct reciprocity can stabilise cooperation [@Trivers1971; @AxelrodHamilton1981].
Partner choice is reviewed by @NoeHammerstein1994.
```

- One or more keys inside `[@...]` (semicolon-separated).
- Narrative form: `@Key` (renders as Author Year).
- Prefer the shortest accurate set; do not pad with tangential citations.

## Keys

Keys are `AuthorYear` or `AuthorAuthorYear` (no spaces). When two works share a
year, append a letter (`NowakSigmund1998a`). The `.bib` file is the source of
truth for titles, journals, and DOIs.

## Building a bibliography

From `paper/`:

```bash
pandoc introduction.md methods.md results.md discussion.md \
  --citeproc --bibliography=references.bib -o /tmp/draft.docx
```

Journal docs under `journal/` stay number-backed and do **not** need cite keys;
the manuscript layer is where prior work is positioned.

## Scope of `references.bib`

Core prior work for: direct/indirect reciprocity, partner choice and biological
markets, reputation, second-order free-riding and costly punishment, cognitive /
monitoring costs, mutualism and interspecific cooperation, and PD vs snowdrift
game structure. Add entries when Introduction or Discussion needs them; keep the
file curated rather than exhaustive.
