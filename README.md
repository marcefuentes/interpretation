# interpretation

Documentation and analysis for interpreting TRPS evolutionary simulation outputs —
the evolution of cooperation in a single population and in two potentially
mutualistic populations, across social dilemmas, cost constraints, and ecological
contexts.

Current parameterization: K = 0.5, b = 0.4 fixed, c varies from 0 to b. See
`journal/parameterization.md` for the payoff/folder reference.

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
- **.github/copilot-instructions.md** — active repository guidance for agents.

## Journal contents

| File | Role |
| ---- | ---- |
| journal/framework.md | Independent variables and the three outcome variables (the conceptual spine) |
| journal/parameterization.md | Current payoff equations and dilemma-folder reference |
| journal/synthesis.md | Cross-study: maps prisoners/snowdrift payoff axes onto symmetric_c/asymmetric_c0_c1 thresholds; information-cost axis |
| journal/symmetric_c.md | Index + game parameters for symmetric_c (equal-cost, c0 = c1) |
| journal/symmetric_c_partner_choice.md | Mechanism P; PD and snowdrift; pop_1/2/3; groupsize |
| journal/symmetric_c_reciprocity.md | M, IM, IJM; shuffle effects; IJM groupsize reversal |
| journal/symmetric_c_combined.md | MP, MPQ, IMP, IJMPQ; hierarchy; IJMPQ symmetry |
| journal/symmetric_c_i.md | Cost x c triangular sweep; information cost |
| journal/asymmetric_c1_i.md | Cost x c1 at fixed c0; information cost under deterministic cooperator/exploiter roles |
| journal/asymmetric_i0_i1.md | Cost0 x Cost1 at symmetric c; supply-side role split |
| journal/asymmetric_c0_c1.md | Index + model overview for the primary two-population study |
| journal/asymmetric_c0_c1_partner_choice.md | P: chooser bottleneck, exploitation, groupsize |
| journal/asymmetric_c0_c1_reciprocity.md | M (noshuffle + gs=4); IM, IJM (shuffle) |
| journal/asymmetric_c0_c1_combined.md | MP, MPQ, IMP, IJMPQ; Pop_1 lift |
| journal/prisoners.md | Calibration index; PD payoff-plane sweep + d0 control |
| journal/prisoners_calibration.md | Payoff-axis attribution; gs=4 mirror |
| journal/prisoners_partner_choice.md | P on the (R, P) sweep; temporal |
| journal/prisoners_reciprocity.md | M, IM, IJM on the (R, P) sweep |
| journal/snowdrift.md | Calibration index; snowdrift payoff-plane sweep |
| journal/snowdrift_calibration.md | Payoff-axis attribution; shuffle/groupsize |
| journal/snowdrift_partner_choice.md | P: robustness, genotypes, pop_2 symmetry breaking |
| journal/snowdrift_reciprocity.md | M, IM, IJM; insensitivity to the sucker payoff S |

## Project framing

- **asymmetric_c0_c1** is the primary study (two populations with potentially different
  parameters; the biologically central case).
- **symmetric_c** is the equal-parameter special case (c0 = c1) of asymmetric_c0_c1 (c0 = c1), and the
  single-population baseline.
- **prisoners** and **snowdrift** are auxiliary calibration studies used to interpret
  mechanisms and signatures seen in asymmetric_c0_c1 and symmetric_c.
- **symmetric_c_i** extends symmetric_c with the information-cost axis.
- **asymmetric_c1_i** extends the information-cost axis to pinned cooperator/exploiter
  roles (fixed c0 = 0.10, sweep c1) and shows where the soft symmetric_c_i Cost effect
  breaks down — see
  journal/asymmetric_c1_i.md. Part of the single unified manuscript (paper/roadmap.md).
- **asymmetric_i0_i1** sweeps asymmetric per-population information cost (Cost0 x
  Cost1) at symmetric cooperation cost (c0 = c1); see journal/asymmetric_i0_i1.md.

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
python3 ai/verify_claims.py symmetric_c  # filter by substring
```

When you change or add a headline number, add or update the matching check. Shared
loaders/stats live in `ai/trps_io.py`. Checks whose `.con` is missing report SKIP
rather than fail (regenerate the export to activate them).
