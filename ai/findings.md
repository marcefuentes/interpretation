# Key Findings — New Parameterization

Quick reference for future AI sessions. All data from gs=128, shuffle conditions unless noted.
Source analysis: ai/analyze_new_data.py. Full write-ups: hamilton_partner_choice.md, hamilton_reciprocity.md, hamilton_combined.md, mutualism_partner_choice.md, mutualism_reciprocity.md, mutualism_combined.md.

## Hamilton — Critical Thresholds (PD, shuffle, pop_1 unless noted)

| Mechanism | Key finding                                                                   |
| --------- | ----------------------------------------------------------------------------- |
| \_        | Drops from qB~0.53 at c=0 (T=R, no temptation) to ~0.04 by c=0.10           |
| M shuffle | Indistinguishable from control at all c — partner shuffling kills reciprocity |
| M noshuffle | 0.915 at c=0.10, 0.672 at c=0.30; largest shuffle sensitivity of any mech  |
| P         | Threshold at c≈0.34-0.36: qB drops from 0.408 to 0.036 across one step      |
| MP        | Lifts P threshold: maintains ~0.60 at c=0.36 vs 0.036 for P alone            |
| IJMPQ     | Most robust: 0.939 at c=0.30, 0.672 at c=0.40 (survives to R-P = 0)         |

## Hamilton — Population Contrasts (PD, shuffle, c=0.20)

| Scenario | Mechanism | qB (fset_0) | qB (fset_1) | Pattern                              |
| -------- | --------- | ----------- | ----------- | ------------------------------------ |
| pop_1    | P         | ~0.65       | —           | Cooperators choose in/out            |
| pop_2    | P         | 0.95        | 0.05        | Symmetry broken: one pop defects     |
| pop_2    | IJMPQ     | 0.85        | 0.72        | Both cooperate, asymmetry milder     |
| pop_3    | P         | 0.70        | 0.25 (fixed)| Evolving pop cooperates vs 25% fixed |

## Hamilton — Genotype Structure (P mechanism, PD, pop_1, shuffle)

At c=0.20: C1P1 (choosers) ~0.65, C1P0 (non-choosing cooperators) ~0.02, C0P1 (silent carriers) ~0.15.
C0P1 accumulates as neutral mutation from C1P1 especially in the transition zone near the P threshold.
Below threshold (high c): C1P1 collapses, P1 allele remains elevated due to C0P1 carriers.

## Mutualism — Role Split

Role split is deterministic: fset_0 (lower-cost pop, c0) cooperates more in 100% of cells
for every mechanism tested. This contrasts with hamilton pop_2 where the split is stochastic
and either population can end up as the cooperating side.

## Mutualism — Cooperation at Key Cells (noshuffle, PD, pop_2)

Near-symmetric high cooperation (closest to true mutualism) at mild asymmetry (c0=0.10, c1=0.12):

| Mechanism | fset_0 qB | fset_1 qB |
| --------- | --------- | --------- |
| \_        | ~0.05     | ~0.03     |
| M         | 0.91      | 0.87      |
| P         | 0.93      | 0.91      |
| IMP       | 0.954     | 0.952     |
| IJMPQ     | 0.96      | 0.95      |

## Mutualism — Exploitation Pattern (noshuffle, PD, c0=0.10, fset_1 qB)

As c1 increases away from c0, the high-cost population defects more while low-cost continues cooperating:

| Mechanism | c1=0.12 | c1=0.20 | c1=0.30 | c1=0.40 |
| --------- | ------- | ------- | ------- | ------- |
| \_        | ~0.03   | ~0.01   | ~0.01   | ~0.01   |
| IMP       | 0.952   | 0.91    | 0.72    | 0.44    |
| IJMPQ     | 0.95    | 0.93    | 0.82    | 0.59    |

## M Mechanism — Shuffle Sensitivity

Direct reciprocity (M) requires stable partner pairings to track history.
With shuffle: qB at c=0.10 ≈ 0.05 (control level).
With noshuffle: qB at c=0.10 ≈ 0.915.
This is the largest shuffle/noshuffle gap of any mechanism in hamilton.

## Snowdrift (dilemma 2) — Base Behavior

S = K+b-c > P = K for all c < 0.40, so cooperation is individually rational even for defectors.
Control (\_) reaches qB~0.96 at moderate c without any mechanism.
Mechanisms add marginal lift but the snowdrift floor is already high.
PD (dilemma 1) is the informative dilemma for mechanism discrimination.

## Analysis Scripts Available

- ai/analyze_new_data.py: full cross-study analysis (hamilton, mutualism; all mechanisms, cells, populations)
- ai/analyze_single_run.py: temporal dynamics from _1run studies

## Hamilton gs=4 — Key Findings (vs gs=128, PD, shuffle, pop_1)

| Mechanism | gs=4 effect                                                               |
| --------- | ------------------------------------------------------------------------- |
| \_        | Identical at both groupsizes                                              |
| M noshuffle | Invariant; near-identical profiles                                      |
| P         | Threshold shifts c≈0.34 → c≈0.08; effectively fails beyond c=0.10       |
| IJM       | REVERSAL: one of weakest (gs=128) → one of strongest (gs=4); 0.923 at c=0.20 vs 0.195 |
| IM        | Better at gs=4: 0.699 vs 0.404 at c=0.20                                 |
| IJMPQ     | Worse at high c: 0.341 vs 0.676 at c=0.40 (partner choice component fails) |
| IMP       | Broadly similar                                                           |

Interpretation: small groups make reputation signals (I, J loci) more reliable
(you observe more of partners' interactions) but make the chooser bottleneck
(P locus) far worse (fewer opportunities for mutual-swap in small groups).

## Mutualism gs=4 — Key Findings (vs gs=128, PD, noshuffle, pop_2)

- P collapses at c0,c1 ≥ 0.10 — same threshold as hamilton
- IMP and IJMPQ broadly similar; better for large asymmetries (fset_1)
  - IMP fset_1 at c0=0.20, c1=0.30: gs=4=0.851 vs gs=128=0.510

## Pending

- mutualism shuffle: analyzed — P (mutualism_partner_choice.md), M and indirect IM/IJM (mutualism_reciprocity.md), combined (mutualism_combined.md)
- prisoners/snowdrift: deprecated parameterization (old cost12/cost3 data); not part of the current K=0.5, b=0.4 study
