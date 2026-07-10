#!/usr/bin/env python3
"""
Analyze the asymmetric_c1_i study: how information cost Cost interacts with the
deterministic cooperator/exploiter split of asymmetric_c0_c1 pop_2.

Unlike symmetric_c_i, this sweep fixes c0 = 0.10 for the low-cost population and
sweeps Cost jointly with c1 over the triangular grid Cost + c1 <= 0.40, c1 > c0.
Cell key is therefore (Cost, c1), with pop_0 the low-cost side and pop_1 the
high-cost side.

Primary condition: pop_2, PD (dilemma 1), noshuffle, gs=128.
"""

import os
from statistics import mean

from trps_io import allele, corr, load

BASE = os.path.expanduser("~/results")
MC = f"{BASE}/asymmetric_c1_i"
MC1 = f"{BASE}/asymmetric_c1_i_1run"
ASYMM = f"{BASE}/asymmetric_c0_c1"
HC = f"{BASE}/symmetric_c_i"

MECHS = ["_", "M", "P", "MP", "MPQ", "IMP", "IJMPQ"]
PRIMARY_MECHS = ["M", "P", "IMP", "IJMPQ"]
SAMPLE_COSTS = [0.0, 0.04, 0.08, 0.12, 0.20, 0.28]
SAMPLE_C1 = [0.12, 0.20, 0.30, 0.40]


def mc_path(study, sh, gs, mech, d, f, movie=False):
    suffix = "movie" if movie else "image"
    return f"{BASE}/{study}/{sh}/{gs}/{mech}/{d}/pop_2/csv_{f}_for_{suffix}.con"


def asymmetric_c0_c1_path(sh, gs, mech, d, f):
    return f"{ASYMM}/{sh}/{gs}/{mech}/{d}/pop_2/csv_{f}_for_image.con"


def hc_path(sh, gs, mech, d, pop, f):
    return f"{HC}/{sh}/{gs}/{mech}/{d}/{pop}/csv_{f}_for_image.con"


def mc_cell(rows, cost, c1, col="qBSeen"):
    for r in rows:
        if abs(float(r["Cost"]) - cost) < 0.005 and abs(float(r["c1"]) - c1) < 0.005:
            return float(r[col])
    return float("nan")


def mc_cell_row(rows, cost, c1):
    for r in rows:
        if abs(float(r["Cost"]) - cost) < 0.005 and abs(float(r["c1"]) - c1) < 0.005:
            return r
    return None


def asymmetric_c0_c1_cell(rows, c0, c1, col="qBSeen"):
    for r in rows:
        if abs(float(r["c0"]) - c0) < 0.005 and abs(float(r["c1"]) - c1) < 0.005:
            return float(r[col])
    return float("nan")


def hc_cell(rows, cost, c, col="qBSeen"):
    for r in rows:
        if abs(float(r["Cost"]) - cost) < 0.005 and abs(float(r["c0"]) - c) < 0.005:
            return float(r[col])
    return float("nan")


def threshold(rows, cost):
    vals = sorted((float(r["c1"]), float(r["qBSeen"])) for r in rows
                  if abs(float(r["Cost"]) - cost) < 0.005)
    good = [c1 for c1, q in vals if q >= 0.5]
    return max(good) if good else None


def mean_at_cost(rows, cost, col="qBSeen"):
    vals = [float(r[col]) for r in rows if abs(float(r["Cost"]) - cost) < 0.005]
    return mean(vals) if vals else float("nan")


def paired_deltas(mech, d=1, sh="noshuffle", gs="128"):
    r0 = load(mc_path("asymmetric_c1_i", sh, gs, mech, d, 0))
    r1 = load(mc_path("asymmetric_c1_i", sh, gs, mech, d, 1))
    m1 = {(round(float(r["Cost"]), 3), round(float(r["c1"]), 3)): r for r in r1}
    dq, dw = [], []
    for r in r0:
        rr = m1[(round(float(r["Cost"]), 3), round(float(r["c1"]), 3))]
        dq.append(float(r["qBSeen"]) - float(rr["qBSeen"]))
        dw.append(float(r["wmean"]) - float(rr["wmean"]))
    return dq, dw


print("=" * 78)
print("ASYMMETRIC_C1_I  (fixed c0=0.10; triangular Cost x c1 grid, Cost+c1<=0.40)")
print("Primary: pop_2, PD (d1), noshuffle, gs=128.  cell=(Cost,c1).")
print("=" * 78)

print("\n--- A. SANITY: Cost=0 slice vs asymmetric_c0_c1 at c0=0.10 (PD, ns, gs128) ---")
for mech in MECHS:
    r0 = load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 0))
    r1 = load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 1))
    b0 = load(asymmetric_c0_c1_path("noshuffle", "128", mech, 1, 0))
    b1 = load(asymmetric_c0_c1_path("noshuffle", "128", mech, 1, 1))
    print(f"  {mech}:")
    for c1 in SAMPLE_C1:
        a0 = mc_cell(r0, 0.0, c1)
        a1 = mc_cell(r1, 0.0, c1)
        m0 = asymmetric_c0_c1_cell(b0, 0.10, c1)
        m1 = asymmetric_c0_c1_cell(b1, 0.10, c1)
        print(f"    c1={c1:.2f}: pop0 {a0:.3f} vs {m0:.3f} ({a0-m0:+.3f}), "
              f"pop1 {a1:.3f} vs {m1:.3f} ({a1-m1:+.3f})")

print("\n--- B. COST MEANS (PD, noshuffle, gs128) ---")
print("mean qBSeen over each available c1 column")
for mech in MECHS:
    r0 = load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 0))
    r1 = load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 1))
    line = f"  {mech:6}"
    for co in SAMPLE_COSTS:
        a0 = mean_at_cost(r0, co)
        a1 = mean_at_cost(r1, co)
        if a0 == a0:
            line += f"  C{co:0.2f}:{a0:.3f}/{a1:.3f}"
    print(line)

print("\n--- C. c1 THRESHOLD RETREAT (max c1 with qBSeen>=0.5; PD, ns, gs128) ---")
for mech in PRIMARY_MECHS + ["MP", "MPQ"]:
    for f in (0, 1):
        r = load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, f))
        vals = []
        for co in SAMPLE_COSTS:
            vals.append(f"C{co:0.2f}:{threshold(r, co)}")
        print(f"  {mech} pop_{f}: " + "  ".join(vals))

print("\n--- D. ASYMMETRY COMPRESSION (Pop0-Pop1; PD, ns, gs128) ---")
for mech in PRIMARY_MECHS:
    dq, dw = paired_deltas(mech)
    print(f"  {mech}: corr(dq,dw)={corr(dq,dw):.3f}, "
          f"inverted_cells={sum(1 for x,y in zip(dq,dw) if x*y<0)}/{len(dq)}")
    r0 = load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 0))
    r1 = load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 1))
    m1 = {(round(float(r['Cost']), 3), round(float(r['c1']), 3)): r for r in r1}
    for co in SAMPLE_COSTS:
        xq, xw = [], []
        for r in r0:
            if abs(float(r["Cost"]) - co) >= 0.005:
                continue
            rr = m1[(round(float(r["Cost"]), 3), round(float(r["c1"]), 3))]
            xq.append(float(r["qBSeen"]) - float(rr["qBSeen"]))
            xw.append(float(r["wmean"]) - float(rr["wmean"]))
        if xq:
            print(f"    Cost={co:.2f}: mean dq={mean(xq):.3f}, mean dw={mean(xw):+.3f}")

print("\n--- E. M CONTROL DECOMPOSITION (means over c1; ns gs128) ---")
for co in SAMPLE_COSTS:
    out = []
    for d in (0, 1, 2):
        for f in (0, 1):
            rows = load(mc_path("asymmetric_c1_i", "noshuffle", "128", "M", d, f))
            vals = [r for r in rows if abs(float(r["Cost"]) - co) < 0.005]
            out.append((d, f,
                        mean(float(r["qBSeen"]) for r in vals),
                        mean(allele(r, "M1") for r in vals)))
    print(f"  Cost={co:.2f}: " + "  ".join(
        f"d{d} pop_{f} q={q:.3f} M1={m1:.3f}" for d, f, q, m1 in out))

print("\n--- F. MACHINERY EROSION IN SELECTED CELLS (PD, ns, gs128) ---")
for mech, tok in (("P", "P1"), ("M", "M1")):
    print(f"  {mech}:")
    for f in (0, 1):
        rows = load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, f))
        print(f"    pop_{f}:")
        for co, c1 in ((0.0, 0.20), (0.08, 0.20), (0.12, 0.20), (0.20, 0.18)):
            r = mc_cell_row(rows, co, c1)
            if r:
                free = allele(r, "C1", tok[0] + "0")
                print(f"      (Cost={co:.2f}, c1={c1:.2f}) q={float(r['qBSeen']):.3f} "
                      f"{tok}={allele(r, tok):.3f} free={free:.3f}")

print("\n--- G. SHUFFLE / GROUPSIZE MIRRORS (PD means) ---")
for mech in ("P", "MP", "IMP", "IJMPQ"):
    print(f"  {mech}:")
    for co in (0.0, 0.08, 0.12):
        ns0 = mean_at_cost(load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 0)), co)
        ns1 = mean_at_cost(load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 1)), co)
        sh0 = mean_at_cost(load(mc_path("asymmetric_c1_i", "shuffle", "128", mech, 1, 0)), co)
        sh1 = mean_at_cost(load(mc_path("asymmetric_c1_i", "shuffle", "128", mech, 1, 1)), co)
        print(f"    Cost={co:.2f}: ns {ns0:.3f}/{ns1:.3f}  sh {sh0:.3f}/{sh1:.3f}")
for mech in ("M", "P", "IJMPQ"):
    print(f"  gs comparison {mech}:")
    for co in (0.0, 0.08, 0.20):
        a0 = mean_at_cost(load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 0)), co)
        a1 = mean_at_cost(load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 1)), co)
        b0 = mean_at_cost(load(mc_path("asymmetric_c1_i", "noshuffle", "4", mech, 1, 0)), co)
        b1 = mean_at_cost(load(mc_path("asymmetric_c1_i", "noshuffle", "4", mech, 1, 1)), co)
        print(f"    Cost={co:.2f}: gs128 {a0:.3f}/{a1:.3f}  gs4 {b0:.3f}/{b1:.3f}")

print("\n--- H. SNOWDRIFT CONTRAST (means by Cost; ns gs128) ---")
for mech in ("M", "P", "IJMPQ"):
    print(f"  {mech}:")
    for d in (1, 2):
        line = f"    d{d}:"
        for co in (0.0, 0.08, 0.20, 0.28):
            r0 = mean_at_cost(load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, d, 0)), co)
            r1 = mean_at_cost(load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, d, 1)), co)
            line += f"  C{co:.2f}:{r0:.3f}/{r1:.3f}"
        print(line)

print("\n--- I. TEMPORAL SAMPLES (asymmetric_c1_i_1run movies, ns gs128 PD) ---")
for mech, co, c1 in (("P", 0.00, 0.20), ("P", 0.12, 0.20),
                     ("M", 0.00, 0.20), ("IJMPQ", 0.12, 0.20),
                     ("IJMPQ", 0.20, 0.20)):
    print(f"  {mech} at (Cost={co:.2f}, c1={c1:.2f})")
    for f in (0, 1):
        rows = load(mc_path("asymmetric_c1_i_1run", "noshuffle", "128", mech, 1, f, movie=True))
        pts = sorted((int(float(r["Time"])), float(r["qBSeen"])) for r in rows
                     if abs(float(r["Cost"]) - co) < 0.005 and abs(float(r["c1"]) - c1) < 0.005)
        print(f"    pop_{f}: " + "  ".join(f"{t}:{q:.3f}" for t, q in pts))

print("\n--- J. SYMMETRIC REFERENCE: symmetric_c_i pop_2 at c=0.10 vs asymmetric_c1_i c1=0.12 ---")
for mech in PRIMARY_MECHS:
    h0 = hc_cell(load(hc_path("noshuffle", "128", mech, 1, "pop_2", 0)), 0.0, 0.10)
    h1 = hc_cell(load(hc_path("noshuffle", "128", mech, 1, "pop_2", 1)), 0.0, 0.10)
    m0 = mc_cell(load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 0)), 0.0, 0.12)
    m1 = mc_cell(load(mc_path("asymmetric_c1_i", "noshuffle", "128", mech, 1, 1)), 0.0, 0.12)
    print(f"  {mech}: symmetric_c_i {h0:.3f}/{h1:.3f}  asymmetric_c1_i {m0:.3f}/{m1:.3f}")

print("\n" + "=" * 78)
print("DONE")
print("=" * 78)
