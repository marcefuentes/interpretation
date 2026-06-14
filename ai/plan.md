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

## Larger (blocked on data generation)

7. [~] Snowdrift multi-run study (unblocks the pending snowdrift.md).
   - Maintainer is generating the 30-run snowdrift data (in progress, 2026-06).
   - When done: graphgen .con + write snowdrift_*.md following the prisoners
     calibration template. Snowdrift axes: temptation T - R and the snowdrift
     gap S - P. The prisoners-derived prediction to test: M should be far less
     risk-limited here because high S keeps the sucker gap small.

8. [ ] Regenerate missing .con exports.
   - prisoners gs=4 movie exports so gs=4 transition-zone dynamics can be
     examined (currently gs=128 temporal only). Low priority.
   - (hamilton gs=4 image .con: done 2026-06.)

## Decisions needed from maintainer

- (a) Keep or drop mutualism pop_3 (item 6).
- (b) Is snowdrift in scope enough to justify generating multi-run data (item 7)?

## Suggested order

1-3 immediately (fast, prevent regressions), then 4 (high interpretive payoff,
no new data), then 5-6. Hold 7-8 until the underlying data exists.
