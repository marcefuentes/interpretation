# Hamilton

Analysis for the equal-cost diagonal of the mutualism parameter space (c0 = c1 =
c), split by mechanism family:

- **[hamilton_partner_choice.md](hamilton_partner_choice.md)** — mechanism P:
  PD and snowdrift cooperation profiles, P1 hitchhiking, population-structure
  contrasts (pop_1, pop_2, pop_3), groupsize effects on partner choice
- **[hamilton_reciprocity.md](hamilton_reciprocity.md)** — mechanisms M, IM,
  IJM: shuffle effects, IJM groupsize reversal, direct vs indirect reciprocity
- **[hamilton_combined.md](hamilton_combined.md)** — mechanisms MP, MPQ, IMP,
  IJMPQ: mechanism hierarchy, IJMPQ symmetry suppression, groupsize effects

For asymmetric costs (c0 ≠ c1), see **mutualism.md**.

## Game parameters

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

Folder 0 (given=0): T = P and R = S — partner moves do not affect focal
payoffs. High qBSeen for c < b is a private cost–benefit outcome, not social
cooperation.
