# The American Naturalist — local submission reference

Condensed from the journal’s [Instructions for Authors](https://www.journals.uchicago.edu/journals/an/instruct) (UChicago Press). Check the live page before final submission in case policies change.

**Submission portal:** [Editorial Manager](http://amnat.edmgr.com)  
**LaTeX template:** [AmNat MS template](https://www.journals.uchicago.edu/pb-assets/docs/journals/AmNat_MS_template-1683838715810.tex)  
**Best practices checklist:** [ASN MS checklist](https://www.amnat.org/announcements/MS-Checklist.html)  
**Data archiving:** [Code + data guidelines](https://comments.amnat.org/2021/12/guidelines-for-archiving-code-with-data.html)

## Aims (relevance test)

Am Nat seeks manuscripts that advance conceptual unification in evolution, ecology,
behavior, and related organismal biology — new syntheses, significant problems, novel
subjects, or changed thinking. Methods papers need to show how the method advances a
general conceptual issue, illustrate it on data, and discuss broader use.

## Article type for this manuscript

**Major Article** — new data, theory, and/or analysis. Target limits:

| Item | Limit |
| ---- | ----- |
| Main text | ≤ 7,500 words (excluding Literature Cited; including boxes) |
| Abstract | ≤ **200 words** |
| Figures + tables (print) | ≤ 6 |
| Figure legends | generally ≤ 100 words each |
| Short title (running head) | ≤ **40 characters** (including spaces) |

Exceeding word limits requires justification in Editorial Manager Author Comments.

Other types: Notes (≤ 3,000 words, abstract ≤ 150); Comments (abstract ≤ 100).

## Double-anonymous review

**Remove from the manuscript file before review:**

- Author names, affiliations, and acknowledgments
- Author contribution statements
- Self-identifying citations (“we showed in Smith 2024” → “Smith 2024 showed”)

**Enter only in Editorial Manager (not on blind manuscript):**

- All authors, affiliations, emails, ORCIDs
- Acknowledgments and author contributions (paste into Comments or restore after acceptance)
- Cover letters are optional and may be removed

Preprints on BioRxiv / arXiv / EcoEvoRxiv / PCI are allowed (noncommercial repos); they can compromise blind review.

## Required formatting before review

- **Double-spaced** entire manuscript
- **Line numbers** and **page numbers** (continuous)
- Math fonts **embedded** in PDF (check Editorial Manager PDF carefully)
- **(Author, Year)** in-text citations preferred for review
- **Methods before Results** (IMRaD not rigid, but Methods must precede matching Results)
- Figures and tables **in text where first cited**, caption on same page when possible

Exact Am Nat reference style not required at first submission; required at acceptance.

## Manuscript file order (this repo)

Mapped to files in `paper/`. See [README.md](README.md).

1. **Title page** — `title-page.md` (no authors on blind MS)
2. **Abstract** — `abstract.md` (separate page; ≤ 200 words)
3. **Introduction** — `introduction.md`
4. **Methods** — `methods.md`
5. **Results** — `results.md`
6. **Discussion** — `discussion.md`
7. **Literature Cited** — generated from `references.bib` via pandoc
8. **Supplement** — `supplement.md` (online supplement; cite panels in main text)
9. **Figure legends** — `captions.md` (for production: after Literature Cited; for review, prefer inline with figures)

## Title page content (first page of manuscript)

- Title (clear, concise; ~8–10 words often effective; no series numbering)
- **Short title** ≤ 40 characters
- **Article type** (e.g. Major Article)
- **Keywords:** **1–6** (on title page, not inside abstract)
- **Word count** of main text (excluding Literature Cited)
- **List of manuscript elements** (figures, tables, boxes, appendices) so reviewers see nothing is missing

Keywords and short title are also entered in Editorial Manager at submission.

## Abstract

- **Single narrative paragraph** — no structured headings (Background / Methods / …)
- ≤ 200 words for Major Articles
- Separate page with the word **Abstract** alone on the first line
- **Same text** pasted into Editorial Manager abstract field
- Optional secondary abstract in another language (secondary title field)

Internal structured mirror for planning: `manuscript/summary.md` (not for submission).

## Keywords

1–6 terms on the title page. Prefer terms readers search for over clever title-only phrasing.

## Text style (at acceptance)

- *Chicago Manual of Style* and *CSE Scientific Style and Format*
- Scientific and common names for organisms
- SI units
- No italics or bold for emphasis
- No bulleted or numbered indented lists in main text
- Define every symbol at first use; symbol table in main text if helpful

## References (Literature Cited)

Review: author–date in text, alphabetical Literature Cited acceptable if consistent.

At acceptance: chronological in text, then alphabetical within year; spell out journal and press names; city for books. Example:

> Maynard Smith, J. 1966. Sympatric speciation. American Naturalist 100:637–650.

Unpublished work: “A. B. Smith, unpublished data” — not in Literature Cited. “In review” → unpublished manuscript in text only.

Supplement references are typeset in the main Literature Cited list.

## Tables

- No vertical/horizontal rules in table body; no colors/shading/panels in tables (use a figure instead)
- Table title short; notes after table
- For production: after Literature Cited, before figure legends
- For review: may be inline where cited

## Figures

- Panels labeled with capital letters; cite as “figure 2A”
- All panels of one figure on same page when possible
- Supplement figures: figure S1, etc.; appendix figures: figure B1, etc.
- For production: separate files; legends after tables
- Color: CMYK for print vs RGB online can shift ~15%

## Data and code (required at submission)

- Data and code needed to reproduce results must be archived (Dryad, Zenodo, OSF, Figshare, Dataverse, etc.)
- **README** describing archive contents (prefer single README.txt / README.md)
- Private reviewer link or zip via Editorial Manager at submission
- Data/code accessibility statement after Acknowledgments **after acceptance**

## Submission checklist (Editorial Manager)

1. Article type
2. Manuscript PDF or source (LaTeX template recommended)
3. Data/code archive + reviewer access
4. Suggested reviewers (diverse / early career encouraged; no recent collaborators)
5. Preprint status
6. Data location URL
7. Agreement to data policy
8. Optional associate editor suggestion
9. Author Comments: acknowledgments + contributions (removed from blind MS)
10. Title, short title, abstract, full author list with affiliations and emails

## After acceptance

- Acknowledgments restored (include funding)
- Data and code accessibility statement + citation in Literature Cited
- Author contribution statement (multi-author)
- Publication agreement (copyright to University of Chicago)
- Page charges: $90/typeset page; ASN grant-in-aid possible for members without funding
- Open access: CC-BY-NC or CC-BY with APC

## Repo mapping

| Am Nat element | Repo file |
| -------------- | --------- |
| Instructions (this note) | `paper/amnat-instructions.md` |
| Assembly guide | `paper/README.md` |
| Title page (blind) | `paper/title-page.md` |
| Abstract | `paper/abstract.md` |
| Authors (EM only) | `paper/authors-submission.md` |
| Acknowledgments (EM / post-acceptance) | `paper/acknowledgments-submission.md` |
| Body | `paper/introduction.md` … `paper/discussion.md` |
| Supplement | `paper/supplement.md` |
| Captions | `paper/captions.md` |
| Bibliography | `paper/references.bib` |
| Figure provenance | `paper/figures.md` |
| Internal planning | `manuscript/` |
