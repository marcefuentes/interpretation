# Mutualism — Reciprocity

Pure reciprocity analysis for the two-population mutualism study — direct
reciprocity (**M**) and indirect reciprocity (**IM**, **IJM**), no
partner-choice locus. M is present under both shuffle and noshuffle; IM and
IJM exist only under the shuffle conditions, which is precisely where direct
reciprocity collapses and reputation-based reciprocity earns its keep. Partner
choice (P) is in **mutualism_partner_choice.md**; combined mechanisms (MP, MPQ,
IMP, IJMPQ) are in **mutualism_combined.md**.

## Overview

See **[asymmetric_c0_c1.md](asymmetric_c0_c1.md#overview)** for the common model overview and parameter space.

## Payoff structure

See **[asymmetric_c0_c1.md](asymmetric_c0_c1.md#payoff-structure)** for the common payoff structure and control baseline. Reciprocity mechanisms must be evaluated against the high snowdrift baseline, not against near-zero cooperation as in PD.

## Cooperation landscape

### Dilemma 1 (PD)

Mechanism M, noshuffle, groupsize 128, Pop_0 (lower-cost population):

| c0 \ c1 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------- | ------- | ------- | ------- | ------- |
| c0=0.00 | 0.918   | 0.633   | 0.545   | 0.484   |
| c0=0.10 | ---     | 0.869   | 0.680   | 0.215   |
| c0=0.20 | ---     | ---     | 0.780   | 0.232   |
| c0=0.30 | ---     | ---     | ---     | 0.197   |

Cooperation in Pop_0 decreases as c1 increases: even though Pop_0's own
incentive is high (c0 small), the partner bottleneck limits achievable
cooperation. When c1 is large, population 1 evolves few cooperators, which
starves Pop_0 of reciprocal partners.

Along the c0 = 0 column:

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| \_     | 0.487   | 0.498   | 0.500   | 0.502   | 0.500   |
| M      | 0.941   | 0.918   | 0.654   | 0.569   | 0.513   |

### Dilemma 2 (snowdrift)

Mechanism M, noshuffle, groupsize 128, Pop_0:

| c0 \ c1 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------- | ------- | ------- | ------- | ------- |
| c0=0.00 | 0.950   | 0.953   | 0.954   | 0.953   |
| c0=0.10 | ---     | 0.945   | 0.945   | 0.945   |
| c0=0.20 | ---     | ---     | 0.927   | 0.930   |
| c0=0.30 | ---     | ---     | ---     | 0.880   |

Pop_0 cooperation is near ceiling across the grid. The landscape is flat
along rows of constant c0: reciprocity does not need to bootstrap cooperation
from scratch as in PD. Decline appears only at high c0 (Pop_0's own cost
rises), not from partner-side bottlenecks.

Along the c0 = 0 column:

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| \_     | 0.922   | 0.975   | 0.976   | 0.976   | 0.976   |
| M      | 0.927   | 0.950   | 0.951   | 0.952   | 0.955   |

Mechanism M adds little marginal lift for Pop_0 above the snowdrift control.
The action is in Pop_1, where reciprocity can raise cooperation well above
the control floor of 0.091. Combined mechanisms (IMP, IJMPQ) elevate Pop_1
much further — see **mutualism_combined.md**.

### Role split (both dilemmas)

Mean qBSeen across all 210 cells (noshuffle, gs=128):

| Mech   | Dilemma | Pop_0 (lower c0) | Pop_1 (higher c1) | Pop_0 > Pop_1 |
| ------ | ------- | ----------------- | ------------------ | --------------- |
| \_     | 1 (PD)  | 0.103             | 0.025              | 210/210         |
| M      | 1 (PD)  | 0.637             | 0.551              | 210/210         |
| \_     | 2 (SD)  | 0.955             | 0.091              | 210/210         |
| M      | 2 (SD)  | 0.926             | 0.191              | 210/210         |

In PD, simple reciprocity (M) preserves the deterministic role split in every
cell. In snowdrift, M roughly doubles Pop_1 cooperation (0.191 vs 0.091)
but leaves a large gap below Pop_0.

### Cooperation Boost vs. Asymmetry Effects

Comparing direct reciprocity (M) to the control (_) in Mutualism shows a strong tendency to enforce symmetry compared to partner choice:

- **Prisoner's Dilemma (PD):** 
  - The major effect of allowing reciprocity is **to increase cooperation symmetrically** in both populations, keeping asymmetry low. Pop_0's cooperation increases by +0.534 (from 0.103 to 0.637) and Pop_1's cooperation increases by +0.526 (from 0.025 to 0.551). The net asymmetry change is a negligible +0.008 (from 0.078 to 0.086). Because conditional cooperation (TFT) ties players' actions together, Pop_0 cannot cooperate without Pop_1 reciprocating, which successfully lifts Pop_1 to cooperate and prevents the emergence of high exploitation asymmetries.
- **Snowdrift:** 
  - The major effect of allowing reciprocity is **to decrease asymmetry** (by -0.129 on average). Under the control, asymmetry is extremely high (0.864) because Pop_0 cooperates at ceiling while Pop_1 free-rides and defects. Reciprocity elevates Pop_1's cooperation by +0.100 (from 0.091 to 0.191) while Pop_0's cooperation drops slightly (by -0.029), narrowing the asymmetry.

## Mechanism comparison

Cooperation at (c0=0.1, c1=0.2) and (c0=0.1, c1=0.3), noshuffle, gs=128:

**Dilemma 1 (PD):**

| Mech   | (0.1, 0.2) Pop_0 | (0.1, 0.2) Pop_1 | (0.1, 0.3) Pop_0 | (0.1, 0.3) Pop_1 |
| ------ | ----------------- | ----------------- | ----------------- | ----------------- |
| \_     | 0.051             | 0.026             | 0.047             | 0.018             |
| M      | 0.869             | 0.830             | 0.680             | 0.616             |

**Dilemma 2 (snowdrift):**

| Mech   | (0.1, 0.2) Pop_0 | (0.1, 0.2) Pop_1 | (0.1, 0.3) Pop_0 | (0.1, 0.3) Pop_1 |
| ------ | ----------------- | ----------------- | ----------------- | ----------------- |
| \_     | 0.972             | 0.089             | 0.972             | 0.057             |
| M      | 0.945             | 0.188             | 0.945             | 0.123             |

At mild asymmetry (c0=0.1, c1=0.2), M achieves high cooperation in both
populations in PD (0.869/0.830) but only modest Pop_1 lift in snowdrift
(0.188 vs 0.089 control).

## Exploitation and reciprocity

Reciprocity elevates Pop_1 cooperation, which weakens the cooperation/fitness
link relative to the control. The correlation between ΔqBSeen and Δfitness:

| Mech   | Dilemma | noshuffle | shuffle |
| ------ | ------- | --------- | ------- |
| \_     | 1 (PD)  | -1.000    | -1.000  |
| M      | 1 (PD)  | -0.867    | -1.000  |
| \_     | 2 (SD)  | -0.148    | -0.141  |
| M      | 2 (SD)  | -0.265    | -0.141  |

In PD, M noshuffle shows the weakest exploitation (−0.867): direct reciprocity
elevates Pop_1 enough to partially equalize fitness. Shuffling restores the
deterministic link (−1.000) by destroying partner memory.

In snowdrift, all correlations are weaker than in PD because the payoff floor
sustains high Pop_0 cooperation regardless of mechanism. M noshuffle shows
moderate coupling (−0.265) from reciprocity-driven elevation of Pop_1.

### Snowdrift-specific dynamics in Pop_1

The control leaves Pop_1 near 0.09 despite S1 > P1, because Pop_0's heavy
cooperation means defectors receive T1 = R1 (the shared benefit b arrives
regardless). Direct reciprocity partially overcomes this:

| Mech   | Pop_1 mean (all 210 cells) | Pop_1 at (0.1, 0.3) |
| ------ | --------------------------- | -------------------- |
| \_     | 0.091                       | 0.057                |
| M      | 0.191                       | 0.123                |

## Reciprocity Locus (M1) Dynamics

In the coevolving two-population mutualism, the frequency of the active reciprocity locus M1 under mechanism M frequently drops significantly below its nearly neutral control baseline (which drifts at approx. 0.49 - 0.51). Aggregated across every condition (3 dilemmas x 2 populations x 2 shuffle settings x 2 groupsizes = 5,040 cell-conditions over the 210-cell grid), M1 under M is suppressed below the control baseline in 3,701 of them. This suppression is driven by three distinct game-theoretic mechanisms depending on the dilemma type (including dilemma 0 where there is no social dilemma):

### Unwitting self-harm under no social dilemma (Dilemma 0)
In Dilemma 0 (Control baseline), there is no social dilemma because payoffs do not depend on the partner's move (focal fitness depends only on paying cost c to receive private benefit b). Since b > c, cooperating (paying c) is always privately optimal. However, under mechanism M, a reciprocating cooperator (C1M1) will mimic defection if paired with a mutant defector. 

Since mimicking defection does not affect the partner's payoff (no sharing of b), the reciprocator does not punish the defector; instead, it only hurts itself by forfeiting its own private payoff (earning K = 0.50 instead of K + b - c0 = 0.80). Always-cooperating C1M0 avoids this error and outcompetes C1M1. As the partner's cost c1 increases, cooperation in Pop_1 decays, producing more defectors. This increases the frequency of suboptimal mimicry events in Pop_0, driving Pop_0's M1 frequency down from 0.356 (at c1 = 0.12) to 0.068 (at c1 = 0.40), compared to the control baseline of approx. 0.50.

### Cross-population reciprocity hitchhiking (PD)
Along the c0 = 0.10 row in Dilemma 1 (PD), Pop_0 has a lower cost and readily evolves reciprocators (M1 approx. 0.749 at c1 = 0.30). Pop_0's reciprocators punish defection, forcing Pop_1 to cooperate (qBSeen = 0.616). Once Pop_1 is forced to cooperate, Pop_1 cooperators no longer need to perform the policing themselves. They can play Always Cooperate (C1M0) to save the 0.001 locus cost and let Pop_0's reciprocators handle defection. Pop_1 cooperators thus "hitchhike" on the reciprocity of Pop_0, driving Pop_1's M1 frequency down to 0.370 (compared to 0.500 in control).

### Suboptimal mimicry defection penalty (Snowdrift)
In Dilemma 2 (Snowdrift), cooperating when the partner defects is a dominant strategy (S > P). Under control, Pop_0 cooperates at ceiling (approx. 0.97) while Pop_1 free-rides and defects. Under mechanism M, a reciprocating cooperator (C1M1) in Pop_0 mimics Pop_1's defection, causing it to defect in subsequent rounds and earn mutual defection payoff (P = 0.50). An unconditional cooperator (C1M0) ignores the defection and continues cooperating, earning S = K + b - c0 = 0.78 (at c0 = 0.12). 

This imposes a severe game payoff penalty of 0.28 per round on C1M1. Selection acts extremely strongly against reciprocity in Pop_0, collapsing its M1 frequency to approx. 0.033 (only 3.3%) across all c1 values, compared to the nearly neutral control baseline of approx. 0.50.

## Shuffle effect on M mechanism

Shuffling destroys direct reciprocity in PD but is inconsequential in snowdrift,
where the cooperation floor is already high.

**Dilemma 1 (PD), Pop_0:**

| Condition        | (0.02, 0.38) | (0.10, 0.20) | (0.20, 0.38) |
| ---------------- | ------------ | ------------ | ------------ |
| noshuffle_gs128  | 0.312        | 0.869        | 0.360        |
| shuffle_gs128    | 0.207        | 0.051        | 0.025        |

At (c0=0.1, c1=0.2), M noshuffle achieves qBSeen_0 = 0.869 vs 0.051 with
shuffle — a 17× difference. The effect is largest at near-diagonal cells where
both populations can sustain iterated reciprocal cooperation.

**Dilemma 2 (snowdrift), Pop_0:**

| Condition        | (0.02, 0.38) | (0.10, 0.20) | (0.20, 0.38) |
| ---------------- | ------------ | ------------ | ------------ |
| noshuffle_gs128  | 0.953        | 0.945        | 0.929        |
| shuffle_gs128    | 0.973        | 0.968        | 0.960        |

Shuffle has no penalty and may slightly increase cooperation in snowdrift,
because the shared-benefit payoff structure does not depend on stable partner
pairings for Pop_0 to cooperate. Direct reciprocity's value in snowdrift is
concentrated in elevating Pop_1, not in bootstrapping Pop_0.

For M in snowdrift, shuffle reduces the exploitation correlation from −0.265
(noshuffle) to −0.141 (shuffle) — matching the control — because shuffling
removes the reciprocity-driven elevation of Pop_1 that creates cooperation
asymmetry.

## Indirect reciprocity under shuffle (IM, IJM)

The mutualism grid only ran IM and IJM under the shuffle conditions. This is
the informative regime: shuffling destroys direct reciprocity (M shuffle
collapses to the control), so any cooperation that IM and IJM sustain is
attributable to reputation signals (the I locus copies a new partner's last
move toward a third party; J copies the partner's lifetime cooperation
average). The pattern mirrors diagonal_reciprocity.md: reputation-based
reciprocity survives partner turnover where memory-based reciprocity cannot,
and the lifetime signal J (in IJM) is far more robust than the recent-only
signal I (in IM).

### Cooperation along the c0 = 0 column (shuffle, gs=128, Pop_0)

**Dilemma 1 (PD):**

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| M      | 0.529   | 0.518   | 0.538   | 0.523   | 0.512   |
| IM     | 0.938   | 0.841   | 0.742   | 0.682   | 0.625   |
| IJM    | 0.971   | 0.970   | 0.806   | 0.738   | 0.691   |

M under shuffle sits at the control drift level (≈ 0.5 at c0 = 0, where
T = R removes the temptation). IM and IJM recover high cooperation; IJM holds
near ceiling through c1 = 0.10 and stays above IM across the column.

**Dilemma 2 (snowdrift):**

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| M      | 0.912   | 0.969   | 0.972   | 0.971   | 0.973   |
| IM     | 0.942   | 0.950   | 0.953   | 0.950   | 0.953   |
| IJM    | 0.971   | 0.972   | 0.929   | 0.930   | 0.931   |

In snowdrift the floor already sustains Pop_0 near ceiling; IM and IJM add
little for the lower-cost population (the action is in Pop_1, below).

### Mean cooperation and role split across 210 cells (shuffle, gs=128)

| Mech   | Dilemma | Pop_0 | Pop_1 | Pop_0 > Pop_1 |
| ------ | ------- | ------ | ------ | --------------- |
| M      | 1 (PD)  | 0.108  | 0.026  | 210/210         |
| IM     | 1 (PD)  | 0.362  | 0.167  | 210/210         |
| IJM    | 1 (PD)  | 0.453  | 0.299  | 203/210         |
| M      | 2 (SD)  | 0.953  | 0.095  | 210/210         |
| IM     | 2 (SD)  | 0.927  | 0.199  | 210/210         |
| IJM    | 2 (SD)  | 0.917  | 0.378  | 204/210         |

For reference, M under noshuffle averages 0.637/0.551 (PD) and 0.926/0.191
(snowdrift). So in PD, shuffled IJM (0.453/0.299) recovers roughly two-thirds
of the cooperation that shuffled M loses, without restoring partner memory. In
snowdrift the IM/IJM benefit is concentrated in Pop_1: IJM lifts the
higher-cost population to 0.378 (vs 0.095 for shuffled M and 0.191 for
noshuffle M), the largest Pop_1 elevation of any pure-reciprocity mechanism.
The role split also begins to soften — IJM reverses it in 7/210 PD cells and
6/210 snowdrift cells, because lifetime reputation occasionally lets the
higher-cost population out-cooperate the lower-cost one.

### Sample cells (shuffle, gs=128)

| Mech   | Dilemma | (0.1, 0.2) Pop_0 | (0.1, 0.2) Pop_1 | (0.1, 0.3) Pop_0 | (0.1, 0.3) Pop_1 |
| ------ | ------- | ----------------- | ----------------- | ----------------- | ----------------- |
| IM     | 1 (PD)  | 0.511             | 0.286             | 0.258             | 0.115             |
| IJM    | 1 (PD)  | 0.911             | 0.846             | 0.258             | 0.141             |
| IM     | 2 (SD)  | 0.941             | 0.188             | 0.943             | 0.125             |
| IJM    | 2 (SD)  | 0.924             | 0.363             | 0.919             | 0.205             |

At mild PD asymmetry (c0=0.1, c1=0.2), IJM achieves near-symmetric high
cooperation (0.911/0.846) where IM manages only 0.511/0.286 — the lifetime
signal J is what bootstraps both populations together. By (0.1, 0.3) both
collapse toward the chooser-free reciprocity floor, confirming that indirect
reciprocity, like direct, has a cost-asymmetry ceiling.

## Single-run dynamics (asymmetric_c0_c1_1run)

Along the c0 = 0 column (mechanism M, noshuffle, PD, Pop_0), single-run
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

This single-run section is restricted to the available PD movie slice; the
snowdrift branch is not analyzed temporally here.

## Groupsize 4

### Cooperation landscape

Mechanism M, Pop_0, noshuffle:

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

| Mech   | Dilemma | Pop_0 | Pop_1 | Pop_0 > Pop_1 |
| ------ | ------- | ------ | ------ | --------------- |
| M      | 1 (PD)  | 0.636  | 0.551  | 209/210         |
| M      | 2 (SD)  | 0.926  | 0.191  | 210/210         |

In PD, the gs=4 landscape matches gs=128 qualitatively. In snowdrift, Pop_0
stays near ceiling.

### Exploitation at gs=4

| Mech   | Dilemma | noshuffle |
| ------ | ------- | --------- |
| M      | 1 (PD)  | -0.864    |
| M      | 2 (SD)  | -0.268    |

M noshuffle shows weaker coupling at gs=4 than gs=128 in PD (−0.864 vs
−0.867) because direct reciprocity elevates Pop_1 cooperation enough to
partially equalize fitness in the small group. Snowdrift correlations follow
the same weak pattern as gs=128.

### Shuffle effect at gs=4

Sample cells for mechanism M, Pop_0:

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
does not depend on stable partner pairings for Pop_0.

## Groupsize comparison (gs=4 vs gs=128)

Mechanism M is largely invariant to groupsize reduction:

**Dilemma 1 (PD), noshuffle:**

| c0   | c1   | Pop_0 gs=4 | Pop_0 gs=128 | Pop_1 gs=4 | Pop_1 gs=128 |
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
| M vs control (Pop_0) | 0.637 vs 0.103 — reciprocity essential                      | 0.926 vs 0.955 — marginal; snowdrift floor dominates |
| M vs control (Pop_1) | 0.551 vs 0.025 — large lift                                 | 0.191 vs 0.091 — moderate lift                   |
| Role split            | Pop_0 > Pop_1 in 210/210                                  | Pop_0 > Pop_1 in 210/210                       |
| M vs shuffle          | 17× penalty at (0.1, 0.2): 0.869 → 0.051                  | No penalty; shuffle ≈ noshuffle (~0.95) for Pop_0 |
| Exploitation (M)      | corr = −0.867 noshuffle; shuffle restores −1.000            | corr = −0.265 noshuffle; weaker than PD            |
| Indirect (shuffle)    | IJM 0.453/0.299, IM 0.362/0.167 — recover ~⅔ of shuffled M's loss | IJM lifts Pop_1 to 0.378 (largest pure-reciprocity Pop_1 lift) |
| gs=4 M (PD)           | Landscape matches gs=128; shuffle penalty severe (0.863 → 0.087) | Near ceiling; shuffle penalty absent         |
