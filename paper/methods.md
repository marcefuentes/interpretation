# Methods

*Draft scaffold. Backing: [parameterization.md](../journal/parameterization.md),
[framework.md](../journal/framework.md); replicate/noise detail in
[symmetric_c.md](../journal/symmetric_c.md) and [asymmetric_c0_c1.md](../journal/asymmetric_c0_c1.md).*

## Model

Individuals interact in pairs over repeated rounds and reproduce in proportion to
accumulated fitness. Each carries a cooperation locus (C) and a set of mechanism loci
that gate conditional behaviour: partner choice on recent or lifetime cooperation
(P/Q), and reciprocity that copies a partner's behaviour directly, indirectly from a
third party, or from a lifetime reputation (M/I/J). Per round, fitness is the game
payoff minus a machinery cost, w = max(0, payoff − cost) (see Information cost).

The behavioural update and locus semantics are validated against the simulation
source; the confirmed mechanics (decision precedence J > I > M, the C0P1 silent
carrier, the dTFT/dSTFT split) are recorded in `ai/findings.md` and
`.github/copilot-instructions.md`.

## Social dilemmas (payoff structures)

With baseline fitness K = 0.5 and benefit b = 0.4 fixed, the cooperation cost c is
swept from 0 to b. The dilemma folders are:

- **0 — control:** T = P and R = S; a partner's move does not affect the focal
  payoff (no social dilemma).
- **1 — prisoner's dilemma:** T = K + b, R = K + b − c, P = K, S = K − c.
- **2 — snowdrift:** T = K + b, R = K + b − c/2, P = K, S = K + b − c.

Exact tables, including the two-population form, are in
[parameterization.md](../journal/parameterization.md),
[symmetric_c.md](../journal/symmetric_c.md), and [asymmetric_c0_c1.md](../journal/asymmetric_c0_c1.md).

## Independent variables

The design grid (detailed in [framework.md](../journal/framework.md)): social dilemma
(control / PD / snowdrift); cooperation cost c (two costs c0, c1 in the two-population
case); information cost Cost; group size (4 vs 128); partner shuffling (stable vs
re-drawn each round); population structure (pop_1 single, pop_2 two coevolving, pop_3
evolving-vs-fixed); and mechanism (_, M, P, MP, MPQ, IMP, IJMPQ, and shuffle-only IM,
IJM).

## Studies

- **asymmetric_c0_c1** (primary): two coevolving populations, a 2D upper-triangular sweep of
  c0 < c1 (210 cells), dilemmas 1/2, both group sizes, shuffle/noshuffle.
- **symmetric_c**: the equal-cost diagonal (c0 = c1), pop_1/2/3, dilemmas 0/1/2.
- **symmetric_c_Cost**: adds the information-cost axis, sweeping Cost jointly with c on a
  triangular grid (Cost + c ≤ b).
- **prisoners** and **snowdrift**: payoff-plane calibration sweeps that hold two
  payoffs fixed and vary the other two, decoupling temptation, risk, and the
  cooperation advantage R − P that a single cost axis welds together.
- **\*_1run** variants: single realisations for temporal inspection (limited by coarse
  snapshot spacing; see [framework.md](../journal/framework.md) on why oscillation is
  left as an open question rather than a measured outcome).

## Outcome measures

Cooperation level is qBSeen (frequency of cooperative acts); fitness is wmean;
genotype composition is read from the per-genotype frequency columns (e.g. C1P1,
C1P0, C0P1, C1M1, C1M0). Between-population asymmetry is the qBSeen gap (cooperation)
and the wmean gap (exploitation) between file sets _0 and _1.

## Replicates, noise floor, and verification

Main-study values are means over 30 independent runs, with a companion SD column per
statistic. The practical noise floor is qBSeen gaps below ~0.01–0.02 and fitness gaps
below ~0.002; SD peaks in bistable transition cells (details in
[symmetric_c.md](../journal/symmetric_c.md) and [asymmetric_c0_c1.md](../journal/asymmetric_c0_c1.md)).
Every headline number in the journal is regression-checked against the exported data
by `ai/verify_claims.py`, which is run before any documentation edit that changes a
number.
