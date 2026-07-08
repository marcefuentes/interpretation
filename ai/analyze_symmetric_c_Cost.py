#!/usr/bin/env python3
"""
Analyze the symmetric_c_Cost study: how cooperation depends on the *information
cost* of carrying reciprocity / partner-choice machinery.

Standard diagonal fixes the per-round module tax at Cost = 0.001 (negligible)
and sweeps the cooperation cost c in [0, 0.4]. symmetric_c_Cost adds a second axis:
Cost (the "information cost" of a module family) is swept jointly with c over a
triangular grid constrained to Cost + c <= 0.4 (= b). 231 cells:
Cost in {0, 0.02, ..., 0.4}; for each Cost, c in {0, 0.02, ..., 0.4 - Cost}.

Model hook (trps recruits.c):
    ind->cost = Cost * ((Choose || Choose_lt) + (Mimic || Imimic || Imimic_lt))
so an individual pays Cost once for carrying ANY partner-choice locus (P/Q) and
once for carrying ANY reciprocity locus (M/I/J). Combined mechanisms that touch
both families (MP, MPQ, IMP, IJMPQ) therefore pay 2 x Cost per round; single
family mechanisms (M, P) pay 1 x Cost; the control (_) pays 0. Fitness is
w = max(0, payoff - cost) each round.

Primary condition: pop_1, PD (dilemma 1), noshuffle, gs=128, fset 0.
Cell key is (Cost, c) with c = c0 = c1 (the diagonal).
"""

import os
from collections import defaultdict

from trps_io import allele, load  # noqa: F401

HC = os.path.expanduser("~/results/symmetric_c_Cost")
HAM = os.path.expanduser("~/results/symmetric_c")

# families touched by each mechanism -> per-round tax multiplier
FAMILIES = {"_": 0, "M": 1, "P": 1, "MP": 2, "MPQ": 2, "IMP": 2, "IJMPQ": 2,
            "IM": 1, "IJM": 1}
MECHS = ["_", "M", "P", "MP", "MPQ", "IMP", "IJMPQ"]


def hc_path(sh, gs, mech, d, pop, f):
    return f"{HC}/{sh}/{gs}/{mech}/{d}/{pop}/csv_{f}_for_image.con"


def ham_path(sh, gs, mech, d, pop, f):
    return f"{HAM}/{sh}/{gs}/{mech}/{d}/{pop}/csv_{f}_for_image.con"


def grid(sh, gs, mech, d, pop, f):
    """Return {(Cost, c): row} keyed by rounded (Cost, c0)."""
    rows = load(hc_path(sh, gs, mech, d, pop, f))
    if rows is None:
        return None
    return {(round(float(r["Cost"]), 3), round(float(r["c0"]), 3)): r for r in rows}


def q(row):
    return float(row["qBSeen"]) if row else float("nan")


COSTS = [round(0.02 * i, 3) for i in range(21)]
CS = [round(0.02 * i, 3) for i in range(21)]
SAMPLE_COST = [0.0, 0.04, 0.08, 0.12, 0.2, 0.3, 0.4]
SAMPLE_C = [0.0, 0.04, 0.08, 0.16, 0.24, 0.32, 0.4]


def cell(g, cost, c):
    return g.get((round(cost, 3), round(c, 3)))


print("=" * 78)
print("SYMMETRIC_COST  (K=0.5, b=0.4; triangular Cost x c grid, Cost + c <= 0.4)")
print("Primary: pop_1, PD (d1), noshuffle, gs=128, fset0.  cell=(Cost,c).")
print("=" * 78)

# ── A. sanity: Cost=0 column reproduces standard diagonal (Cost=0.001) ────────
print("\n--- A. SANITY: symmetric_c_Cost Cost=0 slice vs standard diagonal (Cost=0.001) ---")
print("qBSeen along c (pop_1, PD, noshuffle, gs=128, fset0)")
print(f"{'mech':6}{'c':>6}  {'HC Cost=0':>10}  {'diagonal':>9}  {'diff':>7}")
for mech in MECHS:
    d = 1
    g = grid("noshuffle", "128", mech, d, "pop_1", 0)
    hrows = load(ham_path("noshuffle", "128", mech, d, "pop_1", 0))
    if g is None or hrows is None:
        print(f"  {mech}: missing"); continue
    hmap = {round(float(r["c0"]), 3): float(r["qBSeen"]) for r in hrows}
    for c in [0.0, 0.1, 0.2, 0.4]:
        hc = cell(g, 0.0, c)
        hv = hmap.get(round(c, 3))
        if hc and hv is not None:
            print(f"  {mech:6}{c:>6.2f}  {q(hc):>10.3f}  {hv:>9.3f}  {q(hc)-hv:>+7.3f}")

# ── B. pure information-cost collapse at c=0 ─────────────────────────────────
print("\n--- B. PURE INFORMATION-COST COLLAPSE (c=0: no cooperation cost) ---")
print("qBSeen vs Cost, pop_1 PD noshuffle gs128 fset0. c=0 so only the module tax bites.")
hdr = f"{'mech':6}{'fam':>4}" + "".join(f"{co:>7.2f}" for co in SAMPLE_COST)
print(hdr)
for mech in MECHS:
    g = grid("noshuffle", "128", mech, 1, "pop_1", 0)
    if g is None:
        continue
    vals = []
    for co in SAMPLE_COST:
        r = cell(g, co, 0.0)
        vals.append(f"{q(r):>7.3f}" if r else f"{'--':>7}")
    print(f"  {mech:6}{FAMILIES[mech]:>4}" + "".join(vals))

# ── C. does the tax act through families x Cost? ─────────────────────────────
print("\n--- C. FAMILY-SCALING: double-family qB(Cost) vs single-family qB(2*Cost) ---")
print("If the module tax drives the collapse, a 2-family mech at Cost=X should")
print("resemble a 1-family mech at Cost=2X (same per-round burden). c=0, pop_1 PD ns gs128.")
print(f"{'Cost':>6}  {'P(1fam)@2C':>11}  {'M(1fam)@2C':>11}  {'MP(2fam)@C':>11}  {'IMP(2fam)@C':>12}  {'IJMPQ@C':>9}")
gP = grid("noshuffle", "128", "P", 1, "pop_1", 0)
gM = grid("noshuffle", "128", "M", 1, "pop_1", 0)
gMP = grid("noshuffle", "128", "MP", 1, "pop_1", 0)
gIMP = grid("noshuffle", "128", "IMP", 1, "pop_1", 0)
gIJ = grid("noshuffle", "128", "IJMPQ", 1, "pop_1", 0)
for co in [0.0, 0.04, 0.08, 0.12, 0.16, 0.2]:
    two = round(2 * co, 3)
    def g2(g, cost):
        r = cell(g, cost, 0.0)
        return f"{q(r):.3f}" if r else "  --"
    print(f"  {co:>4.2f}  {g2(gP, two):>11}  {g2(gM, two):>11}  {g2(gMP, co):>11}  {g2(gIMP, co):>12}  {g2(gIJ, co):>9}")

# ── D. Cost x c interaction: separable or a joint budget? ────────────────────
print("\n--- D. COST x c LANDSCAPE (IJMPQ, pop_1 PD noshuffle gs128 fset0) ---")
print("rows = Cost (information), cols = c (cooperation). blank = outside triangle.")
g = grid("noshuffle", "128", "IJMPQ", 1, "pop_1", 0)
print("Cost\\c " + "".join(f"{c:>6.2f}" for c in SAMPLE_C))
for co in SAMPLE_COST:
    line = f"{co:>5.2f} "
    for c in SAMPLE_C:
        r = cell(g, co, c)
        line += f"{q(r):>6.3f}" if r else f"{'':>6}"
    print(line)

print("\n--- D2. iso-budget test: cells with equal Cost+c, IJMPQ & MP (pop_1 PD ns gs128) ---")
for mech in ["MP", "IMP", "IJMPQ"]:
    g = grid("noshuffle", "128", mech, 1, "pop_1", 0)
    if g is None:
        continue
    print(f"  {mech}:")
    for budget in [0.2, 0.4]:
        pts = []
        for co in COSTS:
            c = round(budget - co, 3)
            if c < 0 or c > 0.4:
                continue
            r = cell(g, co, c)
            if r:
                pts.append((co, c, q(r)))
        if pts:
            qs = [p[2] for p in pts]
            span = max(qs) - min(qs)
            ends = f"(Cost={pts[0][0]:.2f},c={pts[0][1]:.2f})={pts[0][2]:.3f} .. (Cost={pts[-1][0]:.2f},c={pts[-1][1]:.2f})={pts[-1][2]:.3f}"
            print(f"    Cost+c={budget:.1f}: qB span={span:.3f}  {ends}")

# ── E. mechanism ranking reversal: low Cost vs high Cost ─────────────────────
print("\n--- E. RANKING REVERSAL: best mechanism at low vs high Cost (c=0, pop_1 PD ns gs128) ---")
for co in [0.0, 0.04, 0.08, 0.16, 0.3, 0.4]:
    ranking = []
    for mech in MECHS:
        g = grid("noshuffle", "128", mech, 1, "pop_1", 0)
        if g is None:
            continue
        r = cell(g, co, 0.0)
        if r:
            ranking.append((q(r), mech))
    ranking.sort(reverse=True)
    top = ", ".join(f"{m}={v:.3f}" for v, m in ranking[:4])
    print(f"  Cost={co:>4.2f}: {top}")

# ── F. genotype: does the machinery allele get selected out as Cost rises? ───
print("\n--- F. MACHINERY EROSION (c=0, pop_1 PD ns gs128 fset0) ---")
print("P mech: P1 allele freq & C1P1 chooser freq vs Cost.")
g = grid("noshuffle", "128", "P", 1, "pop_1", 0)
print(f"{'Cost':>6}  {'qBSeen':>7}  {'P1':>7}  {'C1P1':>7}  {'C1P0':>7}  {'C0(defect-genos)':>16}")
for co in SAMPLE_COST:
    r = cell(g, co, 0.0)
    if not r:
        continue
    p1 = allele(r, "P1")
    c1p1 = allele(r, "C1", "P1")
    c1p0 = allele(r, "C1", "P0")
    c0 = allele(r, "C0")
    print(f"  {co:>4.2f}  {q(r):>7.3f}  {p1:>7.3f}  {c1p1:>7.3f}  {c1p0:>7.3f}  {c0:>16.3f}")

print("\n  M mech: M1 allele freq & C1M1 (TFT) vs Cost (noshuffle so reciprocity is live).")
g = grid("noshuffle", "128", "M", 1, "pop_1", 0)
print(f"{'Cost':>6}  {'qBSeen':>7}  {'M1':>7}  {'C1M1':>7}  {'C1M0':>7}  {'C0':>7}")
for co in SAMPLE_COST:
    r = cell(g, co, 0.0)
    if not r:
        continue
    print(f"  {co:>4.2f}  {q(r):>7.3f}  {allele(r,'M1'):>7.3f}  {allele(r,'C1','M1'):>7.3f}  {allele(r,'C1','M0'):>7.3f}  {allele(r,'C0'):>7.3f}")

# ── F2. CONTROL DECOMPOSITION: cost erodes machinery, dilemma decides if it matters ─
print("\n--- F2. CONTROL (d0) vs PD (d1) DECOMPOSITION (M, c=0, ns gs128 pop_1) ---")
print("d0 has no social dilemma: isolates the pure module tax with zero enforcement demand.")
print("If M1 erodes at ~the same rate in d0 and d1, erosion is supply-side (cost), and")
print("the dilemma only sets whether losing the machinery drags behavior down.")
g0 = grid("noshuffle", "128", "M", 0, "pop_1", 0)
g1 = grid("noshuffle", "128", "M", 1, "pop_1", 0)
print(f"{'Cost':>6}  {'d0 qB':>7}  {'d0 M1':>7}  {'d0 C1M0':>8}  {'d1 qB':>7}  {'d1 M1':>7}")
for co in SAMPLE_COST:
    r0 = cell(g0, co, 0.0)
    r1 = cell(g1, co, 0.0)
    if not r0 or not r1:
        continue
    print(f"  {co:>4.2f}  {q(r0):>7.3f}  {allele(r0,'M1'):>7.3f}  {allele(r0,'C1','M0'):>8.3f}  {q(r1):>7.3f}  {allele(r1,'M1'):>7.3f}")

# ── G. shuffle: paying the tax for machinery that shuffle disables ───────────
print("\n--- G. SHUFFLE WASTE (M, c=0, pop_1 PD gs128 fset0) ---")
print("Under shuffle M behaves like control (no history), but M-carriers still pay Cost.")
print(f"{'Cost':>6}  {'M noshuffle qB':>14}  {'M shuffle qB':>13}  {'ctrl(_) qB':>11}")
gMns = grid("noshuffle", "128", "M", 1, "pop_1", 0)
gMsh = grid("shuffle", "128", "M", 1, "pop_1", 0)
gC = grid("noshuffle", "128", "_", 1, "pop_1", 0)
for co in SAMPLE_COST:
    rn = cell(gMns, co, 0.0)
    rs = cell(gMsh, co, 0.0) if gMsh else None
    rc = cell(gC, co, 0.0)
    print(f"  {co:>4.2f}  {q(rn):>14.3f}  {q(rs):>13.3f}  {q(rc):>11.3f}")

# ── H. snowdrift dilemma under information cost (dilemma 2) ───────────────────
print("\n--- H. DILEMMA CONTRAST at c=0 (pop_1 noshuffle gs128 fset0): does high floor buffer Cost? ---")
print(f"{'mech':6}  " + "".join(f"d{d} " + " ".join(f"C{co:.2f}" for co in [0.0, 0.1, 0.2, 0.4]) + "   " for d in [1, 2]))
for mech in ["M", "P", "IJMPQ"]:
    line = f"  {mech:6}"
    for d in [1, 2]:
        g = grid("noshuffle", "128", mech, d, "pop_1", 0)
        if g is None:
            line += "   missing         "
            continue
        line += "  "
        for co in [0.0, 0.1, 0.2, 0.4]:
            r = cell(g, co, 0.0)
            line += f"{q(r):.3f} " if r else " --   "
    print(line)

# ── I. gs=4 (small groups) under information cost ────────────────────────────
print("\n--- I. GROUPSIZE x COST (c=0, pop_1 PD noshuffle, fset0) ---")
print(f"{'mech':6}  " + "".join(f"gs{gs}: " + " ".join(f"C{co:.2f}" for co in [0.0, 0.08, 0.2, 0.4]) + "  " for gs in ["128", "4"]))
for mech in ["M", "P", "IJMPQ"]:
    line = f"  {mech:6}"
    for gs in ["128", "4"]:
        g = grid("noshuffle", gs, mech, 1, "pop_1", 0)
        if g is None:
            line += "  missing        "
            continue
        line += "  "
        for co in [0.0, 0.08, 0.2, 0.4]:
            r = cell(g, co, 0.0)
            line += f"{q(r):.3f} " if r else " --   "
    print(line)

print("\n" + "=" * 78)
print("DONE")
print("=" * 78)
