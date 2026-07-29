# Paper Outline (IMRaD)

Working scaffold for the eventual manuscript. The paper stays narrative and
concise; every quantitative claim is backed by a journal document (`../journal/`),
which is where the full analysis, the numbers, and the reasoning live. The journal
is also our record for answering referee questions later.

Section files:

**Submission (`paper/`):**

- [paper/introduction.md](../paper/introduction.md)
- [paper/methods.md](../paper/methods.md)
- [paper/results.md](../paper/results.md)
- [paper/discussion.md](../paper/discussion.md)
- [paper/supplement.md](../paper/supplement.md) — Figs. S1–S11 + Table S1
- [paper/figures.md](../paper/figures.md) — figure manifest (graphgen commands)
- [paper/captions.md](../paper/captions.md) — figure legends
- [paper/references.bib](../paper/references.bib)
- [paper/citing.md](../paper/citing.md)

**Planning (`planning/`):**

- [summary.md](summary.md) — structured abstract (not submission format)
- [roadmap.md](roadmap.md) — framing and status
- [journal-fit-summaries.md](journal-fit-summaries.md) — alternative journal framings

Active venue front matter: [paper/submission/amnat/](../paper/submission/amnat/).

## One-paragraph thesis

Cooperation between unrelated individuals is sustained by direct reciprocity, partner
choice, and reputation, and models normally treat that enforcement machinery as free.
We make it costly and ask who bears the burden created by that cost. Using an
individual-based model of two coevolving populations varied across cooperation cost,
per-population information cost, dilemma type, group size, and partner mixing, we show
that **the effects of enforcement cost often extend beyond the population that pays it**.
Where both populations face the same costs, information cost can look local: it erodes
enforcement alleles while cooperation persists through tax-free unconditional
cooperators, decoupling behaviour from the mechanism that produced it — but a
symmetric design cannot separate the cost a population pays from the burden that cost
creates for its partner. Varying the two populations independently shows that one
population's information cost can govern the cooperation of both, and which
population's cost matters most depends on the enforcement mechanism: under partner
choice a population is nearly insensitive to its own information cost and collapses
under its partner's, because assortment needs active carriers on both sides and the
pair is limited by whichever population supplies fewer; reciprocity-bearing mechanisms
protect only their carriers, so raising the information cost paid by the
low-cooperation-cost population can impose a larger burden on its partner than on the
payer. Removing the social dilemma removes the coupling entirely, identifying it as a
property of the dilemma rather than of the cost accounting. Two consequences follow.
Equal enforcement budgets are neither fungible nor additive: splitting a budget across
both populations yields less total cooperation than loading it on either one, because
each extreme leaves one population with an intact apparatus while a split breaks both.
And the escape route that makes information cost survivable under symmetry is what
makes it destructive under asymmetry — shedding the machinery relieves the payer and
withdraws the service the partner depended on. Supporting this, we identify the payoff
gap limiting each mechanism (reciprocity risk-limited, partner choice limited by the
cooperation advantage, reputation-rich mechanisms reward-limited), and show that
parameter symmetry does not imply outcome symmetry: partner choice produces a
cooperator/exploiter role split — stochastic under equal costs, deterministic under
asymmetry — in which the more cooperative side is frequently the less fit one. When both
cost axes differ, the cooperation-cost gap remains the default role assigner and
information cost inverts roles only in a thin near-zero-i₀ regime where the cheap-cooperation-cost
population pays nothing; the effect requires a genuine dilemma and vanishes under
snowdrift.

## Section-to-journal map

Results are ordered to build the central claim rather than to tour the sweep axes:
the baseline establishes the mechanism hierarchy and the role split, the symmetric
information-cost branch establishes decoupling *and* its methodological limit, and the
per-population sweep delivers the relational result the rest supports.

| Paper section | Topic (journal/) | Figure(s) |
| ------------- | ---------------- | --------- |
| Introduction | framework.md; references.bib | — |
| Methods: model, payoffs, information cost, grid | parameterization.md, framework.md | — |
| Results 1: mechanism hierarchy and cost thresholds | synthesis.md, calibration docs, baseline sweeps | S1 |
| Results 2: the two-population role split | cooperation-cost asymmetry, reciprocity docs | 1–2 |
| Results 3: costly machinery, decoupling, and why symmetry hides the question | symmetric information-cost sweeps | 3, S7 |
| Results 4 (headline): information cost is relational | per-population i0/i1, both costs asymmetric | 4 |
| Results 5: budget non-convexity and the boundary conditions | both costs asymmetric, snowdrift, dilemma-0 control | 4–5, S4 |
| Discussion | synthesis.md, information-cost analyses, framework.md; references.bib | — |

## Status

Manuscript prose written through (Introduction–Discussion), figures locked
(Figs. 1–5, S1–S11), references and supplement table in place. Numbers cite the
journal (regression-checked by `ai/verify_claims.py`). Figures are produced by the
graphgen pipeline rather than stored here. Target: Am Nat ([paper/README.md](../paper/README.md)).
