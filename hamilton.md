# Interpretation of Hamilton Partner Choice Results

## Overview

This document summarizes Hamilton-specific results from `graphgen --study hamilton --figure s07` (partner choice under mechanism **P** only: **no** direct or indirect reciprocity). It covers pop_1 (panels e-f, single population), pop_2 (panels a-b, two coevolving populations), and pop_3 (panels c-d, one population adapting to a fixed population).

Use **mutualism.md** as the conceptual starting point. Hamilton is the **diagonal special case** of that 2D space:

- *b*₀ − *c*₀ = *b*₁ − *c*₁

So this file focuses on what is specific to the diagonal slice (1D trends, onset shapes, and structure-specific contrasts), while shared mechanism logic (cross-benefit framing and chooser bottleneck) is defined in **mutualism.md**.

**Individual vs population qBSeen.** In the simulation output and figures, **qBSeen denotes the population fraction of cooperators** (C1P1 + C1P0). At the individual level, mechanism **P** does not update reputation: defectors have qBSeen = 0 and cooperators have qBSeen = 1 for their entire life. Partner choice therefore only ever reads a **binary** partner type (defector vs cooperator), not a graded image score.

Later sections emphasize **tables, correlations, and single-run statistics**. Shared mechanism details are documented in **mutualism.md**; only Hamilton-specific empirical patterns are expanded here.

## Document structure by given

This single file keeps all Hamilton interpretations together:

- **Given = 1.0 (PD family, benefit branch)**: main Hamilton results across pop_1/pop_2/pop_3.
- **Given = 0.5 (mixed PD/harmony along diagonal, benefit branch)**: see **Given = 0.5: Game-Type Classification** and **Why g = 0.5 Helps Interpret g = 1.0**.
- **Given = 1.5 (snowdrift branch)**: see **Given = 1.5: Snowdrift-Branch Interpretation**.

## Game parameters and payoff structure

On the diagonal constraint (*b*₀ − *c*₀ = *b*₁ − *c*₁), Hamilton reduces the mutualism grid to one control axis (*b* − *c*). With *g* = 1.0 (full dilemma), a cooperator gives all of its production *b* to its partner and pays cost *c*. The simulation parameters are:

| Parameter      | Value                         | Description                                | In calculate_derived_globals.c |
| -------------- | ----------------------------- | ------------------------------------------ | ------------------------------ |
| *b* − *c*          | 0.008 – 8.0 (log scale)       | Net benefit of mutual cooperation          |                                |
| *c*              | 1.0                           | Cost (fixed throughout; C_MIN)             | k1                             |
| *b*              | *c* + (*b* − *c*) = 1.008–9.0       | Benefit (varies with *b* − *c*)                |                                |
| *g*              | 1.0                           | Given parameter (full dilemma)             |                                |
| *K*              | 2.0                           | Baseline fitness                           | k0                             |
| *B*\_max         | 9.0                           | Maximum benefit (normalization)            |                                |
| groupsize      | 128                           | Individuals per group from each population |                                |

From calculate_derived_globals.c, the Hamilton game at *g* = 1.0 maps exactly to a Prisoner's Dilemma with payoffs:

| Payoff         | Formula          | Meaning                         | In calculate_derived_globals.c |
| ---------------| ---------------- | ------------------------------- | ------------------------------ |
| **T** (Temptation) | 3 + (*b* − *c*)      | Defect while partner cooperates | k0 + k1 + (*b* − *c*)              |
| **R** (Reward)     | 2 + (*b* − *c*)      | Both cooperate                  | k0 + (*b* − *c*)                   |
| **P** (Punishment) | 2                | Both defect                     | k0                             |
| **S** (Sucker)     | 1                | Cooperate while partner defects | k0 - k1                        |

Values at selected *b* − *c* points:

| *b* − *c*     | **T**      | **R**      | **P**   | **S**   |
| ----------| ------ | ------ | --- | --- |
| 0.008     | 3.008  | 2.008  | 2   | 1   |
| 0.125     | 3.125  | 2.125  | 2   | 1   |
| 0.250     | 3.250  | 2.250  | 2   | 1   |
| 1.000     | 4.000  | 3.000  | 2   | 1   |
| 4.000     | 7.000  | 6.000  | 2   | 1   |
| 8.000     | 11.000 | 10.000 | 2   | 1   |

### Comparison with the PD study parameter space

In the PD study (prisoners), **T** = 1.0 and **S** = 0.1 are fixed while **R** and **P** vary across a 2D grid (**R**, **P** ∈ [0.1, 1.0]). Three independent gaps vary simultaneously:

The key relationships are:

| Relationship | Hamilton  | Prisoners   | Interpretation                 |
| -------------| --------- | ----------- | ------------------------------ |
| **R − P**        | *b* − *c*     | [−0.9, 0.9] | Cooperation benefit            |
| **T − R**        | 1         | [0, 0.9]    | Temptation premium             |
| **P − S**        | 1         | [0, 0.9]    | Sucker penalty                 |

In Hamilton, **R − P spans a much wider range** (0.008 to 8.0 vs PD's −0.9 to 0.9). At high *b* − *c*, mutual cooperation is enormously more profitable than mutual defection.

Fitness is normalized as (*K* + *w*) / (*K* + *B*\_max) = (*K* + *w*) / 11. Without any cooperation mechanisms, the theoretical prediction at *g* = 1.0 is zero cooperation: the condition (1−*g*)·*b* > *c* is never satisfied. Partner choice must bootstrap cooperation from scratch.

## Minimal notation for this file

| Term   | Definition                                                            |
| ------ | --------------------------------------------------------------------- |
| C1P1   | Cooperators who choose partners ("Choosers")                          |
| C0P1   | Defectors carrying P1 (P1 is **silent** — they don't actually choose)     |
| C1P0   | Cooperators who don't choose partners ("non-chooser cooperators")     |
| P1     | Total frequency of P1 allele = C0P1 + C1P1                            |
| qBSeen | **In tables and figures:** population cooperation rate (= C1P1 + C1P0).   |
| AllC   | Frequency of C1P0 (cooperators without partner choice)                |
| w̄      | Normalized mean fitness                                               |

For swap eligibility and bottleneck mechanics (`choose_partner.c` behavior, C1P1-only swap pool, and behavioral C1P0 free-riding), use **mutualism.md** as the canonical mechanism reference.

## Single Population (pop_1, panels e-f)

### Cooperation is sustained even at tiny *b* − *c*

In pop_1 (within-population pairing), cooperation is present from the lowest *b* − *c* values and rises monotonically:

| *b* − *c*     | qBSeen | P1    | C1P1  | C1P0  | C1P0/qBSeen |
| ----------| ------ | ----- | ----- | ----- | ----------- |
| 0.008     | 0.132  | 0.585 | 0.120 | 0.012 | 9%          |
| 0.063     | 0.380  | 0.724 | 0.360 | 0.021 | 5%          |
| 0.250     | 0.801  | 0.887 | 0.727 | 0.074 | 9%          |
| 0.500     | 0.894  | 0.854 | 0.772 | 0.122 | 14%         |
| 1.000     | 0.936  | 0.806 | 0.756 | 0.180 | 19%         |
| 4.000     | 0.970  | 0.697 | 0.677 | 0.293 | 30%         |
| 8.000     | 0.973  | 0.674 | 0.656 | 0.317 | 33%         |

At *b* − *c* = 0.008, 13.2% of the population cooperates — far above pop_2 (4.5%) or pop_3 (3.6%) at the same axis value. **Within-population pairing** means both interaction partners are drawn from the **same** population (well-mixed—no geography); swap counterparts are just **other individuals in that pool**. Two eligible **C1P1** there suffice even at the lowest *b* − *c*.

### C1P0 share rises at high *b* − *c* (choosers can be few but are not optional)

Conceptually: partner choice still underwrites the pool; at high *b* − *c* a **thin C1P1 layer** can support many **C1P0** (sparse choosers). Quantitatively: C1P0/qBSeen rises from **9%** (*b* − *c* = 0.25) to **33%** (*b* − *c* = 8.0); **P1** allele frequency falls because **P0** spreads among cooperators, not because sorting switches off.

**Single-run (hamilton_1run, pop_1, shuffle_cost12_128, P, given = 1.0, 9 timesteps/cell):** **C1P1** and **C1P0** move opposite in most adjacent pairs; with **qBSeen** ~flat at high *b* − *c*, anti-phase is **mostly** **C1P1 + C1P0 = qBSeen**, plus **P0**/**P1** turnover among cooperators.

**Groupsize 4 vs 128 (hamilton_1run, same 21 cells, movie csv_0_for_movie.con, pop_1):** **shuffle_cost12_4** yields **narrow, nearly flat qBSeen trajectories** across the nine snapshots—typical within-cell range **~0.07** vs **~0.67** at **shuffle_cost12_128**, with **large last-interval moves rare at 4 (~5% of cells vs ~62% at 128)**—so **groupsize 4** matches **low end-state cooperation** as a **different regime**, not **128 slowed down**.

**Invasion vs late tail (partition timesteps within each cell):** **Invasion** (first three Δ after *t* = 1): **r**(C0, ΔP1) ≈ **+0.71**, **r**(C0, ΔC0) ≈ **−0.62**; high C0 at *t* pairs with large positive **ΔP1** and negative **ΔC0**. **Late** (*t* index ≥ 3): **r**(C0, ΔP1) ≈ **+0.08** — tiny stepwise Δ’s; **no** reliable one-step **P1** ↔ **P0** cycle at nine snapshots (longer period, smaller amplitude, or both). Sharper tail inference: **many replicates** at fixed *b* − *c* and/or **dense checkpoints only near run end** (limits CSV growth vs uniform dense output). High **C1P0**/qBSeen at *t* → slightly positive mean next-step Δ(C1P1/qBSeen) (**suggestive**).

**P1 down at high *b* − *c***: dilution by **C1P0**, not loss of partner choice as the sustaining process.

## P1 Hitchhiking

### The pattern

P1 frequency peaks at a *lower* *b* − *c* than C1P1 frequency. This occurs in all three population structures:

| Population       | P1 max *b* − *c*     | P1    | C1P1 max *b* − *c*     | C1P1  |
| ---------------- | ---------------- | ----- | ------------------ | ----- |
| pop_1            | 0.25             | 0.887 | 0.50               | 0.772 |
| pop_2 (fset_0)   | 2.00             | 0.893 | 5.66               | 0.769 |
| pop_3 (evolving) | 2.00             | 0.858 | 4.00               | 0.736 |

### The mechanism

This is the same neutral hitchhiking observed in the Prisoner's Dilemma analysis. The P1 allele is phenotypically silent in defectors: C0P1 individuals carry P1 but never activate partner choice. The P1 maximum occurs where:

1. C1P1 is still high (partner choice is still under positive selection among cooperators)
2. Enough defectors persist (C0 is present to serve as neutral P1 carriers)
3. Mutation from C1P1 → C0P1 creates a reservoir of neutral P1 carriers

At the P1 maximum in pop_1 (*b* − *c* = 0.25):
- C1P1 = 0.727 (high — cooperation is well-established)
- C0P1 = 0.160 (substantial — 16% of the population are defectors carrying P1)
- P1 = 0.887

At the C1P1 maximum (*b* − *c* = 0.50):
- C1P1 = 0.772 (highest)
- C0P1 = 0.082 (low — defection is suppressed)
- P1 = 0.854 (lower than at *b* − *c* = 0.25)

As *b* − *c* increases from the P1 max:
- C1P1 increases slowly (0.727 → 0.772, Δ = +0.044)
- C0P1 decreases faster (0.160 → 0.082, Δ = -0.078)

The net effect: P1 = C1P1 + C0P1 **decreases** because the loss of neutral carriers outpaces the gain in selected carriers.

### Why the P1 max shifts across population structures

In pop_1, the P1 maximum occurs at *b* − *c* = 0.25 — very early in the *b* − *c* range, because cooperation takes hold at low *b* − *c* in single populations. In pop_2 and pop_3, the P1 maximum shifts to *b* − *c* ≈ 2.0 because cooperation requires higher *b* − *c* to establish in between-population pairing. The P1 peak always occurs in the transition zone where C1P1 is abundant but defection has not yet been fully suppressed.

## Two Coevolving Populations (pop_2, panels a-b)

### Emergent asymmetry

Two symmetric populations spontaneously break symmetry as *b* − *c* increases. One becomes the **cooperator** population (fset_0, orange) and the other the **defector** population (fset_1, red):

| *b* − *c*     | qBSeen_0 | qBSeen_1 | ΔqBSeen  | w̄_0    | w̄_1    | Δw̄     |
| --------- | -------- | -------- | -------- | ------ | ------ | ------ |
| 0.008     | 0.045    | 0.039    | +0.006   | 0.181  | 0.182  | −0.001 |
| 0.177     | 0.376    | 0.355    | +0.020   | 0.186  | 0.190  | −0.004 |
| 0.500     | 0.610    | 0.459    | +0.151   | 0.189  | 0.223  | −0.034 |
| 1.000     | 0.652    | 0.362    | +0.290   | 0.188  | 0.267  | −0.079 |
| 2.000     | 0.767    | 0.310    | +0.457   | 0.197  | 0.363  | −0.166 |
| 4.000     | 0.845    | 0.241    | +0.604   | 0.215  | 0.544  | −0.330 |
| 8.000     | 0.926    | 0.197    | +0.729   | 0.259  | 0.922  | −0.663 |

Correlation between ΔqBSeen and Δfitness: **-0.92**

### The exploitation pattern

At *b* − *c* = 8.0:
- The cooperative population (fset_0) has qBSeen = 0.926 but fitness = 0.259
- The defecting population (fset_1) has qBSeen = 0.197 but fitness = 0.922
- The defecting population has **3.56× higher fitness**

The cooperative population pays costs to benefit the defecting population's individuals, who receive benefits without paying. Partner choice hits the same counterpart bottleneck described in **mutualism.md**: swaps need **counterpart C1P1**; the defecting population contributes few **choosers**, so mismatches persist.

In unnormalized terms at *b* − *c* = 8.0:
- fset_0 fitness: 0.259 × 11 = 2.84 (barely above baseline *k* = 2)
- fset_1 fitness: 0.922 × 11 = 10.14 (near maximum *k* + *B*\_max = 11)

### The asymmetry onset

At low *b* − *c* (< 0.125), both populations are symmetric: mostly defectors with ~4–5% cooperation. The asymmetry grows continuously and is already pronounced by *b* − *c* = 0.5 (ΔqBSeen = 0.151). There is no sharp threshold — unlike the Prisoner's Dilemma where cooperation shows a bimodal phase transition near **R ≈ P**. Instead, the Hamilton game produces a **gradual** symmetry breaking as *b* − *c* increases.

Single-run data (hamilton_1run) confirms that this gradual transition is **genuine, not an averaging artifact**: each *b* − *c* value shows a stable intermediate cooperation level that persists across all 9 timesteps (std typically 2–8%), not all-or-nothing jumps that average into a gradient. The cooperation rises smoothly from ~0.04 at low *b* − *c* through ~0.34 at *b* − *c* = 0.18 to 0.58–0.85 at high *b* − *c*. Hamilton's constant **T − R = 1** keeps a persistent temptation to defect at every parameter value, unlike the PD where varying **T − R** can approach zero and create sharper bistability boundaries.

### The paradox of success

The more successful cooperation is in one population, the more exploitable that population becomes. The correlation between "more choosers" and "lower fitness" is −0.92, matching the pattern found in the Prisoner's Dilemma (where the correlation was −1.00).

Single-run data confirms that the asymmetry is an **absorbing state** at high *b* − *c*: zero role flips occur across all 9 timesteps. Which population becomes the cooperator is **stochastic** — at *b* − *c* = 2.0 and 4.0, fset_0 is the cooperator, but at *b* − *c* = 2.83, 5.66, and 8.0, fset_1 is the cooperator instead. Each cell's symmetry breaking is an independent stochastic event; the averaged data always labels fset_0 as the higher-qBSeen population because it sorts after averaging. At low *b* − *c*, roles flip frequently (2–5 times per cell), consistent with cooperation being too weak to lock in. The weaker averaged correlation in Hamilton (−0.92 vs PD's −1.00) likely reflects this low-*b* − *c* noise rather than role switching at high *b* − *c*.

## Evolving vs Fixed Population (pop_3, panels c-d)

### Sharp transition in the evolving population

In pop_3, the evolving population adapts to a fixed population with 25% each of C0P0, C0P1, C1P0, C1P1 (qBSeen = 0.50, P1 = 0.50 constant). The evolving population shows a sharp cooperation transition:

| *b* − *c*     | qBSeen (evolving) | P1        | C1P1      |
| --------- | ----------------- | --------- | --------- |
| 0.250     | 0.047             | 0.517     | 0.034     |
| 0.354     | 0.053             | 0.538     | 0.040     |
| 0.500     | 0.071             | 0.526     | 0.056     |
| **0.707**     | **0.408**             | **0.746**     | **0.383**     |
| 1.000     | 0.487             | 0.782     | 0.459     |
| 1.414     | 0.585             | 0.827     | 0.545     |
| 2.000     | 0.702             | 0.858     | 0.641     |

Between *b* − *c* = 0.5 and *b* − *c* = 0.707, cooperation jumps from 7.1% to 40.8% — a **~6× increase** in one step. This is the same positive-feedback tipping point seen in the Prisoner's Dilemma: once enough **C1P1** exist for mutual swaps, partner choice activates → choosers pair with other choosers (*R* where swaps succeed) → higher fitness → more cooperators.

Single-run data (hamilton_1run) confirms this is a **sharp one-time transition**: cooperation jumps at the first measured timestep (t = 131072) and remains stable throughout (std ≈ 0.02). No cycling is observed — the positive-feedback cascade ignites once and persists, identical to the pattern in prisoners_1run pop_3.

### Why the transition is sharper than in pop_1

In pop_1, cooperation is 13.2% even at *b* − *c* = 0.008, and rises smoothly. In pop_3, cooperation stays below 7% until *b* − *c* ≈ 0.7, then jumps. The difference is the pairing structure:

- **pop_1** (within-population): Both partners at an interaction come from the **same** population (still well-mixed—no spatial layout). Mutual swaps only need another **C1P1** from **that** pool, not coordinated rare types across two populations. A rare C1P1 paired with a defector can mutually swap with another such C1P1 and immediately gain a C1P1 partner. Partner choice works at any cooperator frequency. **This is pairing/matching structure (one pool of interaction partners), not “two C1P1 are likelier because they share ancestry.”** Finite-population relatedness is secondary here.
- **pop_3** (between-population): The evolving population pairs only with the fixed population. For a mutual swap, a C1P1 in the evolving population stuck with a defector in the fixed population needs **another C1P1** in the evolving population who is also stuck with a defector from the fixed population (choose_partner_L0P2 pairs choosers across populations the same way). When cooperators are rare in the evolving population, such pairs are unlikely. Cooperation must cross a threshold density before the swap cascade ignites.

### Exploitation crossover

The direction of exploitation reverses as cooperation increases in the evolving population:

| *b* − *c*     | w̄_evolving    | w̄_fixed    | Δw̄     | qBSeen_evolving |
| --------- | ------------- | ---------- | ------ | --------------- |
| 0.354     | 0.238         | 0.143      | +0.096 | 0.053           |
| 0.500     | 0.243         | 0.146      | +0.097 | 0.071           |
| 0.707     | 0.222         | 0.200      | +0.023 | 0.408           |
| 1.000     | 0.229         | 0.225      | +0.004 | 0.487           |
| 1.414     | 0.238         | 0.265      | −0.027 | 0.585           |
| 2.000     | 0.254         | 0.328      | −0.073 | 0.702           |
| 4.000     | 0.327         | 0.548      | −0.221 | 0.907           |

The crossover occurs near *b* − *c* ≈ 1.0 (Δw̄ ≈ +0.004), precisely where the evolving population's cooperation level (~0.49) matches the fixed population's (0.50).

**When *b* − *c* < 1.0**: The evolving population is mostly defectors. Its defectors exploit the fixed population's cooperators (who are 50% of the fixed pop). The evolving population has higher fitness.

**When *b* − *c* > 1.0**: The evolving population is mostly cooperators. Its cooperators pay costs to benefit both cooperators and defectors in the fixed population. The fixed population's defectors get a free ride. Same counterpart bottleneck as in **mutualism.md**: fixed population only **25% C1P1**, so few counterparts for clearing mismatches.

At *b* − *c* = 8.0, the fitness gap is large: w̄_evolving = 0.504 vs w̄_fixed = 0.920 (the fixed population's fitness is 1.82x higher).

## Shuffle Effect

Shuffling partners randomly within groups every time step has **negligible effect** on cooperation, P1, or fitness in the Hamilton study. Across all three population structures and the full *b* − *c* range, the difference between shuffle and no-shuffle conditions is typically < 0.02 in qBSeen and < 0.01 in P1.

Shuffle matters little: the next step re-applies the same swap logic (see **mutualism.md** for mechanism details); *b*–*c* payoffs make the outcome insensitive to whether pairs were broken up.

## Comparison with Prisoner's Dilemma

Both studies share **T > R > P > S** and choose_partner.c (Hamilton = mechanism **P** only; binary qBSeen — Overview). Hamilton fixes **T − R = P − S = 1** and varies only **R − P = *b* − *c***.

### Same phenomena

1. **P1 hitchhiking** — see **P1 Hitchhiking**; PD mechanism identical.
2. **pop_2 asymmetry / exploitation** — ΔqBSeen vs Δfitness **−0.92** (PD **−1.00**); **Two Coevolving Populations**.
3. **pop_3 crossover** — **Evolving vs Fixed Population**.
4. **Swap bottleneck** — same counterpart constraint as in **mutualism.md** (**C1P0** cannot swap; need **counterpart C1P1**).

### Different phenomena

1. **pop_2 transition shape**: PD is bimodal near **R ≈ P** (variable **T − R**); Hamilton’s **T − R = 1** yields **gradual** symmetry breaking — single-run: stable intermediate **qBSeen** at each *b* − *c* (std ~2–8%), not a blended artifact.
2. **pop_1 floor**: PD **qBSeen** ≈ 0.49 at lowest **R − P** (0.041); Hamilton **0.13** at 0.008 — Hamilton’s fixed temptation (**T − R** = 1) vs PD’s **T − R** → 0 at low *R*.
3. **High R − P**: C1P0 share **~33%** of cooperators at **R − P = 8** vs **9%** at 0.25 — sparse choosers (**pop_1** table); **R/P = 5** at *b* − *c* = 8 (payoffs in **The Game**).
4. **Exploitation ratio at R − P = 8**: **3.56×** fitness (Hamilton **T** up to **11** vs PD’s compressed scale).

## Regime map across given folders

For Hamilton-related interpretation in this repository, the `given` folders play three distinct roles:

| given folder | Effective game family | Interpretation use |
| ----- | ----- | ----- |
| `1.0` | Prisoner's Dilemma along the Hamilton diagonal | Primary Hamilton dilemma analysis |
| `0.5` | Mixed along the diagonal: PD for low *b* − *c*, harmony-like for high *b* − *c* | Internal calibration of regime-dependent signatures |
| `1.5` | Snowdrift branch from alternate cost-based equations | Comparison extension only; not the same biological `g` meaning |

Important naming note: in this project, the `1.5` folder is treated as a **branching label** (`given >= 1.5` code path) rather than as a literal extension of the Hamilton-branch biological interpretation of `g`.

## Given = 0.5: Game-Type Classification

For the full Hamilton-branch derivation and cross-population generalization, see **mutualism.md** (**Given = 0.5: Correct Game-Type Classification**). Restricting that result to the diagonal (*b*₀ − *c*₀ = *b*₁ − *c*₁, i.e. one shared *b* − *c*), the regime split is:

- *b* − *c* < 1: **T > R > P > S** (PD)
- *b* − *c* = 1: **T = R > P = S** (boundary)
- *b* − *c* > 1: **R > T > S > P** (harmony-like)

On the 21-point Hamilton grid (shuffle_cost12_128, mechanism P, given = 0.5): **14 PD / 1 boundary / 6 harmony-like** cells.

## Why g = 0.5 Helps Interpret g = 1.0

The g = 0.5 sweep provides an internal calibration for interpretation: the same model and mechanism (P) traverses both PD-like and harmony-like local games, with the transition exactly where the payoff ordering predicts (*b* − *c* = 1). Observed shifts in qBSeen, fitness asymmetry, and chooser composition follow that regime boundary, supporting that the analysis logic is causal (payoff structure -> partner-choice bottleneck/exploitation -> outcomes), not a plotting artifact.

This strengthens confidence in the g = 1.0 reading: although g = 1.0 stays in the dilemma family, the same bottleneck and exploitation logic explains the observed gradients and asymmetries there as well. For reusable validation steps (payoff derivation, regime map, signature checks, movie confirmation), see instructions.md §6.

Scope note from the snowdrift extension: these g-based biological interpretations apply to the Hamilton benefit branch (given < 1.5), where g directly weights how much partner benefit enters T/R/S. At given >= 1.5, the code switches to the cost/snowdrift branch with different equations; there, given functions as a branch selector rather than the same biological mixing parameter used in this document.

## Given = 1.5: Snowdrift-Branch Interpretation

At `given = 1.5`, Hamilton runs in the cost/snowdrift branch. With `x = b-c`, `k0 = 2`, `k1 = 1`, payoffs become:

- `T = 3`
- `R = 2.5 + 0.5x`
- `P = 2`
- `S = 2 + x`

So the local regime split along the 21-point axis is:

- `x < 1`: `T > R > S > P`
- `x = 1`: `T = R = S > P`
- `x > 1`: `S > R > T > P`

Counts on the Hamilton grid: **14 / 1 / 6** cells respectively.

### Outcomes by population structure (`shuffle_cost12_128`, mechanism `P`)

- **pop_1**: near-saturated cooperation (`qBSeen` mean **0.956**, range **0.953-0.968**)
- **pop_2**: strong role split with very large exploitation gap  
  - `_0`: `qBSeen` **0.887**, `wmean` **3.401**  
  - `_1`: `qBSeen` **0.041**, `wmean` **9.866**  
  - `_0` more cooperative in **100%** of cells and lower fitness in **100%**
- **pop_3 evolving**: high cooperation (`qBSeen` mean **0.892**) but lower fitness than fixed side (`wmean` **5.310** vs **8.232**)

### Regime-resolved behavior on the Hamilton axis

For pop_1, cooperation stays high in both regimes, but genotype mix shifts strongly:

- `x < 1` (`T>R>S>P`): `qBSeen = 0.955`, `wmean = 6.449`, `C1P1 = 0.707`, `C1P0 = 0.247`
- `x > 1` (`S>R>T>P`): `qBSeen = 0.960`, `wmean = 8.361`, `C1P1 = 0.591`, `C1P0 = 0.370`

Correlations over the full axis confirm dilution of choosers at high `x`:

- `corr(qBSeen, log2(x)) = +0.693`
- `corr(wmean, log2(x)) = +0.776`
- `corr(C1P1, log2(x)) = -0.805`
- `corr(C1P0, log2(x)) = +0.804`

So `given = 1.5` keeps high cooperation while shifting composition from chooser-dominant to more non-chooser cooperators as `x` rises.

For pop_2, the exploitation split is robust in every regime block:

- `x < 1`: `ΔqBSeen = +0.811`, `Δwmean = -7.145`
- `x = 1`: `ΔqBSeen = +0.945`, `Δwmean = -7.558`
- `x > 1`: `ΔqBSeen = +0.910`, `Δwmean = -4.697`

Largest cooperation gap occurs at `x = 2.0` (`ΔqBSeen = +0.948`), while the most negative fitness gap occurs at `x = 0.3536` (`Δwmean = -7.841`).

### Pop_3 structure-specific detail

The evolving population is more cooperative than fixed across the full axis (`ΔqBSeen > 0` everywhere) but remains less fit (`Δwmean < 0` everywhere in sampled cells). The closest approach to parity is only at the largest `x`:

- at `x = 8.0`: `ΔqBSeen = +0.483`, `Δwmean = -0.483`

So unlike the `given = 1.0` crossover narrative, `given = 1.5` does not produce a clear fitness sign switch in pop_3 within the tested range.

### Dynamic anchor from `snowdrift_1run`

`snowdrift_1run` supports a stable-endpoint interpretation for this branch:

- mean starts near zero and end high (for pop_1: `0.0 -> 0.947`)
- late-step movement is small (pop_1 mean absolute final-step change `0.011`, only `2.9%` of cells > `0.05`)
- evolving pop_3 has even smaller late movement (`0.006`, `0.5%` > `0.05`)

This is consistent with reading Hamilton `given = 1.5` final snapshots as branch-level equilibria rather than unresolved transient states.

### Cross-g comparison anchor

Relative to `given = 0.5` and `1.0`, `given = 1.5` shows a branch-switch signature rather than a smooth continuation:

- pop_1 mean `qBSeen`: **0.688** (`0.5`) -> **0.641** (`1.0`) -> **0.956** (`1.5`)
- pop_2 mean `ΔqBSeen` (`_0 - _1`): **+0.072** -> **+0.203** -> **+0.846**
- pop_2 mean `Δwmean` (`_0 - _1`): **-0.072** -> **-1.149** -> **-6.465**

This aligns with the standalone `snowdrift.md` pattern: cooperation can be high while cross-population exploitation remains strong.

## Summary

| Topic                  | Main numbers (detail in sections above)                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| **P1 hitchhiking**         | pop_1 **P1** max **0.887** at **R − P = 0.25**; pop_2 **0.893** at **2.0**                                             |
| **Sparse choosers / C1P0** | **9% → 33%** of cooperators (**0.25 → 8.0**); **qBSeen** ~**0.93–0.97**; 1run anti-phase mostly **identity + P churn** |
| **pop_2**                  | **ΔqBSeen** vs **Δfitness −0.92**; exploit ratio **3.56×** at *b* − *c* = 8; absorbing roles at high *b* − *c*         |
| **pop_3**                  | Jump **7% → 41%** **qBSeen** between **R − P = 0.5** and **0.707**; crossover **Δw̄** near **R − P ≈ 1**                    |
| **Given = 1.5 (snowdrift branch)** | Regimes **14/1/6** (`T>R>S>P` / boundary / `S>R>T>P`); pop_1 `qBSeen` mean **0.956**; pop_2 `_0` more cooperative but lower fitness in **100%** of cells; mean `Δwmean` (`_0-_1`) **-6.465** |
