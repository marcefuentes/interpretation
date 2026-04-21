# Mutualism — Partner Choice (P) Analysis

Study: mutualism, mechanism P, given = 1.0, pop_2 only.

Reference: instructions_mutualism.md for game parameters and payoff structure; instructions.md for shared model.

---

## Overview

The mutualism study generalizes Hamilton from a 1D axis (*b* − *c*) to a 2D triangular grid where the two coevolving populations can have **different** benefit-cost parameters (*b*₀ − *c* and *b*₁ − *c*). The diagonal (*b*₀ − *c* = *b*₁ − *c*) **is** Hamilton (same game — **Diagonal: Consistency with Hamilton**).

**Cross-benefit payoffs** and the **bottleneck** story are developed once in the next sections; the **Summary** table lists the main **percentages and correlations** for quick reference. For **P**-mechanism definitions, see **instructions.md** and **instructions_mutualism.md**.

**Groupsize.** Grid cooperation levels and tables below use **shuffle_cost12_128**. **shuffle_cost12_4** collapses **qBSeen** relative to **128** on the same parameter grid (cross-benefit and **bottleneck** logic still apply; **numeric** claims do not). See **hamilton.md** for **hamilton_1run** end-state and **movie** detail.

The key structural difference: each population's **R − P** is set by the **partner's** *b* − *c*. Since *b*₁ − *c* ≥ *b*₀ − *c*, population 0 always has at least as strong a cooperation incentive as population 1.

---

## The Cooperation Landscape

Cooperation (qBSeen) in pop_0 increases with both *b*₀ − *c* and *b*₁ − *c*, but not symmetrically. At the highest parameters the cooperating population reaches qBSeen ≈ 0.90.

The heatmap for pop_0 shows a smooth gradient from ~0.04 (both *b* − *c* low) to ~0.90 (both high), with most of the variation concentrated along the diagonal and near-diagonal region. Far from the diagonal (large asymmetry), cooperation plateaus at moderate levels (0.2–0.4).

Pop_1's qBSeen stays low across most of the grid (typically below 0.15 off-diagonal), reaching substantial values only near the diagonal.

### The control baseline

Without mechanisms (control _), mean qBSeen ≈ 0.02 for both populations across the entire grid — cooperation cannot self-sustain at *g* = 1.0. All cooperation in the P mechanism is driven by partner choice.

---

## Cross-Benefit Payoffs and Deterministic Role Assignment

From the simulation source (calculate_derived_globals.c), at *g* = 1.0 the payoff structure is:

- Pop_0: R₀ − P₀ = *b*₁ − *c* (partner's parameter)
- Pop_1: R₁ − P₁ = *b*₀ − *c* (partner's parameter)
- T − R = P − S = 1 for both (constant)

Since *b*₁ − *c* ≥ *b*₀ − *c*, **population 0 always has at least as high a cooperation incentive as population 1**. This breaks the symmetry that exists in Hamilton and produces a deterministic outcome:

**Off-diagonal**: pop_0 (lower *b* − *c*) cooperates more than pop_1 in **97.1%** of cells (204/210). Pop_0 has lower fitness in 93.3% of cases — the cooperating population is exploited, just as in Hamilton.

**On the diagonal**: both populations face identical games (R − P equal), and the cooperator role is assigned essentially at random (10 vs 11 out of 21 cells), exactly matching Hamilton's stochastic symmetry breaking.

### Why the lower *b* − *c* population cooperates

The result is initially counterintuitive: the population whose organisms produce *less* benefit is the one that cooperates. But under cross-benefit payoffs, what matters is not what you give but what you receive. Pop_0's cooperation is rewarded by pop_1's high *b*₁ (large R₀), while pop_1's cooperation is rewarded by pop_0's low *b*₀ (small R₁). Pop_0 has more to gain from mutual cooperation because its partner is more "valuable."

---

## The Partner Choice Bottleneck

Despite pop_0's high cooperation incentive, its actual cooperation level is limited by a bottleneck: partner choice requires C1P1 individuals on **both** sides of the swap (well-mixed simulations—**cross-population matching**, not distance or neighborhoods).

Pop_1's low R − P (= *b*₀ − *c*) means pop_1 evolves few C1P1 individuals. Without pop_1 C1P1s, pop_0 cannot execute swaps — even though pop_0 has strong incentive to cooperate.

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

In the high-cooperation region (*b*₀ − *c* ≥ 1.0, off-diagonal):
- **C1P1** (cooperating choosers): mean 0.654 — dominant genotype
- **C1P0** (cooperators without partner choice — behavioral free-riders who do not sort partners): mean 0.057 (7.7% of cooperators)
- C0P1 + C0P0 (defectors): remainder

As *b*₀ − *c* increases toward the diagonal, C1P0 grows from ~0.02 (at *b*₀ − *c* = 0.008) to ~0.14 (at *b*₀ − *c* = 5.66), matching Hamilton's pattern: at high *R* − *P*, a small chooser subpopulation can support a high-cooperation regime, so the P1 allele is **diluted** (many C1P0) even though partner choice still underwrites the pool.

**Grid averages only** here (no full ***_1run** triangle). The **diagonal** is **hamilton_1run** territory for dynamics; off-diagonal **mutualism** would need its own timed runs mainly for **bottleneck** timing — **hamilton.md** / **prisoners.md** for invasion vs equilibrium methodology; **end-of-run–only** dense output if timestep count grows.

### Pop_1 (defector)

Pop_1 is dominated by defectors: C0P1 (mean 0.46) and C0P0 (mean 0.43). The P1 allele in pop_1 is phenotypically silent (C0P1 = defector carrying chooser allele = hitchhiker), consistent with neutral drift of the P allele in a defecting population.

---

## Diagonal: Consistency with Hamilton

On the diagonal (*b*₀ − *c* = *b*₁ − *c*), the game is identical to Hamilton. However, direct comparison of averaged qBSeen values is misleading because the file set assignment differs:

- **Hamilton**: _0 = higher qBSeen (post-hoc sorted) → artificially separates cooperator and defector across runs
- **Mutualism**: _0 and _1 assigned randomly → averaging over runs blurs the asymmetry

At *b* − *c* = 8.0:
- Hamilton (sorted): qBSeen₀ = 0.93, qBSeen₁ = 0.20
- Mutualism diagonal (unsorted): qBSeen₀ = 0.49, qBSeen₁ = 0.63

The mutualism values (~0.5–0.6) are consistent with averaging a cooperator at ~0.9 and a defector at ~0.2 across runs where each population is the cooperator roughly half the time.

At low *b* − *c* (< 0.125), both studies show near-zero cooperation (~0.04–0.09), and the transition to substantial cooperation occurs at the same threshold (*b* − *c* ≈ 0.125–0.177).

---

## Fitness and Exploitation

The cooperating population (pop_0 off-diagonal) has **lower fitness** in 93.3% of off-diagonal cells, with a mean fitness deficit of 0.31. This matches the exploitation pattern from Hamilton: cooperators pay costs that benefit their defecting partners.

The fitness gap widens with asymmetry. At extreme parameter ratios (*b*₁ − *c* / *b*₀ − *c* > 100), the gap is modest (wmean₁ − wmean₀ ≈ 0.15) because cooperation levels are low overall. The gap is largest near the diagonal at high *b* − *c*, where cooperation is high and exploitation is most effective.

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

## Summary

| Topic | Headline figures (detail above) |
| ----- | --------------------------------- |
| **Cross-benefit** | Pop_0's **R − P** = partner's *b*₁ − *c*; pop_1's = *b*₀ − *c*; **T − R = P − S = 1** |
| **Roles** | Pop_0 cooperates **97.1%** (204/210) off-diagonal cells; diagonal ~**50/50** like Hamilton |
| **Bottleneck** | **qBSeen₀** rises **0.32 → 0.90** as *b*₀ − *c* rises (fixed *b*₁ − *c* = 8.0 table); **log₂**(*b*₀ − *c*) vs **qBSeen₀** **0.79–0.92** at fixed *b*₁ − *c* |
| **Fitness** | Cooperating pop lower fitness **93.3%** off-diagonal; mean deficit **0.31** |
| **Genotypes (pop_0)** | **C1P1** mean **0.654**; **C1P0** **7.7%** of cooperators (high-*b* region); **C1P0** up to **~14%** along diagonal slice |
| **Diagonal vs Hamilton** | *b* − *c* = 8: sorted Hamilton **0.93 / 0.20** vs mutualism unsorted **0.49 / 0.63** — assignment artifact (**Diagonal** section) |
