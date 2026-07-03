#!/usr/bin/env python3
"""
Analyze the new-parameterization snowdrift calibration study.

Snowdrift is a raw Snowdrift payoff-plane sweep: T = 0.9 and P = 0.1 are fixed,
while R and S are swept independently over an 18x18 grid (172 cells satisfying
T > R > S > P). Dilemma folder 2 (Snowdrift) only; symmetric payoffs across
populations; pops 1/2/3; shuffle/noshuffle; gs 128/4; Runs = 30.

Cell key is (R0, S0). T0 = 0.9, P0 = 0.1 fixed.
"""

import os
from trps_io import corr, gsum, load, ols2

SD_BASE = os.path.expanduser("~/results/snowdrift")
T_FIX, P_FIX = 0.9, 0.1

def path(sh, gs, mech, pop, fset):
    return os.path.join(SD_BASE, sh, str(gs), mech, "2", pop,
                        f"csv_{fset}_for_image.con")

MECHS = ["_", "M", "P", "MP", "MPQ", "IMP", "IJMPQ"]
SHUFFLE_ONLY = ["IM", "IJM"]

print("=" * 78)
print("SNOWDRIFT CALIBRATION (d2, T=0.9, P=0.1; R,S swept; 172 cells; Runs=30)")
print("=" * 78)

print("\n--- PAYOFF-AXIS SENSITIVITY: qBSeen ~ a*R + b*S ---")
print("a = dq/dR (reward/temptation axis); b = dq/dS (sucker/risk axis)")
print("-b/a > 1 => S-axis dominated; ~1 => tracks R-S; < 1 => R-axis dominated")
print(f"\n{'cond':22} {'mech':6} {'meanQ':>6} {'a(R)':>7} {'b(S)':>7} {'-b/a':>6} {'cR-S':>6} {'cR':>6} {'cS':>6}")
for sh in ["noshuffle", "shuffle"]:
    for gs in ["128", "4"]:
        for mech in MECHS + (SHUFFLE_ONLY if sh == "shuffle" else []):
            for pop, fset in [("pop_1", 0), ("pop_2", 0)]:
                r = load(path(sh, gs, mech, pop, fset))
                if not r:
                    continue
                R = [float(x["R0"]) for x in r]
                S = [float(x["S0"]) for x in r]
                Q = [float(x["qBSeen"]) for x in r]
                RS = [R[i] - S[i] for i in range(len(R))]
                a, b = ols2(R, S, Q)
                tag = f"{sh[:4]}_{gs}_{pop[-1]}"
                print(f"{tag:22} {mech:6} {sum(Q)/len(Q):6.3f} {a:7.3f} {b:7.3f} "
                      f"{(-b/a if a else float('nan')):6.2f} {corr(RS,Q):6.3f} {corr(R,Q):6.3f} {corr(S,Q):6.3f}")
        print()

print("\n--- PARTNER CHOICE: qBSeen collapses onto R-S (pop_1, noshuffle gs128) ---")
r = load(path("noshuffle", "128", "P", "pop_1", 0))
if r:
    bins = {}
    for x in r:
        rs = round(float(x["R0"]) - float(x["S0"]), 2)
        bins.setdefault(rs, []).append(float(x["qBSeen"]))
    print(f"{'R-S':>5} {'n':>3} {'meanQ':>6} {'min':>6} {'max':>6} {'spread':>6}")
    for rs in sorted(bins):
        v = bins[rs]
        print(f"{rs:5.2f} {len(v):3} {sum(v)/len(v):6.3f} {min(v):6.3f} {max(v):6.3f} {max(v)-min(v):6.3f}")

print("\n--- P GENOTYPES along R-S (pop_1, noshuffle gs128): C1P1/C1P0/C0P1 ---")
if r:
    print(f"{'R-S':>5} {'qB':>6} {'C1P1':>6} {'C1P0':>6} {'C0P1':>6}")
    rows = sorted(r, key=lambda x: float(x["R0"]) - float(x["S0"]))
    seen = set()
    for x in rows:
        rs = round(float(x["R0"]) - float(x["S0"]), 2)
        if rs in seen:
            continue
        seen.add(rs)
        print(f"{rs:5.2f} {float(x['qBSeen']):6.3f} {gsum(x,'1','1'):6.3f} "
              f"{gsum(x,'1','0'):6.3f} {gsum(x,'0','1'):6.3f}")

print("\n--- POP_2 SYMMETRY BREAKING (P, noshuffle gs128): fset_0 vs fset_1 ---")
r0 = load(path("noshuffle", "128", "P", "pop_2", 0))
r1 = load(path("noshuffle", "128", "P", "pop_2", 1))
if r0 and r1:
    m1 = {(x["R0"], x["S0"]): x for x in r1}
    print(f"{'R':>5} {'S':>5} {'R-S':>5} {'qB_0':>6} {'qB_1':>6} {'dqB':>6} {'w_0':>6} {'w_1':>6}")
    for x in sorted(r0, key=lambda z: (float(z["S0"]), float(z["R0"]))):
        k = (x["R0"], x["S0"])
        if k not in m1:
            continue
        y = m1[k]
        R = float(x["R0"]); S = float(x["S0"])
        if round(S, 2) != 0.14:  # one S-row slice for brevity
            continue
        q0 = float(x["qBSeen"]); q1 = float(y["qBSeen"])
        print(f"{R:5.2f} {S:5.2f} {R-S:5.2f} {q0:6.3f} {q1:6.3f} {q0-q1:+6.3f} "
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

print("\n--- M MECHANISM: risk (S) sensitivity detail (pop_1, noshuffle gs128) ---")
r = load(path("noshuffle", "128", "M", "pop_1", 0))
if r:
    print("qBSeen at fixed R=0.50 as S rises (risk decreases / sucker payoff increases):")
    for x in sorted(r, key=lambda z: float(z["S0"])):
        if abs(float(x["R0"]) - 0.50) < 1e-6:
            print(f"  S={float(x['S0']):.2f} (S-P={float(x['S0'])-P_FIX:.2f}): qBSeen={float(x['qBSeen']):.3f}")

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
    if r:
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
        S = [float(x["S0"]) for x in r]
        Q = [float(x["qBSeen"]) for x in r]
        a, b = ols2(R, S, Q)
        out.append((sum(Q) / len(Q), -b / a if a else float("nan")))
    print(f"{mech:6} {out[0][0]:7.3f} {out[1][0]:7.3f} {out[0][1]:9.2f} {out[1][1]:7.2f}")

print("\n--- TEMPORAL DYNAMICS (snowdrift_1run, P, pop_1, noshuffle gs128) ---")
RUN = os.path.expanduser("~/results/snowdrift_1run")
mv = f"{RUN}/noshuffle/128/P/2/pop_1/csv_0_for_movie.con"
r = load(mv)
if r:
    from collections import defaultdict
    byc = defaultdict(list)
    for x in r:
        byc[(round(float(x["R0"]), 2), round(float(x["S0"]), 2))].append(x)
    for (R, S) in sorted(byc):
        if round(S, 2) != 0.14 or round(R - S, 2) not in (0.04, 0.08, 0.20, 0.40):
            continue
        rows = sorted(byc[(R, S)], key=lambda z: int(z["Time"]))
        qbs = [float(z["qBSeen"]) for z in rows[1:]]
        print(f"  R-S={R-S:.2f}: range={max(qbs)-min(qbs):.3f} final={qbs[-1]:.3f} "
              f"traj=[{' '.join(f'{q:.2f}' for q in qbs)}]")
else:
    print("  (movie con not found)")

print("\nDONE")
