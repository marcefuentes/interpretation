# Manuscript-only review (agent instructions)

> **Template — not active in the interpretation repo.** Copy this file into an
> external folder together with the manuscript bundle and figures. Agents working
> **in** the interpretation repo should follow `ai/harness.md` instead unless the
> user explicitly runs an isolated external-style review.

You are reviewing a **standalone manuscript bundle**. You have **no access** to
simulation source code, raw or processed data, analysis notebooks, author notes,
journal drafts, or any repository harness. Treat yourself as an external reviewer
who received only the files in this folder.

## What counts as “the manuscript”

**Manuscript** means the full publication bundle in this folder — not Methods
alone and not main text alone. It includes every prose file the reader sees:

introduction, methods, **results**, **discussion**, supplement, captions, abstract
(if present), and **figures/**. Review **all** of them. Gaps in Results or
Discussion (undefined outcomes, unsupported claims, figure–text mismatches) are as
important as gaps in Methods.

## Your deliverable

Produce a **review list only**: critiques, questions, inconsistencies, and missing
information across the **entire manuscript**. **Do not edit any manuscript file.**
Do not rewrite paragraphs, patch any `.md` file, or output “proposed replacement
text” unless the user explicitly overrides this instruction.

The author will take your list back to the **interpretation repository**, where
another agent (with TRPS source, data, harness, and journal analysis) resolves each
item — verifying against code, drafting fixes, and committing edits. Your role ends
when the list is complete.

---

## Hard rules

1. **Read only** files in this folder (see below).
2. **Write only** the structured review document described under [Output format](#output-format).
3. **Never** modify any file in the manuscript bundle: `introduction.md`,
   `methods.md`, `results.md`, `discussion.md`, `supplement.md`, `captions.md`,
   `abstract.md`, or anything under `figures/`.
4. If information is missing, **ask a question** — do not invent answers from
   general knowledge of evolutionary models or guess implementation details.
5. If you are unsure whether something is clear, add it to the list; the in-repo
   agent will triage false positives.

---

## Files you may read (the manuscript bundle)

| File / folder | Part of manuscript |
| ------------- | ------------------ |
| `introduction.md` | Introduction |
| `methods.md` | Methods |
| `results.md` | Results |
| `discussion.md` | Discussion |
| `supplement.md` | Supplement |
| `captions.md` | Figure and table legends |
| `abstract.md` | Abstract (if present) |
| `figures/` | Figure images (PNG/PDF) cited anywhere in the above |

If a file is missing, note it in the review; do not search outside this folder.

---

## Files you must not read

- Simulation or analysis code (TRPS, graphgen, scripts)
- Data exports (`.csv`, `.con`, results folders)
- Internal analysis docs, planning notes, or git history
- The interpretation repo, `ai/harness.md`, or `journal/`

---

## Review passes

Run **both passes** unless the user asks for Pass 1 only.

### Pass 1 — Cold read (reviewer)

Read the **full manuscript** in order: abstract (if any) → introduction → methods →
results → discussion → supplement → captions. Cross-check Results and Discussion
against Methods (are outcomes defined before they are reported? do claims need
unstated procedures?). Open figure images in `figures/` whenever any section cites
them.

Build a numbered list of every place a careful reader would stall. Tag each item
with one or more categories:

| Tag | Meaning |
| --- | ------- |
| `term` | Undefined or ambiguous term, notation, or mechanism label |
| `procedure` | Missing or unclear step (initialization, timestep, selection, etc.) |
| `causality` | Claim depends on unstated assumption; IV/DV unclear |
| `reproduce` | Another group could not re-implement or re-run from the text alone |
| `results-gap` | Result or metric not defined earlier; figure needs unstated Methods detail |
| `inconsistent` | Conflict between sections, captions, or tables |

For each item include:

- **ID** — stable label with section prefix, e.g. `I-03` (introduction), `M-12`
  (methods), `R-05` (results), `D-02` (discussion), `S-01` (supplement), `C-04`
  (captions)
- **Location** — file and section (quote or paraphrase the triggering passage)
- **Issue** — what is wrong or missing, in one or two sentences
- **Question** — phrasing as a reviewer would ask the authors

Prefer concrete questions (“How are acts initialized at round 0?”) over vague
notes (“clarify initialization”).

### Pass 2 — Triage (editor)

Re-read Pass 1. For each item add:

- **Severity** — `blocking` (major revision / reproducibility) or `polish`
- **Suggested placement** — where the answer should eventually live: `main` /
  `supplement` / `caption` / `drop` (false alarm on second read)

Do not draft the fix; only say **what** is needed and **where** it should go.

---

## What to prioritize

**Methods**

- Population and genotype initialization at run start
- Order of events within a round (payoffs, shuffling, partner choice, death/birth,
  strategy update)
- Operational definitions of loci and combined mechanism labels (M, P, MP, IJMPQ)
- Cooperation frequency vs C-locus genotype
- Information cost (per locus vs per family, combined mechanisms)
- Simulation grids, constraints (e.g. i + c ≤ b), replicates, averaging

**Results and Discussion**

- Outcome measures defined before first use in Results
- Whether reported patterns are interpretable without the journal or code
- Figure claims vs captions vs Methods (panels, axes, mechanism sets, populations)
- Gaps between main-text figures and supplement figures
- Discussion claims that go beyond what Results showed

Deprioritize: formatting, word counts, citation style, cosmetic renames.

---

## Output format

Write a single markdown document (e.g. `manuscript_review.md` in this folder, or
paste in chat). Use this structure:

```markdown
# Manuscript-only review

## Summary
[2–4 sentences: overall clarity and reproducibility verdict]

## Review list

### Blocking

| ID | Tag(s) | Location | Issue | Question | Placement |
|----|--------|----------|-------|----------|-----------|
| M-01 | procedure, reproduce | methods.md §Model | … | … | main |
| R-02 | results-gap | results.md §2 | … | … | main |

### Non-blocking

| ID | Tag(s) | Location | Issue | Question | Placement |
|----|--------|----------|-------|----------|-----------|
| … | … | … | … | … | … |

## Consistency checks
[Terminology, caption vs text, table notation — bullet list]

## Figures checked
[Files opened; caption–panel mismatches]

## Handoff note
[N items blocking, N non-blocking. Ready for triage in interpretation repo.]
```

The **Review list** table is the primary artifact. The author will paste or
reference it in the interpretation repo with a prompt such as:

> Here is a manuscript-only review list. For each item, say whether it is a real
> gap, already addressed in the text, or a false positive; then fix the manuscript
> using TRPS and journal docs as needed.

---

## What this review does not do

- Verify manuscript text against the simulator
- Check numeric claims against data
- Edit or patch manuscript files
- Replace domain-expert peer review

After the in-repo agent addresses the list, refresh **all manuscript files** in
this folder and run a new review pass if the author wants a second cold read.
