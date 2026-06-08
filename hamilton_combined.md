# Hamilton — Combined Mechanisms

Analysis of mechanisms that combine partner choice with reciprocity: **MP**,
**MPQ**, **IMP**, and **IJMPQ**. Pure partner choice (P) is in
**hamilton_partner_choice.md**; pure reciprocity (M, IM, IJM) is in
**hamilton_reciprocity.md**.

| Mechanism | Loci        | Components                          |
| --------- | ----------- | ----------------------------------- |
| MP        | C, M, P     | Direct reciprocity + partner choice |
| MPQ       | C, M, P, Q  | MP + lifetime partner-choice memory |
| IMP       | C, I, M, P  | Indirect + direct reciprocity + PC  |
| IJMPQ     | C, I, J, M, P, Q | Full stack with lifetime memory |

For asymmetric costs (c0 ≠ c1), see **mutualism_combined.md**.

## Overview

Hamilton is the equal-cost diagonal (c0 = c1 = c). The x-axis is c ∈ [0, 0.40]
with b = 0.40 fixed and K = 0.50. Analysis covers dilemmas 1 (PD) and 2
(snowdrift), groupsize 128 (primary) and groupsize 4.

## Cooperation profiles

### Dilemma 1 (PD), shuffle, groupsize 128, pop_2 fset_0

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| P      | 0.963  | 0.849  | 0.728  | 0.630  | 0.553  | 0.022  |
| MP     | 0.961  | 0.847  | 0.728  | 0.651  | 0.553  | 0.023  |
| MPQ    | 0.967  | 0.872  | 0.737  | 0.643  | 0.563  | 0.036  |
| IMP    | 0.963  | 0.951  | 0.939  | 0.776  | 0.805  | 0.170  |
| IJMPQ  | 0.975  | 0.972  | 0.967  | 0.958  | 0.923  | 0.672  |

Key patterns:

- MP and MPQ track P closely at low-to-moderate c; reciprocity adds little
  beyond partner choice until high c.
- IMP: extends cooperation above P alone; 0.170 vs 0.022 for P at c = 0.40.
- IJMPQ: most robust — above 0.92 through c = 0.32, 0.672 at c = 0.40.

### Dilemma 2 (snowdrift), shuffle, groupsize 128, pop_2 fset_0

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| \_     | 0.881  | 0.968  | 0.964  | 0.954  | 0.917  | 0.184  |
| P      | 0.955  | 0.970  | 0.969  | 0.958  | 0.930  | 0.679  |
| MPQ    | 0.964  | 0.970  | 0.965  | 0.957  | 0.935  | 0.780  |
| IJMPQ  | 0.973  | 0.971  | 0.969  | 0.966  | 0.962  | 0.960  |

Snowdrift provides a cooperation floor; IJMPQ reaches 0.960 at c = 0.40 vs
0.672 in PD.

## Shuffle vs noshuffle

IJMPQ shows a distinctive shuffle pattern — partner-choice components can
leverage shuffling for diverse interactions:

| Mech  | Condition | c=0.00 | c=0.10 | c=0.20 | c=0.30 | c=0.40 |
| ----- | --------- | ------ | ------ | ------ | ------ | ------ |
| IJMPQ | shuffle   | 0.975  | 0.971  | 0.964  | 0.939  | 0.672  |
| IJMPQ | noshuffle | 0.969  | 0.965  | 0.953  | 0.921  | 0.382  |

IJMPQ with shuffle outperforms noshuffle at high c (0.672 vs 0.382), because
partner-choice components leverage shuffling for diverse interactions.

## pop_2 symmetry: IJMPQ suppresses exploitation

P mechanism shows strong symmetry breaking (see **hamilton_partner_choice.md**).
IJMPQ nearly eliminates it:

| c    | qBSeen_0 | qBSeen_1 | ΔqBSeen | w\_0  | w\_1  | Δw     |
| ---- | -------- | -------- | ------- | ----- | ----- | ------ |
| 0.00 | 0.975    | 0.974    | +0.002  | 0.888 | 0.888 | -0.001 |
| 0.20 | 0.964    | 0.962    | +0.002  | 0.690 | 0.691 | -0.001 |
| 0.40 | 0.672    | 0.664    | +0.009  | 0.495 | 0.502 | -0.007 |

Both populations converge to near-identical high cooperation; the fitness
disadvantage of the cooperating population vanishes.

## Comparison across mechanisms

PD hierarchy at high c (c = 0.30–0.40):

1. IJMPQ: 0.939 at c = 0.30, 0.672 at c = 0.40
2. IMP: 0.804 at c = 0.30, 0.170 at c = 0.40
3. P / MP / MPQ: 0.55–0.57 at c = 0.30, collapse to ≈ 0.02 at c = 0.40
4. IJM: 0.084 at c = 0.30 (pure reciprocity — see **hamilton_reciprocity.md**)
5. IM: 0.062 at c = 0.30
6. M (shuffle) / \_: near zero

The IJMPQ advantage over IMP at high c comes from Q (lifetime partner-choice
memory) and J (lifetime indirect reciprocity).

For snowdrift, all mechanisms perform better; IJMPQ = 0.960 at c = 0.40.

## Groupsize 4

### Cooperation profiles

PD, shuffle, pop_2 fset_0:

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| IMP    | 0.951  | 0.935  | 0.900  | 0.801  | 0.555  | 0.065  |
| IJMPQ  | 0.967  | 0.961  | 0.954  | 0.940  | 0.892  | 0.342  |

Compared with gs=128:

- **IJMPQ**: 0.892 at c = 0.32, 0.342 at c = 0.40 — weaker high-c tail than
  gs=128 (0.672), because the P component fails in small groups.

### Snowdrift at gs=4

| Mech   | c=0.32 | c=0.40 |
| ------ | ------ | ------ |
| IJMPQ  | 0.949  | 0.933  |

### Shuffle vs noshuffle at gs=4

| Mech  | Condition | c=0.10 | c=0.20 | c=0.30 |
| ----- | --------- | ------ | ------ | ------ |
| IJMPQ | shuffle   | 0.958  | 0.948  | 0.914  |
| IJMPQ | noshuffle | 0.956  | 0.942  | 0.900  |

### MP/MPQ recovery at gs=4

With only four individuals per group, pure P collapses by c ≈ 0.08 (see
**hamilton_partner_choice.md**). MP and MPQ partially recover via reciprocity
components:

| Mechanism | c=0.20 gs=4 | c=0.20 gs=128 | c=0.30 gs=4 | c=0.30 gs=128 |
| --------- | ----------- | ------------- | ----------- | ------------- |
| MP        | 0.708       | 0.039         | 0.039       | 0.017         |
| MPQ       | 0.795       | 0.521         | 0.521       | 0.017         |
| IMP       | 0.900       | 0.933         | 0.777       | 0.873         |
| IJMPQ     | 0.943       | 0.960         | 0.900       | 0.939         |

### Revised mechanism hierarchy at gs=4 (PD, c = 0.20–0.30)

1. IJM: 0.923 / 0.790 — best at moderate-to-high c (pure reciprocity)
2. IJMPQ: 0.943 / 0.900
3. IMP: 0.900 / 0.777
4. MPQ: 0.795 / 0.521
5. MP: 0.708 / 0.039
6. P: 0.026 / 0.017

## Summary

| Topic                   | Key finding                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| Best combined (gs=128)  | IJMPQ: 0.923 at c=0.32, 0.672 at c=0.40 (PD)                            |
| IJMPQ vs IMP at high c  | Q and J loci extend cooperation window                                   |
| pop_2 IJMPQ             | Symmetry breaking suppressed; ΔqBSeen < 0.01 through c = 0.38           |
| IJMPQ shuffle at high c | 0.672 shuffle vs 0.382 noshuffle at c = 0.40                             |
| Snowdrift IJMPQ         | 0.960 at c = 0.40                                                        |
| gs=4 IJMPQ              | Weaker at high c (0.342 vs 0.672 at c=0.40) — P component fails in small groups |
| gs=4 MP/MPQ             | Partial recovery when P alone collapses                                  |
