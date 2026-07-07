# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal doc backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

The manuscript figure set now lives in ../graph/graphgen/studies/interpretation/
as m1–m5 (main text) and ms1–ms5 (supplement). These figure ids pull data
from the underlying study-specific manifests, so the paper can be regenerated with
one study namespace while the original study figures remain available.

Do not pass --dilemma-type when generating the interpretation study. These
manuscript figures rely on the source studies' own default dilemma folders, and
ms5 intentionally mixes two dilemma types in one figure.

Status: provisional — m1–m5 / ms1–ms5 are current candidates, implemented in
graphgen for review. Adjust before locking the manuscript figure set.

## Main text figures (candidates)

| Fig | Message | Manuscript figure id | graphgen command | Output | Journal backing |
| --- | ------- | -------------------- | ---------------- | ------ | --------------- |
| 1 | Equal-cost baseline: the three canonical families define the mechanism hierarchy on the hamilton diagonal | m1 | python -m graphgen.main --study interpretation --figure m1 --groupsize 128 --output ~/figures | ~/figures/interpretation/m1.png | hamilton_partner_choice.md, hamilton_reciprocity.md, hamilton_combined.md, synthesis.md |
| 2 | Two-population asymmetry: partner choice creates the deterministic role split, IJMPQ suppresses it | m2 | python -m graphgen.main --study interpretation --figure m2 --groupsize 128 --output ~/figures | ~/figures/interpretation/m2.png | mutualism_partner_choice.md, mutualism_combined.md, synthesis.md |
| 3 | Price versus demand on the symmetric branch: Cost is soft alone but retreats the c ceiling | m3 | python -m graphgen.main --study interpretation --figure m3 --groupsize 128 --output ~/figures | ~/figures/interpretation/m3.png | hamilton_cost.md |
| 4 | Behaviour–mechanism decoupling on the symmetric branch: enforcement alleles erode before cooperation does | m4 | python -m graphgen.main --study interpretation --figure m4 --groupsize 128 --output ~/figures | ~/figures/interpretation/m4.png | hamilton_cost.md |
| 5 | Price versus demand under pinned roles: no harmless Cost edge remains once c0 is fixed above zero | m5 | python -m graphgen.main --study interpretation --figure m5 --groupsize 128 --output ~/figures | ~/figures/interpretation/m5.png | mutualism_cost.md, synthesis.md |

### Panel order notes

1. m1: columns = P, M, IJMPQ.
2. m2: rows top to bottom = P high-cost population, P low-cost population, IJMPQ high-cost population, IJMPQ low-cost population; columns = cooperation, fitness.
3. m3: columns = cooperation, fitness for IJMPQ on hamilton_cost.
4. m4: rows = P then M; columns = machinery allele then cooperation.
5. m5: rows = high-cost then low-cost population under P on mutualism_cost; columns = cooperation, fitness.

### Exact commands for the main-text set

1. Fig 1
   - python -m graphgen.main --study interpretation --figure m1 --groupsize 128 --output ~/figures
2. Fig 2
   - python -m graphgen.main --study interpretation --figure m2 --groupsize 128 --output ~/figures
3. Fig 3
   - python -m graphgen.main --study interpretation --figure m3 --groupsize 128 --output ~/figures
4. Fig 4
   - python -m graphgen.main --study interpretation --figure m4 --groupsize 128 --output ~/figures
5. Fig 5
   - python -m graphgen.main --study interpretation --figure m5 --groupsize 128 --output ~/figures

## Supplement figures (candidates)

| Supp fig | Message | Manuscript figure id | graphgen command | Output |
| -------- | ------- | -------------------- | ---------------- | ------ |
| S1 | Payoff-axis calibration in the PD sweep: P, M, and IJMPQ define the cooperation-advantage / risk / reward split | ms1 | python -m graphgen.main --study interpretation --figure ms1 --groupsize 128 --output ~/figures | ~/figures/interpretation/ms1.png |
| S2 | Snowdrift mirror: high S raises the cooperation floor and softens risk-led collapse | ms2 | python -m graphgen.main --study interpretation --figure ms2 --groupsize 128 --output ~/figures | ~/figures/interpretation/ms2.png |
| S3 | Short-memory comparison on the hamilton diagonal: adding or removing the direct-reciprocity branch shifts the collapse ordering | ms3 | python -m graphgen.main --study interpretation --figure ms3 --groupsize 128 --output ~/figures | ~/figures/interpretation/ms3.png |
| S4 | Small-group mirror for mutualism partner choice: gs = 4 removes the broad high-cooperation basin and exposes the role split more starkly | ms4 | python -m graphgen.main --study interpretation --figure ms4 --groupsize 4 --output ~/figures | ~/figures/interpretation/ms4.png |
| S5 | Control decomposition for information cost: machinery erodes similarly with and without a social dilemma | ms5 | python -m graphgen.main --study interpretation --figure ms5 --groupsize 128 --output ~/figures | ~/figures/interpretation/ms5.png |

## Draft captions

1. Fig 1. On the equal-cost diagonal, partner choice, direct reciprocity, and the reputation-rich combined mechanism define the threshold hierarchy the rest of the paper explains.
2. Fig 2. In mutualism, partner choice converts the built-in cost asymmetry into a cooperator/exploiter split, while the combined mechanism lifts the expensive population and softens both cooperation and fitness asymmetry.
3. Fig 3. On the symmetric branch, information cost is soft by itself but lowers the cooperation-cost ceiling once the two costs overlap.
4. Fig 4. On the symmetric low-demand edge, the machinery alleles are selected away before cooperation disappears, so behaviour and mechanism decouple.
5. Fig 5. On the asymmetric branch with c0 fixed above zero, the harmless Cost edge disappears: Cost retreats the c1 ceiling and compresses the cooperator/exploiter split.
