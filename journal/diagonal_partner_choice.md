# Diagonal — Partner Choice

Partner-choice analysis for the equal-cost Diagonal study (mechanism **P**
only — no reciprocity locus). Pure reciprocity (M, IM, IJM) is in
**diagonal_reciprocity.md**; combined mechanisms (MP, MPQ, IMP, IJMPQ) are in
**diagonal_combined.md**. For asymmetric costs (c0 ≠ c1), see
**mutualism_partner_choice.md**.

## Overview

This study is the equal-cost diagonal ($c_0 = c_1 = c$). See **[diagonal.md](diagonal.md)** for the central game parameters.

Unlike mutualism (pop_2 only, strict upper triangle), Diagonal includes
pop_1 (single population), pop_2 (two coevolving populations), and pop_3
(evolving vs fixed partner). Analysis covers dilemma types 0 (control),
1 (PD), and 2 (snowdrift), groupsize 128 (primary) and groupsize 4
(dedicated section plus comparison). Partner-choice analysis focuses on d1
and d2; d0 is not meaningful for P.

## Game parameters and payoffs

See **[diagonal.md](diagonal.md#game-parameters)** for the common game parameters and payoff structure. Partner-choice mechanisms are not tested meaningfully at dilemma 0.

## Cooperation profiles (P mechanism)

### Dilemma 1 (PD), shuffle, groupsize 128, pop_2 fset_0

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| P      | 0.963  | 0.849  | 0.728  | 0.630  | 0.553  | 0.022  |

Partner choice sustains high cooperation at low to moderate c, then drops
sharply between c = 0.34 and c = 0.36 (qBSeen falls from 0.41 to 0.036 for P).
This threshold is the chooser bottleneck: at high c, defection dominates and
insufficient C1P1 individuals exist to sustain swaps.

### Dilemma 2 (snowdrift), shuffle, groupsize 128, pop_2 fset_0

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| \_     | 0.881  | 0.968  | 0.964  | 0.954  | 0.917  | 0.184  |
| P      | 0.955  | 0.970  | 0.969  | 0.958  | 0.930  | 0.679  |

The control already sustains qBSeen ≈ 0.96 at moderate c. P adds modest lift;
the main benefit is at c = 0.40 (P = 0.679 vs control 0.184).

## Shuffle vs noshuffle (P)

| Mech  | Condition | c=0.00 | c=0.10 | c=0.20 | c=0.30 | c=0.40 |
| ----- | --------- | ------ | ------ | ------ | ------ | ------ |
| P     | shuffle   | 0.963  | 0.833  | 0.667  | 0.566  | 0.022  |
| P     | noshuffle | 0.961  | 0.811  | 0.688  | 0.569  | 0.023  |

Partner choice is largely insensitive to shuffle: cooperation levels differ
by less than 0.03 across the cooperation range. The chooser bottleneck
determines outcomes, not partner continuity.

## P1 hitchhiking

The P1 allele peaks at a lower c than C1P1 across all population structures:

| Population       | P1 max c | P1    | C1P1 max c | C1P1  |
| ---------------- | -------- | ----- | ---------- | ----- |
| pop_1            | 0.34     | 0.898 | 0.30       | 0.774 |
| pop_2 (fset_0)   | 0.18     | 0.858 | 0.10       | 0.687 |
| pop_3 (evolving) | 0.14     | 0.821 | 0.08       | 0.666  |

P1 is phenotypically silent in defectors (C0P1). The P1 maximum occurs where
C1P1 is still substantial but defectors persist as neutral P1 carriers via
mutation from C1P1.

The P1 peak shifts with population structure: pop_1 at c = 0.34 (cooperation
strong through c = 0.30); pop_2 at c = 0.18; pop_3 at c = 0.14 — because
cross-population pairing requires higher R − P to establish cooperation, moving
the transition zone to lower c.

## Population structure

### Single population (pop_1)

P mechanism, shuffle, PD:

| c    | qBSeen | C1P1  | C1P0  | C0P1  | P1    | C1P0/qBSeen |
| ---- | ------ | ----- | ----- | ----- | ----- | ----------- |
| 0.00 | 0.961  | 0.632 | 0.329 | 0.024 | 0.656 | 34%         |
| 0.10 | 0.949  | 0.669 | 0.280 | 0.035 | 0.704 | 29%         |
| 0.20 | 0.929  | 0.748 | 0.181 | 0.054 | 0.802 | 19%         |
| 0.30 | 0.864  | 0.774 | 0.090 | 0.109 | 0.883 | 10%         |
| 0.36 | 0.668  | 0.639 | 0.029 | 0.242 | 0.881 |  4%         |
| 0.40 | 0.056  | 0.049 | 0.007 | 0.463 | 0.511 | 13%         |

Pop_1 maintains higher cooperation than pop_2 because the chooser bottleneck is
weaker: swap partners are drawn from the same pool. At high c, C1P0 becomes
rare; C0P1 hitchhikers dominate P1 even after cooperation collapses.

### Two coevolving populations (pop_2)

Symmetry breaks stochastically: one population cooperates more (fset_0).

P mechanism, shuffle, PD:

| c    | qBSeen_0 | qBSeen_1 | ΔqBSeen | w\_0  | w\_1  | Δw     |
| ---- | -------- | -------- | ------- | ----- | ----- | ------ |
| 0.04 | 0.928    | 0.405    | +0.523  | 0.623 | 0.853 | -0.230 |
| 0.06 | 0.891    | 0.330    | +0.562  | 0.577 | 0.835 | -0.258 |
| 0.10 | 0.833    | 0.315    | +0.518  | 0.541 | 0.800 | -0.259 |
| 0.30 | 0.566    | 0.475    | +0.091  | 0.518 | 0.582 | -0.064 |
| 0.36 | 0.036    | 0.033    | +0.004  | 0.498 | 0.501 | -0.003 |

Asymmetry peaks at c ≈ 0.04–0.08 (ΔqBSeen ≈ 0.52–0.56). Correlation between
cooperation advantage and fitness deficit: −0.984 (paradox of success). This
contrasts with mutualism pop_2, where the role split is deterministic off the
diagonal. Under partner choice (P), Pop_0 (the sorted higher-cooperating role) can suffer lower fitness than in the control (mechanism _):
- **Prisoner's Dilemma (PD):** At c = 0.40, Pop_0's fitness is slightly lower under P than under the control (0.4974 vs. 0.4976 under shuffle). This minor drop is negligible and near the noise floor, reflecting the inability of either population to sustain cooperation at such high cost.
- **Snowdrift:** Pop_0 gets lower fitness under P than under the control in 8 out of 21 cells (shuffle). At c = 0.40, cooperation rises from 0.1841 (control) to 0.6789 (P), but average fitness drops from 0.5460 (control) to 0.5167 (P) — a significant, non-noise deficit of 0.0293. Unilateral cooperation at c = 0.40 is highly penalized (earning K + b - c = 0.50) compared to defection (earning K + b = 0.90). The selective pressure of partner choice drives high levels of cooperation, but because the cost is too high to establish a fully cooperative group, individuals are frequently exploited, leading to lower average payoffs than if they had simply remained defectors.

### Cooperation Boost vs. Asymmetry Effects

Comparing partner choice (P) to the control (_) in the coevolving setup (pop_2) shows how the primary effect shifts depending on cost and dilemma:

- **Prisoner's Dilemma (PD):** 
  - The overall effect is a massive boost in average cooperation (lifting the pop_2 average from ~0.06 under control to ~0.50 under P).
  - **At low costs (c ≤ 0.16):** The major effect is **to increase cooperation** in both populations (e.g., at c = 0.02, cooperation rises from 0.233/0.200 to 0.960/0.783).
  - **At moderate costs (c = 0.04 to 0.12):** The major effect is **to increase asymmetry** (+0.548 asymmetry change at c = 0.06). While both populations are lifted, symmetry breaks stochastically and one population becomes highly cooperative (~0.89) while the other remains moderately cooperative (~0.33).
- **Snowdrift:** 
  - **At low and moderate costs (c ≤ 0.34):** Partner choice has **almost no effect** on cooperation or asymmetry compared to the control. The Snowdrift payoff floor already sustains near-perfect cooperation in Pop_0 (0.95+) and defection in Pop_1 under control, leaving no room for P to change the outcome.
  - **At very high costs (c ≥ 0.36):** The major effect is **to increase asymmetry**. The control population collapses toward mutual defection (at c = 0.40, control is 0.182/0.130). Partner choice prevents this collapse by driving Pop_0 to maintain high cooperation (0.684) while Pop_1 defects (0.080), resulting in a massive asymmetry change of +0.552.



### Pop_3: evolving vs fixed partner

P mechanism, shuffle, PD:

| c    | qBSeen (evolving) | C1P1  | C1P0  | C0P1  |
| ---- | ----------------- | ----- | ----- | ----- |
| 0.08 | 0.856             | 0.666 | 0.190 | 0.103 |
| 0.16 | 0.604             | 0.548 | 0.056 | 0.263 |
| 0.24 | 0.392             | 0.368 | 0.024 | 0.370 |
| 0.26 | 0.073             | 0.059 | 0.014 | 0.476 |

Sharp transition near c = 0.24–0.26. Exploitation direction reverses with c:
evolving population exploited at c < 0.18; exploits fixed population at c > 0.20.

## Temporal dynamics (diagonal_1run)

Single-run data (shuffle, PD, P, pop_2) shows metastability at intermediate c:

| c    | Range (max−min) | Representative trajectory     |
| ---- | --------------- | ----------------------------- |
| 0.04 | 0.165           | 0.455 → 0.372 → 0.457 → 0.363 |
| 0.08 | 0.104           | 0.851 → 0.801 → 0.905 → 0.899 |
| 0.32 | 0.219           | 0.569 → 0.483 → 0.367 → 0.563 |

Multi-run averages smooth genuine role fluctuation in the transition zone.

## Groupsize 4

### Cooperation profiles (P)

PD, shuffle, pop_2 fset_0:

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| P      | 0.878  | 0.812  | 0.038  | 0.024  | 0.018  | 0.014  |

P holds cooperation through c ≈ 0.08 (0.812) then collapses by c = 0.16
(0.038), versus gs=128 where P stays above 0.55 through c = 0.32.

### Snowdrift at gs=4

Snowdrift cooperation remains high through moderate c at gs=4, similar to
gs=128. P stays near ceiling at moderate c; see **diagonal_combined.md**
for IJMPQ snowdrift profiles at gs=4.

### Shuffle vs noshuffle at gs=4 (P)

| Mech  | Condition | c=0.10 | c=0.20 | c=0.30 |
| ----- | --------- | ------ | ------ | ------ |
| P     | shuffle   | 0.698  | 0.029  | 0.019  |
| P     | noshuffle | 0.749  | 0.029  | 0.018  |

P collapses by c = 0.20 under both conditions at gs=4.

### pop_2 symmetry breaking at gs=4

| c    | fset_0 | fset_1 | ΔqBSeen |
| ---- | ------ | ------ | ------- |
| 0.08 | 0.812  | 0.367  | +0.445  |
| 0.10 | 0.698  | 0.339  | +0.359  |
| 0.16 | 0.038  | 0.031  | +0.007  |

Symmetry breaks at low c but both populations collapse by c = 0.16.

## Groupsize comparison (gs=4 vs gs=128)

PD, shuffle, pop_1:

| c    | gs=4  | gs=128 |
| ---- | ----- | ------ |
| 0.06 | 0.763 | 0.955  |
| 0.08 | 0.728 | 0.950  |
| 0.10 | 0.058 | 0.949  |
| 0.20 | 0.026 | 0.929  |
| 0.30 | 0.017 | 0.864  |
| 0.36 | 0.014 | 0.668  |

The P threshold shifts from c ≈ 0.34 (gs=128) to c ≈ 0.08 (gs=4). With only
four individuals per group, mutual C1P1 swaps are too rare to sustain
cooperation beyond mild costs. MP and MPQ partially recover via reciprocity
components — see **diagonal_combined.md**.

## Summary

| Topic                 | Key finding                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| P threshold (gs=128)  | Sharp collapse at c = 0.34–0.36 (PD)                                     |
| P threshold (gs=4)    | Collapses by c ≈ 0.08                                                    |
| Shuffle effect on P   | Negligible (< 0.03 difference)                                         |
| P1 hitchhiking        | P1 peaks at lower c than C1P1; location shifts with pop structure        |
| pop_2 exploitation    | corr(Δq, Δw) = −0.984; stochastic symmetry breaking                      |
| pop_3 transition      | Sharp collapse at c = 0.24–0.26; exploitation crossover at c ≈ 0.18   |
| Snowdrift (P)         | Near ceiling at moderate c; benefit at c = 0.40 (0.679 vs 0.184 control) |
| vs mutualism          | Diagonal pop_2 symmetry is stochastic; mutualism role split is deterministic |
