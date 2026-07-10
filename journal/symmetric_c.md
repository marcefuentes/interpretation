# symmetric_c

Analysis for symmetric_c (equal-cost, c0 = c1) of the two-population parameter space (c0 = c1 =
c), split by mechanism family:

- **[symmetric_c_partner_choice.md](symmetric_c_partner_choice.md)** — mechanism P:
  PD and snowdrift cooperation profiles, P1 hitchhiking, population-structure
  contrasts (pop_1, pop_2, pop_3), groupsize effects on partner choice
- **[symmetric_c_reciprocity.md](symmetric_c_reciprocity.md)** — mechanisms M, IM,
  IJM: shuffle effects, IJM groupsize reversal, direct vs indirect reciprocity
- **[symmetric_c_combined.md](symmetric_c_combined.md)** — mechanisms MP, MPQ, IMP,
  IJMPQ: mechanism hierarchy, IJMPQ symmetry suppression, groupsize effects
- **[symmetric_c_i.md](symmetric_c_i.md)** — the information-cost extension:
  Cost (information cost on carrying the machinery) swept jointly with c, and
  how rising information cost interacts with rising cooperation cost

For asymmetric costs (c0 ≠ c1), see **asymmetric_c0_c1.md**. For which payoff gap
(temptation, risk, or R − P) drives each mechanism's c-collapse, and how the
information-cost axis fits, see **[synthesis.md](synthesis.md)**.

## Game parameters

Canonical constants and payoff equations live in
**[parameterization.md](parameterization.md)** (verified against `.glo` metadata);
the tables below are the local, self-contained copy for this study.

| Parameter | Value         | Description                              |
| --------- | ------------- | ---------------------------------------- |
| b         | 0.40          | Benefit (fixed)                          |
| c         | 0.00 – 0.40   | Cost (x-axis; 21 values in steps of 0.02) |
| K         | 0.50          | Baseline fitness (T and P floor)         |
| groupsize | 4 and 128     | Individuals per group from each population |

### Payoff structure (dilemmas 1 and 2)

| Folder | Dilemma    | T        | R          | P    | S          | R - P  |
| ------ | ---------- | -------- | ---------- | ---- | ---------- | ------ |
| 1      | PD         | K+b=0.90 | K+b-c      | 0.50 | K-c        | b-c    |
| 2      | Snowdrift  | K+b=0.90 | K+b-c/2    | 0.50 | K+b-c      | b-c/2  |

At c = 0: T = R for dilemmas 1 and 2 — no temptation to defect. For PD,
T − R = c increases with c; at c = 0.40, R − P = 0. For snowdrift, S > P
for all c < 0.40.

Folder 0 (control): T = P and R = S — partner moves do not affect focal
payoffs. High qBSeen for c < b is a private cost–benefit outcome, not social
cooperation.

## Replicates and noise floor

Every value in these write-ups is a mean over 30 independent simulation runs
(Runs = 30 in the .glo metadata). The csv_*_for_image.con files carry a
companion SD column for each statistic (qBSeenSD, wmeanSD, …) giving the
standard deviation across those 30 runs; the standard error of a cell mean is
SD / √30.

Typical noise floor (gs=128, PD): median wmeanSD ≈ 0.001 (control) to 0.010
(M), i.e. SE ≈ 0.0002–0.002; median qBSeenSD ≈ 0.007 (control) to 0.037 (P),
i.e. SE ≈ 0.001–0.007. SD peaks in the transition zones (max wmeanSD ≈
0.07–0.10) where individual runs split between a cooperative and a collapsed
fixed point, so multi-run means there reflect a mix of bistable outcomes
rather than a single equilibrium (see the single-run dynamics sections).

Practical reading guide: fitness (wmean) gaps below ~0.002 and qBSeen gaps
below ~0.01–0.02 are within run-to-run noise. Statements like "near the noise
floor" or "negligible" in the analysis docs refer to differences at or below
these magnitudes.
