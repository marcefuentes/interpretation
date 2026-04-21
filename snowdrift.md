# Interpretation of Snowdrift Partner Choice Results

## Overview

This document is the analysis workspace for the snowdrift study, following the same reporting structure used in prisoners.md.

Primary objective:
- characterize cooperation, chooser dynamics, and exploitation patterns under snowdrift payoff construction

---

## Study Status

- [x] Confirm exact payoff equations from ~/code/trps/code/src/modules/calculate_derived_globals.c
- [ ] Verify parameter grid and valid-cell constraints
- [ ] Map panel/population correspondence for figure s07
- [ ] Compute core derived traits (C1P1, C0P1, C1P0, P1)
- [ ] Draft full interpretation sections (pop_1, pop_2, pop_3 if present)

---

## Payoff Setup (given >= 1.5 branch)

From calculate_derived_globals.c (hamilton branch, snowdrift mode):

- c_i = k1 - b_c_i
- T_i = k0 + k1
- R_i = k0 + k1 - c_i/2
- P_i = k0
- S_i = k0 + k1 - c_i

With k0 = 2, k1 = 1, and x_i = b_c_i:
- T_i = 3
- R_i = 2.5 + 0.5x_i
- P_i = 2
- S_i = 2 + x_i

Local ordering for each population:
- x_i < 1: T_i > R_i > S_i > P_i
- x_i = 1: T_i = R_i = S_i > P_i
- x_i > 1: S_i > R_i > T_i > P_i

---

## Notes

Snowdrift payoffs are **not** the same as prisoners payoffs. Any claim about game regime boundaries must be derived from the source equations before interpretation.

Current data status:
- ~/results/snowdrift/ is present but currently has no CSV outputs in this environment.
- Snowdrift-variant numeric summaries in this repo are therefore being bootstrapped from given = 1.5 runs under hamilton and mutualism, which use the same source payoff branch (given >= 1.5).
