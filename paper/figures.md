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

The report includes main text Figs 1–6 (fig1–fig6) and supplement Figs S1–S8
(figS1–figS8) in manuscript order, with cross-references in each legend. Calibration
panels cal1–cal2 are omitted. Outputs:

- DOCX: ~/figures/interpretation/interpretation.docx
- Markdown mirror: paper/captions.md (sibling interpretation repo; PNG embeds
  point at the figure output directory used for that run)

The manuscript figure set lives in ../graph/graphgen/studies/interpretation/ as
fig1–fig6 (main text) and figS1–figS8 (supplement). Graphgen ids match how figures
are called in the manuscript (Fig. 1 → fig1, Fig. S1 → figS1). Auxiliary payoff-plane
calibration panels are cal1–cal2 in the same namespace (not published). Underlying
simulation export names in the pipeline config are internal and do not appear in
manuscript prose.

Do not pass --dilemma-type when generating the interpretation study. figS6 intentionally
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
| fig2 | Line (PLOT) | symmetric_c pop_2, P | Partner choice; PD row stochastic split vs figS2 control |
| fig3 | Heatmap | asymmetric_c0_c1 pop_2, P + IJMPQ | Correct — full c0 × c1 triangle |
| fig4 | Heatmap | symmetric_c_i pop_1, IJMPQ | Correct — Cost × c grid |
| fig5 | Heatmap | symmetric_c_i pop_1, P + M | Correct — machinery vs cooperation |
| fig6 | Heatmap | asymmetric_c1_i pop_2, P | Correct — c1 × Cost with c0 fixed |
| figS1 | Line (PLOT) | symmetric_c pop_1, _ | No enforcement; contrast for fig1 (PD vs snowdrift) |
| figS2 | Line (PLOT) | symmetric_c pop_2, _ | No enforcement; contrast for fig2 (PD vs snowdrift) |
| figS3 | Heatmap | asymmetric_c0_c1 pop_2, _ | No enforcement; contrast for fig3 |
| figS4 | Line | symmetric_c pop_1, shuffle | Short-memory robustness |
| figS5 | Heatmap | asymmetric_c0_c1 pop_2, P, gs = 4 | Small-group robustness |
| figS6 | Heatmap | symmetric_c_i pop_1, M, dt 0 vs 1 | Dilemma-0 control |
| figS7 | Line (PLOT) | asymmetric_c0_c1_lines pop_2, P | Row 0: c1 = c0 + 0.02; row 1: c0 = c1 |
| figS8 | Heatmap | asymmetric_i0_i1 pop_2, P + IJMPQ | i0 × i1 at c0 = c1 = 0.10; P vs IJMPQ inversion |
| cal1, cal2 | Heatmap | prisoners / snowdrift calibration | Auxiliary — not in supplement |

**Line vs heatmap balance.** Main text: two line figures (fig1, fig2) and four heatmaps
(fig3–fig6). Supplement: four line figures (figS1, figS2, figS4, figS7) and four heatmaps (figS3, figS5, figS6, figS8).

**Dilemma rows.** Single-row figures (fig1, fig2, fig4, figS1, figS2, figS4) stack prisoner's dilemma
(row 0) and snowdrift (row 1). Multi-row figures keep their existing row semantics
(mechanism, population, or line-slice contrasts). figS6 intentionally compares dilemma 0
versus prisoner's dilemma only; fig5 is mechanism rows (P then M), not a dilemma contrast.

**Not yet wired.** The full i0 × i1 square under crossed cost asymmetry remains
journal-backed and regression-checked but has no interpretation-namespace figure yet
(optional if the manuscript needs a dedicated panel). The symmetric_i study provides
an information-cost line reslice at c = 0.10 (presentation-only alternative to fig4/fig5
heatmaps).

## Main text figures (candidates)

| Fig | Message | Figure id | Command | Output | Journal backing |
| --- | ------- | --------- | ------- | ------ | --------------- |
| 1 | Equal cooperation cost: mechanism hierarchy (single population) | fig1 | `python -m graphgen.main --study interpretation --figure fig1 --groupsize 128 --output ~/figures` | ~/figures/interpretation/fig1.png | Baseline partner choice, reciprocity, combined |
| 2 | Outcome asymmetry under parameter symmetry (c0 = c1), partner choice | fig2 | `... --figure fig2 ...` | ~/figures/interpretation/fig2.png | Two populations, equal cooperation cost |
| 3 | Deterministic outcome split under cooperation-cost parameter asymmetry | fig3 | `... --figure fig3 ...` | ~/figures/interpretation/fig3.png | Cooperation-cost asymmetry |
| 4 | Information cost versus cooperation cost (equal between populations) | fig4 | `... --figure fig4 ...` | ~/figures/interpretation/fig4.png | Information cost sweep |
| 5 | Behaviour–mechanism decoupling where cooperation cost is zero | fig5 | `... --figure fig5 ...` | ~/figures/interpretation/fig5.png | Information cost sweep |
| 6 | Information cost under fixed cooperation-cost asymmetry | fig6 | `... --figure fig6 ...` | ~/figures/interpretation/fig6.png | Fixed c0, i × c1 |

### Panel order notes

1. fig1: columns = P, M, IJMPQ; single coevolving population; row 0 = prisoner's dilemma, row 1 = snowdrift.
2. fig2: line chart, two coevolving populations at c0 = c1 under P; row 0 = prisoner's dilemma, row 1 = snowdrift; columns =
   cooperation then fitness. **PD:** partner choice stochastically assigns cooperator and exploiter roles absent under figS2. **Snowdrift:** outcome asymmetry already present without enforcement machinery; P mainly reshapes high-c regimes. Fitness can invert (paradox of success).
3. fig3: parameter-asymmetric cooperation cost (c0 < c1), **prisoner's dilemma only**; rows = P and IJMPQ for high-
   then low-cost side; columns = cooperation, fitness. Contrast with fig2 (PD row): deterministic
   outcome split; IJMPQ lifts the expensive population. **Why no snowdrift row:** the cheap population
   already cooperates at ceiling under no enforcement (~0.96), so partner choice adds little beyond the
   payoff floor; between-population snowdrift asymmetry is shown in fig2 (row 1) and figS2–S3 instead.
   A full asymmetric snowdrift heatmap would mostly restate game-structure effects, not a new
   mechanism attribution.
4. fig4: IJMPQ; row 0 = prisoner's dilemma, row 1 = snowdrift; columns = cooperation, fitness; information cost × cooperation cost grid.
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

Robustness panels from the primary sweeps only. No-enforcement controls (figS1–figS3) open the supplement; no calibration heatmaps.

| Supp fig | Message | Figure id | Command | Output |
| -------- | ------- | --------- | ------- | ------ |
| S1 | No-enforcement control for Fig. 1 (single population) | figS1 | `... --figure figS1 ...` | ~/figures/interpretation/figS1.png |
| S2 | No-enforcement control for Fig. 2 (symmetric two populations) | figS2 | `... --figure figS2 ...` | ~/figures/interpretation/figS2.png |
| S3 | No-enforcement control for Fig. 3 (asymmetric two populations) | figS3 | `... --figure figS3 ...` | ~/figures/interpretation/figS3.png |
| S4 | Short-memory comparison: direct-reciprocity branch shifts collapse ordering | figS4 | `... --figure figS4 ...` | ~/figures/interpretation/figS4.png |
| S5 | Small groups (gs = 4): cooperation-cost asymmetry under partner choice | figS5 | `... --figure figS5 --groupsize 4 ...` | ~/figures/interpretation/figS5.png |
| S6 | Dilemma-0 control: machinery erodes with and without a social dilemma | figS6 | `... --figure figS6 ...` | ~/figures/interpretation/figS6.png |
| S7 | Parameter-symmetric vs parameter-asymmetric cooperation cost (line slices) | figS7 | `... --figure figS7 ...` | ~/figures/interpretation/figS7.png |
| S8 | Information-cost parameter asymmetry at equal cooperation cost (c = 0.10) | figS8 | `... --figure figS8 ...` | ~/figures/interpretation/figS8.png |

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
2. Fig 2. Two coevolving populations at equal cooperation cost (c0 = c1) under partner choice. In the prisoner's dilemma (top row), partner choice stochastically assigns cooperator and exploiter roles that are absent under the no-machinery control (Fig. S2); the cooperator side can earn lower fitness. In snowdrift (bottom row), a similar split already appears without enforcement machinery; partner choice mainly reshapes outcomes at high cooperation cost.
3. Fig 3. Parameter-asymmetric cooperation cost (c0 < c1), prisoner's dilemma: partner choice converts
   the payoff gap into a deterministic cooperator/exploiter split; the combined
   mechanism lifts the expensive population and softens both cooperation and fitness
   gaps. Shown for the PD only: snowdrift already sustains high cooperation and
   outcome asymmetry without enforcement (see Fig. 2 snowdrift row and Fig. S2–S3), so
   an asymmetric snowdrift heatmap would not isolate what partner choice adds.
4. Fig 4. When cooperation cost is equal between populations, information cost is soft by itself but lowers the cooperation-cost ceiling once the two costs overlap.
5. Fig 5. Where cooperation cost is zero, the machinery alleles are selected away before cooperation disappears, so behaviour and mechanism decouple.
6. Fig 6. With cooperation-cost asymmetry and c0 fixed above zero, the harmless information-cost edge disappears: information cost retreats the cooperation-cost ceiling and compresses the cooperator/exploiter split.

Supplement captions:

S1. Control baseline for Fig. 1: enforcement off in a single population. Cooperation collapses in the prisoner's dilemma; snowdrift sustains cooperation from payoffs alone.
S2. Control baseline for Fig. 2: enforcement off with two symmetric populations. Prisoner's dilemma populations remain outcome-symmetric at moderate cost; snowdrift breaks outcome symmetry from the payoff structure alone.
S3. Control baseline for Fig. 3: enforcement off with cooperation-cost parameter asymmetry. Partner choice is what pins the deterministic cooperator/exploiter split.
S4. Short-memory mechanisms shift the direct-reciprocity collapse ordering relative to the baseline hierarchy (Fig 1).
S5. At group size 4, cooperation-cost asymmetry under partner choice preserves the deterministic cooperator/exploiter split.
S6. Under dilemma 0, machinery alleles erode with or without a social dilemma; the decoupling in Fig 5 requires the dilemma case.
S7. Line slices contrast deterministic split under c1 = c0 + 0.02 (top row) with the stochastic split at c0 = c1 (bottom row; same data as Fig 2).
S8. At c0 = c1 = 0.10, information-cost asymmetry (i0 < i1) assigns the cooperator role deterministically under partner choice (top rows); combined IJMPQ inverts via cross-population hitchhiking (bottom rows).
