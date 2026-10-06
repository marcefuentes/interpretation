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

The report includes main text Figs 1–4 (fig1–fig4) and supplement Figs S1–S23
(figS1–S23) in manuscript order, with cross-references in each legend. Calibration
panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx
- Markdown mirror: paper/captions.md (sibling interpretation repo; PNG embeds
  point at the figure output directory used for that run)

The manuscript figure set lives in ../graph/graphgen/studies/interpretation/ as
fig1–fig4 (main text) and figS1–S23 (supplement). Graphgen ids match how figures
are called in the manuscript (Fig. 1 → fig1, Fig. S3 → figS3). PD and snowdrift
never share a figure. Fig. S21 is the full i₀ × i₁ PD heatmap behind the relational
line cuts (Figs. 3–4, S17); there is no snowdrift twin of S21.
Auxiliary panels cal1–cal2 (payoff-plane calibration) and aux_m_nodilemma (M under
dilemma 0 vs PD; internal only) are in the same namespace and are not published.

Do not pass --dilemma-type when generating the interpretation study unless you
intentionally want a single-dilemma figure; aux_m_nodilemma mixes dilemma types
for internal use only.

**Payoff-plane calibration sweeps** are auxiliary — they support the payoff-gap
attributions cited in the text but do not appear as manuscript figures. Regenerate
with `--figure cal1` or `--figure cal2` when needed; see the supplement table and
the journal calibration analyses.

Status: revised 2026-10 — main text is four line figures (PD coop, snowdrift coop,
relational i, wedge). Old decoupling figure demoted to Fig. S11. Fitness of
Figs. 1–2 is Figs. S5–S6. Former sym-vs-asym contrast (old S5) absorbed into
Figs. 1–2.

## Setup audit (2026-10)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| fig1 | Line (PLOT) | asymmetric_c0_c1_lines pop_2, _/P/M/IJMPQ | PD; row0 sym, row1 gap |
| fig2 | Line (PLOT) | same cuts as fig1 | Snowdrift twin of fig1 |
| fig3 | Line (PLOT) | asymmetric_c1_i0_i1_lines pop_2, P + IJMPQ | PD; full grid → figS21; twin → figS22 |
| fig4 | Line (PLOT) | asymmetric_c1_i0_i1_lines pop_2, IJMPQ | PD; full grid → figS21; twin → figS23 |
| figS1 | Line (PLOT) | symmetric_c pop_1, _/P/M/IJMPQ | PD one-pop ceilings |
| figS2 | Line (PLOT) | symmetric_c pop_1, _/P/M/IJMPQ | Snowdrift one-pop ceilings |
| figS3 | Line | symmetric_c pop_1, shuffle M/MP/IM/IMP | PD |
| figS4 | Line | symmetric_c pop_1, shuffle | Snowdrift twin of S3 |
| figS5 | Line (PLOT) | same as fig1, trait wmean | Fitness of Fig. 1 |
| figS6 | Line (PLOT) | same as fig2, trait wmean | Fitness of Fig. 2 |
| figS7 | Heatmap | asymmetric_c0_c1 pop_2, P + IJMPQ | PD; twin → figS8 |
| figS9 | Heatmap | asymmetric_c0_c1 pop_2, P, gs = 4 | PD; twin → figS10 |
| figS11 | Line (PLOT) | symmetric_c_i_lines pop_1, P + M at c = 0 | PD; twin → figS12 |
| figS13 | Heatmap | symmetric_c_i pop_1, IJMPQ | PD Cost×c; twin → figS14 |
| figS15 | Heatmap | asymmetric_c1_i pop_2, P | PD; twin → figS16 |
| figS17 | Line (PLOT) | asymmetric_c1_i0_i1_lines, P + IJMPQ | Fitness of Fig. 3; twin → figS18 |
| figS19 | Heatmap | asymmetric_i0_i1 pop_2, P + IJMPQ | PD; twin → figS20 |
| figS21 | Heatmap | asymmetric_c1_i0_i1 pop_2, P + IJMPQ | PD; full square (no SD twin) |
| figS22–S23 | (twins) | same cuts as Figs. 3–4 | Snowdrift |
| aux_m_nodilemma | Heatmap | symmetric_c_i pop_1, M, dt 0 vs 1 | Internal only |
| cal1, cal2 | Heatmap | prisoners / snowdrift calibration | Auxiliary — not in supplement |

### Main-text set, locked 2026-10

Four main line figures. Cost-threshold comparison remains Fig. S1 (one-pop PD).
Decoupling demoted to Fig. S11.

| Fig | Content | Renderer |
| --- | ------- | -------- |
| 1 | PD coop: matched costs over c₁ = c₀ + 0.02; columns —, P, M, IJMPQ | line |
| 2 | Snowdrift twin of Fig. 1 | line |
| 3 | Information cost is relational (strips + fixed total) | line |
| 4 | Wedge boundary and its closing | line |

## Main text figures

| Fig | Message | Figure id | Command | Output | Journal backing |
| --- | ------- | --------- | ------- | ------ | --------------- |
| 1 | Matched vs gap cooperation cost (PD; four mechanisms) | fig1 | `... --figure fig1 ...` | ~/figures/interpretation/fig1.png | Two populations, equal and unequal c |
| 2 | Matched vs gap cooperation cost (snowdrift) | fig2 | `... --figure fig2 ...` | ~/figures/interpretation/fig2.png | Snowdrift twin of Fig. 1 |
| 3 | Information cost is relational: binding axis and budget non-convexity | fig3 | `... --figure fig3 ...` | ~/figures/interpretation/fig3_qBSeen.png | Crossed cost asymmetries |
| 4 | Role inversion appears only when the cheap population's information cost is near zero | fig4 | `... --figure fig4 ...` | ~/figures/interpretation/fig4_qBSeen.png | Crossed cost asymmetries |

### Panel order notes

1. fig1 / fig2: 2×4; row 0 = matched costs (greens), row 1 = c₁ = c₀ + 0.02
   (orange/red); columns = —, P, M, IJMPQ; trait qBSeen only.
2. fig3: rows = P then IJMPQ; columns = i0 strip, i1 strip, fixed total.
3. fig4: IJMPQ; columns = i0 held at 0, 0.02, 0.04, 0.1 while i1 is swept; row 1 =
   cooperation, row 2 = fitness; both rows show ±1 SD bands.

### Exact commands for the main-text set

1. Fig 1 — fig1 — `python -m graphgen.main --study interpretation --figure fig1 --groupsize 128 --output ~/figures`
2. Fig 2 — fig2 — `... --figure fig2 ...`
3. Fig 3 — fig3 — `... --figure fig3 ...`
4. Fig 4 — fig4 — `... --figure fig4 ...`

Figs 1–4 need the line-slice caches warmed first; see the sections below.

## Cooperation-cost strips (matched and c1 = c0 + 0.02)

Figs. 1–2 (and fitness twins S5–S6) use `asymmetric_c0_c1_lines` with filters
`symmetric_diagonal` (results_name=symmetric_c) and `asymmetric_offset`
(c1 = c0 + 0.02). Warm with:

```bash
python -m graphgen.main --study asymmetric_c0_c1_lines --export-slices --groupsize 128
```

## Cooperation after allele loss: line reslice at c = 0

Fig. S11 is a dose-response line chart at zero cooperation cost rather than the full
Cost × c heatmap (figS13). Study `symmetric_c_i_lines` with filter `c_zero`. Warm:

```bash
python -m graphgen.main --study symmetric_c_i_lines --export-slices --groupsize 128
```

## Relational information cost: line reslices

Study `asymmetric_c1_i0_i1_lines`. Warm:

    python -m graphgen.main --study asymmetric_c1_i0_i1_lines --export-slices --results ~/results

| Fig | Message | Slices used |
| --- | ------- | ----------- |
| 3 | Binding axis (own vs partner cost) and budget non-convexity | `tax_on_pop_0`, `tax_on_pop_1`, `iso_budget` |
| 4 | Role inversion appears only when the cheap population's information cost is near zero | `wedge_c0_000/002/004/010` |

Bands are opt-in per figure via a `show_band` source parameter, set only on Fig. 4.

### Full square behind the relational line cuts

A full i0 × i1 square (c0 = 0.10, c1 = 0.20 fixed) is published as Fig. S21 (imshow).
The line reslices (Figs. 3–4, S17) carry the dose-response claims; S21 is the full grid.

## Supplement figures

| Supp fig | Message | Figure id | Command | Output |
| -------- | ------- | --------- | ------- | ------ |
| S1 | One-pop equal-c ceilings (PD) | figS1 | `... --figure figS1 ...` | ~/figures/interpretation/figS1.png |
| S2 | One-pop equal-c ceilings (snowdrift) | figS2 | `... --figure figS2 ...` | ~/figures/interpretation/figS2.png |
| S3 | Shuffle reciprocity branches (PD) | figS3 | `... --figure figS3 ...` | ~/figures/interpretation/figS3.png |
| S4 | Shuffle reciprocity branches (snowdrift) | figS4 | `... --figure figS4 ...` | ~/figures/interpretation/figS4.png |
| S5 | Fitness twin of Fig. 1 (PD) | figS5 | `... --figure figS5 ...` | ~/figures/interpretation/figS5.png |
| S6 | Fitness twin of Fig. 2 (snowdrift) | figS6 | `... --figure figS6 ...` | ~/figures/interpretation/figS6.png |
| S7 | Full c₀ × c₁ grid (PD) | figS7 | `... --figure figS7 ...` | ~/figures/interpretation/figS7.png |
| S8 | Full c₀ × c₁ grid (snowdrift) | figS8 | `... --figure figS8 ...` | ~/figures/interpretation/figS8.png |
| S9 | gs = 4 asymmetry (PD) | figS9 | `... --figure figS9 ...` | ~/figures/interpretation/figS9.png |
| S10 | gs = 4 asymmetry (snowdrift) | figS10 | `... --figure figS10 ...` | ~/figures/interpretation/figS10.png |
| S11 | c = 0 decoupling (PD) | figS11 | `... --figure figS11 ...` | ~/figures/interpretation/figS11.png |
| S12 | c = 0 decoupling (snowdrift) | figS12 | `... --figure figS12 ...` | ~/figures/interpretation/figS12.png |
| S13 | Cost × c heatmap (PD) | figS13 | `... --figure figS13 ...` | ~/figures/interpretation/figS13.png |
| S14 | Cost × c heatmap (snowdrift) | figS14 | `... --figure figS14 ...` | ~/figures/interpretation/figS14.png |
| S15 | Shared-i under c-gap (PD) | figS15 | `... --figure figS15 ...` | ~/figures/interpretation/figS15.png |
| S16 | Shared-i under c-gap (snowdrift) | figS16 | `... --figure figS16 ...` | ~/figures/interpretation/figS16.png |
| S17 | Fitness of Fig. 3 (PD) | figS17 | `... --figure figS17 ...` | ~/figures/interpretation/figS17_wmean.png |
| S18 | Fitness of Fig. S22 (snowdrift) | figS18 | `... --figure figS18 ...` | ~/figures/interpretation/figS18_wmean.png |
| S19 | Equal-c i asymmetry (PD) | figS19 | `... --figure figS19 ...` | ~/figures/interpretation/figS19.png |
| S20 | Equal-c i asymmetry (snowdrift) | figS20 | `... --figure figS20 ...` | ~/figures/interpretation/figS20.png |
| S21 | Full i₀ × i₁ grid (PD) | figS21 | `... --figure figS21 ...` | ~/figures/interpretation/figS21.png |
| S22 | Snowdrift twin of Fig. 3 | figS22 | `... --figure figS22 ...` | ~/figures/interpretation/figS22_qBSeen.png |
| S23 | Snowdrift twin of Fig. 4 | figS23 | `... --figure figS23 ...` | ~/figures/interpretation/figS23_qBSeen.png |

## Auxiliary figures (not in supplement)

| Figure id | Command | Output |
| --------- | ------- | ------ |
| cal1 (PD payoff plane) | `... --figure cal1 ...` | ~/figures/interpretation/cal1.png |
| cal2 (snowdrift payoff plane) | `... --figure cal2 ...` | ~/figures/interpretation/cal2.png |
| aux_m_nodilemma (M, dilemma 0 vs PD; internal) | `... --figure aux_m_nodilemma ...` | ~/figures/interpretation/aux_m_nodilemma.png |

## Supplement table (Table S1)

Payoff-axis attribution from auxiliary calibration sweeps. Canonical copy for the
manuscript supplement: [supplement.md](supplement.md).

## Draft captions

Authoritative source: `graphgen/studies/interpretation/manifest.py`
(`manuscript_report` context); regenerate `paper/captions.md` with `--report`.
