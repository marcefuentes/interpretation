# Target-journal formatting

Venue class (locked in [roadmap.md](roadmap.md)): full research article in a
specialist theoretical-biology / evolution journal. Final class file and reference
style are chosen at submission; this note keeps the manuscript portable until then.

## Portable manuscript source

Assemble from `paper/` with pandoc (once installed):

```bash
cd paper
pandoc frontmatter.md introduction.md methods.md results.md discussion.md \
  supplement.md \
  --citeproc --bibliography=references.bib \
  -o interpretation-draft.docx
```

YAML for a future `manuscript.yaml` / journal template:

```yaml
title: "The cost of enforcement is not private: information cost between coevolving populations"
author:
  - name: Marcelino Fuentes
    email: marcelino.fuentes@udc.es
    affiliation: Department of Biology, University of A Coruña, A Coruña, Spain
keywords:
  - cooperation
  - reciprocity
  - partner choice
  - mutualism
  - information cost
  - prisoner's dilemma
  - snowdrift
bibliography: references.bib
```

## House style until a journal is chosen

- **Structure:** IMRaD + numbered main figures (1–6) + supplement (S1–S9, Table S1).
- **Citations:** pandoc `[@Key]` against `references.bib` ([citing.md](citing.md)).
- **Numbers:** cite journal docs; do not duplicate full analyses in the manuscript.
- **Figures:** regenerate via graphgen; do not commit PNG binaries
  ([figures.md](figures.md)).
- **Notation:** prefer Unicode subscripts in prose (c₀, i₁, R − P); ASCII `c0`/`i1`
  only in code-facing paths and figure filenames.
- **Mechanism codes:** _, M, P, MP, MPQ, IMP, IJMPQ as in Methods; expand on first
  use in each major section when space allows.

## Likely venue checklist (fill at submission)

| Item | Status |
| ---- | ------ |
| Journal name | TBD |
| Word / figure limits | Main text ~5–7 figures (locked); confirm abstract word limit |
| Reference style | pandoc `--csl` once CSL chosen (e.g. journal-of-theoretical-biology.csl) |
| Supplement format | PDF or journal supplement portal; captions already in captions.md |
| Data / code availability | Simulation engine + graphgen commands in figures.md; results under ~/results |
| Conflict / funding | TBD |

## What “formatted” means in-repo now

Front matter, IMRaD sections, supplement table, bibliography, and caption set are
aligned. Journal-specific LaTeX/DOCX templates are deferred until the venue is
picked; the pandoc assembly above is the submission precursor.
