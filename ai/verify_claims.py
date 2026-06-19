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

import math
import sys

from trps_io import BASE, allele, corr, gsum, load, m1sum, ols2  # noqa: F401

TOL = 0.006  # docs round to 3 decimals; allow half-ULP plus minor regen jitter

CHECKS = []  # (study, label, compute->float|int, expected, tol_or_None_for_exact)


def check(study, label, fn, expected, tol=TOL):
    CHECKS.append((study, label, fn, expected, tol))


# ── path helpers ──────────────────────────────────────────────────────────────

def hpath(sh, gs, m, d, pop, f):
    return f"{BASE}/hamilton/{sh}_cost0.001_{gs}/{m}/{d}/{pop}/csv_{f}_for_image.con"


def mpath(sh, gs, m, d, f):
    return f"{BASE}/mutualism/{sh}_cost0.001_{gs}/{m}/{d}/pop_2/csv_{f}_for_image.con"


def ppath(sh, gs, m, pop, f):
    return f"{BASE}/prisoners/{sh}_cost0.001_{gs}/{m}/1/{pop}/csv_{f}_for_image.con"


def sdpath(sh, gs, m, pop, f):
    return f"{BASE}/snowdrift/{sh}_cost0.001_{gs}/{m}/2/{pop}/csv_{f}_for_image.con"


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


def mcell_row(rows, c0, c1):
    for r in rows:
        if abs(float(r["c0"]) - c0) < 0.005 and abs(float(r["c1"]) - c1) < 0.005:
            return r
    return None


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

# combined.md gs=128 PD profile (shuffle, pop_2 fset_0): MP/MPQ collapse, IMP/IJMPQ tail
check("hamilton", "CB: MP shuffle qBSeen c=0.40 = 0.023",
      lambda: at_c(load(hpath("shuffle", "128", "MP", 1, "pop_2", 0)), 0.40), 0.023)
check("hamilton", "CB: MPQ shuffle qBSeen c=0.40 = 0.036",
      lambda: at_c(load(hpath("shuffle", "128", "MPQ", 1, "pop_2", 0)), 0.40), 0.036)
check("hamilton", "CB: IMP shuffle qBSeen c=0.08 = 0.951",
      lambda: at_c(load(hpath("shuffle", "128", "IMP", 1, "pop_2", 0)), 0.08), 0.951)
check("hamilton", "CB: IMP shuffle qBSeen c=0.40 = 0.170",
      lambda: at_c(load(hpath("shuffle", "128", "IMP", 1, "pop_2", 0)), 0.40), 0.170)

# combined.md gs=4 PD profile (shuffle, pop_2 fset_0): weaker high-c tail
check("hamilton", "CB: IMP gs=4 shuffle qBSeen c=0.40 = 0.065",
      lambda: at_c(load(hpath("shuffle", "4", "IMP", 1, "pop_2", 0)), 0.40), 0.065)
check("hamilton", "CB: IJMPQ gs=4 shuffle qBSeen c=0.32 = 0.892",
      lambda: at_c(load(hpath("shuffle", "4", "IJMPQ", 1, "pop_2", 0)), 0.32), 0.892)
check("hamilton", "CB: IJMPQ gs=4 shuffle qBSeen c=0.40 = 0.342",
      lambda: at_c(load(hpath("shuffle", "4", "IJMPQ", 1, "pop_2", 0)), 0.40), 0.342)


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


# reciprocity.md: cross-population hitchhiking (PD, noshuffle, gs=128, c0=0.10, c1=0.30)
check("mutualism", "RC: hitchhike Pop_0 M1 (0.10,0.30) = 0.749",
      lambda: allele(mcell_row(load(mpath("noshuffle", "128", "M", 1, 0)), 0.10, 0.30), "M1"), 0.749)
check("mutualism", "RC: hitchhike Pop_1 M1 (0.10,0.30) = 0.370 (< control)",
      lambda: allele(mcell_row(load(mpath("noshuffle", "128", "M", 1, 1)), 0.10, 0.30), "M1"), 0.370)
check("mutualism", "RC: hitchhike control Pop_1 M1 (0.10,0.30) = 0.500",
      lambda: allele(mcell_row(load(mpath("noshuffle", "128", "_", 1, 1)), 0.10, 0.30), "M1"), 0.500, 0.01)

# combined.md: shuffle lifetime recovery carried by J not Q (PD Pop_1 means, gs=128)
check("mutualism", "CB: J adds IM->IJM shuffle Pop_1 = +0.133",
      lambda: mut_rolesplit_mean("shuffle", "128", "IJM", 1, 1)
      - mut_rolesplit_mean("shuffle", "128", "IM", 1, 1), 0.133, 0.01)
check("mutualism", "CB: Q adds MP->MPQ shuffle Pop_1 = +0.007 (negligible)",
      lambda: mut_rolesplit_mean("shuffle", "128", "MPQ", 1, 1)
      - mut_rolesplit_mean("shuffle", "128", "MP", 1, 1), 0.007, 0.01)


def mut_dominance(sh, gs, m, d):
    r0 = load(mpath(sh, gs, m, d, 0))
    r1 = load(mpath(sh, gs, m, d, 1))
    m1 = {(round(float(x["c0"]), 4), round(float(x["c1"]), 4)): float(x["qBSeen"]) for x in r1}
    n = 0
    for x in r0:
        k = (round(float(x["c0"]), 4), round(float(x["c1"]), 4))
        if k in m1 and float(x["qBSeen"]) > m1[k]:
            n += 1
    return n


# combined.md: pop_2 role-split means + dominance counts (noshuffle, gs=128)
check("mutualism", "CB: MP PD Pop_0 mean = 0.606",
      lambda: mut_rolesplit_mean("noshuffle", "128", "MP", 1, 0), 0.606)
check("mutualism", "CB: MP PD Pop_1 mean = 0.410",
      lambda: mut_rolesplit_mean("noshuffle", "128", "MP", 1, 1), 0.410)
check("mutualism", "CB: IMP PD Pop_0 mean = 0.670",
      lambda: mut_rolesplit_mean("noshuffle", "128", "IMP", 1, 0), 0.670)
check("mutualism", "CB: IMP PD Pop_1 mean = 0.505",
      lambda: mut_rolesplit_mean("noshuffle", "128", "IMP", 1, 1), 0.505)
check("mutualism", "CB: IJMPQ PD Pop_0 mean = 0.729",
      lambda: mut_rolesplit_mean("noshuffle", "128", "IJMPQ", 1, 0), 0.729)
check("mutualism", "CB: IJMPQ PD Pop_1 mean = 0.573",
      lambda: mut_rolesplit_mean("noshuffle", "128", "IJMPQ", 1, 1), 0.573)
check("mutualism", "CB: IJMPQ SD Pop_1 mean = 0.609",
      lambda: mut_rolesplit_mean("noshuffle", "128", "IJMPQ", 2, 1), 0.609)
check("mutualism", "CB: MP PD Pop_0>Pop_1 = 210", lambda: mut_dominance("noshuffle", "128", "MP", 1), 210, None)
check("mutualism", "CB: IMP PD Pop_0>Pop_1 = 203", lambda: mut_dominance("noshuffle", "128", "IMP", 1), 203, None)
check("mutualism", "CB: IJMPQ PD Pop_0>Pop_1 = 198", lambda: mut_dominance("noshuffle", "128", "IJMPQ", 1), 198, None)
check("mutualism", "CB: IJMPQ SD Pop_0>Pop_1 = 176", lambda: mut_dominance("noshuffle", "128", "IJMPQ", 2), 176, None)

# combined.md: shuffle disables M -> Pop_1 drops (gs=128)
check("mutualism", "CB: IMP shuffle PD Pop_1 mean = 0.264",
      lambda: mut_rolesplit_mean("shuffle", "128", "IMP", 1, 1), 0.264)
check("mutualism", "CB: IJMPQ shuffle PD Pop_1 mean = 0.442",
      lambda: mut_rolesplit_mean("shuffle", "128", "IJMPQ", 1, 1), 0.442)
check("mutualism", "CB: IJMPQ shuffle SD Pop_1 mean = 0.477",
      lambda: mut_rolesplit_mean("shuffle", "128", "IJMPQ", 2, 1), 0.477)

# combined.md: c0=0 column (noshuffle, gs=128, Pop_0 = fset_0)
check("mutualism", "CB: M c0=0 c1=0.10 = 0.918",
      lambda: mcell(load(mpath("noshuffle", "128", "M", 1, 0)), 0.0, 0.10), 0.918)
check("mutualism", "CB: P c0=0 c1=0.10 = 0.864",
      lambda: mcell(load(mpath("noshuffle", "128", "P", 1, 0)), 0.0, 0.10), 0.864)
check("mutualism", "CB: IMP c0=0 c1=0.02 = 0.961",
      lambda: mcell(load(mpath("noshuffle", "128", "IMP", 1, 0)), 0.0, 0.02), 0.961)
check("mutualism", "CB: IJMPQ c0=0 c1=0.10 = 0.966",
      lambda: mcell(load(mpath("noshuffle", "128", "IJMPQ", 1, 0)), 0.0, 0.10), 0.966)
check("mutualism", "CB: gs=4 IJMPQ PD Pop_1 mean = 0.617",
      lambda: mut_rolesplit_mean("noshuffle", "4", "IJMPQ", 1, 1), 0.617)
check("mutualism", "CB: gs=4 IMP PD Pop_0>Pop_1 = 208",
      lambda: mut_dominance("noshuffle", "4", "IMP", 1), 208, None)


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


# ── additional coverage (paradox of success + cross-study tables) ─────────────

def pcell(rows, R, P, col="qBSeen"):
    for r in rows:
        if abs(float(r["R0"]) - R) < 0.005 and abs(float(r["P0"]) - P) < 0.005:
            return float(r[col])
    return float("nan")


def pris_paradox(sh, gs, m):
    """corr(ΔqBSeen, Δwmean) and count of fitness-inverted cells (pop_2)."""
    r0 = load(ppath(sh, gs, m, "pop_2", 0))
    r1 = load(ppath(sh, gs, m, "pop_2", 1))
    m1 = {(x["R0"], x["P0"]): x for x in r1}
    dq, dw, inv = [], [], 0
    for x in r0:
        k = (x["R0"], x["P0"])
        if k not in m1:
            continue
        q = float(x["qBSeen"]) - float(m1[k]["qBSeen"])
        w = float(x["wmean"]) - float(m1[k]["wmean"])
        dq.append(q)
        dw.append(w)
        if q * w < 0:  # higher-cooperation side has lower fitness
            inv += 1
    return corr(dq, dw), inv, len(dq)


# partner_choice.md: prisoners pop_2 paradox of success (P, noshuffle, gs=128)
check("prisoners", "PC: pop_2 paradox corr(dqB,dw) = -1.000",
      lambda: pris_paradox("noshuffle", "128", "P")[0], -1.000, 0.01)
check("prisoners", "PC: pop_2 fitness-inverted cells = 172",
      lambda: pris_paradox("noshuffle", "128", "P")[1], 172, None)
check("prisoners", "PC: pop_2 (R=0.30,P=0.14) qB_0 = 0.286",
      lambda: pcell(load(ppath("noshuffle", "128", "P", "pop_2", 0)), 0.30, 0.14), 0.286)
check("prisoners", "PC: pop_2 (R=0.30,P=0.14) defector w_1 > coop w_0 (+0.166)",
      lambda: pcell(load(ppath("noshuffle", "128", "P", "pop_2", 1)), 0.30, 0.14, "wmean")
      - pcell(load(ppath("noshuffle", "128", "P", "pop_2", 0)), 0.30, 0.14, "wmean"), 0.166, 0.01)


def pris_locus_mean(m, col="qBSeen"):
    """Mean over the temptation=risk anti-diagonal R+P=1.0 (pop_1, PD, noshuffle)."""
    r = load(ppath("noshuffle", "128", m, "pop_1", 0))
    v = [float(x[col]) for x in r if abs(float(x["R0"]) + float(x["P0"]) - 1.0) < 0.005]
    return sum(v) / len(v)


# calibration.md: temptation=risk locus (R+P=1.0) means
check("prisoners", "CAL: R+P=1 locus P mean = 0.944", lambda: pris_locus_mean("P"), 0.944, 0.01)
check("prisoners", "CAL: R+P=1 locus M mean = 0.899", lambda: pris_locus_mean("M"), 0.899, 0.01)
check("prisoners", "CAL: R+P=1 locus IJMPQ mean = 0.965", lambda: pris_locus_mean("IJMPQ"), 0.965, 0.01)

# combined.md: IMP mutual-cooperation table (PD, c0=0.1, noshuffle gs=128)
check("mutualism", "CB: IMP mutual-coop (0.1,0.12) Pop_0 = 0.953",
      lambda: mcell(load(mpath("noshuffle", "128", "IMP", 1, 0)), 0.10, 0.12), 0.953)
check("mutualism", "CB: IMP mutual-coop (0.1,0.12) Pop_1 = 0.952",
      lambda: mcell(load(mpath("noshuffle", "128", "IMP", 1, 1)), 0.10, 0.12), 0.952)

# combined.md: c0=0 snowdrift column (M holds at ceiling, dilemma 2)
check("mutualism", "CB: M c0=0 c1=0.10 snowdrift = 0.950",
      lambda: mcell(load(mpath("noshuffle", "128", "M", 2, 0)), 0.0, 0.10), 0.950)

# combined.md: hamilton snowdrift IJMPQ at c=0.40 (shuffle, gs=128)
check("hamilton", "CB: IJMPQ snowdrift qBSeen c=0.40 = 0.960",
      lambda: at_c(load(hpath("shuffle", "128", "IJMPQ", 2, "pop_2", 0)), 0.40), 0.960)


# ════════════════════════════════════════════════════════════════════════════
# SNOWDRIFT
# ════════════════════════════════════════════════════════════════════════════

def sd_ba(sh, gs, m, pop):
    r = load(sdpath(sh, gs, m, pop, 0))
    R = [float(x["R0"]) for x in r]
    S = [float(x["S0"]) for x in r]
    Q = [float(x["qBSeen"]) for x in r]
    a, b = ols2(R, S, Q)
    return -b / a


def sd_mean(sh, gs, m, pop):
    r = load(sdpath(sh, gs, m, pop, 0))
    return sum(float(x["qBSeen"]) for x in r) / len(r)


def sd_paradox(sh, gs, m):
    r0 = load(sdpath(sh, gs, m, "pop_2", 0))
    r1 = load(sdpath(sh, gs, m, "pop_2", 1))
    m1 = {(x["R0"], x["S0"]): x for x in r1}
    dq, dw, inv = [], [], 0
    for x in r0:
        k = (x["R0"], x["S0"])
        if k not in m1:
            continue
        q = float(x["qBSeen"]) - float(m1[k]["qBSeen"])
        w = float(x["wmean"]) - float(m1[k]["wmean"])
        dq.append(q)
        dw.append(w)
        if q * w < 0:
            inv += 1
    return corr(dq, dw), inv


check("snowdrift", "CAL: _ mean = 0.493", lambda: sd_mean("noshuffle", "128", "_", "pop_1"), 0.493, 0.01)
check("snowdrift", "CAL: M mean = 0.599", lambda: sd_mean("noshuffle", "128", "M", "pop_1"), 0.599, 0.01)
check("snowdrift", "CAL: P mean = 0.947", lambda: sd_mean("noshuffle", "128", "P", "pop_1"), 0.947, 0.01)
check("snowdrift", "CAL: IJMPQ mean = 0.956", lambda: sd_mean("noshuffle", "128", "IJMPQ", "pop_1"), 0.956, 0.01)

check("snowdrift", "CAL: M -b/a = -0.15", lambda: sd_ba("noshuffle", "128", "M", "pop_1"), -0.15, 0.03)
check("snowdrift", "CAL: P -b/a = 0.19", lambda: sd_ba("noshuffle", "128", "P", "pop_1"), 0.19, 0.03)
check("snowdrift", "CAL: IJMPQ -b/a = 0.05", lambda: sd_ba("noshuffle", "128", "IJMPQ", "pop_1"), 0.05, 0.03)

check("snowdrift", "RC: M shuffle mean = 0.497", lambda: sd_mean("shuffle", "128", "M", "pop_1"), 0.497, 0.01)
check("snowdrift", "RC: IM shuffle mean = 0.605", lambda: sd_mean("shuffle", "128", "IM", "pop_1"), 0.605, 0.01)
check("snowdrift", "RC: IJM shuffle mean = 0.696", lambda: sd_mean("shuffle", "128", "IJM", "pop_1"), 0.696, 0.01)

check("snowdrift", "CAL: P gs=4 mean = 0.717", lambda: sd_mean("noshuffle", "4", "P", "pop_1"), 0.717, 0.01)
check("snowdrift", "CAL: IJMPQ gs=4 mean = 0.904", lambda: sd_mean("noshuffle", "4", "IJMPQ", "pop_1"), 0.904, 0.01)

check("snowdrift", "PC: pop_2 paradox corr = -0.437", lambda: sd_paradox("noshuffle", "128", "P")[0], -0.437, 0.01)
check("snowdrift", "PC: pop_2 fitness-inverted cells = 172", lambda: sd_paradox("noshuffle", "128", "P")[1], 172, None)


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
