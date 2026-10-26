# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal topic backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

`--groupsize` overrides every source, including figS29–figS30 (which embed
`groupsize=4` as counterparts of Figs. 3 and S25). Regenerate those without the
flag, or with `--groupsize 4`:

    python -m graphgen.main --study interpretation --figure figS29 --output ~/figures

Generate all manuscript PNGs and publication reports (figures must exist in the
output directory first). Prefer omitting `--groupsize` for `--all` so source-
level sizes (S29–S30) are kept; pass `--groupsize 128` only for single figures
that should force 128:

    python -m graphgen.main --study interpretation --all --output ~/figures
    python -m graphgen.main --study interpretation --report --output ~/figures

The report includes main text Figs 1–3 (fig1–fig3) and supplement Figs S1–S30
(figS1–S30) in manuscript order. Calibration panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx (internal; all figures)
- Markdown: paper/captions.md (supplement legends S1–S30 only; main-text legends live in results.md)

PD and snowdrift never share a figure. Opener S1–S6 is i × c. S7–S10 are
cooperation-cost line strips with a one-population top row (fitness twins S8/S10;
snowdrift S9/S10). Fig. 1 is asymmetric cooperation cost with low symmetric
information cost (snowdrift twin S13; fitness S12). Fig. 2 is asymmetric
information cost at symmetric cooperation cost (snowdrift twin S17; fitness S16).
Fig. 3 and S25 are asymmetric information cost under asymmetric cooperation costs
(fitness S24/S26). Fixed-total line cuts of Fig. 3 are S27–S28. Group-size-4
counterparts of Figs. 3 and S25 are S29–S30.

Status: revised 2026-10 — one-pop low-i ceilings folded into S7–S10; gs=4 cost
strips dropped; supplement runs to S30. Main Figs. 1–3 are 3×4 (—|P|M|IMP);
supplement heatmaps are 3×5. S11, S15, S23 are five-column twins of Figs. 1–3.

## Setup audit (2026-10)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| figS1 | Heatmap | symmetric_c_i pop_1 | PD i × c; 2×5 coop/fitness |
| figS2 | Heatmap | same as figS1 | Snowdrift twin of S1 |
| figS3 | Heatmap | symmetric_c_i pop_2 | PD 3×5 i × c coop+difference |
| figS4 | Heatmap | same as figS3, wmean | Fitness of Fig. S3 |
| figS5 | Heatmap | twin of figS3 | Snowdrift twin of S3 |
| figS6 | Heatmap | twin of figS4 | Fitness of Fig. S5 |
| figS7 | Line | symmetric_c pop_1 + asymmetric_c0_c1_lines | PD 3×5: one-pop / sym / asym |
| figS8 | Line | same as figS7, wmean | Fitness of Fig. S7 |
| figS9 | Line | same as figS7 | Snowdrift twin of figS7 |
| figS10 | Line | same as figS9, wmean | Fitness of Fig. S9 |
| fig1 | Heatmap | asymmetric_c0_c1, plane qBSeen | PD coop 3×4; twin → figS13; 5-col → figS11 |
| figS12 | Heatmap | asymmetric_c0_c1, plane wmean | PD fitness; twin → figS14 |
| fig2 | Heatmap | asymmetric_i0_i1 | Symmetric-c PD 3×4; twin → figS17; 5-col → figS15 |
| figS16 | Heatmap | asymmetric_i0_i1, plane wmean | Symmetric-c fitness; twin → figS18 |
| fig3 | Heatmap | asymmetric_c1_i0_i1 | Crossed PD 3×4; twin → figS25; 5-col → figS23 |
| figS24 | Heatmap | twin layout of fig3, wmean | Fitness plane; twin → figS26 |
| figS19 | Heatmap | asymmetric_c1_i, plane qBSeen | Symmetric-i coop; twin → figS21 |
| figS20 | Heatmap | asymmetric_c1_i, plane wmean | Symmetric-i fitness; twin → figS22 |
| figS27 | Line | asymmetric_c1_i0_i1_lines, iso-budget | Fixed-total coop+fitness; twin → figS28 |
| figS29 | Heatmap | same as fig3, gs = 4 | Fig. 3 at gs = 4; twin → figS30 |

## Main text figures

| Fig | Message | Figure id | Output |
| --- | ------- | --------- | ------ |
| 1 | Asymmetric cooperation costs (coop + difference) | fig1 | ~/figures/interpretation/fig1.png |
| 2 | Asymmetric information costs: — / P / M / IMP × low-i / high-i / difference | fig2 | ~/figures/interpretation/fig2.png |
| 3 | Asymmetric cooperation and information costs: — / P / M / IMP × cheap / expensive / difference | fig3 | ~/figures/interpretation/fig3.png |

### Panel order notes

1. Main Figs. 1–3: 3×4; columns — | P | M | IMP. Supplement two-pop planes: 3×5.
2. figS1 / figS2: 2×5 one-pop i × c heatmaps; y-axis i, x-axis c.
3. figS7 / figS9: 3×5 strips; row 0 = one population, row 1 = c₁ = c₀, row 2 = c₁ = c₀ + 0.02.
4. figS27 / S28: fixed-total line cuts (2×5; rows coop / fitness).
5. figS29 / S30: gs=4 counterparts of Figs. 3 and S25.

Warm line-slice caches before regenerating Figs. S7–S10 / S27–S28:

```bash
python -m graphgen.main --study asymmetric_c0_c1_lines --export-slices --groupsize 128
python -m graphgen.main --study asymmetric_c1_i0_i1_lines --export-slices --results ~/results
```

## Supplement figures

| Supp | Message | id |
| ---- | ------- | -- |
| S1 | Cooperation and fitness in one population (PD) | figS1 |
| S2 | Cooperation and fitness in one population (snowdrift) | figS2 |
| S3 | Symmetric cooperation and information costs (PD; coop + difference) | figS3 |
| S4 | Fitness under symmetric cooperation and information costs (PD) | figS4 |
| S5 | Symmetric cooperation and information costs (snowdrift) | figS5 |
| S6 | Fitness under symmetric cooperation and information costs (snowdrift) | figS6 |
| S7 | Cooperation under low information costs (PD; one-pop + strips) | figS7 |
| S8 | Fitness under low information costs (PD; one-pop + strips) | figS8 |
| S9 | Cooperation under low information costs (snowdrift; one-pop + strips) | figS9 |
| S10 | Fitness under low information costs (snowdrift; one-pop + strips) | figS10 |
| S11 | Asymmetric cooperation costs (PD) | figS11 |
| S12 | Fitness under asymmetric cooperation costs (PD) | figS12 |
| S13 | Asymmetric cooperation costs (snowdrift; coop) | figS13 |
| S14 | Fitness under asymmetric cooperation costs (snowdrift) | figS14 |
| S15 | Asymmetric information costs (PD) | figS15 |
| S16 | Fitness under asymmetric information costs (PD) | figS16 |
| S17 | Asymmetric information costs (snowdrift) | figS17 |
| S18 | Fitness under asymmetric information costs (snowdrift) | figS18 |
| S19 | Asymmetric cooperation costs and varying information costs (PD; coop) | figS19 |
| S20 | Fitness under asymmetric cooperation costs and varying information costs (PD) | figS20 |
| S21 | Asymmetric cooperation costs and varying information costs (snowdrift; coop) | figS21 |
| S22 | Fitness under asymmetric cooperation costs and varying information costs (snowdrift) | figS22 |
| S23 | Asymmetric cooperation and information costs (PD) | figS23 |
| S24 | Fitness under asymmetric cooperation and information costs (PD) | figS24 |
| S25 | Asymmetric cooperation and information costs (snowdrift) | figS25 |
| S26 | Fitness under asymmetric cooperation and information costs (snowdrift) | figS26 |
| S27 | Asymmetric cooperation costs in two populations (PD; coop + fitness) | figS27 |
| S28 | Asymmetric cooperation costs in two populations (snowdrift) | figS28 |
| S29 | Asymmetric cooperation and information costs at group size 4 (PD) | figS29 |
| S30 | Asymmetric cooperation and information costs at group size 4 (snowdrift) | figS30 |

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
Supplement legends (S1–S30): regenerate `paper/captions.md` from the interpretation
manifest with `--report`. The DOCX at `~/figures/interpretation/interpretation.docx`
is internal and may differ.
