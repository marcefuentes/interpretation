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

| File                         | Status   | Notes                                              |
| ---------------------------- | -------- | -------------------------------------------------- |
| hamilton.md                  | Index    | Links to partner-choice, reciprocity, and combined write-ups |
| hamilton_partner_choice.md   | Complete | gs=128 + gs=4; pop_1/2/3; P mechanism; PD and snowdrift      |
| hamilton_reciprocity.md      | Complete | gs=128 + gs=4; M, IM, IJM; IJM groupsize reversal            |
| hamilton_combined.md         | Complete | gs=128 + gs=4; MP, MPQ, IMP, IJMPQ; IJMPQ symmetry          |
| mutualism.md                 | Index    | Links to partner-choice, reciprocity, and combined write-ups |
| mutualism_partner_choice.md  | Complete | gs=128 noshuffle + gs=4 (P mechanism)                          |
| mutualism_reciprocity.md     | Complete | M (gs=128 noshuffle + gs=4); IM, IJM (shuffle)               |
| mutualism_combined.md        | Complete | gs=128 noshuffle + gs=4 (MP, MPQ, IMP, IJMPQ)                |
| prisoners.md                 | Index    | Calibration study index; PD payoff-plane sweep + d0 control  |
| prisoners_calibration.md     | Complete | Payoff-axis attribution; gs=128 + gs=4 (shuffle/groupsize)  |
| prisoners_partner_choice.md  | Complete | P on (R,P) sweep; gs=128 + gs=4; temporal (1run)            |
| prisoners_reciprocity.md     | Complete | M, IM, IJM on (R,P) sweep; gs=128 + gs=4                    |
| snowdrift.md                 | Pending  | Only single-run (snowdrift_1run) exists; no multi-run .con   |
| synthesis.md                 | Complete | Cross-study: maps prisoners payoff axes onto hamilton/mutualism thresholds |

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

For Markdown files intended for human reading (for example hamilton_*.md, mutualism_*.md, and prisoners_*.md), format tables for source readability as well as rendered output. Prefer aligned pipe tables with consistent spacing when practical, so the raw .md remains easy to scan and edit in a terminal or text editor.

## Verifying numeric claims

Headline numbers in the analysis docs are regression-checked against the .con
data by `ai/verify_claims.py`. Run it before committing any doc edit that
touches a number; it exits non-zero on any prose/data mismatch:

```bash
python3 ai/verify_claims.py            # all studies
python3 ai/verify_claims.py mutualism  # filter by substring
```

When you change or add a headline number, add or update the matching check.
Shared loaders/stats live in `ai/trps_io.py`. Checks whose .con is missing
report SKIP rather than fail (regenerate the export to activate them).
