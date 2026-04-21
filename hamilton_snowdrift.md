# Hamilton Snowdrift Variant (given = 1.5)

## Overview

This file tracks analysis for the Hamilton study under the snowdrift variant (given = 1.5), complementing the existing Hamilton documentation for given = 1.0 and given = 0.5.

---

## The Game (Source-Derived)

At given = 1.5, calculate_derived_globals.c switches to the cost/snowdrift branch:

- c = k1 - b_c
- T = k0 + k1
- R = k0 + k1 - c/2
- P = k0
- S = k0 + k1 - c

With Hamilton constants k0 = 2, k1 = 1, and x = b_c:

| Payoff | Formula           |
| ------ | ----------------- |
| T    | 3               |
| R    | 2.5 + 0.5x      |
| P    | 2               |
| S    | 2 + x           |

Key differences from given = 1.0/0.5:
- T is constant (3) instead of increasing with b-c
- S varies strongly with x (can exceed R and T)
- interpretation must be rebuilt from this branch, not ported from prior Hamilton docs

---

## Analysis Checklist

- [x] Derive exact payoff equations from source for this given
- [ ] Classify local game orderings across the axis
- [ ] Recompute qBSeen/wmean/chooser signatures for given = 1.5
- [ ] Compare with Hamilton given = 1.0 and 0.5 to isolate what changes

---

## Regime Map (by x = b_c)

From the formulas above:

- x < 1  -> T > R > S > P (snowdrift ordering)
- x = 1  -> T = R = S > P (boundary)
- x > 1  -> S > R > T > P

This should be the first validation layer before reading cooperation/fitness outcomes.

On the 21-point Hamilton grid (shuffle_cost12_128, mechanism P, given = 1.5):

| Regime        | Cells |
| ------------- | ----- |
| T > R > S > P | 14    |
| T = R = S > P | 1     |
| S > R > T > P | 6     |

---

## First-Pass Outcomes (from raw per-cell finals)

Data source for this draft: final row of each 000*_*.csv file in
~/results/hamilton/shuffle_cost12_128/P/1.5/ (no csv_*_for_image.con present yet).

### Population means by scenario

| Scenario | qBSeen mean | qBSeen min-max | wmean mean | C1P1 mean | C1P0 mean | P1 mean |
| -------- | ----------- | -------------- | ---------- | --------- | --------- | ------- |
| pop_1 (_0) | 0.956 | 0.953-0.968 | 7.015 | 0.673 | 0.284 | 0.703 |
| pop_2 (_0) | 0.887 | 0.756-0.986 | 3.401 | 0.506 | 0.380 | 0.573 |
| pop_2 (_1) | 0.041 | 0.026-0.221 | 9.866 | 0.022 | 0.019 | 0.500 |
| pop_3 (_0, evolving) | 0.892 | 0.825-0.983 | 5.310 | 0.658 | 0.234 | 0.737 |
| pop_3 (_1, fixed) | 0.500 | 0.497-0.504 | 8.232 | 0.250 | 0.250 | 0.500 |

### pop_2 asymmetry signature

- Pop_0 has higher cooperation in **100%** of cells (21/21).
- Pop_0 has lower fitness in **100%** of cells (21/21).
- Mean gaps: ΔqBSeen = +0.846, Δwmean = -6.465.
- Correlation corr(ΔqBSeen, Δwmean) = -0.129 (weakly negative over this 1D sweep).

### Extremes

- pop_1 qBSeen max: 0.968 at b_c = 8.0; min: 0.953 at b_c = 0.177.
- pop_2 (_0) qBSeen max: 0.986 at b_c = 8.0; min: 0.756 at b_c = 0.008.
- pop_2 (_1) qBSeen max: 0.221 at b_c = 8.0; min: 0.026 at b_c = 1.0.

---

## Comparison with given = 0.5 and 1.0

Same extraction method for all three givens: final row from per-cell raw CSVs under
~/results/hamilton/shuffle_cost12_128/P/{given}/.

### pop_1 trajectory across givens

| given | qBSeen mean | wmean mean | C1P1 mean | C1P0 mean | P1 mean |
| ----- | ----------- | ---------- | --------- | --------- | ------- |
| 0.5   | 0.688 | 3.250 | 0.494 | 0.195 | 0.680 |
| 1.0   | 0.641 | 3.237 | 0.524 | 0.117 | 0.738 |
| 1.5   | 0.956 | 7.015 | 0.673 | 0.284 | 0.703 |

### pop_2 asymmetry across givens (_0 - _1)

| given | mean ΔqBSeen | mean Δwmean | corr(ΔqBSeen,Δwmean) | pop_0 more coop | pop_0 lower fitness |
| ----- | -------------- | ------------- | ---------------------- | --------------- | ------------------- |
| 0.5   | +0.072 | -0.072 | -1.000 | 100% | 100% |
| 1.0   | +0.203 | -1.149 | -0.922 | 100% | 100% |
| 1.5   | +0.846 | -6.465 | -0.129 | 100% | 100% |

### pop_3 evolving (_0) across givens

| given | qBSeen mean | wmean mean | C1P1 mean | C1P0 mean | P1 mean |
| ----- | ----------- | ---------- | --------- | --------- | ------- |
| 0.5   | 0.474 | 2.945 | 0.308 | 0.166 | 0.585 |
| 1.0   | 0.303 | 2.847 | 0.252 | 0.052 | 0.620 |
| 1.5   | 0.892 | 5.310 | 0.658 | 0.234 | 0.737 |

Interpretation anchor: given = 1.5 sits in a different payoff branch than 0.5/1.0, and this is reflected by the jump to near-saturated cooperation in pop_1 and very large pop_2 exploitation gaps.
