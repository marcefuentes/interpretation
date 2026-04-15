# Mutualism — Partner Choice (P) Analysis

Study: `mutualism`, mechanism `P`, given = 1.0, pop_2 only.

Reference: `instructions_mutualism.md` for game parameters and payoff structure; `instructions.md` for shared model.

---

## Overview

The mutualism study generalizes Hamilton from a 1D axis (*b* − *c*) to a 2D triangular grid where the two coevolving populations can have **different** benefit-cost parameters (*b*₀ − *c* and *b*₁ − *c*). The diagonal (*b*₀ − *c* = *b*₁ − *c*) recovers Hamilton exactly.

The key structural difference: each population's cooperation benefit (R − P) is set by the **partner's** *b* − *c*, not its own (cross-benefit payoffs). Since *b*₁ − *c* ≥ *b*₀ − *c* by construction, population 0 always faces a cooperation incentive at least as strong as population 1's.

---

## The Cooperation Landscape

Cooperation (qBSeen) in pop_0 increases with both *b*₀ − *c* and *b*₁ − *c*, but not symmetrically. At the highest parameters the cooperating population reaches qBSeen ≈ 0.90.

The heatmap for pop_0 shows a smooth gradient from ~0.04 (both *b* − *c* low) to ~0.90 (both high), with most of the variation concentrated along the diagonal and near-diagonal region. Far from the diagonal (large asymmetry), cooperation plateaus at moderate levels (0.2–0.4).

Pop_1's qBSeen stays low across most of the grid (typically below 0.15 off-diagonal), reaching substantial values only near the diagonal.

### The control baseline

Without mechanisms (control `_`), mean qBSeen ≈ 0.02 for both populations across the entire grid — cooperation cannot self-sustain at *g* = 1.0. All cooperation in the P mechanism is driven by partner choice.

---

## Cross-Benefit Payoffs and Deterministic Role Assignment

From the simulation source (`calculate_derived_globals.c`), at *g* = 1.0 the payoff structure is:

- Pop_0: R₀ − P₀ = *b*₁ − *c* (partner's parameter)
- Pop_1: R₁ − P₁ = *b*₀ − *c* (partner's parameter)
- T − R = P − S = 2 for both (constant)

Since *b*₁ − *c* ≥ *b*₀ − *c*, **population 0 always has at least as high a cooperation incentive as population 1**. This breaks the symmetry that exists in Hamilton and produces a deterministic outcome:

**Off-diagonal**: pop_0 (lower *b* − *c*) cooperates more than pop_1 in **97.1%** of cells (204/210). Pop_0 has lower fitness in 93.3% of cases — the cooperating population is exploited, just as in Hamilton.

**On the diagonal**: both populations face identical games (R − P equal), and the cooperator role is assigned essentially at random (10 vs 11 out of 21 cells), exactly matching Hamilton's stochastic symmetry breaking.

### Why the lower *b* − *c* population cooperates

The result is initially counterintuitive: the population whose organisms produce *less* benefit is the one that cooperates. But under cross-benefit payoffs, what matters is not what you give but what you receive. Pop_0's cooperation is rewarded by pop_1's high *b*₁ (large R₀), while pop_1's cooperation is rewarded by pop_0's low *b*₀ (small R₁). Pop_0 has more to gain from mutual cooperation because its partner is more "valuable."

---

## The Partner Choice Bottleneck

Despite pop_0's high cooperation incentive, its actual cooperation level is limited by a bottleneck: partner choice requires C1P1 individuals on **both** sides of the swap.

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
- **C1P0** (cooperating free-riders): mean 0.057 (7.7% of cooperators)
- C0P1 + C0P0 (defectors): remainder

As *b*₀ − *c* increases toward the diagonal, C1P0 grows from ~0.02 (at *b*₀ − *c* = 0.008) to ~0.14 (at *b*₀ − *c* = 5.66), matching Hamilton's pattern: when cooperation can partly self-sustain (high R − P), the chooser allele becomes dispensable and free-riders accumulate.

### Pop_1 (defector)

Pop_1 is dominated by defectors: C0P1 (mean 0.46) and C0P0 (mean 0.43). The P1 allele in pop_1 is phenotypically silent (C0P1 = defector carrying chooser allele = hitchhiker), consistent with neutral drift of the P allele in a defecting population.

---

## Diagonal: Consistency with Hamilton

On the diagonal (*b*₀ − *c* = *b*₁ − *c*), the game is identical to Hamilton. However, direct comparison of averaged qBSeen values is misleading because the file set assignment differs:

- **Hamilton**: `_0` = higher qBSeen (post-hoc sorted) → artificially separates cooperator and defector across runs
- **Mutualism**: `_0` and `_1` assigned randomly → averaging over runs blurs the asymmetry

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

## Summary

1. **Cross-benefit payoffs** determine the mutualism game structure: each population's R − P equals the partner's *b* − *c*. Pop_0 (lower *b* − *c*) has higher cooperation incentive because its partner provides larger benefits.

2. **Deterministic role assignment**: unlike Hamilton (stochastic), the payoff asymmetry causes pop_0 to cooperate in 97% of off-diagonal cells. The diagonal recovers Hamilton's random ~50/50 split.

3. **Partner choice bottleneck**: cooperation level scales primarily with the *smaller* of the two *b* − *c* values, because pop_1's low R − P limits the C1P1 individuals available for swaps. Pop_0's own high incentive cannot be realized without sufficient pop_1 cooperators.

4. **Genotype composition** matches Hamilton: C1P1 dominates the cooperating population, with C1P0 free-riders accumulating at high *b* − *c* (up to 7.7% of cooperators).

5. **Exploitation**: the cooperating population has lower fitness in 93.3% of off-diagonal cells, consistent with Hamilton's asymmetry pattern.

6. **Diagonal consistency**: mutualism's diagonal reproduces Hamilton's cooperation levels and transition threshold. Apparent differences in asymmetry magnitude are an artifact of unsorted vs sorted file set assignment.
