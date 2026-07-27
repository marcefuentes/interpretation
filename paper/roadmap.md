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

- [x] **Main-text figure list locked (2026-07), seven figures.** Line charts carry the
  main text and heatmaps move to the supplement as coverage evidence, because the
  headline claims are dose-response comparisons and a flat-versus-cliff contrast is not
  legible as a colour field. fig1 (single-population hierarchy), fig2 (stochastic
  two-population split), fig3 (deterministic split under cooperation-cost asymmetry),
  fig4 (behaviour–mechanism decoupling), fig5–fig7 (the relational result: own versus
  partner cost, iso-budget non-convexity, wedge boundary). fig5–fig7 are new, built from
  a new `asymmetric_c1_i0_i1_lines` graphgen study; the two demoted heatmaps became
  figS7 and figS8. See figures.md for the slot table.
  - [x] Seven rather than six: decoupling stays in the main text as fig4 because the
    relational argument needs it as setup — the escape route that relieves the payer is
    what withdraws the service its partner depends on.
  - [x] The bistable threshold is now shown, not just stated. Added opt-in ±1 SD band
    support to the plot renderer (`show_band` source parameter) and enabled it on fig7,
    where the band is wide below the threshold and collapses above it.
  - [ ] Decide whether the dilemma-0 control (figS4) is promoted to the main text; under
    this framing it carries the causal attribution rather than being robustness. Would
    make eight main figures, so it likely displaces something.
- [x] Supplement figure list locked: figS1–figS8 (no-enforcement control for Fig. 3,
  shuffle, gs = 4, dilemma-0 control, parameter-symmetric vs asymmetric line contrast,
  information-cost asymmetry at equal c, and the two demoted information-cost heatmaps)
  plus attribution table; cal1–cal2 auxiliary only.
- [x] Generate figures via graphgen; record commands in figures.md.
- [x] Draft captions via graphgen report (`paper/captions.md`); revise when Results
  prose is written to final figures.

## Phase 2 — prose (scaffold -> manuscript)

- [ ] **Methods** — closest to done; complete model, IV grid, replicates/verification.
- [ ] **Results** — write to final figures; cite journal, not internal study names.
- [ ] **Introduction** — related work; information cost versus cooperation cost.
- [ ] **Discussion** — interpretation, limitations, future directions.

### Phase 2b — related work / references (biggest content gap)

- [ ] Bibliography: reciprocity, partner choice, reputation, cost of cognition, mutualism.
- [ ] Citation system for the repo.
- [ ] Position information-cost contribution against prior work.

## Phase 3 — front matter and polish

- [ ] Abstract and title.
- [ ] Author list, affiliations, keywords.
- [ ] Consistency pass; ai/verify_claims.py; link check.
- [ ] Supplement cross-referencing and caption polish.
- [ ] Target-journal formatting.

## Open items / risks

- **Results prose still lags the locked figure set** — Figs. 1–7 and S1–S8 are built and
  captioned, but results.md still orders the relational material as a late finding rather
  than the spine. Reordering is a Phase 2 task, not a rewrite.
- **Related-work layer is absent** — gates Introduction and Discussion.
- **Attribution without calibration figures** — supplement table must carry payoff-gap claims.
- **Tooling stays authoritative** — headline numbers trace to journal + verify_claims.py.

## Definition of done

Submittable IMRaD prose, finalized figures, referenced Introduction/Discussion,
assembled supplement, abstract/title, green verify_claims.py.

## Suggested order

Phase 1 and Phase 2b in parallel; then Methods → Results → Introduction → Discussion → Phase 3.
