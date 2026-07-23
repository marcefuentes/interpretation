#!/usr/bin/env python3
"""
Analyze Study B (asymmetric_c1_i0_i1): fixed cooperation-cost gap c0=0.10, c1=0.20
with full Cost0 x Cost1 square (176 valid cells).

Both asymmetries are present at once: cooperation cost c0 < c1 **and** independent
per-population information cost (Cost0, Cost1). The central question is whether
information-cost asymmetry can override the cooperation-cost role assignment.

Cost0 in {0.00, 0.02, ..., 0.30}; Cost1 in {0.00, 0.02, ..., 0.20} — each capped
at b - c_p.  pop_2 only.

Primary condition: PD (dilemma 1), noshuffle, gs=128.
"""

import os
from collections import defaultdict
from statistics import mean

from trps_io import allele, corr, load

BASE = os.path.expanduser("~/results")
STUDY = "asymmetric_c1_i0_i1"
STUDY1 = "asymmetric_c1_i0_i1_1run"
ASYMM = f"{BASE}/asymmetric_c0_c1"
C1I = f"{BASE}/asymmetric_c1_i"
I0I1 = f"{BASE}/asymmetric_i0_i1"
SYM_CI = f"{BASE}/symmetric_c_i"

MECHS = ["_", "M", "P", "MP", "MPQ", "IMP", "IJMPQ"]
PRIMARY = ["M", "P", "IMP", "IJMPQ"]
FIXED_C0, FIXED_C1 = 0.10, 0.20
SAMPLE_CO0 = [0.0, 0.04, 0.08, 0.10, 0.14, 0.20, 0.30]
SAMPLE_CO1 = [0.0, 0.04, 0.08, 0.10, 0.14, 0.20]
FAMILIES = {"_": 0, "M": 1, "P": 1, "MP": 2, "MPQ": 2, "IMP": 2, "IJMPQ": 2,
            "IM": 1, "IJM": 1}


def study_path(study, sh, gs, mech, d, f, movie=False):
    tag = "movie" if movie else "image"
    return f"{BASE}/{study}/{sh}/{gs}/{mech}/{d}/pop_2/csv_{f}_filtered_for_{tag}.con"


def load_con(study, sh, gs, mech, d, f, movie=False):
    """Load filtered .con file for a study/condition/fileset."""
    path = study_path(study, sh, gs, mech, d, f, movie=movie)
    rows = load(path)
    return rows if rows else []


def cell(rows, co0, co1, col="qBSeen"):
    for r in rows:
        if (abs(float(r["Cost0"]) - co0) < 0.005
                and abs(float(r["Cost1"]) - co1) < 0.005):
            return float(r[col])
    return float("nan")


def cell_row(rows, co0, co1):
    for r in rows:
        if (abs(float(r["Cost0"]) - co0) < 0.005
                and abs(float(r["Cost1"]) - co1) < 0.005):
            return r
    return None


def square_pairs(r0, r1):
    m1 = {(round(float(r["Cost0"]), 2), round(float(r["Cost1"]), 2)): r for r in r1}
    for r in r0:
        key = (round(float(r["Cost0"]), 2), round(float(r["Cost1"]), 2))
        if key in m1:
            yield r, m1[key]


def gap_stats(mech, sh="noshuffle", gs="128", d=1):
    r0 = load_con(STUDY, sh, gs, mech, d, 0)
    r1 = load_con(STUDY, sh, gs, mech, d, 1)
    dq, dw, igap = [], [], []
    for a, b in square_pairs(r0, r1):
        dq.append(float(a["qBSeen"]) - float(b["qBSeen"]))
        dw.append(float(a["wmean"]) - float(b["wmean"]))
        igap.append(float(b["Cost1"]) - float(a["Cost0"]))
    return dq, dw, igap


def mean_at_co0(rows, co0, col="qBSeen"):
    vals = [float(r[col]) for r in rows if abs(float(r["Cost0"]) - co0) < 0.005]
    return mean(vals) if vals else float("nan")


def mean_at_co1(rows, co1, col="qBSeen"):
    vals = [float(r[col]) for r in rows if abs(float(r["Cost1"]) - co1) < 0.005]
    return mean(vals) if vals else float("nan")


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


# ═══════════════════════════════════════════════════════════════════════
print("=" * 78)
print("ASYMMETRIC_C1_I0_I1  (c0=0.10, c1=0.20; full Cost0 x Cost1 square)")
print("Primary: pop_2, PD (d1), noshuffle, gs=128.")
print("=" * 78)

# ── A. GRID ────────────────────────────────────────────────────────────
r0 = load_con(STUDY, "noshuffle", "128", "IJMPQ", 1, 0)
print(f"\n--- A. GRID ---\n  cells loaded: {len(r0)} (expect 176)")

# ── B. SANITY: (0,0) vs asymmetric_c0_c1 ──────────────────────────────
print("\n--- B. SANITY: (Cost0,Cost1)=(0,0) vs asymmetric_c0_c1 (c0=0.10,c1=0.20) ---")
for mech in MECHS:
    a0 = load_con(STUDY, "noshuffle", "128", mech, 1, 0)
    a1 = load_con(STUDY, "noshuffle", "128", mech, 1, 1)
    b0 = load(f"{ASYMM}/noshuffle/128/{mech}/1/pop_2/csv_0_for_image.con")
    b1 = load(f"{ASYMM}/noshuffle/128/{mech}/1/pop_2/csv_1_for_image.con")
    q0 = cell(a0, 0.0, 0.0)
    q1 = cell(a1, 0.0, 0.0)
    m0 = asym_c0_c1_cell(b0, 0.10, 0.20) if b0 else float("nan")
    m1 = asym_c0_c1_cell(b1, 0.10, 0.20) if b1 else float("nan")
    if q0 == q0:
        print(f"  {mech:6} pop0 {q0:.3f} vs {m0:.3f} ({q0-m0:+.3f})  "
              f"pop1 {q1:.3f} vs {m1:.3f} ({q1-m1:+.3f})")

# ── C. ROLE SPLIT (square-wide means; pop0 - pop1) ────────────────────
print("\n--- C. ROLE SPLIT (square means; pop0 - pop1) ---")
for mech in PRIMARY:
    dq, dw, igap = gap_stats(mech)
    p0 = sum(1 for x in dq if x > 0.02)
    p1 = sum(1 for x in dq if x < -0.02)
    print(f"  {mech}: mean dq={mean(dq):+.3f}, mean dw={mean(dw):+.3f}, "
          f"corr(i-gap,dq)={corr(igap, dq):.3f}, corr(dq,dw)={corr(dq, dw):.3f}, "
          f"pop0 coops {p0}/{len(dq)}, pop1 coops {p1}/{len(dq)}")

# ── C2. INFO-GAP REGRESSION ──────────────────────────────────────────
print("\n--- C2. INFO-GAP SENSITIVITY (c-gap fixed at 0.10; i-gap = Cost1-Cost0) ---")
print("c-gap is constant so the only varying predictor of dq is the info gap.")
for mech in PRIMARY:
    r0 = load_con(STUDY, "noshuffle", "128", mech, 1, 0)
    r1 = load_con(STUDY, "noshuffle", "128", mech, 1, 1)
    dqs, dws, igaps = [], [], []
    for a, b in square_pairs(r0, r1):
        dqs.append(float(a["qBSeen"]) - float(b["qBSeen"]))
        dws.append(float(a["wmean"]) - float(b["wmean"]))
        igaps.append(float(b["Cost1"]) - float(a["Cost0"]))
    r_dq = corr(igaps, dqs)
    r_dw = corr(igaps, dws)
    print(f"  {mech}: corr(igap,dq)={r_dq:.3f}, corr(igap,dw)={r_dw:.3f}, "
          f"n={len(dqs)}")

# ── D. SELECTED CELLS ─────────────────────────────────────────────────
print("\n--- D. SELECTED CELLS ---")
for mech in PRIMARY + ["_"]:
    r0 = load_con(STUDY, "noshuffle", "128", mech, 1, 0)
    r1 = load_con(STUDY, "noshuffle", "128", mech, 1, 1)
    print(f"  {mech}:")
    for co0, co1 in ((0.0, 0.0), (0.0, 0.10), (0.0, 0.20), (0.10, 0.10),
                     (0.20, 0.0), (0.20, 0.20), (0.30, 0.0), (0.30, 0.20)):
        q0 = cell(r0, co0, co1)
        q1 = cell(r1, co0, co1)
        if q0 == q0:
            w0 = cell(r0, co0, co1, "wmean")
            w1 = cell(r1, co0, co1, "wmean")
            print(f"    ({co0:.2f},{co1:.2f}): q {q0:.3f}/{q1:.3f} dq={q0-q1:+.3f}  "
                  f"w {w0:.3f}/{w1:.3f} dw={w0-w1:+.3f}")

# ── E. DIAGONAL Cost0=Cost1 vs parent studies ─────────────────────────
print("\n--- E. DIAGONAL Cost0=Cost1 vs asymmetric_c1_i at Cost=c, c1=0.20 ---")
for mech in PRIMARY:
    r0 = load_con(STUDY, "noshuffle", "128", mech, 1, 0)
    r1 = load_con(STUDY, "noshuffle", "128", mech, 1, 1)
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

# ── E2. CROSS-STUDY: same (Cost0, Cost1) point in Study A ────────────
print("\n--- E2. vs asymmetric_i0_i1 (Study A) at same (Cost0, Cost1) point ---")
print("Study A has c0=c1=0.10 (symmetric c); Study B has c0=0.10, c1=0.20.")
for mech in PRIMARY:
    for co0, co1 in ((0.0, 0.20), (0.0, 0.10), (0.10, 0.20)):
        r0b = load_con(STUDY, "noshuffle", "128", mech, 1, 0)
        r1b = load_con(STUDY, "noshuffle", "128", mech, 1, 1)
        q0b = cell(r0b, co0, co1)
        q1b = cell(r1b, co0, co1)
        a0 = load(f"{I0I1}/noshuffle/128/{mech}/1/pop_2/csv_0_filtered_for_image.con")
        a1 = load(f"{I0I1}/noshuffle/128/{mech}/1/pop_2/csv_1_filtered_for_image.con")
        q0a = i0i1_cell(a0, 0.10, co0, co1) if a0 else float("nan")
        q1a = i0i1_cell(a1, 0.10, co0, co1) if a1 else float("nan")
        if q0b == q0b:
            print(f"  {mech} ({co0:.2f},{co1:.2f}): A {q0a:.3f}/{q1a:.3f} dq={q0a-q1a:+.3f}  "
                  f"B {q0b:.3f}/{q1b:.3f} dq={q0b-q1b:+.3f}")

# ── F. DOSE-RESPONSE STRIPS ──────────────────────────────────────────
print("\n--- F. DOSE-RESPONSE: IJMPQ at Cost0=0, sweeping Cost1 ---")
r0 = load_con(STUDY, "noshuffle", "128", "IJMPQ", 1, 0)
r1 = load_con(STUDY, "noshuffle", "128", "IJMPQ", 1, 1)
for co1 in [0.0, 0.02, 0.04, 0.08, 0.10, 0.14, 0.20]:
    q0 = cell(r0, 0.0, co1)
    q1 = cell(r1, 0.0, co1)
    w0 = cell(r0, 0.0, co1, "wmean")
    w1 = cell(r1, 0.0, co1, "wmean")
    if q0 == q0:
        print(f"  Cost1={co1:.2f}: q {q0:.3f}/{q1:.3f} dq={q0-q1:+.3f} "
              f"dw={w0-w1:+.3f}")

print("\n  DOSE-RESPONSE: P at Cost0=0, sweeping Cost1 ---")
r0 = load_con(STUDY, "noshuffle", "128", "P", 1, 0)
r1 = load_con(STUDY, "noshuffle", "128", "P", 1, 1)
for co1 in [0.0, 0.04, 0.08, 0.10, 0.14, 0.20]:
    q0 = cell(r0, 0.0, co1)
    q1 = cell(r1, 0.0, co1)
    if q0 == q0:
        print(f"  Cost1={co1:.2f}: q {q0:.3f}/{q1:.3f} dq={q0-q1:+.3f}")

print("\n  DOSE-RESPONSE: IJMPQ at Cost1=0, sweeping Cost0 ---")
r0 = load_con(STUDY, "noshuffle", "128", "IJMPQ", 1, 0)
r1 = load_con(STUDY, "noshuffle", "128", "IJMPQ", 1, 1)
for co0 in [0.0, 0.04, 0.08, 0.10, 0.14, 0.20, 0.30]:
    q0 = cell(r0, co0, 0.0)
    q1 = cell(r1, co0, 0.0)
    if q0 == q0:
        print(f"  Cost0={co0:.2f}: q {q0:.3f}/{q1:.3f} dq={q0-q1:+.3f}")

# ── F2. MEAN COOPERATION BY Cost0 ROW (PD, ns, gs128) ────────────────
print("\n--- F2. MEAN COOPERATION BY Cost0 ROW (all c1-columns averaged) ---")
for mech in MECHS:
    r0 = load_con(STUDY, "noshuffle", "128", mech, 1, 0)
    r1 = load_con(STUDY, "noshuffle", "128", mech, 1, 1)
    if not r0:
        continue
    line = f"  {mech:6}"
    for co0 in [0.0, 0.04, 0.10, 0.20, 0.30]:
        a0 = mean_at_co0(r0, co0)
        a1 = mean_at_co0(r1, co0)
        if a0 == a0:
            line += f"  C0={co0:.2f}:{a0:.3f}/{a1:.3f}"
    print(line)

# ── G. GENOTYPE DECOMPOSITION ─────────────────────────────────────────
print("\n--- G. GENOTYPE DECOMPOSITION ---")
for mech, tok in (("P", "P1"), ("M", "M1"), ("IJMPQ", "P1"), ("IJMPQ", "M1")):
    print(f"  {mech} ({tok}):")
    for co0, co1 in ((0.0, 0.0), (0.0, 0.20), (0.20, 0.0), (0.30, 0.0),
                     (0.10, 0.10), (0.30, 0.20)):
        for f in (0, 1):
            rows = load_con(STUDY, "noshuffle", "128", mech, 1, f)
            r = cell_row(rows, co0, co1)
            if r:
                free = allele(r, "C1", tok[0] + "0")
                c0geno = allele(r, "C0")
                print(f"    pop_{f} ({co0:.2f},{co1:.2f}): q={float(r['qBSeen']):.3f} "
                      f"{tok}={allele(r, tok):.3f} C1{tok[0]}0={free:.3f} C0={c0geno:.3f}")

# ── G2. MACHINERY EROSION: P1 and M1 across Cost0 at fixed Cost1=0 ───
print("\n--- G2. MACHINERY EROSION vs Cost0 (Cost1=0, PD, ns, gs128) ---")
print("P mech:")
r = load_con(STUDY, "noshuffle", "128", "P", 1, 0)
print(f"  {'Cost0':>6}  {'pop_0 qB':>8}  {'P1':>7}  {'C1P1':>7}  {'C1P0':>7}  {'C0':>7}")
for co0 in SAMPLE_CO0:
    row = cell_row(r, co0, 0.0)
    if row:
        print(f"  {co0:>4.2f}  {float(row['qBSeen']):>8.3f}  "
              f"{allele(row, 'P1'):>7.3f}  {allele(row, 'C1', 'P1'):>7.3f}  "
              f"{allele(row, 'C1', 'P0'):>7.3f}  {allele(row, 'C0'):>7.3f}")

print("M mech:")
r = load_con(STUDY, "noshuffle", "128", "M", 1, 0)
print(f"  {'Cost0':>6}  {'pop_0 qB':>8}  {'M1':>7}  {'C1M1':>7}  {'C1M0':>7}  {'C0':>7}")
for co0 in SAMPLE_CO0:
    row = cell_row(r, co0, 0.0)
    if row:
        print(f"  {co0:>4.2f}  {float(row['qBSeen']):>8.3f}  "
              f"{allele(row, 'M1'):>7.3f}  {allele(row, 'C1', 'M1'):>7.3f}  "
              f"{allele(row, 'C1', 'M0'):>7.3f}  {allele(row, 'C0'):>7.3f}")

# ── H. PARADOX OF SUCCESS (dq * dw < 0) ──────────────────────────────
print("\n--- H. PARADOX OF SUCCESS (dq*dw < 0) ---")
for mech in PRIMARY:
    dq, dw, _ = gap_stats(mech)
    inv = sum(1 for x, y in zip(dq, dw) if x * y < 0)
    print(f"  {mech}: inverted {inv}/{len(dq)}")

# ── H2. FITNESS DOMINANCE ────────────────────────────────────────────
print("\n--- H2. FITNESS DOMINANCE ---")
for mech in PRIMARY:
    dq, dw, _ = gap_stats(mech)
    p0 = sum(1 for x in dw if x > 0.005)
    p1 = sum(1 for x in dw if x < -0.005)
    print(f"  {mech}: pop0 fitter {p0}/{len(dw)}, pop1 fitter {p1}/{len(dw)}")

# ── I. COLLAPSE (q0+q1 < 0.15) ───────────────────────────────────────
print("\n--- I. COLLAPSE (q0+q1 < 0.15) ---")
for mech in ["P", "M", "IJMPQ", "IMP", "MP", "_"]:
    r0 = load_con(STUDY, "noshuffle", "128", mech, 1, 0)
    r1 = load_con(STUDY, "noshuffle", "128", mech, 1, 1)
    if not r0:
        print(f"  {mech}: MISSING")
        continue
    n = sum(1 for a, b in square_pairs(r0, r1)
            if float(a["qBSeen"]) + float(b["qBSeen"]) < 0.15)
    print(f"  {mech}: {n}/{len(r0)}")

# ── J. ISO-BUDGET ANALYSIS ───────────────────────────────────────────
print("\n--- J. ISO-BUDGET: cooperation along constant Cost0+Cost1 lines ---")
print("If info costs are fungible, cells with equal budget should have equal qB.")
COSTS = [round(0.02 * i, 2) for i in range(21)]
for mech in ["IJMPQ", "P", "M"]:
    r0 = load_con(STUDY, "noshuffle", "128", mech, 1, 0)
    r1 = load_con(STUDY, "noshuffle", "128", mech, 1, 1)
    if not r0:
        continue
    print(f"  {mech}:")
    for budget in [0.0, 0.10, 0.20, 0.30, 0.40]:
        pts = []
        for co0 in COSTS:
            co1 = round(budget - co0, 2)
            if co1 < -0.005 or co0 > 0.30 + 0.005 or co1 > 0.20 + 0.005:
                continue
            q0 = cell(r0, co0, co1)
            q1 = cell(r1, co0, co1)
            if q0 == q0:
                pts.append((co0, co1, q0, q1))
        if len(pts) >= 2:
            qs0 = [p[2] for p in pts]
            qs1 = [p[3] for p in pts]
            span0 = max(qs0) - min(qs0)
            span1 = max(qs1) - min(qs1)
            ends = (f"({pts[0][0]:.2f},{pts[0][1]:.2f})={pts[0][2]:.3f}/{pts[0][3]:.3f} .. "
                    f"({pts[-1][0]:.2f},{pts[-1][1]:.2f})={pts[-1][2]:.3f}/{pts[-1][3]:.3f}")
            print(f"    C0+C1={budget:.2f}: pop0 span={span0:.3f}, pop1 span={span1:.3f}  {ends}")

# ── K. MECHANISM RANKING REVERSALS ───────────────────────────────────
print("\n--- K. MECHANISM RANKING at low vs high info cost (PD, ns, gs128) ---")
corners = [(0.0, 0.0), (0.0, 0.20), (0.30, 0.0), (0.30, 0.20), (0.10, 0.10)]
for co0, co1 in corners:
    ranking = []
    for mech in MECHS:
        r0 = load_con(STUDY, "noshuffle", "128", mech, 1, 0)
        r1 = load_con(STUDY, "noshuffle", "128", mech, 1, 1)
        if not r0:
            continue
        q0 = cell(r0, co0, co1)
        q1 = cell(r1, co0, co1)
        if q0 == q0:
            ranking.append(((q0 + q1) / 2, mech, q0, q1))
    ranking.sort(reverse=True)
    top = ", ".join(f"{m}={v:.3f}" for v, m, _, _ in ranking[:4])
    print(f"  ({co0:.2f},{co1:.2f}): {top}")

# ── L. DILEMMA 0 CONTROL DECOMPOSITION ───────────────────────────────
print("\n--- L. DILEMMA 0 (CONTROL) vs PD: supply-side erosion ---")
print("d0 has no social dilemma; M1 erosion measures pure information-cost tax.")
for d_label, d in [("d0 (ctrl)", 0), ("d1 (PD)", 1)]:
    r0 = load_con(STUDY, "noshuffle", "128", "M", d, 0)
    r1 = load_con(STUDY, "noshuffle", "128", "M", d, 1)
    if not r0:
        print(f"  M {d_label}: MISSING")
        continue
    print(f"  M {d_label}:")
    for co0, co1 in ((0.0, 0.0), (0.10, 0.0), (0.20, 0.0), (0.30, 0.0),
                     (0.0, 0.20)):
        row0 = cell_row(r0, co0, co1)
        row1 = cell_row(r1, co0, co1)
        if row0 and row1:
            print(f"    ({co0:.2f},{co1:.2f}): "
                  f"pop0 q={float(row0['qBSeen']):.3f} M1={allele(row0,'M1'):.3f} C1M0={allele(row0,'C1','M0'):.3f}  "
                  f"pop1 q={float(row1['qBSeen']):.3f} M1={allele(row1,'M1'):.3f} C1M0={allele(row1,'C1','M0'):.3f}")

print("\n  _ (control mechanism) across d0, d1, d2:")
for d in (0, 1, 2):
    r0 = load_con(STUDY, "noshuffle", "128", "_", d, 0)
    r1 = load_con(STUDY, "noshuffle", "128", "_", d, 1)
    if not r0:
        print(f"    d{d}: MISSING")
        continue
    for co0, co1 in ((0.0, 0.0), (0.20, 0.0), (0.0, 0.20)):
        q0 = cell(r0, co0, co1)
        q1 = cell(r1, co0, co1)
        if q0 == q0:
            print(f"    d{d} ({co0:.2f},{co1:.2f}): q {q0:.3f}/{q1:.3f}")

# ── M. SHUFFLE / GS ─────────────────────────────────────────────────
print("\n--- M. SHUFFLE / GS ---")
for sh, gs in [("noshuffle", "128"), ("shuffle", "128"), ("noshuffle", "4"),
               ("shuffle", "4")]:
    for mech in ("P", "IJMPQ", "M"):
        dq, dw, _ = gap_stats(mech, sh=sh, gs=gs)
        if not dq:
            print(f"  {sh} gs{gs} {mech}: MISSING")
            continue
        print(f"  {sh} gs{gs} {mech}: mean dq={mean(dq):+.3f}, mean dw={mean(dw):+.3f}, "
              f"n={len(dq)}")

# ── M2. SHUFFLE-ONLY MECHANISMS (IM, IJM) ────────────────────────────
print("\n--- M2. SHUFFLE-ONLY MECHANISMS (IM, IJM; gs128 d1) ---")
for mech in ("IM", "IJM"):
    dq, dw, _ = gap_stats(mech, sh="shuffle", gs="128")
    if not dq:
        print(f"  {mech}: MISSING")
        continue
    p0 = sum(1 for x in dq if x > 0.02)
    p1 = sum(1 for x in dq if x < -0.02)
    print(f"  {mech}: mean dq={mean(dq):+.3f}, pop0 coops {p0}/{len(dq)}, "
          f"pop1 coops {p1}/{len(dq)}")

# ── N. SNOWDRIFT d=2 ─────────────────────────────────────────────────
print("\n--- N. SNOWDRIFT d=2 (triangle summary) ---")
for mech in PRIMARY + ["_"]:
    dq, dw, igap = gap_stats(mech, d=2)
    if not dq:
        print(f"  {mech}: MISSING")
        continue
    p0 = sum(1 for x in dq if x > 0.02)
    p1 = sum(1 for x in dq if x < -0.02)
    tie = len(dq) - p0 - p1
    print(f"  {mech}: mean dq={mean(dq):+.3f}, pop0>{p0} pop1>{p1} tie={tie}, "
          f"corr(igap,dq)={corr(igap, dq):.3f}, corr(dq,dw)={corr(dq, dw):.3f}")

# ── N2. SNOWDRIFT vs PD SELECTED CELLS ───────────────────────────────
print("\n--- N2. SNOWDRIFT vs PD selected cells ---")
for mech in ("P", "IJMPQ", "IMP"):
    print(f"  {mech}:")
    for d, name in ((1, "PD"), (2, "SD")):
        r0 = load_con(STUDY, "noshuffle", "128", mech, d, 0)
        r1 = load_con(STUDY, "noshuffle", "128", mech, d, 1)
        if not r0:
            print(f"    {name}: MISSING")
            continue
        for co0, co1 in ((0.0, 0.0), (0.0, 0.20), (0.30, 0.0), (0.30, 0.20)):
            q0 = cell(r0, co0, co1)
            q1 = cell(r1, co0, co1)
            if q0 == q0:
                print(f"    {name} ({co0:.2f},{co1:.2f}): q {q0:.3f}/{q1:.3f} dq={q0-q1:+.3f}")

# ── N3. SNOWDRIFT Cost0-ROW SIGN FLIPS ───────────────────────────────
print("\n--- N3. SNOWDRIFT Cost0-row sign flips (does the inversion survive?) ---")
for mech in ("P", "IJMPQ"):
    r0 = load_con(STUDY, "noshuffle", "128", mech, 2, 0)
    r1 = load_con(STUDY, "noshuffle", "128", mech, 2, 1)
    if not r0 or not r1:
        print(f"  {mech}: MISSING")
        continue
    by_c0 = defaultdict(list)
    for a, b in square_pairs(r0, r1):
        co0 = round(float(a["Cost0"]), 2)
        dq = float(a["qBSeen"]) - float(b["qBSeen"])
        by_c0[co0].append(dq)
    mixed = sum(1 for dqs in by_c0.values()
                if any(x > 0.02 for x in dqs) and any(x < -0.02 for x in dqs))
    print(f"  {mech}: Cost0-rows with both dq signs: {mixed}/{len(by_c0)}")

# ── O. OVERRIDE TEST: when does IJMPQ/IMP flip from c-gap default? ──
print("\n--- O. OVERRIDE TEST: IJMPQ pop1-cooperates-more cells ---")
for mech in ("IJMPQ", "IMP"):
    r0 = load_con(STUDY, "noshuffle", "128", mech, 1, 0)
    r1 = load_con(STUDY, "noshuffle", "128", mech, 1, 1)
    if not r0:
        print(f"  {mech}: MISSING")
        continue
    flip = sum(1 for a, b in square_pairs(r0, r1)
               if float(a["qBSeen"]) - float(b["qBSeen"]) < -0.02)
    stay = sum(1 for a, b in square_pairs(r0, r1)
               if float(a["qBSeen"]) - float(b["qBSeen"]) > 0.02)
    print(f"  {mech}: pop1 coops more: {flip}/{len(r0)}; pop0 coops more: {stay}/{len(r0)}")
    # Show the geography of flips
    flip_cells = [(round(float(a["Cost0"]), 2), round(float(b["Cost1"]), 2),
                   float(a["qBSeen"]) - float(b["qBSeen"]))
                  for a, b in square_pairs(r0, r1)
                  if float(a["qBSeen"]) - float(b["qBSeen"]) < -0.02]
    if flip_cells:
        co0_range = sorted(set(c[0] for c in flip_cells))
        co1_range = sorted(set(c[1] for c in flip_cells))
        print(f"    Flip Cost0 range: {co0_range}")
        print(f"    Flip Cost1 range: {co1_range}")
    # Dose-response along Cost1=0.20 row
    print(f"    Cost1=0.20 row:")
    for co0 in [0.0, 0.02, 0.04, 0.10, 0.20, 0.30]:
        q0 = cell(r0, co0, 0.20)
        q1 = cell(r1, co0, 0.20)
        if q0 == q0:
            print(f"      Cost0={co0:.2f}: q {q0:.3f}/{q1:.3f} dq={q0-q1:+.3f}")

# ── P. COST0 x COST1 LANDSCAPE (IJMPQ) ──────────────────────────────
print("\n--- P. COST0 x COST1 LANDSCAPE: pop0 qBSeen (IJMPQ, PD, ns, gs128) ---")
print("rows = Cost0, cols = Cost1. blank = outside grid.")
r0 = load_con(STUDY, "noshuffle", "128", "IJMPQ", 1, 0)
if r0:
    print("C0\\C1 " + "".join(f"{c1:>7.2f}" for c1 in SAMPLE_CO1))
    for co0 in SAMPLE_CO0:
        line = f"{co0:>5.2f} "
        for co1 in SAMPLE_CO1:
            q = cell(r0, co0, co1)
            line += f"{q:>7.3f}" if q == q else f"{'':>7}"
        print(line)

print("\n  pop1 qBSeen:")
r1 = load_con(STUDY, "noshuffle", "128", "IJMPQ", 1, 1)
if r1:
    print("C0\\C1 " + "".join(f"{c1:>7.2f}" for c1 in SAMPLE_CO1))
    for co0 in SAMPLE_CO0:
        line = f"{co0:>5.2f} "
        for co1 in SAMPLE_CO1:
            q = cell(r1, co0, co1)
            line += f"{q:>7.3f}" if q == q else f"{'':>7}"
        print(line)

print("\n  dq = pop0 - pop1:")
if r0 and r1:
    print("C0\\C1 " + "".join(f"{c1:>7.2f}" for c1 in SAMPLE_CO1))
    for co0 in SAMPLE_CO0:
        line = f"{co0:>5.2f} "
        for co1 in SAMPLE_CO1:
            q0 = cell(r0, co0, co1)
            q1 = cell(r1, co0, co1)
            dq = q0 - q1 if q0 == q0 and q1 == q1 else float("nan")
            line += f"{dq:>+7.3f}" if dq == dq else f"{'':>7}"
        print(line)

# ── Q. TEMPORAL (1run movies, PD) ────────────────────────────────────
print("\n--- Q. TEMPORAL (1run movies, PD, ns, gs128) ---")
for mech, co0, co1 in (("P", 0.0, 0.0), ("P", 0.0, 0.20), ("P", 0.30, 0.0),
                       ("IJMPQ", 0.0, 0.0), ("IJMPQ", 0.0, 0.20),
                       ("IJMPQ", 0.30, 0.0), ("IJMPQ", 0.30, 0.20),
                       ("M", 0.0, 0.0), ("M", 0.0, 0.20)):
    print(f"  {mech} at ({co0:.2f},{co1:.2f})")
    for f in (0, 1):
        rows = load_con(STUDY1, "noshuffle", "128", mech, 1, f, movie=True)
        if not rows:
            print(f"    pop_{f}: MISSING")
            continue
        pts = sorted(
            (int(float(r["Time"])), float(r["qBSeen"]))
            for r in rows
            if abs(float(r["Cost0"]) - co0) < 0.005
            and abs(float(r["Cost1"]) - co1) < 0.005
        )
        if pts:
            show = pts[:2] + pts[-2:]
            print(f"    pop_{f}: " + "  ".join(f"t{t}:{q:.3f}" for t, q in show))
        else:
            print(f"    pop_{f}: no matching rows")

# ── R. SHUFFLE WASTE (M, PD, gs128) ─────────────────────────────────
print("\n--- R. SHUFFLE WASTE (M: noshuffle vs shuffle, PD, gs128) ---")
print("Under shuffle, M1 is behaviourally inactive but carriers still pay Cost.")
for co0, co1 in ((0.0, 0.0), (0.10, 0.0), (0.20, 0.0), (0.0, 0.20)):
    rns0 = load_con(STUDY, "noshuffle", "128", "M", 1, 0)
    rsh0 = load_con(STUDY, "shuffle", "128", "M", 1, 0)
    rc0 = load_con(STUDY, "noshuffle", "128", "_", 1, 0)
    qns = cell(rns0, co0, co1) if rns0 else float("nan")
    qsh = cell(rsh0, co0, co1) if rsh0 else float("nan")
    qc = cell(rc0, co0, co1) if rc0 else float("nan")
    print(f"  ({co0:.2f},{co1:.2f}): M noshuffle={qns:.3f}  M shuffle={qsh:.3f}  _={qc:.3f}")

print("\n" + "=" * 78)
print("DONE")
print("=" * 78)
