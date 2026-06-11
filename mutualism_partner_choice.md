# Mutualism — Partner Choice

Partner-choice analysis for the two-population mutualism study (mechanism **P**
only — no reciprocity locus). Pure reciprocity (M) is in
**mutualism_reciprocity.md**; combined mechanisms (MP, MPQ, IMP, IJMPQ) are in
**mutualism_combined.md**.

## Overview

Mutualism is the primary study: two populations with potentially different
costs interact exclusively across populations. Population 0 has cost c0 and
population 1 has cost c1, with c0 < c1 always (the plotted triangular grid
constrains c1 > c0). Benefit b = 0.40 is fixed and K = 0.50.

Hamilton is the diagonal special case where c0 = c1. This file develops
the asymmetric general case: because c0 < c1, population 0 always has a
higher cooperation incentive (R0 − P0 > R1 − P1) in both dilemma types.

The parameter space is a strict upper-triangular 20 × 20 grid:
c0 ∈ {0.00, 0.02, …, 0.38} and c1 ∈ {0.02, 0.04, …, 0.40} with c0 < c1,
giving 210 cells. Only pop_2 (cross-population pairing) is present. Analysis
covers dilemma 1 (prisoner's dilemma) and dilemma 2 (snowdrift), groupsize
128 noshuffle (primary) and groupsize 4 (dedicated section plus comparison);
shuffle conditions are included where noted.

## Payoff structure

See **[mutualism.md](mutualism.md#payoff-structure)** for the common payoff structure and control baseline. Under partner choice (P), dilemma 2 (snowdrift) adds little marginal lift for the lower-cost population (P mean = 0.956 vs control 0.955) but the asymmetric dynamics remain important for the higher-cost population and for fitness outcomes.

## Cooperation under partner choice (P)

### Dilemma 1 (PD)

Along the c0 = 0 column (pop_0 has zero cost), noshuffle, groupsize 128:

| Mech   | c1=0.02 | c1=0.10 | c1=0.18 | c1=0.26 | c1=0.34 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| \_     | 0.487   | 0.498   | 0.500   | 0.502   | 0.500   |
| P      | 0.961   | 0.864   | 0.791   | 0.735   | 0.710   |

Even with c0 = 0 (no cost to cooperate), fset_0 cooperation declines as c1
rises, because the bottleneck is driven by the partner population's low R1 − P1.

Cooperation landscape, mechanism P, fset_0:

| c0 \ c1 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------- | ------- | ------- | ------- | ------- |
| c0=0.00 | 0.864   | 0.770   | 0.722   | 0.672   |
| c0=0.10 | ---     | 0.600   | 0.369   | 0.183   |
| c0=0.20 | ---     | ---     | 0.405   | 0.133   |
| c0=0.30 | ---     | ---     | ---     | 0.044   |

### Dilemma 2 (snowdrift)

Along the c0 = 0 column, noshuffle, groupsize 128:

| Mech   | c1=0.02 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------ | ------- | ------- | ------- | ------- | ------- |
| \_     | 0.922   | 0.975   | 0.976   | 0.976   | 0.976   |
| P      | 0.961   | 0.977   | 0.977   | 0.977   | 0.978   |

Partner choice raises cooperation only at the lowest c1 (0.961 vs 0.922);
above c1 = 0.02 the control is already near ceiling and P adds negligible
lift for fset_0.

Cooperation landscape, mechanism P, fset_0:

| c0 \ c1 | c1=0.10 | c1=0.20 | c1=0.30 | c1=0.40 |
| ------- | ------- | ------- | ------- | ------- |
| c0=0.00 | 0.977   | 0.977   | 0.977   | 0.978   |
| c0=0.10 | ---     | 0.973   | 0.972   | 0.971   |
| c0=0.20 | ---     | ---     | 0.964   | 0.965   |
| c0=0.30 | ---     | ---     | ---     | 0.944   |

### Role split (both dilemmas)

For all 210 cells (noshuffle, gs=128, P mechanism), fset_0 (lower-cost
population) cooperates more than fset_1 in every single cell for both dilemma
types. The split is deterministic: since c0 < c1 always, pop_0 has higher
R − P.

Mean qBSeen across all 210 cells:

| Mech   | Dilemma | fset_0 (lower c0) | fset_1 (higher c1) |
| ------ | ------- | ----------------- | ------------------ |
| \_     | 1 (PD)  | 0.103             | 0.025              |
| P      | 1 (PD)  | 0.472             | 0.146              |
| \_     | 2 (SD)  | 0.955             | 0.091              |
| P      | 2 (SD)  | 0.956             | 0.096              |

In snowdrift, partner choice barely changes the cooperation means: the
snowdrift floor sustains high fset_0 cooperation without sorting, while
fset_1 remains near 0.10 regardless of mechanism.

## The partner choice bottleneck

### Dilemma 1 (PD)

Despite pop_0's cooperation incentive, its achievable cooperation is capped by
a bottleneck: partner-choice swaps require C1P1 individuals on both sides of
the exchange. Population 1's low R1 − P1 = b − c1 means it evolves few C1P1
individuals. Without C1P1 counterparts in pop_1, pop_0 cannot execute swaps
even though it has strong incentive to cooperate.

Along the c0 = 0 column (P mechanism, noshuffle) — where pop_0 has the maximum
possible incentive (R0 − P0 = 0.40) — cooperation still falls as c1 rises
because the bottleneck is entirely on the partner side:

| c1   | R1-P1 | q\_fset0 | q\_fset1 |
| ---- | ----- | -------- | -------- |
| 0.02 | 0.38  | 0.961    | 0.642    |
| 0.10 | 0.30  | 0.864    | 0.122    |
| 0.20 | 0.20  | 0.770    | 0.054    |
| 0.30 | 0.10  | 0.722    | 0.033    |
| 0.40 | 0.00  | 0.672    | 0.023    |

Pop_0's cooperation falls from 0.961 to 0.672 as c1 rises from 0.02 to 0.40
— not because pop_0's own incentive changes (R0 − P0 = 0.40 throughout), but
because pop_1's C1P1 frequency collapses with rising c1. The correlation
between qBSeen_0 and R1 − P1 across all 210 cells is 0.90; the correlation
with the focal population's own incentive R0 − P0 is 0.67. The partner's
incentive explains more variance than the focal's own.

### Dilemma 2 (snowdrift)

The bottleneck manifests differently in snowdrift. Pop_0 cooperation is at
ceiling (~0.97) regardless of c1, so partner choice does not limit the
lower-cost population:

| c1   | R1-P1 | q\_fset0 | q\_fset1 |
| ---- | ----- | -------- | -------- |
| 0.02 | 0.39  | 0.961    | 0.818    |
| 0.10 | 0.35  | 0.977    | 0.176    |
| 0.20 | 0.30  | 0.977    | 0.090    |
| 0.30 | 0.25  | 0.977    | 0.059    |
| 0.40 | 0.20  | 0.978    | 0.045    |

Pop_0 stays near 0.97 while pop_1's cooperation collapses from 0.818 to 0.045
as c1 rises. The correlation between qBSeen_0 and R1 − P1 is −0.01 (no
bottleneck on pop_0). Instead, the constraint operates on pop_1: when pop_0
cooperates heavily, pop_1's defectors receive T1 = R1 (the shared benefit b
arrives regardless), eliminating the marginal payoff advantage of cooperating.
Pop_1 defects even though S1 > P1 holds throughout.

Partner choice provides almost no benefit for pop_1 in snowdrift: at
(c0=0.1, c1=0.3), P gives fset_1 = 0.061 vs control 0.057. The bottleneck
is not swap scarcity but payoff structure — sorting cannot overcome the
free-rider advantage when the partner population is already cooperating at
ceiling.

## Exploitation: the paradox of success

Population 0 cooperates more but often earns less. The correlation between
ΔqBSeen (qBSeen_0 − qBSeen_1) and Δfitness (w0 − w1):

| Mech   | Dilemma | noshuffle | shuffle |
| ------ | ------- | --------- | ------- |
| \_     | 1 (PD)  | -1.000    | -1.000  |
| P      | 1 (PD)  | -0.986    | -0.986  |
| \_     | 2 (SD)  | -0.148    | -0.141  |
| P      | 2 (SD)  | -0.144    | -0.165  |

In PD, the cooperation/fitness link is nearly deterministic: pop_0 cooperates
more and earns less in 199/210 cells (mean fitness deficit = 0.140). In
snowdrift, the correlation is weak (−0.144) because the snowdrift payoff
structure sustains high cooperation without the same fitness penalty; pop_0
has lower fitness in 187/210 cells with a smaller mean deficit (0.104).

### Exploitation at the cell level (P mechanism, c0=0.1)

**Dilemma 1 (PD):**

| c1   | qBSeen_0 | qBSeen_1 | w\_0  | w\_1  |
| ---- | -------- | -------- | ----- | ----- |
| 0.12 | 0.759    | 0.304    | 0.544 | 0.765 |
| 0.16 | 0.694    | 0.216    | 0.515 | 0.742 |
| 0.20 | 0.600    | 0.187    | 0.513 | 0.701 |
| 0.30 | 0.369    | 0.101    | 0.502 | 0.616 |
| 0.40 | 0.183    | 0.046    | 0.498 | 0.553 |

Population 0 cooperates 2–4× more than population 1, yet earns less fitness.
At (c0=0.1, c1=0.12), w\_1/w\_0 = 1.41. As c1 increases, the exploitation
ratio narrows: at (c0=0.1, c1=0.40), w\_1/w\_0 = 1.11.

**Dilemma 2 (snowdrift):**

| c1   | qBSeen_0 | qBSeen_1 | w\_0  | w\_1  |
| ---- | -------- | -------- | ----- | ----- |
| 0.12 | 0.896    | 0.238    | 0.806 | 0.869 |
| 0.20 | 0.973    | 0.089    | 0.795 | 0.879 |
| 0.30 | 0.972    | 0.061    | 0.794 | 0.879 |
| 0.40 | 0.971    | 0.044    | 0.792 | 0.878 |

The cooperation gap is far larger (16× at c1=0.30) but fitness differences
are smaller and more stable across c1. Pop_1 earns more despite cooperating
at a fraction of pop_0's rate, because snowdrift payoffs reward the
defecting high-cost population when paired against abundant cooperators.

### Mechanism comparison at sample cells

| Mech   | Dilemma | (0.1, 0.2) fset_0 | (0.1, 0.2) fset_1 | (0.1, 0.3) fset_0 | (0.1, 0.3) fset_1 |
| ------ | ------- | ----------------- | ----------------- | ----------------- | ----------------- |
| \_     | 1 (PD)  | 0.051             | 0.026             | 0.047             | 0.018             |
| P      | 1 (PD)  | 0.600             | 0.187             | 0.369             | 0.101             |
| \_     | 2 (SD)  | 0.972             | 0.089             | 0.972             | 0.057             |
| P      | 2 (SD)  | 0.973             | 0.089             | 0.972             | 0.061             |

In PD, partner choice creates substantial cooperation where the control
fails. In snowdrift, the control already sustains high fset_0 cooperation
and partner choice changes outcomes only marginally.

## Genotype composition

Under the P mechanism (noshuffle, gs=128), averaged across all 210 cells:

**Dilemma 1 (PD):**

| Genotype | Pop_0 (lower cost) | Pop_1 (higher cost) |
| -------- | ------------------ | ------------------- |
| C1P1     | 0.382              | 0.126               |
| C1P0     | 0.090              | 0.020               |
| C0P1     | 0.304              | 0.442               |
| qBSeen   | 0.472              | 0.146               |

Pop_0 is dominated by C1P1 (active choosers) and C0P1. Pop_1 is dominated by
C0P1 (0.443) — defectors carrying the P1 allele silently. This is the
hitchhiking pattern: mutations from C1P1 generate C0P1 that persist as neutral
carriers.

In the high-cooperation region (c0 < 0.10, c1 < 0.20): pop_0 C1P1 rises
to 0.58 while pop_0 C1P0 averages ≈ 0.22 (roughly 22% of cooperators are
non-chooser free-riders on the cooperator pool). At high asymmetry
(c1 > 0.30), pop_0 C1P0 falls to near zero — when c1 is large, only C1P1
individuals can sustain cooperation and non-chooser cooperators are selected
out.

**Dilemma 2 (snowdrift):**

| Genotype | Pop_0 (lower cost) | Pop_1 (higher cost) |
| -------- | ------------------ | ------------------- |
| C1P1     | 0.472              | 0.048               |
| C1P0     | 0.484              | 0.048               |
| C0P1     | 0.022              | 0.446               |
| qBSeen   | 0.956              | 0.096               |

The genotype structure inverts relative to PD. Pop_0 cooperators are split
almost evenly between C1P1 (0.472) and C1P0 (0.484) — the sparse-choosers
pattern: a thin C1P1 layer sustains a high-cooperation pool of behavioral
free-riders. Pop_1 retains the C0P1 hitchhiking signature (0.446) with very
few active choosers (C1P1 = 0.048).

In the high-cooperation region (c0 < 0.10, c1 < 0.20), pop_0 C1P1 ≈ 0.47
and C1P0 ≈ 0.49 — roughly half of cooperators carry P0 and do not sort
partners, because the snowdrift floor makes chooser density unnecessary for
sustaining cooperation.

## Groupsize 4

All mutualism runs use pop_2 only. Unless noted, tables are noshuffle,
fset_0 (lower-cost population).

### Partner choice at gs=4

Mean qBSeen across all 210 cells:

| Dilemma | Mech   | fset_0 (lower c0) | fset_1 (higher c1) | fset_0 > fset_1 |
| ------- | ------ | ----------------- | ------------------ | --------------- |
| 1 (PD)  | P      | 0.204             | 0.046              | 209/210         |
| 2 (SD)  | P      | 0.959             | 0.092              | 210/210         |

In PD, the role split holds in 209/210 cells but cooperation levels collapse
outside the smallest cost cells. In snowdrift, fset_0 remains near ceiling
(0.959 vs 0.956 at gs=128) and partner choice stays functional across the
grid.

### Partner bottleneck at gs=4

Along the c0 = 0 column (P mechanism):

**Dilemma 1 (PD):**

| c1   | qBSeen fset_0 | qBSeen fset_1 |
| ---- | ------------- | ------------- |
| 0.02 | 0.932         | 0.620         |
| 0.10 | 0.849         | 0.122         |
| 0.20 | 0.743         | 0.050         |
| 0.30 | 0.680         | 0.032         |
| 0.40 | 0.632         | 0.022         |

Pop_0 cooperation falls as c1 rises even with zero own cost — the same
bottleneck logic as gs=128. Partner choice barely functions beyond mild
asymmetry: at (c0, c1) = (0.10, 0.30), qBSeen = 0.049.

**Dilemma 2 (snowdrift):**

| c1   | qBSeen fset_0 | qBSeen fset_1 |
| ---- | ------------- | ------------- |
| 0.02 | 0.942         | 0.742         |
| 0.10 | 0.975         | 0.180         |
| 0.20 | 0.977         | 0.087         |
| 0.30 | 0.977         | 0.058         |
| 0.40 | 0.977         | 0.046         |

Fset_0 stays near ceiling regardless of c1. The bottleneck affects only
fset_1, as at gs=128.

### Exploitation at gs=4

| Dilemma | Mech   | noshuffle | shuffle |
| ------- | ------ | --------- | ------- |
| 1 (PD)  | P      | -0.998    | -0.998  |
| 2 (SD)  | P      | -0.178    | -0.171  |

The exploitation paradox persists at gs=4 for PD. In snowdrift the correlation
remains weak, matching the gs=128 pattern.

## Groupsize comparison (gs=4 vs gs=128)

All comparisons are noshuffle, pop_2, fset_0 (lower-cost population).

### Partner choice (P) — PD collapses at gs=4; snowdrift robust

**Dilemma 1 (PD):** The P mechanism fails at gs=4 for all but the smallest
cost cells. Near the diagonal, the threshold drops to c0 ≈ 0.08:

| c0   | c1   | gs=4  | gs=128 |
| ---- | ---- | ----- | ------ |
| 0.00 | 0.02 | 0.932 | 0.961  |
| 0.06 | 0.08 | 0.820 | 0.845  |
| 0.08 | 0.10 | 0.778 | 0.780  |
| 0.10 | 0.12 | 0.059 | 0.759  |
| 0.20 | 0.22 | 0.026 | 0.636  |
| 0.30 | 0.32 | 0.016 | 0.500  |

This mirrors the **hamilton_partner_choice.md** gs=4 finding: the chooser bottleneck is
catastrophically worsened by small groups, and partner choice becomes
effectively non-functional throughout most of the parameter space.

**Dilemma 2 (snowdrift):** Partner choice is robust to groupsize reduction.
Cooperation stays high even at moderate asymmetry:

| c0   | c1   | gs=4  | gs=128 |
| ---- | ---- | ----- | ------ |
| 0.00 | 0.02 | 0.942 | 0.961  |
| 0.08 | 0.10 | 0.849 | 0.878  |
| 0.10 | 0.12 | 0.815 | 0.896  |
| 0.10 | 0.30 | 0.972 | 0.972  |
| 0.20 | 0.22 | 0.791 | 0.879  |
| 0.30 | 0.32 | 0.941 | 0.795  |

## Shuffle vs noshuffle

The partner choice mechanism (P) is almost completely insensitive to partner shuffling:

- **Dilemma 1 (PD):** 
  - Mean cooperation across all 210 cells under noshuffle is **0.472 / 0.146** (fset_0 / fset_1) vs. **0.470 / 0.146** under shuffle (gs=128). 
  - At groupsize 4, it is **0.204 / 0.046** under noshuffle vs. **0.201 / 0.046** under shuffle.
- **Dilemma 2 (SD):** 
  - Mean cooperation across all 210 cells under noshuffle is **0.956 / 0.096** vs. **0.956 / 0.097** under shuffle (gs=128).
  - At groupsize 4, it is **0.959 / 0.092** under noshuffle vs. **0.959 / 0.091** under shuffle.

This invariance occurs because partner choice operates dynamically on a per-step rematching basis within groups, rendering any initial random partner shuffling irrelevant.

## Summary

| Topic                      | PD (dilemma 1)                                                                        | Snowdrift (dilemma 2)                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| P vs control (fset_0 mean) | 0.472 vs 0.103 — partner choice essential                                             | 0.956 vs 0.955 — marginal lift; snowdrift floor dominates                             |
| Role split                 | fset_0 > fset_1 in 210/210 cells                                                      | fset_0 > fset_1 in 210/210 cells                                                      |
| Bottleneck                 | Pop_0 capped by pop_1's C1P1; corr(qB0, R1-P1) = 0.90                                 | Pop_0 at ceiling; pop_1 defects because T1 = R1 when partner cooperates               |
| Exploitation               | Pop_0 lower fitness in 199/210 cells; mean deficit = 0.140; corr = −0.986             | Pop_0 lower fitness in 187/210 cells; mean deficit = 0.104; corr = −0.144             |
| Genotypes pop_0            | C1P1-dominated choosers (0.382); C1P0 free-riders at 9%                               | Sparse choosers: C1P1 ≈ C1P0 ≈ 0.47 each                                              |
| Genotypes pop_1            | C0P1 hitchhikers dominate (0.442)                                                     | Same hitchhiking pattern (C0P1 = 0.446); few choosers (C1P1 = 0.048)                  |
| gs=4 P mechanism           | Collapses by c0/c1 ≈ 0.10                                                             | Robust; fset_0 ≈ 0.96 at (0.1, 0.3) for both groupsizes                               |
| gs=4 exploitation (P)      | corr = −0.998                                                                         | corr = −0.178 — weak, as at gs=128                                                    |
