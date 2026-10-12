# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal topic backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

`--groupsize` overrides every source, including figS7/figS8 (which embed
`groupsize=4`). Regenerate those without the flag, or with `--groupsize 4`:

    python -m graphgen.main --study interpretation --figure figS7 --output ~/figures
    python -m graphgen.main --study interpretation --figure figS8 --output ~/figures

Generate all manuscript PNGs and publication reports (figures must exist in the
output directory first). Prefer omitting `--groupsize` for `--all` so source-
level sizes (S7/S8) are kept; pass `--groupsize 128` only for single figures
that should force 128:

    python -m graphgen.main --study interpretation --all --output ~/figures
    python -m graphgen.main --study interpretation --report --output ~/figures

The report includes main text Figs 1–4 (fig1–fig4) and supplement Figs S1–S20
(figS1–S20) in manuscript order. Calibration panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx (internal; all figures)
- Markdown: paper/captions.md (supplement legends S1–S20 only; main-text legends live in results.md)

PD and snowdrift never share a figure. Figs. 3–4 are a PD/SD pair (like Figs. 1–2)
on the full i₀ × i₁ square. Fitness twins are S13–S14. Line cuts (coop + fitness)
are S15–S16 (who-pays) and S17–S18 (wedge). Shuffle short-memory branches are
prose-only (no dedicated S panels).

Status: revised 2026-10 — Figs. 3–4 are 3×3 heatmaps (P|M|IJMPQ × cheap/expensive/gap)
on the full [0, b]×[0, b] square (441 cells). Who-pays and wedge line plots (with
fitness rows) are S15–S18; equal-c asymmetry is S19–S20; supplement runs to S20.

## Setup audit (2026-10)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| fig1 | Line | asymmetric_c0_c1_lines, _/P/M/IJMPQ | PD; row0 sym, row1 gap |
| fig2 | Line | same as fig1 | Snowdrift twin of fig1 |
| fig3 | Heatmap | asymmetric_c1_i0_i1, P+M+IJMPQ, qBSeen+ΔqBSeen | PD 3×3 plane; twin → fig4 |
| fig4 | Heatmap | twin of fig3 | Snowdrift 3×3 plane |
| figS1 | Line | symmetric_c pop_1, _/P/M/IJMPQ | PD; 2×4 coop/fitness |
| figS2 | Line | same as figS1 | Snowdrift twin of S1 |
| figS3 | Line | same as fig1, wmean | Fitness of Fig. 1 |
| figS4 | Line | same as fig2, wmean | Fitness of Fig. 2 |
| figS5 | Heatmap | asymmetric_c0_c1, P + IJMPQ | PD 2×4; twin → figS6 |
| figS7 | Heatmap | asymmetric_c0_c1, P + IJMPQ, gs = 4 | PD 2×4; twin → figS8 |
| figS9 | Heatmap | symmetric_c_i, P + IJMPQ | PD 2×2 Cost×c; twin → figS10 |
| figS11 | Heatmap | asymmetric_c1_i, P + IJMPQ | PD 2×4; twin → figS12 |
| figS13 | Heatmap | twin layout of fig3, wmean+Δwmean | Fitness plane; twin → figS14 |
| figS15 | Line | asymmetric_c1_i0_i1_lines, P + IJMPQ | Who-pays coop+fitness; twin → figS16 |
| figS17 | Line | wedge, qBSeen+wmean, P + IJMPQ | Wedge coop+fitness; twin → figS18 |
| figS19 | Heatmap | asymmetric_i0_i1, P + IJMPQ | Equal-c; twin → figS20 |

## Main text figures

| Fig | Message | Figure id | Output |
| --- | ------- | --------- | ------ |
| 1 | Matched vs gap cooperation cost (PD) | fig1 | ~/figures/interpretation/fig1.png |
| 2 | Matched vs gap cooperation cost (snowdrift) | fig2 | ~/figures/interpretation/fig2.png |
| 3 | i₀ × i₁ plane: cheap / expensive / gap (PD) | fig3 | ~/figures/interpretation/fig3.png |
| 4 | i₀ × i₁ plane: cheap / expensive / gap (snowdrift) | fig4 | ~/figures/interpretation/fig4.png |

### Panel order notes

1. fig1 / fig2: 2×4; row 0 = matched costs, row 1 = c₁ = c₀ + 0.02; columns —, P, M, IJMPQ.
2. figS1 / figS2: 2×4; row 0 = coop, row 1 = fitness; same mechanism columns.
3. Heatmaps S5–S8, S11–S12, S19–S20: 2×4; rows = coop / fitness; spanning column titles P | IJMPQ; within each mechanism, cheap then expensive file set. S9–S10: 2×2 one-pop Cost×c; same row grammar; columns P | IJMPQ.
4. fig3 / fig4 / S13–S14: 3×3; columns P | M | IJMPQ; rows = cheap, expensive, gap (coop or fitness); one colorbar per row.
5. figS15 / S16: who-pays line cuts (4×3; rows P-coop, P-fitness, IJMPQ-coop, IJMPQ-fitness; columns tax-cheap, fixed total, tax-expensive). figS17 / S18: wedge line cuts (4×4; same row grammar; columns hold i₀ while sweeping i₁).

Warm line-slice caches before regenerating Figs. 1–2 / S3–S4 / S15–S18:

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
| S9 | Cost × c heatmap PD | figS9 |
| S10 | Cost × c heatmap snowdrift | figS10 |
| S11 | Shared-i under c-gap PD | figS11 |
| S12 | Shared-i under c-gap snowdrift | figS12 |
| S13 | Fitness twin of Fig. 3 | figS13 |
| S14 | Fitness twin of Fig. 4 | figS14 |
| S15 | Who-pays line cuts (PD; coop + fitness) | figS15 |
| S16 | Who-pays line cuts (snowdrift) | figS16 |
| S17 | Wedge line cuts (PD; coop + fitness) | figS17 |
| S18 | Wedge line cuts (snowdrift) | figS18 |
| S19 | Equal-c i asymmetry PD | figS19 |
| S20 | Equal-c i asymmetry snowdrift | figS20 |

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
Supplement legends (S1–S20): regenerate `paper/captions.md` from the interpretation
manifest with `--report`. The DOCX at `~/figures/interpretation/interpretation.docx`
is internal and may differ. Am Nat legends should generally stay near ≤100 words:
descriptive panel text and short cross-figure pointers only; interpretation belongs
in Results.
