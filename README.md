# interpretation

Documentation and analysis for interpreting TRPS evolutionary simulation outputs.
Current parameterization: K = 0.5, b = 0.4 fixed, c varies from 0 to b. See new.md for the change note.
Old docs from the previous parameterization are preserved in legacy/ for reference.

## Repository layout

- **Repository root**: human-facing analysis and reference docs
- **.github/copilot-instructions.md**: active GitHub Copilot repository guidance
- **ai/**: agent-only support material, including analysis scripts and key findings
- **legacy/**: archived docs from the previous parameterization (K=2, c=1 fixed, given folders)
- **new.md**: note documenting the parameterization change

## Active analysis documents

| File          | Status   | Notes                                              |
| ------------- | -------- | -------------------------------------------------- |
| hamilton.md   | Complete | gs=128 only; gs=4 pending graphgen                 |
| mutualism.md  | Complete | gs=128 noshuffle only; shuffle and gs=4 pending    |
| prisoners.md  | Pending  | Simulations still running                          |
| snowdrift.md  | Pending  | Simulations still running                          |

## Related repositories (same machine)

- **~/code/trps/** — C simulation source code
- **~/results/** — simulation output data. Metadata in \*.glo files. Raw data in \*.csv files. Pre-processed data in \*.con files.
- **~/code/graph/graphgen/** — figure pipeline, study manifests, mech_trait_map.csv

## Project framing

- **mutualism** is the primary study (two populations with potentially different parameters; biologically central case).
- **hamilton** is the diagonal/equal-parameter special case of mutualism (c0 = c1).
- **prisoners** and **snowdrift** are auxiliary calibration studies used to interpret mechanisms and signatures seen in mutualism and hamilton, not primary project endpoints.

The repository includes multi-run averages (hamilton, prisoners, mutualism, snowdrift) and single-run variants (hamilton_1run, prisoners_1run, snowdrift_1run, mutualism_1run) for tracking temporal dynamics.

## Documentation conventions

For Markdown files intended for human reading (for example prisoners.md, hamilton.md, and mutualism.md), format tables for source readability as well as rendered output. Prefer aligned pipe tables with consistent spacing when practical, so the raw .md remains easy to scan and edit in a terminal or text editor.

