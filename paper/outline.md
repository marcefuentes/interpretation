# Paper Outline (IMRaD)

Working scaffold for the eventual manuscript. The paper stays narrative and
concise; every quantitative claim is backed by a journal document (`../journal/`),
which is where the full analysis, the numbers, and the reasoning live. The journal
is also our record for answering referee questions later.

Section files:

- summary.md — draft publication summary (structured abstract)
- introduction.md
- methods.md
- results.md
- discussion.md
- figures.md — figure manifest (provenance + graphgen commands; no image binaries in-repo)
- roadmap.md — plan from scaffold to finished manuscript (framing, phases, open items)

## One-paragraph thesis

Cooperation between unrelated individuals is sustained by direct reciprocity, partner
choice, and reputation, and models normally treat that enforcement machinery as free.
We make it costly and ask who bears the cost. Using an individual-based model of two
coevolving populations swept across cooperation cost, per-population information cost,
dilemma type, group size, and partner mixing, we show that **the cost of enforcement is
not borne privately**. Where both populations face the same costs, information cost
looks like a private burden: it erodes enforcement alleles while cooperation persists
through tax-free unconditional cooperators, decoupling behaviour from the mechanism
that produced it — but a symmetric design cannot separate the cost a population pays
from the cost its partner pays. Sweeping the two independently shows the burden is
relational. A single population's information cost governs the cooperation of both, and
which population that is depends on the enforcement mechanism: under partner choice a
population is nearly insensitive to its own cost and collapses under its partner's,
because assortment is a service that needs active carriers on both sides and the pair
is limited by whichever population supplies fewer, whereas reciprocity-bearing
mechanisms protect only their carriers and are bound by the focal population's own
cost. Removing the social dilemma removes the coupling entirely, identifying it as a
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
asymmetry — in which the cooperating side is frequently the less fit one. When both
cost axes differ, the cooperation-cost gap remains the default role assigner and
information cost inverts roles only in a thin wedge where the cheap-cooperation-cost
population pays nothing; the effect requires a genuine dilemma and vanishes under
snowdrift.

## Section-to-journal map

Results are ordered to build the central claim rather than to tour the sweep axes:
the baseline establishes the mechanism hierarchy and the role split, the symmetric
information-cost branch establishes decoupling *and* its methodological limit, and the
per-population sweep delivers the relational result the rest supports.

| Paper section | Topic (journal/) | Figure(s) |
| ------------- | ---------------- | --------- |
| Introduction | framework.md | — |
| Methods: model, payoffs, information cost, grid | parameterization.md, framework.md | — |
| Results 1: mechanism hierarchy and cost thresholds | synthesis.md, calibration docs, baseline sweeps | 1 |
| Results 2: the two-population role split | cooperation-cost asymmetry, reciprocity docs | 2–3 |
| Results 3: costly machinery, decoupling, and why symmetry hides the question | symmetric information-cost sweeps | 4, S7 |
| Results 4 (headline): information cost is relational | per-population i0/i1, both costs asymmetric | 5 |
| Results 5: budget non-convexity and the boundary conditions | both costs asymmetric, snowdrift, dilemma-0 control | 6–7, S4 |
| Discussion | synthesis.md, information-cost analyses, framework.md | — |

## Status

First-draft scaffold. Prose is provisional and numbers are cited rather than
restated in full; consult the linked journal doc for the exact values (all
regression-checked by `ai/verify_claims.py`). Figures are produced by the graphgen
pipeline (`../graph/graphgen/`) rather than stored here.
