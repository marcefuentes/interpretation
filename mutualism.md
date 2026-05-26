# Mutualism — Two-Population Partner Choice

## Overview

Mutualism is the primary study: two populations with potentially different
costs interact exclusively across populations. Population 0 has cost c0 and
population 1 has cost c1, with c0 < c1 always (the plotted triangular grid
constrains c1 > c0). Benefit b = 0.40 is fixed and K = 0.50.

Hamilton is the diagonal special case where c0 = c1. This file develops
the asymmetric general case: because c0 < c1, population 0 always has a
higher cooperation incentive (R0 − P0 = b − c0 > b − c1 = R1 − P1).

The parameter space is a strict upper-triangular 20 × 20 grid:
c0 ∈ {0.00, 0.02, …, 0.38} and c1 ∈ {0.02, 0.04, …, 0.40} with c0 < c1,
giving 210 cells. Only pop_2 (cross-population pairing) is present.

## Payoff structure

All payoffs use cross-benefit form: the benefit b is the contribution received
from the partner, while the cost c is paid by the focal individual.

### Dilemma 1 (PD, folder 1)

| Payoff | Pop 0          | Pop 1          |
| ------ | -------------- | -------------- |
| T      | K + b = 0.90   | K + b = 0.90   |
| R      | K + b - c0     | K + b - c1     |
| P      | K = 0.50       | K = 0.50       |
| S      | K - c0         | K - c1         |
| R - P  | b - c0         | b - c1         |

Since c0 < c1: R0 − P0 > R1 − P1. Population 0 always has a stronger
cooperation incentive than population 1.

### Dilemma 2 (snowdrift, folder 2)

| Payoff | Pop 0          | Pop 1          |
| ------ | -------------- | -------------- |
| T      | K + b = 0.90   | K + b = 0.90   |
| R      | K + b - c0/2   | K + b - c1/2   |
| P      | K = 0.50       | K = 0.50       |
| S      | K + b - c0     | K + b - c1     |
| R - P  | b - c0/2       | b - c1/2       |

In snowdrift, S > P for all c < 0.40 = b, so unilateral cooperation is always
better than mutual defection. This inherently selects for cooperation in both
populations without any mechanism.

## Cooperation landscape

Mechanism M, noshuffle, groupsize 128, dilemma 1 (PD), fset_0 (lower-cost
population):

| c0 \ c1 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------- | ------- | ------- | ------- | ------- |
| c0=0.00 | 0.916   | 0.642   | 0.555   | 0.490   |
| c0=0.10 | ---     | 0.878   | 0.670   | 0.213   |
| c0=0.20 | ---     | ---     | 0.781   | 0.228   |
| c0=0.30 | ---     | ---     | ---     | 0.195   |

Cooperation in the lower-cost population (fset_0) decreases as c1 increases:
even though pop_0's own incentive is high (c0 small), the partner bottleneck
limits achievable cooperation. When c1 is large, population 1 evolves few
choosers, which starves pop_0 of swap partners.

Along the c0 = 0 row (pop_0 has zero cost):

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| \_     | 0.485   | 0.499   | 0.497   | 0.492   | 0.493   |
| M      | 0.939   | 0.916   | 0.653   | 0.570   | 0.519   |
| P      | 0.957   | 0.866   | 0.794   | 0.737   | 0.693   |
| MP     | 0.962   | 0.867   | 0.756   | 0.689   | 0.618   |
| IMP    | 0.963   | 0.961   | 0.769   | 0.693   | 0.622   |
| IJMPQ  | 0.968   | 0.965   | 0.804   | 0.715   | 0.647   |

Even with c0 = 0 (no cost to cooperate), fset_0 cooperation declines as c1
rises, because the bottleneck is driven by the partner population's low R1 − P1.

## Role split: which population cooperates more?

For all 210 cells and all mechanisms tested (dilemma 1, noshuffle, gs=128),
fset_0 (lower-cost population) cooperates more than fset_1 in every single
cell. The split is deterministic: since c0 < c1 in every cell, pop_0 always
has higher R − P and therefore stronger selection for cooperation.

Mean qBSeen across all 210 cells:

| Mech   | Dilemma | fset_0 (lower c0) | fset_1 (higher c1) |
| ------ | ------- | ----------------- | ------------------ |
| \_     | 1       | 0.103             | 0.025              |
| \_     | 2       | 0.963             | 0.084              |
| M      | 1       | 0.637             | 0.550              |
| M      | 2       | 0.930             | 0.187              |
| P      | 1       | 0.472             | 0.146              |
| P      | 2       | 0.966             | 0.086              |
| MP     | 1       | 0.607             | 0.409              |
| MP     | 2       | 0.936             | 0.215              |
| IJMPQ  | 1       | 0.730             | 0.572              |
| IJMPQ  | 2       | 0.923             | 0.611              |

In snowdrift (folder 2), the control (\_ mechanism) shows qBSeen_0 = 0.963 but
qBSeen_1 = 0.084. Population 1 defects even under snowdrift conditions when it
has high cost — the snowdrift property (S > P) is still present for pop_1, but
the cooperation incentive R1 − P1 = b − c1/2 is weaker, and without mechanisms
the high-cost population free-rides on the cooperating partner.

## Exploitation: the paradox of success

Population 0 cooperates more but earns less. The correlation between
ΔqBSeen (qBSeen_0 − qBSeen_1) and Δfitness (w0 − w1) is strongly negative:

| Mech   | noshuffle | shuffle |
| ------ | --------- | ------- |
| \_     | -1.000    | -1.000  |
| M      | -0.833    | -1.000  |
| P      | -0.985    | -0.985  |
| IJMPQ  | -0.977    | -0.976  |

The control achieves a perfect −1.00 correlation because both cooperation and
fitness differences are determined purely by the payoff asymmetry (c0 < c1)
without any mechanism confounding the relationship.

The M mechanism shows weaker exploitation in noshuffle (−0.833): direct
reciprocity elevates cooperation in fset_1 enough to partially equalize
fitness, reducing the strength of the deterministic cooperation/fitness link.

## Mechanism comparison at selected cells

Cooperation at (c0=0.1, c1=0.2) and (c0=0.1, c1=0.3), noshuffle_128, PD:

| Mech   | (0.1, 0.2) fset_0 | (0.1, 0.2) fset_1 | (0.1, 0.3) fset_0 | (0.1, 0.3) fset_1 |
| ------ | ----------------- | ----------------- | ----------------- | ----------------- |
| \_     | 0.048             | 0.026             | 0.048             | 0.017             |
| M      | 0.878             | 0.846             | 0.670             | 0.600             |
| P      | 0.607             | 0.183             | 0.375             | 0.101             |
| MP     | 0.729             | 0.457             | 0.478             | 0.257             |
| MPQ    | 0.691             | 0.304             | 0.484             | 0.182             |
| IMP    | 0.948             | 0.944             | 0.505             | 0.248             |
| IJMPQ  | 0.957             | 0.956             | 0.571             | 0.289             |

At mild asymmetry (c0=0.1, c1=0.2; close to diagonal), IMP and IJMPQ achieve
near-symmetric high cooperation in both populations (0.944–0.957). The role
split nearly disappears: IMP fset_0 = 0.948, fset_1 = 0.944. This is the
closest approach to mutualistic reciprocity — both populations cooperate at
nearly identical high rates.

At high asymmetry (c0=0.1, c1=0.3), IJMPQ fset_0 = 0.571 and fset_1 = 0.289 —
cooperation persists but the asymmetry is large. No mechanism achieves
symmetric cooperation when the cost gap is wide.

### Exploitation at the cell level (P mechanism, c0=0.1)

| c1   | qBSeen_0 | qBSeen_1 | w\_0  | w\_1  |
| ---- | -------- | -------- | ----- | ----- |
| 0.12 | 0.777    | 0.278    | 0.531 | 0.776 |
| 0.16 | 0.679    | 0.223    | 0.519 | 0.734 |
| 0.20 | 0.607    | 0.183    | 0.511 | 0.705 |
| 0.30 | 0.375    | 0.101    | 0.501 | 0.618 |
| 0.40 | 0.177    | 0.044    | 0.498 | 0.552 |

Population 0 cooperates 3–6× more than population 1, yet earns less fitness.
At (c0=0.1, c1=0.12), w\_1/w\_0 = 0.776/0.531 = 1.46 (population 1 earns 46%
more fitness despite cooperating at only 36% of population 0's level). As c1
increases and cooperation shrinks in both populations, the exploitation ratio
narrows: at (c0=0.1, c1=0.40), w\_1/w\_0 = 0.552/0.498 = 1.11.

### Mutual cooperation (IMP mechanism, c0=0.1)

| c1   | qBSeen_0 | qBSeen_1 | w\_0  | w\_1  |
| ---- | -------- | -------- | ----- | ----- |
| 0.12 | 0.954    | 0.952    | 0.775 | 0.775 |
| 0.16 | 0.949    | 0.946    | 0.761 | 0.747 |
| 0.20 | 0.948    | 0.944    | 0.750 | 0.720 |
| 0.30 | 0.505    | 0.248    | 0.547 | 0.626 |

IMP eliminates the cooperation asymmetry and the fitness gap at mild cost
differences. At (c0=0.1, c1=0.12), both populations cooperate at 0.95 and earn
identical fitness. This is the mutualistic equilibrium: all-mechanism
cooperation enforces symmetric payoffs. As c1 increases beyond 0.20 the
enforcement breaks down and the IMP advantage over simpler mechanisms erodes.

## Shuffle effect on M mechanism

Shuffling destroys direct reciprocity just as in Hamilton:

| Condition        | (0.02, 0.38) | (0.10, 0.20) | (0.20, 0.38) |
| ---------------- | ------------ | ------------ | ------------ |
| shuffle_gs128    | 0.218        | 0.051        | 0.025        |
| noshuffle_gs128  | 0.305        | 0.878        | 0.360        |

At (c0=0.1, c1=0.2), the M mechanism noshuffle achieves qBSeen_0 = 0.878
vs 0.051 with shuffle — an 17× difference. The effect is particularly large
at near-diagonal cells (mild asymmetry) where both populations have
cooperative incentives and can sustain iterated reciprocal cooperation.
At high asymmetry (c0=0.02, c1=0.38), the noshuffle advantage is smaller
(0.305 vs 0.218) because even without shuffling, population 1's low incentive
limits what M can achieve.

## Snowdrift dilemma summary

In snowdrift (folder 2), all mechanisms push fset_0 cooperation to near-maximum:

| Mech   | (0.1, 0.3) fset_0 | (0.1, 0.3) fset_1 |
| ------ | ----------------- | ----------------- |
| \_     | 0.972             | 0.059             |
| P      | 0.972             | 0.057             |
| M      | 0.944             | 0.120             |
| MP     | 0.948             | 0.125             |
| IJMPQ  | 0.900             | 0.292             |

The remarkable finding is fset_1 in snowdrift. Population 1 cooperates at only
0.057–0.120 even though the snowdrift property (S1 > P1) should incentivize
cooperation. The partner bottleneck from the opposite direction: population 0
cooperates so heavily that population 1 always receives b regardless (T1 = R1
for defectors when the partner cooperates), eliminating any marginal benefit for
pop_1 to cooperate. IJMPQ partially corrects this, bringing fset_1 to 0.292.

## Single-run dynamics (mutualism_1run)

Along the c0 = 0 row (mechanism M, noshuffle, PD, fset_0), single-run
trajectories show high but variable cooperation:

| c1   | Range | Representative trajectory              |
| ---- | ----- | -------------------------------------- |
| 0.02 | 0.951 | 0.934 → 0.948 → 0.929 → 0.951         |
| 0.10 | 0.940 | 0.924 → 0.914 → 0.932 → 0.940         |
| 0.18 | 0.680 | 0.680 → 0.569 → 0.626 → 0.658         |
| 0.20 | 0.714 | 0.589 → 0.632 → 0.714 → 0.702         |

The trajectory ranges increase as c1 increases (the cooperation is less stable
at higher c1), while still showing persistent non-zero cooperation even at
c1 = 0.20 for mechanism M. This confirms that the multi-run averages represent
genuine intermediate cooperation levels, not averaging of all-or-nothing states.

## Groupsize comparison (gs=4 vs gs=128)

All comparisons are PD (dilemma 1), noshuffle, pop_2, fset_0 (lower-cost
population) unless noted.

### Partner choice (P) — collapse at gs=4 even for mild asymmetry

The P mechanism fails at gs=4 for all but the smallest cost cells. Near the
diagonal where both costs are similar, the threshold drops to c0 ≈ 0.08:

| c0   | c1   | gs=4  | gs=128 |
| ---- | ---- | ----- | ------ |
| 0.00 | 0.02 | 0.928 | 0.957  |
| 0.06 | 0.08 | 0.832 | 0.854  |
| 0.08 | 0.10 | 0.765 | 0.810  |
| 0.10 | 0.12 | 0.059 | 0.777  |
| 0.20 | 0.22 | 0.027 | 0.635  |
| 0.30 | 0.32 | 0.018 | 0.494  |

This mirrors the hamilton gs=4 finding exactly: the chooser bottleneck is
catastrophically worsened by small groups, and partner choice becomes
effectively non-functional throughout most of the parameter space.

### IMP and IJMPQ — broadly similar to gs=128, better at large asymmetries

Unlike partner choice, the reciprocity-based mechanisms (IMP, IJMPQ) are
robust to groupsize reduction. At mild asymmetry they match gs=128 closely,
and at large asymmetry they can exceed gs=128 in the high-cost population
(fset_1):

| Mechanism | c0   | c1   | fset_0 gs=4 | fset_0 gs=128 | fset_1 gs=4 | fset_1 gs=128 |
| --------- | ---- | ---- | ----------- | ------------- | ----------- | ------------- |
| IMP       | 0.10 | 0.12 | 0.944       | 0.954         | 0.941       | 0.952         |
| IMP       | 0.10 | 0.30 | 0.597       | 0.505         | 0.450       | 0.248         |
| IMP       | 0.20 | 0.30 | 0.865       | 0.639         | 0.851       | 0.510         |
| IJMPQ     | 0.10 | 0.12 | 0.957       | 0.963         | 0.955       | 0.962         |
| IJMPQ     | 0.10 | 0.30 | 0.544       | 0.571         | 0.327       | 0.289         |
| IJMPQ     | 0.20 | 0.30 | 0.919       | 0.930         | 0.916       | 0.928         |

At c0 = 0.20, c1 = 0.30 the IMP mechanism shows the largest gs=4 advantage:
fset_1 (high-cost population) reaches 0.851 at gs=4 vs 0.510 at gs=128. Small
groups allow the high-cost cooperators to interact more repeatedly with the
same partners, making direct reciprocity (M, I loci) more effective at
sustaining cooperation despite the cost disadvantage.

### Summary

| Mechanism | gs=4 effect relative to gs=128           |
| --------- | ---------------------------------------- |
| \_        | Identical                                |
| M         | Negligible difference                    |
| P         | Collapses; only works at c0,c1 < 0.10    |
| IMP       | Broadly similar; better at large asymmetry |
| IJMPQ     | Broadly similar; better at large asymmetry |
