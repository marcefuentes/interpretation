#!/usr/bin/env python3
"""
Analyze the new-parameterization prisoners calibration study.

Prisoners is a raw PD payoff-plane sweep: T = 0.9 and S = 0.1 are fixed, while
R and P are swept independently over an 18x18 grid (172 cells satisfying
T > R > P > S). Dilemma folder 1 (PD) only; symmetric payoffs across
populations; pops 1/2/3; shuffle/noshuffle; gs 128/4; Runs = 30.

Purpose: hamilton/mutualism weld temptation (T-R), risk (P-S) and the
cooperation advantage (R-P) onto a single cost axis c. This sweep decouples
them, so we can attribute each mechanism's behavior to a payoff axis.

Cell key is (R0, P0). T0 = 0.9, S0 = 0.1 fixed.
"""

import os

from trps_io import corr, gsum, load, ols2  # noqa: F401

PRIS_BASE = os.path.expanduser("~/results/prisoners")
T_FIX, S_FIX = 0.9, 0.1


def path(sh, gs, mech, pop, fset):
    return os.path.join(PRIS_BASE, f"{sh}_cost0.001_{gs}", mech, "1", pop,
                        f"csv_{fset}_for_image.con")


MECHS = ["_", "M", "P", "MP", "MPQ", "IMP", "IJMPQ"]
SHUFFLE_ONLY = ["IM", "IJM"]


def sensitivity(sh, gs, mech, pop, fset):
    r = load(path(sh, gs, mech, pop, fset))
    if not r:
        return None
    R = [float(x["R0"]) for x in r]
    P = [float(x["P0"]) for x in r]
    Q = [float(x["qBSeen"]) for x in r]
    a, b = ols2(R, P, Q)
    return sum(Q) / len(Q), a, b, (-b / a if a else float("nan"))


print("=" * 78)
print("PRISONERS CALIBRATION (PD, T=0.9, S=0.1; R,P swept; 172 cells; Runs=30)")
print("=" * 78)

print("\n--- PAYOFF-AXIS SENSITIVITY: qBSeen ~ a*R + b*P ---")
print("a = dq/dR (reward/temptation axis); b = dq/dP (risk/defection-payoff)")
print("-b/a > 1 => P-axis dominated; ~1 => tracks R-P; < 1 => R-axis dominated")
print(f"\n{'cond':22} {'mech':6} {'meanQ':>6} {'a(R)':>7} {'b(P)':>7} {'-b/a':>6} {'cR-P':>6} {'cR':>6} {'cP':>6}")
for sh in ["noshuffle", "shuffle"]:
    for gs in ["128", "4"]:
        for mech in MECHS + (SHUFFLE_ONLY if sh == "shuffle" else []):
            for pop, fset in [("pop_1", 0), ("pop_2", 0)]:
                r = load(path(sh, gs, mech, pop, fset))
                if not r:
                    continue
                R = [float(x["R0"]) for x in r]
                P = [float(x["P0"]) for x in r]
                Q = [float(x["qBSeen"]) for x in r]
                RP = [R[i] - P[i] for i in range(len(R))]
                a, b = ols2(R, P, Q)
                tag = f"{sh[:4]}_{gs}_{pop[-1]}"
                print(f"{tag:22} {mech:6} {sum(Q)/len(Q):6.3f} {a:7.3f} {b:7.3f} "
                      f"{(-b/a if a else float('nan')):6.2f} {corr(RP,Q):6.3f} {corr(R,Q):6.3f} {corr(P,Q):6.3f}")
        print()


print("\n--- PARTNER CHOICE: qBSeen collapses onto R-P (pop_1, noshuffle gs128) ---")
r = load(path("noshuffle", "128", "P", "pop_1", 0))
bins = {}
for x in r:
    rp = round(float(x["R0"]) - float(x["P0"]), 2)
    bins.setdefault(rp, []).append(float(x["qBSeen"]))
print(f"{'R-P':>5} {'n':>3} {'meanQ':>6} {'min':>6} {'max':>6} {'spread':>6}")
for rp in sorted(bins):
    v = bins[rp]
    print(f"{rp:5.2f} {len(v):3} {sum(v)/len(v):6.3f} {min(v):6.3f} {max(v):6.3f} {max(v)-min(v):6.3f}")


print("\n--- P GENOTYPES along R-P (pop_1, noshuffle gs128): C1P1/C1P0/C0P1 ---")
print(f"{'R-P':>5} {'qB':>6} {'C1P1':>6} {'C1P0':>6} {'C0P1':>6}")
rows = sorted(r, key=lambda x: float(x["R0"]) - float(x["P0"]))
seen = set()
for x in rows:
    rp = round(float(x["R0"]) - float(x["P0"]), 2)
    if rp in seen:
        continue
    seen.add(rp)
    print(f"{rp:5.2f} {float(x['qBSeen']):6.3f} {gsum(x,'1','1'):6.3f} "
          f"{gsum(x,'1','0'):6.3f} {gsum(x,'0','1'):6.3f}")


print("\n--- POP_2 SYMMETRY BREAKING (P, noshuffle gs128): fset_0 vs fset_1 ---")
r0 = load(path("noshuffle", "128", "P", "pop_2", 0))
r1 = load(path("noshuffle", "128", "P", "pop_2", 1))
m1 = {(x["R0"], x["P0"]): x for x in r1}
print(f"{'R':>5} {'P':>5} {'R-P':>5} {'qB_0':>6} {'qB_1':>6} {'dqB':>6} {'w_0':>6} {'w_1':>6}")
for x in sorted(r0, key=lambda z: (float(z["P0"]), float(z["R0"]))):
    k = (x["R0"], x["P0"])
    if k not in m1:
        continue
    y = m1[k]
    R = float(x["R0"]); P = float(x["P0"])
    if round(P, 2) != 0.14:  # one P-row slice for brevity
        continue
    q0 = float(x["qBSeen"]); q1 = float(y["qBSeen"])
    print(f"{R:5.2f} {P:5.2f} {R-P:5.2f} {q0:6.3f} {q1:6.3f} {q0-q1:+6.3f} "
          f"{float(x['wmean']):6.3f} {float(y['wmean']):6.3f}")


print("\n--- MEAN qBSeen per mechanism/condition (pop_1) ---")
print(f"{'mech':6}", end="")
conds = [("noshuffle", "128"), ("shuffle", "128"), ("noshuffle", "4"), ("shuffle", "4")]
for sh, gs in conds:
    print(f" {sh[:2]+gs:>9}", end="")
print()
for mech in MECHS + SHUFFLE_ONLY:
    print(f"{mech:6}", end="")
    for sh, gs in conds:
        r = load(path(sh, gs, mech, "pop_1", 0))
        print(f" {(sum(float(x['qBSeen']) for x in r)/len(r) if r else float('nan')):9.3f}", end="")
    print()


print("\n--- M MECHANISM: risk (P) sensitivity detail (pop_1, noshuffle gs128) ---")
r = load(path("noshuffle", "128", "M", "pop_1", 0))
print("qBSeen at fixed R=0.50 as P rises (risk increases):")
for x in sorted(r, key=lambda z: float(z["P0"])):
    if abs(float(x["R0"]) - 0.50) < 1e-6:
        print(f"  P={float(x['P0']):.2f} (P-S={float(x['P0'])-S_FIX:.2f}): qBSeen={float(x['qBSeen']):.3f}")


print("\n--- IM / IJM (shuffle only): mean qBSeen vs M, pop_1 & pop_2 ---")
for gs in ["128", "4"]:
    print(f"  gs={gs}:")
    for mech in ["M", "IM", "IJM"]:
        vals = []
        for pop in ["pop_1", "pop_2"]:
            r = load(path("shuffle", gs, mech, pop, 0))
            vals.append(sum(float(x["qBSeen"]) for x in r) / len(r) if r else float("nan"))
        print(f"    {mech:4} shuffle: pop_1={vals[0]:.3f} pop_2={vals[1]:.3f}")


print("\n--- POP_3 (evolving vs fixed), P mechanism, noshuffle gs128 ---")
for fset, label in [(0, "evolving"), (1, "fixed")]:
    r = load(path("noshuffle", "128", "P", "pop_3", fset))
    if not r:
        continue
    mq = sum(float(x["qBSeen"]) for x in r) / len(r)
    print(f"  fset_{fset} ({label}): mean qBSeen={mq:.3f}")


print("\n--- GROUPSIZE 4 vs 128 (pop_1, noshuffle): mean qB and -b/a ---")
print("gs=4 strips the partner-choice (P) component (mirror of shuffle stripping M)")
print(f"{'mech':6} {'qB_128':>7} {'qB_4':>7} {'-b/a_128':>9} {'-b/a_4':>7}")
for mech in MECHS:
    out = []
    for gs in ["128", "4"]:
        r = load(path("noshuffle", gs, mech, "pop_1", 0))
        if not r:
            out.append((float("nan"), float("nan")))
            continue
        R = [float(x["R0"]) for x in r]
        P = [float(x["P0"]) for x in r]
        Q = [float(x["qBSeen"]) for x in r]
        a, b = ols2(R, P, Q)
        out.append((sum(Q) / len(Q), -b / a if a else float("nan")))
    print(f"{mech:6} {out[0][0]:7.3f} {out[1][0]:7.3f} {out[0][1]:9.2f} {out[1][1]:7.2f}")


print("\n--- TEMPORAL DYNAMICS (prisoners_1run, P, pop_1, noshuffle gs128) ---")
print("Transition-zone fluctuation vs stable saturated cells (qBSeen by R-P, P=0.14)")
RUN = os.path.expanduser("~/results/prisoners_1run")
mv = f"{RUN}/noshuffle_cost0.001_128/P/1/pop_1/csv_0_for_movie.con"
r = load(mv)
if r:
    from collections import defaultdict
    byc = defaultdict(list)
    for x in r:
        byc[(round(float(x["R0"]), 2), round(float(x["P0"]), 2))].append(x)
    for (R, P) in sorted(byc):
        if round(P, 2) != 0.14 or round(R - P, 2) not in (0.04, 0.08, 0.20, 0.40):
            continue
        rows = sorted(byc[(R, P)], key=lambda z: int(z["Time"]))
        qbs = [float(z["qBSeen"]) for z in rows[1:]]
        print(f"  R-P={R-P:.2f}: range={max(qbs)-min(qbs):.3f} final={qbs[-1]:.3f} "
              f"traj=[{' '.join(f'{q:.2f}' for q in qbs)}]")
else:
    print("  (movie con not found)")

print("\nDONE")
