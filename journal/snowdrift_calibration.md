# Snowdrift — Payoff-Axis Calibration

Cross-mechanism calibration analysis for the snowdrift study. Per-mechanism detail is in **snowdrift_partner_choice.md** (P) and **snowdrift_reciprocity.md** (M, IM, IJM). See **snowdrift.md** for the index.

## Why this study exists

symmetric_c and asymmetric_c0_c1 derive payoffs from a single cost parameter c. For dilemma 2 (Snowdrift), this means T = K + b, R = K + b − c/2, P = K, and S = K + b − c. That welds three distinct quantities onto one axis:

- temptation T − R = c/2
- risk (sucker gap) R − S = c/2
- cooperation advantage R − P = b − c/2

Because all three move together with c, symmetric_c can show that a mechanism collapses as c rises but cannot say which payoff gap drives the collapse. The snowdrift calibration study removes that confound: it fixes T = 0.90 and P = 0.10 and sweeps R and S independently over an 18 × 18 grid (172 cells satisfying T > R > S > P). Each cell is a mean over 30 runs. Dilemma folder 2 (Snowdrift) is the sweep of interest; payoffs are symmetric across populations.

## Payoff geometry

With T and P pinned, the two free coordinates are:

- R — the mutual-cooperation reward. Raising R lowers temptation (T − R = 0.90 − R) and raises the cooperation advantage (R − P).
- S — the sucker payoff. Raising S reduces the risk of being exploited (reduces R − S and increases S − P).

In a Snowdrift game, S > P always holds. This establishes a high baseline cooperation floor because even when playing against defectors, a cooperator receives S (which is higher than the mutual-defection payoff P = 0.10). Cooperation is therefore individually rational when the partner defects.

## Payoff-axis sensitivity

Fitting qBSeen ≈ a·R + b·S + const across the 172 cells gives the marginal response to each axis. The ratio −b/a measures whether cooperation responds more to the reward/temptation axis (R) or the sucker/risk axis (S). A negative ratio −b/a indicates that both R and S coefficients are positive: raising reward R increases cooperation (a > 0) and raising sucker payoff S also increases cooperation (b > 0) by reducing the exploitation penalty.

Pop_1 (single population), Snowdrift, noshuffle, gs=128:

| Mech | mean qB | a (dq/dR) | b (dq/dS) | −b/a | corr(qB, RS) | Controlled by |
| ---- | ------- | --------- | --------- | ---- | ------------ | ------------- |
| _ | 0.493 | 0.746 | 0.741 | −0.99 | −0.012 | payoff floor (R and S) |
| M | 0.599 | 1.456 | 0.223 | −0.15 | 0.356 | reward R (S-insensitive) |
| P | 0.947 | 0.231 | −0.044 | 0.19 | 0.486 | reward R (saturated) |
| MP | 0.944 | 0.311 | −0.017 | 0.05 | 0.411 | reward R (saturated) |
| MPQ | 0.951 | 0.362 | −0.017 | 0.05 | 0.348 | reward R (saturated) |
| IMP | 0.926 | 0.505 | −0.050 | 0.10 | 0.459 | reward R (saturated) |
| IJMPQ | 0.956 | 0.315 | −0.015 | 0.05 | 0.323 | reward R (saturated) |

Three regimes emerge from this sweep:

- **Control matches the payoff floor.** Under the dummy control mechanism _, cooperation is highly sensitive to both reward R and sucker payoff S (a ≈ 0.75, b ≈ 0.74, so −b/a = −0.99). This reflects a mixed population driven entirely by mutations and selection: higher payoffs for cooperation (whether mutual or unilateral) naturally increase cooperation.
- **Direct reciprocity (M) is insensitive to the sucker payoff S.** Cooperation under M responds strongly to R (a = 1.456) but is nearly flat with S (b = 0.223, so −b/a = −0.15). Direct reciprocity (TFT) cooperates on the first round and then defects if the partner defects. Consequently, the sucker payoff S is paid exactly once per pairing; all subsequent rounds result in mutual defection (earning P = 0.10). Because the number of rounds per pairing is large, the single round 1 sucker penalty is heavily discounted, making the evolutionary success of TFT almost completely insensitive to S.
- **Partner choice and combined mechanisms are reward-led and saturated.** Under P, MP, MPQ, IMP, and IJMPQ, cooperation is extremely high (mean qB sits at 0.92 to 0.96) across the entire payoff plane. Coefficients are small and −b/a is close to zero, showing that cooperation is maintained at near-saturation levels and is limited only at very low values of R.

## Shuffle decomposes the mechanisms additively

Shuffling destroys direct reciprocity because stable pairings are required to track partner history. In the payoff-axis fit, this shows up as M dropping out cleanly, reverting the combined mechanisms to partner-choice behavior:

Pop_1, Snowdrift, gs=128:

| Mech | mean qB noshuffle | mean qB shuffle | −b/a noshuffle | −b/a shuffle | Reading |
| ---- | ----------------- | --------------- | -------------- | ------------ | ------- |
| M | 0.599 | 0.497 | −0.15 | −0.96 | dies; reverts to control |
| P | 0.947 | 0.946 | 0.19 | 0.19 | shuffle-invariant |
| MP | 0.944 | 0.946 | 0.05 | 0.20 | M term removed; reverts to P |
| MPQ | 0.951 | 0.959 | 0.05 | 0.11 | M term removed; reverts to P |
| IMP | 0.926 | 0.956 | 0.10 | 0.04 | stays reward-led |
| IJMPQ | 0.956 | 0.960 | 0.05 | 0.06 | stays reward-led |

Under shuffle, direct reciprocity M falls to control levels (0.497 vs 0.493) and its payoff signature reverts to the control's equal sensitivity (−b/a = −0.96). MP and MPQ snap to the partner-choice signature (−b/a ≈ 0.11 to 0.20). IJMPQ is unaffected because its lifetime components (J and Q) are shuffle-invariant. The shuffle-only reputation mechanisms confirm this: recent reputation IM recovers cooperation to 0.605 with a reciprocity-like signature (−b/a = −0.18), and lifetime reputation IJM recovers to 0.696 and becomes highly reward-led (−b/a = −0.10) as the lifetime signal J is added.

## Groupsize 4 is not a complete collapse

In Prisoners (PD), a groupsize of 4 catastrophically collapses partner choice (P mean qB falls to 0.075) because the chooser bottleneck cannot bootstrap. In Snowdrift, the high cooperation floor (0.493 under control) ensures that cooperators are abundant even in small groups. Cooperators easily find each other to swap, preventing a complete collapse:

Pop_1, Snowdrift, noshuffle, gs=4 vs gs=128:

| Mech | mean qB gs=128 | mean qB gs=4 | −b/a gs=128 | −b/a gs=4 | Reading at gs=4 |
| ---- | -------------- | ------------ | ----------- | --------- | --------------- |
| M | 0.599 | 0.599 | −0.15 | −0.15 | groupsize-invariant |
| P | 0.947 | 0.717 | 0.19 | 0.01 | weakened but survives |
| MP | 0.944 | 0.769 | 0.05 | 0.09 | P term weakened; M carries |
| MPQ | 0.951 | 0.812 | 0.05 | 0.07 | P term weakened |
| IMP | 0.926 | 0.823 | 0.10 | 0.14 | P term weakened |
| IJMPQ | 0.956 | 0.904 | 0.05 | 0.14 | robust to gs=4 |

Direct reciprocity M is perfectly invariant to groupsize (mean qB is 0.599 at both gs = 128 and gs = 4) because stable pairings supply the needed history. Partner choice P drops from 0.947 to 0.717 but does not collapse, and its payoff signature remains strongly reward-led (−b/a = 0.01). Combined mechanisms (MP, MPQ, IMP, IJMPQ) remain highly cooperative at gs = 4, falling back on the groupsize-invariant M component and reputation signals.

## Cross-checks with symmetric_c and asymmetric_c0_c1

- **Cooperation floor.** In symmetric_c and asymmetric_c0_c1 dilemma 2, cooperation remains high across all mechanisms at moderate costs. The snowdrift sweep explains why: the baseline payoff S > P provides an evolutionary floor that prevents defection from dominating, ensuring that partner choice and direct reciprocity operate in a cooperator-rich environment.
- **Direct reciprocity.** Direct reciprocity noshuffle M in symmetric_c snowdrift maintains high cooperation because TFT is insensitive to the sucker payoff S. The collapse of M in symmetric_c PD is a rising-risk (P-defection payoff) effect, which is absent in Snowdrift since P is fixed at the low value of 0.10.
- **Symmetry breaking.** Snowdrift pop_2 breaks symmetry stochastically into cooperator and defector populations under partner choice P. Because the defector population earns the temptation payoff T while the cooperator population is stuck earning the sucker payoff S, the defector earns significantly more (w_1 > w_0). This is the paradox-of-success signature, now visible in its most extreme form in the raw Snowdrift payoff plane.

## Caveats

- Complementary, not a superset: snowdrift fixes P = 0.10 whereas symmetric_c's P = 0.50 is fixed at baseline. The sweep variables are R and S, whereas in Prisoners they were R and P.
- gs = 128 and gs = 4 con exports exist; gs = 128 movie exports (snowdrift_1run) exist for temporal dynamics.

## Summary

| Mechanism family | Limiting payoff axis | −b/a (pop_1) | symmetric_c/asymmetric_c0_c1 reading |
| ---------------- | -------------------- | ------------ | -------------------------- |
| M | reward R (insensitive to S) | −0.15 | TFT pays S only once; risk is set by P, not S |
| P | reward R (saturated) | 0.19 | high cooperation floor prevents the chooser bottleneck from collapsing |
| MP, MPQ | reward R (saturated) | 0.05 | partner choice and reciprocity easily maintain cooperation |
| IMP, IJMPQ | reward R (saturated) | 0.05–0.10 | reputation and choice are robust to groupsize and turnover |
| IM (shuffle) | reward R (S-insensitive) | −0.18 | reputation-led reciprocity tracks reward R |
| IJM (shuffle) | reward R (S-insensitive) | −0.10 | lifetime signal J makes reputation reward-led |
