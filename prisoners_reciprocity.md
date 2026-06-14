# Prisoners — Reciprocity

Reciprocity analysis for the prisoners payoff-plane sweep — direct reciprocity
(**M**) and indirect reciprocity (**IM**, **IJM**). Partner choice (P) is in
**prisoners_partner_choice.md**; the cross-mechanism payoff-axis attribution is
in **prisoners_calibration.md**. M is present under both shuffle and noshuffle;
IM and IJM exist only under shuffle.

## Overview

Prisoners fixes T = 0.90 and S = 0.10 and sweeps R and P independently
(172 cells, T > R > P > S). Dilemma 1 (PD) only, symmetric payoffs, pops
1/2/3, gs = 128, 30 runs per cell. See **prisoners.md** for the framing.

## Direct reciprocity is risk-limited

Across the grid (pop_1, noshuffle, gs=128) M cooperation responds about twice
as strongly to the defection-payoff axis P as to the reward axis R
(qBSeen ≈ a·R + b·P with a = 0.837, b = −1.447, so −b/a = 1.73; corr(qB, P) =
−0.601). Holding the reward fixed at R = 0.50 and raising only P (raising the
risk P − S while leaving R − P to fall) drives the collapse:

| P    | P − S | qBSeen |
| ---- | ----- | ------ |
| 0.14 | 0.04  | 0.859  |
| 0.22 | 0.12  | 0.864  |
| 0.30 | 0.20  | 0.829  |
| 0.34 | 0.24  | 0.789  |
| 0.38 | 0.28  | 0.748  |
| 0.42 | 0.32  | 0.662  |
| 0.46 | 0.36  | 0.469  |

The mechanism is mechanistic: TFT's punishment outcome is mutual defection, so
the value of retaliating is bounded by how bad mutual defection is. When P is
high (defection comfortable), TFT cannot enforce cooperation and M decays
toward the control. This is the payoff gap hamilton cannot expose on its own —
hamilton holds P = K = 0.50 fixed and only ever moves R. It reframes the
hamilton/mutualism finding that M collapses near c = 0.40 as primarily a
rising-risk effect rather than a vanishing cooperation gap.

## Shuffle destroys direct reciprocity

Mean qBSeen (pop_1, gs=128): M drops from 0.730 (noshuffle) to 0.017 (shuffle)
— indistinguishable from the control (\_ = 0.017). Without stable pairings TFT
cannot accumulate the partner history it needs. This matches the largest
shuffle penalty seen in hamilton and mutualism.

## Indirect reciprocity recovers what shuffle takes (IM, IJM)

IM and IJM were run only under shuffle — the informative regime, since direct
reciprocity is dead there and any cooperation is attributable to reputation
signals (I copies a new partner's last move toward a third party; J copies the
partner's lifetime cooperation average). Mean qBSeen, shuffle, gs=128:

| Mech | pop_1 | pop_2 | −b/a (pop_1) | Limiting axis           |
| ---- | ----- | ----- | ------------ | ----------------------- |
| M    | 0.017 | 0.019 | —            | dead under shuffle      |
| IM   | 0.381 | 0.330 | 0.90         | cooperation gap R − P   |
| IJM  | 0.360 | 0.378 | 0.55         | reward / temptation R   |

Both recover substantial cooperation from M's collapse. Their payoff-axis
signatures differ informatively: IM (recent reputation only) behaves like
partner choice, tracking R − P (−b/a = 0.90); adding the lifetime signal J
turns IJM reward-dominated (−b/a = 0.55), the same shift toward R-limitation
seen when reputation is layered onto the combined mechanisms in
**prisoners_calibration.md**. This mirrors the hamilton and mutualism result
that lifetime indirect reciprocity (J) is the noise-resistant component that
survives partner turnover.

## Caveats

Only gs = 128 .con exports exist so far; gs = 4 and movie/temporal exports are
not yet generated. PD only; pop_2 payoffs are symmetric.

## Summary

| Topic                  | Finding                                                          |
| ---------------------- | ---------------------------------------------------------------- |
| M limiting axis        | risk / defection payoff P (−b/a = 1.73); collapses as P rises      |
| M at R=0.50            | qBSeen 0.86 (P=0.14) → 0.47 (P=0.46)                              |
| M shuffle              | 0.730 → 0.017 (reverts to control)                               |
| IM / IJM (shuffle)     | recover to 0.381 / 0.360; IM tracks R − P, IJM reward-limited     |
| vs hamilton/mutualism  | recasts the c-collapse of M as a rising-risk effect              |
