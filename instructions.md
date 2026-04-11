# Simulation Model Reference

**Read this file first.** It covers the simulation model, mechanisms, and population structures shared by all studies (prisoners, hamilton, snowdrift, etc.). For game-specific parameters, data formats, and results, see:

- `instructions_prisoners.md` — Prisoner's Dilemma (T/S fixed, R/P vary on 2D grid)
- `instructions_hamilton.md` — Hamilton altruism game (b−c on 1D axis)

---

## 1. The Game

All studies use a symmetric 2×2 game with payoffs T > R > P > S:

|  | Partner C | Partner D |
|--|-----------|-----------|
| Focal C | R | S |
| Focal D | T | P |

How T, R, P, S are parameterized differs by study — see the game-specific instructions.

---

## 2. The Simulation Model

### 2.1 Alleles

Each individual carries alleles at up to 6 loci. Some studies use 4 loci (C, P, M, I → 16 genotypes); others use all 6 (C, I, J, M, P, Q → 64 genotypes).

| Locus | 0 allele | 1 allele | What the 1-allele does |
|-------|----------|----------|------------------------|
| **C** | Defect first | Cooperate first | Determines initial cooperation decision |
| **P** | — | Choose by recent qBSeen | Partner choice using the **most recent** qBSeen of potential partners |
| **Q** | — | Choose by avg qBSeen | Partner choice using the **average lifetime** qBSeen of potential partners |
| **M** | — | Tit-for-tat | Direct reciprocity |
| **I** | — | Use recent qBSeen | Indirect reciprocity using the **most recent** qBSeen of the current partner (including new partners) |
| **J** | — | Use avg qBSeen | Indirect reciprocity using the **average lifetime** qBSeen of the current partner (its "image score") |

**Critical**: P1 (and Q1) are phenotypically silent in defectors. A C0P1 individual carries the chooser allele but never uses it — only C1P1 individuals actually choose partners.

### 2.2 Mechanisms

Each simulation run activates a subset of cooperation modules. The mechanism name corresponds to the active loci (folder name in results path):

| Mechanism folder | Active loci | Modules enabled |
|-----------------|-------------|-----------------|
| `_` | All 6 (but only C is expressed) | None (control — P, Q, M, I, J drift neutrally with a small cost) |
| `P` | C, P | Partner choice |
| `M` | C, M | Direct reciprocity |
| `MP` | C, M, P | Reciprocity + partner choice |
| `IM` | C, I, M | Direct + indirect reciprocity |
| `IMP` | C, I, M, P | All three |
| `IJMPQ` | All 6 | All three, with lifetime variants |

Full mapping: `../graph/graphgen/studies/trps/mech_trait_map.csv` — defines which alleles are evolvable and how derived traits (AllC, AllD, Choose, dTFT, iTFT, etc.) map to genotype sums for each mechanism.

### 2.3 Partner Choice

From `choose_partner.c` — a C1P1 individual can improve its partner if:

```c
ind->Choose != 0 &&        // has P1 allele
ind->qBSeen != 0 &&        // is a cooperator (C1)
ind->partner->qBSeen == 0  // current partner is a defector
```

**Swapping**: Two C1P1 individuals both paired with C0 can swap partners. After the swap, both C1P1 have cooperator partners (get R), both C0 have defector partners (get P).

**Key constraint**: Swaps require C1P1 on BOTH sides. When cooperators are rare, swap opportunities are scarce.

### 2.4 Simulation Loop

Source: `~/code/trps/code/src/`. Main loop in `modules_common/simulation.c`, executed **per time step** in this order:

| Step | What happens | Source file |
|------|-------------|-------------|
| 1. Fitness | Compute payoffs from game with current partners | `modules/fitness.c` |
| 2. Analyze | Record statistics (genotype frequencies, qBSeen, wmean) | `modules/stats.c`, `modules/write.c` |
| 3. Update scores | Update lifetime qBSeen averages (if Q/J loci enabled) | `modules/individual_tools.c` → `update_scores()` |
| 4. Shuffle | Randomly reassign partners within groups | `modules_common/shuffle_partners.c` |
| 5. Partner choice | C1P1 swap away from defector partners | `modules/choose_partner.c` |
| 6. Recruitment | Death, fitness-proportional reproduction, mutation | `modules/recruits.c` → `handle_recruitment()` |
| 7. Decide qB | Update cooperation decision (reciprocity) | `modules/decide_qB.c` |

Other files: `main.c` (entry point), `modules/individual_tools.c` (allocation, initial pairing via `initial_pairs_1`/`initial_pairs_2`, fixed-population setup), `modules/read_globals.c` (parameters), `modules/calculate_derived_globals.c` (derived parameters).

---

## 3. Population Scenarios

### pop_1: Single population
- Individuals pair within the same population
- Standard evolutionary dynamics

### pop_2: Two coevolving populations
- Both populations evolve
- All pairing is **between** populations — no intrapopulational pairs, no solitary individuals
- Each group has **128 individuals from each population** (128 pairs per group)
- `file_set _0` = the population with **higher** qBSeen; `_1` = **lower** qBSeen

### pop_3: One evolving + one fixed
- `file_set _0`: **Evolving** population (frequencies change)
- `file_set _1`: **Fixed** population (25% each of C0P0, C0P1, C1P0, C1P1; constant)
- All pairing is between populations
- The fixed population provides a constant selective environment

---

## 4. Data

### 4.1 Results path

All studies live under `~/results/{study}/`:

```
~/results/{study}/{path_template}/{population}/
```

The common path template is `{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}`. See the game-specific instructions for concrete examples.

### 4.2 Data files

| File | Contents |
|------|----------|
| `csv_0_for_image.con` | Final-timestep data for file_set _0 (one row per parameter cell) |
| `csv_1_for_image.con` | Final-timestep data for file_set _1 |
| `csv_0_for_movie.con` | Multi-timestep data for _0 (9 snapshots: t=1 to t=1048576) |
| `csv_1_for_movie.con` | Multi-timestep data for _1 |

### 4.3 .con file columns (common)

All formats share:
- Game parameter columns (varies by study — see game-specific instructions)
- `Time` — simulation timestep
- `wmean, wsd` — population mean fitness and stdev
- `qBDefault, qBSeen` — cooperation probabilities
- Genotype frequency columns (16 or 64 depending on active loci)
- Each genotype column has a corresponding `SD` column

> **⚠ Data version note**: `hamilton` and `hamilton_1run` use the **current** format (64 genotypes, 6 loci). All other studies (prisoners, snowdrift, cgnr, mgnr, etc.) still use the **legacy** format (16 genotypes, 4 loci). See the game-specific instructions for column details.

### 4.4 Computing derived traits from genotypes

Allele frequencies and derived traits must be computed from genotype columns. Example for the P1 allele:

```python
# Exclude SD columns, then sum genotypes by allele prefix
c0p1_cols = [c for c in df.columns if c.startswith('C0P1') and not c.endswith('SD')]
c1p1_cols = [c for c in df.columns if c.startswith('C1P1') and not c.endswith('SD')]

df['C0P1'] = df[c0p1_cols].sum(axis=1)  # defectors carrying P1 (silent)
df['C1P1'] = df[c1p1_cols].sum(axis=1)  # cooperators who choose (active)
df['P1'] = df['C0P1'] + df['C1P1']      # total P1 allele frequency
df['Choosers'] = df['C1P1']             # only C1P1 actually choose!
```

For the full mapping of mechanisms to derived traits, see `../graph/graphgen/studies/trps/mech_trait_map.csv`.

---

## 5. graphgen Files

| File | Purpose |
|------|---------|
| `../graph/graphgen/studies/{study}/manifest.py` | Study config, figure definitions, MAIN_ROWS |
| `../graph/graphgen/studies/trps/config.py` | Shared TRPS trait definitions, figure structure |
| `../graph/graphgen/studies/trps/mech_trait_map.csv` | Mechanism → trait mapping (see §2.2) |
| `../graph/graphgen/studies/common/shared.py` | Common path template |
