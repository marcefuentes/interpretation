# Prisoners — Payoff-Axis Calibration

Cross-mechanism calibration analysis for the prisoners study. Per-mechanism
detail is in **prisoners_partner_choice.md** (P) and
**prisoners_reciprocity.md** (M, IM, IJM). See **prisoners.md** for the index.

## Why this study exists

Hamilton and mutualism derive payoffs from a single cost parameter c
(T = K + b, R = K + b − c, P = K, S = K − c). That welds three distinct
quantities onto one axis:

- temptation T − R = c
- risk (sucker gap) P − S = c
- cooperation advantage R − P = b − c

Because all three move together with c, hamilton can show *that* a mechanism
collapses as c rises but cannot say *which* payoff gap drives the collapse.
The prisoners study removes that confound: it fixes T = 0.90 and S = 0.10 and
sweeps R and P independently over an 18 × 18 grid (172 cells satisfying
T > R > P > S). Each cell is a mean over 30 runs (see the noise-floor note in
**hamilton.md**). Dilemma folder 1 (PD) only; payoffs are symmetric across
populations.

## Payoff geometry

With T and S pinned, the two free coordinates are:

- R — the mutual-cooperation reward. Raising R lowers temptation
  (T − R = 0.90 − R) and raises the cooperation advantage (R − P).
- P — the mutual-defection payoff. Raising P raises risk (P − S = P − 0.10)
  and lowers the cooperation advantage (R − P).

Two reference loci matter for the hamilton/mutualism comparison:

- R − P = const are the iso-cooperation-advantage diagonals.
- R + P = 1.0 is the temptation = risk locus (0.90 − R = P − 0.10). Hamilton
  is structurally pinned to temptation = risk = c, so the R + P = 1 anti-
  diagonal is the closest in-grid analogue of the hamilton constraint; cells
  off it (R + P ≠ 1) are regimes hamilton cannot reach.

## Payoff-axis sensitivity

Fitting qBSeen ≈ a·R + b·P + const across the 172 cells gives the marginal
response to each axis. The ratio −b/a measures whether cooperation responds
more to the reward/temptation axis (R) or the risk/defection-payoff axis (P):
−b/a > 1 means P-dominated, ≈ 1 means it tracks R − P, < 1 means R-dominated.

Pop_1 (single population), PD, noshuffle, gs=128:

| Mech   | mean qB | a (dq/dR) | b (dq/dP) | −b/a | corr(qB, P) | Controlled by         |
| ------ | ------- | --------- | --------- | ---- | ----------- | --------------------- |
| \_     | 0.017   | 0.006     | −0.030    | 4.90 | −0.737      | nothing (no coop)     |
| M      | 0.730   | 0.837     | −1.447    | 1.73 | −0.601      | risk / defection P    |
| P      | 0.898   | 0.447     | −0.399    | 0.89 | −0.274      | cooperation gap R − P |
| MP     | 0.884   | 0.648     | −0.365    | 0.56 | −0.058      | reward / temptation R |
| MPQ    | 0.906   | 0.567     | −0.319    | 0.56 | −0.053      | reward / temptation R |
| IMP    | 0.890   | 0.642     | −0.319    | 0.50 | −0.003      | reward / temptation R |
| IJMPQ  | 0.917   | 0.488     | −0.260    | 0.53 | −0.029      | reward / temptation R |

Three regimes emerge that hamilton could never separate:

- **Direct reciprocity (M) is risk-limited.** M is roughly twice as sensitive
  to P as to R (−b/a = 1.73). Raising the mutual-defection payoff erodes TFT's
  advantage, because TFT's punishment outcome *is* mutual defection: when P is
  high, retaliating costs almost nothing to the defector and TFT can no longer
  enforce cooperation. Holding R = 0.50 fixed, M cooperation falls from 0.86
  (P = 0.14) to 0.47 (P = 0.46) — see **prisoners_reciprocity.md**.
- **Partner choice (P) tracks R − P.** Equal sensitivity to both axes
  (−b/a = 0.89): cooperation is essentially a function of the cooperation
  advantage R − P alone. Cells with identical R − P but very different
  absolute (R, P) give nearly identical cooperation (the collapse is in
  **prisoners_partner_choice.md**).
- **Combined and indirect-rich mechanisms (MP, MPQ, IMP, IJMPQ) are
  reward-limited.** −b/a ≈ 0.5 and corr(qB, P) ≈ 0 — they are almost blind to
  the defection baseline P and respond chiefly to R (reward / low temptation).
  Reciprocity plus reputation removes the risk sensitivity that limits M
  alone.

## Shuffle decomposes the mechanisms additively

Shuffling destroys direct reciprocity (stable pairings are required to
accumulate TFT history). In the payoff-axis fit this shows up as components
dropping out cleanly:

Pop_1, PD, gs=128:

| Mech   | mean qB noshuffle | mean qB shuffle | −b/a noshuffle | −b/a shuffle | Reading                          |
| ------ | ----------------- | --------------- | -------------- | ------------ | -------------------------------- |
| M      | 0.730             | 0.017           | 1.73           | —            | dies; reverts to control         |
| P      | 0.898             | 0.898           | 0.89           | 0.89         | shuffle-invariant                |
| MP     | 0.884             | 0.898           | 0.56           | 0.89         | M term removed; reverts to P     |
| MPQ    | 0.906             | 0.907           | 0.56           | 0.91         | M term removed; reverts to P     |
| IMP    | 0.890             | 0.900           | 0.50           | 0.84         | loses M; I + P remain (toward P) |
| IJMPQ  | 0.917             | 0.937           | 0.53           | 0.52         | J, Q survive; stays reward-led   |

The MP and MPQ rows are the clearest result: under shuffle their payoff-axis
signature snaps exactly onto pure P (−b/a 0.56 → 0.89), making visible that
their noshuffle reward-dominance came entirely from the M component. IJMPQ
keeps its reward-dominated signature because the lifetime loci J and Q are
shuffle-invariant. The shuffle-only mechanisms confirm the split: indirect
reciprocity recovers cooperation that shuffled M loses (mean qB: M = 0.017,
IM = 0.381, IJM = 0.360), with IM tracking R − P (−b/a = 0.90, like partner
choice) and IJM turning reward-dominated once the lifetime signal J is added
(−b/a = 0.55).

## Groupsize 4 is the mirror image of shuffle

Shuffle removes the direct-reciprocity (M) component; small groups remove the
partner-choice (P) component (mutual C1P1 swaps are too rare among four
individuals). The payoff-axis fit makes both subtractions visible, and they
are mirror images of each other.

Pop_1, PD, noshuffle, gs=4 vs gs=128:

| Mech   | mean qB gs=128 | mean qB gs=4 | −b/a gs=128 | −b/a gs=4 | Reading at gs=4                    |
| ------ | -------------- | ------------ | ----------- | --------- | ---------------------------------- |
| M      | 0.730          | 0.730        | 1.73        | 1.72      | groupsize-invariant (stable pairs) |
| P      | 0.898          | 0.075        | 0.89        | (collapsed)| chooser bottleneck fails           |
| MP     | 0.884          | 0.748        | 0.56        | 1.62      | P term removed; reverts to M        |
| MPQ    | 0.906          | 0.782        | 0.56        | 1.50      | P term removed; reverts to M        |
| IMP    | 0.890          | 0.785        | 0.50        | 1.58      | P term removed; reverts to M        |
| IJMPQ  | 0.917          | 0.894        | 0.53        | 0.43      | survives; stays reward-led          |

The contrast is clean. Under shuffle, MP/MPQ snap onto pure P's signature
(−b/a → 0.89, R − P / reward-led) because the M term dies. Under gs = 4, the
same mechanisms snap onto M's signature (−b/a → 1.5–1.6, risk-led) because the
P term dies. Direct reciprocity M is invariant to groupsize (stable pairings
supply history regardless of group size), and IJMPQ is the only mechanism
robust to both perturbations — its indirect (I) and lifetime (J, Q) loci
survive partner turnover and small groups alike. Reading the two tables
together isolates which payoff axis each component contributes: P supplies
R − P sensitivity, M supplies risk (P-axis) sensitivity, and the reputation
loci supply the reward-led robustness.

## The temptation = risk locus (R + P = 1.0)

Mean qBSeen on the hamilton-analogue anti-diagonal (pop_1, PD, noshuffle,
gs=128, 9 cells): P = 0.944, M = 0.899, IMP = 0.956, IJMPQ = 0.965. Along this
locus cooperation stays high and falls only toward the small-R − P corner
(R = 0.54, P = 0.46), where the cooperation advantage shrinks to 0.08 —
mirroring the hamilton collapse as R − P → 0.

## Cross-checks with hamilton and mutualism

- **Partner-choice threshold.** Hamilton P (shuffle, gs=128, pop_1) collapses
  as R − P → 0: qBSeen 0.864 at R − P = 0.10, 0.788 at 0.06, 0.668 at 0.04,
  0.056 at 0.00. The prisoners P landscape reproduces this from the other
  direction — cooperation is monotone in R − P and only crosses below 0.5 in
  the smallest-R − P cells — confirming R − P is the controlling variable, not
  temptation or risk individually.
- **Direct reciprocity.** Hamilton/mutualism could only show M collapsing near
  c = 0.40 (where both R − P → 0 and risk P − S = c is largest). Prisoners
  isolates the cause: M tracks risk P, so the hamilton collapse is largely a
  rising-risk effect, not purely a vanishing cooperation gap.
- **Symmetry breaking.** Prisoners pop_2 is symmetric (like hamilton pop_2)
  and breaks stochastically into a cooperator/defector role split, with the
  cooperating side earning less (paradox of success) — the same signature
  documented for hamilton pop_2. See **prisoners_partner_choice.md**.

## Caveats

- Complementary, not a superset: prisoners fixes S = 0.10 whereas hamilton's
  S = 0.50 − c slides with c, so overlays are structural, not literal, and the
  absolute thresholds sit at a different scale than hamilton's.
- PD only (dilemma 1) — no snowdrift, no dilemma 0, and pop_2 payoffs are
  symmetric (no c0 ≠ c1 mutualism analogue).
- gs = 128 and gs = 4 .con exports exist (noshuffle and shuffle), plus gs = 128
  movie exports (prisoners_1run) for temporal dynamics. gs = 4 movie exports
  are not yet generated.

## Summary

| Mechanism family | Limiting payoff axis        | −b/a (pop_1) | Hamilton/mutualism reading                    |
| ---------------- | --------------------------- | ------------ | --------------------------------------------- |
| M                | risk / defection payoff P   | 1.73         | c-collapse is mostly rising-risk, not just R−P |
| P                | cooperation advantage R − P | 0.89         | chooser bottleneck set by R − P                |
| MP, MPQ          | reward / temptation R       | 0.56         | reward-led only via the M component (shuffle reverts to P) |
| IMP, IJMPQ       | reward / temptation R       | 0.50–0.53    | reputation removes M's risk sensitivity        |
| IM (shuffle)     | cooperation advantage R − P | 0.90         | recent indirect reciprocity acts like P        |
| IJM (shuffle)    | reward / temptation R       | 0.55         | lifetime signal J makes it reward-led          |
