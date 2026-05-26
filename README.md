# interpretation

Documentation and analysis for interpreting TRPS evolutionary simulation outputs.

Old docs are preserved in legacy/ for reference.

## Repository layout

- **Repository root**: human-facing analysis and reference docs
- **.github/copilot-instructions.md**: active GitHub Copilot repository guidance
- **ai/**: agent-only support material, including analysis scripts
- **legacy/**: archived docs from the previous parameterization (K=2, c=1 fixed, given folders)

## Related repositories (same machine)

- **~/code/trps/** — C simulation source code
- **~/results/** — simulation output data. Raw data in \*.csv files. Pre-processed data in \*.con files.
- **~/code/graph/graphgen/** — figure pipeline, study manifests, mech_trait_map.csv

## Project framing:

- **mutualism** is the primary study (two populations with potentially different parameters; biologically central case).
- **hamilton** is the diagonal/equal-parameter special case of mutualism (c0 = c1).
- **prisoners** and **snowdrift** are auxiliary calibration studies used to interpret mechanisms and signatures seen in mutualism/Hamilton, not primary project endpoints.

The repository includes multi-run averages (hamilton, prisoners, mutualism, snowdrift where available) and single-run variants (hamilton_1run, prisoners_1run, snowdrift_1run) for tracking temporal dynamics.

## Documentation conventions

For Markdown files intended for human reading (for example prisoners.md, hamilton.md, and mutualism.md), format tables for source readability as well as rendered output. Prefer aligned pipe tables with consistent spacing when practical, so the raw .md remains easy to scan and edit in a terminal or text editor.

