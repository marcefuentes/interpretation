# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal topic backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

`--groupsize` overrides every source, including figS9–figS12 (which embed
`groupsize=4`). Regenerate those without the flag, or with `--groupsize 4`:

    python -m graphgen.main --study interpretation --figure figS9 --output ~/figures
    python -m graphgen.main --study interpretation --figure figS11 --output ~/figures

Generate all manuscript PNGs and publication reports (figures must exist in the
output directory first). Prefer omitting `--groupsize` for `--all` so source-
level sizes (S9–S12) are kept; pass `--groupsize 128` only for single figures
that should force 128:

    python -m graphgen.main --study interpretation --all --output ~/figures
    python -m graphgen.main --study interpretation --report --output ~/figures

The report includes main text Figs 1–3 (fig1–fig3) and supplement Figs S1–S29
(figS1–S29) in manuscript order. Calibration panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx (internal; all figures)
- Markdown: paper/captions.md (supplement legends S1–S29 only; main-text legends live in results.md)

PD and snowdrift never share a figure. Figs. 3 and S20 are a PD/SD pair (like Figs. 1–2)
on the full i₀ × i₁ square. Two-population heatmaps use that same 3×4 template,
with cooperation and fitness as separate figures. Fitness twins of Figs. 3 and S20 are
S19 and S21. Line cuts (coop + fitness) are S22–S23 (who-pays) and S24–S25 (wedge).
Shuffle short-memory branches are prose-only (no dedicated S panels).

Status: revised 2026-10 — Figs. 3 and S20 and most two-pop supplement heatmaps are 3×4
(—|P|M|IJMPQ × cheap/expensive/gap; one colorbar per row). Cooperation and fitness
are separate figures. Fitness-gap colour scale is ±0.3. Equal-c planes use
low-i/high-i row labels. One-pop Cost×c is 2×4 (S13–S14). Supplement runs to S29.

## Setup audit (2026-10)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| fig1 | Line | asymmetric_c0_c1_lines, _/P/M/IJMPQ | PD; row0 sym, row1 gap |
| fig2 | Line | same as fig1 | Snowdrift twin of fig1 |
| fig3 | Heatmap | asymmetric_c1_i0_i1, _+P+M+IJMPQ, qBSeen+ΔqBSeen | PD 3×4 plane; twin → figS20 |
| figS20 | Heatmap | twin of fig3 | Snowdrift 3×4 plane |
| figS1 | Line | symmetric_c pop_1, _/P/M/IJMPQ | PD; 2×4 coop/fitness |
| figS2 | Line | same as figS1 | Snowdrift twin of S1 |
| figS3 | Line | same as fig1, wmean | Fitness of Fig. 1 |
| figS4 | Line | same as fig2, wmean | Fitness of Fig. 2 |
| figS5 | Heatmap | asymmetric_c0_c1, plane qBSeen | PD coop; twin → figS7 |
| figS6 | Heatmap | asymmetric_c0_c1, plane wmean | PD fitness; twin → figS8 |
| figS9 | Heatmap | asymmetric_c0_c1, gs = 4, plane qBSeen | PD coop; twin → figS11 |
| figS10 | Heatmap | asymmetric_c0_c1, gs = 4, plane wmean | PD fitness; twin → figS12 |
| figS13 | Heatmap | symmetric_c_i, _/P/M/IJMPQ | PD 2×4 Cost×c; twin → figS14 |
| figS15 | Heatmap | asymmetric_c1_i, plane qBSeen | PD coop; twin → figS17 |
| figS16 | Heatmap | asymmetric_c1_i, plane wmean | PD fitness; twin → figS18 |
| figS19 | Heatmap | twin layout of fig3, wmean+Δwmean | Fitness plane; twin → figS21 |
| figS22 | Line | asymmetric_c1_i0_i1_lines, P + IJMPQ | Who-pays coop+fitness; twin → figS23 |
| figS24 | Line | wedge, qBSeen+wmean, P + IJMPQ | Wedge coop+fitness; twin → figS25 |
| figS26 | Heatmap | asymmetric_i0_i1, plane qBSeen | Equal-c coop; twin → figS28 |
| figS27 | Heatmap | asymmetric_i0_i1, plane wmean | Equal-c fitness; twin → figS29 |

## Main text figures

| Fig | Message | Figure id | Output |
| --- | ------- | --------- | ------ |
| 1 | Matched vs gap cooperation cost (PD) | fig1 | ~/figures/interpretation/fig1.png |
| 2 | Matched vs gap cooperation cost (snowdrift) | fig2 | ~/figures/interpretation/fig2.png |
| 3 | i₀ × i₁ plane: — / P / M / IJMPQ × cheap / expensive / gap (PD) | fig3 | ~/figures/interpretation/fig3.png |

### Panel order notes

1. fig1 / fig2: 2×4; row 0 = matched costs, row 1 = c₁ = c₀ + 0.02; columns —, P, M, IJMPQ.
2. figS1 / figS2: 2×4; row 0 = coop, row 1 = fitness; same mechanism columns.
3. Two-pop planes S5–S12, S15–S21, S26–S29 (and Figs. 3 and S20): 3×4; columns — | P | M | IJMPQ; rows = cheap/expensive/gap (or low-i/high-i/gap for equal-c); one colorbar per row; cooperation and fitness are separate figures.
4. S13–S14: 2×4 one-pop Cost×c; rows = coop / fitness; columns — | P | M | IJMPQ.
5. figS22 / S23: who-pays line cuts (4×3; rows P-coop, P-fitness, IJMPQ-coop, IJMPQ-fitness; columns tax-cheap, fixed total, tax-expensive). figS24 / S25: wedge line cuts (4×4; same row grammar; columns hold i₀ while sweeping i₁).

Warm line-slice caches before regenerating Figs. 1–2 / S3–S4 / S22–S25:

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
| S9 | gs = 4 asymmetry PD (coop) | figS9 |
| S10 | gs = 4 asymmetry PD (fitness) | figS10 |
| S11 | gs = 4 asymmetry snowdrift (coop) | figS11 |
| S12 | gs = 4 asymmetry snowdrift (fitness) | figS12 |
| S13 | Cost × c heatmap PD | figS13 |
| S14 | Cost × c heatmap snowdrift | figS14 |
| S15 | Shared-i under c-gap PD (coop) | figS15 |
| S16 | Shared-i under c-gap PD (fitness) | figS16 |
| S17 | Shared-i under c-gap snowdrift (coop) | figS17 |
| S18 | Shared-i under c-gap snowdrift (fitness) | figS18 |
| S19 | Fitness twin of Fig. 3 | figS19 |
| S20 | Snowdrift twin of Fig. 3 (i₀ × i₁ plane) | figS20 |
| S21 | Fitness twin of Fig. S20 | figS21 |
| S22 | Who-pays line cuts (PD; coop + fitness) | figS22 |
| S23 | Who-pays line cuts (snowdrift) | figS23 |
| S24 | Wedge line cuts (PD; coop + fitness) | figS24 |
| S25 | Wedge line cuts (snowdrift) | figS25 |
| S26 | Equal-c i asymmetry PD (coop) | figS26 |
| S27 | Equal-c i asymmetry PD (fitness) | figS27 |
| S28 | Equal-c i asymmetry snowdrift (coop) | figS28 |
| S29 | Equal-c i asymmetry snowdrift (fitness) | figS29 |

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
Supplement legends (S1–S29): regenerate `paper/captions.md` from the interpretation
manifest with `--report`. The DOCX at `~/figures/interpretation/interpretation.docx`
is internal and may differ. Am Nat legends should generally stay near ≤100 words:
descriptive panel text and short cross-figure pointers only; interpretation belongs
in Results.
