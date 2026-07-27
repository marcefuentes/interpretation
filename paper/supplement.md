# Supplement

Companion to the main text. Figure captions and PNG provenance:
[captions.md](captions.md), [figures.md](figures.md). Payoff equations and
constants: [parameterization](../journal/parameterization.md). Headline numbers
are regression-checked by `ai/verify_claims.py`.

## Contents

| Item | Role | Main-text anchor |
| ---- | ---- | ---------------- |
| Fig. S1 | No-enforcement control under cooperation-cost asymmetry | Fig. 2 |
| Fig. S2 | Short-memory / shuffle reciprocity branches | Fig. S10 |
| Fig. S3 | Cooperation-cost asymmetry at group size 4 | Fig. 2 |
| Fig. S4 | Dilemma-0 control for machinery erosion | Fig. 3 |
| Fig. S5 | Parameter-symmetric vs asymmetric line slices | Figs. 1–2 |
| Fig. S6 | Information-cost asymmetry at equal cooperation cost | Figs. 4–5 |
| Fig. S7 | Information cost × cooperation cost (single population) | Fig. 3 |
| Fig. S8 | Information cost under fixed cooperation-cost asymmetry | Figs. 4–5 |
| Fig. S9 | Full c₀ × c₁ cooperation-cost grid | Fig. 2 |
| Fig. S10 | Mechanism hierarchy at equal cooperation cost | Results §1 |
| Table S1 | Payoff-gap attribution by mechanism family | Results §1 |

Captions for Figs. S1–S10 are in [captions.md](captions.md) (regenerated from the
graphgen interpretation study). The panels below are not republished as main-text
figures; they are coverage and robustness evidence for claims stated in the
Results.

## Table S1. Payoff-gap attribution

A single cooperation-cost axis welds temptation (T − R), risk (P − S), and the
cooperation advantage (R − P) together. Orthogonal payoff-plane calibration sweeps
(prisoner's dilemma: R and P varied at fixed T, S; snowdrift: R and S varied at
fixed T, P) decouple these gaps. The sweeps are auxiliary and are not published as
figures; the attributions they support are:

| Mechanism family | Limiting payoff gap | Evidence |
| ---------------- | ------------------- | -------- |
| Direct reciprocity (M) | Risk / mutual-defection payoff P | PD calibration; snowdrift confirms low-risk rescue of M |
| Partner choice (P) | Cooperation advantage R − P | PD calibration; collapse as R − P → 0 |
| Combined / reputation-rich (MP, MPQ, IMP, IJMPQ) | Reward / mutual-cooperation payoff R | PD calibration; largely blind to the defection baseline |

Journal sources: [synthesis](../journal/synthesis.md),
[PD calibration](../journal/prisoners_calibration.md),
[snowdrift calibration](../journal/snowdrift_calibration.md).

## Cross-references from the main text

**Fig. S10 hierarchy.** Shuffle short-memory variants that can shift the
direct-reciprocity collapse ordering: Fig. S2.

**Figs. 1–2 role split.** No-enforcement asymmetric control: Fig. S1. Deterministic
versus stochastic strips on shared axes: Fig. S5. Full c₀ × c₁ coverage: Fig. S9.
Small-group robustness (gs = 4): Fig. S3.

**Fig. 3 decoupling.** Full Cost × c surface: Fig. S7. Dilemma-0 control (machinery
erodes with or without a dilemma; cooperation persists through the shed only with a
dilemma): Fig. S4. Compression when cooperation cost is held above zero: Fig. S8.

**Figs. 4–5 relational cost.** Equal-c information-cost asymmetry and hitchhiking
(stronger inversion than under a cooperation-cost gap): Fig. S6. The full i₀ × i₁
square behind the line reslices remains journal-backed
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)); snowdrift removal of the
wedge is reported in the main text and that journal entry.

## What is intentionally not in the supplement figures

- Payoff-plane calibration heatmaps (cal1, cal2) — attributions only, via Table S1.
- Evolving-versus-fixed (pop₃) panels — redundant with the equal-cost baseline
  ([framework](../journal/framework.md)).
