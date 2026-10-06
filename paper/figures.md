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

The report includes main text Figs 1–4 (fig1–fig4) and supplement Figs S1–S21
(figS1–S21) in manuscript order. Calibration panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx
- Markdown mirror: paper/captions.md

PD and snowdrift never share a figure. Fig. S19 is the full i₀ × i₁ PD heatmap
behind the relational line cuts (Figs. 3–4, S15); there is no snowdrift twin of S19.
Shuffle short-memory branches are prose-only (no dedicated S panels).

Status: revised 2026-10 — S1–S2 one-pop ceilings with coop + fitness rows; former
shuffle S3–S4 dropped; fitness twins of Figs. 1–2 are S3–S4; supplement runs to S21.

## Setup audit (2026-10)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| fig1 | Line | asymmetric_c0_c1_lines, _/P/M/IJMPQ | PD; row0 sym, row1 gap |
| fig2 | Line | same as fig1 | Snowdrift twin of fig1 |
| fig3 | Line | asymmetric_c1_i0_i1_lines, P + IJMPQ | PD; twin → figS20 |
| fig4 | Line | asymmetric_c1_i0_i1_lines, IJMPQ | PD; twin → figS21 |
| figS1 | Line | symmetric_c pop_1, _/P/M/IJMPQ | PD; 2×4 coop/fitness |
| figS2 | Line | same as figS1 | Snowdrift twin of S1 |
| figS3 | Line | same as fig1, wmean | Fitness of Fig. 1 |
| figS4 | Line | same as fig2, wmean | Fitness of Fig. 2 |
| figS5 | Heatmap | asymmetric_c0_c1, P + IJMPQ | PD; twin → figS6 |
| figS7 | Heatmap | asymmetric_c0_c1, P, gs = 4 | PD; twin → figS8 |
| figS9 | Line | symmetric_c_i_lines, P + M at c = 0 | PD; twin → figS10 |
| figS11 | Heatmap | symmetric_c_i, IJMPQ | PD Cost×c; twin → figS12 |
| figS13 | Heatmap | asymmetric_c1_i, P | PD; twin → figS14 |
| figS15 | Line | asymmetric_c1_i0_i1_lines, P + IJMPQ | Fitness of Fig. 3; twin → figS16 |
| figS17 | Heatmap | asymmetric_i0_i1, P + IJMPQ | PD; twin → figS18 |
| figS19 | Heatmap | asymmetric_c1_i0_i1, P + IJMPQ | PD full square (no SD twin) |
| figS20–S21 | twins | Figs. 3–4 | Snowdrift |

## Main text figures

| Fig | Message | Figure id | Output |
| --- | ------- | --------- | ------ |
| 1 | Matched vs gap cooperation cost (PD) | fig1 | ~/figures/interpretation/fig1.png |
| 2 | Matched vs gap cooperation cost (snowdrift) | fig2 | ~/figures/interpretation/fig2.png |
| 3 | Relational information cost | fig3 | ~/figures/interpretation/fig3_qBSeen.png |
| 4 | Near-zero-i₀ wedge | fig4 | ~/figures/interpretation/fig4_qBSeen.png |

### Panel order notes

1. fig1 / fig2: 2×4; row 0 = matched costs, row 1 = c₁ = c₀ + 0.02; columns —, P, M, IJMPQ.
2. figS1 / figS2: 2×4; row 0 = coop, row 1 = fitness; same mechanism columns.
3. fig3: rows P then IJMPQ; columns i0 strip, i1 strip, fixed total.
4. fig4: coop then fitness rows; i0 held per column.

Warm line-slice caches before regenerating Figs. 1–4 / S3–S4:

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
| S5 | Full c₀ × c₁ grid PD | figS5 |
| S6 | Full c₀ × c₁ grid snowdrift | figS6 |
| S7 | gs = 4 asymmetry PD | figS7 |
| S8 | gs = 4 asymmetry snowdrift | figS8 |
| S9 | c = 0 decoupling PD | figS9 |
| S10 | c = 0 decoupling snowdrift | figS10 |
| S11 | Cost × c heatmap PD | figS11 |
| S12 | Cost × c heatmap snowdrift | figS12 |
| S13 | Shared-i under c-gap PD | figS13 |
| S14 | Shared-i under c-gap snowdrift | figS14 |
| S15 | Fitness of Fig. 3 | figS15 |
| S16 | Fitness of Fig. S20 | figS16 |
| S17 | Equal-c i asymmetry PD | figS17 |
| S18 | Equal-c i asymmetry snowdrift | figS18 |
| S19 | Full i₀ × i₁ grid PD | figS19 |
| S20 | Snowdrift twin of Fig. 3 | figS20 |
| S21 | Snowdrift twin of Fig. 4 | figS21 |

## Auxiliary figures (not in supplement)

| id | Output |
| -- | ------ |
| cal1 | ~/figures/interpretation/cal1.png |
| cal2 | ~/figures/interpretation/cal2.png |
| aux_m_nodilemma | ~/figures/interpretation/aux_m_nodilemma.png |

## Supplement table (Table S1)

See [supplement.md](supplement.md).

## Draft captions

Authoritative source: `graphgen/studies/interpretation/manifest.py`; regenerate
`paper/captions.md` with `--report`.
