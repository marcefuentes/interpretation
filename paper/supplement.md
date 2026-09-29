# Supplement

Companion to the main text. Figure captions and PNG provenance:
[captions.md](captions.md), [figures.md](figures.md). Payoff equations and
constants: [parameterization](../journal/parameterization.md). Headline numbers
are regression-checked by `ai/verify_claims.py`.

## Contents

| Item | Role | Main-text anchor |
| ---- | ---- | ---------------- |
| Fig. S1 | Cooperation-cost thresholds by mechanism at equal c (one and two populations; PD + snowdrift) | Results §1–2 |
| Fig. S2 | Short-memory / shuffle reciprocity branches (PD + snowdrift) | Fig. S1 |
| Fig. S3 | No-enforcement control under cooperation-cost asymmetry (PD) | Fig. 2 |
| Fig. S4 | Full c₀ × c₁ cooperation-cost grid (PD) | Fig. 2 |
| Fig. S5 | Parameter-symmetric vs asymmetric line slices (PD) | Figs. 1–2 |
| Fig. S6 | Cooperation-cost asymmetry at group size 4 (PD) | Fig. 2 |
| Fig. S7 | Information cost × cooperation cost (single population; PD + snowdrift) | Fig. 3 |
| Fig. S8 | Information cost under fixed cooperation-cost asymmetry (PD) | Figs. 4–5 |
| Fig. S9 | Fitness counterpart of Fig. 4 (relational slices; PD) | Fig. 4 |
| Fig. S10 | Information-cost asymmetry at equal cooperation cost (PD) | Figs. 4–5 |
| Fig. S11 | Snowdrift twin of Fig. 2 | Fig. 2 |
| Fig. S12 | Snowdrift twin of Fig. S3 | Fig. 2 |
| Fig. S13 | Snowdrift twin of Fig. S4 | Fig. 2 |
| Fig. S14 | Snowdrift twin of Fig. S5 | Figs. 1–2 |
| Fig. S15 | Snowdrift twin of Fig. S6 | Fig. 2 |
| Fig. S16 | Snowdrift twin of Fig. S8 | Figs. 4–5 |
| Fig. S17 | Snowdrift twin of Fig. 4 | Fig. 4 |
| Fig. S18 | Snowdrift twin of Fig. 5 | Fig. 5 |
| Fig. S19 | Snowdrift twin of Fig. S9 | Fig. 4 |
| Fig. S20 | Snowdrift twin of Fig. S10 | Figs. 4–5 |
| Fig. S21 | Snowdrift twin of Fig. 3 | Fig. 3 |
| Table S1 | Payoff-gap attribution by mechanism family | Results §1 |

Captions for Figs. S1–S21 are in [captions.md](captions.md) (regenerated from the
graphgen interpretation study). Figs. S11–S21 reuse the same layout and parameter
cuts as their PD counterparts at dilemma type 2. The dilemma-0 machinery-erosion
control remains internal (`aux_m_nodilemma`) and is not a manuscript figure.

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

**Fig. S1 cost thresholds.** One-population rows (a–h) carry the mechanism ordering of
Results §1 under both games; two-population rows (i–p) add the matched-cost role-split
claims of Results §2. Shuffle short-memory variants: Fig. S2.

**Figs. 1–2 role split.** No-enforcement asymmetric control: Fig. S3 (snowdrift
Fig. S12). Deterministic versus stochastic strips on shared axes: Fig. S5
(snowdrift Fig. S14). Full c₀ × c₁ coverage: Fig. S4 (snowdrift Fig. S13).
Small-group robustness (groups of 4): Fig. S6 (snowdrift Fig. S15). Asymmetric
snowdrift strip matching Fig. 2: Fig. S11.

**Fig. 3: cooperation after allele loss.** Full information-cost × cooperation-cost
surface: Fig. S7. Snowdrift c = 0 slice: Fig. S21.

**Figs. 4–5 relational cost.** Equal-c information-cost asymmetry and role inversion:
Fig. S10 (snowdrift Fig. S20). Shared-i under a cooperation-cost gap: Fig. S8
(snowdrift Fig. S16). Fitness on the Fig. 4 relational slices: Fig. S9 (snowdrift
Fig. S19). Snowdrift relational strips and wedge: Figs. S17–S18. The full i₀ × i₁
square behind the line reslices remains journal-backed
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

## What is intentionally not in the supplement figures

- Payoff-plane calibration heatmaps — attributions only, via Table S1.
- Dilemma-0 machinery-erosion control (`aux_m_nodilemma`) — internal only.
