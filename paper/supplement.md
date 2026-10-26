# Supplement

Companion to the main text. Supplement figure captions:
[captions.md](captions.md). PNG provenance: [figures.md](figures.md). Payoff equations and
constants: [parameterization](../journal/parameterization.md). Headline numbers
are regression-checked by `ai/verify_claims.py`.

## Contents

| Item | Role | Main-text anchor |
| ---- | ---- | ---------------- |
| Fig. S1 | Cooperation and fitness in one population (PD) | Results §1 |
| Fig. S2 | Cooperation and fitness in one population (snowdrift) | Results §1 |
| Fig. S3 | Cooperation under symmetric cooperation and information costs (PD) | Results §3 |
| Fig. S4 | Fitness under symmetric cooperation and information costs (PD) | Figs. S3, S5 |
| Fig. S5 | Cooperation under symmetric cooperation and information costs (snowdrift) | Results §3 |
| Fig. S6 | Fitness under symmetric cooperation and information costs (snowdrift) | Figs. S3, S5 |
| Fig. S7 | Cooperation under low information costs (PD; one-pop + strips) | Fig. 1; Results §1–2 |
| Fig. S8 | Fitness under low information costs (PD; one-pop + strips) | Figs. S7, S9 |
| Fig. S9 | Cooperation under low information costs (snowdrift; one-pop + strips) | Fig. 1; Results §1–2 |
| Fig. S10 | Fitness under low information costs (snowdrift; one-pop + strips) | Figs. S7, S9 |
| Fig. S11 | Cooperation under asymmetric cooperation costs (PD) | Fig. 1 |
| Fig. S12 | Fitness under asymmetric cooperation costs (PD) | Fig. 1 |
| Fig. S13 | Cooperation under asymmetric cooperation costs (snowdrift) | Fig. 1 |
| Fig. S14 | Fitness under asymmetric cooperation costs (snowdrift) | Fig. 1 |
| Fig. S15 | Cooperation under asymmetric information costs (PD) | Fig. 2 |
| Fig. S16 | Fitness under asymmetric information costs (PD) | Fig. 2 |
| Fig. S17 | Cooperation under asymmetric information costs (snowdrift) | Fig. 2 |
| Fig. S18 | Fitness under asymmetric information costs (snowdrift) | Fig. 2 |
| Fig. S19 | Cooperation under asymmetric cooperation costs and varying information costs (PD) | Results §5 |
| Fig. S20 | Fitness under asymmetric cooperation costs and varying information costs (PD) | Results §5 |
| Fig. S21 | Cooperation under asymmetric cooperation costs and varying information costs (snowdrift) | Results §5 |
| Fig. S22 | Fitness under asymmetric cooperation costs and varying information costs (snowdrift) | Results §5 |
| Fig. S23 | Cooperation under asymmetric cooperation and information costs (PD) | Fig. 3 |
| Fig. S24 | Fitness under asymmetric cooperation and information costs (PD) | Fig. 3 |
| Fig. S25 | Cooperation under asymmetric cooperation and information costs (snowdrift) | Fig. 3 |
| Fig. S26 | Fitness under asymmetric cooperation and information costs (snowdrift) | Fig. S25 |
| Fig. S27 | Cooperation and fitness under asymmetric cooperation costs in two populations (PD) | Fig. 3 |
| Fig. S28 | Cooperation and fitness under asymmetric cooperation costs in two populations (snowdrift) | Fig. S25 |
| Fig. S29 | Cooperation under asymmetric cooperation and information costs at group size 4 (PD) | Fig. 3 |
| Fig. S30 | Cooperation under asymmetric cooperation and information costs at group size 4 (snowdrift) | Fig. S25 |
| Table S1 | Payoff-difference attribution by mechanism family | Results §1 |

Captions for Figs. S1–S30 are in [captions.md](captions.md) (regenerated from the
graphgen interpretation study). PD and snowdrift never share a figure. Main-text
Figs. 1–3 use four columns (—|P|M|IMP); every supplement figure uses five
(—|P|M|IMP|IJMPQ). Two-population heatmaps use the Fig. 3 row template
(cheap/expensive/difference or low-i/high-i/difference), with cooperation and fitness as
separate figures. Shuffle
short-memory branches (M collapse; IM and partner-choice combinations sustain; P
nearly unchanged) are discussed in Results §1 without a dedicated figure.
The dilemma-0 machinery-erosion control remains internal (`aux_m_nodilemma`) and is
not a manuscript figure.

## Table S1. Payoff-difference attribution

A single cooperation-cost axis joins temptation (T − R), risk (P − S), and the
cooperation advantage (R − P) together. Orthogonal payoff-plane calibration sweeps
(prisoner's dilemma: R and P varied at fixed T, S; snowdrift: R and S varied at
fixed T, P) separate these differences. The sweeps are auxiliary and are not published as
figures; the attributions they support are:

| Mechanism family | Limiting payoff difference | Evidence |
| ---------------- | ------------------- | -------- |
| Direct reciprocity (M) | Risk / mutual-defection payoff P | PD calibration; snowdrift confirms low-risk rescue of M |
| Partner choice (P) | Cooperation advantage R − P | PD calibration; cooperation falls as R − P → 0 |
| Combined (MP, MPQ, IMP, IJMPQ) | Reward / mutual-cooperation payoff R | PD calibration; unaffected by the defection baseline |

Journal sources: [synthesis](../journal/synthesis.md),
[PD calibration](../journal/prisoners_calibration.md),
[snowdrift calibration](../journal/snowdrift_calibration.md).

## Cross-references from the main text

**Figs. S1–S2 i × c in one population.** Cooperation and fitness across the
information-cost × cooperation-cost triangle (PD and snowdrift). Low-i line ceilings
are the top row of Figs. S7–S10.

**Fig. 1 asymmetric cooperation costs.** Fitness counterpart: Fig. S12. Snowdrift: Figs. S13–S14.
Five-column twin (adds IJMPQ): Fig. S11. Cooperation-cost strips (one-pop + matched/asymmetric):
Figs. S7, S9 (fitness S8, S10). Group-size-4 counterparts of Figs. 3 and S25:
Figs. S29–S30 (cooperation only).

**Figs. S3–S6 symmetric information cost.** i × c surfaces in two populations
(3×5; higher-/lower-coop / difference rows; —|P|M|IMP|IJMPQ columns; PD and snowdrift;
cooperation S3/S5, fitness S4/S6).

**Fig. 2 symmetric-c i asymmetry.** No enforcement, P, M, and IJMPQ with low-i /
high-i / difference rows (prisoner's dilemma). Fitness: Fig. S16. Snowdrift: Figs. S17–S18.
Five-column twin (adds IJMPQ): Fig. S15.

**Figs. S19–S22 shared-i under asymmetric cooperation costs.** Results §5 bridge between
symmetric-c i asymmetry and the crossed plane.

**Fig. 3 and S25 i₀ × i₁ plane.** No enforcement, P, M, and IJMPQ with cheap /
expensive / difference rows (prisoner's dilemma Fig. 3; snowdrift twin Fig. S25). Fitness
counterparts: Figs. S24 and S26. Fixed-total line cuts (coop + fitness): Fig. S27
(snowdrift Fig. S28). gs = 4: Figs. S29–S30. Five-column twin (adds IJMPQ): Fig. S23.

## What is intentionally not in the supplement figures

- Payoff-plane calibration heatmaps — attributions only, via Table S1.
- Dilemma-0 machinery-erosion control (`aux_m_nodilemma`) — internal only.
- Dedicated shuffle-branch panels — claim kept in Results prose.
- Cooperation-cost strips (with one-pop ceilings) live in the supplement (Figs. S7, S9), not the main text.
- Former c = 0 behaviour–mechanism decoupling panels — claim kept in Results §3 prose.
- Former P+IJMPQ-only spanning coop+fitness grids — replaced by Fig. 3-style planes
  with separate cooperation and fitness figures.
