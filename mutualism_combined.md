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

Two populations with c0 < c1 interact across populations only (pop_2, 210-cell
upper triangle). Benefit b = 0.40 fixed, K = 0.50. Analysis covers dilemma 1
(PD) and dilemma 2 (snowdrift), groupsize 128 noshuffle (primary) and
groupsize 4; shuffle where noted.

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
combined mechanisms add little for fset_0 (already at ceiling); the benefit
is elevating fset_1.

## Role split

Mean qBSeen across all 210 cells (noshuffle, gs=128):

| Mech   | Dilemma | fset_0 | fset_1 | fset_0 > fset_1 |
| ------ | ------- | ------ | ------ | --------------- |
| MP     | 1 (PD)  | 0.606  | 0.410  | 210/210         |
| IMP    | 1 (PD)  | 0.670  | 0.505  | 203/210         |
| IJMPQ  | 1 (PD)  | 0.729  | 0.573  | 198/210         |
| MP     | 2 (SD)  | 0.931  | 0.220  | 210/210         |
| IMP    | 2 (SD)  | 0.915  | 0.391  | 196/210         |
| IJMPQ  | 2 (SD)  | 0.923  | 0.609  | 176/210         |

IMP and IJMPQ partially erode the deterministic role split at mild asymmetry.
In snowdrift, IJMPQ brings fset_1 to mean 0.609 (vs 0.091 control) and reverses
the role split in 34/210 cells.

## Mechanism comparison at sample cells

Cooperation at (c0=0.1, c1=0.2) and (c0=0.1, c1=0.3), noshuffle, gs=128:

**Dilemma 1 (PD):**

| Mech   | (0.1, 0.2) fset_0 | (0.1, 0.2) fset_1 | (0.1, 0.3) fset_0 | (0.1, 0.3) fset_1 |
| ------ | ----------------- | ----------------- | ----------------- | ----------------- |
| M      | 0.869             | 0.830             | 0.680             | 0.616             |
| P      | 0.600             | 0.187             | 0.369             | 0.101             |
| MP     | 0.729             | 0.465             | 0.478             | 0.248             |
| MPQ    | 0.701             | 0.317             | 0.472             | 0.172             |
| IMP    | 0.947             | 0.946             | 0.509             | 0.255             |
| IJMPQ  | 0.957             | 0.957             | 0.574             | 0.293             |

**Dilemma 2 (snowdrift):**

| Mech   | (0.1, 0.2) fset_0 | (0.1, 0.2) fset_1 | (0.1, 0.3) fset_0 | (0.1, 0.3) fset_1 |
| ------ | ----------------- | ----------------- | ----------------- | ----------------- |
| M      | 0.945             | 0.188             | 0.945             | 0.123             |
| P      | 0.973             | 0.089             | 0.972             | 0.061             |
| MP     | 0.948             | 0.194             | 0.945             | 0.123             |
| MPQ    | 0.948             | 0.204             | 0.948             | 0.128             |
| IMP    | 0.919             | 0.342             | 0.921             | 0.192             |
| IJMPQ  | 0.962             | 0.962             | 0.896             | 0.293             |

At mild asymmetry (c0=0.1, c1=0.2), IMP and IJMPQ achieve near-symmetric high
cooperation in both dilemma types (0.946–0.962). MP and MPQ sit between M and
P — better than P alone for fset_1 at high asymmetry, but far below IMP/IJMPQ.

At high asymmetry (c0=0.1, c1=0.3), IJMPQ sustains fset_1 = 0.293 in
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

## Exploitation

| Mech   | Dilemma | noshuffle | shuffle |
| ------ | ------- | --------- | ------- |
| IMP    | 1 (PD)  | -0.967    | -0.977  |
| IJMPQ  | 1 (PD)  | -0.948    | -0.963  |
| IMP    | 2 (SD)  | -0.507    | -0.362  |
| IJMPQ  | 2 (SD)  | -0.633    | -0.576  |

Combined mechanisms raise fset_1 cooperation, partially restoring a
cooperation/fitness tradeoff. IJMPQ shows the strongest snowdrift coupling
(−0.633) because it most effectively elevates fset_1.

### fset_1 lift in snowdrift

| Mech   | fset_1 mean | fset_1 at (0.1, 0.3) |
| ------ | ----------- | -------------------- |
| M      | 0.191       | 0.123                |
| P      | 0.096       | 0.061                |
| IMP    | 0.391       | 0.192                |
| IJMPQ  | 0.609       | 0.293                |

IJMPQ is the only mechanism that brings fset_1 into a genuinely cooperative
regime in snowdrift.

## Groupsize 4

Mean qBSeen across all 210 cells (noshuffle):

| Mech   | Dilemma | fset_0 | fset_1 | fset_0 > fset_1 |
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

| Mechanism | c0   | c1   | fset_0 gs=4 | fset_0 gs=128 | fset_1 gs=4 | fset_1 gs=128 |
| --------- | ---- | ---- | ----------- | ------------- | ----------- | ------------- |
| IMP       | 0.10 | 0.12 | 0.943       | 0.953         | 0.943       | 0.952         |
| IMP       | 0.10 | 0.30 | 0.585       | 0.509         | 0.437       | 0.255         |
| IMP       | 0.20 | 0.30 | 0.857       | 0.637         | 0.844       | 0.519         |
| IJMPQ     | 0.10 | 0.12 | 0.955       | 0.963         | 0.954       | 0.963         |
| IJMPQ     | 0.10 | 0.30 | 0.545       | 0.574         | 0.320       | 0.293         |
| IJMPQ     | 0.20 | 0.30 | 0.920       | 0.932         | 0.917       | 0.931         |

At c0 = 0.20, c1 = 0.30, IMP shows the largest gs=4 advantage: fset_1 reaches
0.844 at gs=4 vs 0.519 at gs=128. Small groups allow high-cost cooperators to
interact more repeatedly with the same partners.

**Dilemma 2 (snowdrift):** gs=4 and gs=128 are broadly similar; the large
fset_1 advantage seen in PD at high asymmetry does not appear.

## Summary

| Topic                   | PD (dilemma 1)                                              | Snowdrift (dilemma 2)                                       |
| ----------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Best combined mech      | IJMPQ: mean fset_0 = 0.729, fset_1 = 0.573                  | IJMPQ: mean fset_0 = 0.923, fset_1 = 0.609                  |
| Mutualistic equilibrium | IMP/IJMPQ at (0.1, 0.12–0.20): both pops ≈ 0.95             | IMP at (0.1, 0.12–0.16): both pops ≈ 0.95; breaks by c1=0.20 |
| vs M alone              | IJMPQ raises fset_1 from 0.551 to 0.573                     | IJMPQ raises fset_1 from 0.191 to 0.609                    |
| vs P alone              | IMP/IJMPQ far exceed P for fset_1 at mild asymmetry           | IJMPQ raises fset_1 from 0.096 to 0.609                     |
| gs=4                    | IMP/IJMPQ robust; fset_1 gains at large asymmetry            | Broadly similar to gs=128                                   |
| Role reversals (IJMPQ)  | fset_1 > fset_0 in 12/210 cells (gs=128), 18/210 (gs=4)     | 34/210 (gs=128), 22/210 (gs=4)                              |
