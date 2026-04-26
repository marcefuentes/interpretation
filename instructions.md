# Simulation Model Reference

**Read this file first.** It covers the simulation model, mechanisms, and population structures shared by all studies (prisoners, hamilton, snowdrift, etc.). For game-specific parameters, data formats, and results, see:

- instructions_prisoners.md — Prisoner's Dilemma (T/S fixed, R/P vary on 2D grid)
- instructions_hamilton.md — Hamilton altruism game (b−c on 1D axis)

---

## 1. The Game

All studies use a symmetric 2×2 game with payoffs T > R > P > S:

|         | Partner C   | Partner D   |
| ------- | ----------- | ----------- |
| Focal C | R           | S           |
| Focal D | T           | P           |

How T, R, P, S are parameterized differs by study — see the game-specific instructions.

---

## 2. The Simulation Model

### 2.1 Alleles

Each individual carries alleles at **6 loci** (C, I, J, M, P, Q) → **64 genotypes**.

| Locus   | 0 allele     | 1 allele                | What the 1-allele does                                                                                |
| ------- | ------------ | ----------------------- | ----------------------------------------------------------------------------------------------------- |
| **C**   | Defect first | Cooperate first         | Determines initial cooperation decision                                                               |
| **P**   | —            | Choose by recent qBSeen | Partner choice using the **most recent** qBSeen of potential partners                                 |
| **Q**   | —            | Choose by avg qBSeen    | Partner choice using the **average lifetime** qBSeen of potential partners                            |
| **M**   | —            | Tit-for-tat             | Direct reciprocity                                                                                    |
| **I**   | —            | Use recent qBSeen       | Indirect reciprocity using the **most recent** qBSeen of the current partner (including new partners) |
| **J**   | —            | Use avg qBSeen          | Indirect reciprocity using the **average lifetime** qBSeen of the current partner (its "image score") |

**Critical**: P1 (and Q1) are phenotypically silent in defectors. A C0P1 individual carries the chooser allele but never uses it — only C1P1 individuals actually choose partners.

### 2.2 Mechanisms

Each simulation run activates a subset of cooperation modules. The mechanism name corresponds to the active loci (folder name in results path):

| Mechanism folder  | Active loci                     | Modules enabled                                                  |
| ----------------- | ------------------------------- | ---------------------------------------------------------------- |
| _               | All 6 (but only C is expressed) | None (control — P, Q, M, I, J drift neutrally with a small cost) |
| P               | C, P                            | Partner choice                                                   |
| M               | C, M                            | Direct reciprocity                                               |
| MP              | C, M, P                         | Reciprocity + partner choice                                     |
| IM              | C, I, M                         | Direct + indirect reciprocity                                    |
| IMP             | C, I, M, P                      | All three                                                        |
| IJMPQ           | All 6                           | All three, with lifetime variants                                |

Full mapping: ../graph/graphgen/studies/trps/mech_trait_map.csv — defines which alleles are evolvable and how derived traits (AllC, AllD, Choose, dTFT, iTFT, etc.) map to genotype sums for each mechanism.

### 2.3 Partner Choice

From choose_partner.c — a C1P1 individual can improve its partner if:

c
ind->Choose != 0 &&        // has P1 allele
ind->qBSeen != 0 &&        // is a cooperator (C1)
ind->partner->qBSeen == 0  // current partner is a defector


**Swapping (not abandonment).** Choosers do **not** simply drop a defector for an arbitrary cooperator. In choose_partner_L0P1, individuals in the swap pool satisfy can_improve_L0_partner (C1P1 paired with C0). The code **mutually pairs two such choosers with each other** (swap_partners): after the swap, each chooser’s new partner is the **other chooser**—both are **C1P1**, so each trades a C0 partner for partnership with a **C1P1** (mutual *R*). The two defectors that were released end up paired with each other (C0–C0, *P*). C1P0 never enters this pool (Choose == 0).

**Key constraint**: A successful upgrade requires another C1P1 in the same group who is also stuck with a defector (so both sides of the mutual swap exist). When choosers or pairings are rare, swap opportunities are scarce.

### 2.4 Simulation Loop

Source: ~/code/trps/code/src/. Main loop in modules_common/simulation.c, executed **per time step** in this order:

| Step              | What happens                                            | Source file                                      |
| ----------------- | ------------------------------------------------------- | ------------------------------------------------ |
| 1. Fitness        | Compute payoffs from game with current partners         | modules/fitness.c                              |
| 2. Analyze        | Record statistics (genotype frequencies, qBSeen, wmean) | modules/stats.c, modules/write.c             |
| 3. Update scores  | Update lifetime qBSeen averages (if Q/J loci enabled)   | modules/individual_tools.c → update_scores() |
| 4. Shuffle        | Randomly reassign partners within groups                | modules_common/shuffle_partners.c              |
| 5. Partner choice | C1P1 mutually swap so each pairs with another C1P1 (not lone “abandonment”) | modules/choose_partner.c                       |
| 6. Recruitment    | Death, fitness-proportional reproduction, mutation      | modules/recruits.c → handle_recruitment()    |
| 7. Decide qB      | Update cooperation decision (reciprocity)               | modules/decide_qB.c                            |

Other files: main.c (entry point), modules/individual_tools.c (allocation, initial pairing via initial_pairs_1/initial_pairs_2, fixed-population setup), modules/read_globals.c (parameters), modules/calculate_derived_globals.c (derived parameters).

---

## 3. Population Scenarios

### pop_1: Single population
- Individuals pair within the same population
- Standard evolutionary dynamics

### pop_2: Two coevolving populations
- Both populations evolve
- All pairing is **between** populations — no intrapopulational pairs, no solitary individuals
- Each group has **128 individuals from each population** (128 pairs per group)
- file_set _0 = the population with **higher** qBSeen; _1 = **lower** qBSeen

### pop_3: One evolving + one fixed
- file_set _0: **Evolving** population (frequencies change)
- file_set _1: **Fixed** population (25% each of C0P0, C0P1, C1P0, C1P1; constant)
- All pairing is between populations
- The fixed population provides a constant selective environment

---

## 4. Data

### 4.1 Results path

All studies live under ~/results/{study}/:


~/results/{study}/{path_template}/{population}/


The common path template is {shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}. See the game-specific instructions for concrete examples.

#### Single-run variants (_1run)

The studies hamilton_1run and prisoners_1run are single-run versions of hamilton and prisoners. The main studies average over multiple simulation runs, which smooths out stochastic variation. The _1run variants track a single population through time, making it possible to observe temporal dynamics that averaging would obscure — for example, whether cooperation and defection cycle (phases where partner choosers dominate alternating with phases where AllD does). These temporal patterns can help explain features of the averaged results from the main studies.

### 4.2 Data files

| File                  | Contents                                                         |
| --------------------- | ---------------------------------------------------------------- |
| csv_0_for_image.con | Final-timestep data for file_set _0 (one row per parameter cell) |
| csv_1_for_image.con | Final-timestep data for file_set _1                              |
| csv_0_for_movie.con | Multi-timestep data for _0 (9 snapshots: t=1 to t=1048576)       |
| csv_1_for_movie.con | Multi-timestep data for _1                                       |

### 4.3 .con file columns (common)

All formats share:
- Game parameter columns (varies by study — see game-specific instructions)
- Time — simulation timestep
- wmean, wmeanSD, wsd, wsdSD — population mean fitness and stdev
- qBSeen, qBSeenSD — cooperation probability
- 64 genotype frequency columns (6 loci: C, I, J, M, P, Q)
- Each genotype column has a corresponding SD column

> **Note**: The column P1 is a game parameter in studies with per-population payoffs (prisoners, snowdrift). Do not confuse it with the P1 allele frequency, which must be computed from genotype sums.

### 4.4 Computing derived traits from genotypes

Allele frequencies and derived traits must be computed from genotype columns. Example for the P1 allele:

python
# Exclude SD columns, then sum genotypes by allele prefix
c0p1_cols = [c for c in df.columns if c.startswith('C0P1') and not c.endswith('SD')]
c1p1_cols = [c for c in df.columns if c.startswith('C1P1') and not c.endswith('SD')]

df['C0P1'] = df[c0p1_cols].sum(axis=1)  # defectors carrying P1 (silent)
df['C1P1'] = df[c1p1_cols].sum(axis=1)  # cooperators who choose (active)
df['P1'] = df['C0P1'] + df['C1P1']      # total P1 allele frequency
df['Choosers'] = df['C1P1']             # only C1P1 actually choose!


For the full mapping of mechanisms to derived traits, see ../graph/graphgen/studies/trps/mech_trait_map.csv.

---

## 5. graphgen Files

| File                                                | Purpose                                         |
| --------------------------------------------------- | ----------------------------------------------- |
| ../graph/graphgen/studies/{study}/manifest.py     | Study config, figure definitions, MAIN_ROWS     |
| ../graph/graphgen/studies/trps/config.py          | Shared TRPS trait definitions, figure structure |
| ../graph/graphgen/studies/trps/mech_trait_map.csv | Mechanism → trait mapping (see §2.2)            |
| ../graph/graphgen/studies/common/shared.py        | Common path template                            |

---

## 6. Interpretation Checklist for Any given Value

Use this workflow whenever analyzing a new given (for example 0.5, 1.0, 1.5) so conclusions stay tied to the actual payoff structure.

### 6.1 Re-generate exact inputs

1. Regenerate static and movie outputs with the target given:
   - python -m graphgen.main --study <study> --figure s07 --given-focal <g>
   - python -m graphgen.main --study <study> --figure s07 --given-focal <g> --movie
2. Confirm .con sources exist under:
   - ~/results/{study}/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}/{population}/
3. If temporal interpretation is needed, include _1run movie files (csv_*_for_movie.con) rather than only final snapshots.

Agent policy: if expected summary exports are missing (`csv_*_for_image.con` and/or `csv_*_for_movie.con`), run graphgen first to generate them before proceeding with interpretation.

### 6.2 Compute payoffs from source equations (not assumptions)

Always derive payoffs from ~/code/trps/code/src/modules/calculate_derived_globals.c.

Important scope rule: do not assume the biological meaning of given is universal across branches. In the Hamilton benefit branch (given < 1.5), given is part of the biological payoff weighting; in the snowdrift/cost branch (given >= 1.5), the equations change and given primarily selects a different payoff parameterization.

For the Hamilton branch (given < 1.5), with x_i = b_i - c, b_i = k1 + x_i:

- Population 0:
  - T0 = k0 + b1*given
  - R0 = k0 + b0*(1-given) + b1*given - k1
  - P0 = k0
  - S0 = k0 + b0*(1-given) - k1
- Population 1 swaps b0 and b1.

Do not classify game type until these values are computed for the exact cell (x0, x1).

### 6.3 Build a local game-regime map

For each parameter cell, classify payoff ordering (allowing ties at boundaries), e.g.:

- T > R > P > S (PD)
- R > T > S > P (harmony-like)
- R > S > T > P (possible in asymmetric cross-benefit settings)
- boundary forms such as T = R > P = S

For 2D studies (prisoners, mutualism, snowdrift), report counts per ordering for each population and for important subsets (for example asymmetric vs diagonal when applicable, plus high/low regions).

### 6.4 Check expected signatures in outputs

Given the mapped regimes, test whether observed patterns match expected dynamics:

1. qBSeen:
   - PD-heavy regions should resist cooperation unless mechanisms bootstrap it.
   - Harmony-like regions should allow broad cooperation.
2. wmean:
   - Verify exploitation patterns (cooperator-rich side can have lower fitness).
   - Locate crossover points where fitness advantage changes sign.
3. Genotype decomposition:
   - Separate C1P1, C1P0, C0P1 (P1-silent carriers).
   - Check for chooser bottlenecks and P1 hitchhiking.

### 6.5 Validate against time dynamics

Use movie snapshots to confirm whether spatial/parameter gradients are true dynamics or averaging artifacts:

- Stable intermediate states vs rapid flips
- Early invasion vs late equilibrium behavior
- Role-locking vs frequent reversals in coevolving populations

If only final snapshots are used, mark dynamic claims as provisional.

### 6.6 Minimum reporting block for docs

For each new given, include:

1. Exact payoff equations used (with source file reference)
2. Regime map summary (counts/tables)
3. Key observed signatures (qBSeen, wmean, genotype splits)
4. One short consistency statement:
   - "Observed patterns are/are not consistent with local payoff regimes, with caveats ..."
