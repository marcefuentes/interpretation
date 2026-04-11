# Hamilton Altruism Game — Game-Specific Instructions

**Prerequisite**: Read `instructions.md` first for the shared simulation model.

---

## 1. Game Parameters

The Hamilton altruism game is parameterized by benefit *b*, cost *c*, and given parameter *g*. With *g* = 1.0 (full dilemma), a cooperator gives all of its production *b* to its partner and pays cost *c*.

| Parameter | Value | Description |
|-----------|-------|-------------|
| *b* − *c* | 0.008 – 8.0 | Net benefit of mutual cooperation (x-axis, log₂ scale: 2⁻⁷ to 2³) |
| *c* | 1.0 | Cost (fixed throughout; C_MIN) |
| *b* | 1.008 – 9.0 | Benefit (*c* + x-axis value) |
| *g* | 1.0 | Given parameter (full dilemma) |
| *K* | 2.0 | Baseline fitness (k0 = k1) |
| *B*_max | 9.0 | Maximum benefit (for fitness normalization) |
| groupsize | 128 | Individuals per group from each population |

Constants defined in `../graph/graphgen/studies/hamilton/theory.py`: B_MAX = 9.0, C_MIN = 1.0, K = 2.0.

---

## 2. Equivalent Prisoner's Dilemma Payoffs

From `calculate_derived_globals.c`, the Hamilton game at *g* = 1.0 maps exactly to a Prisoner's Dilemma. With `b0 = K + (b−c)` and `given = 1`:

| Payoff | Formula | Derivation |
|--------|---------|------------|
| **T** (Temptation) | 4 + (*b* − *c*) | K + b0 · given = 2 + (2 + x) |
| **R** (Reward) | 2 + (*b* − *c*) | K + b0·(1−g) + b0·g − K = 2 + x |
| **P** (Punishment) | 2 | K |
| **S** (Sucker) | 0 | K + b0·(1−g) − K = 0 |

Key relationships (all constant except R − P):

| Relationship | Value | Interpretation |
|-------------|-------|----------------|
| **R − P** | *b* − *c* | Cooperation benefit (= x-axis, varies) |
| **T − R** | 2 | Temptation premium (constant) |
| **P − S** | 2 | Sucker penalty (constant) |

Concrete values:

| *b* − *c* | T | R | P | S | R − P |
|-----------|-------|-------|---|---|-------|
| 0.008 | 4.008 | 2.008 | 2 | 0 | 0.008 |
| 0.125 | 4.125 | 2.125 | 2 | 0 | 0.125 |
| 0.250 | 4.250 | 2.250 | 2 | 0 | 0.250 |
| 1.000 | 5.000 | 3.000 | 2 | 0 | 1.000 |
| 4.000 | 8.000 | 6.000 | 2 | 0 | 4.000 |
| 8.000 | 12.000 | 10.000 | 2 | 0 | 8.000 |

### Comparison with the PD study parameter space

In the PD study, T = 1.0 and S = 0.1 are fixed while R and P vary on a 2D grid. Three gaps vary simultaneously: T−R ∈ [0, 0.9], P−S ∈ [0, 0.9], R−P ∈ [−0.9, 0.9].

In Hamilton, only **R − P varies** (= *b* − *c*) while T−R = P−S = 2 are constant:

1. **Fixed, strong temptation** (T−R = 2) vs PD's variable, weaker temptation (max 0.9)
2. **Fixed, severe sucker penalty** (P−S = 2) vs PD's variable penalty (max 0.9)
3. **Much wider R−P range** (0.008 – 8.0) vs PD's (−0.9 – 0.9)

Hamilton is a 1D slice through PD space with fixed temptation/sucker costs and varying cooperation benefit.

---

## 3. Fitness Normalization

Fitness is normalized as: (*K* + *w*) / (*K* + *B*_max) = (2 + *w*) / 11

Without mechanisms at *g* = 1.0, theory predicts zero cooperation: (1−*g*)·*b* > *c* is never satisfied.

---

## 4. Loci and Genotypes

The Hamilton study uses **6 loci** (C, I, J, M, P, Q) → **64 genotype columns** per .con file. Genotype column names: `C0I0J0M0P0Q0` through `C1I1J1M1P1Q1` (alphabetical order).

---

## 5. Results Path

```
~/results/hamilton/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}/{population}/
```

Example: `~/results/hamilton/shuffle_cost12_128/P/1.0/pop_2/csv_0_for_image.con`

---

## 6. Data Format (Current)

CSV columns:
- `k, b_c_0, b_c_1` — game parameters (k = baseline fitness; b_c_0, b_c_1 = benefit − cost for each population)
- `Time` — simulation timestep
- `wmean, wsd` — population mean fitness and stdev
- `qBDefault, qBSeen` — cooperation probabilities
- 64 genotype columns — all combinations of 6 loci, alphabetical: `C0I0J0M0P0Q0` through `C1I1J1M1P1Q1`
- Each genotype column has a corresponding `SD` column
- **No derived trait columns** — compute from genotypes (see `instructions.md` §4.4)

---

## 7. Loading and Analysis

```python
import pandas as pd

df = pd.read_csv('csv_0_for_image.con')
# Keep only final timestep per b-c cell
df = df.sort_values('Time').groupby(['b_c_0']).last().reset_index()

# Compute derived traits (64-genotype format, 6 loci)
c1p1_cols = [c for c in df.columns if c.startswith('C1') and 'P1' in c and not c.endswith('SD')]
c0p1_cols = [c for c in df.columns if c.startswith('C0') and 'P1' in c and not c.endswith('SD')]
c1p0_cols = [c for c in df.columns if c.startswith('C1') and 'P0' in c and not c.endswith('SD')]

df['C1P1'] = df[c1p1_cols].sum(axis=1)  # cooperators who choose
df['C0P1'] = df[c0p1_cols].sum(axis=1)  # defectors carrying P1 (silent)
df['C1P0'] = df[c1p0_cols].sum(axis=1)  # cooperators who don't choose
df['P1'] = df['C1P1'] + df['C0P1']
df['AllC'] = df['C1P0']  # = qBSeen - C1P1

# Line plot (b-c on x-axis, log scale)
import matplotlib.pyplot as plt
plt.semilogx(df['b_c_0'], df['qBSeen'], label='qBSeen')
```

---

## 8. Figure Panel Mapping (s07)

MAIN_ROWS in `manifest.py` defines 3 rows. Hamilton uses multi-line sources (both file sets plotted as separate lines per panel):

| Row | Panels | Population | Lines | Colors |
|-----|--------|------------|-------|--------|
| 0 | a, b | pop_2 | fset_0 (orange) + fset_1 (red) | Higher coop = orange, lower = red |
| 1 | c, d | pop_3 | fset_0 (orange) + fset_1 (lightblue) | Evolving = orange, fixed = lightblue |
| 2 | e, f | pop_1 | fset_0 (orange) | Single population |

Each panel is a **line plot** (plot renderer) with *b* − *c* on the x-axis (log scale).

For mechanism `P`, typical traits per column: P1, Choose (= C1P1), qBSeen, wmean.

---

## 9. Key Findings

See `hamilton.md` for full analysis. Summary:

1. **P1 hitchhiking (all populations)**: P1 peaks at lower R−P than C1P1 because neutral C0P1 carriers inflate P1 in the transition zone. Same mechanism as PD.

2. **P1 dispensability at high R−P (pop_1)**: C1P0 free-riders grow from 9% to 31% of cooperators. When R−P = 8 (R = 10), cooperation self-sustains without partner choice.

3. **Emergent asymmetry (pop_2)**: Gradual symmetry breaking (not bimodal like PD). Cooperating population exploited 3.54× at R−P = 8. Correlation: −0.92.

4. **Sharp transition and exploitation reversal (pop_3)**: Cooperation jumps 6× between R−P = 0.5 and 0.71. Exploitation crossover near R−P ≈ 1.0 where qBSeen_evolving ≈ qBSeen_fixed ≈ 0.5.

5. **Shuffle effect**: Negligible throughout (< 0.02 difference in qBSeen).

6. **Key PD comparison**: Hamilton has constant T−R = P−S = 2 (strong temptation, severe sucker cost), producing gradual rather than bimodal transitions. Pop_1 sustains 13% cooperation even at R−P = 0.008.
