# Snowdrift Calibration Study

Calibration study analysis for the raw Snowdrift payoff-plane sweep. Unlike diagonal and mutualism (which derive payoffs from a single cost c), the snowdrift sweep fixes T = 0.90 and P = 0.10 and sweeps R and S independently over an 18 × 18 grid (172 cells satisfying T > R > S > P). This decouples temptation (T − R), the sucker gap (R − S), risk (P − S), and the cooperation advantage (R − P), which diagonal welds onto one axis — letting us attribute each mechanism's behavior to a specific payoff gap in a snowdrift-ordered payoff space.

The main analysis here is the dilemma 2 (Snowdrift) payoff plane. Payoffs are symmetric across populations; pops 1/2/3; shuffle and noshuffle; gs = 128 and gs = 4 (gs = 128 movie exports available via snowdrift_1run for temporal dynamics); 30 runs per cell in the multi-run sweep.

- **[snowdrift_calibration.md](snowdrift_calibration.md)** — cross-mechanism payoff-axis attribution (which gap limits each mechanism in Snowdrift), the shuffle decomposition, and groupsize reversals
- **[snowdrift_partner_choice.md](snowdrift_partner_choice.md)** — mechanism P: cooperation robustness, genotype structure, pop_2 symmetry breaking, and pop_3
- **[snowdrift_reciprocity.md](snowdrift_reciprocity.md)** — mechanisms M, IM, and IJM: M is insensitive to the sucker payoff S, shuffle sensitivity, and groupsize-reversal boosts

For how these payoff-axis attributions compare to prisoners and map onto the diagonal/mutualism thresholds, see **[synthesis.md](synthesis.md)**.

## Headline result

Because Snowdrift features a high cooperation floor (where cooperation is individually rational when the partner defects, S > P), the evolutionary dynamics differ fundamentally from the Prisoner's Dilemma:

| Mechanism family | Limiting payoff axis | Reading for diagonal/mutualism |
| ---------------- | -------------------- | ------------------------------ |
| M | reward R (insensitive to S) | TFT pays the sucker payoff S only on round 1; risk is set by P, not S |
| P | reward R (cooperation is high) | high cooperation floor prevents the chooser bottleneck from collapsing |
| MP, MPQ, IMP, IJMPQ | reward R (saturation) | partner choice and reputation easily maintain near-perfect cooperation |

## Replicates and noise floor

Every value here is a mean over 30 independent runs (Runs = 30 in the .glo metadata). The csv_0_for_image.con files carry a companion SD column per statistic (qBSeenSD, wmeanSD, etc.); the standard error of a cell mean is SD / √30.

Typical noise floor (gs = 128, pop_1, noshuffle): median qBSeenSD is around 0.002 to 0.015, translating to a standard error of 0.0004 to 0.003. Spread is localized near the transition zones, but since the snowdrift floor is high (average cooperation under control is 0.493), bistability is rare compared to the Prisoner's Dilemma.

Practical reading guide: per-cell qBSeen differences below 0.01 to 0.02 are within run-to-run noise. Mean-qBSeen and payoff-axis fit ratios are fitted over all 172 cells, so they are much more precise; treat differences below 0.03 as not meaningful.

## Role in this project

Snowdrift is an auxiliary calibration study used to interpret mechanism signatures seen in **asymmetric_c0_c1** and **symmetric_c**, not a primary biological endpoint. Earlier write-ups under the previous parameterization are superseded by these documents and are not part of the current K = 0.5, b = 0.4 study.
