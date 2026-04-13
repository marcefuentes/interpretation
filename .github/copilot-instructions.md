# Copilot Instructions

## Repository Purpose

Documentation and analysis for interpreting TRPS evolutionary simulation outputs. Three studies: `prisoners` (Prisoner's Dilemma), `hamilton` (Hamilton altruism), `mutualism`. Each has an `instructions_*.md` (parameters, data format, figures) and a `*.md` (analysis findings).

**Always read `instructions.md` first** — it defines the shared simulation model, mechanisms, population scenarios, and data format used by all studies.

## Related Repositories (same machine)

- `../graph/graphgen/` — figure pipeline, study manifests, `mech_trait_map.csv`
- `../trps/` or `~/code/trps/` — C simulation source code
- `~/results/` — simulation output data

Paths like `../graph/graphgen/...` are relative to this repo root.

## Running the Analysis Script

```bash
python3 analyze_single_run.py
```

This script reads from `~/results/prisoners_1run/shuffle_cost12_128/P/1.0` — the `BASE` path must exist with populated data. No arguments; edit `BASE` at the top to target a different study/condition.

## Architecture

### Document Reading Order

1. `instructions.md` — shared model (mechanisms, population scenarios, data format)
2. `instructions_{study}.md` — game parameters and data format for that study
3. `{study}.md` — analysis findings and conclusions

### Study Differences

| Study | Parameter axes | Grid shape | Loci/Genotypes | Pop scenarios |
|-------|---------------|-----------|----------------|---------------|
| `prisoners` | R × P (2D, triangle in T>R>P>S space) | ~24×24 triangle | 4 loci → 16 genotypes | pop_1, pop_2, pop_3 |
| `hamilton` | b−c (1D, log scale) | 21 points | 6 loci → 64 genotypes | pop_1, pop_2, pop_3 |
| `mutualism` | b₀−c × b₁−c (2D triangular, b₁≥b₀) | 21×21 triangle, 231 cells | 6 loci → 64 genotypes | pop_2 only |

Hamilton is a 1D slice through PD parameter space with fixed T−R = P−S = 2 (much stronger than PD's max 0.9). Mutualism diagonal (b₀−c = b₁−c) reproduces Hamilton results.

### `_1run` Study Variants

`hamilton_1run` and `prisoners_1run` run a single simulation instead of averaging over multiple runs. Same parameters and path structure as the main studies. Use these to observe **temporal dynamics** (cycling, tipping events) that multi-run averaging smooths out.

## Key Conventions

### Data File Layout

Results live at `~/results/{study}/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{given_val}/{population}/`:

| File | Contents |
|------|----------|
| `csv_0_for_image.con` | Final-timestep data, file_set _0 (one row per parameter cell) |
| `csv_1_for_image.con` | Final-timestep data, file_set _1 |
| `csv_0_for_movie.con` | Multi-timestep data, _0 (9 snapshots: t=1 to t=1048576) |
| `csv_1_for_movie.con` | Multi-timestep data, _1 |

### Data Format: Legacy vs Current

**Critical distinction** — do not mix these up:

- **Legacy** (16 genotypes, 4 loci C,P,M,I): `prisoners`, `snowdrift`, `cgnr`, `mgnr`, etc.
  - Genotype columns: `C0P0M0I0` through `C1P1M1I1`
  - Has deprecated derived trait columns (`C0`, `C1`, `C0Choose`, `C1Choose`, etc.)
  - ⚠️ `C0`/`C1` columns equal bare `C0P0M0I0`/`C1P0M0I0` genotypes — **not allele frequencies**
  - Game parameter columns: `T, R, P, S`

- **Current** (64 genotypes, 6 loci C,I,J,M,P,Q): `hamilton`, `mutualism`
  - Genotype columns: `C0I0J0M0P0Q0` through `C1I1J1M1P1Q1` (alphabetical)
  - No pre-computed derived trait columns — compute everything from genotypes
  - Game parameter columns: `k, b_c_0, b_c_1`

### Computing Derived Traits from Genotypes

Never use raw `C0`/`C1` legacy columns for allele frequencies. Always sum genotypes:

```python
# Works for both legacy (4-locus) and current (6-locus) formats
c1p1_cols = [c for c in df.columns if c.startswith('C1') and 'P1' in c and not c.endswith('SD')]
c0p1_cols = [c for c in df.columns if c.startswith('C0') and 'P1' in c and not c.endswith('SD')]
c1p0_cols = [c for c in df.columns if c.startswith('C1') and 'P0' in c and not c.endswith('SD')]

df['C1P1'] = df[c1p1_cols].sum(axis=1)  # cooperators who choose (P1 active)
df['C0P1'] = df[c0p1_cols].sum(axis=1)  # defectors carrying P1 (P1 silent)
df['C1P0'] = df[c1p0_cols].sum(axis=1)  # cooperators who don't choose
df['P1']   = df['C1P1'] + df['C0P1']    # total P1 allele frequency
```

Full mechanism → trait mapping: `../graph/graphgen/studies/trps/mech_trait_map.csv`

### The C0P1 Silencing Rule

**P1 is phenotypically silent in defectors.** A `C0P1` individual carries the partner-choice allele but never uses it. Only `C1P1` individuals actually choose partners. This means:
- `P1` allele frequency ≠ fraction of choosers
- `C0P1` accumulates as a neutral carrier via mutation from `C1P1`, inflating P1 frequency in the transition zone
- Always use `C1P1` (= Choosers) for behavioral analysis, `P1` only for genetic analysis

### File Set `_0`/`_1` Semantics Differ by Study

| Study | `_0` | `_1` |
|-------|------|------|
| `prisoners`, `hamilton` (pop_2) | Higher qBSeen | Lower qBSeen |
| `prisoners`, `hamilton` (pop_3) | Evolving population | Fixed population (25% each genotype) |
| `mutualism` | Assigned randomly (Population 0, lower b₀−c) | Population 1 (higher b₁−c) |

### Population Scenario Semantics

- **pop_1**: Single population; individuals pair within the same population
- **pop_2**: Two coevolving populations; all pairing is **between** populations (128 from each per group)
- **pop_3**: One evolving + one fixed; file_set _1 is held at 25% each of C0P0/C0P1/C1P0/C1P1

### Partner Choice Bottleneck

Swaps require `C1P1` on **both** sides. Two `C1P1` individuals paired with C0s can swap so both get cooperator partners. When cooperators are rare, swap opportunities are scarce — this creates a positive feedback threshold (see sharp phase transition in prisoners pop_2).

### Mutualism Payoff Asymmetry

In mutualism, population *i* receives the **partner's** benefit, not its own:
- Pop 0's R−P = b₁−c (partner's parameter)
- Pop 1's R−P = b₀−c (partner's parameter)

Since b₁−c ≥ b₀−c by construction, population 0 always has the higher cooperation incentive.

## Figure Pipeline (graphgen)

Figures are generated by `../graph/graphgen/studies/{study}/manifest.py`. Key files:
- `../graph/graphgen/studies/{study}/manifest.py` — `MAIN_ROWS` defines panel layout (row → population, file_set, trait, renderer)
- `../graph/graphgen/studies/trps/config.py` — shared trait definitions
- `../graph/graphgen/studies/common/shared.py` — common path template

Renderers: `imshow` for heatmaps (prisoners/mutualism), `plot` for line plots (hamilton).
