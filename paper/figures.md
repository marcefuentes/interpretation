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

The report includes main text Figs 1–5 (fig1–fig5) and supplement Figs S1–S11
(figS1–S11) in manuscript order, with cross-references in each legend. Calibration
panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx
- Markdown mirror: paper/captions.md (sibling interpretation repo; PNG embeds
  point at the figure output directory used for that run)

The manuscript figure set lives in ../graph/graphgen/studies/interpretation/ as
fig1–fig5 (main text) and figS1–S11 (supplement). Graphgen ids match how figures
are called in the manuscript (Fig. 1 → fig1, Fig. S3 → figS3). Auxiliary payoff-plane
calibration panels are cal1–cal2 in the same namespace (not published). Underlying
simulation export names in the pipeline config are internal and do not appear in
manuscript prose.

Do not pass --dilemma-type when generating the interpretation study. figS8 intentionally
mixes two dilemma types in one figure.

**Payoff-plane calibration sweeps** are auxiliary — they support the payoff-gap
attributions cited in the text but do not appear as manuscript figures. Regenerate
with `--figure cal1` or `--figure cal2` when needed; see the supplement table and
the journal calibration analyses.

Status: revised 2026-07 — graphgen ids are fig1–fig5 (main) and figS1–S11
(supplement), matching manuscript labels; calibration panels cal1–cal2 are excluded.
The single-population mechanism hierarchy was demoted to **figS1**. Relational
reframe: Fig. 4 is the fused 2×3 (own/partner strips + iso-budget); Fig. 5 tracks the
near-zero-i₀ inversion regime; decoupling is Fig. 3. Main text is five line figures.

## Setup audit (2026-07)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| fig1 | Line (PLOT) | symmetric_c pop_2, _/P | Control + partner choice; 2×4 panels |
| fig2 | Line (PLOT) | asymmetric_c0_c1_lines pop_2, P + IJMPQ at c1 = c0 + 0.02 | Both pops overlaid; full grid → figS4 |
| fig3 | Line (PLOT) | symmetric_c_i_lines pop_1, P + M at c = 0 | Machinery vs cooperation decoupling |
| fig4 | Line (PLOT) | asymmetric_c1_i0_i1_lines pop_2, P + IJMPQ | 2×3: own/partner strips + iso-budget |
| fig5 | Line (PLOT) | asymmetric_c1_i0_i1_lines pop_2, IJMPQ | Wedge family; cooperation + fitness rows with ±1 SD bands |
| figS1 | Line (PLOT) | symmetric_c pop_1, _/P/M/IJMPQ | Mechanism hierarchy (demoted) |
| figS2 | Line | symmetric_c pop_1, shuffle | Short-memory robustness |
| figS3 | Heatmap | asymmetric_c0_c1 pop_2, _ | No enforcement; contrast for fig2 |
| figS4 | Heatmap | asymmetric_c0_c1 pop_2, P + IJMPQ | Full c0 × c1 grid behind Fig. 2 |
| figS5 | Line (PLOT) | asymmetric_c0_c1_lines pop_2, P | Row 0: c1 = c0 + 0.02; row 1: c0 = c1 |
| figS6 | Heatmap | asymmetric_c0_c1 pop_2, P, gs = 4 | Small-group robustness |
| figS7 | Heatmap | symmetric_c_i pop_1, IJMPQ | Cost × c grid |
| figS8 | Heatmap | symmetric_c_i pop_1, M, dt 0 vs 1 | Dilemma-0 control |
| figS9 | Heatmap | asymmetric_c1_i pop_2, P | c1 × Cost with c0 fixed |
| figS10 | Line (PLOT) | asymmetric_c1_i0_i1_lines pop_2, P + IJMPQ | Fitness counterpart of Fig. 4 slices |
| figS11 | Heatmap | asymmetric_i0_i1 pop_2, P + IJMPQ | i0 × i1 at c0 = c1 = 0.10 |
| cal1, cal2 | Heatmap | prisoners / snowdrift calibration | Auxiliary — not in supplement |

### Main-text set, locked 2026-07

Five main line figures. Hierarchy demoted to Fig. S1. Decoupling (Fig. 3) stays as
setup for the relational claim (Figs. 4–5).

| Fig | Content | Renderer | Was |
| --- | ------- | -------- | --- |
| 1 | Stochastic role split under parameter symmetry | line | former fig2 |
| 2 | Deterministic split under cooperation-cost asymmetry | line | former fig3 |
| 3 | Behaviour–mechanism decoupling | line | former fig4 |
| 4 | **Headline:** information cost is relational (strips + iso-budget) | line | fused former fig5+fig6 |
| 5 | Wedge boundary and its closing | line | former fig7 |

## Main text figures

| Fig | Message | Figure id | Command | Output | Journal backing |
| --- | ------- | --------- | ------- | ------ | --------------- |
| 1 | Outcome asymmetry under parameter symmetry (c0 = c1), partner choice | fig1 | `... --figure fig1 ...` | ~/figures/interpretation/fig1.png | Two populations, equal cooperation cost |
| 2 | Deterministic outcome split under cooperation-cost parameter asymmetry | fig2 | `... --figure fig2 ...` | ~/figures/interpretation/fig2.png | Cooperation-cost asymmetry |
| 3 | Behaviour–mechanism decoupling where cooperation cost is zero | fig3 | `... --figure fig3 ...` | ~/figures/interpretation/fig3.png | Information cost sweep |
| 4 | Information cost is relational: whose information cost matters and why shared budgets can perform poorly | fig4 | `... --figure fig4 ...` | ~/figures/interpretation/fig4_qBSeen.png | Crossed cost asymmetries |
| 5 | Role inversion appears only when the cheap population's information cost is near zero (cooperation + fitness rows) | fig5 | `... --figure fig5 ...` | ~/figures/interpretation/fig5_qBSeen.png | Crossed cost asymmetries |

### Panel order notes

1. fig1: two coevolving populations at c0 = c1; columns = no enforcement then P;
   coop/fitness (`multi_trait` → 2×4). Row 0 = PD, row 1 = snowdrift.
2. fig2: c1 = c0 + 0.02 strip, PD only; rows = P then IJMPQ; both populations overlaid.
3. fig3: rows = P then M; columns = machinery allele then cooperation; c = 0 slice.
4. fig4: rows = P then IJMPQ; columns = i0 strip, i1 strip, iso-budget.
5. fig5: IJMPQ; columns = i0 held at 0, 0.02, 0.04, 0.1 while i1 is swept; row 1 = cooperation, row 2 = fitness; both rows show ±1 SD bands.

### Exact commands for the main-text set

1. Fig 1 — fig1 — `python -m graphgen.main --study interpretation --figure fig1 --groupsize 128 --output ~/figures`
2. Fig 2 — fig2 — `... --figure fig2 ...`
3. Fig 3 — fig3 — `... --figure fig3 ...`
4. Fig 4 — fig4 — `... --figure fig4 ...`
5. Fig 5 — fig5 — `... --figure fig5 ...`

Figs 2–5 need the line-slice caches warmed first; see the sections below.

## Cooperation-cost asymmetry: line reslice at c1 = c0 + 0.02 (built 2026-07)

Fig. 2 overlays both populations on the asymmetric offset strip rather than the full
c0 × c1 heatmap (figS4). The deterministic cooperator/exploiter split under partner
choice reads immediately as one high and one low curve; IJMPQ lifts the expensive
population on the same axes.

Uses the existing `asymmetric_c0_c1_lines` study with filter `asymmetric_offset`
(c1 = c0 + 0.02). Same slice as figS5 top row; caches live under
`asymmetric_c0_c1/.../csv_*_asymmetric_offset_for_image.con`. Warm with:

```bash
python -m graphgen.main --study asymmetric_c0_c1_lines --export-slices --groupsize 128
```

## Behaviour–mechanism decoupling: line reslice at c = 0 (built 2026-07)

Fig. 3 is a dose-response line chart at zero cooperation cost rather than the full
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
| 4 | **Headline.** Binding axis (own vs partner cost) and budget non-convexity | `tax_on_pop_0`, `tax_on_pop_1`, `iso_budget` |
| 5 | Role inversion appears only when the cheap population's information cost is near zero | `wedge_c0_000/002/004/010` |

### What each shows

1. **Fig. 4** — 2 × 3. Rows are mechanism (P, then IJMPQ); columns are the i0 strip
   (i1 = 0), the i1 strip (i0 = 0), and the iso-budget split at total 0.2. In the first
   two columns the flat panel and the cliff panel *swap places* between the rows:
   partner choice is flat in its own cost and collapses under its partner's, the
   combined mechanism the reverse. In the combined bottom-left panel the taxed
   population's partner falls *further* than the payer does (0.957 → 0.268 against
   0.957 → 0.734), which is the relational claim at its sharpest. Both strip columns
   are clipped to the common range 0 ≤ i ≤ 0.2 set by the tighter per-population cap
   b − c_p; the i0 strip extends to 0.30 in the data and stays flat. The third column
   holds total information cost fixed: IJMPQ dips to an interior minimum well below
   both ends; P is monotone, so the non-convexity belongs to reciprocity-bearing
   mechanisms rather than to the budget. Curve endpoints quoted here are pinned in
   ai/verify_claims.py.
2. **Fig. 5** — 2 × 4, IJMPQ, i0 fixed per column. Top row is cooperation; the
   inversion is the expensive population's curve lying above the cheap one's: present
   throughout at i0 = 0, appearing only past a threshold at i0 = 0.02 (visible as a
   discontinuity), absent at 0.04 and 0.1. Bottom row is fitness on the same slices,
   showing the corresponding closure of the high-cooperation/low-fitness inversion as
   i0 rises. Shaded ±1 SD bands over 30 runs are shown on both rows to mark the basin
   boundary directly: the cooperation band is wide below the threshold (SD 0.249 at i1
   = 0, 0.244 at 0.02) and collapses above it (0.009 at 0.04).

Bands are opt-in per figure via a `show_band` source parameter, set only on Fig. 5 —
elsewhere the runs sit inside a single basin and a band would only add clutter.

### Superseded: both-costs-asymmetric heatmaps

A full i0 × i1 square (c0 and c1 fixed) is available as imshow heatmaps in graphgen and
remains the full-coverage evidence for the supplement, but the line reslices above now
carry the claims in the main text.

### Available alternative: single-population information-cost line charts at c = 0.10

The information-cost axis also exists as a 1D line-chart reslice at fixed cooperation
cost c = 0.10 (`symmetric_i`). It carries no new numbers beyond the information-cost
sweep journal doc — presentation option only, and unlike Figs. 4–5 it cannot show a
relational effect because it has only one population. See ai/plan.md.

## Supplement figures

Robustness panels from the primary sweeps only. No-enforcement control for Fig. 2 only (figS3); symmetric baseline is in Fig. 1 control columns.

| Supp fig | Message | Figure id | Command | Output |
| -------- | ------- | --------- | ------- | ------ |
| S1 | Mechanism hierarchy at equal cooperation cost (demoted from main text) | figS1 | `... --figure figS1 ...` | ~/figures/interpretation/figS1.png |
| S2 | Short-memory comparison: direct-reciprocity branch shifts collapse ordering | figS2 | `... --figure figS2 ...` | ~/figures/interpretation/figS2.png |
| S3 | No-enforcement control for Fig. 2 (asymmetric two populations) | figS3 | `... --figure figS3 ...` | ~/figures/interpretation/figS3.png |
| S4 | Full cooperation-cost asymmetry grid, prisoner's dilemma (was Fig 3) | figS4 | `... --figure figS4 ...` | ~/figures/interpretation/figS4.png |
| S5 | Parameter-symmetric vs parameter-asymmetric cooperation cost (line slices) | figS5 | `... --figure figS5 ...` | ~/figures/interpretation/figS5.png |
| S6 | Small groups (gs = 4): cooperation-cost asymmetry under partner choice | figS6 | `... --figure figS6 --groupsize 4 ...` | ~/figures/interpretation/figS6.png |
| S7 | Information cost versus cooperation cost, single population (was Fig 4) | figS7 | `... --figure figS7 ...` | ~/figures/interpretation/figS7.png |
| S8 | Dilemma-0 control: machinery erodes with and without a social dilemma | figS8 | `... --figure figS8 ...` | ~/figures/interpretation/figS8.png |
| S9 | Information cost under fixed cooperation-cost asymmetry (was Fig 6) | figS9 | `... --figure figS9 ...` | ~/figures/interpretation/figS9.png |
| S10 | Fitness counterpart of Fig. 4 (same relational slices) | figS10 | `... --figure figS10 ...` | ~/figures/interpretation/figS10_wmean.png |
| S11 | Information-cost parameter asymmetry at equal cooperation cost (c = 0.10) | figS11 | `... --figure figS11 ...` | ~/figures/interpretation/figS11.png |

## Auxiliary calibration figures (not in supplement)

| Figure id | Command | Output |
| --------- | ------- | ------ |
| cal1 (PD payoff plane) | `... --figure cal1 ...` | ~/figures/interpretation/cal1.png |
| cal2 (snowdrift payoff plane) | `... --figure cal2 ...` | ~/figures/interpretation/cal2.png |

## Supplement table (Table S1)

Payoff-axis attribution from auxiliary calibration sweeps. Canonical copy for the
manuscript supplement: [supplement.md](supplement.md). Reproduce numbers from
journal synthesis and calibration docs; do not publish full payoff-plane heatmaps.

| Mechanism family | Limiting payoff gap | Journal source |
| ---------------- | ------------------- | -------------- |
| M (direct reciprocity) | Risk / defection payoff P | PD and snowdrift calibration |
| P (partner choice) | Cooperation advantage R − P | PD calibration |
| MP, MPQ, IMP, IJMPQ (combined / reputation-rich) | Reward / temptation R | PD calibration |

## Draft captions

Aligned with the Results write-through (2026-07). Authoritative source:
`graphgen/studies/interpretation/manifest.py` (`manuscript_report` context);
regenerate `paper/captions.md` with `--report`.

1. Fig 1. At c₀ = c₁, partner choice yields a stochastic cooperator/exploiter split absent without enforcement (PD); snowdrift already splits in the control columns. Paradox of success in the fitness panels.
2. Fig 2. Along c₁ = c₀ + 0.02, partner choice pins a deterministic split; IJMPQ lifts the expensive population. PD only — Fig. S3 shows partner choice creates the split; snowdrift floor is Fig. 1e–h. Full grid → Fig. S4; gs = 4 → Fig. S6.
3. Fig 3. At c = 0, machinery alleles fall while cooperation holds on unconditional cooperators. Fig. S7 full grid; Fig. S8 dilemma-0 control. Escape route priced by Figs. 4–5.
4. Fig 4. Own- vs partner-cost strips plus iso-budget: under P both populations flat in own cost, collapse under partner's; under IJMPQ the axes swap (taxing cheap side: partner 0.957 → 0.268, payer → 0.734). Third column: IJMPQ interior minimum (shared budget worse); P monotone.
5. Fig 5. Wedge closes as i₀ rises (holds at 0, threshold at 0.02, gone by 0.04). ±1 SD bands mark bistability. Equal-c hitchhiking contrast → Fig. S11.

Supplement captions:

S1. No-enforcement → M → P → IJMPQ raise the ceiling in that order; snowdrift softens the hierarchy (e–h).
S2. Shuffle short-memory variants of Fig. S1: M ordering can shift; P vs combined contrast remains.
S3. No-enforcement control for Fig. 2: cheap PD population barely cooperates, so partner choice creates the deterministic split.
S4. Full c₀ × c₁ grid behind Fig. 2 (P and IJMPQ).
S5. Deterministic strip (Fig. 2) vs stochastic strip (Fig. 1) on shared axes.
S6. Fig. 2 asymmetry at gs = 4: deterministic split survives.
S7. Cost × c grid behind Fig. 3: information cost soft alone, lowers the ceiling where costs overlap.
S8. Machinery erodes with or without a dilemma; cooperation persists through the shed only with a dilemma (cf. Fig. 3).
S9. With c₀ > 0 fixed, information cost compresses the partner-choice split (refuge gone). Complements Figs. 4–5.
S10. Fitness counterpart of Fig. 4 on the same own-cost, partner-cost, and iso-budget slices: relational axis swap and iso-budget interior penalties persist in fitness.
S11. At c₀ = c₁, i-asymmetry assigns roles under P and inverts under IJMPQ; hitchhiking stronger than in Figs. 4–5.

