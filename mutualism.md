# Mutualism

Analysis for the two-population mutualism study (pop_2, 210-cell upper triangle),
split by mechanism family:

- **[mutualism_partner_choice.md](mutualism_partner_choice.md)** — mechanism P: PD and
  snowdrift analysis of chooser bottleneck, genotypes, exploitation, groupsize effects
- **[mutualism_reciprocity.md](mutualism_reciprocity.md)** — mechanism M: PD and
  snowdrift cooperation landscapes, shuffle effects, groupsize comparisons
- **[mutualism_combined.md](mutualism_combined.md)** — mechanisms MP, MPQ, IMP,
  IJMPQ: partner choice plus reciprocity, mutualistic equilibrium, fset_1 lift

Hamilton is the equal-cost diagonal (c0 = c1); see **hamilton.md** (index to
hamilton_partner_choice.md, hamilton_reciprocity.md, and hamilton_combined.md).

**Parameter axes.** graphgen heatmaps plot c0 horizontally and c1 vertically
(upper triangle, c0 < c1). Markdown landscape tables in the sub-docs list c0
as rows and c1 as columns; a fixed-c0 slice is a heatmap column (left edge) but
the top row of those tables.

## Payoff structure

All payoffs use cross-benefit form: the benefit b is the contribution received
from the partner, while the cost c is paid by the focal individual. In
snowdrift, b is a shared resource: both players receive it whenever at least
one cooperates (b appears in T, R, and S).

### Dilemma 1 (PD, folder 1)

| Payoff | Pop 0          | Pop 1          |
| ------ | -------------- | -------------- |
| T      | K + b = 0.90   | K + b = 0.90   |
| R      | K + b - c0     | K + b - c1     |
| P      | K = 0.50       | K = 0.50       |
| S      | K - c0         | K - c1         |
| R - P  | b - c0         | b - c1         |

Since c0 < c1 in every cell: R0 − P0 = b − c0 > R1 − P1 = b − c1. Population
0 always has a stronger cooperation incentive than population 1.

### Dilemma 2 (snowdrift, folder 2)

| Payoff | Pop 0            | Pop 1            |
| ------ | ---------------- | ---------------- |
| T      | K + b = 0.90     | K + b = 0.90     |
| R      | K + b - c0/2     | K + b - c1/2     |
| P      | K = 0.50         | K = 0.50         |
| S      | K + b - c0       | K + b - c1       |
| R - P  | b - c0/2         | b - c1/2         |

In snowdrift, S > P for all c < 0.40 = b, so unilateral cooperation is always
better than mutual defection. The cooperation floor is high even without
mechanisms: the control (\_) reaches mean qBSeen_0 = 0.955.
