# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal topic backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

Generate all manuscript PNGs and publication reports (figures must exist in the
output directory first):

    python -m graphgen.main --study interpretation --all --groupsize 128 --output ~/figures
    python -m graphgen.main --study interpretation --report --groupsize 128 --output ~/figures

The report includes main text Figs 1–7 (fig1–fig7) and supplement Figs S1–S8
(figS1–figS8) in manuscript order, with cross-references in each legend. Calibration
panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx
- Markdown mirror: paper/captions.md (sibling interpretation repo; PNG embeds
  point at the figure output directory used for that run)

The manuscript figure set lives in ../graph/graphgen/studies/interpretation/ as
fig1–fig7 (main text) and figS1–figS8 (supplement). Graphgen ids match how figures
are called in the manuscript (Fig. 1 → fig1, Fig. S1 → figS1). Auxiliary payoff-plane
calibration panels are cal1–cal2 in the same namespace (not published). Underlying
simulation export names in the pipeline config are internal and do not appear in
manuscript prose.

Do not pass --dilemma-type when generating the interpretation study. figS4 intentionally
mixes two dilemma types in one figure.

**Payoff-plane calibration sweeps** are auxiliary — they support the payoff-gap
attributions cited in the text but do not appear as manuscript figures. Regenerate
with `--figure cal1` or `--figure cal2` when needed; see the supplement table and
the journal calibration analyses.

Status: revised 2026-07 — graphgen ids are fig1–fig7 (main) and figS1–figS9
(supplement), matching manuscript labels; calibration panels cal1–cal2 are excluded.
Relational reframe (2026-07): three new line figures added from the
`asymmetric_c1_i0_i1_lines` study and numbered Figs. 5–7; decoupling renumbered to
Fig. 4; two heatmaps demoted to figS7 and figS8. Main text is now seven figures, all
line charts (Fig. 3 converted 2026-07; full c0 × c1 grid demoted to figS9).

## Setup audit (2026-07)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| fig1 | Line (PLOT) | symmetric_c pop_1, _/P/M/IJMPQ | Mechanism hierarchy with no-enforcement control column |
| fig2 | Line (PLOT) | symmetric_c pop_2, _/P | Control + partner choice; 2×4 panels (coop/fitness × no enforcement/P) |
| fig3 | Line (PLOT) | asymmetric_c0_c1_lines pop_2, P + IJMPQ at c1 = c0 + 0.02 | Both pops overlaid; full grid → figS9 |
| fig4 | Line (PLOT) | symmetric_c_i_lines pop_1, P + M at c = 0 | Correct — machinery vs cooperation decoupling |
| fig5 | Line (PLOT) | asymmetric_c1_i0_i1_lines pop_2, P + IJMPQ | Own- vs partner-cost strips, both populations overlaid |
| fig6 | Line (PLOT) | asymmetric_c1_i0_i1_lines pop_2, IJMPQ + P | Iso-budget split at a fixed total of 0.2 |
| fig7 | Line (PLOT) | asymmetric_c1_i0_i1_lines pop_2, IJMPQ | Wedge family, i0 fixed per panel; ±1 SD bands |
| figS1 | Heatmap | asymmetric_c0_c1 pop_2, _ | No enforcement; contrast for fig3 |
| figS2 | Line | symmetric_c pop_1, shuffle | Short-memory robustness |
| figS3 | Heatmap | asymmetric_c0_c1 pop_2, P, gs = 4 | Small-group robustness |
| figS4 | Heatmap | symmetric_c_i pop_1, M, dt 0 vs 1 | Dilemma-0 control |
| figS5 | Line (PLOT) | asymmetric_c0_c1_lines pop_2, P | Row 0: c1 = c0 + 0.02; row 1: c0 = c1 |
| figS6 | Heatmap | asymmetric_i0_i1 pop_2, P + IJMPQ | i0 × i1 at c0 = c1 = 0.10; P vs IJMPQ inversion |
| figS7 | Heatmap | symmetric_c_i pop_1, IJMPQ | Cost × c grid; demoted from main text |
| figS8 | Heatmap | asymmetric_c1_i pop_2, P | c1 × Cost with c0 fixed; demoted from main text |
| figS9 | Heatmap | asymmetric_c0_c1 pop_2, P + IJMPQ | Full c0 × c1 grid; demoted from Fig. 3 |
| cal1, cal2 | Heatmap | prisoners / snowdrift calibration | Auxiliary — not in supplement |

### Main-text set, locked 2026-07

Line charts carry the main text; heatmaps move to the supplement as full-coverage
evidence. Seven main figures, all line charts. The dilemma-0 control (figS4) stays in
the supplement so the main text never mixes renderers; Fig. 4 cites it for the
decoupling attribution.

| Fig | Content | Renderer | Was |
| --- | ------- | -------- | --- |
| 1 | Mechanism hierarchy, single population | line | fig1 |
| 2 | Stochastic role split under parameter symmetry | line | fig2 |
| 3 | Deterministic split under cooperation-cost asymmetry | line | fig3 (was heatmap) |
| 4 | Behaviour–mechanism decoupling | line | old fig5 (was heatmap) |
| 5 | **Headline:** information cost is relational | line | new |
| 6 | Shared budget worse than concentrated | line | new |
| 7 | Wedge boundary and its closing | line | new |

Decoupling stays in the main text as slot 4 because the relational argument needs it as
its setup: the escape route that relieves the payer is exactly what withdraws the
service its partner depends on, so Figs. 5–7 price a mechanism Fig. 4 establishes.

Demoted: old fig3 heatmap → **figS9** (full c0 × c1 triangle), old fig4 → **figS7**
(information × cooperation cost square), old fig6 → **figS8** (information cost under
fixed cooperation-cost asymmetry). The crossed `asymmetric_c1_i0_i1` square remains
available as coverage evidence for Figs. 5–7.

**Line vs heatmap balance.** Main text: seven line figures (1–7). Supplement: two line
figures (figS2, figS5) and seven heatmaps (figS1, figS3, figS4, figS6, figS7, figS8,
figS9).

**Dilemma rows.** Single-row figures (fig1, fig2, figS7, figS2) stack prisoner's dilemma
(row 0) and snowdrift (row 1). Multi-row figures keep their existing row semantics
(mechanism, population, or line-slice contrasts). figS4 intentionally compares dilemma 0
versus prisoner's dilemma only; fig4 is mechanism rows (P then M), not a dilemma
contrast. Figs. 5–7 are prisoner's dilemma only, since the relational claim is about
what enforcement adds to a dilemma.

**Not yet wired.** The full i0 × i1 square under crossed cost asymmetry remains
journal-backed and regression-checked but has no interpretation-namespace heatmap; Figs.
5–7 now reslice it as lines instead. The symmetric_i study provides an information-cost
line reslice at c = 0.10 (presentation-only alternative to the fig4/figS7 heatmaps).

## Main text figures

| Fig | Message | Figure id | Command | Output | Journal backing |
| --- | ------- | --------- | ------- | ------ | --------------- |
| 1 | Equal cooperation cost: mechanism hierarchy (single population) | fig1 | `python -m graphgen.main --study interpretation --figure fig1 --groupsize 128 --output ~/figures` | ~/figures/interpretation/fig1.png | Baseline partner choice, reciprocity, combined |
| 2 | Outcome asymmetry under parameter symmetry (c0 = c1), partner choice | fig2 | `... --figure fig2 ...` | ~/figures/interpretation/fig2.png | Two populations, equal cooperation cost |
| 3 | Deterministic outcome split under cooperation-cost parameter asymmetry | fig3 | `... --figure fig3 ...` | ~/figures/interpretation/fig3.png | Cooperation-cost asymmetry |
| 4 | Behaviour–mechanism decoupling where cooperation cost is zero | fig4 | `... --figure fig4 ...` | ~/figures/interpretation/fig4.png | Information cost sweep |
| 5 | Information cost is relational: whose cost binds depends on the mechanism | fig5 | `... --figure fig5 ...` | ~/figures/interpretation/fig5_qBSeen.png | Crossed cost asymmetries |
| 6 | A shared enforcement budget is worse than a concentrated one | fig6 | `... --figure fig6 ...` | ~/figures/interpretation/fig6_qBSeen.png | Crossed cost asymmetries |
| 7 | The role inversion is confined to a wedge | fig7 | `... --figure fig7 ...` | ~/figures/interpretation/fig7_qBSeen.png | Crossed cost asymmetries |

### Panel order notes

1. fig1: columns = no enforcement (_), M, P, IJMPQ (increasing robustness to c); single coevolving population; row 0 = prisoner's dilemma, row 1 = snowdrift.
2. fig2: line chart, two coevolving populations at c0 = c1; columns = no enforcement (_)
   then partner choice (P), each expanded by cooperation and fitness (`multi_trait` → 2×4
   panels). Row 0 = prisoner's dilemma, row 1 = snowdrift. **PD:** partner choice
   stochastically assigns cooperator and exploiter roles absent in the left control columns.
   **Snowdrift:** outcome asymmetry already present without enforcement; P mainly reshapes
   high-c regimes. Fitness can invert (paradox of success).
3. fig3: **c1 = c0 + 0.02 strip**, prisoner's dilemma only; rows = P then IJMPQ;
   both populations overlaid (orange = cheap c0, red = expensive c1); columns =
   cooperation, fitness. Contrast with fig2 (PD row): deterministic outcome split;
   IJMPQ lifts the expensive population. Full c0 × c1 triangle → figS9. **Why no
   snowdrift row:** the cheap population already cooperates at ceiling under no
   enforcement (~0.96), so partner choice adds little beyond the payoff floor;
   between-population snowdrift asymmetry is shown in fig2 (row 1) and figS1 instead.
4. fig4: rows = P then M; columns = machinery allele then cooperation; **c = 0 slice**
   sweeping information cost (Cost 0 → b). Full Cost × c grid → figS7.
5. fig5: rows = P then IJMPQ; columns = i0 taxed then i1 taxed; both populations overlaid.
6. fig6: rows = IJMPQ then P; iso-budget split at a fixed total of 0.2.
7. fig7: IJMPQ; columns = i0 held at 0, 0.02, 0.04, 0.1 while i1 is swept; ±1 SD bands.
   - figS7: IJMPQ; row 0 = prisoner's dilemma, row 1 = snowdrift; information cost × cooperation cost grid.
   - figS8: rows = high- then low-cooperation-cost population under P; information cost with c0 fixed.

### Exact commands for the main-text set

1. Fig 1 — fig1
   - python -m graphgen.main --study interpretation --figure fig1 --groupsize 128 --output ~/figures
2. Fig 2 — fig2
   - python -m graphgen.main --study interpretation --figure fig2 --groupsize 128 --output ~/figures
3. Fig 3 — fig3
   - python -m graphgen.main --study interpretation --figure fig3 --groupsize 128 --output ~/figures
4. Fig 4 — fig4
   - python -m graphgen.main --study interpretation --figure fig4 --groupsize 128 --output ~/figures
5. Fig 5 — fig5
   - python -m graphgen.main --study interpretation --figure fig5 --groupsize 128 --output ~/figures
6. Fig 6 — fig6
   - python -m graphgen.main --study interpretation --figure fig6 --groupsize 128 --output ~/figures
7. Fig 7 — fig7
   - python -m graphgen.main --study interpretation --figure fig7 --groupsize 128 --output ~/figures

Figs 3–7 need the line-slice caches warmed first; see the sections below.

## Cooperation-cost asymmetry: line reslice at c1 = c0 + 0.02 (built 2026-07)

Fig. 3 overlays both populations on the asymmetric offset strip rather than the full
c0 × c1 heatmap (figS9). The deterministic cooperator/exploiter split under partner
choice reads immediately as one high and one low curve; IJMPQ lifts the expensive
population on the same axes.

Uses the existing `asymmetric_c0_c1_lines` study with filter `asymmetric_offset`
(c1 = c0 + 0.02). Same slice as figS5 top row; caches live under
`asymmetric_c0_c1/.../csv_*_asymmetric_offset_for_image.con`. Warm with:

```bash
python -m graphgen.main --study asymmetric_c0_c1_lines --export-slices --groupsize 128
```

## Behaviour–mechanism decoupling: line reslice at c = 0 (built 2026-07)

Fig. 4 is a dose-response line chart at zero cooperation cost rather than the full
Cost × c heatmap (figS7). At c = 0 the decoupling reads immediately: machinery alleles
fall while cooperation stays high on unconditional cooperators.

Study `symmetric_c_i_lines` reslices the same `symmetric_c_i` square with filter
`c_zero` (keeps c0 = 0, sweeps Cost). Warm caches with:

```bash
python -m graphgen.main --study symmetric_c_i_lines --export-slices --groupsize 128
```

## Relational information cost: line reslices (built 2026-07)

Under the relational framing the headline claims are dose-response comparisons, so
they are rendered as line charts rather than heatmaps. Reading a *flat* response
against a *cliff* off a colour field is a judgment call; on a shared y-axis it is
immediate, the magnitudes are recoverable, and both populations fit in one panel so a
role inversion reads as one curve crossing another.

These use a new graphgen study, `asymmetric_c1_i0_i1_lines`, which reslices the same
Cost0 × Cost1 square that `asymmetric_c1_i0_i1` renders as heatmaps. Seven named
slices are defined in its `filters.py`; each is a row filter that keeps the fixed
cooperation-cost gap and then cuts one line through the square. Slices get their own
`.con` caches, warmed with:

    python -m graphgen.main --study asymmetric_c1_i0_i1_lines --export-slices --results ~/results

| Fig | Message | Slices used |
| --- | ------- | ----------- |
| 5 | **Headline.** Information cost is relational; which axis binds depends on the mechanism | `tax_on_pop_0`, `tax_on_pop_1` |
| 6 | A shared enforcement budget is worse than a concentrated one | `iso_budget` |
| 7 | The role inversion is confined to a wedge where the cheap population pays nothing | `wedge_c0_000/002/004/010` |

### What each shows

1. **Fig. 5** — 2 × 2. Rows are mechanism (P, then IJMPQ); columns hold one population's
   information cost at zero and sweep the other. The flat panel and the cliff panel
   *swap places* between the rows: partner choice is flat in its own cost and collapses
   under its partner's, the combined mechanism the reverse. In the combined bottom-left
   panel the taxed population's partner falls *further* than the payer does
   (0.957 → 0.268 against 0.957 → 0.734), which is the relational claim at its sharpest.
   Both columns are clipped to the common range 0 ≤ i ≤ 0.2 set by the tighter
   per-population cap b − c_p; the i0 strip extends to 0.30 in the data and stays flat.
   All nine curve endpoints quoted here are pinned in ai/verify_claims.py.
2. **Fig. 6** — 2 × 1, IJMPQ then P. Every x position costs the pair the same total
   (0.2), split differently. IJMPQ dips to an interior minimum well below both ends;
   P is monotone, so the non-convexity belongs to reciprocity-bearing mechanisms
   rather than to the budget.
3. **Fig. 7** — 1 × 4, IJMPQ, i0 fixed per panel. The inversion is the expensive
   population's curve lying above the cheap one's: present throughout at i0 = 0,
   appearing only past a threshold at i0 = 0.02 (visible as a discontinuity), absent
   at 0.04 and 0.1. Shaded ±1 SD bands over 30 runs show the basin boundary directly:
   the band is wide below the threshold (SD 0.249 at i1 = 0, 0.244 at 0.02) and
   collapses above it (0.009 at 0.04).

Bands are opt-in per figure via a `show_band` source parameter, set only on Fig. 7 —
elsewhere the runs sit inside a single basin and a band would only add clutter.

### Superseded: both-costs-asymmetric heatmaps

A full i0 × i1 square (c0 and c1 fixed) is available as imshow heatmaps in graphgen and
remains the full-coverage evidence for the supplement, but the line reslices above now
carry the claims in the main text.

### Available alternative: single-population information-cost line charts at c = 0.10

The information-cost axis also exists as a 1D line-chart reslice at fixed cooperation
cost c = 0.10 (`symmetric_i`). It carries no new numbers beyond the information-cost
sweep journal doc — presentation option only, and unlike Figs. 5–7 it cannot show a
relational effect because it has only one population. See ai/plan.md.

## Supplement figures

Robustness panels from the primary sweeps only. No-enforcement control for Fig. 3 only (figS1); symmetric baseline is in Fig. 2 control columns.

| Supp fig | Message | Figure id | Command | Output |
| -------- | ------- | --------- | ------- | ------ |
| S1 | No-enforcement control for Fig. 3 (asymmetric two populations) | figS1 | `... --figure figS1 ...` | ~/figures/interpretation/figS1.png |
| S2 | Short-memory comparison: direct-reciprocity branch shifts collapse ordering | figS2 | `... --figure figS2 ...` | ~/figures/interpretation/figS2.png |
| S3 | Small groups (gs = 4): cooperation-cost asymmetry under partner choice | figS3 | `... --figure figS3 --groupsize 4 ...` | ~/figures/interpretation/figS3.png |
| S4 | Dilemma-0 control: machinery erodes with and without a social dilemma | figS4 | `... --figure figS4 ...` | ~/figures/interpretation/figS4.png |
| S5 | Parameter-symmetric vs parameter-asymmetric cooperation cost (line slices) | figS5 | `... --figure figS5 ...` | ~/figures/interpretation/figS5.png |
| S6 | Information-cost parameter asymmetry at equal cooperation cost (c = 0.10) | figS6 | `... --figure figS6 ...` | ~/figures/interpretation/figS6.png |
| S7 | Information cost versus cooperation cost, single population (was Fig 4) | figS7 | `... --figure figS7 ...` | ~/figures/interpretation/figS7.png |
| S8 | Information cost under fixed cooperation-cost asymmetry (was Fig 6) | figS8 | `... --figure figS8 ...` | ~/figures/interpretation/figS8.png |
| S9 | Full cooperation-cost asymmetry grid, prisoner's dilemma (was Fig 3) | figS9 | `... --figure figS9 ...` | ~/figures/interpretation/figS9.png |

## Auxiliary calibration figures (not in supplement)

| Figure id | Command | Output |
| --------- | ------- | ------ |
| cal1 (PD payoff plane) | `... --figure cal1 ...` | ~/figures/interpretation/cal1.png |
| cal2 (snowdrift payoff plane) | `... --figure cal2 ...` | ~/figures/interpretation/cal2.png |

## Supplement table (no figure)

Payoff-axis attribution from auxiliary calibration sweeps. Reproduce numbers from
journal synthesis and calibration docs; do not publish full payoff-plane heatmaps.

| Mechanism family | Limiting payoff gap | Journal source |
| ---------------- | ------------------- | -------------- |
| M (direct reciprocity) | Risk / defection payoff P | PD and snowdrift calibration |
| P (partner choice) | Cooperation advantage R − P | PD calibration |
| MP, MPQ, IMP, IJMPQ (combined / reputation-rich) | Reward / temptation R | PD calibration |

## Draft captions

1. Fig 1. At equal cooperation cost, the no-enforcement control and the partner-choice, direct-reciprocity, and reputation-rich combined mechanisms define the threshold hierarchy the rest of the paper explains.
2. Fig 2. Two coevolving populations at equal cooperation cost (c0 = c1). Left columns: no enforcement; right columns: partner choice. In the prisoner's dilemma (top row), partner choice stochastically assigns cooperator and exploiter roles absent in the control columns; the cooperator side can earn lower fitness. In snowdrift (bottom row), a similar split already appears without enforcement; partner choice mainly reshapes outcomes at high cooperation cost.
3. Fig 3. Along c1 = c0 + 0.02 with both populations overlaid, partner choice converts
   the payoff gap into a deterministic cooperator/exploiter split; combined IJMPQ lifts
   the expensive population. Full c0 × c1 grid → Fig. S9.
4. Fig 4. Where cooperation cost is zero, the machinery alleles are selected away before cooperation disappears, so behaviour and mechanism decouple. This is the escape route the next three figures price.
5. Fig 5. Holding one population's information cost at zero and sweeping the other's shows that the binding axis is not the one a population pays: under partner choice each population is nearly flat in its own cost and collapses under its partner's, and under the combined mechanism the two axes swap. Taxing the cheap-cooperation-cost population costs its partner more (0.957 → 0.268) than it costs the payer (0.957 → 0.734).
6. Fig 6. Along a fixed total information-cost budget, the combined mechanism cooperates least at an interior split and most at either extreme, so an enforcement budget is not fungible between populations. Partner choice is monotone, placing the non-convexity with reciprocity rather than with the budget.
7. Fig 7. The role inversion occupies a narrow wedge: it holds when the cheap population pays nothing, survives past a threshold when it pays 0.02, and is gone by 0.04. The ±1 SD bands show runs splitting between two attractors below that threshold.

Supplement captions:

S1. Control baseline for Fig. 3: enforcement off with cooperation-cost parameter asymmetry. Partner choice is what pins the deterministic cooperator/exploiter split.
S2. Short-memory mechanisms shift the direct-reciprocity collapse ordering relative to the baseline hierarchy (Fig 1).
S3. At group size 4, cooperation-cost asymmetry under partner choice preserves the deterministic cooperator/exploiter split.
S4. Under dilemma 0, machinery alleles erode with or without a social dilemma; the decoupling in Fig 4 requires the dilemma case.
S5. Line slices contrast deterministic split under c1 = c0 + 0.02 (top row) with the stochastic split at c0 = c1 (bottom row; same data as Fig 2).
S6. At c0 = c1 = 0.10, information-cost asymmetry (i0 < i1) assigns the cooperator role deterministically under partner choice (top rows); combined IJMPQ inverts via cross-population hitchhiking (bottom rows).
S7. In a single population, information cost is soft by itself but lowers the cooperation-cost ceiling once the two costs overlap. Full-coverage grid behind Fig 4.
S8. With cooperation-cost asymmetry and c0 fixed above zero, the harmless information-cost edge disappears: information cost retreats the cooperation-cost ceiling and compresses the cooperator/exploiter split. Full-coverage grid complementing Figs 5–7, which cross both asymmetries.
S9. Full c0 × c1 cooperation-cost asymmetry grid behind Fig 3; prisoner's dilemma, partner choice and combined IJMPQ rows.
