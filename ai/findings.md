# Agent Orientation

Entry point for future AI sessions. The analytical findings themselves live in
`journal/` (regression-checked by `ai/verify_claims.py`); this file is an index into
them plus the agent-only operational notes. Do not restate journal numbers here — it
creates drift. If a result belongs in the analysis, put it in the relevant
`journal/*.md` and add a verifier check.

## Where things live

- **paper/** — IMRaD manuscript scaffold; cites journal for numbers.
- **journal/** — the analytical record. Start at `journal/framework.md` (the
  independent/outcome-variable model) and `journal/synthesis.md` (cross-study).
- **journal/parameterization.md** — canonical model constants and payoffs
  (verified against `.glo` metadata). Do not restate K/b/Cost elsewhere; link here.
- **ai/** — scripts, this file, `plan.md`.

## Findings index (which journal doc owns what)

| Topic | Journal doc |
| ----- | ----------- |
| Conceptual model: IVs and the three outcomes | framework.md |
| Cross-study payoff-axis attribution; info-cost axis | synthesis.md |
| Diagonal P / M+indirect / combined | diagonal_partner_choice.md, diagonal_reciprocity.md, diagonal_combined.md |
| Information cost of the machinery (Cost x c) | symmetric_c_Cost.md |
| Information cost under asymmetry | asymmetric_c1_Cost.md |
| Mutualism P / M+indirect / combined | mutualism_partner_choice.md, mutualism_reciprocity.md, mutualism_combined.md |
| Prisoners payoff-plane calibration | prisoners_calibration.md, prisoners_partner_choice.md, prisoners_reciprocity.md |
| Snowdrift payoff-plane calibration | snowdrift_calibration.md, snowdrift_partner_choice.md, snowdrift_reciprocity.md |

One-line orientation to the headline results (see the docs for numbers and checks):
M is risk-limited, P is limited by the cooperation advantage R − P, combined/
reputation-rich mechanisms are reward-limited; two populations lock into a
cooperator/exploiter split (stochastic when symmetric, deterministic when c0 < c1);
information cost erodes the machinery while cooperation can persist through
unconditional cooperators (behaviour/mechanism decoupling).

## Model mechanics (source-validated)

The locus semantics and payoff matrices are validated against `~/code/trps` and
documented in `.github/copilot-instructions.md` (decision precedence J > I > M; the
C0P1 silent carrier; dTFT/dSTFT; the per-family Cost tax in recruits.c). Treat that
section plus `journal/parameterization.md` as the reference; re-validate against
source if the engine changes.

## Analysis scripts

- `ai/analyze_new_data.py` — cross-study analysis (diagonal, mutualism).
- `ai/analyze_prisoners.py` — prisoners payoff-axis calibration.
- `ai/analyze_snowdrift.py` — snowdrift payoff-axis calibration.
- `ai/analyze_symmetric_c_Cost.py` — information-cost axis (Cost x c grid).
- `ai/analyze_asymmetric_c1_Cost.py` — information-cost axis under built-in asymmetry
  (Cost x c1 with c0 fixed).
- `ai/analyze_single_run.py` — temporal dynamics from `*_1run` studies.
- `ai/validate_mechanisms.py` — hitchhiking and IJMPQ-shuffle narrative validation
  (genotype decomposition + source gradient).
- `ai/verify_claims.py` — regression-checks headline journal numbers and the
  parameterization constants against `.con`/`.glo` data (PASS/FAIL/SKIP).
- `ai/trps_io.py` — shared loaders/stats (`load`, `glo`, `any_glo`, `corr`, `ols2`,
  `allele`, `gsum`, `m1sum`).

## Operational notes

- **Verification workflow.** Run `python3 ai/verify_claims.py` before committing any
  doc edit that changes a number. SKIP means the `.con` is absent (not a pass) —
  regenerate it with graphgen. When you add or change a headline number, add or
  update the matching check.
- **Directory layout.** `~/results/{study}/{shuffle}/{groupsize}/{mech}/{dilemma}/{pop}/`
  with `csv_{fset}_for_{image,movie}.con`. Cost is read from `.glo`/`.con` metadata,
  not the path.
- **Regenerating summaries.** graphgen (`~/code/graph`, venv there) writes the
  `csv_*_for_image.con` and `csv_*_for_movie.con` exports; see
  `.github/copilot-instructions.md` for exact commands. The M dilemma-0 control cells
  and gs=4 temporal sets were filled 2026-07 (all diagonal-family and
  prisoners_1run/snowdrift_1run gaps closed).
