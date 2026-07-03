# interpretation

Documentation and analysis for interpreting TRPS evolutionary simulation outputs —
the evolution of cooperation in a single population and in two potentially
mutualistic populations, across social dilemmas, cost constraints, and ecological
contexts.

Current parameterization: K = 0.5, b = 0.4 fixed, c varies from 0 to b. See
`journal/parameterization.md` for the payoff/folder reference. Old docs from the
previous parameterization are preserved in `legacy/`.

## Two layers: paper and journal

The repository is organised for an eventual IMRaD manuscript, with the detailed
quantitative work kept separate as a running journal.

- **paper/** — the manuscript scaffold (Introduction, Methods, Results, Discussion,
  plus `figures.md`, a text figure manifest). Narrative and concise; it cites the
  journal for every number rather than restating the analysis. Figures are generated
  artifacts and are **not** stored here — `figures.md` records how to reproduce them.
  Start at `paper/outline.md`.
- **journal/** — the analytical record: per-study and per-mechanism write-ups, the
  cross-study synthesis, the parameterization reference, and the framework note that
  fixes the independent- and outcome-variable model. This is where the numbers,
  derivations, and reasoning live, and our record for answering referee questions
  later. Start at `journal/framework.md`.
- **ai/** — agent-only support: analysis scripts, the numeric-claim verifier, and a
  findings quick-reference.
- **legacy/** — archived docs from the previous parameterization (K = 2, c = 1 fixed).
- **.github/copilot-instructions.md** — active repository guidance for agents.

## Journal contents

| File | Role |
| ---- | ---- |
| journal/framework.md | Independent variables and the three outcome variables (the conceptual spine) |
| journal/parameterization.md | Current payoff equations and dilemma-folder reference |
| journal/synthesis.md | Cross-study: maps prisoners/snowdrift payoff axes onto hamilton/mutualism thresholds; information-cost axis |
| journal/hamilton.md | Index + game parameters for the equal-cost diagonal |
| journal/hamilton_partner_choice.md | Mechanism P; PD and snowdrift; pop_1/2/3; groupsize |
| journal/hamilton_reciprocity.md | M, IM, IJM; shuffle effects; IJM groupsize reversal |
| journal/hamilton_combined.md | MP, MPQ, IMP, IJMPQ; hierarchy; IJMPQ symmetry |
| journal/hamilton_cost.md | Cost x c triangular sweep; information cost of the machinery |
| journal/mutualism.md | Index + model overview for the primary two-population study |
| journal/mutualism_partner_choice.md | P: chooser bottleneck, exploitation, groupsize |
| journal/mutualism_reciprocity.md | M (noshuffle + gs=4); IM, IJM (shuffle) |
| journal/mutualism_combined.md | MP, MPQ, IMP, IJMPQ; Pop_1 lift |
| journal/prisoners.md | Calibration index; PD payoff-plane sweep + d0 control |
| journal/prisoners_calibration.md | Payoff-axis attribution; gs=4 mirror |
| journal/prisoners_partner_choice.md | P on the (R, P) sweep; temporal |
| journal/prisoners_reciprocity.md | M, IM, IJM on the (R, P) sweep |
| journal/snowdrift.md | Calibration index; snowdrift payoff-plane sweep |
| journal/snowdrift_calibration.md | Payoff-axis attribution; shuffle/groupsize |
| journal/snowdrift_partner_choice.md | P: robustness, genotypes, pop_2 symmetry breaking |
| journal/snowdrift_reciprocity.md | M, IM, IJM; insensitivity to the sucker payoff S |

## Project framing

- **mutualism** is the primary study (two populations with potentially different
  parameters; the biologically central case).
- **hamilton** is the equal-parameter special case of mutualism (c0 = c1), and the
  single-population baseline.
- **prisoners** and **snowdrift** are auxiliary calibration studies used to interpret
  mechanisms and signatures seen in mutualism and hamilton.
- **hamilton_cost** extends hamilton with the information-cost axis.

Each study has a multi-run average (30 runs) and a single-run variant (`*_1run`) for
temporal inspection.

## Related repositories (same machine)

- **~/code/trps/** — C simulation source code.
- **~/results/** — simulation output. Metadata in `*.glo`, raw data in `*.csv`,
  pre-processed summaries in `*.con`. Layout:
  `~/results/{study}/{shuffle}/{groupsize}/{mechanism}/{dilemma}/{population}/`.
- **~/code/graph/graphgen/** — figure pipeline, study manifests, mech_trait_map.csv.

## Documentation conventions

For human-facing Markdown (the journal and paper docs), format tables for source
readability as well as rendered output: prefer aligned pipe tables with consistent
spacing so the raw `.md` stays easy to scan and edit in a terminal.

## Verifying numeric claims

Headline numbers in the journal are regression-checked against the `.con` data by
`ai/verify_claims.py`. Run it before committing any doc edit that touches a number;
it exits non-zero on any prose/data mismatch:

```bash
python3 ai/verify_claims.py            # all studies
python3 ai/verify_claims.py mutualism  # filter by substring
```

When you change or add a headline number, add or update the matching check. Shared
loaders/stats live in `ai/trps_io.py`. Checks whose `.con` is missing report SKIP
rather than fail (regenerate the export to activate them).
