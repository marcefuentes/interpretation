# Manuscript Roadmap

From the current scaffold to a finished manuscript. Companion to outline.md
(structure) and figures.md (figure provenance). Status legend: [ ] todo,
[~] in progress, [x] done.

## Framing decisions (locked 2026-07)

- **Central contribution:** the information-cost axis — enforcement machinery is
  itself costly, giving a *price* (Cost) versus *demand* (c) view of cooperation, and
  the finding that behaviour and mechanism decouple (cooperation can persist through
  unconditional cooperators after the machinery is taxed away).
- **Venue / type:** full research article, specialist theoretical-biology / evolution
  journal. Implies ~5-7 main figures, a complete Methods, and a supplement.
- **Scope:** one manuscript — main text = diagonal + mutualism (baseline demand and
  two-population roles) + symmetric_cost + mutualism_cost (price–demand in symmetric
  and asymmetric settings); supplement = robustness panels from the primary studies
  (shuffle, groupsize, dilemma-0 control) plus an attribution table.
- **Calibration studies (prisoners, snowdrift):** auxiliary only. They justify the
  payoff-gap attributions (M risk-limited, P limited by R − P, combined reward-limited)
  and live in journal/prisoners_calibration.md and journal/snowdrift_calibration.md.
  Cite them in Methods/Results prose and the supplement table; do not publish their
  payoff-plane figures.
- **Retired split (2026-07):** we had considered a price–demand paper (diagonal only)
  and a separate asymmetry/exploitation paper (mutualism + diagonal).
  mutualism_cost is price–demand data on the asymmetric branch, so it belongs in the
  unified article, not a second publication.

## Narrative arc (for this framing)

1. Cooperation between non-kin needs enforcement (reciprocity, partner choice,
   reputation), and models normally treat that machinery as free.
2. Baseline: how each mechanism sustains cooperation as the cooperation cost c rises,
   in one population (diagonal pop_1) and two (diagonal pop_2 and mutualism pop_2),
   including how partner choice creates or converts the cooperator/exploiter asymmetry.
3. Headline: make the machinery itself costly (symmetric_cost; mutualism_cost on the
   asymmetric branch). Information cost is soft alone but compounds with cooperation
   cost (price starves the defence demand requires), and taxing the machinery erodes
   the apparatus while cooperation can persist — behaviour and mechanism decouple;
   under built-in roles, Cost also modulates cooperation and fitness gaps between
   populations.
4. Payoff-axis attribution (why each mechanism has the threshold it does) is stated
   in the main text and summarized in a supplement table; the prisoners/snowdrift
   calibration sweeps that derive it remain in the journal, not the figure set.

## Phase 0 — framing [x]

Decisions above recorded. Thesis paragraph drafted in outline.md.

## Phase 1 — figure set (do before Results prose)

- [~] Finalize the main-text figure list from the candidates in figures.md (target
  ~5-7): current draft is m1 (diagonal pop_1 hierarchy), m6 (diagonal pop_2
  stochastic asymmetry under P), m2 (mutualism deterministic split and IJMPQ
  suppression), m3–m5 (symmetric_cost and mutualism_cost price–demand panels) — not
  yet locked.
- [~] Decide the supplement figure list: current draft is ms3–ms5 only (shuffle,
  gs = 4 robustness, symmetric_cost dilemma-0 control) plus a text attribution table;
  no prisoners/snowdrift heatmaps.
- [x] Generate candidate figures via graphgen; record exact commands + output paths
  in figures.md (interpretation study namespace).
- [~] Draft one-sentence captions, each traceable to a journal doc (and a
  verify_claims.py check); revise when the set is finalized.

## Phase 2 — prose (scaffold -> manuscript)

- [ ] **Methods** — closest to done; complete the model description, the IV grid, and
  the replicate/verification paragraph. Link constants to journal/parameterization.md.
  Describe prisoners/snowdrift as orthogonal calibration sweeps (journal only).
- [ ] **Results** — write to the final figures, in the narrative-arc order; keep
  numbers cited to journal docs, not re-derived.
- [ ] **Introduction** — requires the related-work layer (see Phase 2b); frame the
  price-vs-demand question and the three outcomes.
- [ ] **Discussion** — interpretation, limitations (temporal under-instrumentation;
  calibration is structural not literal; pop_3 redundancy), future directions.

### Phase 2b — related work / references (biggest content gap)

- [ ] Assemble a bibliography (no references layer exists yet). Core areas: direct
  reciprocity / TFT, partner choice / biological markets, indirect reciprocity and
  reputation, the cost of cognition / information, and mutualism theory.
- [ ] Choose a citation system for the repo (e.g. a paper/references.bib +
  pandoc-citeproc, or inline). Decide before writing Introduction/Discussion.
- [ ] Position the information-cost contribution against existing "cost of the
  machinery" treatments.

## Phase 3 — front matter and polish

- [ ] Abstract and title.
- [ ] Author list, affiliations, keywords.
- [ ] Consistency pass; run ai/verify_claims.py (numbers) and the link check.
- [ ] Supplement cross-referencing and caption polish in the manuscript text.
- [ ] Target-journal formatting (length, figure specs, reference style).

## Open items / risks

- **Figure set is provisional** — Results prose depends on it; finalize in Phase 1.
- **Related-work layer is absent** — gates Introduction and Discussion; start early.
- **Attribution without calibration figures** — main text must cite the supplement
  table (and journal calibration docs) wherever it asserts a mechanism's limiting
  payoff gap.
- **Tooling stays authoritative** — any new headline number in the paper must trace to
  a journal doc with a verify_claims.py check; the paper cites, it does not originate
  numbers.

## Definition of done

A submittable manuscript: complete IMRaD prose tied to a finalized figure set, a
referenced Introduction/Discussion, an assembled supplement, an abstract and title,
and a green ai/verify_claims.py with every main-text number traceable to the journal.

## Suggested order

Phase 1 (figures) and Phase 2b (start the bibliography) in parallel first, since both
gate prose; then Methods -> Results -> Introduction -> Discussion; then Phase 3.
