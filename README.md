# interpretation

Methodology and notes for interpreting TRPS simulation outputs: model reference, data paths, and study-specific analyses. Studies include multi-run averages (`hamilton`, `prisoners`, `mutualism`) and single-run variants (`hamilton_1run`, `prisoners_1run`) for tracking temporal dynamics.

This material sits alongside other checkouts on one machine:

- **`../graph/graphgen/`** — figure pipeline, study manifests, `mech_trait_map.csv`, etc.
- **`../trps/`** (or `~/code/trps/`) — C simulation sources
- **`~/results/`** — run outputs (local layout; see `instructions.md`)

Paths in the docs that look like `../graph/graphgen/...` are relative to this repository root.

## Contents

| File | Description |
|------|-------------|
| `instructions.md` | Shared simulation model reference (read first) |
| `instructions_prisoners.md` | Prisoner's Dilemma game parameters, data format, figures |
| `instructions_hamilton.md` | Hamilton altruism game parameters, data format, figures |
| `instructions_mutualism.md` | Mutualism game parameters, cross-benefit payoffs, data format |
| `prisoners.md` | Analysis of PD partner choice results (s07) |
| `hamilton.md` | Analysis of Hamilton partner choice results (s07) |
| `mutualism.md` | Analysis of mutualism partner choice results (s07) |
| `analyze_single_run.py` | Script used to analyze `_1run` temporal dynamics |
