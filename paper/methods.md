# Methods

*Draft scaffold. Backing: [parameterization](../journal/parameterization.md),
[framework](../journal/framework.md); replicate and noise-floor detail in the journal
(regression-checked by ai/verify_claims.py).*

## Model

Individuals interact in pairs over repeated rounds and reproduce in proportion to
accumulated fitness. Each carries a cooperation locus (C) and a set of mechanism loci
that gate conditional behaviour: partner choice on recent or lifetime cooperation
(P/Q), and reciprocity that copies a partner's behaviour directly, indirectly from a
third party, or from a lifetime reputation (M/I/J). Per round, fitness is the game
payoff minus information cost, w = max(0, payoff − cost) (see Information cost).

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
[parameterization](../journal/parameterization.md) and the journal payoffs docs.

## Independent variables

The design grid (detailed in [framework](../journal/framework.md)): social dilemma
(control / PD / snowdrift); cooperation cost c (two costs c0, c1 in the two-population
case); information cost (including per-population i0 and i1 in the two-population
case); group size (4 vs 128); partner shuffling (stable vs re-drawn each round);
population structure
(one coevolving population, two coevolving populations, or an evolving-vs-fixed
control); and mechanism (_, M, P, MP, MPQ, IMP, IJMPQ, and shuffle-only IM, IJM).

## Simulation sweeps

The headline sweeps are:

1. **Cooperation cost, equal between populations** — single population and two
   coevolving populations; c0 = c1; dilemmas 0/1/2; the baseline hierarchy and
   stochastic two-population split.
2. **Cooperation cost, unequal between populations** — two coevolving populations;
   upper-triangular c0 < c1 (210 cells); dilemmas 1/2; deterministic role split.
3. **Information cost and cooperation cost, equal between populations** — triangular
   information cost × cooperation cost grid (i + c ≤ b); adds the information-cost
   axis to the baseline.
4. **Information cost under fixed cooperation-cost asymmetry** — c0 fixed at 0.10,
   information cost swept jointly with c1 (i + c1 ≤ b).
5. **Per-population information cost at symmetric cooperation cost** — c0 = c1,
   strict triangle i0 < i1 (per-axis cap b − c).
6. **Both costs asymmetric** — c0 = 0.10, c1 = 0.20 fixed; full i0 × i1 square
   (176 cells).

Auxiliary **payoff-plane calibration sweeps** hold two payoffs fixed and vary the
other two, decoupling temptation, risk, and the cooperation advantage R − P that a
single cooperation-cost axis welds together. These support attribution in the main
text but are not primary result figures.

**Single-run companions** (nine snapshots from t = 131072 to 10⁶) provide temporal
inspection: coarse spacing is sufficient to confirm early lock-in of role splits but
not sub-establishment ordering ([framework](../journal/framework.md)).

## Outcome measures

Cooperation level is qBSeen (frequency of cooperative acts); fitness is wmean;
genotype composition is read from the per-genotype frequency columns (e.g. C1P1,
C1P0, C0P1, C1M1, C1M0). **Between-population asymmetry** is the qBSeen gap
(cooperation) and the wmean gap (exploitation) between the two coevolving populations —
an **outcome** variable, distinct from **parameter** symmetry or asymmetry in c0, c1,
i0, i1, and payoffs.

## Replicates, noise floor, and verification

Main-study values are means over 30 independent runs, with a companion SD column per
statistic. The practical noise floor is qBSeen gaps below ~0.01–0.02 and fitness gaps
below ~0.002; SD peaks in bistable transition cells (details in the journal baseline
docs). Every headline number in the journal is regression-checked against the exported
data by `ai/verify_claims.py`, which is run before any documentation edit that
changes a number.
