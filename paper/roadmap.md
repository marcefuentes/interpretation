# Manuscript Roadmap

From the current scaffold to a finished manuscript. Companion to `outline.md`
(structure) and `figures.md` (figure provenance). Status legend: [ ] todo,
[~] in progress, [x] done.

## Framing decisions (locked 2026-07)

- **Central contribution:** the information-cost axis — enforcement machinery is
  itself costly, giving a *price* (Cost) versus *demand* (c) view of cooperation, and
  the finding that behaviour and mechanism decouple (cooperation can persist through
  unconditional cooperators after the machinery is taxed away).
- **Venue / type:** full research article, specialist theoretical-biology / evolution
  journal. Implies ~5-7 main figures, a complete Methods, and a supplement.
- **Scope:** one manuscript — main text = hamilton + mutualism (baseline demand and
  two-population roles) + hamilton_cost + mutualism_cost (price–demand in symmetric
  and asymmetric settings); supplement = prisoners/snowdrift payoff-axis calibration
  and the gs=4 / shuffle robustness.
- **Retired split (2026-07):** we had considered a price–demand paper (hamilton only)
  and a separate asymmetry/exploitation paper (mutualism + hamilton diagonal).
  mutualism_cost is price–demand data on the asymmetric branch, so it belongs in the
  unified article, not a second publication.

## Narrative arc (for this framing)

1. Cooperation between non-kin needs enforcement (reciprocity, partner choice,
   reputation), and models normally treat that machinery as free.
2. Baseline: how each mechanism sustains cooperation as the cooperation cost c rises,
   in one population (hamilton) and two (mutualism), including the cooperator/exploiter
   asymmetry.
3. Headline: make the machinery itself costly (hamilton_cost; mutualism_cost on the
   asymmetric branch). Information cost is soft alone but compounds with cooperation
   cost (price starves the defence demand requires), and taxing the machinery erodes
   the apparatus while cooperation can persist — behaviour and mechanism decouple;
   under built-in roles, Cost also modulates cooperation and fitness gaps between
   populations.
4. The payoff-axis attribution (why each mechanism has the threshold it does) is the
   mechanistic backbone; stated in the main text as established, derived in the
   supplement (prisoners/snowdrift).

## Phase 0 — framing [x]

Decisions above recorded. Thesis paragraph drafted in `outline.md`.

## Phase 1 — figure set (do before Results prose)

- [ ] Finalize the main-text figure list from the candidates in `figures.md` (target
  ~5-7): baseline cooperation-vs-c per mechanism; two-population role split
  (cooperation + fitness); the Cost x c / Cost x c1 landscapes; the allele-erosion /
  decoupling panel; the dilemma-0 control decomposition; optional asymmetry-under-Cost
  panel (cooperation and fitness gaps vs Cost).
- [ ] Decide the supplement figure list (payoff-axis fits; gs=4/shuffle mirrors).
- [ ] Generate the chosen figures via graphgen; record exact commands + output paths
  in `figures.md` (already templated there).
- [ ] Draft one-sentence captions, each traceable to a `journal/` doc (and a
  verify_claims.py check).

## Phase 2 — prose (scaffold -> manuscript)

- [ ] **Methods** — closest to done; complete the model description, the IV grid, and
  the replicate/verification paragraph. Link constants to `journal/parameterization.md`.
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
- [ ] Choose a citation system for the repo (e.g. a `paper/references.bib` +
  pandoc-citeproc, or inline). Decide before writing Introduction/Discussion.
- [ ] Position the information-cost contribution against existing "cost of the
  machinery" treatments.

## Phase 3 — front matter and polish

- [ ] Abstract and title.
- [ ] Author list, affiliations, keywords.
- [ ] Consistency pass; run `ai/verify_claims.py` (numbers) and the link check.
- [ ] Supplement assembly (calibration + robustness), cross-referenced from main text.
- [ ] Target-journal formatting (length, figure specs, reference style).

## Pending simulations — mutualism_cost (submitted 2026-07)

We are waiting on **mutualism_cost_1run** (then **mutualism_cost**, Runs = 30) to
close the price–demand question under **built-in asymmetry**. hamilton_cost covers
only the symmetric diagonal (c0 = c1); it cannot say how information cost interacts
with the deterministic cooperator/exploiter split in mutualism pop_2.

**Design:** c0 fixed at 0.10; sweep Cost and c1 (c1 > c0) on the triangular grid
Cost + c1 ≤ 0.40 — 120 cells per leaf, ~8,640 jobs total across mutualism_short +
mutualism_long layouts. Same mechanisms, dilemmas, groupsizes, and shuffle conditions
as mutualism.

**What it unlocks for the manuscript:**

- Price–demand under pinned roles: does Cost shift the c1-collapse threshold the same
  way it shifts c on the hamilton diagonal (~1.5 c per Cost unit)?
- Cooperation and fitness gaps between populations as Cost rises — provisional 1-run
  data show gaps compressing before full collapse; needs 30-run confirmation.
- Behaviour–machinery decoupling (C1P0 / C1M0) on cooperator vs exploiter sides —
  the result hamilton_cost cannot provide.
- Completes the unified price–demand story (symmetric slice in hamilton_cost,
  asymmetric slice here); not material for a separate publication.

Full specification: journal/mutualism_cost.md. Analysis pipeline to be added when
results land (analyze_mutualism_cost.py, verify_claims checks, graphgen .con).

## Open items / risks

- **mutualism_cost data not yet in** — blocks any claim about Cost under asymmetry;
  hamilton_cost results must not be extrapolated to mutualism pop_2.
- **Related-work layer is absent** — gates Introduction and Discussion; start early.
- **Figure set is provisional** — Results prose depends on it; finalize in Phase 1.
- **Main-text attribution without the calibration** — ensure the supplement is
  referenced wherever the main text asserts a mechanism's limiting payoff gap.
- **Tooling stays authoritative** — any new headline number in the paper must trace to
  a journal doc with a verify_claims.py check; the paper cites, it does not originate
  numbers.

## Definition of done

A submittable manuscript: complete IMRaD prose tied to a finalized figure set, a
referenced Introduction/Discussion, an assembled supplement, an abstract and title,
and a green `ai/verify_claims.py` with every main-text number traceable to the journal.

## Suggested order

Phase 1 (figures) and Phase 2b (start the bibliography) in parallel first, since both
gate prose; then Methods -> Results -> Introduction -> Discussion; then Phase 3.
