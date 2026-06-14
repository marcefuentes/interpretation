# Mutualism — Combined Mechanisms

Analysis of mechanisms that combine partner choice with reciprocity: **MP**,
**MPQ**, **IMP**, and **IJMPQ**. Pure partner choice (P) is in
**mutualism_partner_choice.md**; pure reciprocity (M, IM, IJM) is in
**mutualism_reciprocity.md**.

| Mechanism | Loci        | Components                          |
| --------- | ----------- | ----------------------------------- |
| MP        | C, M, P     | Direct reciprocity + partner choice |
| MPQ       | C, M, P, Q  | MP + lifetime partner-choice memory |
| IMP       | C, I, M, P  | Indirect + direct reciprocity + PC  |
| IJMPQ     | C, I, J, M, P, Q | Full stack with lifetime memory |

Hamilton (c0 = c1) is the diagonal special case; see **hamilton_combined.md**.

## Overview

See **[mutualism.md](mutualism.md#overview)** for the common model overview and parameter space.

## Cooperation along c0 = 0 column

Mechanisms add partner-choice sorting on top of reciprocity. Along the c0 = 0
column (noshuffle, gs=128):

**Dilemma 1 (PD):**

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| M      | 0.941   | 0.918   | 0.654   | 0.569   | 0.513   |
| P      | 0.961   | 0.864   | 0.791   | 0.735   | 0.710   |
| MP     | 0.961   | 0.867   | 0.756   | 0.689   | 0.635   |
| IMP    | 0.961   | 0.960   | 0.770   | 0.685   | 0.613   |
| IJMPQ  | 0.969   | 0.966   | 0.802   | 0.716   | 0.651   |

**Dilemma 2 (snowdrift):**

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| M      | 0.927   | 0.950   | 0.951   | 0.952   | 0.955   |
| P      | 0.961   | 0.977   | 0.977   | 0.977   | 0.978   |
| MP     | 0.956   | 0.953   | 0.954   | 0.955   | 0.954   |
| IMP    | 0.951   | 0.950   | 0.929   | 0.930   | 0.932   |
| IJMPQ  | 0.967   | 0.964   | 0.963   | 0.912   | 0.912   |

In PD, IMP and IJMPQ exceed both M and P alone at moderate c1. In snowdrift,
combined mechanisms add little for Pop_0 (already at ceiling); the benefit
is elevating Pop_1.

## Cooperation Boost vs. Asymmetry Effects (pop_2 Role Splits)

Mean qBSeen across all 210 cells (noshuffle, gs=128):

| Mech   | Dilemma | Pop_0 | Pop_1 | Pop_0 > Pop_1 |
| ------ | ------- | ------ | ------ | --------------- |
| MP     | 1 (PD)  | 0.606  | 0.410  | 210/210         |
| IMP    | 1 (PD)  | 0.670  | 0.505  | 203/210         |
| IJMPQ  | 1 (PD)  | 0.729  | 0.573  | 198/210         |
| MP     | 2 (SD)  | 0.931  | 0.220  | 210/210         |
| IMP    | 2 (SD)  | 0.915  | 0.391  | 196/210         |
| IJMPQ  | 2 (SD)  | 0.923  | 0.609  | 176/210         |

Combining partner choice (P) and reciprocity (M, IMP, IJMPQ) in Mutualism demonstrates how reciprocity acts to reduce the asymmetry driven by partner choice:

- **Prisoner's Dilemma (PD):** 
  - Under partner choice alone (P), asymmetry is high (0.325) because Pop_0 cooperates at 0.472 while Pop_1 cooperates at only 0.146.
  - Adding reciprocity (**IMP** and **IJMPQ**) has the major effect of **decreasing asymmetry** relative to P alone (falling from 0.325 to 0.165 for IMP, and to 0.156 for IJMPQ), partially eroding the deterministic role split at mild asymmetry.
  - This reduction is achieved by **increasing cooperation in Pop_1** (from 0.146 under P to 0.573 under IJMPQ, a +0.427 boost). Conditional reciprocity forces Pop_1 to coevolve cooperation to access partners, preventing the extreme exploitation asymmetry of partner choice alone.
- **Snowdrift:** 
  - Partner choice alone (P) leaves asymmetry almost unchanged compared to the control (0.860 vs. 0.864).
  - Combining them (**IMP** and **IJMPQ**) has a massive major effect of **decreasing asymmetry** (average asymmetry collapses from 0.864 in control to 0.524 under IMP, and to 0.313 under IJMPQ), which brings Pop_1 to a mean of 0.609 (vs. 0.091 control) and reverses the role split in 34 out of 210 cells.
  - The asymmetry drop is driven entirely by **elevating Pop_1's cooperation** (from 0.091 under control to 0.391 under IMP, and a massive 0.609 under IJMPQ). Reciprocity resolves the free-riding bottleneck that partner choice alone could not affect.

### Shuffling Shifts the Balance Between Partner Choice and Reciprocity

Under shuffling, direct reciprocity (M) is completely disabled. This allows partner choice (P) to dominate the combined mechanisms, causing cooperation to drop and asymmetry to surge:
- For **IMP**, where M is shuffled, Pop_1 cooperation drops from 0.505 (noshuffle) to 0.264 (shuffle), and asymmetry surges from 0.165 to 0.303, returning close to partner choice's baseline asymmetry of 0.325.
- For **IJMPQ**, Pop_1 cooperation remains much higher at 0.442 and asymmetry is kept lower at 0.286. Partner choice and indirect reciprocity both run every round regardless of shuffle (the simulation loop calls choose_partner after shuffle_partners; only direct reciprocity M, which requires partner == oldpartner, is disabled). Isolating the lifetime loci shows the recovery over IMP is carried specifically by **J** (lifetime indirect reciprocity): IM → IJM lifts Pop_1 by +0.133 under shuffle, whereas Q (MP → MPQ) adds only +0.007. The lifetime cooperation average (qBSeen_lt) that J reads is robust to the partner turnover that makes the recent indirect signal (I) noisy. (The M1 allele frequency actually rises under shuffle in the full IJMPQ stack, but M is behaviorally inert there — it fires only when partner == oldpartner — so this is neutral drift / hitchhiking on the active loci, not direct reciprocity doing work.)

## Mechanism comparison at sample cells

Cooperation at (c0=0.1, c1=0.2) and (c0=0.1, c1=0.3), noshuffle, gs=128:

**Dilemma 1 (PD):**

| Mech   | (0.1, 0.2) Pop_0 | (0.1, 0.2) Pop_1 | (0.1, 0.3) Pop_0 | (0.1, 0.3) Pop_1 |
| ------ | ----------------- | ----------------- | ----------------- | ----------------- |
| M      | 0.869             | 0.830             | 0.680             | 0.616             |
| P      | 0.600             | 0.187             | 0.369             | 0.101             |
| MP     | 0.729             | 0.465             | 0.478             | 0.248             |
| MPQ    | 0.701             | 0.317             | 0.472             | 0.172             |
| IMP    | 0.947             | 0.946             | 0.509             | 0.255             |
| IJMPQ  | 0.957             | 0.957             | 0.574             | 0.293             |

**Dilemma 2 (snowdrift):**

| Mech   | (0.1, 0.2) Pop_0 | (0.1, 0.2) Pop_1 | (0.1, 0.3) Pop_0 | (0.1, 0.3) Pop_1 |
| ------ | ----------------- | ----------------- | ----------------- | ----------------- |
| M      | 0.945             | 0.188             | 0.945             | 0.123             |
| P      | 0.973             | 0.089             | 0.972             | 0.061             |
| MP     | 0.948             | 0.194             | 0.945             | 0.123             |
| MPQ    | 0.948             | 0.204             | 0.948             | 0.128             |
| IMP    | 0.919             | 0.342             | 0.921             | 0.192             |
| IJMPQ  | 0.962             | 0.962             | 0.896             | 0.293             |

At mild asymmetry (c0=0.1, c1=0.2), IMP and IJMPQ achieve near-symmetric high
cooperation in both dilemma types (0.946–0.962). MP and MPQ sit between M and
P — better than P alone for Pop_1 at high asymmetry, but far below IMP/IJMPQ.

At high asymmetry (c0=0.1, c1=0.3), IJMPQ sustains Pop_1 = 0.293 in
snowdrift vs 0.057 for the control — a fivefold lift.

## Mutual cooperation (IMP, c0=0.1)

**Dilemma 1 (PD):**

| c1   | qBSeen_0 | qBSeen_1 | w\_0  | w\_1  |
| ---- | -------- | -------- | ----- | ----- |
| 0.12 | 0.953    | 0.952    | 0.784 | 0.765 |
| 0.16 | 0.951    | 0.950    | 0.783 | 0.727 |
| 0.20 | 0.947    | 0.946    | 0.782 | 0.688 |
| 0.30 | 0.509    | 0.255    | 0.549 | 0.626 |

**Dilemma 2 (snowdrift):**

| c1   | qBSeen_0 | qBSeen_1 | w\_0  | w\_1  |
| ---- | -------- | -------- | ----- | ----- |
| 0.12 | 0.949    | 0.949    | 0.836 | 0.827 |
| 0.16 | 0.946    | 0.946    | 0.836 | 0.807 |
| 0.20 | 0.919    | 0.342    | 0.793 | 0.834 |
| 0.30 | 0.921    | 0.192    | 0.786 | 0.839 |

IMP eliminates cooperation asymmetry at mild cost differences: at (c0=0.1,
c1=0.12), both populations cooperate at ≈ 0.95 with nearly equal fitness. The
breakdown point differs by dilemma — symmetry holds through c1 = 0.20 in PD but
collapses by c1 = 0.20 in snowdrift.

IJMPQ extends this further: at (c0=0.1, c1=0.2) both populations reach
0.957/0.957 in PD and 0.962/0.962 in snowdrift.

## Shuffle vs noshuffle

Partner shuffling has a major impact on combined mechanisms because it disables the direct reciprocity ($M$) component. However, the presence of other loci (like partner choice $P$, lifetime memory $Q$, and indirect reciprocity $I, J$) provides varying levels of robustness:

### Mean cooperation across all 210 cells (gs=128)

| Mechanism | Dilemma | noshuffle (Pop_0 / Pop_1) | shuffle (Pop_0 / Pop_1) | Key observation |
| --------- | ------- | --------------------------- | ------------------------- | --------------- |
| **M**     | 1 (PD)  | 0.637 / 0.551               | 0.108 / 0.026             | Collapses to control baseline |
| **P**     | 1 (PD)  | 0.472 / 0.146               | 0.470 / 0.146             | Completely unaffected by shuffle |
| **MP**    | 1 (PD)  | 0.606 / 0.410               | 0.474 / 0.148             | Collapses to P-only baseline |
| **MPQ**   | 1 (PD)  | 0.594 / 0.318               | 0.523 / 0.155             | Q memory locus adds slight resilience |
| **IMP**   | 1 (PD)  | 0.670 / 0.505               | 0.567 / 0.264             | I locus (reputation) resists turnover |
| **IJMPQ** | 1 (PD)  | 0.729 / 0.573               | 0.729 / 0.442             | Extremely robust; Pop_0 unchanged |
| **IJMPQ** | 2 (SD)  | 0.923 / 0.609               | 0.932 / 0.477             | Maintains substantial Pop_1 lift |

### Role Split under Shuffle

Shuffling does not erase the deterministic role split (where the lower-cost population 0 cooperates more). In fact, the fraction of cells where Pop_0 > Pop_1 increases under shuffling for the most robust mechanisms:
- **IMP** (PD): Pop_0 > Pop_1 in **203/210** cells (noshuffle) $\rightarrow$ **210/210** cells (shuffle)
- **IJMPQ** (PD): Pop_0 > Pop_1 in **198/210** cells (noshuffle) $\rightarrow$ **205/210** cells (shuffle)
- **IJMPQ** (SD): Pop_0 > Pop_1 in **176/210** cells (noshuffle) $\rightarrow$ **197/210** cells (shuffle)

This happens because shuffling suppresses cooperation in the higher-cost population (Pop_1) more than in the lower-cost population (Pop_0), making the asymmetric role split even more pronounced across the parameter space.

## Exploitation

| Mech   | Dilemma | noshuffle | shuffle |
| ------ | ------- | --------- | ------- |
| IMP    | 1 (PD)  | -0.967    | -0.977  |
| IJMPQ  | 1 (PD)  | -0.948    | -0.963  |
| IMP    | 2 (SD)  | -0.507    | -0.362  |
| IJMPQ  | 2 (SD)  | -0.633    | -0.576  |

Combined mechanisms raise Pop_1 cooperation, partially restoring a
cooperation/fitness tradeoff. IJMPQ shows the strongest snowdrift coupling
(−0.633) because it most effectively elevates Pop_1.

### Pop_1 lift in snowdrift

| Mech   | Pop_1 mean | Pop_1 at (0.1, 0.3) |
| ------ | ----------- | -------------------- |
| M      | 0.191       | 0.123                |
| P      | 0.096       | 0.061                |
| IMP    | 0.391       | 0.192                |
| IJMPQ  | 0.609       | 0.293                |

IJMPQ is the only mechanism that brings Pop_1 into a genuinely cooperative
regime in snowdrift.

## Groupsize 4

Mean qBSeen across all 210 cells (noshuffle):

| Mech   | Dilemma | Pop_0 | Pop_1 | Pop_0 > Pop_1 |
| ------ | ------- | ------ | ------ | --------------- |
| IMP    | 1 (PD)  | 0.709  | 0.600  | 208/210         |
| IJMPQ  | 1 (PD)  | 0.740  | 0.617  | 190/210         |
| IMP    | 2 (SD)  | 0.904  | 0.364  | 196/210         |
| IJMPQ  | 2 (SD)  | 0.908  | 0.567  | 187/210         |

Unlike pure partner choice (P), combined mechanisms are robust to groupsize
reduction. IJMPQ shows role reversals in 18/210 PD cells and 22/210 snowdrift
cells at gs=4.

### Groupsize comparison (gs=4 vs gs=128)

**Dilemma 1 (PD):**

| Mechanism | c0   | c1   | Pop_0 gs=4 | Pop_0 gs=128 | Pop_1 gs=4 | Pop_1 gs=128 |
| --------- | ---- | ---- | ----------- | ------------- | ----------- | ------------- |
| IMP       | 0.10 | 0.12 | 0.943       | 0.953         | 0.943       | 0.952         |
| IMP       | 0.10 | 0.30 | 0.585       | 0.509         | 0.437       | 0.255         |
| IMP       | 0.20 | 0.30 | 0.857       | 0.637         | 0.844       | 0.519         |
| IJMPQ     | 0.10 | 0.12 | 0.955       | 0.963         | 0.954       | 0.963         |
| IJMPQ     | 0.10 | 0.30 | 0.545       | 0.574         | 0.320       | 0.293         |
| IJMPQ     | 0.20 | 0.30 | 0.920       | 0.932         | 0.917       | 0.931         |

At c0 = 0.20, c1 = 0.30, IMP shows the largest gs=4 advantage: Pop_1 reaches
0.844 at gs=4 vs 0.519 at gs=128. Small groups allow high-cost cooperators to
interact more repeatedly with the same partners.

**Dilemma 2 (snowdrift):** gs=4 and gs=128 are broadly similar; the large
Pop_1 advantage seen in PD at high asymmetry does not appear.

## Summary

| Topic                   | PD (dilemma 1)                                              | Snowdrift (dilemma 2)                                       |
| ----------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Best combined mech      | IJMPQ: mean Pop_0 = 0.729, Pop_1 = 0.573                  | IJMPQ: mean Pop_0 = 0.923, Pop_1 = 0.609                  |
| Mutualistic equilibrium | IMP/IJMPQ at (0.1, 0.12–0.20): both pops ≈ 0.95             | IMP at (0.1, 0.12–0.16): both pops ≈ 0.95; breaks by c1=0.20 |
| vs M alone              | IJMPQ raises Pop_1 from 0.551 to 0.573                     | IJMPQ raises Pop_1 from 0.191 to 0.609                    |
| vs P alone              | IMP/IJMPQ far exceed P for Pop_1 at mild asymmetry           | IJMPQ raises Pop_1 from 0.096 to 0.609                     |
| gs=4                    | IMP/IJMPQ robust; Pop_1 gains at large asymmetry            | Broadly similar to gs=128                                   |
| Role reversals (IJMPQ)  | Pop_1 > Pop_0 in 12/210 cells (gs=128), 18/210 (gs=4)     | 34/210 (gs=128), 22/210 (gs=4)                              |
