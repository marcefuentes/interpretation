# Next Steps Plan

Roadmap for the interpretation repo after the prisoners calibration work.
Status legend: [ ] todo, [~] in progress, [x] done.

## Near-term (cheap, no new data)

1. [x] Wire the verifier into the workflow.
   - Expanded ai/verify_claims.py to 82 checks: diagonal_combined (gs=128 +
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

- diagonal gs=4 .con were briefly missing; regenerated 2026-06 (170 .con). All
  gs=4 diagonal doc claims now verify.

## Medium

4. [x] Cross-study synthesis doc (synthesis.md).
   - Wrote synthesis.md: master attribution table + per-axis sections (M->risk
     P, P->R-P, combined->reward R), the two-perturbation framework (shuffle
     removes M, gs=4 removes P), and the two routes to the role split. Linked
     from README and the diagonal/mutualism/prisoners indexes.

5. [x] Validate the remaining mechanistic narratives.
   - Done in ai/validate_mechanisms.py (+ 5 regression checks in verify_claims.py).
   - Cross-population hitchhiking: CONFIRMED (Pop_1 M1=0.370 < control 0.500
     while cooperating at 0.616; gradient = the 0.001/round M-locus cost).
   - IJMPQ shuffle robustness: behavioral claim confirmed; mechanism CORRECTED —
     the recovery is carried by J (lifetime indirect, +0.133 Pop_1), not Q
     (+0.007). Fixed mutualism_combined.md. Diagonal high-c window is synergistic
     (J/Q epistatic), so diagonal_combined.md phrasing stays.

6. [x] Resolve mutualism pop_3: DROP (maintainer: redundant with diagonal pop_3).
   - Docs already frame it as redundant ("use Diagonal pop_3"); no further data
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
   diagonal/mutualism/prisoners/snowdrift headline numbers reproducing exactly.

10. [x] snowdrift multi-run confirmed present (Runs=30); all snowdrift doc claims verify.
    Updated the stale "snowdrift is single-run only / dir empty" notes in findings.md and
    copilot-instructions.md.

11. [x] symmetric_cost + symmetric_cost_1run (new information-cost study).
    - Wrote symmetric_cost.md; added the price-vs-demand section to synthesis.md.
    - ai/analyze_symmetric_cost.py + 14 regression checks.
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
    - Headline result: the soft Cost effect from symmetric_cost depends on the c = 0
      refuge. With c0 fixed at 0.10 on the asymmetric branch, Cost retreats the c1
      ceiling immediately, compresses the cooperation/fitness split, and leaves much
      less behavior-mechanism decoupling.
    - Related framework, synthesis, README, and paper notes updated to treat
      mutualism_cost as part of the settled manuscript scope.

## Proposed — asymmetric information cost (2026-07)

14. [ ] Asymmetric information-cost study (per-population Cost0, Cost1).
    - **Question.** Existing cost studies tax the machinery symmetrically (a single
      global `Cost` shared by both populations): symmetric_cost sweeps symmetric Cost x
      symmetric c, mutualism_cost sweeps symmetric Cost x asymmetric c1 (c0 = 0.10).
      The empty cell is asymmetric *price*: Cost0 != Cost1. The higher-Cost population
      sheds its enforcement machinery faster (supply-side erosion, see
      journal/symmetric_cost.md), so the novel question is whether it becomes the
      exploiter (free-rides, tax-free) or the exploited (undefended). This is a **third
      route to the cooperator/exploiter role split** — deterministic symmetry breaking
      via the *price* of enforcement, complementing the two routes in
      journal/synthesis.md (stochastic under symmetric payoffs; deterministic via the
      *demand* c0 < c1). Ties directly to the manuscript's price-vs-demand thesis
      (paper/roadmap.md).

    - **Feasibility dependency (code change in ~/code/trps).** The simulation currently
      uses a single scalar `globals->cost`; per-population cost is not supported. Needs:
      add `cost0`/`cost1` to Globals (`~/code/trps/code/src/include/globals.h`), read
      them (`.../modules/read_globals.c`, alongside c0/c1), select on the population
      index in the per-round tax (`.../modules/recruits.c` lines 130-131, where
      `current_pop_index` is already in scope), and extend the `.glo`/CSV headers
      (`.../modules/write.c`, `.../modules/write_ics.c`). Modest, but a source change +
      re-run, not just a new sweep config. Confirm before generating the grid.

    - **Study A (symmetric c, asymmetric Cost) — the clean first study.**
      - pop_2 only. Fix c0 = c1 = c at a positive value so demand bites (c = 0 is a
        near-null: symmetric_cost pop_2 barely breaks symmetry with no temptation).
        **c = 0.10 primary** (nests the Cost0 = Cost1 edge onto symmetric_cost pop_2 at
        c = 0.10, and sits adjacent to mutualism_cost's low-asymmetry edge) plus
        **c = 0.20 secondary** (machinery more load-bearing, so the Cost-asymmetry role
        split should read sharper; guards against a muted signal at c = 0.10).
      - Sweep (Cost0, Cost1) on a **0.02 grid** (matches symmetric_cost / mutualism_cost
        so cells nest exactly).
      - **Ordering triangle Cost0 <= Cost1** (not a full square): under symmetric c the
        populations are exchangeable, so (Cost0, Cost1) and its mirror are the same
        experiment; the triangle avoids redundant runs. The Cost0 = Cost1 edge is the
        pure-Cost axis already covered by symmetric_cost pop_2.
      - **Per-axis cap Cmax = b - c** (LOCKED), i.e. each axis bounded independently by
        the single-family break-even c + Cost = b, beyond which a cooperate-and-enforce
        individual cannot beat the mutual-defection floor K even in its best case
        (mutual coop: K + b - c - Cost < K). NOT the sum-cut Cost0 + Cost1 <= b: the two
        costs are paid by different individuals in different populations, never summed
        within one individual, so the sum-cut would wrongly exclude payoff-feasible
        cells (e.g. c = 0.10, Cost0 = 0.15, Cost1 = 0.25: both have c + Cost_p < b, but
        sum = 0.40). Combined mechanisms (2 x Cost) break even earlier at c + 2 Cost = b;
        as in symmetric_cost, cells past that are kept but read knowing the combined
        strategy is already underwater there.

    - **Study B (crossed asymmetries) — reserved, higher payoff, more expensive.**
      - The headline question: do the two asymmetry axes reinforce or fight? With
        c0 < c1 (built-in cooperator = pop_0) plus asymmetric Cost, does giving the
        natural cooperator the expensive machinery *flip* the role — can the price of
        enforcement override the payoff structure?
      - Requires the **full square** in (Cost0, Cost1) at fixed c-gap: with c0 < c1 the
        populations are no longer exchangeable, so the *sign* of Cost1 - Cost0 matters
        (taxing the cheap cooperator vs the expensive exploiter are different
        experiments, not mirror images).
      - Scope (which c-gap, Cost sub-grid) TBD; do after Study A.

    - **Mechanism-level hypothesis to test.** Partner choice has a built-in role
      asymmetry (chooser vs chosen) that reciprocity lacks, so asymmetric Cost may act
      *directionally* on P (taxing the chooser side != the chosen side) in a way M does
      not — a discriminator between the assortment (P) and history (M) accounts in
      synthesis.md.

    - **Locked decisions (this thread):** per-population Cost0/Cost1; 0.02 grid on
      Cost0, Cost1, c; Study A = symmetric c with ordering triangle Cost0 <= Cost1;
      per-axis cap Cmax = b - c; Study A c = 0.10 primary + c = 0.20 secondary; Study B
      reserved with a full square.
    - **No c = 0 slice** (would land in symmetric_cost's harmless-shedding regime where
      the Cost asymmetry is a near-null; not worth the runs).
    - **Open decisions:** Study B c-gap and Cost sub-grid.

## Newly landed data — diagonal_infocost (2026-07)

15. [ ] diagonal_infocost + diagonal_infocost_1run (line-chart reslice, not yet integrated).
    - Maintainer extracted these from symmetric_cost / symmetric_cost_1run: a fixed
      cooperation-cost slice at c = c0 = c1 = 0.10, sweeping the information cost Cost
      from 0 to 0.30 in 0.02 steps (16 cells). Same diagonal structure otherwise —
      pops 1/2/3, shuffle + noshuffle, gs 128 + 4, dilemmas, the diagonal mechanism set.
      Data and csv_*_for_image.con exports are in ~/results/diagonal_infocost{,_1run}/.
    - Rendered as line charts (x-axis "Information cost") via
      ../graph/graphgen/studies/diagonal_infocost/manifest.py, mirroring the diagonal
      line-chart builder. diagonal_infocost_1run is the single-run temporal companion.
    - Purpose: a presentation variant, not new science. The information-cost findings
      are already analysed on the full Cost x c grid in journal/symmetric_cost.md
      (soft erosion of the machinery, the C1P0/C1M0 free-cooperator niche, the P-vs-M
      split). This gives a clean cooperation-vs-Cost line view at one load-bearing c,
      visually parallel to the existing diagonal cooperation-vs-c line figures.
    - Status: registered here as candidate figure material only. No journal doc,
      analysis script, or verifier checks yet. Consider these as an option if the
      manuscript wants a line-chart companion for the price-of-enforcement axis
      (see paper/figures.md, Fig 4/5 backing symmetric_cost.md). Decide before
      building whether the line reslice adds enough over the m3/m4 heatmaps to earn a
      figure slot.

## Decisions needed from maintainer

- (a) Keep or drop mutualism pop_3 (item 6).
- (b) Is snowdrift in scope enough to justify generating multi-run data (item 7)?
- (c) Study B scope (item 14 open decisions).

## Suggested order

1-3 immediately (fast, prevent regressions), then 4 (high interpretive payoff,
no new data), then 5-6. Hold 7-8 until the underlying data exists.
