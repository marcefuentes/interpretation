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

Cooperation between unrelated individuals can be sustained by direct reciprocity,
partner choice, and reputation, but which mechanism works — and how much
cooperation, how symmetric, and produced by which genotypes — depends on the social
dilemma, on how costly cooperation and the enforcement machinery are, and on the
ecological context. Using an individual-based model swept across these axes, we show
that (i) the payoff gap each mechanism is limited by is identifiable and stable
(reciprocity is risk-limited, partner choice is limited by the cooperation
advantage, reputation-rich mechanisms are reward-limited); (ii) with two populations
a cooperator/exploiter role split emerges, stochastically when payoffs are symmetric
and deterministically when they are not; and (iii) making the machinery itself
costly sets a price on enforcement whose effects depend on demand: on the symmetric
low-demand edge, cooperation can persist after the apparatus is eroded, decoupling
behaviour from the mechanism that produced it, but under built-in asymmetry the same
price more directly retreats the cooperation ceiling and compresses the
cooperator/exploiter split.

## Section-to-journal map

| Paper section | Backed by (journal/) |
| ------------- | -------------------- |
| Introduction | framework.md |
| Methods: model, payoffs, grid | parameterization.md, framework.md; hamilton.md and mutualism.md (noise floor, replicates) |
| Results 1: level of cooperation | synthesis.md, prisoners_calibration.md, snowdrift_calibration.md, hamilton_*.md, mutualism_*.md, hamilton_cost.md, mutualism_cost.md |
| Results 2: between-population asymmetry | mutualism_partner_choice.md, mutualism_combined.md, mutualism_cost.md, prisoners_partner_choice.md, synthesis.md |
| Results 3: composition / route to cooperation | hamilton_cost.md, mutualism_cost.md, hamilton_reciprocity.md, mutualism_reciprocity.md, synthesis.md |
| Discussion | synthesis.md, hamilton_cost.md, mutualism_cost.md, framework.md |

## Status

First-draft scaffold. Prose is provisional and numbers are cited rather than
restated in full; consult the linked journal doc for the exact values (all
regression-checked by `ai/verify_claims.py`). Figures are produced by the graphgen
pipeline (`../graph/graphgen/`) rather than stored here.
