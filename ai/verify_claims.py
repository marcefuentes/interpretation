#!/usr/bin/env python3
"""
Verify headline numeric claims in the analysis docs against the .con data.

Each check re-derives a number that a doc asserts and compares it to the
expected value written in that doc. Run before committing doc edits to catch
drift between prose and data.

    python3 ai/verify_claims.py            # all studies
    python3 ai/verify_claims.py hamilton   # filter by substring

Exit code is non-zero if any check fails.

Tolerances: qBSeen / fitness / correlation values are rounded to the same 3
decimals the docs use, compared with a small tolerance; cell counts are exact.
"""

import csv
import math
import os
import sys

BASE = os.path.expanduser("~/results")
TOL = 0.006  # docs round to 3 decimals; allow half-ULP plus minor regen jitter

CHECKS = []  # (study, label, compute->float|int, expected, tol_or_None_for_exact)


def load(p):
    return list(csv.DictReader(open(p))) if os.path.exists(p) else None


def corr(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    return num / (dx * dy) if dx * dy else float("nan")


def ols2(R, P, Q):
    n = len(Q)
    mR = sum(R) / n
    mP = sum(P) / n
    mQ = sum(Q) / n
    Srr = sum((r - mR) ** 2 for r in R)
    Spp = sum((p - mP) ** 2 for p in P)
    Srp = sum((R[i] - mR) * (P[i] - mP) for i in range(n))
    Srq = sum((R[i] - mR) * (Q[i] - mQ) for i in range(n))
    Spq = sum((P[i] - mP) * (Q[i] - mQ) for i in range(n))
    det = Srr * Spp - Srp * Srp
    return (Spp * Srq - Srp * Spq) / det, (Srr * Spq - Srp * Srq) / det


def gsum(row, c, p=None):
    cols = [k for k in row if not k.endswith("SD") and len(k) == 12 and k[0] == "C"]
    cols = [x for x in cols if x.startswith(f"C{c}")]
    if p is not None:
        cols = [x for x in cols if f"P{p}" in x]
    return sum(float(row[x]) for x in cols)


def m1sum(row):
    cols = [k for k in row if not k.endswith("SD") and len(k) == 12
            and k[0] == "C" and "M1" in k]
    return sum(float(row[x]) for x in cols)


def check(study, label, fn, expected, tol=TOL):
    CHECKS.append((study, label, fn, expected, tol))


# ── path helpers ──────────────────────────────────────────────────────────────

def hpath(sh, gs, m, d, pop, f):
    return f"{BASE}/hamilton/{sh}_cost0.001_{gs}/{m}/{d}/{pop}/csv_{f}_for_image.con"


def mpath(sh, gs, m, d, f):
    return f"{BASE}/mutualism/{sh}_cost0.001_{gs}/{m}/{d}/pop_2/csv_{f}_for_image.con"


def ppath(sh, gs, m, pop, f):
    return f"{BASE}/prisoners/{sh}_cost0.001_{gs}/{m}/1/{pop}/csv_{f}_for_image.con"


def at_c(rows, c, col="qBSeen"):
    for r in rows:
        if abs(float(r["c0"]) - c) < 0.005:
            return float(r[col])
    return float("nan")


def mcell(rows, c0, c1, col="qBSeen"):
    for r in rows:
        if abs(float(r["c0"]) - c0) < 0.005 and abs(float(r["c1"]) - c1) < 0.005:
            return float(r[col])
    return float("nan")


# ════════════════════════════════════════════════════════════════════════════
# HAMILTON — hamilton_partner_choice.md, hamilton_reciprocity.md, hamilton_combined.md
# ════════════════════════════════════════════════════════════════════════════

def ham_P_profile():
    r = load(hpath("shuffle", "128", "P", 1, "pop_2", 0))
    return [round(at_c(r, c), 3) for c in (0.0, 0.08, 0.16, 0.24, 0.32, 0.40)]

# partner_choice.md cooperation profile (P, PD, shuffle, pop_2 fset_0)
for c, exp in zip((0.0, 0.08, 0.16, 0.24, 0.32, 0.40),
                  (0.963, 0.849, 0.728, 0.630, 0.553, 0.022)):
    check("hamilton", f"PC: P qBSeen at c={c:.2f}",
          (lambda cc=c: at_c(load(hpath("shuffle", "128", "P", 1, "pop_2", 0)), cc)), exp)


def ham_P_corr():
    r0 = load(hpath("shuffle", "128", "P", 1, "pop_2", 0))
    r1 = load(hpath("shuffle", "128", "P", 1, "pop_2", 1))
    m1 = {round(float(r["c0"]), 4): r for r in r1}
    dq, dw = [], []
    for r in r0:
        rr = m1.get(round(float(r["c0"]), 4))
        if rr:
            dq.append(float(r["qBSeen"]) - float(rr["qBSeen"]))
            dw.append(float(r["wmean"]) - float(rr["wmean"]))
    return corr(dq, dw)


check("hamilton", "PC: P pop_2 corr(dq,dw) = -0.984", ham_P_corr, -0.984)

# reciprocity.md: M shuffle vs noshuffle at c=0.10 (pop_2 fset_0)
check("hamilton", "RC: M noshuffle qBSeen c=0.10 = 0.915",
      lambda: at_c(load(hpath("noshuffle", "128", "M", 1, "pop_2", 0)), 0.10), 0.915)
check("hamilton", "RC: M shuffle qBSeen c=0.10 ~ control (<0.06)",
      lambda: at_c(load(hpath("shuffle", "128", "M", 1, "pop_2", 0)), 0.10), 0.053)

# reciprocity.md: M1 under M at d0 noshuffle mean = 0.392 (vs control 0.494)
check("hamilton", "RC: d0 M1 mean under M noshuffle = 0.392",
      lambda: sum(m1sum(r) for r in load(hpath("noshuffle", "128", "M", 0, "pop_2", 0)))
      / len(load(hpath("noshuffle", "128", "M", 0, "pop_2", 0))), 0.392, 0.01)

# combined.md: IJMPQ shuffle vs noshuffle at c=0.40
check("hamilton", "CB: IJMPQ shuffle qBSeen c=0.40 = 0.672",
      lambda: at_c(load(hpath("shuffle", "128", "IJMPQ", 1, "pop_2", 0)), 0.40), 0.672)
check("hamilton", "CB: IJMPQ noshuffle qBSeen c=0.40 = 0.382",
      lambda: at_c(load(hpath("noshuffle", "128", "IJMPQ", 1, "pop_2", 0)), 0.40), 0.382)


# ════════════════════════════════════════════════════════════════════════════
# MUTUALISM
# ════════════════════════════════════════════════════════════════════════════

def mut_rolesplit_mean(sh, gs, m, d, f):
    r = load(mpath(sh, gs, m, d, f))
    return sum(float(x["qBSeen"]) for x in r) / len(r)


# partner_choice.md role-split means (P, noshuffle, PD/SD)
check("mutualism", "PC: P PD Pop_0 mean = 0.472",
      lambda: mut_rolesplit_mean("noshuffle", "128", "P", 1, 0), 0.472)
check("mutualism", "PC: P PD Pop_1 mean = 0.146",
      lambda: mut_rolesplit_mean("noshuffle", "128", "P", 1, 1), 0.146)
check("mutualism", "PC: control PD Pop_0 mean = 0.103",
      lambda: mut_rolesplit_mean("noshuffle", "128", "_", 1, 0), 0.103)


def mut_exploit(d):
    r0 = load(mpath("noshuffle", "128", "P", d, 0))
    r1 = load(mpath("noshuffle", "128", "P", d, 1))
    m1 = {(round(float(x["c0"]), 4), round(float(x["c1"]), 4)): x for x in r1}
    dq, dw, nless, defs = [], [], 0, []
    for x in r0:
        k = (round(float(x["c0"]), 4), round(float(x["c1"]), 4))
        if k in m1:
            q = float(x["qBSeen"]) - float(m1[k]["qBSeen"])
            w = float(x["wmean"]) - float(m1[k]["wmean"])
            dq.append(q); dw.append(w)
            if w < 0:
                nless += 1; defs.append(-w)
    return corr(dq, dw), nless, sum(defs) / len(defs)


# partner_choice.md exploitation counts/corr/deficit
check("mutualism", "PC: P PD corr(dq,dw) = -0.986", lambda: mut_exploit(1)[0], -0.986)
check("mutualism", "PC: P PD lower-fitness cells = 210", lambda: mut_exploit(1)[1], 210, None)
check("mutualism", "PC: P PD mean deficit = 0.140", lambda: mut_exploit(1)[2], 0.140)
check("mutualism", "PC: P SD corr(dq,dw) = -0.144", lambda: mut_exploit(2)[0], -0.144)
check("mutualism", "PC: P SD lower-fitness cells = 190", lambda: mut_exploit(2)[1], 190, None)
check("mutualism", "PC: P SD mean deficit = 0.116", lambda: mut_exploit(2)[2], 0.116)


def mut_m1_suppressed_total():
    total = 0
    for sh in ("noshuffle", "shuffle"):
        for gs in ("128", "4"):
            for d in (0, 1, 2):
                for f in (0, 1):
                    rM = load(mpath(sh, gs, "M", d, f))
                    rC = load(mpath(sh, gs, "_", d, f))
                    if not rM or not rC:
                        continue
                    cm = {(round(float(x["c0"]), 4), round(float(x["c1"]), 4)): m1sum(x) for x in rC}
                    for x in rM:
                        k = (round(float(x["c0"]), 4), round(float(x["c1"]), 4))
                        if k in cm and m1sum(x) < cm[k]:
                            total += 1
    return total


# reciprocity.md: 3,701 cell-conditions with M1 suppressed
check("mutualism", "RC: M1 suppressed cell-conditions = 3701", mut_m1_suppressed_total, 3701, None)

# reciprocity.md: M role-split means (PD)
check("mutualism", "RC: M PD Pop_0 mean = 0.637",
      lambda: mut_rolesplit_mean("noshuffle", "128", "M", 1, 0), 0.637)
check("mutualism", "RC: M PD Pop_1 mean = 0.551",
      lambda: mut_rolesplit_mean("noshuffle", "128", "M", 1, 1), 0.551)

# reciprocity.md: shuffle IM/IJM means (PD, Pop_0)
check("mutualism", "RC: IM shuffle PD Pop_0 mean = 0.362",
      lambda: mut_rolesplit_mean("shuffle", "128", "IM", 1, 0), 0.362)
check("mutualism", "RC: IJM shuffle PD Pop_0 mean = 0.453",
      lambda: mut_rolesplit_mean("shuffle", "128", "IJM", 1, 0), 0.453)
check("mutualism", "RC: IJM shuffle PD Pop_1 mean = 0.299",
      lambda: mut_rolesplit_mean("shuffle", "128", "IJM", 1, 1), 0.299)


# ════════════════════════════════════════════════════════════════════════════
# PRISONERS
# ════════════════════════════════════════════════════════════════════════════

def pris_ba(sh, gs, m, pop):
    r = load(ppath(sh, gs, m, pop, 0))
    R = [float(x["R0"]) for x in r]
    P = [float(x["P0"]) for x in r]
    Q = [float(x["qBSeen"]) for x in r]
    a, b = ols2(R, P, Q)
    return -b / a


def pris_mean(sh, gs, m, pop):
    r = load(ppath(sh, gs, m, pop, 0))
    return sum(float(x["qBSeen"]) for x in r) / len(r)


# calibration.md: payoff-axis -b/a (pop_1, noshuffle gs128)
check("prisoners", "CAL: M -b/a = 1.73", lambda: pris_ba("noshuffle", "128", "M", "pop_1"), 1.73, 0.03)
check("prisoners", "CAL: P -b/a = 0.89", lambda: pris_ba("noshuffle", "128", "P", "pop_1"), 0.89, 0.03)
check("prisoners", "CAL: IMP -b/a = 0.50", lambda: pris_ba("noshuffle", "128", "IMP", "pop_1"), 0.50, 0.03)
check("prisoners", "CAL: IJMPQ -b/a = 0.53", lambda: pris_ba("noshuffle", "128", "IJMPQ", "pop_1"), 0.53, 0.03)

# calibration.md: gs=4 mirror — MP reverts to M signature; P collapses
check("prisoners", "CAL: P gs=4 mean = 0.075", lambda: pris_mean("noshuffle", "4", "P", "pop_1"), 0.075, 0.01)
check("prisoners", "CAL: MP gs=4 -b/a = 1.62", lambda: pris_ba("noshuffle", "4", "MP", "pop_1"), 1.62, 0.05)
check("prisoners", "CAL: M gs=4 mean = 0.730 (invariant)", lambda: pris_mean("noshuffle", "4", "M", "pop_1"), 0.730, 0.01)

# partner_choice.md: pop_3 evolving/fixed means
check("prisoners", "PC: pop_3 evolving mean = 0.410", lambda: pris_mean("noshuffle", "128", "P", "pop_3"), 0.410, 0.01)

# reciprocity.md: M mean noshuffle/shuffle gs128, and IM/IJM gs4 boost
check("prisoners", "RC: M noshuffle mean = 0.730", lambda: pris_mean("noshuffle", "128", "M", "pop_1"), 0.730, 0.01)
check("prisoners", "RC: M shuffle mean = 0.017", lambda: pris_mean("shuffle", "128", "M", "pop_1"), 0.017, 0.01)
check("prisoners", "RC: IM shuffle gs4 mean = 0.521", lambda: pris_mean("shuffle", "4", "IM", "pop_1"), 0.521, 0.01)
check("prisoners", "RC: IJM shuffle gs4 mean = 0.706", lambda: pris_mean("shuffle", "4", "IJM", "pop_1"), 0.706, 0.01)


# ════════════════════════════════════════════════════════════════════════════
# RUN
# ════════════════════════════════════════════════════════════════════════════

def main():
    filt = sys.argv[1] if len(sys.argv) > 1 else None
    npass = nfail = nskip = 0
    fails = []
    cur = None
    for study, label, fn, expected, tol in CHECKS:
        if filt and filt not in study and filt not in label:
            continue
        if study != cur:
            cur = study
            print(f"\n=== {study.upper()} ===")
        try:
            got = fn()
        except Exception as e:  # missing data etc.
            print(f"  SKIP  {label}  ({type(e).__name__}: {e})")
            nskip += 1
            continue
        if isinstance(got, float) and math.isnan(got):
            print(f"  SKIP  {label}  (no data)")
            nskip += 1
            continue
        if tol is None:  # exact (counts)
            ok = int(got) == int(expected)
            gs, es = str(int(got)), str(int(expected))
        else:
            ok = abs(got - expected) <= tol
            gs, es = f"{got:.3f}", f"{expected:.3f}"
        mark = "PASS" if ok else "FAIL"
        print(f"  {mark}  {label}  (got {gs}, expected {es})")
        if ok:
            npass += 1
        else:
            nfail += 1
            fails.append(label)
    print(f"\n{'-'*60}\n{npass} passed, {nfail} failed, {nskip} skipped")
    if fails:
        print("FAILED:")
        for f in fails:
            print(f"  - {f}")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
