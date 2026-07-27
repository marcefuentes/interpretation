# Manuscript Roadmap

From the current scaffold to a finished manuscript. Companion to outline.md
(structure) and figures.md (figure provenance). Status legend: [ ] todo,
[~] in progress, [x] done.

## Framing decisions (locked 2026-07)

- **Central contribution (relocked 2026-07 after the crossed-asymmetry study):** the
  cost of enforcement is **not borne privately**. Enforcement machinery is itself
  costly, and because enforcement operates *between* populations, a single
  population's information cost governs the cooperation of both — which population
  that is depends on the mechanism family. Behaviour–mechanism decoupling is retained
  as the *mechanism* of this result rather than as the headline: shedding the
  apparatus relieves the payer and withdraws the service the partner depended on.
  Corollaries carried in the main text: enforcement budgets are non-fungible and
  non-convex (concentrating beats splitting), and role assignment under crossed
  asymmetry stays with the cooperation-cost gap.
  - *Superseded framing:* information-cost axis with decoupling as the headline.
    Decoupling sits close to established second-order free-rider results; the
    relational finding requires the two-population design with independent
    per-population cost axes, which is what this corpus uniquely has, and it subsumes
    the existing "partner choice assorts, reciprocity remembers" distinction as its
    explanation.
- **Presentation strategy:** single central claim with the sweep axes demoted to
  **boundary conditions**, not a systematic factorial tour. Every de-emphasised axis
  appears as a robustness statement in main-text prose plus a supplement panel.
  Conditions where the effect *vanishes* (snowdrift; non-zero Cost0) are reported in
  the main text, not hidden in the supplement — the journal and
  `ai/verify_claims.py` keep every de-emphasised condition auditable.
- **Venue / type:** full research article, specialist theoretical-biology / evolution
  journal. Implies ~5-7 main figures, a complete Methods, and a supplement.
- **Scope:** one manuscript — baseline cooperation-cost sweeps (single and two
  populations) plus the full information-cost programme (information cost × cooperation
  cost at equal cooperation cost; information cost under cooperation-cost asymmetry;
  per-population information cost at symmetric cooperation cost; both costs
  asymmetric); supplement = robustness panels (shuffle, groupsize, dilemma-0 control)
  plus an attribution table.
- **Calibration sweeps:** auxiliary only. They justify the payoff-gap attributions
  (M risk-limited, P limited by R − P, combined reward-limited) and live in the
  journal only. Cite in Methods/Results prose and the supplement table; do not
  publish payoff-plane figures.
- **Retired split (2026-07):** we had considered separate papers for the
  information-cost axis and for two-population exploitation asymmetry. The unified
  article covers both.

## Narrative arc (for this framing)

1. Cooperation between non-kin needs enforcement (reciprocity, partner choice,
   reputation), and models normally treat that machinery as free.
2. Baseline: how each mechanism sustains cooperation as cooperation cost rises, in
   one population and two (equal and unequal cooperation cost between populations),
   including how partner choice creates or converts the cooperator/exploiter asymmetry
   and why the cooperating side is often the less fit one.
3. Make the machinery costly. On the symmetric branch information cost looks like a
   private burden: it erodes the apparatus while cooperation persists through tax-free
   unconditional cooperators, so behaviour and mechanism decouple. Note the
   methodological limit — a symmetric design *cannot* separate the cost a population
   pays from the cost its partner pays, which motivates the per-population sweep.
4. **Headline:** sweep information cost per population and the burden turns out to be
   relational. One cost axis governs both populations, and which one depends on the
   mechanism family: under partner choice a population is nearly insensitive to its own
   cost and collapses under its partner's, because assortment is a service needing
   active carriers on both sides and the pair is limited by whichever supplies fewer;
   reciprocity-bearing mechanisms protect only their carriers, so their binding axis is
   the focal population's own. The dilemma-0 control shows the coupling is created by
   the dilemma, not by the cost accounting.
5. Consequences: enforcement budgets are non-fungible and non-convex (splitting is
   worse than concentrating); and the escape route from step 3 is what makes the cost
   destructive in step 4 — shedding relieves the payer and withdraws the partner's
   service.
6. Boundary conditions: the effect needs a genuine dilemma (snowdrift removes the
   wedge); role inversion needs the cheap-cooperation-cost side to pay nothing; the
   crossing into the machinery-free state is a bistable threshold, not a slope; shuffle
   and group size locate which loci carry the effect.
7. Payoff-axis attribution is stated in the main text and summarized in a supplement
   table; the calibration sweeps that derive it remain in the journal, not the figure set.

## Phase 0 — framing [x]

Decisions above recorded. Thesis paragraph drafted in outline.md.

## Phase 1 — figure set (do before Results prose)

- [x] **Main-text figure list locked (2026-07), five figures.** Line charts carry the
  main text and heatmaps move to the supplement as coverage evidence, because the
  headline claims are dose-response comparisons and a flat-versus-cliff contrast is not
  legible as a colour field. fig1 (stochastic two-population split), fig2 (deterministic
  split under cooperation-cost asymmetry), fig3 (behaviour–mechanism decoupling), fig4
  (relational result: own versus partner cost strips plus iso-budget non-convexity),
  fig5 (wedge boundary). The single-population hierarchy is figS10. fig4–fig5 are built
  from the `asymmetric_c1_i0_i1_lines` graphgen study (fig4 fused the former strip and
  iso-budget panels into one 2×3). See figures.md for the slot table.
  - [x] Decoupling stays in the main text as fig3 because the relational argument needs
    it as setup — the escape route that relieves the payer is what withdraws the
    service its partner depends on.
  - [x] The bistable threshold is now shown, not just stated. Added opt-in ±1 SD band
    support to the plot renderer (`show_band` source parameter) and enabled it on fig5,
    where the band is wide below the threshold and collapses above it.
  - [x] **figS4 stays in the supplement (locked 2026-07).** The dilemma-0 control carries
    causal attribution for the decoupling claim, but promoting it would break the
    all-line main text and ask readers to parse one heatmap mid-argument. Fig. 3 and
    the Results prose cite figS4 explicitly; the control remains one click away, not
    buried.
- [x] Supplement figure list locked: figS1–figS10 (no-enforcement control for Fig. 2,
  shuffle, gs = 4, dilemma-0 control, parameter-symmetric vs asymmetric line contrast,
  information-cost asymmetry at equal c, the two demoted information-cost heatmaps,
  the full cooperation-cost asymmetry grid behind Fig. 2, and the demoted mechanism
  hierarchy) plus attribution table; cal1–cal2 auxiliary only.
- [x] Generate figures via graphgen; record commands in figures.md.
- [x] Draft captions via graphgen report (`paper/captions.md`).
- [x] Revise captions against the Results write-through (2026-07; source:
  `graphgen/studies/interpretation/manifest.py` `manuscript_report` contexts).

## Phase 2 — prose (scaffold -> manuscript)

- [x] **Methods** — model, payoffs, information cost, IV grid, sweeps↔figures,
  replicates/verification written through (2026-07).
- [x] **Results** — reordered to the outline spine and written through to Figs. 1–5
  (2026-07); journal links retained for number provenance.
- [x] **Introduction** — related work; information cost versus cooperation cost;
  contribution locked to the relational framing (2026-07).
- [x] **Discussion** — interpretation against prior work; limitations; future
  directions (2026-07).

### Phase 2b — related work / references

- [x] Bibliography: reciprocity, partner choice, reputation, cost of cognition /
  second-order free riding, mutualism (`paper/references.bib`).
- [x] Citation system for the repo (`paper/citing.md`; pandoc `[@Key]` → `.bib`).
- [x] Position information-cost contribution against prior work (Intro + Discussion).

## Phase 3 — front matter and polish

- [x] **Abstract and title** — [frontmatter.md](frontmatter.md);
  structured mirror in [summary.md](summary.md).
- [x] **Author list, affiliations, keywords** — Marcelino Fuentes, Department of
  Biology, University of A Coruña, A Coruña, Spain; marcelino.fuentes@udc.es.
- [x] **Consistency pass; ai/verify_claims.py; link check** — 353 passed, 0 failed,
  0 skipped (2026-07; missing asymmetric_c1_i `.con` exports warmed from raw CSVs;
  M-suppressed census scoped to condition blocks with both M and `_` present).
  Journal links from `paper/` resolve; no internal study-name leakage in
  Intro/Results/Discussion/front matter.
- [x] **Supplement cross-referencing** — [supplement.md](supplement.md) (Figs. S1–S10
  anchors + Table S1 attribution); captions already revised against Results.
- [x] **Target-journal formatting** — portable pandoc assembly notes in
  [formatting.md](formatting.md); venue-specific class/CSL deferred until journal
  chosen.

## Open items / risks

- **Venue TBD** — pick journal + CSL before submission (formatting.md).
- **Tooling stays authoritative** — headline numbers trace to journal + verify_claims.py.

## Definition of done

Submittable IMRaD prose, finalized figures, referenced Introduction/Discussion,
assembled supplement, abstract/title, green verify_claims.py — **met in-repo**
aside from journal-specific template.

## Suggested order

Phase 3 complete for in-repo manuscript readiness. Remaining submission chore:
pick venue + CSL, run pandoc assembly from formatting.md.
