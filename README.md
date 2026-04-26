# interpretation

Methodology and notes for interpreting TRPS simulation outputs: model reference, data paths, and study-specific analyses.

Project framing:
- **mutualism** is the primary study (two populations with potentially different parameters; biologically central case).
- **hamilton** is the diagonal/equal-parameter special case of mutualism (`b0 - c0 = b1 - c1`).
- **prisoners** and **snowdrift** are auxiliary calibration studies used to interpret mechanisms and signatures seen in mutualism/Hamilton, not primary project endpoints.

The repository includes multi-run averages (hamilton, prisoners, mutualism, snowdrift where available) and single-run variants (hamilton_1run, prisoners_1run) for tracking temporal dynamics.

This material sits alongside other checkouts on one machine:

- **../graph/graphgen/** — figure pipeline, study manifests, mech_trait_map.csv, etc.
- **../trps/** (or ~/code/trps/) — C simulation sources
- **~/results/** — run outputs (local layout; see instructions.md)

Paths in the docs that look like ../graph/graphgen/... are relative to this repository root.

## Repository layout

- **Repository root**: human-facing analysis and reference docs
- **.github/copilot-instructions.md**: active GitHub Copilot repository guidance
- **ai/**: agent-only support material, including analysis scripts

## Contents

| File                          | Description                                                    |
| ----------------------------- | -------------------------------------------------------------- |
| instructions.md             | Shared simulation model reference (read first)                 |
| instructions_prisoners.md   | Prisoner's Dilemma game parameters, data format, figures       |
| instructions_hamilton.md    | Hamilton altruism game parameters, data format, figures        |
| instructions_mutualism.md   | Mutualism game parameters, cross-benefit payoffs, data format  |
| mutualism.md                | Primary analysis: mutualistic interactions with asymmetric populations |
| hamilton.md                 | Special-case analysis: diagonal/equal-parameter slice of mutualism |
| prisoners.md                | Auxiliary calibration: PD partner choice used to interpret mutualism/Hamilton |
| snowdrift.md                | Auxiliary calibration: snowdrift partner choice used to interpret mutualism/Hamilton |
| .github/                    | Active Copilot repository instructions                         |
| ai/analyze_single_run.py    | Script used to analyze _1run temporal dynamics               |
| ai/                         | Additional agent-only support material and analysis scripts    |

## Documentation conventions

For Markdown files intended for human reading (for example prisoners.md, hamilton.md, and mutualism.md), format tables for source readability as well as rendered output. Prefer aligned pipe tables with consistent spacing when practical, so the raw .md remains easy to scan and edit in a terminal or text editor.
