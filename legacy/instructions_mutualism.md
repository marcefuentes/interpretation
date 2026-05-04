# Mutualism Game — Game-Specific Instructions

**Prerequisite**: Read instructions.md first for the shared simulation model.

---

## 1. Game Parameters

The mutualism game uses the same Hamilton altruism payoff structure but allows the two coevolving populations to have **different** benefit-cost parameters. Each population *i* has its own *b*_*i* − *c*, while the cost *c* = 1.0 is shared.

| Parameter   | Value       | Description                                                       |
| ----------- | ----------- | ----------------------------------------------------------------- |
| *b*₀ − *c*  | 0.008 – 8.0 | Net benefit-cost for population 0 (x-axis, log₂ scale: 2⁻⁷ to 2³) |
| *b*₁ − *c*  | 0.008 – 8.0 | Net benefit-cost for population 1 (y-axis, same scale)            |
| *c*         | 1.0         | Cost (fixed; C_MIN)                                               |
| *g*         | 1.0         | Given parameter (full dilemma)                                    |
| *K*         | 2.0         | Baseline fitness (k0 = k1)                                        |
| *B*_max     | 9.0         | Maximum benefit (for fitness normalization)                       |
| groupsize   | 128         | Individuals per group from each population                        |

The parameter space is a **triangular matrix**: only cells where *b*₁ − *c* ≥ *b*₀ − *c* are simulated (21 × 21 grid, 231 cells). For the current heatmap analyses, the focus is the strict asymmetric subset *b*₁ − *c* > *b*₀ − *c* (210 cells).

Constants: same as Hamilton — B_MAX = 9.0, C_MIN = 1.0, K = 2.0 (from theory.py).

---

## 2. Cross-Benefit Payoff Structure

The critical difference from Hamilton is that the two populations exchange **different** benefits. When population *i* cooperates, it produces benefit *b*_*i* and gives it to its partner from the other population. Each population's payoff therefore has a cross-benefit, own-cost form: benefit from the partner population's *b*, cost from the focal population's *c*.

From calculate_derived_globals.c, at *g* = 1.0, with x0 = b0−c, x1 = b1−c, b0 = k1 + x0, and b1 = k1 + x1:

### Population 0's payoff matrix (receives *b*₁ from partner)

| Payoff   | Formula            | Value            |
| -------- | ------------------ | ---------------- |
| **T₀**   | *k0* + *b*₁        | 3 + (*b*₁ − *c*) |
| **R₀**   | *K* + (*b*₁ − *c*) | 2 + (*b*₁ − *c*) |
| **P₀**   | *K*                | 2                |
| **S₀**   | *k0* − *k1*        | 1                |

### Population 1's payoff matrix (receives *b*₀ from partner)

| Payoff   | Formula            | Value            |
| -------- | ------------------ | ---------------- |
| **T₁**   | *k0* + *b*₀        | 3 + (*b*₀ − *c*) |
| **R₁**   | *K* + (*b*₀ − *c*) | 2 + (*b*₀ − *c*) |
| **P₁**   | *K*                | 2                |
| **S₁**   | *k0* − *k1*        | 1                |

### Key relationships

|           | Pop 0                  | Pop 1                  |
| --------- | ---------------------- | ---------------------- |
| **R − P** | *b*₁ − *c*₀ | *b*₀ − *c*₁ |
| **T − R** | 1 (constant)           | 1 (constant)           |
| **P − S** | 1 (constant)           | 1 (constant)           |

Since *b*₁ − *c*₀ ≥ *b*₀ − *c*₁ by construction in the current analyzed matrix (with shared *c*), **population 0 always has R − P ≥ population 1's R − P**. This asymmetry in cooperation incentives is the central feature of the mutualism study.

### Asymmetry focus

In the analyzed asymmetric subset (*b*₁ − *c* > *b*₀ − *c*), the payoff asymmetry makes role assignment deterministic (§3 of mutualism.md).

---

## 3. Population Scenario

Mutualism uses **only pop_2** (two coevolving populations). No pop_1 or pop_3 scenarios.

**File set assignment**: Unlike Hamilton (where _0 = higher qBSeen, _1 = lower qBSeen), mutualism assigns _0 and _1 **randomly** — they are not sorted by cooperation level. The manifest labels them as "Population 0" and "Population 1", with population 1 having higher *b*₁ − *c* values.

---

## 4. Loci and Genotypes

Same as Hamilton: **6 loci** (C, I, J, M, P, Q) → **64 genotype columns**. Column names: C0I0J0M0P0Q0 through C1I1J1M1P1Q1.

---

## 5. Results Path


~/results/mutualism/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}/{population}/


Example: ~/results/mutualism/shuffle_cost12_128/P/1.0/pop_2/csv_0_for_image.con

Available given values: 0.5, 1.0, 1.5 (only *g* = 1.0 analyzed here).

---

## 6. Data Format

Same as Hamilton (current 64-genotype format). CSV columns:
- k, b_c_0, b_c_1 — game parameters
- Time — simulation timestep
- wmean, wsd — population mean fitness and stdev
- qBSeen — cooperation probability
- 64 genotype columns + SD columns

231 rows per file (triangular matrix, one per parameter cell).

---

## 7. Loading and Analysis

python
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


---

## 8. Figure Panel Mapping (s07)

MAIN_ROWS in manifest.py defines 2 rows:

| Row   | Panels   | Population   | File_set   | Notes                            |
| ----- | -------- | ------------ | ---------- | -------------------------------- |
| 0     | a, b     | pop_2        | _1         | Population 1 (higher *b*₁ − *c*) |
| 1     | c, d     | pop_2        | _0         | Population 0 (lower *b*₀ − *c*)  |

Each panel is a **heatmap** with *b*₀ − *c* on the x-axis and *b*₁ − *c* on the y-axis (triangular matrix, imshow renderer).

Legend footer: "Population 1 has higher values of (*b* − *c*)."

---

## 9. Key Findings

See mutualism.md for full analysis.
