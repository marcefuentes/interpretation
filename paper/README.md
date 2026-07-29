# Manuscript and submission

**Venue-agnostic body** (IMRaD, supplement, figures, bibliography) plus **venue-specific
submission** files under [submission/](submission/README.md).

**Active target:** The American Naturalist — [submission/amnat/](submission/amnat/).

Internal planning (outline, structured abstract, fallback venues):
[../planning/README.md](../planning/README.md).

## Manuscript body (reuse across journals)

| File | Role |
| ---- | ---- |
| [introduction.md](introduction.md) | Introduction |
| [methods.md](methods.md) | Methods |
| [results.md](results.md) | Results |
| [discussion.md](discussion.md) | Discussion |
| [supplement.md](supplement.md) | Supplement (Figs. S1–S11, Table S1) |
| [captions.md](captions.md) | Figure legends |
| [figures.md](figures.md) | Figure manifest (graphgen commands) |
| [references.bib](references.bib) | Bibliography |
| [citing.md](citing.md) | Citation convention |

## Build review PDF (current venue: Am Nat)

From `paper/`:

```bash
pandoc submission/amnat/title-page.md submission/amnat/abstract.md \
  introduction.md methods.md results.md discussion.md \
  supplement.md captions.md \
  --citeproc --bibliography=references.bib \
  -o interpretation-amnat-review.docx
```

Before export: double-space, line numbers, embed figures at first citation.

Main-text word count (Introduction–Discussion):

```bash
pandoc introduction.md methods.md results.md discussion.md -t plain | wc -w
```

See [submission/amnat/instructions.md](submission/amnat/instructions.md) for Am Nat limits and checklist.
