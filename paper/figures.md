# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal doc backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

The manuscript figure set lives in ../graph/graphgen/studies/interpretation/ as
m1–m6 (main text) and ms3–ms5 (supplement). These figure ids pull data from the
underlying study-specific manifests, so the paper can be regenerated with one study
namespace while the original study figures remain available.

Do not pass --dilemma-type when generating the interpretation study. These
manuscript figures rely on the source studies' own default dilemma folders, and
ms5 intentionally mixes two dilemma types in one figure.

**Calibration studies (prisoners, snowdrift)** are auxiliary — they support the
payoff-axis attributions cited in the text but do not appear as manuscript figures.
See the supplement table below and journal/prisoners_calibration.md,
journal/snowdrift_calibration.md.

Status: provisional — adjust before locking the manuscript figure set.

## Main text figures (candidates)

| Fig | Message | Manuscript figure id | graphgen command | Output | Journal backing |
| --- | ------- | -------------------- | ---------------- | ------ | --------------- |
| 1 | Equal-cost baseline: the three canonical families define the mechanism hierarchy on the diagonal (single population) | m1 | python -m graphgen.main --study interpretation --figure m1 --groupsize 128 --output ~/figures | ~/figures/interpretation/m1.png | symmetric_c_partner_choice.md, symmetric_c_reciprocity.md, symmetric_c_combined.md, synthesis.md |
| 2 | Stochastic two-population asymmetry: partner choice breaks symmetry between identical populations; the cooperating side earns less | m6 | python -m graphgen.main --study interpretation --figure m6 --groupsize 128 --output ~/figures | ~/figures/interpretation/m6.png | symmetric_c_partner_choice.md, synthesis.md |
| 3 | Deterministic two-population asymmetry: built-in cost difference is converted into a cooperator/exploiter split; combined mechanisms suppress it | m2 | python -m graphgen.main --study interpretation --figure m2 --groupsize 128 --output ~/figures | ~/figures/interpretation/m2.png | asymmetric_c0_c1_partner_choice.md, asymmetric_c0_c1_combined.md, synthesis.md |
| 4 | Price versus demand on the symmetric branch: Cost is soft alone but retreats the c ceiling | m3 | python -m graphgen.main --study interpretation --figure m3 --groupsize 128 --output ~/figures | ~/figures/interpretation/m3.png | symmetric_c_i.md |
| 5 | Behaviour–mechanism decoupling on the symmetric branch: enforcement alleles erode before cooperation does | m4 | python -m graphgen.main --study interpretation --figure m4 --groupsize 128 --output ~/figures | ~/figures/interpretation/m4.png | symmetric_c_i.md |
| 6 | Price versus demand under pinned roles: no harmless Cost edge remains once c0 is fixed above zero | m5 | python -m graphgen.main --study interpretation --figure m5 --groupsize 128 --output ~/figures | ~/figures/interpretation/m5.png | asymmetric_c1_i.md, synthesis.md |

### Panel order notes

1. m1: columns = P, M, IJMPQ (symmetric_c pop_1).
2. m6: symmetric_c pop_2 under P; rows top to bottom = population with higher cooperation cost label (_1), lower (_0); columns = cooperation, fitness. On the equal-cost diagonal, partner choice stochastically assigns the cooperator role; fitness inverts (paradox of success).
3. m2: asymmetric_c0_c1 pop_2; rows top to bottom = P high-cost population, P low-cost population, IJMPQ high-cost population, IJMPQ low-cost population; columns = cooperation, fitness. Contrast with m6: the same mechanism family now splits deterministically off the diagonal, and IJMPQ lifts the expensive population.
4. m3: columns = cooperation, fitness for IJMPQ on symmetric_c_i.
5. m4: rows = P then M; columns = machinery allele then cooperation.
6. m5: rows = high-cost then low-cost population under P on asymmetric_c1_i; columns = cooperation, fitness.

### Exact commands for the main-text set

1. Fig 1 — m1
   - python -m graphgen.main --study interpretation --figure m1 --groupsize 128 --output ~/figures
2. Fig 2 — m6
   - python -m graphgen.main --study interpretation --figure m6 --groupsize 128 --output ~/figures
3. Fig 3 — m2
   - python -m graphgen.main --study interpretation --figure m2 --groupsize 128 --output ~/figures
4. Fig 4 — m3
   - python -m graphgen.main --study interpretation --figure m3 --groupsize 128 --output ~/figures
5. Fig 5 — m4
   - python -m graphgen.main --study interpretation --figure m4 --groupsize 128 --output ~/figures
6. Fig 6 — m5
   - python -m graphgen.main --study interpretation --figure m5 --groupsize 128 --output ~/figures

### Available alternative: information-cost line charts (not yet a manuscript figure)

The Cost axis backing Fig 4 / Fig 5 also exists as a 1D line-chart reslice, should a
line presentation read better than the m3/m4 heatmaps. The symmetric_c_i study
(and its single-run companion symmetric_c_i_1run) fixes the cooperation cost at
c = c0 = c1 = 0.10 and sweeps the information cost Cost from 0 to 0.30, rendered like
the diagonal cooperation-vs-c line figures but with an "Information cost" x-axis. Data
and image exports are in ~/results/symmetric_c_i{,_1run}/; the manifest is
../graph/graphgen/studies/symmetric_c_i/. It carries no new numbers beyond
journal/symmetric_c_i.md — it is a presentation option only, and is not yet wired
into the interpretation figure namespace. See ai/plan.md item 15.

## Supplement figures (candidates)

Robustness and control panels from the primary studies only. No prisoners or
snowdrift calibration heatmaps.

| Supp fig | Message | Manuscript figure id | graphgen command | Output |
| -------- | ------- | -------------------- | ---------------- | ------ |
| S1 | Short-memory comparison on the diagonal: adding or removing the direct-reciprocity branch shifts the collapse ordering | ms3 | python -m graphgen.main --study interpretation --figure ms3 --groupsize 128 --output ~/figures | ~/figures/interpretation/ms3.png |
| S2 | Small-group mirror for mutualism partner choice: gs = 4 removes the broad high-cooperation basin and exposes the role split more starkly | ms4 | python -m graphgen.main --study interpretation --figure ms4 --groupsize 4 --output ~/figures | ~/figures/interpretation/ms4.png |
| S3 | Control decomposition for information cost: machinery erodes similarly with and without a social dilemma | ms5 | python -m graphgen.main --study interpretation --figure ms5 --groupsize 128 --output ~/figures | ~/figures/interpretation/ms5.png |

## Supplement table (no figure)

Payoff-axis attribution from the auxiliary calibration sweeps. Reproduce the
numbers from journal/synthesis.md and the prisoners/snowdrift calibration docs;
do not publish the full payoff-plane heatmaps.

| Mechanism family | Limiting payoff gap | Primary calibration doc |
| ---------------- | ------------------- | --------------------- |
| M (direct reciprocity) | Risk / defection payoff P | prisoners_calibration.md, snowdrift_calibration.md |
| P (partner choice) | Cooperation advantage R − P | prisoners_calibration.md |
| MP, MPQ, IMP, IJMPQ (combined / reputation-rich) | Reward / temptation R | prisoners_calibration.md |

## Draft captions

1. Fig 1. On the equal-cost diagonal, partner choice, direct reciprocity, and the reputation-rich combined mechanism define the threshold hierarchy the rest of the paper explains.
2. Fig 2. With two identical populations, partner choice breaks symmetry stochastically: one population becomes the cooperator and is exploited by the other (symmetric_c pop_2).
3. Fig 3. With built-in cost asymmetry, partner choice converts the payoff gap into a deterministic cooperator/exploiter split; the combined mechanism lifts the expensive population and softens both cooperation and fitness asymmetry (asymmetric_c0_c1 pop_2).
4. Fig 4. On the symmetric branch, information cost is soft by itself but lowers the cooperation-cost ceiling once the two costs overlap.
5. Fig 5. On the symmetric low-demand edge, the machinery alleles are selected away before cooperation disappears, so behaviour and mechanism decouple.
6. Fig 6. On the asymmetric branch with c0 fixed above zero, the harmless Cost edge disappears: Cost retreats the c1 ceiling and compresses the cooperator/exploiter split.
