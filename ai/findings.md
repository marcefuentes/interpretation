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

## Prisoners — Payoff-Axis Calibration (new parameterization)

Prisoners is now a raw PD payoff-plane sweep: T=0.9, S=0.1 fixed; R and P swept
(18x18, 172 cells). Decouples temptation/risk/(R-P) that hamilton welds onto c.
Fitting qBSeen ~ a*R + b*P (pop_1, PD, noshuffle, gs=128); -b/a = P:R weight:

| Mechanism | -b/a | Limiting axis |
| --------- | ---- | ------------- |
| M         | 1.73 | risk / defection payoff P |
| P         | 0.89 | cooperation advantage R-P |
| MP/MPQ/IMP/IJMPQ | 0.50-0.56 | reward / temptation R (P-insensitive) |

- Partner choice collapses onto R-P (iso-R-P cells give equal qB).
- M is risk-limited: at R=0.50, qB falls 0.86 (P=0.14) -> 0.47 (P=0.46).
- Shuffle strips the M term: MP -b/a 0.56 -> 0.89 (reverts to pure P); M dies (0.730 -> 0.017).
- gs=4 is the MIRROR: strips the P term. P collapses (0.898 -> 0.075); MP/MPQ/IMP revert
  to M's risk signature (-b/a -> 1.5-1.6); M is groupsize-invariant (0.730 both); IJMPQ
  robust to both (0.894 at gs=4).
- IM/IJM (shuffle only) recover to 0.381/0.360 (gs=128); BOOSTED at gs=4 to 0.521/0.706
  (closed-pool reputation; hamilton's IJM reversal reproduced).
- Temporal (prisoners_1run, gs=128): only threshold cells (R-P~0.04) fluctuate; saturated stable.
- .con exports: gs=128 + gs=4 (image); gs=128 movie. gs=4 movie not generated.
- Full write-up: prisoners_calibration.md, prisoners_partner_choice.md, prisoners_reciprocity.md.

## Snowdrift (new parameterization) — single-run only

snowdrift_1run is a single-run (Runs=1) snowdrift-ordered payoff sweep: T=0.9, P=0.10
fixed; R and S swept (172 cells, T>R>S>P), dilemma 2. The multi-run snowdrift/ dir is
empty (no 30-run .con). Single-run landscape (noisy): control meanQ~0.49 (vs ~0.017 for
PD control) confirms the snowdrift cooperation floor in the raw payoff plane. NOT written
up as a doc — single runs violate the 30-run rigor standard; needs multi-run data first.

## Model mechanics (validated against trps source, 2026-06)

Confirmed directly in ~/code/trps/code/src against the analysis docs' claims:

- decide_qB.c: each round qBDecided = qBDefault unless age>0 and partner age>0.
  Precedence under indirect_r: J (Imimic_lt, language=1) copies round(partner->qBSeen_lt)
  > I (Imimic) copies partner->qBSeen (third party, any partner) > M (Mimic) copies
  partner->qBSeen only if partner==oldpartner (direct). So C1M1=TFT (coop first), C0M1=
  suspicious TFT (defect first then mimic) — C0M1 is NOT silent.
- fitness.c: w = w_matrix[pop][own][partner] - cost; then qBSeen=qBDecided (partner reads
  your last move), oldpartner=partner, age++. Round loop is the simulation.c time loop.
- calculate_derived_globals.c: payoff matrices exactly match docs (PD T=K+b,R=K+b-c,P=K,S=K-c;
  SD R=K+b-c/2,S=K+b-c; folder 0 T=P=K,R=S=K+b-c). populations==3 => pop_1 fixed at 50/50
  per locus (=> 25% each of 4 genotypes for a 2-locus mechanism).
- choose_partner.c: C0P1 silencing confirmed — can_improve_L0_partner requires Choose && qBSeen!=0
  && partner->qBSeen==0, so a defector (qBSeen=0) never swaps. Mutual swap: both sides must prefer;
  two stuck cooperators pair up and their ex-defector partners pair together. Choose=P (recent,
  qBSeen), Choose_lt=Q (lifetime, qBSeen_lt).
- recruits.c: cost = 0.001 * ((Choose||Choose_lt) + (Mimic||Imimic||Imimic_lt)) per round —
  per-module-family, not per-locus. C0P1/C0M1 carriers still pay it.
- Alternation math (validated): C1M1 vs C0M1 lock out-of-phase -> avg (T+S)/2 = (0.9+0.5)/2 = 0.70
  at c=0; C1M0 vs C0M1 -> mutual cooperation R=0.90. Snowdrift S-P penalty at c=0.12 = 0.78-0.50
  = 0.28 = 280 x the 0.001 locus cost. Matches hamilton_reciprocity.md / mutualism_reciprocity.md.

## Verification

- ai/verify_claims.py: re-derives headline doc numbers from .con data, PASS/FAIL (39 checks).
  Run before committing doc edits to catch prose/data drift.

## Analysis Scripts Available

- ai/analyze_new_data.py: full cross-study analysis (hamilton, mutualism; all mechanisms, cells, populations)
- ai/analyze_prisoners.py: prisoners payoff-axis calibration (sensitivity fit, R-P collapse, genotypes, pop_2/3, shuffle, IM/IJM)
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
