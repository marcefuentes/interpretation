# Manuscript Roadmap

From the current scaffold to a finished manuscript. Companion to outline.md
(structure) and figures.md (figure provenance). Status legend: [ ] todo,
[~] in progress, [x] done.

## Framing decisions (locked 2026-07)

- **Central contribution:** the information-cost axis — enforcement machinery is
  itself costly, giving an information-cost versus cooperation-cost view of cooperation, and
  the finding that behaviour and mechanism decouple (cooperation can persist through
  unconditional cooperators after the machinery is taxed away).
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
   including how partner choice creates or converts the cooperator/exploiter asymmetry.
3. Headline: make the machinery itself costly. Information cost is soft alone but
   compounds with cooperation cost, erodes the apparatus while cooperation can persist
   — behaviour and mechanism decouple; under cooperation-cost or information-cost
   asymmetry between populations, information cost modulates cooperation and fitness
   gaps; when both costs differ, the cooperation-cost gap dominates and information
   cost inverts roles only locally.
4. Payoff-axis attribution is stated in the main text and summarized in a supplement
   table; the calibration sweeps that derive it remain in the journal, not the figure set.

## Phase 0 — framing [x]

Decisions above recorded. Thesis paragraph drafted in outline.md.

## Phase 1 — figure set (do before Results prose)

- [~] Finalize the main-text figure list from the candidates in figures.md (target
  ~5-7): m1 (single-population hierarchy), m6 (stochastic two-population split,
  **line chart**), m2 (deterministic split under cooperation-cost asymmetry),
  m3–m5 (information-cost panels) — not yet locked.
- [~] Decide the supplement figure list: ms1–ms5 (shuffle, gs = 4, dilemma-0
  control, parameter-symmetric vs asymmetric line contrast, information-cost
  asymmetry at equal c) plus attribution table; cal1–cal2 auxiliary only.
- [x] Generate candidate figures via graphgen; record commands in figures.md.
- [~] Draft one-sentence captions, each traceable to a journal check; revise when
  the set is finalized.

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

- **Figure set is provisional** — Results prose depends on it.
- **Related-work layer is absent** — gates Introduction and Discussion.
- **Attribution without calibration figures** — supplement table must carry payoff-gap claims.
- **Tooling stays authoritative** — headline numbers trace to journal + verify_claims.py.

## Definition of done

Submittable IMRaD prose, finalized figures, referenced Introduction/Discussion,
assembled supplement, abstract/title, green verify_claims.py.

## Suggested order

Phase 1 and Phase 2b in parallel; then Methods → Results → Introduction → Discussion → Phase 3.
