# Parameterization (canonical reference)

This is the single source of truth for the model constants and payoff structures.
Other docs should link here rather than restate the equations; where a study doc
keeps a local payoff table for self-containedness, this file is authoritative if they
ever disagree. The constants below are regression-checked against the simulation
`.glo` metadata by `ai/verify_claims.py` (study "parameterization"), so a drift
between this doc and the data fails the verifier.

## Constants

| Constant | Value | Applies to | Source of truth |
| -------- | ----- | ---------- | --------------- |
| K (baseline fitness) | 0.5 | diagonal, mutualism, symmetric_c_i | .glo `K` |
| b (benefit) | 0.4, fixed | diagonal, mutualism, symmetric_c_i | .glo `b` |
| c (cooperation cost) | swept 0 to b | diagonal (c0 = c1), mutualism (c0 < c1) | .glo `c0`, `c1` |
| Cost (information cost) | 0.001 default; swept 0 to 0.4 in symmetric_c_i | all studies | .glo `Cost` |
| Runs | 30 (multi-run); 1 (`*_1run`) | all studies | .glo `Runs` |
| MutationRate | 0.01 | all studies | .glo `MutationRate` |

Cost is information cost for expressing machinery, charged once for any
partner-choice locus (P/Q) plus once for any reciprocity locus (M/I/J):
cost = Cost × ((Choose or Choose_lt) + (Mimic or Imimic or Imimic_lt)); fitness is
w = max(0, payoff − cost). See journal/symmetric_c_i.md for the swept-Cost study.

## Diagonal / mutualism payoffs

These two studies are parameterized by K, b, and cost. Diagonal is the equal-cost
diagonal (c0 = c1 = c); mutualism uses two costs with c0 < c1.

- PD (folder 1): T = K + b, R = K + b − c, P = K, S = K − c
- Snowdrift (folder 2): T = K + b, R = K + b − c/2, P = K, S = K + b − c

Result folders are named by dilemma type:

- **0 — control:** T = P, R = S; a partner's move does not affect the focal payoff.
  Interactive cooperation is not in the game (high qBSeen for c < b is a private
  cost–benefit outcome, not social cooperation).
- **1 — prisoner's dilemma:** T = K + b, R = K + b − c, P = K, S = K − c.
- **2 — snowdrift:** T = K + b, R = K + b − c/2, P = K, S = K + b − c.

Two-population form (mutualism): population 0 uses c0 and population 1 uses c1, with
c0 < c1 in every plotted cell, so R0 − P0 = b − c0 > R1 − P1 = b − c1 (population 0
always has the stronger cooperation incentive). Full tables in journal/symmetric_c.md
and journal/asymmetric_c0_c1.md.

Derived gaps welded onto the single cost axis (the confound the calibration sweeps
remove): temptation T − R = c, risk P − S = c, cooperation advantage R − P = b − c.

## Prisoners / snowdrift payoffs (payoff-plane sweeps)

These two calibration studies are **not** parameterized by K and b. They sweep the
raw payoff plane directly, so the `.glo` files carry T0/R0/P0/S0 (and T1/R1/P1/S1),
not K/b/c. Cell keys are payoff coordinates, not costs:

- prisoners: T = 0.9 and S = 0.1 fixed; R and P swept (T > R > P > S). Cell key
  (R0, P0). Purpose: decouple temptation, risk, and R − P.
- snowdrift: T = 0.9 and P = 0.10 fixed; R and S swept (T > R > S > P). Cell key
  (R0, S0). Purpose: confirm the low-risk (high S) attribution from the other side.

See journal/prisoners_calibration.md and journal/snowdrift_calibration.md.
