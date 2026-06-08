# Mutualism — Reciprocity

Pure reciprocity analysis for the two-population mutualism study (mechanism
**M** only — no partner-choice locus). Partner choice (P) is in
**mutualism_partner_choice.md**; combined mechanisms (MP, MPQ, IMP, IJMPQ) are
in **mutualism_combined.md**.

## Overview

Mutualism is the primary study: two populations with potentially different
costs interact exclusively across populations. Population 0 has cost c0 and
population 1 has cost c1, with c0 < c1 always (the plotted triangular grid
constrains c1 > c0). Benefit b = 0.40 is fixed and K = 0.50.

Hamilton is the diagonal special case where c0 = c1. Because c0 < c1,
population 0 always has a higher cooperation incentive (R0 − P0 > R1 − P1)
in both dilemma types.

The parameter space is a strict upper-triangular 20 × 20 grid:
c0 ∈ {0.00, 0.02, …, 0.38} and c1 ∈ {0.02, 0.04, …, 0.40} with c0 < c1,
giving 210 cells. Only pop_2 (cross-population pairing) is present. Analysis
covers dilemma 1 (prisoner's dilemma) and dilemma 2 (snowdrift), groupsize
128 noshuffle (primary) and groupsize 4 (dedicated section plus comparison);
shuffle conditions are included where noted.

## Payoff structure

All payoffs use cross-benefit form: the benefit b is the contribution received
from the partner, while the cost c is paid by the focal individual. In
snowdrift, b is a shared resource: both players receive it whenever at least
one cooperates (b appears in T, R, and S).

### Dilemma 1 (PD, folder 1)

| Payoff | Pop 0          | Pop 1          |
| ------ | -------------- | -------------- |
| T      | K + b = 0.90   | K + b = 0.90   |
| R      | K + b - c0     | K + b - c1     |
| P      | K = 0.50       | K = 0.50       |
| S      | K - c0         | K - c1         |
| R - P  | b - c0         | b - c1         |

### Dilemma 2 (snowdrift, folder 2)

| Payoff | Pop 0            | Pop 1            |
| ------ | ---------------- | ---------------- |
| T      | K + b = 0.90     | K + b = 0.90     |
| R      | K + b - c0/2     | K + b - c1/2     |
| P      | K = 0.50         | K = 0.50         |
| S      | K + b - c0       | K + b - c1       |
| R - P  | b - c0/2         | b - c1/2         |

In snowdrift, S > P for all c < b, so unilateral cooperation is always
better than mutual defection. The control (\_) already sustains mean qBSeen_0
= 0.955. Reciprocity mechanisms must be evaluated against this high baseline,
not against near-zero cooperation as in PD.

## Cooperation landscape

### Dilemma 1 (PD)

Mechanism M, noshuffle, groupsize 128, fset_0 (lower-cost population):

| c0 \ c1 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------- | ------- | ------- | ------- | ------- |
| c0=0.00 | 0.918   | 0.633   | 0.545   | 0.484   |
| c0=0.10 | ---     | 0.869   | 0.680   | 0.215   |
| c0=0.20 | ---     | ---     | 0.780   | 0.232   |
| c0=0.30 | ---     | ---     | ---     | 0.197   |

Cooperation in fset_0 decreases as c1 increases: even though pop_0's own
incentive is high (c0 small), the partner bottleneck limits achievable
cooperation. When c1 is large, population 1 evolves few cooperators, which
starves pop_0 of reciprocal partners.

Along the c0 = 0 row:

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| \_     | 0.487   | 0.498   | 0.500   | 0.502   | 0.500   |
| M      | 0.941   | 0.918   | 0.654   | 0.569   | 0.513   |

### Dilemma 2 (snowdrift)

Mechanism M, noshuffle, groupsize 128, fset_0:

| c0 \ c1 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------- | ------- | ------- | ------- | ------- |
| c0=0.00 | 0.950   | 0.953   | 0.954   | 0.953   |
| c0=0.10 | ---     | 0.945   | 0.945   | 0.945   |
| c0=0.20 | ---     | ---     | 0.927   | 0.930   |
| c0=0.30 | ---     | ---     | ---     | 0.880   |

Fset_0 cooperation is near ceiling across the grid. The landscape is flat
along rows of constant c0: reciprocity does not need to bootstrap cooperation
from scratch as in PD. Decline appears only at high c0 (pop_0's own cost
rises), not from partner-side bottlenecks.

Along the c0 = 0 row:

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| \_     | 0.922   | 0.975   | 0.976   | 0.976   | 0.976   |
| M      | 0.927   | 0.950   | 0.951   | 0.952   | 0.955   |

Mechanism M adds little marginal lift for fset_0 above the snowdrift control.
The action is in fset_1, where reciprocity can raise cooperation well above
the control floor of 0.091. Combined mechanisms (IMP, IJMPQ) elevate fset_1
much further — see **mutualism_combined.md**.

### Role split (both dilemmas)

Mean qBSeen across all 210 cells (noshuffle, gs=128):

| Mech   | Dilemma | fset_0 (lower c0) | fset_1 (higher c1) | fset_0 > fset_1 |
| ------ | ------- | ----------------- | ------------------ | --------------- |
| \_     | 1 (PD)  | 0.103             | 0.025              | 210/210         |
| M      | 1 (PD)  | 0.637             | 0.551              | 210/210         |
| \_     | 2 (SD)  | 0.955             | 0.091              | 210/210         |
| M      | 2 (SD)  | 0.926             | 0.191              | 210/210         |

In PD, simple reciprocity (M) preserves the deterministic role split in every
cell. In snowdrift, M roughly doubles fset_1 cooperation (0.191 vs 0.091)
but leaves a large gap below fset_0.

## Mechanism comparison

Cooperation at (c0=0.1, c1=0.2) and (c0=0.1, c1=0.3), noshuffle, gs=128:

**Dilemma 1 (PD):**

| Mech   | (0.1, 0.2) fset_0 | (0.1, 0.2) fset_1 | (0.1, 0.3) fset_0 | (0.1, 0.3) fset_1 |
| ------ | ----------------- | ----------------- | ----------------- | ----------------- |
| \_     | 0.051             | 0.026             | 0.047             | 0.018             |
| M      | 0.869             | 0.830             | 0.680             | 0.616             |

**Dilemma 2 (snowdrift):**

| Mech   | (0.1, 0.2) fset_0 | (0.1, 0.2) fset_1 | (0.1, 0.3) fset_0 | (0.1, 0.3) fset_1 |
| ------ | ----------------- | ----------------- | ----------------- | ----------------- |
| \_     | 0.972             | 0.089             | 0.972             | 0.057             |
| M      | 0.945             | 0.188             | 0.945             | 0.123             |

At mild asymmetry (c0=0.1, c1=0.2), M achieves high cooperation in both
populations in PD (0.869/0.830) but only modest fset_1 lift in snowdrift
(0.188 vs 0.089 control).

## Exploitation and reciprocity

Reciprocity elevates fset_1 cooperation, which weakens the cooperation/fitness
link relative to the control. The correlation between ΔqBSeen and Δfitness:

| Mech   | Dilemma | noshuffle | shuffle |
| ------ | ------- | --------- | ------- |
| \_     | 1 (PD)  | -1.000    | -1.000  |
| M      | 1 (PD)  | -0.867    | -1.000  |
| \_     | 2 (SD)  | -0.148    | -0.141  |
| M      | 2 (SD)  | -0.265    | -0.141  |

In PD, M noshuffle shows the weakest exploitation (−0.867): direct reciprocity
elevates fset_1 enough to partially equalize fitness. Shuffling restores the
deterministic link (−1.000) by destroying partner memory.

In snowdrift, all correlations are weaker than in PD because the payoff floor
sustains high fset_0 cooperation regardless of mechanism. M noshuffle shows
moderate coupling (−0.265) from reciprocity-driven elevation of fset_1.

### Snowdrift-specific dynamics in fset_1

The control leaves fset_1 near 0.09 despite S1 > P1, because pop_0's heavy
cooperation means defectors receive T1 = R1 (the shared benefit b arrives
regardless). Direct reciprocity partially overcomes this:

| Mech   | fset_1 mean (all 210 cells) | fset_1 at (0.1, 0.3) |
| ------ | --------------------------- | -------------------- |
| \_     | 0.091                       | 0.057                |
| M      | 0.191                       | 0.123                |

## Shuffle effect on M mechanism

Shuffling destroys direct reciprocity in PD but is inconsequential in snowdrift,
where the cooperation floor is already high.

**Dilemma 1 (PD), fset_0:**

| Condition        | (0.02, 0.38) | (0.10, 0.20) | (0.20, 0.38) |
| ---------------- | ------------ | ------------ | ------------ |
| noshuffle_gs128  | 0.312        | 0.869        | 0.360        |
| shuffle_gs128    | 0.207        | 0.051        | 0.025        |

At (c0=0.1, c1=0.2), M noshuffle achieves qBSeen_0 = 0.869 vs 0.051 with
shuffle — a 17× difference. The effect is largest at near-diagonal cells where
both populations can sustain iterated reciprocal cooperation.

**Dilemma 2 (snowdrift), fset_0:**

| Condition        | (0.02, 0.38) | (0.10, 0.20) | (0.20, 0.38) |
| ---------------- | ------------ | ------------ | ------------ |
| noshuffle_gs128  | 0.953        | 0.945        | 0.929        |
| shuffle_gs128    | 0.973        | 0.968        | 0.960        |

Shuffle has no penalty and may slightly increase cooperation in snowdrift,
because the shared-benefit payoff structure does not depend on stable partner
pairings for fset_0 to cooperate. Direct reciprocity's value in snowdrift is
concentrated in elevating fset_1, not in bootstrapping fset_0.

For M in snowdrift, shuffle reduces the exploitation correlation from −0.265
(noshuffle) to −0.141 (shuffle) — matching the control — because shuffling
removes the reciprocity-driven elevation of fset_1 that creates cooperation
asymmetry.

## Single-run dynamics (mutualism_1run)

Along the c0 = 0 row (mechanism M, noshuffle, PD, fset_0), single-run
trajectories show high but variable cooperation:

| c1   | Range | Representative trajectory              |
| ---- | ----- | -------------------------------------- |
| 0.02 | 0.951 | 0.934 → 0.948 → 0.929 → 0.951         |
| 0.10 | 0.940 | 0.924 → 0.914 → 0.932 → 0.940         |
| 0.18 | 0.680 | 0.680 → 0.569 → 0.626 → 0.658         |
| 0.20 | 0.714 | 0.589 → 0.632 → 0.714 → 0.702         |

The trajectory ranges increase as c1 increases, while still showing persistent
non-zero cooperation even at c1 = 0.20. This confirms that the multi-run
averages represent genuine intermediate cooperation levels, not averaging of
all-or-nothing states.

Snowdrift single-run analysis is pending (mutualism_1run exports not yet
available for dilemma 2).

## Groupsize 4

### Cooperation landscape

Mechanism M, fset_0, noshuffle:

**Dilemma 1 (PD):**

| c0 \ c1 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------- | ------- | ------- | ------- | ------- |
| c0=0.00 | 0.915   | 0.643   | 0.541   | 0.485   |
| c0=0.10 | ---     | 0.863   | 0.684   | 0.211   |
| c0=0.20 | ---     | ---     | 0.777   | 0.236   |
| c0=0.30 | ---     | ---     | ---     | 0.188   |

**Dilemma 2 (snowdrift):**

| c0 \ c1 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------- | ------- | ------- | ------- | ------- |
| c0=0.00 | 0.947   | 0.953   | 0.954   | 0.956   |
| c0=0.10 | ---     | 0.943   | 0.946   | 0.945   |
| c0=0.20 | ---     | ---     | 0.927   | 0.930   |
| c0=0.30 | ---     | ---     | ---     | 0.875   |

Mean qBSeen across all 210 cells (noshuffle):

| Mech   | Dilemma | fset_0 | fset_1 | fset_0 > fset_1 |
| ------ | ------- | ------ | ------ | --------------- |
| M      | 1 (PD)  | 0.636  | 0.551  | 209/210         |
| M      | 2 (SD)  | 0.926  | 0.191  | 210/210         |

In PD, the gs=4 landscape matches gs=128 qualitatively. In snowdrift, fset_0
stays near ceiling.

### Exploitation at gs=4

| Mech   | Dilemma | noshuffle |
| ------ | ------- | --------- |
| M      | 1 (PD)  | -0.864    |
| M      | 2 (SD)  | -0.268    |

M noshuffle shows weaker coupling at gs=4 than gs=128 in PD (−0.864 vs
−0.867) because direct reciprocity elevates fset_1 cooperation enough to
partially equalize fitness in the small group. Snowdrift correlations follow
the same weak pattern as gs=128.

### Shuffle effect at gs=4

Sample cells for mechanism M, fset_0:

**Dilemma 1 (PD):**

| Condition       | (0.02, 0.38) | (0.10, 0.20) | (0.20, 0.38) |
| --------------- | ------------ | ------------ | ------------ |
| noshuffle_gs4   | 0.301        | 0.863        | 0.363        |
| shuffle_gs4     | 0.377        | 0.087        | 0.034        |

The shuffle penalty on M at gs=4 (0.863 → 0.087 at (0.10, 0.20)) is
comparable to gs=128. Small groups do not rescue shuffled direct reciprocity
in PD.

**Dilemma 2 (snowdrift):**

| Condition       | (0.02, 0.38) | (0.10, 0.20) | (0.20, 0.38) |
| --------------- | ------------ | ------------ | ------------ |
| noshuffle_gs4   | 0.954        | 0.943        | 0.929        |
| shuffle_gs4     | 0.953        | 0.940        | 0.926        |

As at gs=128, shuffle has no penalty in snowdrift — the cooperation floor
does not depend on stable partner pairings for fset_0.

## Groupsize comparison (gs=4 vs gs=128)

Mechanism M is largely invariant to groupsize reduction:

**Dilemma 1 (PD), noshuffle:**

| c0   | c1   | fset_0 gs=4 | fset_0 gs=128 | fset_1 gs=4 | fset_1 gs=128 |
| ---- | ---- | ----------- | ------------- | ----------- | ------------- |
| 0.10 | 0.20 | 0.863       | 0.869         | 0.830       | 0.830         |
| 0.20 | 0.30 | 0.777       | 0.780         | 0.519       | 0.519         |

**Dilemma 2 (snowdrift), noshuffle:** gs=4 and gs=128 are broadly similar for
both populations.

| Mechanism | gs=4 effect relative to gs=128 (PD) | gs=4 effect relative to gs=128 (snowdrift) |
| --------- | ----------------------------------- | ------------------------------------------ |
| \_        | Identical                           | Identical                                  |
| M         | Negligible difference               | Negligible difference                      |

Combined mechanisms show different groupsize sensitivity — see
**mutualism_combined.md**.

## Summary

| Topic                 | PD (dilemma 1)                                              | Snowdrift (dilemma 2)                              |
| --------------------- | ----------------------------------------------------------- | -------------------------------------------------- |
| M vs control (fset_0) | 0.637 vs 0.103 — reciprocity essential                      | 0.926 vs 0.955 — marginal; snowdrift floor dominates |
| M vs control (fset_1) | 0.551 vs 0.025 — large lift                                 | 0.191 vs 0.091 — moderate lift                   |
| Role split            | fset_0 > fset_1 in 210/210                                  | fset_0 > fset_1 in 210/210                       |
| M vs shuffle          | 17× penalty at (0.1, 0.2): 0.869 → 0.051                  | No penalty; shuffle ≈ noshuffle (~0.95) for fset_0 |
| Exploitation (M)      | corr = −0.867 noshuffle; shuffle restores −1.000            | corr = −0.265 noshuffle; weaker than PD            |
| gs=4 M (PD)           | Landscape matches gs=128; shuffle penalty severe (0.863 → 0.087) | Near ceiling; shuffle penalty absent         |
