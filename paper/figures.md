# Figure Manifest

Specification and provenance for the manuscript figures. No image binaries live in
this repo — figures are generated artifacts. This manifest records, per manuscript
figure, what it shows, the graphgen figure id that produces it, the exact command,
where the output lands, a draft caption, and the journal topic backing it.

Regenerate any manuscript figure from ~/code/graph with the venv active:

    cd ~/code/graph && . .venv/bin/activate
    python -m graphgen.main --study interpretation --figure FIG --groupsize 128 --output ~/figures

The manuscript figure set lives in ../graph/graphgen/studies/interpretation/ as
m1–m6 (main text) and ms3–ms5 (supplement). Figure ids m1–m6 pull from underlying
simulation exports via the interpretation namespace; graphgen study names in the
pipeline config are internal and do not appear in manuscript prose.

Do not pass --dilemma-type when generating the interpretation study. ms5 intentionally
mixes two dilemma types in one figure.

**Payoff-plane calibration sweeps** are auxiliary — they support the payoff-gap
attributions cited in the text but do not appear as manuscript figures. See the
supplement table and the journal calibration analyses.

Status: provisional — adjust before locking the manuscript figure set.

## Main text figures (candidates)

| Fig | Message | Figure id | Command | Output | Journal backing |
| --- | ------- | --------- | ------- | ------ | --------------- |
| 1 | Equal cooperation cost: mechanism hierarchy (single population) | m1 | `python -m graphgen.main --study interpretation --figure m1 --groupsize 128 --output ~/figures` | ~/figures/interpretation/m1.png | Baseline partner choice, reciprocity, combined |
| 2 | Stochastic two-population split under partner choice | m6 | `... --figure m6 ...` | ~/figures/interpretation/m6.png | Two populations, equal cooperation cost |
| 3 | Deterministic split under cooperation-cost asymmetry; combined mechanisms suppress it | m2 | `... --figure m2 ...` | ~/figures/interpretation/m2.png | Cooperation-cost asymmetry |
| 4 | Information cost versus cooperation cost (equal between populations) | m3 | `... --figure m3 ...` | ~/figures/interpretation/m3.png | Information cost sweep |
| 5 | Behaviour–mechanism decoupling where cooperation cost is zero | m4 | `... --figure m4 ...` | ~/figures/interpretation/m4.png | Information cost sweep |
| 6 | Information cost under fixed cooperation-cost asymmetry | m5 | `... --figure m5 ...` | ~/figures/interpretation/m5.png | Fixed c0, i × c1 |

### Panel order notes

1. m1: columns = P, M, IJMPQ; single coevolving population.
2. m6: two equal-cooperation-cost populations under P; rows = higher- then lower-cost
   population labels; columns = cooperation, fitness. Partner choice stochastically
   assigns the cooperator role; fitness inverts (paradox of success).
3. m2: two populations with c0 < c1; rows = P and IJMPQ for high- then low-cost
   side; columns = cooperation, fitness. Contrast with m6: deterministic split;
   IJMPQ lifts the expensive population.
4. m3: IJMPQ; columns = cooperation, fitness; information cost × cooperation cost grid.
5. m4: rows = P then M; columns = machinery allele then cooperation.
6. m5: rows = high- then low-cooperation-cost population under P; columns = cooperation,
   fitness; information cost with c0 fixed.

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
| S1 | Short-memory comparison: direct-reciprocity branch shifts collapse ordering | ms3 | `... --figure ms3 ...` | ~/figures/interpretation/ms3.png |
| S2 | Small groups (gs = 4): cooperation-cost asymmetry under partner choice | ms4 | `... --figure ms4 --groupsize 4 ...` | ~/figures/interpretation/ms4.png |
| S3 | Dilemma-0 control: machinery erodes with and without a social dilemma | ms5 | `... --figure ms5 ...` | ~/figures/interpretation/ms5.png |

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
2. Fig 2. With two identical populations, partner choice breaks symmetry stochastically: one population becomes the cooperator and is exploited by the other.
3. Fig 3. With cooperation-cost asymmetry, partner choice converts the payoff gap into a deterministic cooperator/exploiter split; the combined mechanism lifts the expensive population and softens both cooperation and fitness asymmetry.
4. Fig 4. When cooperation cost is equal between populations, information cost is soft by itself but lowers the cooperation-cost ceiling once the two costs overlap.
5. Fig 5. Where cooperation cost is zero, the machinery alleles are selected away before cooperation disappears, so behaviour and mechanism decouple.
6. Fig 6. With cooperation-cost asymmetry and c0 fixed above zero, the harmless information-cost edge disappears: information cost retreats the cooperation-cost ceiling and compresses the cooperator/exploiter split.
