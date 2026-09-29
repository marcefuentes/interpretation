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
| Fig. S11 | Full i₀ × i₁ grid under a cooperation-cost gap (PD) | Figs. 4–5, S9 |
| Table S1 | Payoff-gap attribution by mechanism family | Results §1 |

Captions for Figs. S1–S11 are in [captions.md](captions.md) (regenerated from the
graphgen interpretation study). The dilemma-0 machinery-erosion control remains
internal (`aux_m_nodilemma`) and is not a manuscript figure.

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

**Figs. 1–2 role split.** No-enforcement asymmetric control: Fig. S3.
Deterministic versus stochastic strips on shared axes: Fig. S5. Full c₀ × c₁
coverage: Fig. S4. Small-group robustness (groups of 4): Fig. S6.

**Fig. 3: cooperation after allele loss.** Full information-cost × cooperation-cost
surface: Fig. S7.

**Figs. 4–5 relational cost.** Equal-c information-cost asymmetry and role inversion:
Fig. S10. Shared-i under a cooperation-cost gap: Fig. S8. Fitness on the Fig. 4
relational slices: Fig. S9. Full i₀ × i₁ square behind the line reslices: Fig. S11.

## What is intentionally not in the supplement figures

- Payoff-plane calibration heatmaps — attributions only, via Table S1.
- Dilemma-0 machinery-erosion control (`aux_m_nodilemma`) — internal only.
