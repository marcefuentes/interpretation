# Mutualism Game — Game-Specific Instructions

**Prerequisite**: Read `instructions.md` first for the shared simulation model.

---

## 1. Game Parameters

The mutualism game uses the same Hamilton altruism payoff structure but allows the two coevolving populations to have **different** benefit-cost parameters. Each population *i* has its own *b*_*i* − *c*, while the cost *c* = 1.0 is shared.

| Parameter | Value | Description |
|-----------|-------|-------------|
| *b*₀ − *c* | 0.008 – 8.0 | Net benefit-cost for population 0 (x-axis, log₂ scale: 2⁻⁷ to 2³) |
| *b*₁ − *c* | 0.008 – 8.0 | Net benefit-cost for population 1 (y-axis, same scale) |
| *c* | 1.0 | Cost (fixed; C_MIN) |
| *g* | 1.0 | Given parameter (full dilemma) |
| *K* | 2.0 | Baseline fitness (k0 = k1) |
| *B*_max | 9.0 | Maximum benefit (for fitness normalization) |
| groupsize | 128 | Individuals per group from each population |

The parameter space is a **triangular matrix**: only cells where *b*₁ − *c* ≥ *b*₀ − *c* are simulated (21 × 21 grid, 231 cells). The **diagonal** (*b*₀ − *c* = *b*₁ − *c*) is the Hamilton-equivalent special case where both populations face the same game.

Constants: same as Hamilton — `B_MAX = 9.0`, `C_MIN = 1.0`, `K = 2.0` (from `theory.py`).

---

## 2. Cross-Benefit Payoff Structure

The critical difference from Hamilton is that the two populations exchange **different** benefits. When population *i* cooperates, it produces benefit *b*_*i* and gives it to its partner from the other population. Each population's payoff therefore depends on the **partner's** *b* − *c*, not its own.

From `calculate_derived_globals.c`, at *g* = 1.0, with *b*₀ = *K* + (*b*₀ − *c*) and *b*₁ = *K* + (*b*₁ − *c*):

### Population 0's payoff matrix (receives *b*₁ from partner)

| Payoff | Formula | Value |
|--------|---------|-------|
| **T₀** | *K* + *b*₁ | 4 + (*b*₁ − *c*) |
| **R₀** | *K* + (*b*₁ − *c*) | 2 + (*b*₁ − *c*) |
| **P₀** | *K* | 2 |
| **S₀** | 0 | 0 |

### Population 1's payoff matrix (receives *b*₀ from partner)

| Payoff | Formula | Value |
|--------|---------|-------|
| **T₁** | *K* + *b*₀ | 4 + (*b*₀ − *c*) |
| **R₁** | *K* + (*b*₀ − *c*) | 2 + (*b*₀ − *c*) |
| **P₁** | *K* | 2 |
| **S₁** | 0 | 0 |

### Key relationships

| | Pop 0 | Pop 1 |
|--|-------|-------|
| **R − P** | *b*₁ − *c* (partner's) | *b*₀ − *c* (partner's) |
| **T − R** | 2 (constant) | 2 (constant) |
| **P − S** | 2 (constant) | 2 (constant) |

Since *b*₁ − *c* ≥ *b*₀ − *c* by construction (triangular matrix), **population 0 always has R − P ≥ population 1's R − P**. This asymmetry in cooperation incentives is the central feature of the mutualism study.

### Comparison with Hamilton

Hamilton is the diagonal of mutualism: *b*₀ − *c* = *b*₁ − *c*, so both populations face identical payoffs and R − P is equal. In Hamilton, which population cooperates is random (stochastic symmetry breaking). In mutualism off-diagonal, the payoff asymmetry makes role assignment deterministic (§3 of `mutualism.md`).

---

## 3. Population Scenario

Mutualism uses **only pop_2** (two coevolving populations). No pop_1 or pop_3 scenarios.

**File set assignment**: Unlike Hamilton (where `_0` = higher qBSeen, `_1` = lower qBSeen), mutualism assigns `_0` and `_1` **randomly** — they are not sorted by cooperation level. The manifest labels them as "Population 0" and "Population 1", with population 1 having higher *b*₁ − *c* values.

---

## 4. Loci and Genotypes

Same as Hamilton: **6 loci** (C, I, J, M, P, Q) → **64 genotype columns**. Column names: `C0I0J0M0P0Q0` through `C1I1J1M1P1Q1`.

---

## 5. Results Path

```
~/results/mutualism/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}/{population}/
```

Example: `~/results/mutualism/shuffle_cost12_128/P/1.0/pop_2/csv_0_for_image.con`

Available given values: 0.5, 1.0, 1.5 (only *g* = 1.0 analyzed here).

---

## 6. Data Format

Same as Hamilton (current 64-genotype format). CSV columns:
- `k, b_c_0, b_c_1` — game parameters
- `Time` — simulation timestep
- `wmean, wsd` — population mean fitness and stdev
- `qBSeen` — cooperation probability
- 64 genotype columns + SD columns

231 rows per file (triangular matrix, one per parameter cell).

---

## 7. Loading and Analysis

```python
import pandas as pd
import numpy as np

d0 = pd.read_csv('csv_0_for_image.con')
d1 = pd.read_csv('csv_1_for_image.con')

# Compute derived traits
def add_genotypes(df):
    c1p1 = [c for c in df.columns if c.startswith('C1') and 'P1' in c and not c.endswith('SD')]
    c1p0 = [c for c in df.columns if c.startswith('C1') and 'P0' in c and not c.endswith('SD')]
    df['C1P1'] = df[c1p1].sum(axis=1)
    df['C1P0'] = df[c1p0].sum(axis=1)
    return df

d0, d1 = add_genotypes(d0), add_genotypes(d1)

# Merge both populations on parameter cell
m = d0[['b_c_0','b_c_1','qBSeen','wmean','C1P1','C1P0']].merge(
    d1[['b_c_0','b_c_1','qBSeen','wmean','C1P1','C1P0']],
    on=['b_c_0','b_c_1'], suffixes=('_0','_1'))

# Heatmap (b_c_1 on y-axis descending, b_c_0 on x-axis)
pivot = m.pivot(index='b_c_1', columns='b_c_0', values='qBSeen_0')
pivot = pivot.reindex(index=sorted(pivot.index, reverse=True))
```

---

## 8. Figure Panel Mapping (s07)

MAIN_ROWS in `manifest.py` defines 2 rows:

| Row | Panels | Population | File_set | Notes |
|-----|--------|------------|----------|-------|
| 0 | a, b | pop_2 | _1 | Population 1 (higher *b*₁ − *c*) |
| 1 | c, d | pop_2 | _0 | Population 0 (lower *b*₀ − *c*) |

Each panel is a **heatmap** with *b*₀ − *c* on the x-axis and *b*₁ − *c* on the y-axis (triangular matrix, imshow renderer).

Legend footer: "Population 1 has higher values of (*b* − *c*)."

---

## 9. Key Findings

See `mutualism.md` for full analysis.
