# Snowdrift Game — Game-Specific Instructions

**Prerequisite**: Read instructions.md first for the shared simulation model.

Scope in this project:
- **mutualism** is the primary study (two populations can differ in parameters).
- **hamilton** is the equal-parameter diagonal special case of mutualism (b0 - c0 = b1 - c1).
- **prisoners** and **snowdrift** are calibration studies used to interpret mechanism signatures, not primary biological endpoints.

---

## 1. Game Parameters

For the exported snowdrift study used in this repository (graphgen --study snowdrift --figure s07), the payoff columns in csv_*_for_image.con are:

- T0 = T1 = 1.0 (constant)
- P0 = P1 = 0.1 (constant)
- R and S vary by cell with valid ordering T > R > S > P

This is a snowdrift/Hawk-Dove style sweep in (R, S) space. It is distinct from the Hamilton cost-branch formulation used in given >= 1.5 runs of other studies.

---

## 2. Payoff Form in Current Exports

For each population (pop_1, pop_2, pop_3) in the current snowdrift exports:

| Parameter | Value/range |
| --------- | ----------- |
| T       | 1.0       |
| P       | 0.1       |
| R       | 0.182 to 0.959 |
| S       | 0.141 to 0.918 |

Cell validity follows:

- T > R > S > P
- R - S > 0 (cooperator-vs-cooperator edge over cooperator-vs-defector)
- T - R > 0 (temptation still present)

---

## 3. Regime Interpretation

All valid cells in this exported grid are in a snowdrift ordering:

- T > R > S > P

So analysis focuses on how outcome metrics vary across the magnitude of:

- T - R (temptation premium)
- R - S (cost-sharing/cooperation edge)
- S - P (benefit of unilateral cooperation relative to mutual defection)

---

## 4. Results Path Pattern

~/results/{study}/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}/{population}/

For current snowdrift exports used by this repo, target path is typically:

- ~/results/snowdrift/shuffle_cost12_128/P/1.0/{population}/

Expected summary files:

- csv_0_for_image.con
- csv_1_for_image.con (for pop_2 and pop_3)

---

## 5. Data and Derived Traits

Same genotype schema/workflow as other TRPS studies:
- 6 loci -> 64 genotype columns
- derive C1P1, C0P1, C1P0, P1 from genotype sums
- do not confuse payoff parameter columns with allele frequencies

---

## 6. Analysis Workflow

1. Confirm exported payoff ordering (T > R > S > P) from csv_*_for_image.con.
2. Compute derived traits from genotypes (C1P1, C0P1, C1P0, P1).
3. Compare mechanism P against control _ to quantify partner-choice lift.
4. For pop_2/pop_3, test cooperation-vs-fitness asymmetry between file sets.
5. Use R-S and T-R trends (not PD-style R-P thresholds) to interpret gradients.
