# Copilot Instructions

## Repository Purpose

Documentation and analysis for interpreting TRPS evolutionary simulation outputs.

Current active study: **hamilton** (~/results/hamilton). Mutualism and calibration studies pending new data. Old docs from the previous parameterization are preserved in legacy/.

## Repo Layout

- Keep human-facing analysis and reference docs at the repository root.
- Keep active Copilot instructions in .github/copilot-instructions.md.
- Put any additional agent-only support material under ai/ so it stays separate from the docs intended for human reading.
- legacy/ holds archived docs from the previous parameterization — do not edit or cite those as current.

## Related Repositories (same machine)

- ~/code/graph/graphgen/ (same as ../graph/graphgen/ from this repo) — figure pipeline, study manifests, mech_trait_map.csv. Run **graphgen** here to **regenerate** csv_*_for_image.con (final timestep) and csv_*_for_movie.con (multi-timestep) whenever those exports are missing from ~/results/.
- ../trps/ or ~/code/trps/ — C simulation source code
- ~/results/ — simulation output data

Paths like ../graph/graphgen/... are relative to this repo root.

### Missing summary exports policy (for AI agents)

- Before analysis, verify that required summary exports exist in the target results folder:
  - csv_*_for_image.con for final-state summaries
  - csv_*_for_movie.con for time-series summaries
- If required exports are missing, run graphgen from ~/code/graph/graphgen/ to generate them before continuing interpretation.
- Treat missing *image.con or *movie.con summary files as a data-prep step, not an analysis failure.

## Architecture

### Study Status

**hamilton**: complete data at ~/results/hamilton (shuffle and noshuffle, groupsize 128 and 4, all mechanisms, dilemmas 0/1/2, pop_1/2/3).

**mutualism**: incomplete data at ~/results/mutualism (noshuffle_cost0.001_128 only; mechanisms M, MP, IMP, IJMPQ; dilemmas 0/1/2; pop_2 only). Raw csv files exist per cell but graphgen summary exports (.con files) have not yet been generated. Do not create interpretation docs until data is complete.

### Hamilton Parameter Space

Hamilton is a 1D sweep with **b = 0.4 (fixed)** and **c varying from 0 to b**. The x-axis is therefore c ∈ [0, 0.4]. The baseline fitness is **K = 0.5**.

Payoffs by dilemma type (folder names 0, 1, 2):

| Folder | Dilemma      | T       | R           | P   | S           |
| ------ | ------------ | ------- | ----------- | --- | ----------- |
| 0      | No dilemma   | K + b   | K + b       | K   | K           |
| 1      | PD           | K + b   | K + b - c   | K   | K - c       |
| 2      | Snowdrift    | K + b   | K + b - c/2 | K   | K + b - c   |

With K = 0.5, b = 0.4: T = 0.9, P = 0.5 (constant). R and S vary with c.

### Mechanisms Available (hamilton)

| Mechanism folder | Active loci                      | Modules enabled                                                   |
| ---------------- | -------------------------------- | ----------------------------------------------------------------- |
| \_               | All 6 (only C expressed)         | None (control)                                                    |
| P                | C, P                             | Partner choice                                                    |
| M                | C, M                             | Direct reciprocity                                                |
| MP               | C, M, P                          | Reciprocity + partner choice                                      |
| MPQ              | C, M, P, Q                       | Reciprocity + partner choice (recent + lifetime)                  |
| IM               | C, I, M                          | Direct + indirect reciprocity (recent)                            |
| IJM              | C, I, J, M                       | Direct + indirect reciprocity (recent + lifetime)                 |
| IMP              | C, I, M, P                       | All three                                                         |
| IJMPQ            | All 6                            | All three, with lifetime variants                                 |

Mechanisms \_ and M are run for all three dilemma folders (0, 1, 2). All other mechanisms are run for folders 1 and 2 only (dilemma conditions required for partner choice and indirect reciprocity to be meaningful).

## Key Conventions

### AI Writing Rule

- Do not use backticks in Markdown documentation.

### Markdown Table Formatting

When editing Markdown tables, keep raw-source alignment readable in plain text editors (especially Vim with conceal enabled):

- Treat *, **, and backticks as formatting markers, not visible cell content.
- Treat escape backslashes (for example in \_) as visible characters for raw-source alignment unless your editor conceal settings explicitly hide them.
- Pad cells based on the **visible rendered text width**, not raw character count including formatting markers.
- Keep each column width consistent across header, separator, and body rows.
- Prefer simple ASCII separators in table text (- vs −) when alignment is sensitive.
- After editing a table, quickly re-check the raw Markdown in a monospaced editor to confirm columns still line up.

### Data File Layout

Results live at ~/results/{study}/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{dilemma}/{population}/:

- **dilemma**: 0 (no dilemma), 1 (PD), 2 (snowdrift)
- **shuffle**: shuffle or noshuffle
- **cost**: mutation cost (currently 0.001)
- **groupsize**: 128 or 4

Example: ~/results/hamilton/shuffle_cost0.001_128/P/1/pop_2/csv_0_for_image.con

| File                  | Contents                                                         |
| --------------------- | ---------------------------------------------------------------- |
| csv_0_for_image.con | Final-timestep data, file_set _0 (one row per parameter cell)    |
| csv_1_for_image.con | Final-timestep data, file_set _1                                 |
| csv_0_for_movie.con | Multi-timestep data, _0 (snapshots from t=1 to t=1048576)        |
| csv_1_for_movie.con | Multi-timestep data, _1                                          |

### Data Format

All studies use **64 genotypes** from **6 loci** (C, I, J, M, P, Q):
- Genotype columns: C0I0J0M0P0Q0 through C1I1J1M1P1Q1 (alphabetical)
- No pre-computed derived trait columns — compute everything from genotypes
- Game parameter columns for hamilton/mutualism: **c0, c1** (cost for each population)

### Computing Derived Traits from Genotypes

Always sum genotypes to get allele frequencies:

python
c1p1_cols = [c for c in df.columns if c.startswith('C1') and 'P1' in c and not c.endswith('SD')]
c0p1_cols = [c for c in df.columns if c.startswith('C0') and 'P1' in c and not c.endswith('SD')]
c1p0_cols = [c for c in df.columns if c.startswith('C1') and 'P0' in c and not c.endswith('SD')]

df['C1P1'] = df[c1p1_cols].sum(axis=1)  # cooperators who choose (P1 active)
df['C0P1'] = df[c0p1_cols].sum(axis=1)  # defectors carrying P1 (P1 silent)
df['C1P0'] = df[c1p0_cols].sum(axis=1)  # cooperators who don't choose
df['P1']   = df['C1P1'] + df['C0P1']    # total P1 allele frequency


Full mechanism → trait mapping: ../graph/graphgen/studies/trps/mech_trait_map.csv

### The C0P1 Silencing Rule

**P1 is phenotypically silent in defectors.** A C0P1 individual carries the partner-choice allele but never uses it. Only C1P1 individuals actually choose partners. This means:
- P1 allele frequency ≠ fraction of choosers
- C0P1 accumulates as a neutral carrier via mutation from C1P1, inflating P1 frequency in the transition zone
- Always use C1P1 (= Choosers) for behavioral analysis, P1 only for genetic analysis

### File Set _0/_1 Semantics

| Study    | _0                      | _1                                      |
| -------- | ----------------------- | --------------------------------------- |
| hamilton (pop_2) | Higher qBSeen  | Lower qBSeen                            |
| hamilton (pop_3) | Evolving population | Fixed population (25% each genotype) |

### Population Scenario Semantics

- **pop_1**: Single population; individuals pair within the same population
- **pop_2**: Two coevolving populations; all pairing is **between** populations (128 from each per group)
- **pop_3**: One evolving + one fixed; file_set _1 is held at 25% each of C0P0/C0P1/C1P0/C1P1

### Partner Choice Bottleneck

Swaps require C1P1 on **both** sides. The code **mutually** rematches two choosers: each trades a C0 partner for partnership with the **other** C1P1 (not an undirected "abandonment" to a random C1). The two defectors end up paired with each other. When such chooser pairs are rare, swap opportunities are scarce — this creates a positive feedback threshold.

### Mutualism Payoff Asymmetry

In mutualism, the two populations differ in **cost** (c1 > c0 by construction). Since b is fixed and equal for both, the cooperation incentive R−P = b−c differs by population:
- Pop 0's R−P = b − c0 (lower cost → stronger incentive)
- Pop 1's R−P = b − c1 (higher cost → weaker incentive)

Population 0 always has the higher cooperation incentive. The grid is the strict upper triangle c1 > c0, with c ∈ [0, b].

## Figure Pipeline (graphgen)

Figures are generated by ../graph/graphgen/studies/{study}/manifest.py. Key files:
- ../graph/graphgen/studies/{study}/manifest.py — MAIN_ROWS defines panel layout (row → population, file_set, trait, renderer)
- ../graph/graphgen/studies/trps/config.py — shared trait definitions
- ../graph/graphgen/studies/common/shared.py — common path template

Renderers: imshow for heatmaps (prisoners/mutualism), plot for line plots (hamilton).
