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
a cooperator/exploiter role split emerges — stochastically under parameter symmetry
(c0 = c1, i0 = i1) with partner choice, deterministically when cooperation cost or
information cost is parameter-asymmetric, with mechanism-dependent inversions under
combined reputation; and (iii) making the machinery itself
costly makes information cost bite whose effects depend on cooperation cost: where
cooperation cost is zero, cooperation can persist after the apparatus is eroded,
decoupling behaviour from the mechanism that produced it, but under cooperation-cost
asymmetry the same information cost more directly retreats the cooperation ceiling and
compresses the cooperator/exploiter split; per-population information-cost asymmetry
at symmetric cooperation cost can assign or invert roles depending on mechanism, but
when both cooperation cost and information cost differ between populations the
cooperation-cost gap dominates globally and information cost inverts combined
mechanisms only in a thin i0 ≈ 0 wedge.

## Section-to-journal map

| Paper section | Topic (journal/) |
| ------------- | ---------------- |
| Introduction | framework.md |
| Methods: model, payoffs, grid | parameterization.md, framework.md |
| Results 1: level of cooperation | synthesis.md, calibration docs, baseline and information-cost sweeps |
| Results 2: between-population asymmetry | cooperation-cost asymmetry, information-cost asymmetry, per-population i0/i1, both costs asymmetric |
| Results 3: composition / route to cooperation | information-cost sweeps, reciprocity docs, synthesis.md |
| Discussion | synthesis.md, information-cost analyses, framework.md |

## Status

First-draft scaffold. Prose is provisional and numbers are cited rather than
restated in full; consult the linked journal doc for the exact values (all
regression-checked by `ai/verify_claims.py`). Figures are produced by the graphgen
pipeline (`../graph/graphgen/`) rather than stored here.
