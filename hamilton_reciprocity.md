# Hamilton — Reciprocity

Pure reciprocity analysis for the equal-cost Hamilton study (mechanisms **M**,
**IM**, **IJM** — no partner-choice locus). Partner choice (P) is in
**hamilton_partner_choice.md**; combined mechanisms (MP, MPQ, IMP, IJMPQ) are
in **hamilton_combined.md**. For asymmetric costs (c0 ≠ c1), see
**mutualism_reciprocity.md**.

## Overview

Hamilton is the equal-cost diagonal ($c_0 = c_1 = c$). See **[hamilton.md](hamilton.md)** for the central game parameters. Studies
include pop_1, pop_2, and pop_3 across dilemma types 0, 1 (PD), and 2
(snowdrift), groupsize 128 and 4, shuffle and noshuffle.

Mechanisms \_ and M are present for all three dilemma folders. IM and IJM are
present for dilemmas 1 and 2 only. All .con summary files are present under
~/results/hamilton/ for both groupsizes.

## Game parameters and payoffs

See **[hamilton.md](hamilton.md#game-parameters)** for the common game parameters and payoff structure.

## Cooperation profiles

### Dilemma 1 (PD), shuffle, groupsize 128, pop_2 fset_0

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| \_     | 0.535  | 0.066  | 0.034  | 0.022  | 0.017  | 0.014  |
| M      | 0.541  | 0.068  | 0.035  | 0.023  | 0.017  | 0.014  |
| IM     | 0.944  | 0.909  | 0.676  | 0.148  | 0.051  | 0.032  |
| IJM    | 0.973  | 0.968  | 0.961  | 0.141  | 0.076  | 0.043  |

Key patterns:

- Control and M with shuffle: near-zero cooperation for c > 0.
- IM: drops sharply at c ≈ 0.20 (0.676 → 0.148 at c = 0.24).
- IJM: high through c = 0.16 (0.961), drops at c = 0.24 (0.141).

### Dilemma 2 (snowdrift), shuffle, groupsize 128, pop_2 fset_0

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| \_     | 0.881  | 0.968  | 0.964  | 0.954  | 0.917  | 0.184  |
| M      | 0.888  | 0.963  | 0.960  | 0.949  | 0.916  | 0.182  |

Snowdrift provides a cooperation floor for M. Combined mechanisms (IJMPQ)
extend cooperation further — see **hamilton_combined.md**.

### Folder 0 (given=0), control baseline

Folder 0 is the old **given=0.0** control: payoffs do not depend on the
partner's move (T = P = K, R = S = K + b − c). Interactive cooperation is not
in the game — focal fitness depends only on whether the focal individual pays
cost c, not on partner behavior.

| c    | \_ (d0) | \_ (d1) | \_ (d2) |
| ---- | ------- | ------- | ------- |
| 0.00 | 0.979   | 0.535   | 0.881   |
| 0.08 | 0.977   | 0.066   | 0.968   |
| 0.40 | 0.528   | 0.014   | 0.184   |

High qBSeen at d0 (for c < b) reflects a **private** cost–benefit tradeoff:
the dominant strategy is to **produce b** (cooperate, pay c, receive b). Partner
moves do not enter the payoff matrix, but **M1 still shapes behavior**: a C1M1
individual paired with a mutant partner at qBSeen = 0 will mimic defection and
earn K instead of K + b − c. Always-cooperating **C1M0** avoids that error. M1
is therefore **slightly selected against** at d0, not neutral.

#### M1 allele frequency at d0 (pop_2, gs=128)

Under mechanism **\_**, M1 is a dummy locus (same mutation rate, no behavioral
effect) and drifts near 0.5. Under **M**, mimicry is active and M1 is selected
against when produce-b is optimal.

| Condition  | \_ M1 mean | M M1 mean | M − \_ |
| ---------- | ---------- | --------- | ------ |
| shuffle    | 0.495      | 0.494     | −0.001 |
| noshuffle  | 0.494      | 0.392     | −0.102 |

Noshuffle, selected c values:

| c    | \_ M1 | M M1 | M − \_ |
| ---- | ----- | ---- | ------ |
| 0.08 | 0.478 | 0.377| −0.101 |
| 0.16 | 0.495 | 0.375| −0.120 |
| 0.32 | 0.493 | 0.409| −0.084 |

| Condition      | c=0.08 C1M0 | c=0.08 C1M1 | c=0.32 C1M0 | c=0.32 C1M1 |
| -------------- | ----------- | ----------- | ----------- | ----------- |
| noshuffle d0 M | 0.607       | 0.341       | 0.552       | 0.335       |
| noshuffle d1 M | 0.537       | 0.378       | 0.135       | 0.621       |

With **noshuffle**, M1 under M falls ~0.10 below the dummy baseline while
**C1M0** dominates (~0.55–0.61) — consistent with selection against copying
when produce-b is optimal. At **d1** noshuffle the pattern reverses: C1M1 rises
with c (0.621 at c = 0.32) as reciprocity becomes advantageous.

With **shuffle**, M and \_ both stay near **0.5**: frequent partner turnover
limits repeated mimicry, so the penalty from copying a mutant defector is weak.

Genotype split at d0 shuffle (c = 0.00–0.32): almost all M1 is **C1M1** (dTFT,
≈ 0.46–0.49); **C0M1** (dSTFT, suspicious TFT) is rare (≈ 0.01–0.03). At d1
shuffle the split inverts: M1 ≈ 0.49 but mostly **C0M1** (≈ 0.44–0.49) because
defectors dominate — suspicious TFT players (defect first round, then mimic),
not silent carriers.

## Shuffle vs noshuffle

The largest shuffle effect is on direct reciprocity (M):

| Mech  | Condition | c=0.00 | c=0.10 | c=0.20 | c=0.30 | c=0.40 |
| ----- | --------- | ------ | ------ | ------ | ------ | ------ |
| M     | shuffle   | 0.541  | 0.053  | 0.028  | 0.019  | 0.014  |
| M     | noshuffle | 0.941  | 0.915  | 0.859  | 0.754  | 0.084  |

M with shuffle equals the control — TFT cannot accumulate credit without
stable pairings. M noshuffle is strongest individually at moderate c (0.915 at
c = 0.10) but collapses at c = 0.40.

## Comparison across mechanisms

PD hierarchy at high c (c = 0.30–0.40), pure reciprocity only:

1. IJM: 0.084 at c = 0.30, 0.043 at c = 0.40
2. IM: 0.062 at c = 0.30, 0.032 at c = 0.40
3. M (shuffle) / \_: near zero
4. M (noshuffle): 0.754 at c = 0.30, 0.084 at c = 0.40

Combined mechanisms (IMP, IJMPQ) and partner choice (P) extend cooperation
much further — see **hamilton_combined.md** and **hamilton_partner_choice.md**.

## Groupsize 4

### Cooperation profiles

PD, shuffle, pop_2 fset_0:

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| M      | 0.851  | 0.169  | 0.053  | 0.031  | 0.022  | 0.017  |
| IM     | 0.944  | 0.923  | 0.841  | 0.340  | 0.074  | 0.040  |
| IJM    | 0.970  | 0.967  | 0.956  | 0.930  | 0.176  | 0.059  |

Compared with gs=128:

- **IJM reversal**: remains above 0.93 through c = 0.24 at gs=4; collapses near
  c = 0.20 at gs=128. Closed reputation pools favor indirect reciprocity.
- **M with shuffle**: not identical to control at gs=4 (residual signal in small
  groups).

### Snowdrift at gs=4

| Mech   | c=0.32 | c=0.40 |
| ------ | ------ | ------ |
| M      | 0.832  | 0.690  |

M sustains much higher cooperation in snowdrift than PD at gs=4 (0.690 vs 0.017
at c = 0.40).

### Shuffle vs noshuffle at gs=4

| Mech  | Condition | c=0.10 | c=0.20 | c=0.30 |
| ----- | --------- | ------ | ------ | ------ |
| M     | shuffle   | 0.112  | 0.040  | 0.023  |
| M     | noshuffle | 0.912  | 0.857  | 0.740  |

M still shows the largest shuffle penalty (0.857 → 0.040 at c = 0.20).

## Groupsize comparison (gs=4 vs gs=128)

PD, shuffle, pop_1:

| Mechanism | c=0.10 gs=4 | c=0.10 gs=128 | c=0.20 gs=4 | c=0.20 gs=128 | c=0.30 gs=4 | c=0.30 gs=128 |
| --------- | ----------- | ------------- | ----------- | ------------- | ----------- | ------------- |
| M shuffle | 0.164       | 0.049         | 0.040       | 0.026         | 0.023       | 0.017         |
| IM        | 0.911       | 0.901         | 0.699       | 0.404         | 0.180       | 0.062         |
| IJM       | 0.947       | 0.965         | 0.923       | 0.195         | 0.790       | 0.079         |

### Indirect reciprocity (IJM) — dramatic reversal

| c    | IJM gs=4 | IJM gs=128 | IM gs=4 | IM gs=128 |
| ---- | -------- | ---------- | ------- | --------- |
| 0.20 | 0.923    | 0.195      | 0.699   | 0.404     |
| 0.30 | 0.790    | 0.079      | 0.180   | 0.062     |

At gs=4, reputation signals circulate among four fixed individuals; at gs=128,
defector signals disrupt the cascade.

### Direct reciprocity (M noshuffle) — groupsize invariant

| c    | M noshuffle gs=4 | M noshuffle gs=128 |
| ---- | ---------------- | ------------------ |
| 0.10 | 0.906            | 0.910              |
| 0.20 | 0.867            | 0.858              |
| 0.30 | 0.759            | 0.741              |
| 0.40 | 0.075            | 0.080              |

Stable pairings provide sufficient history regardless of group size.

### Revised mechanism hierarchy at gs=4 (PD, c = 0.20–0.30), pure reciprocity

1. IJM: 0.923 / 0.790 — best at moderate-to-high c (reversed from gs=128)
2. IM: 0.699 / 0.180
3. M shuffle: 0.040 / 0.026

Combined mechanisms rank above pure reciprocity at gs=4 — see
**hamilton_combined.md**.

## Cooperation Boost vs. Asymmetry Effects

Comparing direct reciprocity (M) to the control (_) in the coevolving setup (pop_2) reveals that reciprocity has a strong tendency to enforce symmetry and prevent role splits:

- **Prisoner's Dilemma (PD):** 
  - Under control, cooperation is nearly zero. Allowing reciprocity (M, under noshuffle) has a major effect of **increasing cooperation symmetrically** in both populations (Pop_0 +0.689, Pop_1 +0.690 on average across cells). Net asymmetry remains virtually zero (average 0.009). Because conditional reciprocity (TFT) ties cooperation to the partner's actions, a cooperator cannot play unless its partner cooperates too. This prevents one population from exploiting the other and suppresses the stochastic symmetry breaking seen under partner choice.
- **Snowdrift:** 
  - The major effect of reciprocity is **to decrease asymmetry** (by -0.217 on average). Under the control, the Snowdrift payoff floor already sustains high cooperation in Pop_0 (0.89) but low cooperation in Pop_1 (0.20), leading to high asymmetry (0.69). Reciprocity enforces symmetry by bootstrapping cooperation in Pop_1 to 0.40 (+0.208 boost), narrowing the asymmetry to 0.475 on average. At moderate costs (e.g. c = 0.08), asymmetry drops from 0.725 (control) to 0.015 (M) as both populations converge on symmetric cooperation.

## Summary

| Topic                    | Key finding                                                                 |
| ------------------------ | --------------------------------------------------------------------------- |
| Best pure reciprocity (gs=128) | IJM: 0.961 at c=0.16, collapses at c=0.24 (0.141)                    |
| Shuffle effect on M      | M shuffle = control; M noshuffle = 0.915 at c=0.10                         |
| Snowdrift M              | 0.916 at c = 0.32, 0.182 at c = 0.40                                       |
| gs=4 IJM reversal        | Weakest at gs=128 → near top at gs=4                                        |
| gs=4 M noshuffle         | Invariant to groupsize                                                      |
| vs mutualism             | Hamilton 1D c sweep; mutualism 2D asymmetric triangle with deterministic role split |
