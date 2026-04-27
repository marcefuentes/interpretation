# Mutualism — General Partner-Choice Framework

Study: mutualism, mechanism P, given = 1.0, pop_2 only.

Reference: instructions_mutualism.md for game parameters and payoff structure; instructions.md for shared model.

---

## Overview

Mutualism is the **general two-population formulation** for this branch: each population has its own net-benefit axis value (*b*₀ − *c*₀ and *b*₁ − *c*₁), and partner choice operates on cross-population pairing. Conceptually, this is the parent model for interpretation.

Hamilton is recovered as a **special diagonal slice** of this space where both populations share the same net benefit:

- *b*₀ − *c*₀ = *b*₁ − *c*₁

When that equality holds cell-by-cell, the asymmetric role split disappears by construction and the model reduces to the 1D Hamilton path. See **hamilton.md** for that diagonal-only readout and population-structure contrasts (pop_1, pop_2, pop_3).

This document therefore develops the reusable mechanism first: **cross-benefit payoffs**, the **chooser bottleneck**, and resulting cooperation/fitness asymmetries. The **Summary** table lists headline percentages and correlations. For **P**-mechanism definitions, see **instructions.md** and **instructions_mutualism.md**.

**Groupsize.** Grid cooperation levels and tables below use **shuffle_cost12_128**. **shuffle_cost12_4** collapses **qBSeen** relative to **128** on the same parameter grid (cross-benefit and **bottleneck** logic still apply; **numeric** claims do not). See **hamilton.md** for **hamilton_1run** end-state and **movie** detail.

The key structural feature is that each population's **R − P** has a cross-benefit, own-cost form: the benefit term comes from the partner population, while the cost term comes from the focal population. In the asymmetric region analyzed here (*b*₁ − *c*₁ >= *b*₀ − *c*₀), population 0 always has at least as strong a cooperation incentive as population 1.

## Document structure by given

This single file is organized by branch/regime role:

- **Given = 1.0 (PD family, benefit branch)**: main asymmetric mutualism interpretation (sections above and below on cooperation landscape, bottleneck, genotypes, and exploitation).
- **Given = 0.5 (mixed local regimes, benefit branch)**: see **Given = 0.5: Correct Game-Type Classification** and **Why g = 0.5 Helps Interpret g = 1.0**.
- **Given = 1.5 (snowdrift branch)**: see **Given = 1.5: Snowdrift-Branch Interpretation**.

---

## The Cooperation Landscape

Cooperation (qBSeen) in pop_0 increases with both *b*₀ − *c* and *b*₁ − *c*, but not symmetrically. At the highest parameters the cooperating population reaches qBSeen ≈ 0.90.

The heatmap for pop_0 shows a smooth gradient from ~0.04 (both *b* − *c* low) to ~0.90 (both high), with most of the variation concentrated in low-asymmetry regions. At large asymmetry, cooperation plateaus at moderate levels (0.2–0.4).

Pop_1's qBSeen stays low across most of the asymmetric grid (typically below 0.15), reaching substantial values only when asymmetry is small.

### The control baseline

Without mechanisms (control _), mean qBSeen ≈ 0.02 for both populations across the entire grid — cooperation cannot self-sustain at *g* = 1.0. All cooperation in the P mechanism is driven by partner choice.

---

## Cross-Benefit Payoffs and Deterministic Role Assignment

From the simulation source (calculate_derived_globals.c), at *g* = 1.0 the payoff structure is:

- Pop_0: R₀ − P₀ = *b*₁ − *c*₀
- Pop_1: R₁ − P₁ = *b*₀ − *c*₁
- T − R = P − S = 1 for both (constant)

Since *b*₁ − *c*₀ > *b*₀ − *c*₁ in the analyzed heatmap region, **population 0 always has a higher cooperation incentive than population 1**. This yields a deterministic role split:

In the asymmetric region: pop_0 (lower *b* − *c*) cooperates more than pop_1 in **97.1%** of cells (204/210). Pop_0 has lower fitness in 93.3% of cases — the cooperating population is exploited.

### Why the lower *b* − *c* population cooperates

The result is initially counterintuitive: the population whose organisms produce *less* benefit is the one that cooperates. But under cross-benefit payoffs, what matters is not what you give but what you receive. Pop_0's cooperation is rewarded by pop_1's high *b*₁ (large R₀), while pop_1's cooperation is rewarded by pop_0's low *b*₀ (small R₁). Pop_0 has more to gain from mutual cooperation because its partner is more "valuable."

---

## The Partner Choice Bottleneck

Despite pop_0's high cooperation incentive, its actual cooperation level is limited by a bottleneck: partner choice requires C1P1 individuals on **both** sides of the swap (well-mixed simulations—**cross-population matching**, not distance or neighborhoods).

Pop_1's low R − P (= *b*₀ − *c*₁) means pop_1 evolves few C1P1 individuals. Without pop_1 C1P1s, pop_0 cannot execute swaps — even though pop_0 has strong incentive to cooperate.

This explains why **cooperation scales primarily with the smaller of the two *b* − *c* values**:

| *b*₀ − *c* effect (at fixed *b*₁ − *c* = 8.0)     | Observed cooperation           |
| ----------------------------------------- | ------------------------------ |
| *b*₀ − *c* = 0.008                            | qBSeen₀ = 0.32, qBSeen₁ = 0.05 |
| *b*₀ − *c* = 0.25                             | qBSeen₀ = 0.40, qBSeen₁ = 0.06 |
| *b*₀ − *c* = 1.0                              | qBSeen₀ = 0.60, qBSeen₁ = 0.09 |
| *b*₀ − *c* = 4.0                              | qBSeen₀ = 0.85, qBSeen₁ = 0.14 |
| *b*₀ − *c* = 5.66                             | qBSeen₀ = 0.90, qBSeen₁ = 0.17 |

Pop_0's cooperation rises from 0.32 to 0.90 as *b*₀ − *c* increases — not because pop_0's own incentive changes (*b*₁ − *c* = 8.0 throughout), but because pop_1's C1P1 frequency rises with *b*₀ − *c*, relieving the bottleneck.

Within-slice correlations confirm this: at fixed *b*₁ − *c*, the correlation between qBSeen₀ and log₂(*b*₀ − *c*) is 0.79–0.92. At fixed *b*₀ − *c*, the correlation with log₂(*b*₁ − *c*) is weaker and can even be negative (−0.46 at *b*₀ − *c* = 0.25), because increasing the asymmetry locks in the cooperator/defector roles more firmly rather than raising overall cooperation.

---

## Genotype Composition

### Pop_0 (cooperator)

In the high-cooperation region (*b*₀ − *c* ≥ 1.0, asymmetric cells):
- **C1P1** (cooperating choosers): mean 0.654 — dominant genotype
- **C1P0** (cooperators without partner choice — behavioral free-riders who do not sort partners): mean 0.057 (7.7% of cooperators)
- C0P1 + C0P0 (defectors): remainder

As asymmetry decreases (increasing *b*₀ − *c* at fixed high *b*₁ − *c*), C1P0 grows from ~0.02 (at *b*₀ − *c* = 0.008) to ~0.14 (at *b*₀ − *c* = 5.66): at high *R* − *P*, a small chooser subpopulation can support a high-cooperation regime, so the P1 allele is **diluted** (many C1P0) even though partner choice still underwrites the pool.

**Grid averages only** here (no full ***_1run** triangle). Asymmetric-region **mutualism** would need its own timed runs mainly for **bottleneck** timing — see **prisoners.md** for invasion vs equilibrium methodology; **end-of-run–only** dense output if timestep count grows.

### Pop_1 (defector)

Pop_1 is dominated by defectors: C0P1 (mean 0.46) and C0P0 (mean 0.43). The P1 allele in pop_1 is phenotypically silent (C0P1 = defector carrying chooser allele = hitchhiker), consistent with neutral drift of the P allele in a defecting population.

---

## Fitness and Exploitation

The cooperating population (pop_0, asymmetric cells) has **lower fitness** in 93.3% of asymmetric cells, with a mean fitness deficit of 0.31. Cooperators pay costs that benefit their defecting partners.

The fitness gap widens as asymmetry decreases. At extreme parameter ratios (*b*₁ − *c* / *b*₀ − *c* > 100), the gap is modest (wmean₁ − wmean₀ ≈ 0.15) because cooperation levels are low overall. The gap is largest in low-asymmetry, high-*b* regions where cooperation is high and exploitation is most effective.

---

## Regime map across given folders

For interpretation across runs, it helps to separate three folder-level regimes:

| given folder | Effective game family in these studies | Interpretation use |
| ----- | ----- | ----- |
| 1.0 | Prisoner's Dilemma family | Main mutualism/Hamilton dilemma readout |
| 0.5 | Mixed: PD in part of the grid, harmony-like orderings in other cells | Diagnostic regime map for mechanism validation |
| 1.5 | Snowdrift branch (cost-based equations) | Extension/comparison only; re-derive interpretation |

Important naming note: 1.5 is used here as a **folder/branch marker** for the code path switch (given >= 1.5), not as the same biological mixing parameter interpretation used in the Hamilton-benefit branch (given < 1.5).

---

## Given = 0.5: Correct Game-Type Classification

Using the exact Hamilton-branch payoffs from calculate_derived_globals.c (given < 1.5), for a focal population with own x_self = b − c and partner x_partner:

- T = 2 + 0.5(1 + x_partner)
- R = 2 + 0.5(x_self + x_partner)
- P = 2
- S = 1 + 0.5(1 + x_self)

Equivalent differences:

- T − R = 0.5(1 - x_self)
- P − S = 0.5(1 - x_self)
- R − S = 0.5(1 + x_partner)

So the focal game family is controlled by x_self around 1.0, while cross-population asymmetry (x_partner vs x_self) can yield additional orderings beyond simple PD/harmony.

On the triangular mutualism grid (shuffle_cost12_128, mechanism P, given = 0.5, 231 cells):

### Population 0 (x_self = x0, x_partner = x1, with x1 >= x0)

| Ordering | Cells |
| -------- | ----- |
| T > R > P > S | 203 |
| R > T > S > P | 21 |
| T = R > P = S | 6 |
| R = T > P = S | 1 |

### Population 1 (x_self = x1, x_partner = x0)

| Ordering | Cells |
| -------- | ----- |
| T > R > P > S | 105 |
| R > S > T > P | 68 |
| R > T > S > P | 42 |
| T = R > P = S | 15 |
| R > T = S > P | 1 |

This corrects the simplified two-regime view: at given = 0.5, mutualism includes a large R > S > T > P region (especially for population 1) created by cross-benefit asymmetry.

## Why g = 0.5 Helps Interpret g = 1.0

The g = 0.5 results show directly that mutualism cannot be interpreted as one global game type across the triangle: local orderings differ by cell and by population. Once those local regimes are mapped, the observed cooperation and fitness asymmetries become predictable from the cross-benefit structure and chooser bottleneck. This provides a stronger causal baseline for reading g = 1.0, where the same mechanisms operate but with a different regime mix.

In short, g = 0.5 functions as a diagnostic case that validates the interpretation framework used at g = 1.0 (local payoff ordering -> genotype bottlenecks -> qBSeen/wmean patterns). For the reusable workflow, see instructions.md §6.

Scope note from the snowdrift extension: the interpretation above is specific to the Hamilton/mutualism benefit branch (given < 1.5), where g has direct biological meaning in the payoff construction. In the snowdrift branch (given >= 1.5), calculate_derived_globals.c uses different cost-based equations and removes this same cross-benefit g interpretation, so conclusions must be re-derived rather than transferred.

## Given = 1.5: Snowdrift-Branch Interpretation

At given = 1.5, mutualism is no longer in the cross-benefit Hamilton branch. From calculate_derived_globals.c (cost/snowdrift branch), with x0 = b_c_0, x1 = b_c_1, k0 = 2, k1 = 1:

- pop_0: T0 = 3, R0 = 2.5 + 0.5x0, P0 = 2, S0 = 2 + x0
- pop_1: T1 = 3, R1 = 2.5 + 0.5x1, P1 = 2, S1 = 2 + x1

Key structural shift relative to given < 1.5: there is no cross-benefit coupling. Each population's local game is set by its **own** b_c, not by the partner's.

### Local regime map (231-cell triangle, x1 >= x0)

For each population i:

- x_i < 1: T_i > R_i > S_i > P_i
- x_i = 1: T_i = R_i = S_i > P_i
- x_i > 1: S_i > R_i > T_i > P_i

Observed counts:

- **pop_0**: 203 T>R>S>P, 7 boundary, 21 S>R>T>P
- **pop_1**: 105 T>R>S>P, 15 boundary, 111 S>R>T>P

Because x1 >= x0, pop_1 sits in the high-x (S>R>T>P) regime much more often than pop_0, which reverses the dominant role pattern seen at given = 1.0.

### Outcomes (shuffle_cost12_128, mechanism P, pop_2)

- pop_0 mean: qBSeen = 0.125, wmean = 9.450
- pop_1 mean: qBSeen = 0.835, wmean = 5.072
- pop_0 is more cooperative in only **5.2%** of cells (12/231)
- pop_0 has lower fitness in only **5.2%** of cells (12/231)
- mean gaps (pop_0 - pop_1): ΔqBSeen = -0.710, Δwmean = +4.378

So at given = 1.5, the given = 1.0 asymmetric narrative flips: the more cooperative side is typically pop_1, while the higher-fitness side is typically pop_0.

### Regime-combination decomposition (why the flip is systematic)

Because cells are triangular (x1 >= x0), populations occupy ordered regime combinations:

- (TRSP, TRSP): 105 cells
- (TRSP, boundary): 14 cells
- (TRSP, SRTP): 84 cells
- (boundary, boundary): 1 cell
- (boundary, SRTP): 6 cells
- (SRTP, SRTP): 21 cells

The key pattern is not just a global mean but a per-combination reversal:

- In (TRSP, SRTP) (84 cells), pop_0 stays near defection (qBSeen_0 = 0.025) while pop_1 is near full cooperation (qBSeen_1 = 0.983), with large fitness inversion (wmean_0 - wmean_1 = +4.749).
- In (TRSP, TRSP) (105 cells), both are more mixed, but pop_1 still cooperates more (0.687 vs 0.212) and pop_0 still has higher fitness (+4.070).
- Even in (SRTP, SRTP) (21 cells), cooperation remains higher in pop_1 (0.872 vs 0.159) with pop_0 fitter (+2.500), so the flip is not restricted to a single regime block.

Only the single (boundary, boundary) cell behaves symmetrically enough to soften the pattern (ΔqBSeen = +0.124, Δwmean = -0.991).

### Gradient and asymmetry diagnostics

Across all 231 cells:

- corr(ΔqBSeen, Δwmean) = -0.699 (strong exploitation signature)
- qBSeen_1 tracks x1 strongly (corr with log2(x1) = +0.811)
- qBSeen_0 falls as partner axis x1 rises (corr with log2(x1) = -0.658)

Across asymmetric cells only (x1 > x0, 210 cells), asymmetry strengthens with ratio:

- low asymmetry bin: ΔqBSeen = -0.587, Δwmean = +3.850
- mid asymmetry bin: ΔqBSeen = -0.807, Δwmean = +5.515
- high asymmetry bin: ΔqBSeen = -0.947, Δwmean = +5.135

So increasing asymmetry mostly drives sharper cooperation separation, while fitness advantage for the less cooperative side remains large throughout.

### Genotype composition under given = 1.5

The role flip appears directly in chooser composition:

- pop_0 means: C1P1 = 0.075, C1P0 = 0.050
- pop_1 means: C1P1 = 0.439, C1P0 = 0.396

Both chooser and non-chooser cooperators concentrate in pop_1, while pop_0 remains chooser-poor. This is the opposite of given = 1.0, where cross-benefit coupling pushed the lower-b_c side toward chooser-heavy cooperation.

### Dynamic anchor from snowdrift_1run

mutualism does not yet have a full *_1run triangular movie analysis for given = 1.5, so dynamics are interpreted with snowdrift_1run as a process-level anchor:

- rapid invasion from all-defection is common (pop_1 mean start qBSeen = 0.0, mean end 0.947)
- late-step changes are small (pop_1 mean absolute final-step change 0.011; only 2.9% of cells exceed 0.05)

This supports reading the given = 1.5 mutualism endpoints as stable snowdrift-branch outcomes rather than unresolved transients, while leaving open a dedicated mutualism 1run follow-up for full triangular timing.

### Relation to the standalone snowdrift study

This is consistent with snowdrift.md: high cooperation can coexist with exploitation asymmetry, and cooperation level is not a reliable proxy for higher fitness in cross-population settings. The given = 1.5 mutualism results should therefore be read as snowdrift-branch behavior under mutualism parameter geometry, not as a continuation of the given = 1.0 cross-benefit mechanism.

## Summary

| Topic | Headline figures (detail above) |
| ----- | --------------------------------- |
| **Cross-benefit, own-cost** | Pop_0's **R − P** = *b*₁ − *c*₀; pop_1's = *b*₀ − *c*₁; **T − R = P − S = 1** |
| **Roles** | Pop_0 cooperates **97.1%** (204/210) across asymmetric cells (*b*₁ − *c* > *b*₀ − *c*) |
| **Bottleneck** | **qBSeen₀** rises **0.32 → 0.90** as *b*₀ − *c* rises (fixed *b*₁ − *c* = 8.0 table); **log₂**(*b*₀ − *c*) vs **qBSeen₀** **0.79–0.92** at fixed *b*₁ − *c* |
| **Fitness** | Cooperating pop lower fitness **93.3%** across asymmetric cells; mean deficit **0.31** |
| **Genotypes (pop_0)** | **C1P1** mean **0.654**; **C1P0** **7.7%** of cooperators (high-*b* region); **C1P0** up to **~14%** in low-asymmetry slices |
| **Given = 1.5 (snowdrift branch)** | No cross-benefit coupling; pop_1 more cooperative in **94.8%** of cells (219/231), while pop_0 higher fitness in **94.8%** (219/231); mean gaps (pop_0-pop_1): **ΔqBSeen -0.710**, **Δwmean +4.378** |
