# Cross-Study Synthesis — The Payoff Axes Behind the Thresholds

Diagonal and mutualism show *that* each mechanism collapses as the cost c rises,
but their single cost axis cannot say *which* payoff gap drives the collapse.
The prisoners calibration (fixed T = 0.90, S = 0.10; R and P swept
independently) decouples the gaps and attributes each mechanism to one of them.
This document maps that attribution back onto the specific diagonal and
mutualism thresholds, consolidating the cross-checks otherwise scattered across
the per-study write-ups.

See **prisoners_calibration.md** for the payoff-axis fits, **symmetric_c.md** and
**asymmetric_c0_c1.md** for the threshold profiles, and **symmetric_c.md** for the 30-run
noise floor that bounds the comparisons below.

## The confound prisoners removes

In diagonal/mutualism the four payoffs are functions of one cost c
(T = K + b, R = K + b − c, P = K, S = K − c), which welds three gaps together:

- temptation T − R = c
- risk (sucker gap) P − S = c
- cooperation advantage R − P = b − c

A rising-c collapse is therefore simultaneously a rising-temptation,
rising-risk, and shrinking-cooperation-advantage event. Prisoners pins T and S
and varies R and P, so the marginal response −b/a (from qBSeen ≈ a·R + b·P)
separates them: −b/a > 1 is risk-led (P axis), ≈ 1 tracks R − P, < 1 is
reward-led (R axis).

## Master attribution

| Mechanism family | Prisoners −b/a | Limiting axis              | Diagonal / mutualism threshold it explains                    |
| ---------------- | -------------- | -------------------------- | ------------------------------------------------------------- |
| M                | 1.73           | risk / defection payoff P  | M's c-collapse is mostly rising risk, not a vanishing R − P    |
| P                | 0.89           | cooperation advantage R − P | the chooser bottleneck and the mutualism role split track R − P |
| MP, MPQ          | 0.56           | reward / temptation R      | reward-led only via M; shuffle reverts them to the P signature |
| IMP, IJMPQ       | 0.50–0.53      | reward / temptation R      | reputation removes M's risk sensitivity, extending coop to high c |
| IM (shuffle)     | 0.90           | cooperation advantage R − P | recent indirect reciprocity behaves like partner choice        |
| IJM (shuffle)    | 0.55           | reward / temptation R      | the lifetime signal J makes it reward-led                      |

## M is risk-limited (P axis)

Prisoners: M is roughly twice as sensitive to P as to R (−b/a = 1.73). Holding
R = 0.50 fixed and raising the mutual-defection payoff, M cooperation falls
0.86 (P = 0.14) → 0.47 (P = 0.46): TFT can only enforce cooperation when mutual
defection is cheap, because its punishment outcome *is* mutual defection.

This reinterprets two diagonal/mutualism results:

- **The diagonal c-collapse is largely a risk effect.** M noshuffle holds
  0.915 at c = 0.10 and 0.754 at c = 0.30, then collapses to 0.084 at c = 0.40.
  Diagonal cannot tell whether the collapse is the shrinking R − P or the
  growing risk P − S = c; prisoners attributes the bulk to risk.
- **Snowdrift confirms it from the other side.** In snowdrift S is high
  (S = K + b − c), so the sucker gap P − S is small — i.e. low risk. M then
  sustains cooperation where it cannot in PD: at gs = 4, c = 0.40, M reaches
  0.690 in snowdrift versus 0.017 in PD (**diagonal_reciprocity.md**). Low
  risk, not high reward, is what rescues M. The mutualism mirror is the
  snowdrift mimicry penalty (S > P makes mimicking a defector strictly costly,
  collapsing Pop_0 M1 to ≈ 0.033; **mutualism_reciprocity.md**).
- **Groupsize-invariant in both.** Prisoners M keeps −b/a = 1.73 → 1.72 from
  gs = 128 to gs = 4; diagonal M noshuffle is flat across groupsize (0.906 vs
  0.910 at c = 0.10). Stable pairings supply TFT history regardless of group
  size.

## P is cooperation-advantage-limited (R − P axis)

Prisoners: P cooperation is essentially a function of R − P alone (−b/a = 0.89;
cells with equal R − P but different absolute R, P give near-identical
cooperation). This is the unifying key for partner choice across both primary
studies:

- **Diagonal chooser bottleneck = R − P collapse.** Diagonal P (shuffle,
  gs = 128, pop_1) falls as R − P → 0: 0.864 at R − P = 0.10, 0.788 at 0.06,
  0.668 at 0.04, 0.056 at 0.00. Prisoners reproduces the same monotone-in-R − P
  curve from the orthogonal sweep, confirming R − P (not temptation or risk
  individually) sets the threshold.
- **Mutualism's deterministic role split is an R − P asymmetry.** Because
  c0 < c1 by construction, Pop_0 has the larger cooperation advantage
  (R − P = b − c0 > b − c1) and wins the chooser bottleneck in every cell:
  Pop_0 = 0.472 vs Pop_1 = 0.146 under P (asymmetry 0.325;
  **mutualism_partner_choice.md**). Partner choice converts the built-in R − P
  gap directly into a cooperation gap.
- **Shuffle-invariant, gs = 4-fragile** in prisoners (0.898 → 0.898 under
  shuffle; 0.898 → 0.075 at gs = 4), matching diagonal/mutualism: shuffle
  leaves P untouched while small groups starve the mutual C1P1 swap.

## Combined and reputation-rich mechanisms are reward-limited (R axis)

Prisoners: MP, MPQ, IMP, IJMPQ have −b/a ≈ 0.5 and corr(qB, P) ≈ 0 — almost
blind to the defection baseline P, responding chiefly to the reward R.
Reciprocity plus reputation strips out the risk sensitivity that limits M alone.

This explains why the combined mechanisms break the diagonal/mutualism ceilings
that bound M and P:

- **High-c persistence in diagonal.** At c = 0.40 (maximum risk and minimum
  R − P), IJMPQ holds 0.672 while P collapses to 0.022 and M to 0.084. Being
  reward-led, IJMPQ is largely indifferent to the rising risk that kills M and
  the shrinking R − P that kills P.
- **Pop_1 lift in mutualism.** Combined mechanisms raise the exploited
  high-cost population: IJMPQ Pop_1 = 0.573 (PD) and 0.609 (snowdrift) versus
  0.146 / 0.096 under P alone (**mutualism_combined.md**). Reward-led
  cooperation does not require Pop_1 to win an R − P contest it is structurally
  set up to lose.

## Two perturbations isolate the components

Shuffle subtracts the direct-reciprocity (M) component; gs = 4 subtracts the
partner-choice (P) component. The prisoners payoff-axis fit makes both
subtractions legible, and they are mirror images:

| Mechanism | noshuffle gs=128 −b/a | shuffle gs=128 −b/a | noshuffle gs=4 −b/a | Reads as            |
| --------- | --------------------- | ------------------- | ------------------- | ------------------- |
| MP        | 0.56                  | 0.89                | 1.62                | M off → P; P off → M |
| MPQ       | 0.56                  | 0.91                | 1.50                | M off → P; P off → M |
| IMP       | 0.50                  | 0.84                | 1.58                | M off → toward P; P off → M |
| IJMPQ     | 0.53                  | 0.52                | 0.43                | robust to both       |

The diagonal/mutualism shuffle and groupsize results are the same story at the
threshold level:

- **Shuffle removes M-dependent cooperation.** Diagonal M 0.915 → 0.053 at
  c = 0.10; mutualism MP reverts from 0.606 / 0.410 (Pop_0 / Pop_1) to the
  P-only baseline 0.474 / 0.148. Prisoners shows why: the M term simply drops
  out of the payoff-axis fit.
- **gs = 4 removes P-dependent cooperation.** Diagonal/mutualism P collapses in
  small groups, while MP / MPQ *recover* via their M component (e.g. diagonal
  MP 0.039 → 0.708 at c = 0.20), and pure reciprocity IJM becomes the best
  mechanism (0.923 at c = 0.20, gs = 4). Prisoners shows MP/MPQ snapping onto
  M's risk-led signature (−b/a → 1.5–1.6) under the same perturbation.
- **IJMPQ survives both** because its indirect (I) and lifetime (J, Q) loci are
  shuffle-invariant and circulate well in small closed groups — hence
  0.672 shuffle vs 0.382 noshuffle at c = 0.40 in diagonal, and the only
  mechanism reward-led in every prisoners condition.

## Symmetry breaking: two routes to the same role split

Both primary studies show a cooperator/defector role split with the cooperating
side earning less (the paradox of success), but they reach it differently, and
prisoners pins the difference to R − P:

- **Symmetric payoffs split stochastically.** Prisoners pop_2 (symmetric, like
  symmetric_c pop_2) breaks into a role split by chance, the cooperating side
  earning less (**prisoners_partner_choice.md**) — the same signature as
  symmetric_c pop_2.
- **Asymmetric payoffs split deterministically.** Mutualism pop_2 has a
  built-in R − P asymmetry (c0 < c1), so the lower-cost population always takes
  the cooperator role. Same outcome, but seeded by the payoff structure rather
  than by stochastic symmetry breaking. The combined mechanisms then suppress
  the split (IMP/IJMPQ asymmetry ≈ 0.16 vs 0.325 under P in PD) precisely
  because, being reward-led, they no longer route the R − P gap into a
  cooperation gap.

## The information-cost axis: price vs demand for enforcement

Prisoners/snowdrift decompose the payoff gaps behind the c-thresholds;
**symmetric_c_Cost** adds an orthogonal axis — the information cost Cost of carrying
the machinery, charged once per round for being a partner chooser (P/Q locus) and
once for being a reciprocator (M/I/J locus), independent of the game payoffs (see
**symmetric_c_Cost.md**). It reframes the whole picture as a supply-and-demand for
enforcement:

- **c is the demand.** Rising cooperation cost is rising temptation and risk —
  the pressure the machinery must resist.
- **Cost is the price.** Rising information cost is a per-round tax on the
  machinery itself, escapable only by shedding it.

The two are benign alone and destructive together:

- **Information cost is soft on its own** (c = 0): at Cost = 0.40 IJMPQ still
  holds 0.810, versus 0.378 at c = 0.40. With no temptation the population simply
  sheds the taxed machinery — the enforcement allele collapses (P1 0.67 to 0.02;
  M1 0.44 to 0.02 across the Cost sweep) while cooperation is carried by tax-free
  unconditional cooperators (C1P0, C1M0). **Behavior and mechanism decouple.**
- **Information cost lowers the c-ceiling.** Because it thins the very apparatus
  that resists temptation, adding Cost retreats the c-collapse threshold —
  IJMPQ's half-cooperation c-threshold falls 0.38 to 0.08 as Cost goes 0 to 0.20
  (roughly 1.5 units of tolerable c lost per unit Cost). This is not an
  equal-budget effect: at fixed Cost + c = 0.4 cooperation ranges 0.378 (all-c)
  to 0.810 (all-Cost); c is far more destructive per unit.
- **On the asymmetric branch there is no harmless Cost edge.** asymmetric_c1_Cost fixes
  c0 = 0.10 and sweeps Cost x c1, so even the cheap population always faces
  nonzero demand. The result is the complement of symmetric_c_Cost: Cost no longer
  erodes behavior softly, but immediately compresses the cooperator/exploiter split,
  retreats the c1 ceiling, and removes most of the behavior-mechanism decoupling
  that the symmetric c = 0 edge allowed.
- **The reward-led / assortment / risk attributions carry over.** Combined
  reputation-rich mechanisms are the most Cost-robust despite paying the double
  (two-family) tax — family count does not predict the collapse, the enforcement
  architecture does. Along c > 0, P defends cooperation to a higher c than M at
  equal Cost (a residual chooser minority sorts the whole population; a residual
  TFT minority protects only itself) — the same population-level (P) vs
  individual-level (M) split seen in the payoff-axis fits.
- **Snowdrift buffers the price** (M/P hold about 0.87 at Cost = 0.40 in
  dilemma 2 vs 0.54–0.63 in PD): a high cooperation floor makes the apparatus
  optional, so taxing it barely matters — the low-risk snowdrift result, seen on
  the information-cost axis.

## Caveats

- **Structural, not literal.** Prisoners fixes S = 0.10, whereas diagonal's
  S = 0.50 − c slides with cost, so the overlays are about which axis governs a
  mechanism, not about matching absolute thresholds — the prisoners and
  diagonal numbers sit on different scales.
- **Calibration sweeps.** Prisoners measures dilemma 1 (PD) with symmetric pop_2
  payoffs and has a dilemma 0 control rerun. The Snowdrift calibration study
  adds an independent snowdrift payoff-plane sweep (dilemma 2) confirming the
  low-risk nature of the game (high S) and direct reciprocity's insensitivity
  to S (see **snowdrift.md**).
- **Noise floor.** Per-cell qBSeen differences below ~0.01–0.02 and −b/a
  differences below ~0.03 are within run-to-run noise (see **prisoners.md** and
  **symmetric_c.md**).

## One-line readings

| Phenomenon (diagonal / mutualism)            | Prisoners attribution                      |
| -------------------------------------------- | ------------------------------------------ |
| M collapses as c rises                       | rising risk P, not vanishing R − P         |
| M survives in snowdrift                       | snowdrift has low risk (high S)            |
| Partner choice collapses near c = 0.40        | R − P → 0 at the chooser bottleneck        |
| Mutualism deterministic role split            | c0 < c1 is an R − P asymmetry              |
| IMP / IJMPQ hold cooperation at high c        | reward-led; blind to risk P                |
| Shuffle kills M-based cooperation             | the M term drops from the payoff-axis fit  |
| gs = 4 kills P-based cooperation, M recovers   | the P term drops; risk-led M remains       |
| Information cost Cost erodes cooperation slowly on the diagonal | machinery is shed harmlessly at c = 0; behavior decouples from mechanism |
| ...but not on the asymmetric branch             | with c0 fixed above zero there is no harmless-shedding refuge |
| In both cases Cost lowers the demand ceiling    | Cost thins the apparatus that c or c1 demands (price vs demand) |
