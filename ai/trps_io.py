#!/usr/bin/env python3
"""
Shared helpers for the TRPS analysis/verification scripts.

Centralizes .con loading, statistics (correlation, 2-variable OLS), and
genotype-frequency sums so analyze_*.py and verify_claims.py stay in sync.

Data convention: .con rows are dicts keyed by column name. Genotype columns are
the 12-char names C0I0J0M0P0Q0 ... C1I1J1M1P1Q1 (each with a matching *SD
column); game-parameter columns are c0/c1 (symmetric_c, asymmetric_c0_c1) or
T0/R0/P0/S0 (prisoners, snowdrift).
"""

import csv
import math
import os

BASE = os.path.expanduser("~/results")


def load(path):
    """Read a .con file into a list of dict rows, or None if absent."""
    return list(csv.DictReader(open(path))) if os.path.exists(path) else None


def glo(path):
    """Read a two-column `.glo` metadata file into a {key: value} dict (values as
    strings), or None if absent. Keys include K, b, Cost, Runs, Dilemma, GroupSize,
    Shuffle (symmetric_c/asymmetric_c0_c1), and T0/R0/P0/S0 (prisoners/snowdrift)."""
    if not os.path.exists(path):
        return None
    out = {}
    for row in csv.reader(open(path)):
        if len(row) >= 2:
            out[row[0]] = row[1]
    return out


def any_glo(dirpath):
    """Return the parsed metadata of the first `.glo` file found under dirpath, or
    None. Used to assert study-wide constants that are identical across cells."""
    if not os.path.isdir(dirpath):
        return None
    for name in sorted(os.listdir(dirpath)):
        if name.endswith(".glo"):
            return glo(os.path.join(dirpath, name))
    return None


def corr(xs, ys):
    """Pearson correlation; nan if undefined."""
    n = len(xs)
    if n < 2:
        return float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    return num / (dx * dy) if dx * dy else float("nan")


def ols2(R, P, Q):
    """Least squares Q ~ a*R + b*P + const. Returns (a, b)."""
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


def genotype_cols(row, c=None, p=None):
    """12-char genotype columns (no SD), optionally filtered by C{c} and P{p}."""
    cols = [k for k in row if not k.endswith("SD") and len(k) == 12 and k[0] == "C"]
    if c is not None:
        cols = [x for x in cols if x.startswith(f"C{c}")]
    if p is not None:
        cols = [x for x in cols if f"P{p}" in x]
    return cols


def gsum(row, c=None, p=None):
    """Summed genotype frequency over the matching columns."""
    return sum(float(row[x]) for x in genotype_cols(row, c, p))


def allele(row, *tokens):
    """Summed frequency over genotype columns containing every token.

    Tokens are locus-state strings like "M1", "J1", "C0". allele(row, "C1",
    "M0") is the frequency of always-cooperate (C1, M0) genotypes.
    """
    cols = [k for k in row if not k.endswith("SD") and len(k) == 12 and k[0] == "C"
            and all(t in k for t in tokens)]
    return sum(float(row[x]) for x in cols)


def m1sum(row):
    """M1 allele frequency = sum of all genotype columns containing M1."""
    return allele(row, "M1")
