# Mutualism Snowdrift Variant (given = 1.5)

## Overview

This file tracks analysis for the Mutualism study under the snowdrift variant (given = 1.5), parallel to existing Mutualism notes for given = 1.0 and given = 0.5.

---

## The Game (Source-Derived)

At given = 1.5, calculate_derived_globals.c uses the cost/snowdrift branch:

- c0 = k1 - b_c_0
- c1 = k1 - b_c_1

Population-specific payoffs:

| Population | T         | R                    | P    | S                |
| ---------- | --------- | -------------------- | ---- | ---------------- |
| pop_0      | k0 + k1 | k0 + k1 - c0/2     | k0 | k0 + k1 - c0   |
| pop_1      | k0 + k1 | k0 + k1 - c1/2     | k0 | k0 + k1 - c1   |

With k0 = 2, k1 = 1, x0 = b_c_0, x1 = b_c_1:

- pop_0: T0 = 3, R0 = 2.5 + 0.5x0, P0 = 2, S0 = 2 + x0
- pop_1: T1 = 3, R1 = 2.5 + 0.5x1, P1 = 2, S1 = 2 + x1

Critical structural change vs mutualism at given < 1.5:
- there is **no cross-benefit term** (R0/S0 no longer depend on x1, and R1/S1 no longer depend on x0)
- each population's game is driven by its **own** parameter only

---

## Analysis Checklist

- [x] Derive population-specific payoff equations at given = 1.5
- [ ] Build regime-map counts for both populations across the triangular grid
- [ ] Re-evaluate role assignment, bottlenecks, and exploitation under snowdrift payoffs
- [ ] Compare to existing Mutualism (given = 1.0, 0.5) patterns

---

## Regime Map Rules (per population)

For each population i with x_i = b_c_i:

- x_i < 1 -> T_i > R_i > S_i > P_i
- x_i = 1 -> T_i = R_i = S_i > P_i
- x_i > 1 -> S_i > R_i > T_i > P_i

Because mutualism uses a triangular grid (x1 >= x0), the two populations can occupy different regime families in the same cell.

On the 231-cell triangular grid (shuffle_cost12_128, mechanism P, given = 1.5):

### Population 0 (x0 = b_c_0)

| Ordering | Cells |
| -------- | ----- |
| T > R > S > P | 203 |
| T = R = S > P | 7 |
| S > R > T > P | 21 |

### Population 1 (x1 = b_c_1)

| Ordering | Cells |
| -------- | ----- |
| T > R > S > P | 105 |
| T = R = S > P | 15 |
| S > R > T > P | 111 |

---

## First-Pass Outcomes (from raw per-cell finals)

Data source for this draft: final row of each 000*_*.csv file in
~/results/mutualism/shuffle_cost12_128/P/1.5/pop_2/ (no csv_*_for_image.con present yet).

| Population | qBSeen mean | qBSeen min-max | wmean mean | C1P1 mean | C1P0 mean | P1 mean |
| ---------- | ----------- | -------------- | ---------- | --------- | --------- | ------- |
| pop_0 (_0) | 0.125 | 0.023-0.600 | 9.450 | 0.075 | 0.050 | 0.517 |
| pop_1 (_1) | 0.835 | 0.309-0.988 | 5.072 | 0.439 | 0.396 | 0.524 |

Pairwise asymmetry across cells:

- pop_0 is more cooperative in **5.2%** of cells (12/231).
- pop_0 has lower fitness in **5.2%** of cells (12/231).
- Mean gaps (pop_0 - pop_1): ΔqBSeen = -0.710, Δwmean = +4.378.
- corr(ΔqBSeen, Δwmean) = -0.699.
- Cell counts: 21 diagonal, 210 off-diagonal.

Interpretation note: unlike given < 1.5 mutualism, these outcomes no longer follow cross-benefit coupling; the direction now tracks each population's own b_c-driven snowdrift regime mix.

---

## Comparison with given = 0.5 and 1.0

Same extraction method for all three givens: final row from per-cell raw CSVs under
~/results/mutualism/shuffle_cost12_128/P/{given}/pop_2/.

### Population means across givens

| given | pop_0 qBSeen | pop_1 qBSeen | pop_0 wmean | pop_1 wmean |
| ----- | ------------ | ------------ | ----------- | ----------- |
| 0.5   | 0.289 | 0.688 | 3.391 | 2.992 |
| 1.0   | 0.276 | 0.125 | 2.110 | 2.393 |
| 1.5   | 0.125 | 0.835 | 9.450 | 5.072 |

### Pair asymmetry across givens (pop_0 - pop_1)

| given | mean ΔqBSeen | mean Δwmean | corr(ΔqBSeen,Δwmean) | pop_0 more coop | pop_0 lower fitness |
| ----- | -------------- | ------------- | ---------------------- | --------------- | ------------------- |
| 0.5   | -0.399 | +0.399 | -1.000 | 8.2% | 8.2% |
| 1.0   | +0.151 | -0.282 | -0.821 | 92.6% | 89.2% |
| 1.5   | -0.710 | +4.378 | -0.699 | 5.2% | 5.2% |

### Genotype-level comparison (means)

| given | pop_0 C1P1 | pop_0 C1P0 | pop_1 C1P1 | pop_1 C1P0 |
| ----- | ------------ | ------------ | ------------ | ------------ |
| 0.5   | 0.206 | 0.082 | 0.420 | 0.267 |
| 1.0   | 0.256 | 0.020 | 0.109 | 0.015 |
| 1.5   | 0.075 | 0.050 | 0.439 | 0.396 |

Interpretation anchor: the sign flip between given = 1.0 and given = 1.5 is consistent with switching from the benefit/cross-benefit branch (given < 1.5) to the snowdrift cost branch (given >= 1.5), where each population's local game follows its own b_c rather than partner-coupled payoffs.
