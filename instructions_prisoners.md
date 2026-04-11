# Prisoner's Dilemma — Game-Specific Instructions

**Prerequisite**: Read `instructions.md` first for the shared simulation model.

---

## 1. Game Parameters

Standard Prisoner's Dilemma with **T = 1.0** and **S = 0.1** fixed. R and P vary across a 2D grid:

- R ∈ [0.1, 1.0], P ∈ [0.1, 1.0], spacing ≈ 0.041
- Valid cells satisfy T > R > P > S, forming a triangle in (R, P) space
- The diagonal R = P is the boundary where cooperation and defection pay equally

| Gap | Range | Interpretation |
|-----|-------|----------------|
| T − R | 0.0 – 0.9 | Temptation to defect (varies) |
| P − S | 0.0 – 0.9 | Sucker penalty (varies) |
| R − P | −0.9 – 0.9 | Cooperation benefit (varies, both axes) |

Three independent gaps vary simultaneously, making the PD a 2D parameter exploration.

---

## 2. Loci and Genotypes

The prisoners study uses **4 loci** (C, P, M, I) → **16 genotype columns** per .con file. Genotype column names: `C0P0M0I0` through `C1P1M1I1`.

---

## 3. Results Path

```
~/results/prisoners/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}/{population}/
```

Example: `~/results/prisoners/shuffle_cost12_128/P/1.0/pop_2/csv_0_for_image.con`

---

## 4. Data Format (Legacy)

CSV columns:
- `T, R, P, S` — payoff matrix parameters (T=1.0, S=0.1 constant; R, P vary)
- `Time` — simulation timestep
- `wmean, wsd` — population mean fitness and stdev
- `qBDefault, qBSeen` — cooperation probabilities
- Deprecated derived trait columns: `C1hoose`, `C1hoose_lt`, `Mimic`, `Imimic`, `Imimic_lt`, `C0`, `C1`, `C0Choose`, `C1Choose`, `dSTFT`, `dTFT`, `iSTFT`, `iTFT`
- 16 genotype columns — 4 loci in order C, P, M, I: `C0P0M0I0` through `C1P1M1I1`
- Each genotype column has a corresponding `SD` column

**Caution**: The legacy `C0` and `C1` columns equal `C0P0M0I0` and `C1P0M0I0` respectively (the bare genotype with all other loci at 0), **not** allele frequencies. To get true allele frequencies, sum all genotypes starting with C0 or C1.

---

## 5. Loading and Analysis

```python
import pandas as pd

df = pd.read_csv('csv_0_for_image.con')
# Keep only final timestep per (R, P) cell
df = df.sort_values('Time').groupby(['R', 'P']).last().reset_index()

# Heatmap view (R vs P): high R at top, low P at left
r_vals = sorted(df['R'].unique(), reverse=True)
p_vals = sorted(df['P'].unique())
pivot = df.pivot(index='R', columns='P', values='TRAIT')
pivot = pivot.reindex(index=r_vals, columns=p_vals)

# Find maximum location
row = df.loc[df['TRAIT'].idxmax()]
print(f"Max at R={row['R']:.2f}, P={row['P']:.2f}")

# Correlation with R-P
df['R_minus_P'] = df['R'] - df['P']
print(df['TRAIT'].corr(df['R_minus_P']))
```

---

## 6. Figure Panel Mapping (s07)

MAIN_ROWS in `manifest.py` defines 5 rows:

| Row | Panels | Population | File_set | Notes |
|-----|--------|------------|----------|-------|
| 0 | a, b | pop_2 | _1 | Higher qBSeen pop |
| 1 | c, d | pop_2 | _0 | Lower qBSeen pop |
| 2 | e, f | pop_3 | _0 | Evolving population |
| 3 | g, h | pop_3 | _1 | Fixed population |
| 4 | i, j | pop_1 | _0 | Single population |

For mechanism `P`, typical traits per column: P1, Choosers, qBSeen, wmean.

Each panel is a **heatmap** with R on the y-axis and P on the x-axis (imshow renderer).

---

## 7. Key Findings

See `prisoners.md` for full analysis.

### Single-run variant

The `prisoners_1run` study uses the same parameters and path structure but runs a single simulation instead of averaging over multiple runs. Use it to track temporal dynamics — e.g., whether cooperation and defection cycle over time — that are smoothed out in the main study's averaged results. Summary:

1. **P1 hitchhiking (pop_3)**: P1 frequency peaks at intermediate R−P, not where selection is strongest, because C0P1 accumulates as a neutral carrier via mutation from C1P1.

2. **Exploitation asymmetry (pop_3)**: Direction flips at R = (T+P)/2. Above threshold: fixed defectors exploit evolving cooperators. Below: evolving defectors exploit fixed cooperators.

3. **Emergent symmetry breaking (pop_2)**: Two identical coevolving populations spontaneously diverge — one becomes cooperator-heavy (exploited, low fitness) and the other defector-heavy (exploiter, high fitness). Correlation: more choosers = lower fitness (r = −0.99).

4. **Partner choice bottleneck**: Swaps require C1P1 on BOTH sides. When defectors are rare in your population, partner choice provides little benefit.

5. **Sharp phase transition (pop_2)**: Cooperation near R ≈ P shows an all-or-nothing transition driven by positive feedback (more cooperators → more swaps → higher cooperator fitness → more cooperators). Below R−P ≈ 0.041, the loop never ignites. Above R−P ≈ 0.123, it always does. The transition is bimodal with no stable intermediate.
