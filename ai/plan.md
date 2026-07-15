# Next Steps Plan

Roadmap for the interpretation repo after the prisoners calibration work.
Status legend: [ ] todo, [~] in progress, [x] done.

## Near-term (cheap, no new data)

1. [x] Wire the verifier into the workflow.
   - Expanded ai/verify_claims.py to 82 checks: symmetric_c_combined (gs=128 +
     gs=4 shuffle, snowdrift), asymmetric_c0_c1_combined mean-qB / dominance-count /
     mutual-coop tables, c0 = 0 columns, hitchhiking, J-vs-Q shuffle split,
     prisoners pop_2 paradox of success, and the R+P=1 locus. Documented "run
     before committing doc edits" in README and .github/copilot-instructions.md.
     All 82 checks pass, 0 skipped.

2. [x] Prisoners noise-floor consistency.
   - Added the 30-run SD / SE note to prisoners.md (median qBSeenSD ~0.002-0.016,
     bistable transition cells up to ~0.40 for M; -b/a differences below ~0.03
     not meaningful).

3. [x] Consolidate analysis scripts.
   - Factored shared helpers into ai/trps_io.py; analyze_new_data.py,
     analyze_prisoners.py, and verify_claims.py now import it and produce
     byte-identical output to before.

### Data gap found while expanding the verifier (resolved)

- symmetric_c gs=4 .con were briefly missing; regenerated 2026-06 (170 .con). All
  gs=4 symmetric_c doc claims now verify.

## Medium

4. [x] Cross-study synthesis doc (synthesis.md).
   - Wrote synthesis.md: master attribution table + per-axis sections (M->risk
     P, P->R-P, combined->reward R), the two-perturbation framework (shuffle
     removes M, gs=4 removes P), and the three routes to the role split. Linked
     from README and the symmetric_c/asymmetric_c0_c1/prisoners indexes.

5. [x] Validate the remaining mechanistic narratives.
   - Done in ai/validate_mechanisms.py (+ 5 regression checks in verify_claims.py).
   - Cross-population hitchhiking: CONFIRMED (Pop_1 M1=0.370 < control 0.500
     while cooperating at 0.616; gradient = the 0.001/round M-locus cost).
   - IJMPQ shuffle robustness: behavioral claim confirmed; mechanism CORRECTED —
     the recovery is carried by J (lifetime indirect, +0.133 Pop_1), not Q
     (+0.007). Fixed asymmetric_c0_c1_combined.md. symmetric_c high-c window is synergistic
     (J/Q epistatic), so symmetric_c_combined.md phrasing stays.

6. [x] Resolve asymmetric_c0_c1 pop_3: DROP (maintainer: redundant with symmetric_c pop_3).
   - Docs already frame it as redundant ("use symmetric_c pop_3"); no further data
     or analysis. No write-up will be produced.

## Larger completed data tasks

7. [x] Snowdrift multi-run study (completes snowdrift.md).
   - Wrote snowdrift.md, snowdrift_calibration.md, snowdrift_partner_choice.md, and snowdrift_reciprocity.md following the prisoners template.
   - Identified that direct reciprocity (M) is insensitive to sucker payoff S because TFT only pays it once per pairing (risk determined by P, not S).
   - Confirmed partner choice (P) does not collapse at gs=4 due to the high cooperation floor.
   - Documented extreme pop_2 symmetry breaking exploitation.

8. [x] Regenerate missing con exports.
   - Generated both prisoners gs=4 movie exports and snowdrift gs=4 movie exports using the graphgen pipeline.
   - Removed the gs=4 movie caveats from all prisoners and snowdrift documents.

## Newly landed data (2026-07)

9. [x] All studies migrated to the modern `{shuffle}/{groupsize}` layout; ai/*.py path
   helpers updated to match. verify_claims.py passes 110/110, with all existing
   symmetric_c/asymmetric_c0_c1/prisoners/snowdrift headline numbers reproducing exactly.

10. [x] snowdrift multi-run confirmed present (Runs=30); all snowdrift doc claims verify.
    Updated the stale "snowdrift is single-run only / dir empty" notes in findings.md and
    copilot-instructions.md.

11. [x] symmetric_c_i + symmetric_c_i_1run (new information-cost study).
    - Wrote symmetric_c_i.md; added the information-cost vs cooperation-cost section to synthesis.md.
    - ai/analyze_symmetric_c_i.py + 14 regression checks.
    - Findings: information cost is soft vs cooperation cost (machinery shed harmlessly at
      c=0), family count does not predict collapse (combined most robust), machinery erosion
      decouples behavior from mechanism, and Cost lowers the c-collapse threshold (~1.5 c per
      Cost, not iso-budget). P/M split two ways; snowdrift buffers Cost; gs=4 double-penalizes P.

## Paper restructure (2026-07)

12. [x] Reorganised the repo into two layers for the eventual IMRaD manuscript.
    - paper/ — manuscript scaffold (outline, introduction, methods, results,
      discussion); narrative, cites journal/ for all numbers. results.md is
      organised around the three outcome variables.
    - journal/ — moved all analysis docs (study indexes, mechanism write-ups,
      synthesis.md) plus new.md -> parameterization.md; added framework.md fixing
      the independent variables (dilemma x costs x ecology x mechanism, population
      structure) and the three outcome variables (cooperation level; between-pop
      asymmetry = cooperation + exploitation/fitness; genotype composition / route).
    - Temporal dynamics dropped as a standalone outcome (regime is absorbing-state,
      invariant to population count, and under-instrumented for oscillation).
    - README, copilot-instructions, findings.md updated to the journal/ paths;
      no broken relative links; verifier 121/121.

## Completed — asymmetric_c1_i integration (2026-07)

13. [x] asymmetric_c1_i_1run + asymmetric_c1_i (information cost vs cooperation cost under built-in asymmetry).
    - Analysis now lives in journal/asymmetric_c1_i.md, with regression checks in
      ai/verify_claims.py and support script ai/analyze_asymmetric_c1_i.py.
    - Headline result: the soft Cost effect from symmetric_c_i depends on the c = 0
      refuge. With c0 fixed at 0.10 on the asymmetric branch, Cost retreats the c1
      ceiling immediately, compresses the cooperation/fitness split, and leaves much
      less behavior-mechanism decoupling.
    - Related framework, synthesis, README, and paper notes updated to treat
      asymmetric_c1_i as part of the settled manuscript scope.

## Proposed — asymmetric information cost (2026-07)

14. [x] Asymmetric information-cost study — Study A (asymmetric_i0_i1).
    - **Question.** Per-population Cost0/Cost1 at symmetric c (the supply-side
      counterpart to asymmetric_c1_i's demand asymmetry). See journal/asymmetric_i0_i1.md.
    - **Headline result.** Deterministic role split, but mechanism-dependent: P
      assigns cooperator to low-Cost pop; IJMPQ inverts (cross-population
      hitchhiking). Third route to the role split — updated synthesis.md.
    - ai/analyze_asymmetric_i0_i1.py + 26 regression checks in verify_claims.py
      (183/183 pass on full suite; 12 skipped unchanged).
    - c = 0.20 slice exports (`csv_*_c020_for_image.con`) and 1run movie `.con`
      generated via graphgen `--export-slices`.
    - **Remaining:** Study B (crossed c-gap + Cost square) — see item 15.

15. [x] Study B — crossed asymmetries (`asymmetric_c1_i0_i1`).
    - Fixed c0 = 0.10, c1 = 0.20; full Cost0 x Cost1 square (176 cells at
      per-axis caps Cmax_p = b - c_p: 16 x 11).
    - Cesga setup added; graphgen manifests added (`asymmetric_c1_i0_i1`,
      `asymmetric_c1_i0_i1_1run`).
    - **Headline result.** c-gap is the primary role assigner (P: pop₀ coops in
      170/176 cells). IJMPQ hitchhiking wedge survives only on Cost₀ ≈ 0 strip
      (13 flip cells). journal/asymmetric_c1_i0_i1.md + ai/analyze_asymmetric_c1_i0_i1.py
      + 28 verifier checks.
    - **Remaining:** 1run IJMPQ jobs; graphgen `--export-slices` for .con cache.

## Newly landed data — symmetric_c_i (2026-07)

15. [ ] symmetric_c_i + symmetric_c_i_1run (line-chart reslice, not yet integrated).
    - Maintainer extracted these from symmetric_c_i / symmetric_c_i_1run: a fixed
      cooperation-cost slice at c = c0 = c1 = 0.10, sweeping the information cost Cost
      from 0 to 0.30 in 0.02 steps (16 cells). Same c0 = c1 line structure otherwise —
      pops 1/2/3, shuffle + noshuffle, gs 128 + 4, dilemmas, the symmetric_c mechanism set.
      Data and csv_*_for_image.con exports are in ~/results/symmetric_c_i{,_1run}/.
    - Rendered as line charts (x-axis "Information cost") via
      ../graph/graphgen/studies/symmetric_c_i/manifest.py, mirroring symmetric_c
      line-chart builder. symmetric_c_i_1run is the single-run temporal companion.
    - Purpose: a presentation variant, not new science. The information-cost findings
      are already analysed on the full Cost x c grid in journal/symmetric_c_i.md
      (soft erosion of the machinery, the C1P0/C1M0 free-cooperator niche, the P-vs-M
      split). This gives a clean cooperation-vs-Cost line view at one load-bearing c,
      visually parallel to the existing symmetric_c cooperation-vs-c line figures.
    - Status: registered here as candidate figure material only. No journal doc,
      analysis script, or verifier checks yet. Consider these as an option if the
      manuscript wants a line-chart companion for the information-cost axis
      (see paper/figures.md, Fig 4/5 backing symmetric_c_i.md). Decide before
      building whether the line reslice adds enough over the m3/m4 heatmaps to earn a
      figure slot.

## Decisions needed from maintainer

- (a) Keep or drop asymmetric_c0_c1 pop_3 (item 6).
- (b) Is snowdrift in scope enough to justify generating multi-run data (item 7)?
- (c) Study B scope (item 15 open decisions).

## Suggested order

1-3 immediately (fast, prevent regressions), then 4 (high interpretive payoff,
no new data), then 5-6. Hold 7-8 until the underlying data exists.
