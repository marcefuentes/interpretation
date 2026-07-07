# Next Steps Plan

Roadmap for the interpretation repo after the prisoners calibration work.
Status legend: [ ] todo, [~] in progress, [x] done.

## Near-term (cheap, no new data)

1. [x] Wire the verifier into the workflow.
   - Expanded ai/verify_claims.py to 82 checks: hamilton_combined (gs=128 +
     gs=4 shuffle, snowdrift), mutualism_combined mean-qB / dominance-count /
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

- hamilton gs=4 .con were briefly missing; regenerated 2026-06 (170 .con). All
  gs=4 hamilton doc claims now verify.

## Medium

4. [x] Cross-study synthesis doc (synthesis.md).
   - Wrote synthesis.md: master attribution table + per-axis sections (M->risk
     P, P->R-P, combined->reward R), the two-perturbation framework (shuffle
     removes M, gs=4 removes P), and the two routes to the role split. Linked
     from README and the hamilton/mutualism/prisoners indexes.

5. [x] Validate the remaining mechanistic narratives.
   - Done in ai/validate_mechanisms.py (+ 5 regression checks in verify_claims.py).
   - Cross-population hitchhiking: CONFIRMED (Pop_1 M1=0.370 < control 0.500
     while cooperating at 0.616; gradient = the 0.001/round M-locus cost).
   - IJMPQ shuffle robustness: behavioral claim confirmed; mechanism CORRECTED —
     the recovery is carried by J (lifetime indirect, +0.133 Pop_1), not Q
     (+0.007). Fixed mutualism_combined.md. Hamilton high-c window is synergistic
     (J/Q epistatic), so hamilton_combined.md phrasing stays.

6. [x] Resolve mutualism pop_3: DROP (maintainer: redundant with hamilton pop_3).
   - Docs already frame it as redundant ("use Hamilton pop_3"); no further data
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
   hamilton/mutualism/prisoners/snowdrift headline numbers reproducing exactly.

10. [x] snowdrift multi-run confirmed present (Runs=30); all snowdrift doc claims verify.
    Updated the stale "snowdrift is single-run only / dir empty" notes in findings.md and
    copilot-instructions.md.

11. [x] hamilton_cost + hamilton_cost_1run (new information-cost study).
    - Wrote hamilton_cost.md; added the price-vs-demand section to synthesis.md.
    - ai/analyze_hamilton_cost.py + 14 regression checks.
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

## Completed — mutualism_cost integration (2026-07)

13. [x] mutualism_cost_1run + mutualism_cost (price–demand under built-in asymmetry).
    - Analysis now lives in journal/mutualism_cost.md, with regression checks in
      ai/verify_claims.py and support script ai/analyze_mutualism_cost.py.
    - Headline result: the soft Cost effect from hamilton_cost depends on the c = 0
      refuge. With c0 fixed at 0.10 on the asymmetric branch, Cost retreats the c1
      ceiling immediately, compresses the cooperation/fitness split, and leaves much
      less behavior-mechanism decoupling.
    - Related framework, synthesis, README, and paper notes updated to treat
      mutualism_cost as part of the settled manuscript scope.

## Decisions needed from maintainer

- (a) Keep or drop mutualism pop_3 (item 6).
- (b) Is snowdrift in scope enough to justify generating multi-run data (item 7)?

## Suggested order

1-3 immediately (fast, prevent regressions), then 4 (high interpretive payoff,
no new data), then 5-6. Hold 7-8 until the underlying data exists.
