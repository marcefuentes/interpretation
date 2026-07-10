#!/usr/bin/env python3
"""
Analyze the asymmetric_i0_i1 study: symmetric cooperation cost (c0 = c1 = c) with
asymmetric per-population information cost (Cost0, Cost1).

Cell key is (c, Cost0, Cost1) with Cost0 < Cost1 on a strict triangle bounded by
Cost_p <= b - c per population. Primary slice: c = 0.10 (120 cells); secondary
c = 0.20 exists in raw CSV (55 cells) but is omitted from filtered .con exports.

Primary condition: pop_2, PD (dilemma 1), noshuffle, gs = 128.
"""

import glob
import os
from statistics import mean

from trps_io import allele, corr, glo, load

BASE = os.path.expanduser("~/results")
STUDY = "asymmetric_i0_i1"
STUDY1 = "asymmetric_i0_i1_1run"
SYM_C = f"{BASE}/symmetric_c"

MECHS = ["_", "M", "P", "MP", "MPQ", "IMP", "IJMPQ"]
PRIMARY = ["M", "P", "IMP", "IJMPQ"]


def ai_path(study, sh, gs, mech, d, f, movie=False, slice_tag="filtered"):
    tag = f"{slice_tag}_" if slice_tag else ""
    suffix = "movie" if movie else "image"
    return f"{BASE}/{study}/{sh}/{gs}/{mech}/{d}/pop_2/csv_{f}_{tag}for_{suffix}.con"


def grid_key(r):
    return (round(float(r["c0"]), 2), round(float(r["Cost0"]), 2), round(float(r["Cost1"]), 2))


def ai_cell(rows, c, cost0, cost1, col="qBSeen"):
    for r in rows:
        if (abs(float(r["c0"]) - c) < 0.005 and abs(float(r["Cost0"]) - cost0) < 0.005
                and abs(float(r["Cost1"]) - cost1) < 0.005):
            return float(r[col])
    return float("nan")


def ai_cell_row(rows, c, cost0, cost1):
    for r in rows:
        if (abs(float(r["c0"]) - c) < 0.005 and abs(float(r["Cost0"]) - cost0) < 0.005
                and abs(float(r["Cost1"]) - cost1) < 0.005):
            return r
    return None


def triangle_pairs(r0, r1, c=0.10):
    """Yield (r0, r1) for strict triangle cells at cooperation cost c."""
    m1 = {grid_key(r): r for r in r1}
    for r in r0:
        if abs(float(r["c0"]) - c) > 0.005:
            continue
        if float(r["Cost0"]) >= float(r["Cost1"]) - 0.001:
            continue
        yield r, m1[grid_key(r)]


def gap_stats(mech, c=0.10, sh="noshuffle", gs="128", d=1, slice_tag="filtered"):
    r0 = load(ai_path(STUDY, sh, gs, mech, d, 0, slice_tag=slice_tag))
    r1 = load(ai_path(STUDY, sh, gs, mech, d, 1, slice_tag=slice_tag))
    dq, dw, gaps = [], [], []
    for a, b in triangle_pairs(r0, r1, c):
        dq.append(float(a["qBSeen"]) - float(b["qBSeen"]))
        dw.append(float(a["wmean"]) - float(b["wmean"]))
        gaps.append(float(b["Cost1"]) - float(a["Cost0"]))
    return dq, dw, gaps


def sym_c_q(mech, f, c=0.10):
    rows = load(f"{SYM_C}/noshuffle/128/{mech}/1/pop_2/csv_{f}_for_image.con")
    for r in rows:
        if abs(float(r["c0"]) - c) < 0.005:
            return float(r["qBSeen"])
    return float("nan")


def c20_dq_from_csv(mech):
    """Secondary c = 0.20 slice from per-cell CSV (not in filtered .con)."""
    d = f"{BASE}/{STUDY}/noshuffle/128/{mech}/1/pop_2"
    dqs = []
    for gpath in glob.glob(f"{d}/*.glo"):
        m = glo(gpath)
        if abs(float(m["c0"]) - 0.20) > 0.005:
            continue
        co0, co1 = float(m["Cost0"]), float(m["Cost1"])
        if co0 >= co1 - 0.001:
            continue
        stem = gpath.replace(".glo", "")
        qs = []
        for pop in ("0", "1"):
            cp = f"{stem}_{pop}.csv"
            if not os.path.exists(cp):
                break
            import csv
            with open(cp) as f:
                rows = list(csv.reader(f))
            qi = rows[0].index("qBSeen")
            qs.append(float(rows[-1][qi]))
        if len(qs) == 2:
            dqs.append(qs[0] - qs[1])
    return dqs


print("=" * 78)
print("ASYMMETRIC_I0_I1  (symmetric c; triangle Cost0 < Cost1; pop_2)")
print("Primary: c=0.10, PD (d1), noshuffle, gs=128.  cell=(Cost0,Cost1).")
print("=" * 78)

print("\n--- A. GRID ---")
r0 = load(ai_path(STUDY, "noshuffle", "128", "IJMPQ", 1, 0))
print(f"  filtered con cells at c=0.10: {len(r0)} (expect 120)")

print("\n--- B. vs symmetric_c pop_2 at c=0.10 (stochastic baseline) ---")
for mech in PRIMARY:
    s0, s1 = sym_c_q(mech, 0), sym_c_q(mech, 1)
    print(f"  {mech}: sym {s0:.3f}/{s1:.3f} dq={s0 - s1:+.3f}")

print("\n--- C. ROLE SPLIT (triangle means; pop0 - pop1) ---")
for mech in PRIMARY:
    dq, dw, gaps = gap_stats(mech)
    p0 = sum(1 for x in dq if x > 0.02)
    p1 = sum(1 for x in dq if x < -0.02)
    print(f"  {mech}: mean dq={mean(dq):+.3f}, mean dw={mean(dw):+.3f}, "
          f"corr(gap,dq)={corr(gaps, dq):.3f}, pop0 coops {p0}/{len(dq)}, pop1 coops {p1}/{len(dq)}")

print("\n--- D. SELECTED CELLS c=0.10 (Cost0, Cost1) ---")
for mech in MECHS:
    if mech in ("MPQ",):
        continue
    r0 = load(ai_path(STUDY, "noshuffle", "128", mech, 1, 0))
    r1 = load(ai_path(STUDY, "noshuffle", "128", mech, 1, 1))
    print(f"  {mech} at (0.00, 0.20):")
    q0 = ai_cell(r0, 0.10, 0.0, 0.20)
    q1 = ai_cell(r1, 0.10, 0.0, 0.20)
    if q0 == q0:
        print(f"    q {q0:.3f}/{q1:.3f}  dq={q0 - q1:+.3f}  "
              f"w {ai_cell(r0, 0.10, 0.0, 0.20, 'wmean'):.3f}/"
              f"{ai_cell(r1, 0.10, 0.0, 0.20, 'wmean'):.3f}")

print("\n--- E. IJMPQ dose-response at Cost0=0 ---")
r0 = load(ai_path(STUDY, "noshuffle", "128", "IJMPQ", 1, 0))
r1 = load(ai_path(STUDY, "noshuffle", "128", "IJMPQ", 1, 1))
for co1 in [0.02, 0.10, 0.20, 0.30]:
    q0 = ai_cell(r0, 0.10, 0.0, co1)
    q1 = ai_cell(r1, 0.10, 0.0, co1)
    w0 = ai_cell(r0, 0.10, 0.0, co1, "wmean")
    w1 = ai_cell(r1, 0.10, 0.0, co1, "wmean")
    print(f"  Cost1={co1:.2f}: q {q0:.3f}/{q1:.3f} dq={q0 - q1:+.3f} dw={w0 - w1:+.3f}")

print("\n--- F. GENOTYPE DECOMPOSITION ---")
for mech, tok in (("P", "P1"), ("M", "M1"), ("IJMPQ", "P1")):
    print(f"  {mech}:")
    for co0, co1 in ((0.0, 0.10), (0.0, 0.20)):
        for f in (0, 1):
            rows = load(ai_path(STUDY, "noshuffle", "128", mech, 1, f))
            r = ai_cell_row(rows, 0.10, co0, co1)
            if r:
                free = allele(r, "C1", tok[0] + "0")
                print(f"    pop_{f} ({co0:.2f},{co1:.2f}): q={float(r['qBSeen']):.3f} "
                      f"{tok}={allele(r, tok):.3f} C1{tok[0]}0={free:.3f}")

print("\n--- G. PARADOX OF SUCCESS (dq*dw < 0) ---")
for mech in PRIMARY:
    dq, dw, _ = gap_stats(mech)
    inv = sum(1 for x, y in zip(dq, dw) if x * y < 0)
    print(f"  {mech}: inverted {inv}/{len(dq)}")

print("\n--- H. FITNESS DOMINANCE ---")
for mech in PRIMARY:
    dq, dw, _ = gap_stats(mech)
    p0 = sum(1 for x in dw if x > 0.005)
    p1 = sum(1 for x in dw if x < -0.005)
    print(f"  {mech}: pop0 fitter {p0}/{len(dw)}, pop1 fitter {p1}/{len(dw)}")

print("\n--- I. SHUFFLE / GS ---")
for sh, gs in [("noshuffle", "128"), ("shuffle", "128"), ("noshuffle", "4")]:
    for mech in ("P", "IJMPQ"):
        dq, dw, _ = gap_stats(mech, sh=sh, gs=gs)
        print(f"  {sh} gs{gs} {mech}: mean dq={mean(dq):+.3f}, mean dw={mean(dw):+.3f}")

print("\n--- J. SNOWDRIFT d=2 (triangle summary) ---")
for mech in PRIMARY + ["_"]:
    dq, dw, gaps = gap_stats(mech, d=2)
    p0 = sum(1 for x in dq if x > 0.02)
    p1 = sum(1 for x in dq if x < -0.02)
    tie = len(dq) - p0 - p1
    print(f"  {mech}: mean dq={mean(dq):+.3f}, pop0>{p0} pop1>{p1} tie={tie}, "
          f"corr(gap,dq)={corr(gaps, dq):.3f}, corr(dq,dw)={corr(dq, dw):.3f}")

print("\n--- J2. SNOWDRIFT vs PD selected cells ---")
for mech in ("P", "IJMPQ"):
    print(f"  {mech}:")
    for d, name in ((1, "PD"), (2, "SD")):
        r0 = load(ai_path(STUDY, "noshuffle", "128", mech, d, 0))
        r1 = load(ai_path(STUDY, "noshuffle", "128", mech, d, 1))
        for co0, co1 in ((0.0, 0.20), (0.0, 0.30)):
            q0 = ai_cell(r0, 0.10, co0, co1)
            q1 = ai_cell(r1, 0.10, co0, co1)
            if q0 == q0:
                print(f"    {name} ({co0:.2f},{co1:.2f}): q {q0:.3f}/{q1:.3f} dq={q0 - q1:+.3f}")

print("\n--- J3. P snowdrift Cost0-row sign flips ---")
r0 = load(ai_path(STUDY, "noshuffle", "128", "P", 2, 0))
r1 = load(ai_path(STUDY, "noshuffle", "128", "P", 2, 1))
m1 = {grid_key(r): r for r in r1}
by_c0 = {}
for r in r0:
    if float(r["Cost0"]) >= float(r["Cost1"]) - 0.001:
        continue
    co0 = round(float(r["Cost0"]), 2)
    rr = m1[grid_key(r)]
    dq = float(r["qBSeen"]) - float(rr["qBSeen"])
    by_c0.setdefault(co0, []).append(dq)
mixed = sum(1 for dqs in by_c0.values()
            if any(x > 0.02 for x in dqs) and any(x < -0.02 for x in dqs))
print(f"  Cost0-rows with both dq signs: {mixed}/{len(by_c0)}")

print("\n--- K. COLLAPSE (q0+q1 < 0.15) ---")
for mech in ["P", "M", "IJMPQ"]:
    r0 = load(ai_path(STUDY, "noshuffle", "128", mech, 1, 0))
    r1 = load(ai_path(STUDY, "noshuffle", "128", mech, 1, 1))
    n = sum(1 for a, b in triangle_pairs(r0, r1) if float(a["qBSeen"]) + float(b["qBSeen"]) < 0.15)
    print(f"  {mech}: {n}/120")

print("\n--- L. SECONDARY c=0.20 (c020 .con exports, PD d=1) ---")
for mech in ("P", "MP", "IMP", "IJMPQ", "M"):
    dq, dw, _ = gap_stats(mech, c=0.20, slice_tag="c020")
    p1 = sum(1 for x in dq if x < -0.02)
    inv = sum(1 for x, y in zip(dq, dw) if x * y < 0)
    print(f"  {mech}: n={len(dq)}, mean dq={mean(dq):+.3f}, mean dw={mean(dw):+.3f}, "
          f"corr(dq,dw)={corr(dq, dw):.3f}, "
          f"pop0 coops {sum(1 for x in dq if x > 0.02)}/{len(dq)}, "
          f"pop1 coops {p1}/{len(dq)}, inv={inv}/{len(dq)}")

print("\n--- L2. c=0.20 SELECTED CELLS ---")
for mech in ("P", "IJMPQ"):
    print(f"  {mech}:")
    for co0, co1 in ((0.0, 0.10), (0.0, 0.20)):
        r0 = load(ai_path(STUDY, "noshuffle", "128", mech, 1, 0, slice_tag="c020"))
        r1 = load(ai_path(STUDY, "noshuffle", "128", mech, 1, 1, slice_tag="c020"))
        q0 = ai_cell(r0, 0.20, co0, co1)
        q1 = ai_cell(r1, 0.20, co0, co1)
        if q0 == q0:
            print(f"    ({co0:.2f},{co1:.2f}): q {q0:.3f}/{q1:.3f} dq={q0 - q1:+.3f}  "
                  f"w {ai_cell(r0, 0.20, co0, co1, 'wmean'):.3f}/"
                  f"{ai_cell(r1, 0.20, co0, co1, 'wmean'):.3f}")

print("\n--- L3. c=0.20 SNOWDRIFT (d=2) ---")
for mech in ("P", "IJMPQ", "M"):
    try:
        dq, dw, gaps = gap_stats(mech, c=0.20, d=2, slice_tag="c020")
        print(f"  {mech}: n={len(dq)}, mean dq={mean(dq):+.3f}, corr(gap,dq)={corr(gaps, dq):.3f}")
    except Exception as e:
        print(f"  {mech}: ERROR {e}")

print("\n--- M. TEMPORAL (1run movies, PD c=0.10) ---")
for mech, co0, co1 in (("P", 0.0, 0.20), ("P", 0.0, 0.10), ("IJMPQ", 0.0, 0.20)):
    print(f"  {mech} at (Cost0,Cost1)=({co0:.2f},{co1:.2f})")
    for f in (0, 1):
        rows = load(ai_path(STUDY1, "noshuffle", "128", mech, 1, f, movie=True))
        if not rows:
            print(f"    pop_{f}: MISSING movie con")
            continue
        pts = sorted(
            (int(float(r["Time"])), float(r["qBSeen"]))
            for r in rows
            if abs(float(r["c0"]) - 0.10) < 0.005
            and abs(float(r["Cost0"]) - co0) < 0.005
            and abs(float(r["Cost1"]) - co1) < 0.005
        )
        if pts:
            show = pts[:2] + pts[-2:]
            print(f"    pop_{f}: " + "  ".join(f"t{t}:{q:.3f}" for t, q in show))

print("\n" + "=" * 78)
print("DONE")
print("=" * 78)
