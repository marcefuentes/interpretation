# Snowdrift — Partner Choice

Partner-choice analysis (mechanism P) for the snowdrift study. Pure reciprocity (M, IM, IJM) is in **snowdrift_reciprocity.md**; the cross-mechanism payoff-axis attribution is in **snowdrift_calibration.md**.

## Overview

Snowdrift fixes T = 0.90 and P = 0.10 and sweeps R and S independently (18 × 18 grid, 172 cells with T > R > S > P). Dilemma 2 (Snowdrift) only, symmetric payoffs across populations, pops 1/2/3, shuffle and noshuffle, gs = 128. Each cell is a mean over 30 runs. See **snowdrift.md** for the study framing and **snowdrift_calibration.md** for the payoff geometry.

## Cooperation collapses onto R − S

Partner choice cooperation is, to good approximation, a function of the mutual-cooperation-to-sucker payoff advantage R − S. Binning all 172 cells by R − S (pop_1, noshuffle, gs=128) shows the within-bin spread narrowing at high values:

| R − S | cells | mean qB | min | max | spread |
| ----- | ----- | ------- | ----- | ----- | ------ |
| 0.00 | 1 | 0.961 | 0.961 | 0.961 | 0.000 |
| 0.04 | 18 | 0.874 | 0.614 | 0.970 | 0.356 |
| 0.08 | 17 | 0.919 | 0.800 | 0.971 | 0.171 |
| 0.12 | 16 | 0.936 | 0.876 | 0.970 | 0.094 |
| 0.20 | 14 | 0.954 | 0.927 | 0.973 | 0.047 |
| 0.28 | 12 | 0.962 | 0.948 | 0.974 | 0.026 |
| 0.40 | 9 | 0.969 | 0.962 | 0.973 | 0.011 |
| 0.60 | 4 | 0.974 | 0.973 | 0.975 | 0.002 |
| 0.72 | 1 | 0.977 | 0.977 | 0.977 | 0.000 |

Cooperation remains extremely high across the entire sweep. The spread is only visible near the smallest R − S cell columns (R − S = 0.04), where some cells show moderate cooperation (min qB = 0.614) while others saturate near 0.970.

## Genotype structure

C1P1 (active choosers), C1P0 (non-choosing cooperators), and C0P1 (silent choice carriers) along R − S (pop_1, noshuffle, gs=128):

| R − S | qB | C1P1 | C1P0 | C0P1 |
| ----- | ----- | ----- | ----- | ----- |
| 0.00 | 0.961 | 0.485 | 0.475 | 0.019 |
| 0.04 | 0.925 | 0.482 | 0.443 | 0.038 |
| 0.08 | 0.951 | 0.540 | 0.411 | 0.028 |
| 0.16 | 0.964 | 0.556 | 0.409 | 0.020 |
| 0.24 | 0.965 | 0.586 | 0.379 | 0.020 |
| 0.40 | 0.973 | 0.597 | 0.375 | 0.017 |
| 0.72 | 0.977 | 0.633 | 0.344 | 0.015 |

This genotype profile contrasts sharply with Prisoners (PD):

- **High non-choosing cooperators (C1P0).** C1P0 remains very high (ranging from 0.34 to 0.47) across the entire plane. Because the Snowdrift cooperation floor is high, the penalty for cooperating without sorting is small, allowing non-choosing cooperators to coexist easily with choosers.
- **Low silent carriers (C0P1).** Silent choice carriers (C0P1) are almost absent (remaining below 0.04). In Prisoners, C0P1 accumulated up to 0.45 under the threshold because defectors (C0) dominated the population. In Snowdrift, defectors are rare, leaving no room for silent carrier accumulation.

## Pop_2 symmetry breaking: extreme stable exploitation

Under pop_2, the two coevolving populations break symmetry stochastically. One population (fset_0) becomes the cooperating side and climbs to near-perfect cooperation, while the other population (fset_1) defects completely. Slice at S = 0.14 (noshuffle, gs=128):

| R | R − S | qB_0 | qB_1 | ΔqB | w_0 | w_1 |
| ---- | ----- | ----- | ----- | ------ | ----- | ----- |
| 0.18 | 0.04 | 0.962 | 0.012 | +0.950 | 0.138 | 0.859 |
| 0.22 | 0.08 | 0.961 | 0.014 | +0.948 | 0.138 | 0.858 |
| 0.26 | 0.12 | 0.962 | 0.015 | +0.947 | 0.139 | 0.858 |
| 0.30 | 0.16 | 0.963 | 0.015 | +0.948 | 0.140 | 0.860 |
| 0.34 | 0.20 | 0.962 | 0.016 | +0.946 | 0.140 | 0.859 |
| 0.50 | 0.36 | 0.964 | 0.023 | +0.941 | 0.145 | 0.861 |
| 0.78 | 0.64 | 0.969 | 0.075 | +0.894 | 0.185 | 0.865 |
| 0.82 | 0.68 | 0.972 | 0.118 | +0.854 | 0.217 | 0.866 |
| 0.86 | 0.72 | 0.976 | 0.241 | +0.735 | 0.311 | 0.870 |

This split represents an extreme exploitation state:

- **Payoff mapping.** Since pop_2 only pairs individuals between populations, cooperating fset_0 individuals always play against defecting fset_1 individuals. The cooperator earns the sucker payoff S (w_0 ≈ S = 0.14), while the defector earns the temptation payoff T (w_1 ≈ T·qB_0 = 0.90 · 0.96 = 0.86).
- **The paradox of success.** The cooperating population has significantly lower fitness than the defecting population (w_0 is around 0.14 vs w_1 is around 0.86). All 172 cells show this fitness inversion (where the cooperating population has lower fitness), resulting in a strong negative correlation between the cooperation gap and the fitness gap (corr = −0.437).

## Pop_3: evolving vs fixed partner

For the P mechanism under noshuffle gs = 128, the evolving population fset_0 reaches a high mean qBSeen of 0.819 against a fixed partner held at 25% each genotype (whose qBSeen is 0.500 by construction).

## Groupsize 4: chooser bottleneck is bypassed

At gs = 4 (noshuffle, pop_1), mean qBSeen is 0.717 (down from 0.947 at gs=128). In Prisoners, gs=4 caused partner choice to collapse completely (qB = 0.075) because cooperators were too rare to bootstrap mutual swaps. In Snowdrift, the high cooperation floor ensures that cooperators are always common, allowing them to pair up and swap even in small groups of four.

## Temporal dynamics (snowdrift_1run)

Single-run trajectories (P, pop_1, noshuffle, gs=128; snapshots from t = 131072 to 1048576 via snowdrift_1run) show high stability:

| R − S | range (max−min) | representative trajectory |
| ----- | --------------- | ---------------------------------- |
| 0.04 | 0.171 | 0.65 → 0.59 → 0.61 → 0.55 → 0.69 → 0.52 → 0.55 → 0.52 |
| 0.08 | 0.140 | 0.76 → 0.80 → 0.83 → 0.81 → 0.86 → 0.84 → 0.83 → 0.90 |
| 0.20 | 0.034 | 0.92 → 0.91 → 0.90 → 0.92 → 0.91 → 0.93 → 0.93 → 0.93 |
| 0.40 | 0.018 | 0.96 → 0.95 → 0.97 → 0.96 → 0.97 → 0.97 → 0.96 → 0.96 |

Even threshold cells (R − S = 0.04) fluctuate only moderately (range = 0.171), and cells at R − S ≥ 0.20 are extremely stable, showing that cooperation in Snowdrift never crashes.

## Caveats

- con exports and temporal (movie) exports exist for both gs = 128 and gs = 4.
