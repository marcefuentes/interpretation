#!/usr/bin/env python3
"""
Analyze Study B (asymmetric_c1_i0_i1): fixed cooperation-cost gap c0=0.10, c1=0.20
with full Cost0 x Cost1 square (176 valid cells).

Primary condition: pop_2, PD (dilemma 1), noshuffle, gs=128.
"""

import csv
import glob
import os
from statistics import mean

from trps_io import allele, corr, glo, load

BASE = os.path.expanduser("~/results")
STUDY = "asymmetric_c1_i0_i1"
STUDY1 = "asymmetric_c1_i0_i1_1run"
ASYMM = f"{BASE}/asymmetric_c0_c1"
C1I = f"{BASE}/asymmetric_c1_i"
I0I1 = f"{BASE}/asymmetric_i0_i1"

MECHS = ["_", "M", "P", "MP", "MPQ", "IMP", "IJMPQ"]
PRIMARY = ["M", "P", "IMP", "IJMPQ"]
FIXED_C0, FIXED_C1 = 0.10, 0.20


def study_path(study, sh, gs, mech, d, f, movie=False):
    tag = "movie" if movie else "image"
    return f"{BASE}/{study}/{sh}/{gs}/{mech}/{d}/pop_2/csv_{f}_filtered_for_{tag}.con"


def load_square(study, sh, gs, mech, d, f, movie=False):
    """Load from .con cache if present, else aggregate glo+csv pairs."""
    path = study_path(study, sh, gs, mech, d, f, movie=movie)
    rows = load(path)
    if rows:
        return rows
    return load_from_csv(study, sh, gs, mech, d, f, movie=movie)


def load_from_csv(study, sh, gs, mech, d, f, movie=False):
    dpath = f"{BASE}/{study}/{sh}/{gs}/{mech}/{d}/pop_2"
    if not os.path.isdir(dpath):
        return []
    out = []
    for gpath in sorted(glob.glob(f"{dpath}/*.glo")):
        m = glo(gpath)
        if m is None:
            continue
        if abs(float(m.get("c0", -1)) - FIXED_C0) > 0.005:
            continue
        if abs(float(m.get("c1", -1)) - FIXED_C1) > 0.005:
            continue
        co0, co1 = float(m["Cost0"]), float(m["Cost1"])
        if co0 > 0.30 + 0.005 or co1 > 0.20 + 0.005:
            continue
        stem = gpath.replace(".glo", "")
        cp = f"{stem}_{f}.csv"
        if not os.path.exists(cp):
            continue
        with open(cp) as fh:
            rows = list(csv.DictReader(fh))
        if not rows:
            continue
        row = dict(rows[-1] if not movie else rows[0])
        row["Cost0"], row["Cost1"] = str(co0), str(co1)
        row["c0"], row["c1"] = m["c0"], m["c1"]
        out.append(row)
    return out


def cell(rows, co0, co1, col="qBSeen"):
    for r in rows:
        if (abs(float(r["Cost0"]) - co0) < 0.005 and abs(float(r["Cost1"]) - co1) < 0.005):
            return float(r[col])
    return float("nan")


def cell_row(rows, co0, co1):
    for r in rows:
        if (abs(float(r["Cost0"]) - co0) < 0.005 and abs(float(r["Cost1"]) - co1) < 0.005):
            return r
    return None


def square_pairs(r0, r1):
    m1 = {(round(float(r["Cost0"]), 2), round(float(r["Cost1"]), 2)): r for r in r1}
    for r in r0:
        key = (round(float(r["Cost0"]), 2), round(float(r["Cost1"]), 2))
        if key in m1:
            yield r, m1[key]


def gap_stats(mech, sh="noshuffle", gs="128", d=1):
    r0 = load_square(STUDY, sh, gs, mech, d, 0)
    r1 = load_square(STUDY, sh, gs, mech, d, 1)
    dq, dw, cgap, igap = [], [], [], []
    for a, b in square_pairs(r0, r1):
        dq.append(float(a["qBSeen"]) - float(b["qBSeen"]))
        dw.append(float(a["wmean"]) - float(b["wmean"]))
        cgap.append(FIXED_C1 - FIXED_C0)
        igap.append(float(b["Cost1"]) - float(a["Cost0"]))
    return dq, dw, cgap, igap


def asym_c0_c1_cell(rows, c0, c1, col="qBSeen"):
    for r in rows:
        if abs(float(r["c0"]) - c0) < 0.005 and abs(float(r["c1"]) - c1) < 0.005:
            return float(r[col])
    return float("nan")


def c1i_cell(rows, cost, c1, col="qBSeen"):
    for r in rows:
        if abs(float(r["Cost"]) - cost) < 0.005 and abs(float(r["c1"]) - c1) < 0.005:
            return float(r[col])
    return float("nan")


def i0i1_cell(rows, c, co0, co1, col="qBSeen"):
    for r in rows:
        if (abs(float(r["c0"]) - c) < 0.005 and abs(float(r["Cost0"]) - co0) < 0.005
                and abs(float(r["Cost1"]) - co1) < 0.005):
            return float(r[col])
    return float("nan")


print("=" * 78)
print("ASYMMETRIC_C1_I0_I1  (c0=0.10, c1=0.20; Cost0 x Cost1 square)")
print("Primary: pop_2, PD (d1), noshuffle, gs=128.")
print("=" * 78)

r0 = load_square(STUDY, "noshuffle", "128", "IJMPQ", 1, 0)
print(f"\n--- A. GRID ---\n  cells loaded: {len(r0)} (expect 176)")

print("\n--- B. SANITY: (Cost0,Cost1)=(0,0) vs asymmetric_c0_c1 (c0=0.10,c1=0.20) ---")
for mech in MECHS:
    a0 = load_square(STUDY, "noshuffle", "128", mech, 1, 0)
    a1 = load_square(STUDY, "noshuffle", "128", mech, 1, 1)
    b0 = load(f"{ASYMM}/noshuffle/128/{mech}/1/pop_2/csv_0_for_image.con")
    b1 = load(f"{ASYMM}/noshuffle/128/{mech}/1/pop_2/csv_1_for_image.con")
    q0 = cell(a0, 0.0, 0.0)
    q1 = cell(a1, 0.0, 0.0)
    m0 = asym_c0_c1_cell(b0, 0.10, 0.20) if b0 else float("nan")
    m1 = asym_c0_c1_cell(b1, 0.10, 0.20) if b1 else float("nan")
    if q0 == q0:
        print(f"  {mech:6} pop0 {q0:.3f} vs {m0:.3f} ({q0-m0:+.3f})  "
              f"pop1 {q1:.3f} vs {m1:.3f} ({q1-m1:+.3f})")

print("\n--- C. ROLE SPLIT (square means; pop0 - pop1) ---")
for mech in PRIMARY:
    dq, dw, _, igap = gap_stats(mech)
    p0 = sum(1 for x in dq if x > 0.02)
    p1 = sum(1 for x in dq if x < -0.02)
    print(f"  {mech}: mean dq={mean(dq):+.3f}, mean dw={mean(dw):+.3f}, "
          f"corr(i-gap,dq)={corr(igap, dq):.3f}, corr(dq,dw)={corr(dq, dw):.3f}, "
          f"pop0 coops {p0}/{len(dq)}, pop1 coops {p1}/{len(dq)}")

print("\n--- D. SELECTED CELLS ---")
for mech in PRIMARY + ["_"]:
    r0 = load_square(STUDY, "noshuffle", "128", mech, 1, 0)
    r1 = load_square(STUDY, "noshuffle", "128", mech, 1, 1)
    print(f"  {mech}:")
    for co0, co1 in ((0.0, 0.0), (0.0, 0.20), (0.30, 0.0), (0.30, 0.20),
                     (0.10, 0.10), (0.20, 0.20)):
        q0 = cell(r0, co0, co1)
        q1 = cell(r1, co0, co1)
        if q0 == q0:
            print(f"    ({co0:.2f},{co1:.2f}): q {q0:.3f}/{q1:.3f} dq={q0-q1:+.3f}  "
                  f"w {cell(r0, co0, co1, 'wmean'):.3f}/{cell(r1, co0, co1, 'wmean'):.3f}")

print("\n--- E. DIAGONAL Cost0=Cost1 vs parent studies ---")
print("  symmetric-Cost slice (Cost0=Cost1) compared to asymmetric_c1_i at Cost=c, c1=0.20:")
for mech in PRIMARY:
    r0 = load_square(STUDY, "noshuffle", "128", mech, 1, 0)
    r1 = load_square(STUDY, "noshuffle", "128", mech, 1, 1)
    ci0 = load(f"{C1I}/noshuffle/128/{mech}/1/pop_2/csv_0_for_image.con")
    ci1 = load(f"{C1I}/noshuffle/128/{mech}/1/pop_2/csv_1_for_image.con")
    for cost in (0.0, 0.10, 0.20):
        q0 = cell(r0, cost, cost)
        q1 = cell(r1, cost, cost)
        m0 = c1i_cell(ci0, cost, 0.20) if ci0 else float("nan")
        m1 = c1i_cell(ci1, cost, 0.20) if ci1 else float("nan")
        if q0 == q0:
            print(f"    {mech} Cost={cost:.2f}: square {q0:.3f}/{q1:.3f}  "
                  f"c1_i {m0:.3f}/{m1:.3f}")

print("\n--- F. GENOTYPE DECOMPOSITION ---")
for mech, tok in (("P", "P1"), ("M", "M1"), ("IJMPQ", "P1")):
    print(f"  {mech}:")
    for co0, co1 in ((0.0, 0.0), (0.0, 0.20), (0.30, 0.20)):
        for f in (0, 1):
            rows = load_square(STUDY, "noshuffle", "128", mech, 1, f)
            r = cell_row(rows, co0, co1)
            if r:
                free = allele(r, "C1", tok[0] + "0")
                print(f"    pop_{f} ({co0:.2f},{co1:.2f}): q={float(r['qBSeen']):.3f} "
                      f"{tok}={allele(r, tok):.3f} C1{tok[0]}0={free:.3f}")

print("\n--- G. PARADOX / FITNESS ---")
for mech in PRIMARY:
    dq, dw, _, _ = gap_stats(mech)
    inv = sum(1 for x, y in zip(dq, dw) if x * y < 0)
    p0f = sum(1 for x in dw if x > 0.005)
    p1f = sum(1 for x in dw if x < -0.005)
    print(f"  {mech}: inverted {inv}/{len(dq)}, pop0 fitter {p0f}, pop1 fitter {p1f}")

print("\n--- H. COLLAPSE (q0+q1 < 0.15) ---")
for mech in ["P", "M", "IJMPQ", "_"]:
    r0 = load_square(STUDY, "noshuffle", "128", mech, 1, 0)
    r1 = load_square(STUDY, "noshuffle", "128", mech, 1, 1)
    n = sum(1 for a, b in square_pairs(r0, r1) if float(a["qBSeen"]) + float(b["qBSeen"]) < 0.15)
    print(f"  {mech}: {n}/{len(r0)}")

print("\n--- I. SHUFFLE / GS ---")
for sh, gs in [("noshuffle", "128"), ("shuffle", "128"), ("noshuffle", "4")]:
    for mech in ("P", "IJMPQ"):
        dq, dw, _, _ = gap_stats(mech, sh=sh, gs=gs)
        print(f"  {sh} gs{gs} {mech}: mean dq={mean(dq):+.3f}, mean dw={mean(dw):+.3f}")

print("\n--- J. SNOWDRIFT d=2 ---")
for mech in PRIMARY + ["_"]:
    dq, dw, _, igap = gap_stats(mech, d=2)
    p0 = sum(1 for x in dq if x > 0.02)
    p1 = sum(1 for x in dq if x < -0.02)
    print(f"  {mech}: mean dq={mean(dq):+.3f}, pop0>{p0} pop1>{p1}, "
          f"corr(i-gap,dq)={corr(igap, dq):.3f}")

print("\n--- K. TEMPORAL (1run movies, PD) ---")
for mech, co0, co1 in (("P", 0.0, 0.0), ("P", 0.0, 0.20), ("IJMPQ", 0.0, 0.20),
                       ("IJMPQ", 0.30, 0.20)):
    print(f"  {mech} at ({co0:.2f},{co1:.2f})")
    for f in (0, 1):
        rows = load_square(STUDY1, "noshuffle", "128", mech, 1, f, movie=True)
        if not rows:
            print(f"    pop_{f}: MISSING")
            continue
        pts = sorted((int(float(r["Time"])), float(r["qBSeen"])) for r in rows
                     if abs(float(r["Cost0"]) - co0) < 0.005 and abs(float(r["Cost1"]) - co1) < 0.005)
        if pts:
            show = pts[:2] + pts[-2:]
            print(f"    pop_{f}: " + "  ".join(f"t{t}:{q:.3f}" for t, q in show))

print("\n--- L. OVERRIDE TEST: when does IJMPQ flip from c-gap default? ---")
r0 = load_square(STUDY, "noshuffle", "128", "IJMPQ", 1, 0)
r1 = load_square(STUDY, "noshuffle", "128", "IJMPQ", 1, 1)
flip = sum(1 for a, b in square_pairs(r0, r1) if float(a["qBSeen"]) - float(b["qBSeen"]) < -0.02)
stay = sum(1 for a, b in square_pairs(r0, r1) if float(a["qBSeen"]) - float(b["qBSeen"]) > 0.02)
print(f"  IJMPQ pop1 coops more: {flip}/{len(r0)}; pop0 coops more: {stay}/{len(r0)}")
for co0 in (0.0, 0.10, 0.20, 0.30):
    q0 = cell(r0, co0, 0.20)
    q1 = cell(r1, co0, 0.20)
    if q0 == q0:
        print(f"    Cost1=0.20 row, Cost0={co0:.2f}: q {q0:.3f}/{q1:.3f} dq={q0-q1:+.3f}")

print("\n" + "=" * 78)
print("DONE")
print("=" * 78)
