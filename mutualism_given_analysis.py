#!/usr/bin/env python3
"""Analyze mutualism simulation across given={0.5, 1.0, 1.5}."""

import os
import pandas as pd
import numpy as np

BASE = os.path.expanduser("~/results/mutualism/shuffle_cost12_128/P")
GIVENS = [0.5, 1.0, 1.5]

def load_data(given):
    """Load final-timestep data for both file sets. Use .con if available, else build from raw CSVs."""
    pop_dir = os.path.join(BASE, str(given), "pop_2")
    frames = {}
    for fset in [0, 1]:
        con_path = os.path.join(pop_dir, f"csv_{fset}_for_image.con")
        if os.path.exists(con_path):
            df = pd.read_csv(con_path)
        else:
            # Build from last row of each raw CSV
            rows = []
            for i in range(231):
                csv_path = os.path.join(pop_dir, f"{i:04d}_{fset}.csv")
                raw = pd.read_csv(csv_path)
                rows.append(raw.iloc[-1])
            df = pd.DataFrame(rows).reset_index(drop=True)
        frames[fset] = df
    return frames[0], frames[1]


def get_genotype_cols(df):
    """Return column lists for C1P1, C1P0, C0P1, C0P0 genotypes (non-SD)."""
    all_cols = [c for c in df.columns if not c.endswith('SD') and c[0] == 'C']
    c1p1 = [c for c in all_cols if c.startswith('C1') and 'P1' in c]
    c1p0 = [c for c in all_cols if c.startswith('C1') and 'P0' in c]
    c0p1 = [c for c in all_cols if c.startswith('C0') and 'P1' in c]
    c0p0 = [c for c in all_cols if c.startswith('C0') and 'P0' in c]
    return c1p1, c1p0, c0p1, c0p0


def build_combined(df0, df1):
    """Combine file sets: compute max/min qBSeen and identify cooperator/defector populations."""
    combined = pd.DataFrame()
    combined['b_c_0'] = df0['b_c_0'].astype(float)
    combined['b_c_1'] = df0['b_c_1'].astype(float)
    combined['qBSeen_0'] = df0['qBSeen'].astype(float)
    combined['qBSeen_1'] = df1['qBSeen'].astype(float)
    combined['qBSeen_max'] = combined[['qBSeen_0', 'qBSeen_1']].max(axis=1)
    combined['qBSeen_min'] = combined[['qBSeen_0', 'qBSeen_1']].min(axis=1)
    combined['qBSeen_mean'] = combined[['qBSeen_0', 'qBSeen_1']].mean(axis=1)

    combined['log2_bc0'] = np.log2(combined['b_c_0'])
    combined['log2_bc1'] = np.log2(combined['b_c_1'])
    combined['is_diagonal'] = np.isclose(combined['b_c_0'], combined['b_c_1'], rtol=1e-3)
    combined['ratio'] = combined['b_c_1'] / combined['b_c_0']
    combined['high_asymmetry'] = combined['ratio'] > 10

    # Genotype fractions for each file set
    c1p1_cols, c1p0_cols, c0p1_cols, c0p0_cols = get_genotype_cols(df0)
    for fset, df in [(0, df0), (1, df1)]:
        combined[f'C1P1_{fset}'] = df[c1p1_cols].astype(float).sum(axis=1)
        combined[f'C1P0_{fset}'] = df[c1p0_cols].astype(float).sum(axis=1)
        combined[f'C0P1_{fset}'] = df[c0p1_cols].astype(float).sum(axis=1)
        combined[f'C0P0_{fset}'] = df[c0p0_cols].astype(float).sum(axis=1)
        combined[f'C1_total_{fset}'] = combined[f'C1P1_{fset}'] + combined[f'C1P0_{fset}']

    # Identify which fset is the cooperator (higher qBSeen)
    is_0_coop = combined['qBSeen_0'] >= combined['qBSeen_1']
    combined['coop_C1P1'] = np.where(is_0_coop, combined['C1P1_0'], combined['C1P1_1'])
    combined['coop_C1P0'] = np.where(is_0_coop, combined['C1P0_0'], combined['C1P0_1'])
    combined['defect_C1P1'] = np.where(is_0_coop, combined['C1P1_1'], combined['C1P1_0'])
    combined['defect_C1P0'] = np.where(is_0_coop, combined['C1P0_1'], combined['C1P0_0'])

    return combined


# ============================================================
# LOAD ALL DATA
# ============================================================
print("=" * 80)
print("LOADING DATA FOR given = {0.5, 1.0, 1.5}")
print("=" * 80)

data = {}
for g in GIVENS:
    df0, df1 = load_data(g)
    data[g] = build_combined(df0, df1)
    print(f"  given={g}: {len(data[g])} cells loaded")

# ============================================================
# Q1: OVERALL COOPERATION BY GIVEN
# ============================================================
print("\n" + "=" * 80)
print("Q1: OVERALL COOPERATION BY GIVEN VALUE")
print("=" * 80)

print(f"\n{'given':>8s} | {'All cells':>12s} | {'Diagonal':>12s} | {'High asym':>12s} | {'Off-diag':>12s}")
print(f"{'':>8s} | {'mean qBSeen':>12s} | {'mean qBSeen':>12s} | {'mean qBSeen':>12s} | {'mean qBSeen':>12s}")
print("-" * 68)
for g in GIVENS:
    df = data[g]
    all_mean = df['qBSeen_mean'].mean()
    diag_mean = df.loc[df['is_diagonal'], 'qBSeen_mean'].mean()
    hasym_mean = df.loc[df['high_asymmetry'], 'qBSeen_mean'].mean()
    offdiag_mean = df.loc[~df['is_diagonal'], 'qBSeen_mean'].mean()
    print(f"{g:>8.1f} | {all_mean:>12.4f} | {diag_mean:>12.4f} | {hasym_mean:>12.4f} | {offdiag_mean:>12.4f}")

print(f"\n--- Using max qBSeen (cooperating population) ---")
print(f"{'given':>8s} | {'All cells':>12s} | {'Diagonal':>12s} | {'High asym':>12s}")
print("-" * 50)
for g in GIVENS:
    df = data[g]
    print(f"{g:>8.1f} | {df['qBSeen_max'].mean():>12.4f} | {df.loc[df['is_diagonal'], 'qBSeen_max'].mean():>12.4f} | {df.loc[df['high_asymmetry'], 'qBSeen_max'].mean():>12.4f}")

print(f"\n--- Using min qBSeen (defecting population) ---")
print(f"{'given':>8s} | {'All cells':>12s} | {'Diagonal':>12s} | {'High asym':>12s}")
print("-" * 50)
for g in GIVENS:
    df = data[g]
    print(f"{g:>8.1f} | {df['qBSeen_min'].mean():>12.4f} | {df.loc[df['is_diagonal'], 'qBSeen_min'].mean():>12.4f} | {df.loc[df['high_asymmetry'], 'qBSeen_min'].mean():>12.4f}")

# Fraction of cells with substantial cooperation
print(f"\n--- Fraction of cells with qBSeen_max > 0.5 ---")
for g in GIVENS:
    df = data[g]
    frac = (df['qBSeen_max'] > 0.5).mean()
    frac_diag = df.loc[df['is_diagonal'], 'qBSeen_max'].gt(0.5).mean()
    print(f"  given={g}: all={frac:.3f}, diagonal={frac_diag:.3f}")


# ============================================================
# Q2: COOPERATION THRESHOLD SHIFT
# ============================================================
print("\n" + "=" * 80)
print("Q2: COOPERATION THRESHOLD — Does given=0.5 show cooperation at b-c > 1.0?")
print("=" * 80)

# For the diagonal, b_c_0 = b_c_1, so b-c = b_c_0 (since cost=1 is built in as c=1 in b/c ratio... 
# Actually b_c_0 IS b/c. So b = b_c_0 * c. With c=1, b = b_c_0. Then b-c = b_c_0 - 1.
# Wait, the parameter is b/c ratio. Let me re-read: "21 unique b-c values: 2^-7 to 2^3"
# So b_c_0 IS b/c (benefit-to-cost ratio). At given=0.5, cooperation when b/c > 2 (i.e., b > 2c).

print("\nTheory predictions (cooperation self-sustains without mechanisms):")
print("  given=0.5: (1-0.5)*b > c => b > 2c => b/c > 2.0")
print("  given=1.0: (1-1.0)*b > c => 0 > c => NEVER (pure dilemma)")
print("  given=1.5: (1-1.5)*b > c => -0.5b > c => NEVER")

print(f"\n--- Mean qBSeen_max by b/c value on diagonal ---")
print(f"{'b/c':>10s}", end="")
for g in GIVENS:
    print(f" | g={g:>3.1f}", end="")
print()
print("-" * 50)

for g0 in GIVENS:
    diag = data[g0].loc[data[g0]['is_diagonal']].copy()
    break  # just need b_c values

bc_values = sorted(data[0.5].loc[data[0.5]['is_diagonal'], 'b_c_0'].unique())
for bc in bc_values:
    print(f"{bc:>10.4f}", end="")
    for g in GIVENS:
        df = data[g]
        cell = df.loc[df['is_diagonal'] & np.isclose(df['b_c_0'], bc, rtol=1e-3)]
        if len(cell) > 0:
            print(f" | {cell['qBSeen_max'].values[0]:>5.3f}", end="")
        else:
            print(f" |   N/A", end="")
    print()

# Threshold analysis: for given=0.5, find the b/c value where cooperation jumps
print(f"\n--- Off-diagonal cooperation landscape (qBSeen_max > 0.3 fraction) ---")
print("b/c bins: cells grouped by min(b_c_0, b_c_1)")
for g in GIVENS:
    df = data[g]
    df_copy = df.copy()
    df_copy['min_bc'] = df_copy[['b_c_0', 'b_c_1']].min(axis=1)
    df_copy['max_bc'] = df_copy[['b_c_0', 'b_c_1']].max(axis=1)
    bins = sorted(df_copy['min_bc'].unique())
    print(f"\n  given={g}:")
    for bc_bin in bins:
        subset = df_copy[np.isclose(df_copy['min_bc'], bc_bin, rtol=1e-3)]
        frac_coop = (subset['qBSeen_max'] > 0.3).mean()
        mean_q = subset['qBSeen_max'].mean()
        print(f"    min(b/c)={bc_bin:>8.4f}: n={len(subset):>3d}, frac_coop={frac_coop:.3f}, mean_qB={mean_q:.3f}")


# ============================================================
# Q3: GENOTYPE COMPOSITION SHIFT
# ============================================================
print("\n" + "=" * 80)
print("Q3: GENOTYPE COMPOSITION — Choosers (C1P1) vs Free-riders (C1P0)")
print("=" * 80)

print("\n--- Among cooperating population (higher qBSeen), cells where qBSeen_max > 0.3 ---")
print(f"{'given':>8s} | {'n_coop':>8s} | {'C1P1 mean':>10s} | {'C1P0 mean':>10s} | {'C1P1/(C1P1+C1P0)':>18s} | {'C0P0 mean':>10s}")
print("-" * 80)
for g in GIVENS:
    df = data[g]
    coop_cells = df[df['qBSeen_max'] > 0.3]
    if len(coop_cells) == 0:
        print(f"{g:>8.1f} | {'0':>8s} | {'N/A':>10s} | {'N/A':>10s} | {'N/A':>18s} | {'N/A':>10s}")
        continue
    c1p1 = coop_cells['coop_C1P1'].mean()
    c1p0 = coop_cells['coop_C1P0'].mean()
    c0p0_mean = (1 - c1p1 - c1p0 - coop_cells['coop_C1P1'].mean())  # approximate
    ratio = c1p1 / (c1p1 + c1p0) if (c1p1 + c1p0) > 0 else float('nan')
    # Compute defector population genotype too
    dc1p0 = coop_cells['defect_C1P0'].mean()
    print(f"{g:>8.1f} | {len(coop_cells):>8d} | {c1p1:>10.4f} | {c1p0:>10.4f} | {ratio:>18.4f} | {dc1p0:>10.4f}")

print("\n--- Genotype breakdown by b/c range (diagonal only, cooperating pop) ---")
bc_ranges = [(0, 0.5, "b/c<0.5"), (0.5, 1.0, "0.5<b/c<1"), (1.0, 2.0, "1<b/c<2"), (2.0, 4.0, "2<b/c<4"), (4.0, 100, "b/c>4")]
for g in GIVENS:
    print(f"\n  given={g}:")
    df = data[g]
    diag = df[df['is_diagonal']].copy()
    for lo, hi, label in bc_ranges:
        subset = diag[(diag['b_c_0'] >= lo) & (diag['b_c_0'] < hi)]
        if len(subset) == 0:
            continue
        # Use the cooperating population's genotypes
        c1p1 = subset['coop_C1P1'].mean()
        c1p0 = subset['coop_C1P0'].mean()
        qmax = subset['qBSeen_max'].mean()
        chooser_ratio = c1p1 / (c1p1 + c1p0) if (c1p1 + c1p0) > 1e-6 else float('nan')
        print(f"    {label:>12s}: n={len(subset):>2d}, qBmax={qmax:.3f}, C1P1={c1p1:.3f}, C1P0={c1p0:.3f}, chooser_ratio={chooser_ratio:.3f}")

# Deeper: full 4-category breakdown for cooperative cells
print("\n--- Full genotype breakdown (cooperating pop, cells with qBSeen_max > 0.3) ---")
for g in GIVENS:
    df = data[g]
    coop = df[df['qBSeen_max'] > 0.3]
    if len(coop) == 0:
        print(f"  given={g}: no cooperative cells")
        continue
    # For the cooperating population
    is_0 = coop['qBSeen_0'] >= coop['qBSeen_1']
    c1p1 = np.where(is_0, coop['C1P1_0'], coop['C1P1_1']).mean()
    c1p0 = np.where(is_0, coop['C1P0_0'], coop['C1P0_1']).mean()
    c0p1 = np.where(is_0, coop['C0P1_0'], coop['C0P1_1']).mean()
    c0p0 = np.where(is_0, coop['C0P0_0'], coop['C0P0_1']).mean()
    print(f"  given={g} (n={len(coop)}): C1P1={c1p1:.4f}, C1P0={c1p0:.4f}, C0P1={c0p1:.4f}, C0P0={c0p0:.4f}")
    # Defecting pop
    c1p1d = np.where(~is_0, coop['C1P1_0'], coop['C1P1_1']).mean()
    c1p0d = np.where(~is_0, coop['C1P0_0'], coop['C1P0_1']).mean()
    c0p1d = np.where(~is_0, coop['C0P1_0'], coop['C0P1_1']).mean()
    c0p0d = np.where(~is_0, coop['C0P0_0'], coop['C0P0_1']).mean()
    print(f"         defecting pop: C1P1={c1p1d:.4f}, C1P0={c1p0d:.4f}, C0P1={c0p1d:.4f}, C0P0={c0p0d:.4f}")


# ============================================================
# Q4: ASYMMETRY PATTERNS
# ============================================================
print("\n" + "=" * 80)
print("Q4: ASYMMETRY — Which population cooperates when b_c_0 ≠ b_c_1?")
print("=" * 80)

print("\n--- Off-diagonal cells: does higher-b/c pop cooperate more? ---")
for g in GIVENS:
    df = data[g]
    offdiag = df[~df['is_diagonal']].copy()
    # "higher b/c pop" — b_c_1 >= b_c_0 by construction, so pop_1 has higher b/c
    # But fsets are randomly assigned. So check: when qBSeen_0 > qBSeen_1, is that the higher-b/c pop?
    # Actually b_c_0 and b_c_1 are the parameters, not which fset. In the triangular matrix b_c_1 >= b_c_0.
    # fset_0 is pop with b_c_0, fset_1 is pop with b_c_1.
    # Wait, re-read: "File sets _0 and _1 are randomly assigned (NOT sorted by qBSeen)"
    # So csv_0 and csv_1 are the two populations, but which one has b_c_0 vs b_c_1 may be random.
    # Actually I think b_c_0 always corresponds to the parameter for pop in file_0, b_c_1 for file_1.
    
    # Higher b/c pop should cooperate more (higher benefit)
    # b_c_1 >= b_c_0 by construction
    higher_bc_cooperates = (offdiag['qBSeen_1'] > offdiag['qBSeen_0']).sum()
    lower_bc_cooperates = (offdiag['qBSeen_0'] > offdiag['qBSeen_1']).sum()
    tied = (np.isclose(offdiag['qBSeen_0'], offdiag['qBSeen_1'], atol=0.05)).sum()
    
    # Among strongly asymmetric cells
    strong = offdiag[offdiag['ratio'] > 4]
    if len(strong) > 0:
        s_higher = (strong['qBSeen_1'] > strong['qBSeen_0']).sum()
        s_lower = (strong['qBSeen_0'] > strong['qBSeen_1']).sum()
    else:
        s_higher = s_lower = 0
    
    print(f"\n  given={g} (n_offdiag={len(offdiag)}):")
    print(f"    Higher-b/c pop cooperates more: {higher_bc_cooperates}")
    print(f"    Lower-b/c pop cooperates more:  {lower_bc_cooperates}")
    print(f"    ~Tied (within 0.05):            {tied}")
    print(f"    Strong asymmetry (ratio>4): higher={s_higher}, lower={s_lower}")

# Detailed: for each b_c_0 level, mean qBSeen of both pops
print(f"\n--- Mean qBSeen by b_c_0 for off-diagonal cells (fset_0 vs fset_1) ---")
for g in GIVENS:
    df = data[g]
    offdiag = df[~df['is_diagonal']].copy()
    print(f"\n  given={g}:")
    print(f"  {'b_c_0':>10s} | {'n':>4s} | {'qB_0 mean':>10s} | {'qB_1 mean':>10s} | {'qB_1-qB_0':>10s}")
    for bc in sorted(offdiag['b_c_0'].unique()):
        sub = offdiag[np.isclose(offdiag['b_c_0'], bc, rtol=1e-3)]
        q0 = sub['qBSeen_0'].mean()
        q1 = sub['qBSeen_1'].mean()
        print(f"  {bc:>10.4f} | {len(sub):>4d} | {q0:>10.4f} | {q1:>10.4f} | {q1-q0:>+10.4f}")


# ============================================================
# Q5: DIAGONAL COMPARISON ACROSS GIVEN VALUES
# ============================================================
print("\n" + "=" * 80)
print("Q5: DIAGONAL COMPARISON (Hamilton-equivalent: b_c_0 ≈ b_c_1)")
print("=" * 80)

print(f"\n{'b/c':>10s}", end="")
for g in GIVENS:
    print(f" | g={g} max  g={g} min", end="")
print()
print("-" * 80)

bc_values = sorted(data[0.5].loc[data[0.5]['is_diagonal'], 'b_c_0'].unique())
for bc in bc_values:
    print(f"{bc:>10.4f}", end="")
    for g in GIVENS:
        df = data[g]
        cell = df.loc[df['is_diagonal'] & np.isclose(df['b_c_0'], bc, rtol=1e-3)]
        if len(cell) > 0:
            print(f" | {cell['qBSeen_max'].values[0]:>7.3f} {cell['qBSeen_min'].values[0]:>7.3f}", end="")
        else:
            print(f" |     N/A     N/A", end="")
    print()

# Summary stats for diagonal
print(f"\n--- Diagonal summary ---")
print(f"{'given':>8s} | {'mean max':>10s} | {'mean min':>10s} | {'max-min gap':>12s} | {'n cooperating':>14s}")
print("-" * 65)
for g in GIVENS:
    df = data[g]
    diag = df[df['is_diagonal']]
    mm = diag['qBSeen_max'].mean()
    mn = diag['qBSeen_min'].mean()
    gap = (diag['qBSeen_max'] - diag['qBSeen_min']).mean()
    n_coop = (diag['qBSeen_max'] > 0.3).sum()
    print(f"{g:>8.1f} | {mm:>10.4f} | {mn:>10.4f} | {gap:>12.4f} | {n_coop:>14d}/{len(diag)}")


print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
