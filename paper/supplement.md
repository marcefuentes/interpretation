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
| Fig. S3 | Matched vs gap cooperation-cost strips (PD; coop) | Fig. 1; Results §2 |
| Fig. S4 | Matched vs gap cooperation-cost strips (snowdrift; coop) | Fig. 1; Results §2 |
| Fig. S5 | Fitness counterpart of Fig. S3 (PD) | Figs. S3–S4 |
| Fig. S6 | Fitness counterpart of Fig. S4 (snowdrift) | Figs. S3–S4 |
| Fig. S7 | Full c₀ × c₁ cooperation grid (PD; fitness + gap) | Fig. 1 |
| Fig. S8 | Full c₀ × c₁ cooperation grid (snowdrift; coop + gap) | Fig. 1 |
| Fig. S9 | Full c₀ × c₁ cooperation grid (snowdrift; fitness + gap) | Fig. 1 |
| Fig. S10 | Group-size-4 counterpart of Fig. S3 (PD; coop) | Fig. S3 |
| Fig. S11 | Group-size-4 counterpart of Fig. S4 (snowdrift; coop) | Fig. S4 |
| Fig. S12 | Information cost × cooperation cost (two populations; PD) | Results §3 |
| Fig. S13 | Information cost × cooperation cost (two populations; snowdrift) | Results §3 |
| Fig. S14 | Fitness under equal-c i asymmetry (PD) | Fig. 2 |
| Fig. S15 | Equal-c i asymmetry (snowdrift; coop + gap) | Fig. 2 |
| Fig. S16 | Fitness under equal-c i asymmetry (snowdrift) | Fig. 2 |
| Fig. S17 | Shared i under fixed c-gap (PD; coop + gap) | Results §5 |
| Fig. S18 | Shared i under fixed c-gap (PD; fitness + gap) | Results §5 |
| Fig. S19 | Shared i under fixed c-gap (snowdrift; coop + gap) | Results §5 |
| Fig. S20 | Shared i under fixed c-gap (snowdrift; fitness + gap) | Results §5 |
| Fig. S21 | Fitness counterpart of Fig. 3 (i₀ × i₁ plane; prisoner's dilemma) | Fig. 3 |
| Fig. S22 | Information-cost plane under a cooperation-cost gap (snowdrift) | Fig. 3 |
| Fig. S23 | Fitness counterpart of Fig. S22 (i₀ × i₁ plane; snowdrift) | Fig. S22 |
| Fig. S24 | Fixed-total cut (PD; coop + fitness × —|P|M|IMP|IJMPQ) | Fig. 3 |
| Fig. S25 | Fixed-total cut (snowdrift) | Fig. S22 |
| Fig. S26 | Group-size-4 counterpart of Fig. 3 (PD; i₀ × i₁ plane) | Fig. 3 |
| Fig. S27 | Group-size-4 counterpart of Fig. S22 (snowdrift; i₀ × i₁ plane) | Fig. S22 |
| Fig. S28 | Five-column version of Fig. 1 (adds IJMPQ) | Fig. 1 |
| Fig. S29 | Five-column version of Fig. 2 (adds IJMPQ) | Fig. 2 |
| Fig. S30 | Five-column version of Fig. 3 (adds IJMPQ) | Fig. 3 |
| Table S1 | Payoff-gap attribution by mechanism family | Results §1 |

Captions for Figs. S1–S30 are in [captions.md](captions.md) (regenerated from the
graphgen interpretation study). PD and snowdrift never share a figure. Main-text
Figs. 1–3 use four columns (—|P|M|IMP); every supplement figure uses five
(—|P|M|IMP|IJMPQ). Two-population heatmaps use the Fig. 3 row template
(cheap/expensive/gap or low-i/high-i/gap), with cooperation and fitness as
separate figures. Shuffle
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

**Fig. 1 full c₀ × c₁ grid.** Fitness counterpart: Fig. S7. Snowdrift: Figs. S8–S9.
Matched and gap strips (former main-text Figs. 1–2): Figs. S3–S4 (fitness S5–S6).
Group-size-4 counterparts of Figs. S3–S4, 3 and S22: Figs. S10–S11 and S26–S27
(cooperation only).

**Figs. S12–S13 matched information cost.** Cost × c surfaces in two populations
(3×5; higher-/lower-coop / gap rows; —|P|M|IMP|IJMPQ columns; cooperation only; PD and
snowdrift).

**Fig. 2 equal-c i asymmetry.** No enforcement, P, M, and IJMPQ with low-i /
high-i / gap rows (prisoner's dilemma). Fitness: Fig. S14. Snowdrift: Figs. S15–S16.

**Figs. S17–S20 shared-i under a cooperation-cost gap.** Results §5 bridge between
equal-c i asymmetry and the crossed plane.

**Fig. 3 and S22 i₀ × i₁ plane.** No enforcement, P, M, and IJMPQ with cheap /
expensive / gap rows (prisoner's dilemma Fig. 3; snowdrift twin Fig. S22). Fitness
counterparts: Figs. S21 and S23. Fixed-total line cuts (coop + fitness): Fig. S24
(snowdrift Fig. S25). gs = 4: Figs. S26–S27.

## What is intentionally not in the supplement figures

- Payoff-plane calibration heatmaps — attributions only, via Table S1.
- Dilemma-0 machinery-erosion control (`aux_m_nodilemma`) — internal only.
- Dedicated shuffle-branch panels — claim kept in Results prose.
- Matched vs gap strips live in the supplement (Figs. S3–S4), not the main text.
- Former c = 0 behaviour–mechanism decoupling panels — claim kept in Results §3 prose.
- Former P+IJMPQ-only spanning coop+fitness grids — replaced by Fig. 3-style planes
  with separate cooperation and fitness figures.
