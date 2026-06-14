# Prisoners — Partner Choice

Partner-choice analysis (mechanism **P**) for the prisoners payoff-plane
sweep. Pure reciprocity (M, IM, IJM) is in **prisoners_reciprocity.md**; the
cross-mechanism payoff-axis attribution is in **prisoners_calibration.md**.

## Overview

Prisoners fixes T = 0.90 and S = 0.10 and sweeps R and P independently
(18 × 18 grid, 172 cells with T > R > P > S). Dilemma 1 (PD) only, symmetric
payoffs across populations, pops 1/2/3, shuffle and noshuffle, gs = 128. Each
cell is a mean over 30 runs. See **prisoners.md** for the study framing and
**prisoners_calibration.md** for why the sweep decouples temptation, risk, and
the cooperation advantage R − P.

## Cooperation collapses onto R − P

Partner choice cooperation is, to good approximation, a function of the
cooperation advantage R − P alone. Binning all 172 cells by R − P (pop_1,
noshuffle, gs=128) shows the within-bin spread shrinking to near zero away
from the threshold:

| R − P | cells | mean qB | min   | max   | spread |
| ----- | ----- | ------- | ----- | ----- | ------ |
| 0.00  | 1     | 0.059   | 0.059 | 0.059 | 0.000  |
| 0.04  | 18    | 0.660   | 0.508 | 0.726 | 0.218  |
| 0.08  | 17    | 0.835   | 0.780 | 0.871 | 0.091  |
| 0.12  | 16    | 0.889   | 0.861 | 0.909 | 0.048  |
| 0.20  | 14    | 0.932   | 0.918 | 0.939 | 0.021  |
| 0.28  | 12    | 0.949   | 0.944 | 0.953 | 0.010  |
| 0.40  | 9     | 0.963   | 0.961 | 0.965 | 0.004  |
| 0.60  | 4     | 0.972   | 0.971 | 0.973 | 0.001  |
| 0.72  | 1     | 0.975   | 0.975 | 0.975 | 0.000  |

The absolute (R, P) level barely matters: at R − P = 0.20, every cell from
(R = 0.34, P = 0.14) to (R = 0.66, P = 0.46) sits at qB ≈ 0.92–0.94. Spread is
largest near R − P = 0.04, the transition zone where runs split between
cooperative and collapsed fixed points. This is the independent confirmation
of the hamilton chooser-bottleneck story: hamilton P (gs=128, pop_1, shuffle)
falls from 0.788 at R − P = 0.06 to 0.056 at R − P = 0.00, and the prisoners
sweep shows the same threshold is set by R − P rather than by temptation or
risk separately.

## Genotype structure and P1 hitchhiking

C1P1 (active choosers), C1P0 (non-choosing cooperators), and C0P1 (silent
carriers) along R − P (pop_1, noshuffle, gs=128):

| R − P | qB    | C1P1  | C1P0  | C0P1  |
| ----- | ----- | ----- | ----- | ----- |
| 0.00  | 0.059 | 0.052 | 0.007 | 0.454 |
| 0.04  | 0.680 | 0.651 | 0.029 | 0.238 |
| 0.08  | 0.846 | 0.780 | 0.066 | 0.125 |
| 0.16  | 0.925 | 0.799 | 0.125 | 0.061 |
| 0.24  | 0.946 | 0.767 | 0.179 | 0.042 |
| 0.40  | 0.965 | 0.723 | 0.242 | 0.026 |
| 0.72  | 0.975 | 0.649 | 0.326 | 0.017 |

Same pattern as hamilton: choosers (C1P1) carry cooperation, and below the
threshold the collapse leaves a large pool of C0P1 silent carriers (0.454 at
R − P = 0) — P1 hitchhikers that accumulate by neutral mutation from C1P1.
As R − P grows the population can afford non-choosing cooperators (C1P0 rises
to 0.33), because abundant cooperators make partner sorting less necessary.

## Pop_2 symmetry breaking

With symmetric payoffs, two coevolving populations break symmetry
stochastically into a cooperating side (fset_0) and a defecting side
(fset_1). Slice at P = 0.14 (noshuffle, gs=128):

| R    | R − P | qB_0  | qB_1  | ΔqB    | w_0   | w_1   |
| ---- | ----- | ----- | ----- | ------ | ----- | ----- |
| 0.18 | 0.04  | 0.114 | 0.077 | +0.037 | 0.152 | 0.181 |
| 0.30 | 0.16  | 0.286 | 0.079 | +0.207 | 0.148 | 0.314 |
| 0.46 | 0.32  | 0.496 | 0.075 | +0.420 | 0.148 | 0.485 |
| 0.62 | 0.48  | 0.710 | 0.082 | +0.628 | 0.154 | 0.656 |
| 0.78 | 0.64  | 0.899 | 0.120 | +0.779 | 0.184 | 0.808 |
| 0.86 | 0.72  | 0.969 | 0.278 | +0.691 | 0.311 | 0.864 |

The cooperating population (fset_0) climbs with R − P while the defecting
population stays near 0.07–0.10, and the defector consistently earns more
(w_1 > w_0) — the paradox-of-success signature also seen in hamilton pop_2.
The asymmetry peaks around R − P ≈ 0.64 and narrows again only when R is so
large that even the defecting side begins to cooperate.

## Pop_3: evolving vs fixed partner

P mechanism, noshuffle, gs=128, mean over all 172 cells: the evolving
population reaches qBSeen = 0.410 against a fixed partner held at 25% each
genotype; the fixed population reads 0.500 by construction (half its
genotypes are C1).

## Shuffle invariance

Partner choice is insensitive to shuffling — mean qBSeen (pop_1, gs=128) is
0.898 under both noshuffle and shuffle, and the payoff-axis signature is
unchanged (−b/a = 0.89 either way). Per-step rematching within the group makes
any initial random pairing irrelevant, exactly as in hamilton and mutualism.

## Caveats

Only gs = 128 .con exports exist so far; gs = 4 and movie/temporal exports are
not yet generated. PD only.

## Summary

| Topic              | Finding                                                             |
| ------------------ | ------------------------------------------------------------------- |
| Controlling axis   | qBSeen is a function of R − P; absolute (R, P) level irrelevant      |
| Threshold          | Within-bin spread peaks at R − P ≈ 0.04, vanishes by R − P ≥ 0.28    |
| Genotypes          | C1P1 carries coop; C0P1 hitchhikers dominate below threshold (0.45)  |
| Pop_2              | Stochastic symmetry breaking; defecting side earns more (w_1 > w_0)  |
| Shuffle            | Invariant (0.898 both); −b/a = 0.89 unchanged                       |
| vs hamilton        | Reproduces the R − P chooser-bottleneck threshold from the (R,P) plane |
