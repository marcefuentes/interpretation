# Supplement

Companion to the main text. Figure captions and PNG provenance:
[captions.md](captions.md), [figures.md](figures.md). Payoff equations and
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
| Fig. S7 | Cooperation-cost asymmetry at group size 4 (PD) | Fig. 1 |
| Fig. S8 | Cooperation-cost asymmetry at group size 4 (snowdrift) | Fig. 2 |
| Fig. S9 | Behaviour–mechanism decoupling at c = 0 (PD) | Results §3 |
| Fig. S10 | Behaviour–mechanism decoupling at c = 0 (snowdrift) | Fig. S9 |
| Fig. S11 | Information cost × cooperation cost (single population; PD) | Fig. S9 |
| Fig. S12 | Information cost × cooperation cost (single population; snowdrift) | Fig. S10 |
| Fig. S13 | Information cost under fixed cooperation-cost asymmetry (PD) | Figs. 3–4 |
| Fig. S14 | Information cost under fixed cooperation-cost asymmetry (snowdrift) | Figs. 3–4 |
| Fig. S15 | Fitness counterpart of Fig. 3 (PD) | Fig. 3 |
| Fig. S16 | Fitness counterpart of Fig. S20 (snowdrift) | Fig. 3 |
| Fig. S17 | Information-cost asymmetry at equal cooperation cost (PD) | Figs. 3–4 |
| Fig. S18 | Information-cost asymmetry at equal cooperation cost (snowdrift) | Figs. 3–4 |
| Fig. S19 | Full i₀ × i₁ grid under a cooperation-cost gap (PD) | Figs. 3–4, S15 |
| Fig. S20 | Snowdrift twin of Fig. 3 (who pays) | Fig. 3 |
| Fig. S21 | Snowdrift twin of Fig. 4 (near-zero-i₀ wedge) | Fig. 4 |
| Table S1 | Payoff-gap attribution by mechanism family | Results §1 |

Captions for Figs. S1–S21 are in [captions.md](captions.md) (regenerated from the
graphgen interpretation study). PD and snowdrift never share a figure. There is no
snowdrift twin of Fig. S19 (the crossed i₀ × i₁ square under a cooperation-cost
gap). Shuffle short-memory branches (M collapse; IM and partner-choice combinations
sustain; P nearly unchanged) are discussed in Results §1 without a dedicated figure.
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

**Fig. S9: cooperation after allele loss.** Full information-cost × cooperation-cost
surfaces: Figs. S11–S12. Snowdrift c = 0 slice: Fig. S10.

**Figs. 3–4 who-pays designs.** Equal-c information-cost asymmetry and role inversion:
Fig. S17 (snowdrift Fig. S18). Shared-i under a cooperation-cost gap: Fig. S13
(snowdrift Fig. S14). Fitness on the Fig. 3 slices: Fig. S15 (snowdrift
Fig. S16). Full i₀ × i₁ square behind the line reslices: Fig. S19. Snowdrift
who-pays strips and wedge: Figs. S20–S21.

## What is intentionally not in the supplement figures

- Payoff-plane calibration heatmaps — attributions only, via Table S1.
- Dilemma-0 machinery-erosion control (`aux_m_nodilemma`) — internal only.
- Snowdrift twin of Fig. S19 — under snowdrift the c-gap dominates the square;
  Figs. S20–S21 already show that the PD-specific who-pays structure is gone.
- Dedicated shuffle-branch panels (former S3–S4) — claim kept in Results prose.
- Old sym-vs-asym contrast strip — absorbed into Figs. 1–2.
