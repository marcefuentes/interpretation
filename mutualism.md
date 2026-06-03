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
giving 210 cells. Only pop_2 (cross-population pairing) is present. Analysis
covers groupsize 128 noshuffle (primary) and groupsize 4 (dedicated section
plus comparison); shuffle conditions are included in both.

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

Since c0 < c1 in every cell: R0 − P0 = b − c0 > R1 − P1 = b − c1. Population
0 always has a stronger cooperation incentive than population 1. The role split
is therefore deterministic: fset_0 (lower-cost population) cooperates more in
100% of the 210 cells for all mechanisms tested.

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
| c0=0.00 | 0.918   | 0.633   | 0.545   | 0.484   |
| c0=0.10 | ---     | 0.869   | 0.680   | 0.215   |
| c0=0.20 | ---     | ---     | 0.780   | 0.232   |
| c0=0.30 | ---     | ---     | ---     | 0.197   |

Cooperation in the lower-cost population (fset_0) decreases as c1 increases:
even though pop_0's own incentive is high (c0 small), the partner bottleneck
limits achievable cooperation. When c1 is large, population 1 evolves few
choosers, which starves pop_0 of swap partners.

Along the c0 = 0 row (pop_0 has zero cost):

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| \_     | 0.487   | 0.498   | 0.500   | 0.502   | 0.500   |
| M      | 0.941   | 0.918   | 0.654   | 0.569   | 0.513   |
| P      | 0.961   | 0.864   | 0.791   | 0.735   | 0.710   |
| MP     | 0.961   | 0.867   | 0.756   | 0.689   | 0.635   |
| IMP    | 0.961   | 0.960   | 0.770   | 0.685   | 0.613   |
| IJMPQ  | 0.969   | 0.966   | 0.802   | 0.716   | 0.651   |

Even with c0 = 0 (no cost to cooperate), fset_0 cooperation declines as c1
rises, because the bottleneck is driven by the partner population's low R1 − P1.

## The partner choice bottleneck

Despite pop_0's cooperation incentive, its achievable cooperation is capped by
a bottleneck: partner-choice swaps require C1P1 individuals on both sides of
the exchange. Population 1's low R1 − P1 = b − c1 means it evolves few C1P1
individuals. Without C1P1 counterparts in pop_1, pop_0 cannot execute swaps
even though it has strong incentive to cooperate.

Along the c0 = 0 row (P mechanism, noshuffle, PD) — where pop_0 has the
maximum possible incentive (R0 − P0 = 0.40) — cooperation still falls as c1
rises because the bottleneck is entirely on the partner side:

| c1   | R1-P1 | q\_fset0 | q\_fset1 |
| ---- | ----- | -------- | -------- |
| 0.02 | 0.38  | 0.961    | 0.642    |
| 0.10 | 0.30  | 0.864    | 0.122    |
| 0.20 | 0.20  | 0.770    | 0.054    |
| 0.30 | 0.10  | 0.722    | 0.033    |
| 0.40 | 0.00  | 0.672    | 0.023    |

Pop_0's cooperation falls from 0.961 to 0.672 as c1 rises from 0.02 to 0.40
— not because pop_0's own incentive changes (R0 − P0 = 0.40 throughout), but
because pop_1's C1P1 frequency collapses with rising c1. The correlation
between qBSeen_0 and R1 − P1 = b − c1 across all 210 cells is 0.90; the
correlation with the focal population's own incentive R0 − P0 = b − c0 is
0.67. The partner's incentive explains more variance than the focal's own.



For all 210 cells and all mechanisms tested (dilemma 1, noshuffle, gs=128),
fset_0 (lower-cost population) cooperates more than fset_1 in every single
cell. The split is deterministic: since c0 < c1 in every cell, pop_0 always
has higher R − P and therefore stronger selection for cooperation.

Mean qBSeen across all 210 cells:

| Mech   | Dilemma | fset_0 (lower c0) | fset_1 (higher c1) |
| ------ | ------- | ----------------- | ------------------ |
| \_     | 1       | 0.103             | 0.025              |
| \_     | 2       | 0.955             | 0.091              |
| M      | 1       | 0.637             | 0.551              |
| M      | 2       | 0.926             | 0.191              |
| P      | 1       | 0.472             | 0.146              |
| P      | 2       | 0.956             | 0.096              |
| MP     | 1       | 0.606             | 0.410              |
| MP     | 2       | 0.931             | 0.220              |
| IJMPQ  | 1       | 0.729             | 0.573              |
| IJMPQ  | 2       | 0.923             | 0.609              |

In snowdrift (folder 2), the control (\_ mechanism) shows qBSeen_0 = 0.955 but
qBSeen_1 = 0.091. Population 1 defects even under snowdrift conditions when it
has high cost — the snowdrift property (S > P) is still present for pop_1, but
the cooperation incentive R1 − P1 = b − c1/2 is weaker, and without mechanisms
the high-cost population free-rides on the cooperating partner.

## Exploitation: the paradox of success

Population 0 cooperates more but earns less. The correlation between
ΔqBSeen (qBSeen_0 − qBSeen_1) and Δfitness (w0 − w1) is strongly negative:

| Mech   | noshuffle | shuffle |
| ------ | --------- | ------- |
| \_     | -1.000    | -1.000  |
| M      | -0.867    | -1.000  |
| P      | -0.986    | -0.986  |
| IJMPQ  | -0.948    | -0.963  |

The control achieves a perfect −1.00 correlation because both cooperation and
fitness differences are determined purely by the payoff asymmetry (c0 < c1)
without any mechanism confounding the relationship.

The M mechanism shows weaker exploitation in noshuffle (−0.867): direct
reciprocity elevates cooperation in fset_1 enough to partially equalize
fitness, reducing the strength of the deterministic cooperation/fitness link.

Population 0 has lower fitness in 100% of the 210 cells under the P mechanism
(noshuffle, PD). The mean fitness deficit is 0.140 (pop_1 earns 0.140 more
than pop_0 on average). The deficit does not vary strongly with asymmetry:
mean deficit is 0.148 at low asymmetry (Δc ≤ 0.10) and 0.141 at high
asymmetry (Δc > 0.20). Exploitation is persistent across the entire parameter
space, not concentrated at specific cost ratios.

## Genotype composition

Under the P mechanism (noshuffle, PD), averaged across all 210 cells:

| Genotype | Pop_0 (lower cost) | Pop_1 (higher cost) |
| -------- | ------------------ | ------------------- |
| C1P1     | 0.382              | 0.126               |
| C1P0     | 0.090              | 0.020               |
| C0P1     | 0.304              | 0.442               |
| qBSeen   | 0.472              | 0.146               |

Pop_0 is dominated by C1P1 (active choosers) and C0P1. Pop_1 is dominated by
C0P1 (0.443) — defectors carrying the P1 allele silently. This is the
hitchhiking pattern: mutations from C1P1 generate C0P1 that persist as neutral
carriers. The high C0P1 in pop_1 shows that P1 alleles circulate throughout
both populations even though only pop_0's C1P1 individuals actually choose.

In the high-cooperation region (c0 < 0.10, c1 < 0.20): pop_0 C1P1 rises
to 0.58 while pop_0 C1P0 averages ≈ 0.22 (roughly 22% of cooperators are
non-chooser free-riders on the cooperator pool). At high asymmetry
(c1 > 0.30), pop_0 C1P0 falls to near zero — when c1 is large, only C1P1
individuals can sustain cooperation and non-chooser cooperators are selected
out.



Cooperation at (c0=0.1, c1=0.2) and (c0=0.1, c1=0.3), noshuffle_128, PD:

| Mech   | (0.1, 0.2) fset_0 | (0.1, 0.2) fset_1 | (0.1, 0.3) fset_0 | (0.1, 0.3) fset_1 |
| ------ | ----------------- | ----------------- | ----------------- | ----------------- |
| \_     | 0.051             | 0.026             | 0.047             | 0.018             |
| M      | 0.869             | 0.830             | 0.680             | 0.616             |
| P      | 0.600             | 0.187             | 0.369             | 0.101             |
| MP     | 0.729             | 0.465             | 0.478             | 0.248             |
| MPQ    | 0.701             | 0.317             | 0.472             | 0.172             |
| IMP    | 0.947             | 0.946             | 0.509             | 0.255             |
| IJMPQ  | 0.957             | 0.957             | 0.574             | 0.293             |

At mild asymmetry (c0=0.1, c1=0.2; close to diagonal), IMP and IJMPQ achieve
near-symmetric high cooperation in both populations (0.946–0.957). The role
split nearly disappears: IMP fset_0 = 0.947, fset_1 = 0.946. This is the
closest approach to mutualistic reciprocity — both populations cooperate at
nearly identical high rates.

At high asymmetry (c0=0.1, c1=0.3), IJMPQ fset_0 = 0.574 and fset_1 = 0.293 —
cooperation persists but the asymmetry is large. No mechanism achieves
symmetric cooperation when the cost gap is wide.

### Exploitation at the cell level (P mechanism, c0=0.1)

| c1   | qBSeen_0 | qBSeen_1 | w\_0  | w\_1  |
| ---- | -------- | -------- | ----- | ----- |
| 0.12 | 0.759    | 0.304    | 0.544 | 0.765 |
| 0.16 | 0.694    | 0.216    | 0.515 | 0.742 |
| 0.20 | 0.600    | 0.187    | 0.513 | 0.701 |
| 0.30 | 0.369    | 0.101    | 0.502 | 0.616 |
| 0.40 | 0.183    | 0.046    | 0.498 | 0.553 |

Population 0 cooperates 2–4× more than population 1, yet earns less fitness.
At (c0=0.1, c1=0.12), w\_1/w\_0 = 0.765/0.544 = 1.41 (population 1 earns 41%
more fitness despite cooperating at only 40% of population 0's level). As c1
increases and cooperation shrinks in both populations, the exploitation ratio
narrows: at (c0=0.1, c1=0.40), w\_1/w\_0 = 0.553/0.498 = 1.11.

### Mutual cooperation (IMP mechanism, c0=0.1)

| c1   | qBSeen_0 | qBSeen_1 | w\_0  | w\_1  |
| ---- | -------- | -------- | ----- | ----- |
| 0.12 | 0.953    | 0.952    | 0.784 | 0.765 |
| 0.16 | 0.951    | 0.950    | 0.783 | 0.727 |
| 0.20 | 0.947    | 0.946    | 0.782 | 0.688 |
| 0.30 | 0.509    | 0.255    | 0.549 | 0.626 |

IMP eliminates the cooperation asymmetry at mild cost differences. At
(c0=0.1, c1=0.12), both populations cooperate at 0.95 with nearly equal
fitness (w0 = 0.784, w1 = 0.765). This is the mutualistic equilibrium: all-mechanism
cooperation enforces near-symmetric payoffs. As c1 increases beyond 0.20 the
enforcement breaks down and the IMP advantage over simpler mechanisms erodes.

## Shuffle effect on M mechanism

Shuffling destroys direct reciprocity just as in Hamilton:

| Condition        | (0.02, 0.38) | (0.10, 0.20) | (0.20, 0.38) |
| ---------------- | ------------ | ------------ | ------------ |
| shuffle_gs128    | 0.207        | 0.051        | 0.025        |
| noshuffle_gs128  | 0.312        | 0.869        | 0.360        |

At (c0=0.1, c1=0.2), the M mechanism noshuffle achieves qBSeen_0 = 0.869
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
| \_     | 0.972             | 0.057             |
| P      | 0.972             | 0.061             |
| M      | 0.945             | 0.123             |
| MP     | 0.945             | 0.123             |
| IJMPQ  | 0.896             | 0.293             |

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

## Groupsize 4

All mutualism runs use pop_2 only. The triangular 210-cell grid is unchanged;
groupsize 4 means four individuals per population in each fixed group. Unless
noted, the tables below are PD (dilemma 1), noshuffle, fset_0 (lower-cost
population).

### Cooperation landscape (gs=4)

Mechanism M, fset_0:

| c0 \ c1 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------- | ------- | ------- | ------- | ------- |
| c0=0.00 | 0.915   | 0.643   | 0.541   | 0.485   |
| c0=0.10 | ---     | 0.863   | 0.684   | 0.211   |
| c0=0.20 | ---     | ---     | 0.777   | 0.236   |
| c0=0.30 | ---     | ---     | ---     | 0.188   |

The landscape is broadly similar to gs=128: cooperation in fset_0 falls as c1
rises because the partner bottleneck limits achievable cooperation. Along the
c0 = 0 row, fset_0 still declines from 0.915 (c1 = 0.10) to 0.485 (c1 = 0.40)
even though pop_0 pays no cost.

Mean qBSeen across all 210 cells (PD, noshuffle):

| Mech   | fset_0 (lower c0) | fset_1 (higher c1) | fset_0 > fset_1 |
| ------ | ----------------- | ------------------ | --------------- |
| \_     | 0.103             | 0.025              | 208/210 cells   |
| M      | 0.636             | 0.551              | 209/210         |
| P      | 0.204             | 0.046              | 209/210         |
| IMP    | 0.709             | 0.600              | 208/210         |
| IJMPQ  | 0.740             | 0.617              | 190/210         |

The role split (lower-cost population cooperates more) is almost as universal
at gs=4 as at gs=128. IJMPQ is the exception with 20 cells where fset_1 exceeds
fset_0, typically at large asymmetry where the high-cost population benefits
from repeated interaction in the small closed group.

### Partner bottleneck at gs=4

Along c0 = 0 (P mechanism, noshuffle):

| c1   | qBSeen fset_0 | qBSeen fset_1 |
| ---- | ------------- | ------------- |
| 0.02 | 0.932         | 0.620         |
| 0.10 | 0.849         | 0.284         |
| 0.20 | 0.743         | 0.029         |
| 0.30 | 0.680         | 0.017         |
| 0.40 | 0.632         | 0.013         |

Pop_0 cooperation falls as c1 rises even with zero own cost — the same
bottleneck logic as gs=128. Partner choice itself barely functions beyond mild
asymmetry: at (c0, c1) = (0.10, 0.30), qBSeen = 0.049 for the P mechanism
versus 0.684 for M and 0.857 for IMP at (0.20, 0.30).

### Exploitation at gs=4

Correlation between ΔqBSeen and Δfitness (PD):

| Mech   | noshuffle | shuffle |
| ------ | --------- | ------- |
| \_     | -1.000    | -1.000  |
| M      | -0.864    | -0.999  |
| P      | -0.998    | -0.998  |
| IJMPQ  | -0.936    | -0.946  |

The exploitation paradox (more cooperation, lower fitness in fset_0) persists at
gs=4. M noshuffle shows weaker coupling (−0.864 vs −0.867 at gs=128) because
direct reciprocity elevates fset_1 cooperation enough to partially equalize
fitness in the small group.

### Shuffle effect at gs=4

Sample cells for mechanism M, fset_0:

| Condition       | (0.02, 0.38) | (0.10, 0.20) | (0.20, 0.38) |
| --------------- | ------------ | ------------ | ------------ |
| noshuffle_gs4   | 0.301        | 0.863        | 0.363        |
| shuffle_gs4     | 0.377        | 0.087        | 0.034        |

The shuffle penalty on M is severe at gs=4 (0.863 → 0.087 at (0.10, 0.20)),
comparable to gs=128 (0.869 → 0.051). Small groups do not rescue direct
reciprocity under random reshuffling.

## Groupsize comparison (gs=4 vs gs=128)

All comparisons are PD (dilemma 1), noshuffle, pop_2, fset_0 (lower-cost
population) unless noted.

### Partner choice (P) — collapse at gs=4 even for mild asymmetry

The P mechanism fails at gs=4 for all but the smallest cost cells. Near the
diagonal where both costs are similar, the threshold drops to c0 ≈ 0.08:

| c0   | c1   | gs=4  | gs=128 |
| ---- | ---- | ----- | ------ |
| 0.00 | 0.02 | 0.932 | 0.961  |
| 0.06 | 0.08 | 0.820 | 0.845  |
| 0.08 | 0.10 | 0.778 | 0.780  |
| 0.10 | 0.12 | 0.059 | 0.759  |
| 0.20 | 0.22 | 0.026 | 0.636  |
| 0.30 | 0.32 | 0.016 | 0.500  |

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
| IMP       | 0.10 | 0.12 | 0.943       | 0.953         | 0.943       | 0.952         |
| IMP       | 0.10 | 0.30 | 0.585       | 0.509         | 0.437       | 0.255         |
| IMP       | 0.20 | 0.30 | 0.857       | 0.637         | 0.844       | 0.519         |
| IJMPQ     | 0.10 | 0.12 | 0.955       | 0.963         | 0.954       | 0.963         |
| IJMPQ     | 0.10 | 0.30 | 0.545       | 0.574         | 0.320       | 0.293         |
| IJMPQ     | 0.20 | 0.30 | 0.920       | 0.932         | 0.917       | 0.931         |

At c0 = 0.20, c1 = 0.30 the IMP mechanism shows the largest gs=4 advantage:
fset_1 (high-cost population) reaches 0.844 at gs=4 vs 0.519 at gs=128. Small
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

## Summary

| Topic                        | Key finding                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| Parameter space              | 210-cell strict upper triangle: c0 < c1, both in [0.00, 0.40], b = 0.40, K = 0.50   |
| Cross-benefit payoffs (PD)   | R0-P0 = b-c0, R1-P1 = b-c1; higher-cost pop always has weaker incentive              |
| Role split                   | fset_0 cooperates more in 100% of cells for all mechanisms                            |
| Bottleneck                   | Pop_0 cooperation limited by pop_1's R1-P1; partner incentive explains more than own |
| Exploitation (P mechanism)   | Pop_0 lower fitness in 100% of cells; mean deficit = 0.140                           |
| Exploitation correlation     | Corr(ΔqBSeen, Δfitness) = -0.986 (P) to -1.000 (control)                            |
| Genotypes pop_0              | Mean C1P1 = 0.382, C0P1 = 0.304, C1P0 = 0.090 (hitchhiking in both pops)            |
| Genotypes pop_1              | Dominated by C0P1 = 0.442 (silent hitchhikers) + low C1P1 = 0.126                   |
| Mutualistic equilibrium      | IMP at (c0=0.1, c1=0.12): both pops ≈ 0.95; fitness nearly equal                    |
| Snowdrift (folder 2)         | fset_0 near ceiling; fset_1 defects despite S > P (exploited by pop_0 cooperation)  |
| Shuffle effect on M          | 17× difference at (c0=0.1, c1=0.2): noshuffle = 0.869, shuffle = 0.051              |
| gs=4 P mechanism             | Collapses by c0/c1 ≈ 0.10 — bottleneck catastrophic in small groups                 |
| gs=4 IMP/IJMPQ               | Broadly similar to gs=128; better at large asymmetry (fset_1 gains most)             |
