# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal topic backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

`--groupsize` overrides every source, including figS9–figS26 (which embed
`groupsize=4` as counterparts of Figs. 1–2, 4 and S21). Regenerate those without
the flag, or with `--groupsize 4`:

    python -m graphgen.main --study interpretation --figure figS9 --output ~/figures
    python -m graphgen.main --study interpretation --figure figS25 --output ~/figures

Warm group-size-4 line-slice caches before regenerating S9–S10:

    python -m graphgen.main --study asymmetric_c0_c1_lines --export-slices --groupsize 4

Generate all manuscript PNGs and publication reports (figures must exist in the
output directory first). Prefer omitting `--groupsize` for `--all` so source-
level sizes (S9–S10, S25–S26) are kept; pass `--groupsize 128` only for single figures
that should force 128:

    python -m graphgen.main --study interpretation --all --output ~/figures
    python -m graphgen.main --study interpretation --report --output ~/figures

The report includes main text Figs 1–4 (fig1–fig4) and supplement Figs S1–S26
(figS1–S26) in manuscript order. Calibration panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx (internal; all figures)
- Markdown: paper/captions.md (supplement legends S1–S26 only; main-text legends live in results.md)

PD and snowdrift never share a figure. Fig. 3 is equal-c i asymmetry (snowdrift twin
S14). Fig. 4 and S21 are the crossed c-gap × i₀×i₁ PD/SD pair. Two-population
heatmaps use that same 3×4 template, with cooperation and fitness as separate
figures. Fitness twin of Fig. 3 is S13; of Fig. 4 is S20 (snowdrift S22). Fixed-total
line cuts of Fig. 4 (coop + fitness × —|P|M|IJMPQ) are S23–S24. Wedge line cuts are
prose-only (Fig. 4 / S21). Shuffle short-memory branches are prose-only (no dedicated
S panels).

Status: revised 2026-10 — Figs. 3–4 and most two-pop supplement heatmaps are 3×4
(—|P|M|IJMPQ × cheap/expensive/gap or low-i/high-i/gap; one colorbar per row).
Cooperation and fitness are separate figures. Fitness-gap colour scale is ±0.3.
Two-pop matched Cost×c is 3×4 coop+gap (S11–S12; no fitness). Supplement runs to S26.

## Setup audit (2026-10)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| fig1 | Line | asymmetric_c0_c1_lines, _/P/M/IJMPQ | PD; row0 sym, row1 gap |
| fig2 | Line | same as fig1 | Snowdrift twin of fig1 |
| fig3 | Heatmap | asymmetric_i0_i1, _+P+M+IJMPQ, qBSeen+ΔqBSeen | Equal-c PD; twin → figS14 |
| fig4 | Heatmap | asymmetric_c1_i0_i1, _+P+M+IJMPQ, qBSeen+ΔqBSeen | Crossed PD 3×4; twin → figS21 |
| figS21 | Heatmap | twin of fig4 | Snowdrift 3×4 plane |
| figS1 | Line | symmetric_c pop_1, _/P/M/IJMPQ | PD; 2×4 coop/fitness |
| figS2 | Line | same as figS1 | Snowdrift twin of S1 |
| figS3 | Line | same as fig1, wmean | Fitness of Fig. 1 |
| figS4 | Line | same as fig2, wmean | Fitness of Fig. 2 |
| figS5 | Heatmap | asymmetric_c0_c1, plane qBSeen | PD coop; twin → figS7 |
| figS6 | Heatmap | asymmetric_c0_c1, plane wmean | PD fitness; twin → figS8 |
| figS9 | Line | same as fig1, gs = 4 | Fig. 1 at gs = 4; twin → figS10 |
| figS10 | Line | same as fig2, gs = 4 | Fig. 2 at gs = 4 |
| figS11 | Heatmap | symmetric_c_i pop_2, _/P/M/IJMPQ | PD 3×4 Cost×c coop+gap; twin → figS12 |
| figS13 | Heatmap | asymmetric_i0_i1, plane wmean | Equal-c fitness; twin → figS15 |
| figS14 | Heatmap | twin of fig3 | Equal-c snowdrift coop |
| figS16 | Heatmap | asymmetric_c1_i, plane qBSeen | Shared-i coop; twin → figS18 |
| figS17 | Heatmap | asymmetric_c1_i, plane wmean | Shared-i fitness; twin → figS19 |
| figS20 | Heatmap | twin layout of fig4, wmean+Δwmean | Fitness plane; twin → figS22 |
| figS23 | Line | asymmetric_c1_i0_i1_lines, iso-budget, —/P/M/IJMPQ | Fixed-total coop+fitness; twin → figS24 |
| figS25 | Heatmap | same as fig4, gs = 4 | Fig. 4 at gs = 4; twin → figS26 |
| figS26 | Heatmap | same as figS21, gs = 4 | S21 at gs = 4 |

## Main text figures

| Fig | Message | Figure id | Output |
| --- | ------- | --------- | ------ |
| 1 | Matched vs gap cooperation cost (PD) | fig1 | ~/figures/interpretation/fig1.png |
| 2 | Matched vs gap cooperation cost (snowdrift) | fig2 | ~/figures/interpretation/fig2.png |
| 3 | Equal-c i asymmetry: — / P / M / IJMPQ × low-i / high-i / gap (PD) | fig3 | ~/figures/interpretation/fig3.png |
| 4 | Crossed i₀ × i₁ plane: — / P / M / IJMPQ × cheap / expensive / gap (PD) | fig4 | ~/figures/interpretation/fig4.png |

### Panel order notes

1. fig1 / fig2: 2×4; row 0 = matched costs, row 1 = c₁ = c₀ + 0.02; columns —, P, M, IJMPQ.
2. figS1 / figS2: 2×4; row 0 = coop, row 1 = fitness; same mechanism columns.
3. Two-pop planes S5–S8, S13–S22, S25–S26 (and Figs. 3–4 and S21): 3×4; columns — | P | M | IJMPQ; rows = cheap/expensive/gap (or low-i/high-i/gap for equal-c); one colorbar per row; cooperation and fitness are separate figures. S9–S10 are line-plot counterparts of Figs. 1–2 at group size 4; S25–S26 are gs=4 of Fig. 4 / S21.
4. S11–S12: 3×4 two-pop matched Cost×c (coop + gap); rows = higher-/lower-coop / gap; columns — | P | M | IJMPQ.
5. figS23 / S24: fixed-total line cuts (2×4; rows coop / fitness; columns —|P|M|IJMPQ; shared i₁ x title).

Warm line-slice caches before regenerating Figs. 1–2 / S3–S4 / S23–S24:

```bash
python -m graphgen.main --study asymmetric_c0_c1_lines --export-slices --groupsize 128
python -m graphgen.main --study asymmetric_c1_i0_i1_lines --export-slices --results ~/results
python -m graphgen.main --study symmetric_c_i_lines --export-slices --groupsize 128
```

## Supplement figures

| Supp | Message | id |
| ---- | ------- | -- |
| S1 | Cooperation in a single population (PD; coop + fitness) | figS1 |
| S2 | Cooperation in a single population (snowdrift) | figS2 |
| S3 | Fitness twin of Fig. 1 | figS3 |
| S4 | Fitness twin of Fig. 2 | figS4 |
| S5 | Full c₀ × c₁ grid PD (coop) | figS5 |
| S6 | Full c₀ × c₁ grid PD (fitness) | figS6 |
| S7 | Full c₀ × c₁ grid snowdrift (coop) | figS7 |
| S8 | Full c₀ × c₁ grid snowdrift (fitness) | figS8 |
| S9 | Group-size-4 counterpart of Fig. 1 | figS9 |
| S10 | Group-size-4 counterpart of Fig. 2 | figS10 |
| S11 | Matched Cost × c (two pops; PD coop + gap) | figS11 |
| S12 | Matched Cost × c (two pops; snowdrift) | figS12 |
| S13 | Fitness twin of Fig. 3 (equal-c PD) | figS13 |
| S14 | Snowdrift twin of Fig. 3 (equal-c) | figS14 |
| S15 | Fitness twin of Fig. S14 (equal-c snowdrift) | figS15 |
| S16 | Shared-i under c-gap PD (coop) | figS16 |
| S17 | Shared-i under c-gap PD (fitness) | figS17 |
| S18 | Shared-i under c-gap snowdrift (coop) | figS18 |
| S19 | Shared-i under c-gap snowdrift (fitness) | figS19 |
| S20 | Fitness twin of Fig. 4 | figS20 |
| S21 | Snowdrift twin of Fig. 4 (i₀ × i₁ plane) | figS21 |
| S22 | Fitness twin of Fig. S21 | figS22 |
| S23 | Fixed-total cut (PD; coop + fitness) | figS23 |
| S24 | Fixed-total cut (snowdrift) | figS24 |
| S25 | Group-size-4 counterpart of Fig. 4 | figS25 |
| S26 | Group-size-4 counterpart of Fig. S21 | figS26 |

## Auxiliary figures (not in supplement)

| id | Output |
| -- | ------ |
| cal1 | ~/figures/interpretation/cal1.png |
| cal2 | ~/figures/interpretation/cal2.png |
| aux_m_nodilemma | ~/figures/interpretation/aux_m_nodilemma.png |

## Supplement table (Table S1)

See [supplement.md](supplement.md).

## Draft captions

Main-text legends (Figs. 1–4): hand-maintained in `results.md` (source of truth).
Supplement legends (S1–S26): regenerate `paper/captions.md` from the interpretation
manifest with `--report`. The DOCX at `~/figures/interpretation/interpretation.docx`
is internal and may differ. Am Nat legends should generally stay near ≤100 words:
descriptive panel text and short cross-figure pointers only; interpretation belongs
in Results.
