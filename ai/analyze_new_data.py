#!/usr/bin/env python3
"""
Analyze new hamilton and mutualism simulation data.
New parameterization: K=0.5, b=0.4 fixed, c varies from 0 to b.

Dilemma folders: 0 (no dilemma), 1 (PD), 2 (snowdrift)
Payoffs:
  Dilemma 0: T=K,     R=K+b-c,   P=K,   S=K+b-c
  Dilemma 1: T=K+b,   R=K+b-c,   P=K,   S=K-c
  Dilemma 2: T=K+b,   R=K+b-c/2, P=K,   S=K+b-c
With K=0.5, b=0.4.
"""

import csv
import os
import sys
from collections import defaultdict

BASE = os.path.expanduser("~/results")
K = 0.5
B = 0.4


# ── helpers ──────────────────────────────────────────────────────────────────

def load_con(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return list(csv.DictReader(f))


def genotype_cols(row, prefix_c, prefix_p=None):
    """Return columns matching C{prefix_c}...P{prefix_p}... (no SD suffix)."""
    cols = [k for k in row if not k.endswith("SD") and len(k) == 12 and k[0] == "C"]
    if prefix_c is not None:
        cols = [c for c in cols if c.startswith(f"C{prefix_c}")]
    if prefix_p is not None:
        cols = [c for c in cols if f"P{prefix_p}" in c]
    return cols


def coop(row):
    """Total cooperation = C1* allele frequency = qBSeen from file (faster)."""
    return float(row["qBSeen"])


def c1p1(row):
    cols = genotype_cols(row, "1", "1")
    return sum(float(row[c]) for c in cols)


def c1p0(row):
    cols = genotype_cols(row, "1", "0")
    return sum(float(row[c]) for c in cols)


def c0p1(row):
    cols = genotype_cols(row, "0", "1")
    return sum(float(row[c]) for c in cols)


def p1_freq(row):
    return c1p1(row) + c0p1(row)


def fmt(v, d=3):
    return f"{v:.{d}f}"


def sorted_rows(rows, key="c0"):
    return sorted(rows, key=lambda r: float(r[key]))


# ── payoff formulas ──────────────────────────────────────────────────────────

def payoffs(dilemma, c, k=K, b=B):
    c = float(c)
    if dilemma == 0:
        T = k; R = k + b - c; P = k; S = k + b - c
    elif dilemma == 1:
        T = k + b; R = k + b - c; P = k; S = k - c
    elif dilemma == 2:
        T = k + b; R = k + b - c / 2; P = k; S = k + b - c
    return T, R, P, S


# ══════════════════════════════════════════════════════════════════════════════
# HAMILTON ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("HAMILTON ANALYSIS  (K=0.5, b=0.4, c in [0,0.4])")
print("=" * 80)

# ── 1. Payoff table ──────────────────────────────────────────────────────────

print("\n--- PAYOFF TABLE ---")
print(f"{'c':>5}  {'dilemma':>8}  {'T':>5}  {'R':>5}  {'P':>5}  {'S':>5}  {'R-P':>5}")
for dilemma in [0, 1, 2]:
    for c in [0.0, 0.1, 0.2, 0.3, 0.4]:
        T, R, P, S = payoffs(dilemma, c)
        print(f"{c:>5.2f}  {'d'+str(dilemma):>8}  {T:>5.3f}  {R:>5.3f}  {P:>5.3f}  {S:>5.3f}  {R-P:>+5.3f}")
    print()

# ── 2. Cooperation profiles by mechanism/dilemma/pop ─────────────────────────

CONDITIONS = [
    ("shuffle", "128"),
    ("noshuffle", "128"),
    ("shuffle", "4"),
    ("noshuffle", "4"),
]

MECHS_FULL = ["_", "M", "P", "MP", "MPQ", "IM", "IJM", "IMP", "IJMPQ"]
MECHS_PD_ONLY = ["P", "MP", "MPQ", "IM", "IJM", "IMP", "IJMPQ"]
POPS_HAM = ["pop_1", "pop_2", "pop_3"]
DILEMMAS = [0, 1, 2]


def hamilton_path(shuffle, gs, mech, dilemma, pop, fset):
    cond = f"{shuffle}_cost0.001_{gs}"
    return os.path.join(BASE, "hamilton", cond, mech, str(dilemma), pop,
                        f"csv_{fset}_for_image.con")


print("\n--- COOPERATION PROFILES (shuffle_128, PD, mechanisms) ---")
print("Mechanism, pop, fset | c=0.0 -> c=0.1 -> c=0.2 -> c=0.3 -> c=0.4")
for mech in MECHS_FULL:
    for dilemma in [1]:  # PD as primary
        for pop in ["pop_1", "pop_2"]:
            for fset in [0]:
                path = hamilton_path("shuffle", "128", mech, dilemma, pop, fset)
                rows = load_con(path)
                if rows is None:
                    continue
                rows = sorted_rows(rows)
                profile = [(float(r["c0"]), coop(r)) for r in rows]
                # Sample at c = 0, 0.1, 0.2, 0.3, 0.4
                sample_cs = [0.0, 0.1, 0.2, 0.3, 0.4]
                samples = []
                for sc in sample_cs:
                    matching = [q for c, q in profile if abs(c - sc) < 0.015]
                    samples.append(f"{matching[0]:.3f}" if matching else "n/a")
                print(f"  {mech:6s} d{dilemma} {pop} fset{fset}: {' | '.join(samples)}")
        print()

# ── 3. Hamilton pop_2 symmetry-breaking (fset_0 vs fset_1) ──────────────────

print("\n--- POP_2 SYMMETRY BREAKING: fset_0 (higher qBSeen) vs fset_1 ---")
print("(shuffle_128, PD)")
print(f"{'c':>5}  {'qB_0':>6}  {'qB_1':>6}  {'DeltaqB':>8}  {'w_0':>6}  {'w_1':>6}  {'Deltaw':>8}")
for mech in ["_", "M", "P", "MP", "IJMPQ"]:
    dilemma = 1
    path0 = hamilton_path("shuffle", "128", mech, dilemma, "pop_2", 0)
    path1 = hamilton_path("shuffle", "128", mech, dilemma, "pop_2", 1)
    rows0 = load_con(path0)
    rows1 = load_con(path1)
    if rows0 is None or rows1 is None:
        continue
    rows0 = sorted_rows(rows0)
    rows1 = sorted_rows(rows1)
    # merge by c0
    r1_map = {round(float(r["c0"]), 4): r for r in rows1}
    print(f"\n  Mech={mech} d{dilemma}")
    for r0 in rows0:
        c_val = round(float(r0["c0"]), 4)
        r1 = r1_map.get(c_val)
        if r1 is None:
            continue
        qb0 = float(r0["qBSeen"])
        qb1 = float(r1["qBSeen"])
        w0 = float(r0["wmean"])
        w1 = float(r1["wmean"])
        print(f"  {c_val:>5.2f}  {qb0:>6.3f}  {qb1:>6.3f}  {qb0-qb1:>+8.3f}  {w0:>6.3f}  {w1:>6.3f}  {w0-w1:>+8.3f}")

# ── 4. Dilemma comparison (no-dilemma vs PD vs snowdrift) for key mechs ──────

print("\n--- DILEMMA COMPARISON (shuffle_128, pop_2 fset_0) ---")
for mech in ["_", "M", "P"]:
    print(f"\n  Mech={mech}")
    print(f"  {'c':>5}  {'d0_qB':>7}  {'d1_qB':>7}  {'d2_qB':>7}")
    paths = {}
    rows_d = {}
    for d in [0, 1, 2]:
        p = hamilton_path("shuffle", "128", mech, d, "pop_2", 0)
        rows = load_con(p)
        if rows:
            rows_d[d] = {round(float(r["c0"]), 4): r for r in rows}
    for c_val in [0.0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4]:
        c_key = round(c_val, 4)
        vals = []
        for d in [0, 1, 2]:
            r = rows_d.get(d, {}).get(c_key)
            vals.append(f"{float(r['qBSeen']):.3f}" if r else "n/a")
        print(f"  {c_val:>5.2f}  {vals[0]:>7}  {vals[1]:>7}  {vals[2]:>7}")

# ── 5. Groupsize comparison ───────────────────────────────────────────────────

print("\n--- GROUPSIZE COMPARISON (shuffle, PD, pop_2 fset_0) ---")
print("Mech | c=0.0 / c=0.1 / c=0.2 / c=0.3 / c=0.4  [128 | 4]")
for mech in ["_", "M", "P", "IJMPQ"]:
    for gs in ["128", "4"]:
        path = hamilton_path("shuffle", gs, mech, 1, "pop_2", 0)
        rows = load_con(path)
        if rows is None:
            continue
        rows = sorted_rows(rows)
        samples = []
        for sc in [0.0, 0.1, 0.2, 0.3, 0.4]:
            matching = [coop(r) for r in rows if abs(float(r["c0"]) - sc) < 0.015]
            samples.append(f"{matching[0]:.3f}" if matching else "n/a")
        print(f"  {mech:6s} gs={gs}: {' | '.join(samples)}")
    print()

# ── 6. Shuffle vs noshuffle ──────────────────────────────────────────────────

print("\n--- SHUFFLE VS NOSHUFFLE (gs=128, PD, pop_2 fset_0) ---")
for mech in ["_", "M", "P", "IJMPQ"]:
    for shuffle in ["shuffle", "noshuffle"]:
        path = hamilton_path(shuffle, "128", mech, 1, "pop_2", 0)
        rows = load_con(path)
        if rows is None:
            continue
        rows = sorted_rows(rows)
        samples = []
        for sc in [0.0, 0.1, 0.2, 0.3, 0.4]:
            matching = [coop(r) for r in rows if abs(float(r["c0"]) - sc) < 0.015]
            samples.append(f"{matching[0]:.3f}" if matching else "n/a")
        print(f"  {mech:6s} {shuffle:10s}: {' | '.join(samples)}")
    print()

# ── 7. C1P1 / C1P0 / P1 genotype analysis (pop_1, P mechanism) ──────────────

print("\n--- GENOTYPE ANALYSIS (shuffle_128, PD, P mech, pop_1, fset_0) ---")
path = hamilton_path("shuffle", "128", "P", 1, "pop_1", 0)
rows = load_con(path)
if rows:
    rows = sorted_rows(rows)
    print(f"{'c':>5}  {'qBSeen':>7}  {'C1P1':>7}  {'C1P0':>7}  {'C0P1':>7}  {'P1':>7}  {'C1P0/qB%':>9}")
    for r in rows:
        c_val = float(r["c0"])
        qb = coop(r)
        _c1p1 = c1p1(r)
        _c1p0 = c1p0(r)
        _c0p1 = c0p1(r)
        _p1 = p1_freq(r)
        ratio = (_c1p0 / qb * 100) if qb > 0.01 else 0
        print(f"  {c_val:>5.2f}  {qb:>7.3f}  {_c1p1:>7.3f}  {_c1p0:>7.3f}  {_c0p1:>7.3f}  {_p1:>7.3f}  {ratio:>9.1f}")

print("\n--- GENOTYPE ANALYSIS (shuffle_128, PD, P mech, pop_2, fset_0 = higher qB) ---")
path = hamilton_path("shuffle", "128", "P", 1, "pop_2", 0)
rows = load_con(path)
if rows:
    rows = sorted_rows(rows)
    print(f"{'c':>5}  {'qBSeen':>7}  {'C1P1':>7}  {'C1P0':>7}  {'C0P1':>7}  {'P1':>7}  {'C1P0/qB%':>9}")
    for r in rows:
        c_val = float(r["c0"])
        qb = coop(r)
        _c1p1 = c1p1(r)
        _c1p0 = c1p0(r)
        _c0p1 = c0p1(r)
        _p1 = p1_freq(r)
        ratio = (_c1p0 / qb * 100) if qb > 0.01 else 0
        print(f"  {c_val:>5.2f}  {qb:>7.3f}  {_c1p1:>7.3f}  {_c1p0:>7.3f}  {_c0p1:>7.3f}  {_p1:>7.3f}  {ratio:>9.1f}")

# ── 8. Pop_3 analysis ─────────────────────────────────────────────────────────

print("\n--- POP_3 ANALYSIS (shuffle_128, PD, P mech, pop_3) ---")
print("fset_0 = evolving, fset_1 = fixed (25% each C0P0/C0P1/C1P0/C1P1)")
for fset, label in [(0, "evolving"), (1, "fixed")]:
    path = hamilton_path("shuffle", "128", "P", 1, "pop_3", fset)
    rows = load_con(path)
    if rows is None:
        print(f"  fset_{fset}: not found")
        continue
    rows = sorted_rows(rows)
    print(f"\n  fset_{fset} ({label})")
    print(f"  {'c':>5}  {'qBSeen':>7}  {'C1P1':>7}  {'C1P0':>7}  {'C0P1':>7}")
    for r in rows:
        c_val = float(r["c0"])
        qb = coop(r)
        _c1p1 = c1p1(r)
        _c1p0 = c1p0(r)
        _c0p1 = c0p1(r)
        print(f"  {c_val:>5.2f}  {qb:>7.3f}  {_c1p1:>7.3f}  {_c1p0:>7.3f}  {_c0p1:>7.3f}")

# ── 9. All-mechanism summary table (PD, shuffle_128, pop_2 fset_0) ────────────

print("\n--- ALL-MECHANISM SUMMARY (shuffle_128, PD, pop_2 fset_0, qBSeen at selected c) ---")
sample_cs = [0.0, 0.08, 0.16, 0.24, 0.32, 0.4]
header = f"{'Mech':8s}" + "".join(f"  c={c:.2f}" for c in sample_cs)
print(header)
for mech in MECHS_FULL:
    # PD only for mechs that only have PD; else also no-dilemma
    dilemmas_to_check = [0, 1, 2] if mech in ["_", "M"] else [1, 2]
    for d in dilemmas_to_check:
        path = hamilton_path("shuffle", "128", mech, d, "pop_2", 0)
        rows = load_con(path)
        if rows is None:
            continue
        rmap = {round(float(r["c0"]), 4): float(r["qBSeen"]) for r in rows}
        vals = [f"{rmap.get(round(c, 4), float('nan')):.3f}" for c in sample_cs]
        print(f"  {mech:4s} d{d}  {'  '.join(vals)}")

# ── 10. hamilton_1run temporal dynamics ──────────────────────────────────────

print("\n--- HAMILTON_1RUN: TEMPORAL DYNAMICS (shuffle_128, PD, P, pop_2) ---")


def hamilton_1run_path(shuffle, gs, mech, dilemma, pop, fset):
    cond = f"{shuffle}_cost0.001_{gs}"
    return os.path.join(BASE, "hamilton_1run", cond, mech, str(dilemma), pop,
                        f"csv_{fset}_for_movie.con")


for fset in [0, 1]:
    path = hamilton_1run_path("shuffle", "128", "P", 1, "pop_2", fset)
    rows = load_con(path)
    if rows is None:
        print(f"  fset_{fset}: not found at {path}")
        continue
    print(f"\n  fset_{fset}:")
    # Group by c0
    by_c = defaultdict(list)
    for r in rows:
        by_c[round(float(r["c0"]), 4)].append(r)
    c_vals = sorted(by_c.keys())
    for c_val in c_vals:
        cell_rows = sorted(by_c[c_val], key=lambda r: int(r["Time"]))
        times = [int(r["Time"]) for r in cell_rows]
        qbs = [float(r["qBSeen"]) for r in cell_rows]
        mn, mx = min(qbs[1:]) if len(qbs) > 1 else qbs[0], max(qbs[1:]) if len(qbs) > 1 else qbs[0]
        rng = mx - mn
        traj_str = " ".join(f"{q:.3f}" for q in qbs)
        print(f"    c={c_val:.2f}  range={rng:.3f}  traj=[{traj_str}]")


# ══════════════════════════════════════════════════════════════════════════════
# MUTUALISM ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("MUTUALISM ANALYSIS  (K=0.5, b=0.4, c0<c1, triangular grid 210 cells)")
print("=" * 80)
print("pop_2 only; fset_0=higher qBSeen (lower-cost pop), fset_1=lower qBSeen")


def mut_path(shuffle, gs, mech, dilemma, fset):
    cond = f"{shuffle}_cost0.001_{gs}"
    return os.path.join(BASE, "mutualism", cond, mech, str(dilemma), "pop_2",
                        f"csv_{fset}_for_image.con")


# ── 11. Cooperation landscape overview ───────────────────────────────────────

print("\n--- COOPERATION LANDSCAPE (noshuffle_128, PD, M mech) ---")
print("c0/c1 bins: [0-0.1] [0.1-0.2] [0.2-0.3] [0.3-0.4]")
path0 = mut_path("noshuffle", "128", "M", 1, 0)
rows0 = load_con(path0)
if rows0:
    # Show cooperation at selected (c0, c1) pairs
    rmap = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): r for r in rows0}
    print(f"\n  fset_0 (lower-cost pop, higher cooperation):")
    print(f"  {'c0\\c1':>5}", end="")
    c1_samples = [0.1, 0.2, 0.3, 0.4]
    for c1 in c1_samples:
        print(f"  c1={c1:.1f}", end="")
    print()
    for c0 in [0.0, 0.1, 0.2, 0.3]:
        print(f"  {c0:>5.1f}", end="")
        for c1 in c1_samples:
            if c1 <= c0:
                print(f"  {'---':>6}", end="")
                continue
            # find closest cell
            best_key = min(rmap.keys(),
                           key=lambda k: (abs(k[0]-c0) + abs(k[1]-c1)))
            r = rmap[best_key]
            print(f"  {float(r['qBSeen']):>6.3f}", end="")
        print()

# ── 12. Role split: who cooperates more (fset_0 vs fset_1)? ──────────────────

print("\n--- ROLE SPLIT: fset_0 > fset_1 fraction (PD, noshuffle_128, P mech) ---")
for mech in ["_", "M", "P", "MP", "IJMPQ"]:
    for dilemma in [1, 2]:
        path0 = mut_path("noshuffle", "128", mech, dilemma, 0)
        path1 = mut_path("noshuffle", "128", mech, dilemma, 1)
        rows0 = load_con(path0)
        rows1 = load_con(path1)
        if rows0 is None or rows1 is None:
            continue
        r0map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): float(r["qBSeen"]) for r in rows0}
        r1map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): float(r["qBSeen"]) for r in rows1}
        n_fset0_higher = sum(1 for k in r0map if r0map.get(k, 0) > r1map.get(k, 0))
        n_total = len(r0map)
        avg0 = sum(r0map.values()) / len(r0map) if r0map else 0
        avg1 = sum(r1map.values()) / len(r1map) if r1map else 0
        print(f"  {mech:6s} d{dilemma}: fset_0>fset_1 in {n_fset0_higher}/{n_total} cells | mean qB_0={avg0:.3f}, qB_1={avg1:.3f}")

# ── 13. Exploitation correlation ─────────────────────────────────────────────

print("\n--- EXPLOITATION: correlation(ΔqBSeen, Δfitness) ---")
import math

def corr(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan")
    mx = sum(xs) / n; my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx)**2 for x in xs))
    dy = math.sqrt(sum((y - my)**2 for y in ys))
    return num / (dx * dy) if dx * dy > 0 else float("nan")

for mech in ["_", "M", "P", "IJMPQ"]:
    for dilemma in [1]:
        for shuffle in ["noshuffle", "shuffle"]:
            path0 = mut_path(shuffle, "128", mech, dilemma, 0)
            path1 = mut_path(shuffle, "128", mech, dilemma, 1)
            rows0 = load_con(path0)
            rows1 = load_con(path1)
            if rows0 is None or rows1 is None:
                continue
            r0map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): r for r in rows0}
            r1map = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): r for r in rows1}
            dqb = []
            dw = []
            for k in r0map:
                if k not in r1map:
                    continue
                dqb.append(float(r0map[k]["qBSeen"]) - float(r1map[k]["qBSeen"]))
                dw.append(float(r0map[k]["wmean"]) - float(r1map[k]["wmean"]))
            c = corr(dqb, dw)
            print(f"  {mech:6s} d{dilemma} {shuffle:10s}: corr(ΔqBSeen, Δfitness) = {c:.3f}")

# ── 14. Mechanism comparison in mutualism (along diagonal slice) ──────────────

print("\n--- MECHANISM COMPARISON: diagonal slice c0=c1 (noshuffle_128, PD, fset_0) ---")
# Hamilton is the diagonal; for mutualism, the diagonal is where c0=c1
# but in mutualism the triangular grid has c0 < c1 always
# So let's instead compare mechanisms at fixed c0=0.1, c1=0.3 (asymmetric) and c0=0.1, c1=0.2 (mild)
print("  Sample cells: (c0=0.1, c1=0.3) and (c0=0.1, c1=0.2)")
for mech in ["_", "M", "P", "MP", "MPQ", "IMP", "IJMPQ"]:
    for dilemma in [1, 2]:
        for fset in [0, 1]:
            path = mut_path("noshuffle", "128", mech, dilemma, fset)
            rows = load_con(path)
            if rows is None:
                continue
            rmap = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): float(r["qBSeen"]) for r in rows}
            v1 = rmap.get((0.1, 0.3), float("nan"))
            v2 = rmap.get((0.1, 0.2), float("nan"))
            print(f"  {mech:6s} d{dilemma} fset{fset}: (0.1,0.3)={v1:.3f}  (0.1,0.2)={v2:.3f}")
    print()

# ── 15. Mutualism groupsize/shuffle effects ───────────────────────────────────

print("\n--- MUTUALISM GROUPSIZE/SHUFFLE EFFECTS (PD, M mech, fset_0) ---")
sample_cells = [(0.02, 0.38), (0.1, 0.2), (0.2, 0.38)]
print(f"  {'cond':20s}", end="")
for sc in sample_cells:
    print(f"  ({sc[0]:.2f},{sc[1]:.2f})", end="")
print()
for shuffle in ["shuffle", "noshuffle"]:
    for gs in ["128", "4"]:
        path = mut_path(shuffle, gs, "M", 1, 0)
        rows = load_con(path)
        if rows is None:
            continue
        rmap = {(round(float(r["c0"]), 4), round(float(r["c1"]), 4)): float(r["qBSeen"]) for r in rows}
        label = f"{shuffle}_gs{gs}"
        print(f"  {label:20s}", end="")
        for sc in sample_cells:
            best_key = min(rmap.keys(), key=lambda k: abs(k[0]-sc[0])+abs(k[1]-sc[1]))
            if abs(best_key[0]-sc[0]) + abs(best_key[1]-sc[1]) < 0.05:
                print(f"  {rmap[best_key]:.3f}     ", end="")
            else:
                print(f"  n/a       ", end="")
        print()

# ── 16. mutualism_1run temporal dynamics ─────────────────────────────────────

print("\n--- MUTUALISM_1RUN: TEMPORAL DYNAMICS (noshuffle_128, PD, M, fset_0) ---")


def mut_1run_path(shuffle, gs, mech, dilemma, fset):
    cond = f"{shuffle}_cost0.001_{gs}"
    return os.path.join(BASE, "mutualism_1run", cond, mech, str(dilemma), "pop_2",
                        f"csv_{fset}_for_movie.con")


path = mut_1run_path("noshuffle", "128", "M", 1, 0)
rows = load_con(path)
if rows:
    by_c = defaultdict(list)
    for r in rows:
        key = (round(float(r["c0"]), 4), round(float(r["c1"]), 4))
        by_c[key].append(r)
    # Sample a few cells
    sample_keys = sorted(by_c.keys())
    for key in sample_keys[:10]:
        cell_rows = sorted(by_c[key], key=lambda r: int(r["Time"]))
        qbs = [float(r["qBSeen"]) for r in cell_rows]
        rng = max(qbs) - min(qbs)
        print(f"  c0={key[0]:.2f} c1={key[1]:.2f}: range={rng:.3f} traj=[{' '.join(f'{q:.3f}' for q in qbs)}]")
else:
    print("  (file not found)")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
