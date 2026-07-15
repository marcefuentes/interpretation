# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal topic backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

Generate all manuscript PNGs and a publication DOCX with legends (figures must
exist in the output directory first):

    python -m graphgen.main --study interpretation --all --groupsize 128 --output ~/figures
    python -m graphgen.main --study interpretation --report --groupsize 128 --output ~/figures

The report includes main text Figs 1–6 (fig1–fig6) and supplement Figs S1–S5
(figS1–figS5) in manuscript order, with cross-references in each legend. Calibration
panels cal1–cal2 are omitted. Output: ~/figures/interpretation/interpretation.docx.

The manuscript figure set lives in ../graph/graphgen/studies/interpretation/ as
fig1–fig6 (main text) and figS1–figS5 (supplement). Graphgen ids match how figures
are called in the manuscript (Fig. 1 → fig1, Fig. S1 → figS1). Auxiliary payoff-plane
calibration panels are cal1–cal2 in the same namespace (not published). Underlying
simulation export names in the pipeline config are internal and do not appear in
manuscript prose.

Do not pass --dilemma-type when generating the interpretation study. figS3 intentionally
mixes two dilemma types in one figure.

**Payoff-plane calibration sweeps** are auxiliary — they support the payoff-gap
attributions cited in the text but do not appear as manuscript figures. Regenerate
with `--figure cal1` or `--figure cal2` when needed; see the supplement table and
the journal calibration analyses.

Status: revised 2026-07 — graphgen ids renamed fig1–fig6 / figS1–figS5 to match
manuscript labels; calibration panels cal1–cal2. Still provisional before locking.

## Setup audit (2026-07)

| Figure | Renderer | Data source | Verdict |
| ------ | -------- | ----------- | ------- |
| fig1 | Line (PLOT) | symmetric_c pop_1, P/M/IJMPQ | Correct — mechanism hierarchy |
| fig2 | Line (PLOT) | symmetric_c pop_2, P | Fixed — line chart for stochastic split at c0 = c1 |
| fig3 | Heatmap | asymmetric_c0_c1 pop_2, P + IJMPQ | Correct — full c0 × c1 triangle |
| fig4 | Heatmap | symmetric_c_i pop_1, IJMPQ | Correct — Cost × c grid |
| fig5 | Heatmap | symmetric_c_i pop_1, P + M | Correct — machinery vs cooperation |
| fig6 | Heatmap | asymmetric_c1_i pop_2, P | Correct — c1 × Cost with c0 fixed |
| figS1 | Line | symmetric_c pop_1, shuffle | Correct — short-memory robustness |
| figS2 | Heatmap | asymmetric_c0_c1 pop_2, P, gs = 4 | Correct — small-group robustness |
| figS3 | Heatmap | symmetric_c_i pop_1, M, dt 0 vs 1 | Correct — dilemma-0 control |
| figS4 | Line (PLOT) | asymmetric_c0_c1_lines pop_2, P | Row 0: c1 = c0 + 0.02; row 1: c0 = c1 |
| figS5 | Heatmap | asymmetric_i0_i1 pop_2, P + IJMPQ | i0 × i1 at c0 = c1 = 0.10; P vs IJMPQ inversion |
| cal1, cal2 | Heatmap | prisoners / snowdrift calibration | Auxiliary — not in supplement |

**Line vs heatmap balance.** Main text: two line figures (fig1, fig2) and four heatmaps
(fig3–fig6). Supplement: two line figures (figS1, figS4) and three heatmaps (figS2, figS3, figS5).

**Not yet wired.** The full i0 × i1 square under crossed cost asymmetry remains
journal-backed and regression-checked but has no interpretation-namespace figure yet
(optional if the manuscript needs a dedicated panel). The symmetric_i study provides
an information-cost line reslice at c = 0.10 (presentation-only alternative to fig4/fig5
heatmaps).

## Main text figures (candidates)

| Fig | Message | Figure id | Command | Output | Journal backing |
| --- | ------- | --------- | ------- | ------ | --------------- |
| 1 | Equal cooperation cost: mechanism hierarchy (single population) | fig1 | `python -m graphgen.main --study interpretation --figure fig1 --groupsize 128 --output ~/figures` | ~/figures/interpretation/fig1.png | Baseline partner choice, reciprocity, combined |
| 2 | Stochastic outcome split under parameter symmetry (c0 = c1) | fig2 | `... --figure fig2 ...` | ~/figures/interpretation/fig2.png | Two populations, equal cooperation cost |
| 3 | Deterministic outcome split under cooperation-cost parameter asymmetry | fig3 | `... --figure fig3 ...` | ~/figures/interpretation/fig3.png | Cooperation-cost asymmetry |
| 4 | Information cost versus cooperation cost (equal between populations) | fig4 | `... --figure fig4 ...` | ~/figures/interpretation/fig4.png | Information cost sweep |
| 5 | Behaviour–mechanism decoupling where cooperation cost is zero | fig5 | `... --figure fig5 ...` | ~/figures/interpretation/fig5.png | Information cost sweep |
| 6 | Information cost under fixed cooperation-cost asymmetry | fig6 | `... --figure fig6 ...` | ~/figures/interpretation/fig6.png | Fixed c0, i × c1 |

### Panel order notes

1. fig1: columns = P, M, IJMPQ; single coevolving population.
2. fig2: line chart, two coevolving populations at c0 = c1 under P; columns =
   cooperation then fitness; red and orange lines = the two populations on shared
   axes vs c. Stochastic outcome split (one population ~0.5 cooperation plateau,
   the other sheds cooperators); fitness inverts (paradox of success).
3. fig3: parameter-asymmetric cooperation cost (c0 < c1); rows = P and IJMPQ for high-
   then low-cost side; columns = cooperation, fitness. Contrast with fig2: deterministic
   outcome split; IJMPQ lifts the expensive population.
4. fig4: IJMPQ; columns = cooperation, fitness; information cost × cooperation cost grid.
5. fig5: rows = P then M; columns = machinery allele then cooperation.
6. fig6: rows = high- then low-cooperation-cost population under P; columns = cooperation,
   fitness; information cost with c0 fixed.

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

### Available alternative: both-costs-asymmetric heatmaps (not yet a manuscript figure)

A full i0 × i1 square (c0 and c1 fixed) is available as imshow heatmaps in
graphgen. The headline pattern — cooperation-cost gap dominance with an IJMPQ
hitchhiking wedge on the i0 ≈ 0 strip — is documented in the journal and
regression-checked in ai/verify_claims.py. Presentation option alongside Fig 6 if
the manuscript needs a panel with both cooperation cost and information cost varying
between populations.

### Available alternative: information-cost line charts (not yet a manuscript figure)

The information-cost axis backing Fig 4 / Fig 5 also exists as a 1D line-chart
reslice at fixed cooperation cost c = 0.10. It carries no new numbers beyond the
information-cost sweep journal doc — presentation option only. See ai/plan.md.

## Supplement figures (candidates)

Robustness and control panels from the primary sweeps only. No calibration heatmaps.

| Supp fig | Message | Figure id | Command | Output |
| -------- | ------- | --------- | ------- | ------ |
| S1 | Short-memory comparison: direct-reciprocity branch shifts collapse ordering | figS1 | `... --figure figS1 ...` | ~/figures/interpretation/figS1.png |
| S2 | Small groups (gs = 4): cooperation-cost asymmetry under partner choice | figS2 | `... --figure figS2 --groupsize 4 ...` | ~/figures/interpretation/figS2.png |
| S3 | Dilemma-0 control: machinery erodes with and without a social dilemma | figS3 | `... --figure figS3 ...` | ~/figures/interpretation/figS3.png |
| S4 | Parameter-symmetric vs parameter-asymmetric cooperation cost (line slices) | figS4 | `... --figure figS4 ...` | ~/figures/interpretation/figS4.png |
| S5 | Information-cost parameter asymmetry at equal cooperation cost (c = 0.10) | figS5 | `... --figure figS5 ...` | ~/figures/interpretation/figS5.png |

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

1. Fig 1. At equal cooperation cost, partner choice, direct reciprocity, and the reputation-rich combined mechanism define the threshold hierarchy the rest of the paper explains.
2. Fig 2. Parameter-symmetric populations (c0 = c1): partner choice breaks outcome
   symmetry stochastically — one population becomes the cooperator and is exploited.
3. Fig 3. Parameter-asymmetric cooperation cost (c0 < c1): partner choice converts
   the payoff gap into a deterministic cooperator/exploiter split; the combined
   mechanism lifts the expensive population and softens both cooperation and fitness
   gaps.
4. Fig 4. When cooperation cost is equal between populations, information cost is soft by itself but lowers the cooperation-cost ceiling once the two costs overlap.
5. Fig 5. Where cooperation cost is zero, the machinery alleles are selected away before cooperation disappears, so behaviour and mechanism decouple.
6. Fig 6. With cooperation-cost asymmetry and c0 fixed above zero, the harmless information-cost edge disappears: information cost retreats the cooperation-cost ceiling and compresses the cooperator/exploiter split.

Supplement captions:

S1. Short-memory mechanisms shift the direct-reciprocity collapse ordering relative to the baseline hierarchy (Fig 1).
S2. At group size 4, cooperation-cost asymmetry under partner choice preserves the deterministic cooperator/exploiter split.
S3. Under dilemma 0, machinery alleles erode with or without a social dilemma; the decoupling in Fig 5 requires the dilemma case.
S4. Line slices contrast deterministic split under c1 = c0 + 0.02 (top row) with the stochastic split at c0 = c1 (bottom row; same data as Fig 2).
S5. At c0 = c1 = 0.10, information-cost asymmetry (i0 < i1) assigns the cooperator role deterministically under partner choice (top rows); combined IJMPQ inverts via cross-population hitchhiking (bottom rows).
