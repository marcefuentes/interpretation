# Snowdrift Game — Game-Specific Instructions

**Prerequisite**: Read instructions.md first for the shared simulation model.

---

## 1. Game Parameters

The snowdrift payoff construction is activated in calculate_derived_globals.c when:

- globals->hamilton == 1
- globals->given >= 1.5

In this branch, b_c_0 and b_c_1 are treated as **cost-encoded parameters**, not the Hamilton benefit-minus-cost values used for given < 1.5.

---

## 2. Payoff Equations (given >= 1.5)

Source: ~/code/trps/code/src/modules/calculate_derived_globals.c (else branch under if (globals->given < 1.5)).

Definitions:
- c0 = k1 - b_c_0
- c1 = k1 - b_c_1

Population-specific payoffs:

| Population | T                 | R                        | P    | S                    |
| ---------- | ----------------- | ------------------------ | ---- | -------------------- |
| pop_0      | k0 + k1         | k0 + k1 - c0/2         | k0 | k0 + k1 - c0       |
| pop_1      | k0 + k1         | k0 + k1 - c1/2         | k0 | k0 + k1 - c1       |

Equivalent gap form:

| Population | T - R | R - S | S - P | R - P   |
| ---------- | ------- | ------- | ------- | --------- |
| pop_0      | c0/2  | c0/2  | k1-c0 | k1-c0/2 |
| pop_1      | c1/2  | c1/2  | k1-c1 | k1-c1/2 |

With study constants k0 = 2, k1 = 1, and x_i = b_c_i:
- c_i = 1 - x_i
- T_i = 3
- R_i = 2.5 + 0.5x_i
- P_i = 2
- S_i = 2 + x_i

---

## 3. Regime Split by Local x = b_c

For each population independently:

- x < 1: T > R > S > P (Snowdrift/Hawk-Dove ordering)
- x = 1: T = R = S > P (boundary)
- x > 1: S > R > T > P (post-boundary ordering with high S)

Important: this differs from both:
- prisoners (T/S fixed, R/P varied directly), and
- Hamilton/mutualism given < 1.5 branch (benefit/cross-benefit formulation).

---

## 4. Results Path Pattern

~/results/{study}/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}/{population}/

For snowdrift variants here, target given_val = 1.5.

---

## 5. Data and Derived Traits

Same genotype schema/workflow as other TRPS studies:
- 6 loci -> 64 genotype columns
- derive C1P1, C0P1, C1P0, P1 from genotype sums
- do not confuse payoff parameter columns with allele frequencies

---

## 6. Analysis Workflow

1. Compute local payoff ordering per cell using equations above.
2. Build regime maps (counts by ordering, per population).
3. Test expected signatures in qBSeen, wmean, and genotype splits.
4. Validate with movie snapshots when dynamic claims are made.
