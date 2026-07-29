# Submission (venue-specific)

Each subdirectory holds the front matter and instructions for one target journal.
The IMRaD body in `paper/` is shared; only this layer changes when retargeting.

## Active venue

**[amnat/](amnat/)** — *The American Naturalist* (Major Article)

## Retargeting after rejection

1. Copy `amnat/` to a new folder (e.g. `jeb/`).
2. Replace `instructions.md` with the new journal's requirements (or a local copy of their author guidelines).
3. Rewrite `abstract.md` to the new word limit and format.
4. Update `title-page.md` (keywords count, short title rules, element list).
5. Adjust `authors-submission.md` / `acknowledgments-submission.md` if the portal differs.
6. Update the build command in [../README.md](../README.md) and any abstract variants in [../../planning/journal-fit-summaries.md](../../planning/journal-fit-summaries.md).

Fallback abstract drafts for other journals: [planning/journal-fit-summaries.md](../../planning/journal-fit-summaries.md).
