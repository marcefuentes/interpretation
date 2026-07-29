# Manuscript formatting

**Target journal:** The American Naturalist — Major Article. Requirements:
[paper/amnat-instructions.md](../paper/amnat-instructions.md). Assembly:
[paper/README.md](../paper/README.md).

This note duplicates assembly steps for convenience; the canonical build command lives
in `paper/README.md`.

```bash
cd paper
pandoc title-page.md abstract.md introduction.md methods.md results.md discussion.md \
  supplement.md captions.md \
  --citeproc --bibliography=references.bib \
  -o interpretation-amnat-review.docx
```

Then double-space, add line numbers, embed figures. Alternative journal abstracts:
[journal-fit-summaries.md](journal-fit-summaries.md).
