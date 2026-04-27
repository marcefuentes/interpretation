# Copilot Instructions

## Repository Purpose

Documentation and analysis for interpreting TRPS evolutionary simulation outputs. Three studies: prisoners (Prisoner's Dilemma), hamilton (Hamilton altruism), mutualism. Each has an instructions_*.md (parameters, data format, figures) and a *.md (analysis findings).

**Always read instructions.md first** — it defines the shared simulation model, mechanisms, population scenarios, and data format used by all studies.

## Repo Layout

- Keep human-facing analysis and reference docs at the repository root.
- Keep active Copilot instructions in .github/copilot-instructions.md.
- Put any additional agent-only support material under ai/ so it stays separate from the docs intended for human reading.

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
- Use the study/given-specific invocation, for example:
  - python -m graphgen.main --study <study> --figure s07 --given-focal <g>
  - python -m graphgen.main --study <study> --figure s07 --given-focal <g> --movie
- Treat missing *image.con or *movie.con summary files as a data-prep step, not an analysis failure.

## Running the Analysis Script

bash
python3 ai/analyze_single_run.py


This script reads from ~/results/prisoners_1run/shuffle_cost12_128/P/1.0 — the BASE path must exist with populated data. No arguments; edit BASE at the top to target a different study/condition.

## Architecture

### Document Reading Order

1. instructions.md — shared model (mechanisms, population scenarios, data format)
2. instructions_{study}.md — game parameters and data format for that study
3. {study}.md — analysis findings and conclusions

### Study Differences

| Study | Parameter axes | Grid shape | Loci/Genotypes | Pop scenarios |
|-------|---------------|-----------|----------------|---------------|
| prisoners | R × P (2D, triangle in T>R>P>S space) | ~24×24 triangle | 6 loci → 64 genotypes | pop_1, pop_2, pop_3 |
| hamilton | b−c (1D, log scale) | 21 points | 6 loci → 64 genotypes | pop_1, pop_2, pop_3 |
| mutualism | b₀−c × b₁−c (2D triangular, b₁≥b₀) | 21×21 triangle, 231 cells | 6 loci → 64 genotypes | pop_2 only |

Hamilton is a 1D slice through PD parameter space with fixed T−R = P−S = 1 (slightly stronger than PD's max 0.9). The mutualism diagonal (b₀−c = b₁−c) reproduces Hamilton in the full triangular grid, but current mutualism heatmap analyses focus on the strict asymmetric subset (b₁−c > b₀−c).

### _1run Study Variants

hamilton_1run and prisoners_1run run a single simulation instead of averaging over multiple runs. Same parameters and path structure as the main studies. Use these to observe **temporal dynamics** (cycling, tipping events) that multi-run averaging smooths out.

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

Results live at ~/results/{study}/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}/{population}/:

| File | Contents |
|------|----------|
| csv_0_for_image.con | Final-timestep data, file_set _0 (one row per parameter cell) |
| csv_1_for_image.con | Final-timestep data, file_set _1 |
| csv_0_for_movie.con | Multi-timestep data, _0 (9 snapshots: t=1 to t=1048576) |
| csv_1_for_movie.con | Multi-timestep data, _1 |

### Data Format

All studies use **64 genotypes** from **6 loci** (C, I, J, M, P, Q):
- Genotype columns: C0I0J0M0P0Q0 through C1I1J1M1P1Q1 (alphabetical)
- No pre-computed derived trait columns — compute everything from genotypes
- Game parameter columns: T0, R0, P0, S0, T1, R1, P1, S1 (prisoners, snowdrift) or k, b_c_0, b_c_1 (hamilton, mutualism)

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

### File Set _0/_1 Semantics Differ by Study

| Study | _0 | _1 |
|-------|------|------|
| prisoners, hamilton (pop_2) | Higher qBSeen | Lower qBSeen |
| prisoners, hamilton (pop_3) | Evolving population | Fixed population (25% each genotype) |
| mutualism | Assigned randomly (Population 0, lower b₀−c) | Population 1 (higher b₁−c) |

### Population Scenario Semantics

- **pop_1**: Single population; individuals pair within the same population
- **pop_2**: Two coevolving populations; all pairing is **between** populations (128 from each per group)
- **pop_3**: One evolving + one fixed; file_set _1 is held at 25% each of C0P0/C0P1/C1P0/C1P1

### Partner Choice Bottleneck

Swaps require C1P1 on **both** sides. The code **mutually** rematches two choosers: each trades a C0 partner for partnership with the **other** C1P1 (not an undirected “abandonment” to a random C1). The two defectors end up paired with each other. When such chooser pairs are rare, swap opportunities are scarce — this creates a positive feedback threshold (see sharp phase transition in prisoners pop_2).

### Mutualism Payoff Asymmetry

In mutualism, population *i* receives the **partner's** benefit, not its own:
- Pop 0's R−P = b₁−c (partner's parameter)
- Pop 1's R−P = b₀−c (partner's parameter)

Since b₁−c ≥ b₀−c by construction, population 0 always has the higher cooperation incentive.

## Figure Pipeline (graphgen)

Figures are generated by ../graph/graphgen/studies/{study}/manifest.py. Key files:
- ../graph/graphgen/studies/{study}/manifest.py — MAIN_ROWS defines panel layout (row → population, file_set, trait, renderer)
- ../graph/graphgen/studies/trps/config.py — shared trait definitions
- ../graph/graphgen/studies/common/shared.py — common path template

Renderers: imshow for heatmaps (prisoners/mutualism), plot for line plots (hamilton).
