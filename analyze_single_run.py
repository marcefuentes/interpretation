#!/usr/bin/env python3
"""Analyze single-run Prisoner's Dilemma simulation data for 4 questions."""

import os
import csv
import glob as globmod
from collections import defaultdict

BASE = os.path.expanduser("~/results/prisoners_1run/shuffle_cost12_128/P/1.0")

def load_csv(path):
    """Load CSV, return list of dicts with float values where possible."""
    with open(path) as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            d = {}
            for k, v in row.items():
                try:
                    d[k] = float(v)
                except (ValueError, TypeError):
                    d[k] = v
            rows.append(d)
    return rows

def load_pop(pop, fset):
    """Load all cells for a population and fset. Returns dict: cell_idx -> list of row dicts."""
    d = os.path.join(BASE, pop)
    data = {}
    for path in sorted(globmod.glob(os.path.join(d, f"*_{fset}.csv"))):
        fname = os.path.basename(path)
        idx = int(fname.split("_")[0])
        data[idx] = load_csv(path)
    return data

def get_RP(rows):
    """Get R, P from first row (they're constant across timesteps for a cell)."""
    return rows[0]["R0"], rows[0]["P0"]

def compute_C1P1(row):
    return row["C1P1M0I0"] + row["C1P1M0I1"] + row["C1P1M1I0"] + row["C1P1M1I1"]

def compute_C1P0(row):
    return row["C1P0M0I0"] + row["C1P0M0I1"] + row["C1P0M1I0"] + row["C1P0M1I1"]

def compute_C0P1(row):
    return row["C0P1M0I0"] + row["C0P1M0I1"] + row["C0P1M1I0"] + row["C0P1M1I1"]

def fmt_traj(values, width=7):
    return " -> ".join(f"{v:{width}.4f}" for v in values)

def fmt_times(rows):
    return [int(r["Time"]) for r in rows]

# ============================================================
print("=" * 80)
print("LOADING DATA...")
print("=" * 80)

pop1_0 = load_pop("pop_1", "0")
pop2_0 = load_pop("pop_2", "0")
pop2_1 = load_pop("pop_2", "1")
pop3_0 = load_pop("pop_3", "0")
pop3_1 = load_pop("pop_3", "1")

print(f"  pop_1 fset_0: {len(pop1_0)} cells")
print(f"  pop_2 fset_0: {len(pop2_0)} cells, fset_1: {len(pop2_1)} cells")
print(f"  pop_3 fset_0: {len(pop3_0)} cells, fset_1: {len(pop3_1)} cells")

# Build R-P index for pop_2
pop2_cells = []
for idx in pop2_0:
    R, P = get_RP(pop2_0[idx])
    pop2_cells.append((idx, R, P, R - P))
pop2_cells.sort(key=lambda x: x[3])

# ============================================================
print("\n" + "=" * 80)
print("Q1: DO COOPERATION AND DEFECTION CYCLE NEAR THE PHASE BOUNDARY? (pop_2)")
print("=" * 80)

# Use fset_1 qBSeen (the more cooperative population)
boundary_cells = [(idx, R, P, dRP) for idx, R, P, dRP in pop2_cells if 0.04 <= dRP <= 0.15]
coop_cells = [(idx, R, P, dRP) for idx, R, P, dRP in pop2_cells if dRP > 0.2]
defect_cells = [(idx, R, P, dRP) for idx, R, P, dRP in pop2_cells if 0.0 < dRP < 0.04]

print(f"\nCells near boundary (0.04 <= R-P <= 0.15): {len(boundary_cells)}")
print(f"Cells in cooperative region (R-P > 0.2): {len(coop_cells)}")
print(f"Cells in defection region (0 < R-P < 0.04): {len(defect_cells)}")

times = fmt_times(pop2_1[boundary_cells[0][0]]) if boundary_cells else []
print(f"\nTimesteps: {times}")

print("\n--- BOUNDARY CELLS (fset_1 qBSeen trajectory) ---")
for idx, R, P, dRP in boundary_cells[:8]:
    traj = [row["qBSeen"] for row in pop2_1[idx]]
    mn, mx = min(traj[1:]), max(traj[1:])  # skip t=1 (initial)
    print(f"  Cell {idx:4d} R={R:.3f} P={P:.3f} R-P={dRP:.3f} | range=[{mn:.4f},{mx:.4f}] | {fmt_traj(traj)}")

print("\n--- COOPERATIVE REGION (sample, fset_1 qBSeen) ---")
for idx, R, P, dRP in coop_cells[:5]:
    traj = [row["qBSeen"] for row in pop2_1[idx]]
    mn, mx = min(traj[1:]), max(traj[1:])
    print(f"  Cell {idx:4d} R={R:.3f} P={P:.3f} R-P={dRP:.3f} | range=[{mn:.4f},{mx:.4f}] | {fmt_traj(traj)}")

print("\n--- DEFECTION REGION (sample, fset_1 qBSeen) ---")
for idx, R, P, dRP in defect_cells[:5]:
    traj = [row["qBSeen"] for row in pop2_1[idx]]
    mn, mx = min(traj[1:]), max(traj[1:])
    print(f"  Cell {idx:4d} R={R:.3f} P={P:.3f} R-P={dRP:.3f} | range=[{mn:.4f},{mx:.4f}] | {fmt_traj(traj)}")

# Summary stats
print("\n--- SUMMARY: Mean range of qBSeen (max-min, excluding t=1) ---")
for label, cells in [("Boundary", boundary_cells), ("Cooperative", coop_cells), ("Defection", defect_cells)]:
    if not cells:
        print(f"  {label}: no cells")
        continue
    ranges = []
    for idx, R, P, dRP in cells:
        traj = [row["qBSeen"] for row in pop2_1[idx]]
        ranges.append(max(traj[1:]) - min(traj[1:]))
    mean_r = sum(ranges) / len(ranges)
    max_r = max(ranges)
    print(f"  {label:12s}: mean_range={mean_r:.4f}, max_range={max_r:.4f}, n={len(cells)}")

# ============================================================
print("\n" + "=" * 80)
print("Q2: DO EXPLOITER AND EXPLOITED ROLES SWITCH OVER TIME? (pop_2)")
print("=" * 80)

# High R-P cells: fset_1=cooperator(exploited), fset_0=defector(exploiter)
high_RP = [(idx, R, P, dRP) for idx, R, P, dRP in pop2_cells if dRP > 0.3]
print(f"\nHigh R-P cells (R-P > 0.3): {len(high_RP)}")
print(f"Timesteps: {times}")

print("\n--- HIGH R-P CELLS: qBSeen for both fsets ---")
flips = 0
total = 0
for idx, R, P, dRP in high_RP[:8]:
    traj0 = [row["qBSeen"] for row in pop2_0[idx]]
    traj1 = [row["qBSeen"] for row in pop2_1[idx]]
    gaps = [t1 - t0 for t0, t1 in zip(traj0, traj1)]
    sign_changes = sum(1 for i in range(2, len(gaps)) if gaps[i] * gaps[i-1] < 0)
    print(f"  Cell {idx:4d} R={R:.3f} P={P:.3f} R-P={dRP:.3f}")
    print(f"    fset_0 (lower qB): {fmt_traj(traj0)}")
    print(f"    fset_1 (higher qB): {fmt_traj(traj1)}")
    print(f"    gap (1-0):          {fmt_traj(gaps)}")
    print(f"    sign_changes={sign_changes}")
    flips += sign_changes
    total += 1

print(f"\n--- SUMMARY across all high R-P cells ---")
all_sign_changes = []
all_gap_means = []
for idx, R, P, dRP in high_RP:
    traj0 = [row["qBSeen"] for row in pop2_0[idx]]
    traj1 = [row["qBSeen"] for row in pop2_1[idx]]
    gaps = [t1 - t0 for t0, t1 in zip(traj0, traj1)]
    sign_changes = sum(1 for i in range(2, len(gaps)) if gaps[i] * gaps[i-1] < 0)
    all_sign_changes.append(sign_changes)
    if any(g != 0 for g in gaps[1:]):
        all_gap_means.append(sum(gaps[1:]) / len(gaps[1:]))

if all_sign_changes:
    print(f"  Cells with >=1 sign flip: {sum(1 for s in all_sign_changes if s >= 1)}/{len(all_sign_changes)}")
    print(f"  Mean sign changes per cell: {sum(all_sign_changes)/len(all_sign_changes):.2f}")
if all_gap_means:
    pos = sum(1 for g in all_gap_means if g > 0)
    neg = sum(1 for g in all_gap_means if g < 0)
    print(f"  Mean gap positive (fset_1 > fset_0): {pos}/{len(all_gap_means)}")
    print(f"  Mean gap negative (fset_0 > fset_1): {neg}/{len(all_gap_means)}")

# ============================================================
print("\n" + "=" * 80)
print("Q3: IS THE pop_3 COOPERATION JUMP A SINGLE TIPPING EVENT? (pop_3)")
print("=" * 80)

# Build R-P index for pop_3
pop3_cells = []
for idx in pop3_0:
    R, P = get_RP(pop3_0[idx])
    pop3_cells.append((idx, R, P, R - P))
pop3_cells.sort(key=lambda x: x[3])

transition_cells = [(idx, R, P, dRP) for idx, R, P, dRP in pop3_cells if 0.5 <= dRP <= 0.71]
print(f"\nTransition zone cells (0.5 <= R-P <= 0.71): {len(transition_cells)}")

times3 = fmt_times(pop3_0[transition_cells[0][0]]) if transition_cells else []
print(f"Timesteps: {times3}")

print("\n--- TRANSITION ZONE: evolving pop (fset_0) qBSeen trajectory ---")
monotonic_count = 0
cycling_count = 0
for idx, R, P, dRP in transition_cells[:10]:
    traj = [row["qBSeen"] for row in pop3_0[idx]]
    # Check if monotonically increasing after first nonzero
    diffs = [traj[i+1] - traj[i] for i in range(1, len(traj)-1)]  # skip t=1
    reversals = sum(1 for i in range(1, len(diffs)) if diffs[i] * diffs[i-1] < 0)
    # Find first big jump
    jump_idx = None
    for i in range(1, len(traj)):
        if traj[i] > 0.1 and traj[i-1] < 0.05:
            jump_idx = i
            break
    pattern = "MONOTONIC" if reversals <= 1 else f"CYCLING({reversals} reversals)"
    if reversals <= 1:
        monotonic_count += 1
    else:
        cycling_count += 1
    print(f"  Cell {idx:4d} R={R:.3f} P={P:.3f} R-P={dRP:.3f} | {pattern}")
    print(f"    qBSeen: {fmt_traj(traj)}")

# Broader summary
print(f"\n--- SUMMARY across all transition zone cells ---")
mono_all = 0
cycle_all = 0
for idx, R, P, dRP in transition_cells:
    traj = [row["qBSeen"] for row in pop3_0[idx]]
    diffs = [traj[i+1] - traj[i] for i in range(1, len(traj)-1)]
    reversals = sum(1 for i in range(1, len(diffs)) if diffs[i] * diffs[i-1] < 0)
    if reversals <= 1:
        mono_all += 1
    else:
        cycle_all += 1
print(f"  Monotonic (<=1 reversal): {mono_all}/{len(transition_cells)}")
print(f"  Cycling (>1 reversal):    {cycle_all}/{len(transition_cells)}")

# Also show cells just below and above transition for context
below = [(idx, R, P, dRP) for idx, R, P, dRP in pop3_cells if 0.3 <= dRP < 0.5]
above = [(idx, R, P, dRP) for idx, R, P, dRP in pop3_cells if 0.71 < dRP <= 0.9]
print(f"\n--- CONTEXT: below transition (0.3 <= R-P < 0.5), sample ---")
for idx, R, P, dRP in below[:3]:
    traj = [row["qBSeen"] for row in pop3_0[idx]]
    print(f"  Cell {idx:4d} R-P={dRP:.3f} | {fmt_traj(traj)}")
print(f"--- CONTEXT: above transition (0.71 < R-P <= 0.9), sample ---")
for idx, R, P, dRP in above[:3]:
    traj = [row["qBSeen"] for row in pop3_0[idx]]
    print(f"  Cell {idx:4d} R-P={dRP:.3f} | {fmt_traj(traj)}")

# ============================================================
print("\n" + "=" * 80)
print("Q4: DOES C1P0 DISPLACE C1P1 GRADUALLY OR CYCLICALLY? (pop_1)")
print("=" * 80)

pop1_cells = []
for idx in pop1_0:
    R, P = get_RP(pop1_0[idx])
    pop1_cells.append((idx, R, P, R - P))
pop1_cells.sort(key=lambda x: x[3])

high_RP_p1 = [(idx, R, P, dRP) for idx, R, P, dRP in pop1_cells if dRP > 0.3]
print(f"\nHigh R-P cells (R-P > 0.3): {len(high_RP_p1)}")

times1 = fmt_times(pop1_0[high_RP_p1[0][0]]) if high_RP_p1 else []
print(f"Timesteps: {times1}")

print("\n--- HIGH R-P CELLS: C1P1 and C1P0 trajectories ---")
monotonic_displace = 0
oscillatory_displace = 0
for idx, R, P, dRP in high_RP_p1[:8]:
    rows = pop1_0[idx]
    c1p1 = [compute_C1P1(r) for r in rows]
    c1p0 = [compute_C1P0(r) for r in rows]
    # Check if C1P0 monotonically increases (after initial)
    c1p0_diffs = [c1p0[i+1] - c1p0[i] for i in range(1, len(c1p0)-1)]
    reversals = sum(1 for i in range(1, len(c1p0_diffs)) if c1p0_diffs[i] * c1p0_diffs[i-1] < 0)
    pattern = "MONOTONIC" if reversals <= 1 else f"OSCILLATORY({reversals} rev)"
    if reversals <= 1:
        monotonic_displace += 1
    else:
        oscillatory_displace += 1
    print(f"  Cell {idx:4d} R={R:.3f} P={P:.3f} R-P={dRP:.3f} | {pattern}")
    print(f"    C1P1: {fmt_traj(c1p1)}")
    print(f"    C1P0: {fmt_traj(c1p0)}")

# Broader summary
print(f"\n--- SUMMARY across all high R-P cells ---")
mono_q4 = 0
osc_q4 = 0
for idx, R, P, dRP in high_RP_p1:
    rows = pop1_0[idx]
    c1p0 = [compute_C1P0(r) for r in rows]
    c1p1 = [compute_C1P1(r) for r in rows]
    c1p0_diffs = [c1p0[i+1] - c1p0[i] for i in range(1, len(c1p0)-1)]
    reversals = sum(1 for i in range(1, len(c1p0_diffs)) if c1p0_diffs[i] * c1p0_diffs[i-1] < 0)
    if reversals <= 1:
        mono_q4 += 1
    else:
        osc_q4 += 1

print(f"  C1P0 growth monotonic (<=1 reversal): {mono_q4}/{len(high_RP_p1)}")
print(f"  C1P0 growth oscillatory (>1 reversal): {osc_q4}/{len(high_RP_p1)}")

# Also check: does C1P1 decline monotonically?
mono_c1p1 = 0
osc_c1p1 = 0
for idx, R, P, dRP in high_RP_p1:
    rows = pop1_0[idx]
    c1p1 = [compute_C1P1(r) for r in rows]
    c1p1_diffs = [c1p1[i+1] - c1p1[i] for i in range(1, len(c1p1)-1)]
    reversals = sum(1 for i in range(1, len(c1p1_diffs)) if c1p1_diffs[i] * c1p1_diffs[i-1] < 0)
    if reversals <= 1:
        mono_c1p1 += 1
    else:
        osc_c1p1 += 1
print(f"  C1P1 decline monotonic (<=1 reversal): {mono_c1p1}/{len(high_RP_p1)}")
print(f"  C1P1 decline oscillatory (>1 reversal): {osc_c1p1}/{len(high_RP_p1)}")

# Final end-state comparison
print(f"\n--- END-STATE: C1P0 vs C1P1 at final timestep (high R-P cells) ---")
c1p0_wins = 0
for idx, R, P, dRP in high_RP_p1:
    rows = pop1_0[idx]
    final_c1p1 = compute_C1P1(rows[-1])
    final_c1p0 = compute_C1P0(rows[-1])
    if final_c1p0 > final_c1p1:
        c1p0_wins += 1
print(f"  C1P0 > C1P1 at final timestep: {c1p0_wins}/{len(high_RP_p1)}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
