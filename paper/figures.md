# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal topic backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

`--groupsize` overrides every source, including figS7–figS27 (which embed
`groupsize=4` as counterparts of Figs. S3–S4, 3 and S22). Regenerate those without
the flag, or with `--groupsize 4`:

    python -m graphgen.main --study interpretation --figure figS7 --output ~/figures
    python -m graphgen.main --study interpretation --figure figS26 --output ~/figures

Warm group-size-4 line-slice caches before regenerating S7–S8:

    python -m graphgen.main --study asymmetric_c0_c1_lines --export-slices --groupsize 4

Generate all manuscript PNGs and publication reports (figures must exist in the
output directory first). Prefer omitting `--groupsize` for `--all` so source-
level sizes (S7–S8, S26–S27) are kept; pass `--groupsize 128` only for single figures
that should force 128:

    python -m graphgen.main --study interpretation --all --output ~/figures
    python -m graphgen.main --study interpretation --report --output ~/figures

The report includes main text Figs 1–3 (fig1–fig3) and supplement Figs S1–S30
(figS1–S30) in manuscript order. Calibration panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx (internal; all figures)
- Markdown: paper/captions.md (supplement legends S1–S30 only; main-text legends live in results.md)

PD and snowdrift never share a figure. Fig. 1 is the full c₀×c₁ PD coop grid
(snowdrift twin S10; fitness S9). Matched/gap strips are S3–S4 (fitness S5–S6).
Fig. 2 is equal-c i asymmetry (snowdrift twin S15; fitness S14). Fig. 3 and S22 are
the crossed c-gap × i₀×i₁ PD/SD pair (fitness S21/S23). Fixed-total line cuts of
Fig. 3 are S24–S25. Two-population heatmaps use the same row template (4 columns in main text,
5 in the supplement), with cooperation and fitness as separate figures. Wedge line cuts are prose-only
(Fig. 3 / S22). Shuffle short-memory branches are prose-only (no dedicated S panels).

Status: revised 2026-10 — Fig. 1 promoted from former S5; former main Figs. 1–2 are
S3–S4; main text is Figs. 1–3; supplement runs to S30. Main Figs. 1–3 are 3×4 (—|P|M|IMP); supplement
heatmaps are 3×5 (—|P|M|IMP|IJMPQ × cheap/expensive/gap or low-i/high-i/gap;
one colorbar per row). S28–S30 are five-column twins of Figs. 1–3. Cooperation and fitness are separate figures. Fitness-gap colour scale is
±0.3. Two-pop matched Cost×c is 3×5 coop+gap (S12–S13; no fitness).

## Setup audit (2026-10)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| figS3 | Line | asymmetric_c0_c1_lines, _/P/M/IMP/IJMPQ | PD; row0 sym, row1 gap |
| figS4 | Line | same as figS3 | Snowdrift twin of figS3 |
| fig2 | Heatmap | asymmetric_i0_i1, _+P+M+IMP, qBSeen+ΔqBSeen | Equal-c PD 3×4; twin → figS15; 5-col → figS29 |
| fig3 | Heatmap | asymmetric_c1_i0_i1, _+P+M+IMP, qBSeen+ΔqBSeen | Crossed PD 3×4; twin → figS22; 5-col → figS30 |
| figS22 | Heatmap | twin of fig3 layout, 5-col | Snowdrift 3×5 plane |
| figS1 | Line | symmetric_c pop_1, _/P/M/IMP/IJMPQ | PD; 2×5 coop/fitness |
| figS2 | Line | same as figS1 | Snowdrift twin of S1 |
| figS5 | Line | same as figS3, wmean | Fitness of Fig. S3 |
| figS6 | Line | same as figS4, wmean | Fitness of Fig. S4 |
| fig1 | Heatmap | asymmetric_c0_c1, plane qBSeen (_/P/M/IMP) | PD coop 3×4; twin → figS10; 5-col → figS28 |
| figS9 | Heatmap | asymmetric_c0_c1, plane wmean | PD fitness; twin → figS11 |
| figS7 | Line | same as figS3, gs = 4 | Fig. S3 at gs = 4; twin → figS8 |
| figS8 | Line | same as figS4, gs = 4 | Fig. S4 at gs = 4 |
| figS12 | Heatmap | symmetric_c_i pop_2, _/P/M/IMP/IJMPQ | PD 3×5 Cost×c coop+gap; twin → figS13 |
| figS14 | Heatmap | asymmetric_i0_i1, plane wmean | Equal-c fitness; twin → figS16 |
| figS15 | Heatmap | twin of fig2 | Equal-c snowdrift coop |
| figS17 | Heatmap | asymmetric_c1_i, plane qBSeen | Shared-i coop; twin → figS19 |
| figS18 | Heatmap | asymmetric_c1_i, plane wmean | Shared-i fitness; twin → figS20 |
| figS21 | Heatmap | twin layout of fig3, wmean+Δwmean | Fitness plane; twin → figS23 |
| figS24 | Line | asymmetric_c1_i0_i1_lines, iso-budget, —/P/M/IMP/IJMPQ | Fixed-total coop+fitness; twin → figS25 |
| figS26 | Heatmap | same as fig3, gs = 4 | Fig. 3 at gs = 4; twin → figS27 |
| figS27 | Heatmap | same as figS22, gs = 4 | S22 at gs = 4 |

## Main text figures

| Fig | Message | Figure id | Output |
| --- | ------- | --------- | ------ |
| 1 | Full c₀ × c₁ grid PD (coop + gap) | fig1 | ~/figures/interpretation/fig1.png |
| 2 | Equal-c i asymmetry: — / P / M / IMP × low-i / high-i / gap (PD) | fig2 | ~/figures/interpretation/fig2.png |
| 3 | Crossed i₀ × i₁ plane: — / P / M / IMP × cheap / expensive / gap (PD) | fig3 | ~/figures/interpretation/fig3.png |

### Panel order notes

1. Main Figs. 1–3: 3×4; columns — | P | M | IMP. Supplement two-pop planes (S9–S11, S14–S23, S26–S30, S22): 3×5; columns — | P | M | IMP | IJMPQ; rows = cheap/expensive/gap (or low-i/high-i/gap for equal-c); one colorbar per row; cooperation and fitness are separate figures. S28–S30 are five-column twins of Figs. 1–3.
2. figS3 / figS4: 2×5 strip line plots; row 0 = matched costs, row 1 = c₁ = c₀ + 0.02; columns —, P, M, IMP, IJMPQ. S7–S8 are their gs=4 counterparts.
3. figS1 / figS2: 2×5; row 0 = coop, row 1 = fitness; same mechanism columns.
4. S12–S13: 3×5 two-pop matched Cost×c (coop + gap); rows = higher-/lower-coop / gap; columns — | P | M | IMP | IJMPQ.
5. figS24 / S25: fixed-total line cuts (2×5; rows coop / fitness; columns —|P|M|IMP|IJMPQ; shared i₁ x title).

Warm line-slice caches before regenerating Figs. S3–S4 / S5–S6 / S24–S25:

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
| S3 | Matched vs gap cooperation-cost strips (PD) | figS3 |
| S4 | Matched vs gap cooperation-cost strips (snowdrift) | figS4 |
| S5 | Fitness twin of Fig. S3 | figS5 |
| S6 | Fitness twin of Fig. S4 | figS6 |
| S7 | Group-size-4 counterpart of Fig. S3 | figS7 |
| S8 | Group-size-4 counterpart of Fig. S4 | figS8 |
| S9 | Full c₀ × c₁ grid PD (fitness) | figS9 |
| S10 | Full c₀ × c₁ grid snowdrift (coop) | figS10 |
| S11 | Full c₀ × c₁ grid snowdrift (fitness) | figS11 |
| S12 | Matched Cost × c (two pops; PD coop + gap) | figS12 |
| S13 | Matched Cost × c (two pops; snowdrift) | figS13 |
| S14 | Fitness twin of Fig. 2 (equal-c PD) | figS14 |
| S15 | Snowdrift twin of Fig. 2 (equal-c) | figS15 |
| S16 | Fitness twin of Fig. S15 (equal-c snowdrift) | figS16 |
| S17 | Shared-i under c-gap PD (coop) | figS17 |
| S18 | Shared-i under c-gap PD (fitness) | figS18 |
| S19 | Shared-i under c-gap snowdrift (coop) | figS19 |
| S20 | Shared-i under c-gap snowdrift (fitness) | figS20 |
| S21 | Fitness twin of Fig. 3 | figS21 |
| S22 | Snowdrift twin of Fig. 3 (i₀ × i₁ plane) | figS22 |
| S23 | Fitness twin of Fig. S22 | figS23 |
| S24 | Fixed-total cut (PD; coop + fitness) | figS24 |
| S25 | Fixed-total cut (snowdrift) | figS25 |
| S26 | Group-size-4 counterpart of Fig. 3 | figS26 |
| S27 | Group-size-4 counterpart of Fig. S22 | figS27 |
| S28 | Five-column version of Fig. 1 (adds IJMPQ) | figS28 |
| S29 | Five-column version of Fig. 2 (adds IJMPQ) | figS29 |
| S30 | Five-column version of Fig. 3 (adds IJMPQ) | figS30 |

## Auxiliary figures (not in supplement)

| id | Output |
| -- | ------ |
| cal1 | ~/figures/interpretation/cal1.png |
| cal2 | ~/figures/interpretation/cal2.png |
| aux_m_nodilemma | ~/figures/interpretation/aux_m_nodilemma.png |

## Supplement table (Table S1)

See [supplement.md](supplement.md).

## Draft captions

Main-text legends (Figs. 1–3): hand-maintained in `results.md` (source of truth).
Supplement legends (S1–S30, including demoted strips S3–S4): regenerate
`paper/captions.md` from the interpretation manifest with `--report`. The DOCX at
`~/figures/interpretation/interpretation.docx` is internal and may differ. Am Nat
legends should generally stay near ≤100 words: descriptive panel text and short
cross-figure pointers only; interpretation belongs in Results.
