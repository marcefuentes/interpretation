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

| Mech | pop_1 gs=128 | pop_1 gs=4 | −b/a (pop_1, gs=128) | Limiting axis           |
| ---- | ------------ | ---------- | -------------------- | ----------------------- |
| M    | 0.017        | 0.116      | —                    | dead under shuffle      |
| IM   | 0.381        | 0.521      | 0.90                 | cooperation gap R − P   |
| IJM  | 0.360        | 0.706      | 0.55                 | reward / temptation R   |

Both recover substantial cooperation from M's collapse. Their payoff-axis
signatures differ informatively: IM (recent reputation only) behaves like
partner choice, tracking R − P (−b/a = 0.90); adding the lifetime signal J
turns IJM reward-dominated (−b/a = 0.55), the same shift toward R-limitation
seen when reputation is layered onto the combined mechanisms in
**prisoners_calibration.md**. This mirrors the hamilton and mutualism result
that lifetime indirect reciprocity (J) is the noise-resistant component that
survives partner turnover.

Indirect reciprocity is markedly stronger in small groups: at gs=4 (shuffle,
pop_1) IM rises to 0.521 and IJM to 0.706, roughly double their gs=128 levels.
A closed four-individual pool makes reputation signals far more relevant —
every signal concerns someone the focal individual also interacts with, and
defector signals are less prevalent — so the cascade propagates reliably. This
is the same gs=4 indirect-reciprocity boost documented for hamilton (the IJM
groupsize reversal), now reproduced in the raw payoff plane.

## Groupsize 4: direct reciprocity is invariant

Unlike partner choice, M is essentially unchanged at gs=4. Mean qBSeen
(pop_1, noshuffle) is 0.730 at both groupsizes, and the risk profile at
R = 0.50 is identical:

| P    | P − S | gs=128 | gs=4  |
| ---- | ----- | ------ | ----- |
| 0.14 | 0.04  | 0.859  | 0.868 |
| 0.30 | 0.20  | 0.829  | 0.825 |
| 0.42 | 0.32  | 0.662  | 0.652 |
| 0.46 | 0.36  | 0.469  | 0.467 |

Stable pairings supply the partner history TFT needs regardless of group size,
so the risk-limited profile carries over unchanged. This is why the
reciprocity-bearing combinations partially recover at gs=4 where pure partner
choice collapses (see **prisoners_calibration.md**): they fall back on the
groupsize-invariant M component, the mirror image of the shuffle case where
they fall back on P.

Under shuffle, the small group leaves a faint residual: M shuffle mean qBSeen
is 0.116 at gs=4 vs 0.017 at gs=128 — a closed four-individual pool lets a
little reciprocal signal persist, but it is still far below the noshuffle
level. The same small residual appears in hamilton at gs=4.

## Caveats

gs = 128 and gs = 4 .con exports exist; temporal (movie) exports exist for
gs = 128 only. PD only; pop_2 payoffs are symmetric. IM and IJM are present
only under shuffle.

## Summary

| Topic                  | Finding                                                          |
| ---------------------- | ---------------------------------------------------------------- |
| M limiting axis        | risk / defection payoff P (−b/a = 1.73); collapses as P rises      |
| M at R=0.50            | qBSeen 0.86 (P=0.14) → 0.47 (P=0.46)                              |
| M shuffle              | 0.730 → 0.017 (reverts to control); gs=4 residual 0.116           |
| M groupsize            | invariant: 0.730 at gs=128 and gs=4 (stable pairings)            |
| IM / IJM (shuffle)     | recover to 0.381 / 0.360; IM tracks R − P, IJM reward-limited     |
| IM / IJM at gs=4       | boosted to 0.521 / 0.706 (closed-pool reputation; hamilton's IJM reversal) |
| vs hamilton/mutualism  | recasts the c-collapse of M as a rising-risk effect              |
