# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal topic backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

`--groupsize` overrides every source, including figS7–figS30 (which embed
`groupsize=4` as counterparts of Figs. S3, S5, 3 and S25). Regenerate those without
the flag, or with `--groupsize 4`:

    python -m graphgen.main --study interpretation --figure figS7 --output ~/figures
    python -m graphgen.main --study interpretation --figure figS29 --output ~/figures

Warm group-size-4 line-slice caches before regenerating S7–S8:

    python -m graphgen.main --study asymmetric_c0_c1_lines --export-slices --groupsize 4

Generate all manuscript PNGs and publication reports (figures must exist in the
output directory first). Prefer omitting `--groupsize` for `--all` so source-
level sizes (S7–S8, S29–S30) are kept; pass `--groupsize 128` only for single figures
that should force 128:

    python -m graphgen.main --study interpretation --all --output ~/figures
    python -m graphgen.main --study interpretation --report --output ~/figures

The report includes main text Figs 1–3 (fig1–fig3) and supplement Figs S1–S30
(figS1–S30) in manuscript order. Calibration panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx (internal; all figures)
- Markdown: paper/captions.md (supplement legends S1–S30 only; main-text legends live in results.md)

PD and snowdrift never share a figure. Fig. 1 is asymmetric cooperation cost with
low symmetric information cost (snowdrift twin S11; fitness S10). Symmetric/asymmetric-cost
strips are S3, S5 (fitness S4, S6). Fig. 2 is asymmetric information cost at
symmetric cooperation cost (snowdrift twin S17; fitness S16). Fig. 3 and S25 are asymmetric
information cost under asymmetric cooperation costs (fitness S24/S26). Fixed-total line
cuts of Fig. 3 are S27–S28. Two-population heatmaps use the same row template (4 columns in main text,
5 in the supplement), with cooperation and fitness as separate figures. Wedge line cuts are prose-only
(Fig. 3 / S25). Shuffle short-memory branches are prose-only (no dedicated S panels).

Status: revised 2026-10 — Fig. 1 promoted from former S4; former main Figs. 1–2 are
S3, S5; main text is Figs. 1–3; supplement runs to S23. Main Figs. 1–3 are 3×4 (—|P|M|IMP); supplement
heatmaps are 3×5 (—|P|M|IMP|IJMPQ × cheap/expensive/difference or low-i/high-i/difference;
one colorbar per row). S9, S15, S23 are five-column twins of Figs. 1–3. Cooperation and fitness are separate figures. Fitness-difference colour scale is
±0.3. Two-pop symmetric Cost×c is 3×5 coop+difference (S13–S14; no fitness).

## Setup audit (2026-10)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| figS3 | Line | asymmetric_c0_c1_lines, _/P/M/IMP/IJMPQ | PD; row0 sym, row1 asymmetric |
| figS5 | Line | same as figS3 | Snowdrift twin of figS3 |
| fig2 | Heatmap | asymmetric_i0_i1, _+P+M+IMP, qBSeen+ΔqBSeen | Symmetric-c PD 3×4; twin → figS17; 5-col → figS15 |
| fig3 | Heatmap | asymmetric_c1_i0_i1, _+P+M+IMP, qBSeen+ΔqBSeen | Crossed PD 3×4; twin → figS25; 5-col → figS23 |
| figS25 | Heatmap | twin of fig3 layout, 5-col | Snowdrift 3×5 plane |
| figS1 | Line | symmetric_c pop_1, _/P/M/IMP/IJMPQ | PD; 2×5 coop/fitness |
| figS2 | Line | same as figS1 | Snowdrift twin of S1 |
| figS4 | Line | same as figS3, wmean | Fitness of Fig. S3 |
| figS6 | Line | same as figS5, wmean | Fitness of Fig. S5 |
| fig1 | Heatmap | asymmetric_c0_c1, plane qBSeen (_/P/M/IMP) | PD coop 3×4; twin → figS11; 5-col → figS9 |
| figS10 | Heatmap | asymmetric_c0_c1, plane wmean | PD fitness; twin → figS12 |
| figS7 | Line | same as figS3, gs = 4 | Fig. S3 at gs = 4; twin → figS8 |
| figS8 | Line | same as figS5, gs = 4 | Fig. S5 at gs = 4 |
| figS13 | Heatmap | symmetric_c_i pop_2, _/P/M/IMP/IJMPQ | PD 3×5 Cost×c coop+difference; twin → figS14 |
| figS16 | Heatmap | asymmetric_i0_i1, plane wmean | Symmetric-c fitness; twin → figS18 |
| figS17 | Heatmap | twin of fig2 | Symmetric-c snowdrift coop |
| figS19 | Heatmap | asymmetric_c1_i, plane qBSeen | Symmetric-i coop; twin → figS21 |
| figS20 | Heatmap | asymmetric_c1_i, plane wmean | Symmetric-i fitness; twin → figS22 |
| figS24 | Heatmap | twin layout of fig3, wmean+Δwmean | Fitness plane; twin → figS26 |
| figS27 | Line | asymmetric_c1_i0_i1_lines, iso-budget, —/P/M/IMP/IJMPQ | Fixed-total coop+fitness; twin → figS28 |
| figS29 | Heatmap | same as fig3, gs = 4 | Fig. 3 at gs = 4; twin → figS30 |
| figS30 | Heatmap | same as figS25, gs = 4 | S25 at gs = 4 |

## Main text figures

| Fig | Message | Figure id | Output |
| --- | ------- | --------- | ------ |
| 1 | Asymmetric c, low symmetric i (coop + difference) | fig1 | ~/figures/interpretation/fig1.png |
| 2 | Asymmetric i at symmetric c: — / P / M / IMP × low-i / high-i / difference | fig2 | ~/figures/interpretation/fig2.png |
| 3 | Asymmetric i under asymmetric c: — / P / M / IMP × cheap / expensive / difference | fig3 | ~/figures/interpretation/fig3.png |

### Panel order notes

1. Main Figs. 1–3: 3×4; columns — | P | M | IMP. Supplement two-pop planes (S10–S12, S16–S26, S29–S23, S25): 3×5; columns — | P | M | IMP | IJMPQ; rows = cheap/expensive/difference (or low-i/high-i/difference for symmetric-c); one colorbar per row; cooperation and fitness are separate figures. S9, S15, S23 are five-column twins of Figs. 1–3.
2. figS3 / figS5: 2×5 strip line plots; row 0 = symmetric costs, row 1 = c₁ = c₀ + 0.02; columns —, P, M, IMP, IJMPQ. S7–S8 are their gs=4 counterparts.
3. figS1 / figS2: 2×5; row 0 = coop, row 1 = fitness; same mechanism columns.
4. S13–S14: 3×5 two-pop symmetric Cost×c (coop + difference); rows = higher-/lower-coop / difference; columns — | P | M | IMP | IJMPQ.
5. figS27 / S28: fixed-total line cuts (2×5; rows coop / fitness; columns —|P|M|IMP|IJMPQ; shared i₁ x title).

Warm line-slice caches before regenerating Figs. S3, S5 / S4, S6 / S27–S28:

```bash
python -m graphgen.main --study asymmetric_c0_c1_lines --export-slices --groupsize 128
python -m graphgen.main --study asymmetric_c1_i0_i1_lines --export-slices --results ~/results
python -m graphgen.main --study symmetric_c_i_lines --export-slices --groupsize 128
```

## Supplement figures

| Supp | Message | id |
| ---- | ------- | -- |
| S1 | Cooperation in one population (PD; coop + fitness) | figS1 |
| S2 | Cooperation in one population (snowdrift) | figS2 |
| S3 | Symmetric and asymmetric cooperation costs in two populations (PD; coop) | figS3 |
| S4 | Fitness under symmetric and asymmetric cooperation costs in two populations (PD) | figS4 |
| S5 | Symmetric and asymmetric cooperation costs in two populations (snowdrift; coop) | figS5 |
| S6 | Fitness under symmetric and asymmetric cooperation costs in two populations (snowdrift) | figS6 |
| S7 | Symmetric and asymmetric cooperation costs at group size 4 in two populations (PD) | figS7 |
| S8 | Symmetric and asymmetric cooperation costs at group size 4 in two populations (snowdrift) | figS8 |
| S9 | Asymmetric cooperation costs, low symmetric i (PD) | figS9 |
| S10 | Fitness under asymmetric cooperation costs and low symmetric i (PD) | figS10 |
| S11 | Asymmetric cooperation costs and low symmetric i (snowdrift; coop) | figS11 |
| S12 | Fitness under asymmetric cooperation costs and low symmetric i (snowdrift) | figS12 |
| S13 | Symmetric cooperation and information costs (PD; coop + difference) | figS13 |
| S14 | Symmetric cooperation and information costs (snowdrift) | figS14 |
| S15 | Symmetric c, asymmetric i (PD) | figS15 |
| S16 | Fitness under symmetric c and asymmetric i (PD) | figS16 |
| S17 | Symmetric c and asymmetric i (snowdrift) | figS17 |
| S18 | Fitness under symmetric c and asymmetric i (snowdrift) | figS18 |
| S19 | Asymmetric cooperation costs and symmetric i (PD; coop) | figS19 |
| S20 | Fitness under asymmetric cooperation costs and symmetric i (PD) | figS20 |
| S21 | Asymmetric cooperation costs and symmetric i (snowdrift; coop) | figS21 |
| S22 | Fitness under asymmetric cooperation costs and symmetric i (snowdrift) | figS22 |
| S23 | Asymmetric c and asymmetric i (PD) | figS23 |
| S24 | Fitness under asymmetric c and asymmetric i (PD) | figS24 |
| S25 | Asymmetric c and asymmetric i (snowdrift) | figS25 |
| S26 | Fitness under asymmetric c and asymmetric i (snowdrift) | figS26 |
| S27 | Asymmetric c and fixed-total i in two populations (PD; coop + fitness) | figS27 |
| S28 | Asymmetric c and fixed-total i in two populations (snowdrift) | figS28 |
| S29 | Asymmetric i under asymmetric c at group size 4 (PD) | figS29 |
| S30 | Asymmetric i under asymmetric c at group size 4 (snowdrift) | figS30 |

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
Supplement legends (S1–S30, including demoted strips S3, S5): regenerate
`paper/captions.md` from the interpretation manifest with `--report`. The DOCX at
`~/figures/interpretation/interpretation.docx` is internal and may differ. Am Nat
legends should generally stay near ≤100 words: descriptive panel text and short
cross-figure pointers only; interpretation belongs in Results.
