# Supplement

Companion to the main text. Figure captions and PNG provenance:
[captions.md](captions.md), [figures.md](figures.md). Payoff equations and
constants: [parameterization](../journal/parameterization.md). Headline numbers
are regression-checked by `ai/verify_claims.py`.

## Contents

| Item | Role | Main-text anchor |
| ---- | ---- | ---------------- |
| Fig. S1 | Cooperation-cost ceilings by mechanism (one population; PD) | Results §1 |
| Fig. S2 | Cooperation-cost ceilings by mechanism (one population; snowdrift) | Results §1 |
| Fig. S3 | Short-memory / shuffle reciprocity branches (PD) | Fig. S1 |
| Fig. S4 | Short-memory / shuffle reciprocity branches (snowdrift) | Fig. S2 |
| Fig. S5 | Fitness counterpart of Fig. 1 (PD; matched vs gap strips) | Figs. 1–2 |
| Fig. S6 | Fitness counterpart of Fig. 2 (snowdrift) | Figs. 1–2 |
| Fig. S7 | Full c₀ × c₁ cooperation-cost grid (PD) | Fig. 1 |
| Fig. S8 | Full c₀ × c₁ cooperation-cost grid (snowdrift) | Fig. 2 |
| Fig. S9 | Cooperation-cost asymmetry at group size 4 (PD) | Fig. 1 |
| Fig. S10 | Cooperation-cost asymmetry at group size 4 (snowdrift) | Fig. 2 |
| Fig. S11 | Behaviour–mechanism decoupling at c = 0 (PD) | Results §3 |
| Fig. S12 | Behaviour–mechanism decoupling at c = 0 (snowdrift) | Fig. S11 |
| Fig. S13 | Information cost × cooperation cost (single population; PD) | Fig. S11 |
| Fig. S14 | Information cost × cooperation cost (single population; snowdrift) | Fig. S12 |
| Fig. S15 | Information cost under fixed cooperation-cost asymmetry (PD) | Figs. 3–4 |
| Fig. S16 | Information cost under fixed cooperation-cost asymmetry (snowdrift) | Figs. 3–4 |
| Fig. S17 | Fitness counterpart of Fig. 3 (relational slices; PD) | Fig. 3 |
| Fig. S18 | Fitness counterpart of Fig. S22 (relational slices; snowdrift) | Fig. 3 |
| Fig. S19 | Information-cost asymmetry at equal cooperation cost (PD) | Figs. 3–4 |
| Fig. S20 | Information-cost asymmetry at equal cooperation cost (snowdrift) | Figs. 3–4 |
| Fig. S21 | Full i₀ × i₁ grid under a cooperation-cost gap (PD) | Figs. 3–4, S17 |
| Fig. S22 | Snowdrift twin of Fig. 3 (relational strips) | Fig. 3 |
| Fig. S23 | Snowdrift twin of Fig. 4 (near-zero-i₀ wedge) | Fig. 4 |
| Table S1 | Payoff-gap attribution by mechanism family | Results §1 |

Captions for Figs. S1–S23 are in [captions.md](captions.md) (regenerated from the
graphgen interpretation study). PD and snowdrift never share a figure. There is no
snowdrift twin of Fig. S21 (the crossed i₀ × i₁ square under a cooperation-cost
gap). The dilemma-0 machinery-erosion control remains internal (`aux_m_nodilemma`)
and is not a manuscript figure.

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

**Figs. S1–S4 cost thresholds.** One-population PD ceilings (S1) and snowdrift (S2);
shuffle short-memory variants (S3–S4).

**Figs. 1–2 role split.** Matched-cost and c₁ = c₀ + 0.02 strips share axes within
each dilemma. Fitness counterparts: Figs. S5–S6. Full c₀ × c₁ coverage: Figs. S7–S8.
Small-group robustness (groups of 4): Figs. S9–S10.

**Fig. S11: cooperation after allele loss.** Full information-cost × cooperation-cost
surfaces: Figs. S13–S14. Snowdrift c = 0 slice: Fig. S12.

**Figs. 3–4 relational cost.** Equal-c information-cost asymmetry and role inversion:
Fig. S19 (snowdrift Fig. S20). Shared-i under a cooperation-cost gap: Fig. S15
(snowdrift Fig. S16). Fitness on the Fig. 3 relational slices: Fig. S17 (snowdrift
Fig. S18). Full i₀ × i₁ square behind the line reslices: Fig. S21. Snowdrift
relational strips and wedge: Figs. S22–S23.

## What is intentionally not in the supplement figures

- Payoff-plane calibration heatmaps — attributions only, via Table S1.
- Dilemma-0 machinery-erosion control (`aux_m_nodilemma`) — internal only.
- Snowdrift twin of Fig. S21 — under snowdrift the c-gap dominates the square;
  Figs. S22–S23 already show that the PD-specific relational structure is gone.
- Old sym-vs-asym contrast strip (former Fig. S5) — absorbed into Figs. 1–2.
