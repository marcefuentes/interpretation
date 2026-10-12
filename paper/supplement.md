# Supplement

Companion to the main text. Supplement figure captions:
[captions.md](captions.md). PNG provenance: [figures.md](figures.md). Payoff equations and
constants: [parameterization](../journal/parameterization.md). Headline numbers
are regression-checked by `ai/verify_claims.py`.

## Contents

| Item | Role | Main-text anchor |
| ---- | ---- | ---------------- |
| Fig. S1 | Cooperation in a single population (prisoner's dilemma) | Results §1 |
| Fig. S2 | Cooperation in a single population (snowdrift) | Results §1 |
| Fig. S3 | Fitness counterpart of Fig. 1 (PD; matched vs gap strips) | Figs. 1–2 |
| Fig. S4 | Fitness counterpart of Fig. 2 (snowdrift) | Figs. 1–2 |
| Fig. S5 | Full c₀ × c₁ cooperation grid (PD; coop + gap) | Fig. 1 |
| Fig. S6 | Full c₀ × c₁ cooperation grid (PD; fitness + gap) | Fig. 1 |
| Fig. S7 | Full c₀ × c₁ cooperation grid (snowdrift; coop + gap) | Fig. 2 |
| Fig. S8 | Full c₀ × c₁ cooperation grid (snowdrift; fitness + gap) | Fig. 2 |
| Fig. S9 | Group-size-4 counterpart of Fig. 1 (PD; coop) | Fig. 1 |
| Fig. S10 | Group-size-4 counterpart of Fig. 2 (snowdrift; coop) | Fig. 2 |
| Fig. S11 | Information cost × cooperation cost (single population; PD) | Results §3 |
| Fig. S12 | Information cost × cooperation cost (single population; snowdrift) | Results §3 |
| Fig. S13 | Fitness under equal-c i asymmetry (PD) | Fig. 3 |
| Fig. S14 | Equal-c i asymmetry (snowdrift; coop + gap) | Fig. 3 |
| Fig. S15 | Fitness under equal-c i asymmetry (snowdrift) | Fig. 3 |
| Fig. S16 | Shared i under fixed c-gap (PD; coop + gap) | Results §5 |
| Fig. S17 | Shared i under fixed c-gap (PD; fitness + gap) | Results §5 |
| Fig. S18 | Shared i under fixed c-gap (snowdrift; coop + gap) | Results §5 |
| Fig. S19 | Shared i under fixed c-gap (snowdrift; fitness + gap) | Results §5 |
| Fig. S20 | Fitness counterpart of Fig. 4 (i₀ × i₁ plane; prisoner's dilemma) | Fig. 4 |
| Fig. S21 | Information-cost plane under a cooperation-cost gap (snowdrift) | Fig. 4 |
| Fig. S22 | Fitness counterpart of Fig. S21 (i₀ × i₁ plane; snowdrift) | Fig. S21 |
| Fig. S23 | Fixed-total cut (PD; coop + fitness × —|P|M|IJMPQ) | Fig. 4 |
| Fig. S24 | Fixed-total cut (snowdrift) | Fig. S21 |
| Fig. S25 | Group-size-4 counterpart of Fig. 4 (PD; i₀ × i₁ plane) | Fig. 4 |
| Fig. S26 | Group-size-4 counterpart of Fig. S21 (snowdrift; i₀ × i₁ plane) | Fig. S21 |
| Table S1 | Payoff-gap attribution by mechanism family | Results §1 |

Captions for Figs. S1–S26 are in [captions.md](captions.md) (regenerated from the
graphgen interpretation study). PD and snowdrift never share a figure. Two-population
heatmaps use the Fig. 4 template (rows cheap/expensive/gap or low-i/high-i/gap;
columns —|P|M|IJMPQ), with cooperation and fitness as separate figures. Shuffle
short-memory branches (M collapse; IM and partner-choice combinations sustain; P
nearly unchanged) are discussed in Results §1 without a dedicated figure.
The dilemma-0 machinery-erosion control remains internal (`aux_m_nodilemma`) and is
not a manuscript figure.

## Table S1. Payoff-gap attribution

A single cooperation-cost axis joins temptation (T − R), risk (P − S), and the
cooperation advantage (R − P) together. Orthogonal payoff-plane calibration sweeps
(prisoner's dilemma: R and P varied at fixed T, S; snowdrift: R and S varied at
fixed T, P) separate these gaps. The sweeps are auxiliary and are not published as
figures; the attributions they support are:

| Mechanism family | Limiting payoff gap | Evidence |
| ---------------- | ------------------- | -------- |
| Direct reciprocity (M) | Risk / mutual-defection payoff P | PD calibration; snowdrift confirms low-risk rescue of M |
| Partner choice (P) | Cooperation advantage R − P | PD calibration; cooperation falls as R − P → 0 |
| Combined (MP, MPQ, IMP, IJMPQ) | Reward / mutual-cooperation payoff R | PD calibration; unaffected by the defection baseline |

Journal sources: [synthesis](../journal/synthesis.md),
[PD calibration](../journal/prisoners_calibration.md),
[snowdrift calibration](../journal/snowdrift_calibration.md).

## Cross-references from the main text

**Figs. S1–S2 cost thresholds.** One-population PD ceilings with fitness (S1) and
snowdrift (S2).

**Figs. 1–2 role split.** Fitness counterparts: Figs. S3–S4. Full c₀ × c₁ coverage:
Figs. S5–S8 (PD coop/fitness, snowdrift coop/fitness). Group-size-4 counterparts
of Figs. 1–2, 4 and S21: Figs. S9–S10 and S25–S26 (cooperation only).

**Figs. S11–S12 matched information cost.** Cost × c surfaces (2×4; coop/fitness
rows; —|P|M|IJMPQ columns; PD and snowdrift).

**Fig. 3 equal-c i asymmetry.** No enforcement, P, M, and IJMPQ with low-i /
high-i / gap rows (prisoner's dilemma). Fitness: Fig. S13. Snowdrift: Figs. S14–S15.

**Figs. S16–S19 shared-i under a cooperation-cost gap.** Results §5 bridge between
equal-c i asymmetry and the crossed plane.

**Fig. 4 and S21 i₀ × i₁ plane.** No enforcement, P, M, and IJMPQ with cheap /
expensive / gap rows (prisoner's dilemma Fig. 4; snowdrift twin Fig. S21). Fitness
counterparts: Figs. S20 and S22. Fixed-total line cuts (coop + fitness): Fig. S23
(snowdrift Fig. S24). gs = 4: Figs. S25–S26.

## What is intentionally not in the supplement figures

- Payoff-plane calibration heatmaps — attributions only, via Table S1.
- Dilemma-0 machinery-erosion control (`aux_m_nodilemma`) — internal only.
- Dedicated shuffle-branch panels (former S3–S4) — claim kept in Results prose.
- Old sym-vs-asym contrast strip — absorbed into Figs. 1–2.
- Former c = 0 behaviour–mechanism decoupling panels — claim kept in Results §3 prose.
- Former P+IJMPQ-only spanning coop+fitness grids — replaced by Fig. 4-style planes
  with separate cooperation and fitness figures.
