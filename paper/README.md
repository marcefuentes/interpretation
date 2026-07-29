# American Naturalist submission

Blind-review manuscript for *The American Naturalist* (Major Article). Requirements:
[amnat-instructions.md](amnat-instructions.md).

Internal planning (outline, roadmap, structured abstract): [../manuscript/README.md](../manuscript/README.md).

## Manuscript order (blind review PDF)

| Order | File | In blind MS? |
| ----- | ---- | ------------ |
| 1 | [title-page.md](title-page.md) | Yes (no author names) |
| 2 | [abstract.md](abstract.md) | Yes |
| 3 | [introduction.md](introduction.md) | Yes |
| 4 | [methods.md](methods.md) | Yes |
| 5 | [results.md](results.md) | Yes |
| 6 | [discussion.md](discussion.md) | Yes |
| 7 | Literature Cited | Yes (from `references.bib`) |
| 8 | [supplement.md](supplement.md) | Yes (or author-supplied supplement PDF) |
| 9 | [captions.md](captions.md) | Review: inline preferred; production: after Literature Cited |

**Not in blind manuscript** (Editorial Manager only): [authors-submission.md](authors-submission.md), [acknowledgments-submission.md](acknowledgments-submission.md).

## Build review draft (pandoc)

From `paper/`:

```bash
pandoc title-page.md abstract.md introduction.md methods.md results.md discussion.md \
  supplement.md captions.md \
  --citeproc --bibliography=references.bib \
  -o interpretation-amnat-review.docx
```

Before export:

- Double-space and add line numbers in Word/LibreOffice (required for review).
- Embed figures at first citation (paths from [figures.md](figures.md)); regenerate via graphgen.
- Run word count on main text and update [title-page.md](title-page.md).
- Confirm abstract ≤ 200 words (`wc -w abstract.md` — count paragraph only).

LaTeX: [official Am Nat template](https://www.journals.uchicago.edu/pb-assets/docs/journals/AmNat_MS_template-1683838715810.tex).

## Word count (main text only)

```bash
pandoc introduction.md methods.md results.md discussion.md -t plain | wc -w
```

Excludes Literature Cited, supplement, and captions — matches Major Article limit (≤ 7,500 words).
