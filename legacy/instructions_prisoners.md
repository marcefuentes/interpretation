# Prisoner's Dilemma — Game-Specific Instructions

**Prerequisite**: Read instructions.md first for the shared simulation model.

Scope in this project:
- **mutualism** is the primary study (two populations can differ in parameters).
- **hamilton** is the equal-parameter diagonal special case of mutualism (b0 - c0 = b1 - c1).
- **prisoners** and **snowdrift** are calibration studies used to interpret mechanism signatures, not primary biological endpoints.

---

## 1. Game Parameters

Standard Prisoner's Dilemma with **T = 1.0** and **S = 0.1** fixed. R and P vary across a 2D grid:

- R ∈ [0.1, 1.0], P ∈ [0.1, 1.0], spacing ≈ 0.041
- Valid cells satisfy T > R > P > S, forming a triangle in (R, P) space
- The diagonal R = P is the boundary where cooperation and defection pay equally

| Gap   | Range      | Interpretation                          |
| ----- | ---------- | --------------------------------------- |
| T − R | 0.0 – 0.9  | Temptation to defect (varies)           |
| P − S | 0.0 – 0.9  | Sucker penalty (varies)                 |
| R − P | −0.9 – 0.9 | Cooperation benefit (varies, both axes) |

Three independent gaps vary simultaneously, making the PD a 2D parameter exploration.

---

## 2. Loci and Genotypes

The prisoners study uses **6 loci** (C, I, J, M, P, Q) → **64 genotype columns** per .con file. Genotype column names: C0I0J0M0P0Q0 through C1I1J1M1P1Q1 (alphabetical order after C).

---

## 3. Results Path


~/results/prisoners/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}/{population}/


Example: ~/results/prisoners/shuffle_cost12_128/P/1.0/pop_2/csv_0_for_image.con

---

## 4. Data Format (Current)

CSV columns:
- T0, R0, P0, S0, T1, R1, P1, S1 — payoff matrix parameters per population (T0=T1=1.0, S0=S1=0.1 constant; R0=R1, P0=P1 vary)
- Time — simulation timestep
- wmean, wmeanSD, wsd, wsdSD — population mean fitness and stdev (with SD columns)
- qBSeen, qBSeenSD — cooperation probability
- 64 genotype columns — 6 loci in alphabetical order C, I, J, M, P, Q: C0I0J0M0P0Q0 through C1I1J1M1P1Q1
- Each genotype column has a corresponding SD column

**Note**: The column P1 (8th column) is a game parameter (population 1's P payoff), not to be confused with the P1 allele frequency. To compute allele frequencies, sum genotype columns — see §5.

---

## 5. Loading and Analysis

python
import pandas as pd

df = pd.read_csv('csv_0_for_image.con')
# Keep only final timestep per (R, P) cell
df = df.sort_values('Time').groupby(['R0', 'P0']).last().reset_index()

# Compute derived traits from genotype columns
geno = [c for c in df.columns if c[0] == 'C' and not c.endswith('SD') and len(c) == 12]
c1p1 = [c for c in geno if c.startswith('C1') and 'P1' in c]
c0p1 = [c for c in geno if c.startswith('C0') and 'P1' in c]
c1p0 = [c for c in geno if c.startswith('C1') and 'P0' in c]
df['C1P1_t'] = df[c1p1].sum(axis=1)  # cooperators who choose
df['C0P1_t'] = df[c0p1].sum(axis=1)  # defectors carrying P1
df['C1P0_t'] = df[c1p0].sum(axis=1)  # cooperators who don't choose
df['P1_t'] = df['C1P1_t'] + df['C0P1_t']  # total P1 allele frequency

# Heatmap view (R vs P): high R at top, low P at left
r_vals = sorted(df['R0'].unique(), reverse=True)
p_vals = sorted(df['P0'].unique())
pivot = df.pivot(index='R0', columns='P0', values='TRAIT')
pivot = pivot.reindex(index=r_vals, columns=p_vals)

# Find maximum location
row = df.loc[df['TRAIT'].idxmax()]
print(f"Max at R={row['R0']:.2f}, P={row['P0']:.2f}")

# Correlation with R-P
df['R_minus_P'] = df['R0'] - df['P0']
print(df['TRAIT'].corr(df['R_minus_P']))


---

## 6. Figure Panel Mapping (s07)

MAIN_ROWS in manifest.py defines 5 rows:

| Row   | Panels   | Population   | File_set   | Notes               |
| ----- | -------- | ------------ | ---------- | ------------------- |
| 0     | a, b     | pop_2        | _0         | Higher qBSeen pop   |
| 1     | c, d     | pop_2        | _1         | Lower qBSeen pop    |
| 2     | e, f     | pop_3        | _0         | Evolving population |
| 3     | g, h     | pop_3        | _1         | Fixed population    |
| 4     | i, j     | pop_1        | _0         | Single population   |

For mechanism P, typical traits per column: P1, Choosers, qBSeen, wmean.

Each panel is a **heatmap** with R on the y-axis and P on the x-axis (imshow renderer).

---

## 7. Key Findings

See prisoners.md for full analysis.

### Single-run variant

The prisoners_1run study uses the same parameters and path structure but runs a single simulation instead of averaging over multiple runs. Use it to track temporal dynamics — e.g., whether cooperation and defection cycle over time — that are smoothed out in the main study's averaged results. Summary:

1. **P1 hitchhiking (pop_3)**: P1 frequency peaks at intermediate R−P, not where selection is strongest, because C0P1 accumulates as a neutral carrier via mutation from C1P1.

2. **Exploitation asymmetry (pop_3)**: Direction flips at R = (T+P)/2. Above threshold: fixed defectors exploit evolving cooperators. Below: evolving defectors exploit fixed cooperators.

3. **Emergent symmetry breaking (pop_2)**: Two identical coevolving populations spontaneously diverge — one becomes cooperator-heavy (exploited, low fitness) and the other defector-heavy (exploiter, high fitness). Correlation: more choosers = lower fitness (r = −1.00).

4. **Partner choice bottleneck**: Swaps require C1P1 on BOTH sides. When defectors are rare in your population, partner choice provides little benefit.

5. **Sharp phase transition (pop_2)**: Cooperation near R ≈ P shows an all-or-nothing transition driven by positive feedback (more cooperators → more swaps → higher cooperator fitness → more cooperators). Below R−P ≈ 0.041, the loop never ignites. Above R−P ≈ 0.123, it always does. The transition is bimodal with no stable intermediate.
