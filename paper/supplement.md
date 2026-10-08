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
| Fig. S5 | Full c₀ × c₁ cooperation-cost grid (PD) | Fig. 1 |
| Fig. S6 | Full c₀ × c₁ cooperation-cost grid (snowdrift) | Fig. 2 |
| Fig. S7 | Cooperation-cost asymmetry at group size 4 (prisoner's dilemma) | Fig. 1 |
| Fig. S8 | Cooperation-cost asymmetry at group size 4 (snowdrift) | Fig. 2 |
| Fig. S9 | Information cost × cooperation cost (single population; PD) | Results §3 |
| Fig. S10 | Information cost × cooperation cost (single population; snowdrift) | Results §3 |
| Fig. S11 | Information cost under fixed cooperation-cost asymmetry (prisoner's dilemma) | Figs. 3–4 |
| Fig. S12 | Information cost under fixed cooperation-cost asymmetry (snowdrift) | Figs. 3–4 |
| Fig. S13 | Fitness counterpart of Fig. 3 (prisoner's dilemma) | Fig. 3 |
| Fig. S14 | Fitness counterpart of Fig. 3 (snowdrift) | Fig. 3 |
| Fig. S15 | Full i₀ × i₁ grid under a cooperation-cost gap (prisoner's dilemma) | Figs. 3–4 |
| Fig. S16 | Full i₀ × i₁ grid under a cooperation-cost gap (snowdrift) | Figs. 3–4 |
| Fig. S17 | Who pays the information cost matters more than how much (snowdrift) | Fig. 3 |
| Fig. S18 | Information-cost asymmetry at equal cooperation cost (prisoner's dilemma) | Figs. 3–4 |
| Fig. S19 | Information-cost asymmetry at equal cooperation cost (snowdrift) | Figs. 3–4 |
| Fig. S20 | With reciprocity, the expensive population cooperates more only when the cheap one's information is nearly free (snowdrift) | Fig. 4 |
| Fig. S21 | Fitness counterpart of Fig. 4 (prisoner's dilemma) | Fig. 4 |
| Fig. S22 | Fitness counterpart of Fig. 4 (snowdrift) | Fig. 4 |
| Table S1 | Payoff-gap attribution by mechanism family | Results §1 |

Captions for Figs. S1–S22 are in [captions.md](captions.md) (regenerated from the
graphgen interpretation study). PD and snowdrift never share a figure. Shuffle
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
Figs. S5–S6. Small-group robustness (groups of 4): Figs. S7–S8.

**Figs. S9–S10 matched information cost.** Cost × c surfaces under IJMPQ (PD and
snowdrift).

**Figs. 3–4 who-pays designs.** Fitness on the Fig. 3 slices: Fig. S13 (snowdrift
Fig. S14). Full i₀ × i₁ square: Fig. S15 (snowdrift Fig. S16). Snowdrift twin of
Fig. 3: Fig. S17. Equal-c information-cost asymmetry: Fig. S18 (snowdrift Fig. S19).
Shared-i under a cooperation-cost gap: Fig. S11 (snowdrift Fig. S12). Snowdrift twin
of Fig. 4: Fig. S20. Fitness on the Fig. 4 wedge: Fig. S21 (snowdrift Fig. S22).

## What is intentionally not in the supplement figures

- Payoff-plane calibration heatmaps — attributions only, via Table S1.
- Dilemma-0 machinery-erosion control (`aux_m_nodilemma`) — internal only.
- Dedicated shuffle-branch panels (former S3–S4) — claim kept in Results prose.
- Old sym-vs-asym contrast strip — absorbed into Figs. 1–2.
- Former c = 0 behaviour–mechanism decoupling panels — claim kept in Results §3 prose.
