# Snowdrift — Reciprocity

Reciprocity analysis for the snowdrift payoff-plane sweep — direct reciprocity (M) and indirect reciprocity (IM, IJM). Partner choice (P) is in **snowdrift_partner_choice.md**; the cross-mechanism payoff-axis attribution is in **snowdrift_calibration.md**. M is present under both shuffle and noshuffle; IM and IJM exist only under shuffle.

## Overview

Snowdrift fixes T = 0.90 and P = 0.10 and sweeps R and S independently (172 cells, T > R > S > P). Dilemma 2 (Snowdrift) only, symmetric payoffs across populations, pops 1/2/3, gs = 128, 30 runs per cell. See **snowdrift.md** for the framing.

## Direct reciprocity is insensitive to the sucker payoff S

Across the grid (pop_1, noshuffle, gs=128) M cooperation responds strongly to the mutual cooperation reward R (a = 1.456) but is nearly flat with the sucker payoff S (b = 0.223, so −b/a = −0.15; corr(qB, S) = 0.566). Holding the reward fixed at R = 0.50 and raising only S (raising the sucker payoff S while leaving R − S to fall) shows M cooperation rising only slightly:

| S | S − P | qBSeen | Control |
| ---- | ----- | ------ | ------- |
| 0.14 | 0.04 | 0.159 | 0.122 |
| 0.18 | 0.08 | 0.214 | 0.189 |
| 0.22 | 0.12 | 0.268 | 0.243 |
| 0.26 | 0.16 | 0.322 | 0.294 |
| 0.30 | 0.20 | 0.355 | 0.345 |
| 0.34 | 0.24 | 0.405 | 0.383 |
| 0.38 | 0.28 | 0.430 | 0.415 |
| 0.42 | 0.32 | 0.463 | 0.453 |
| 0.46 | 0.36 | 0.486 | 0.477 |

Comparing M to the control reveals that direct reciprocity provides only a tiny boost (around 0.01 to 0.04) in cooperation across all values of S. 

The mechanism is structural: TFT (dTFT) cooperates on the first round of a partner pairing, paying the sucker penalty S if the partner defects. In all subsequent rounds, TFT mimics the partner's defection, resulting in mutual defection (earning P = 0.10). Because the number of rounds per pairing is large, the first-round sucker payoff S is heavily discounted. The long-term payoff is dominated by P, which is fixed at 0.10. Therefore, the value of S does not affect TFT's success against defectors, rendering M cooperation levels highly insensitive to S.

## Shuffle destroys direct reciprocity

Without stable pairings, TFT cannot accumulate history. Mean qBSeen (pop_1, gs=128) for M drops from 0.599 (noshuffle) to 0.497 (shuffle) — indistinguishable from the control (0.493 under control). This matches the shuffle penalty seen in hamilton and mutualism.

## Indirect reciprocity recovers what shuffle takes (IM, IJM)

IM and IJM were run only under shuffle — the informative regime, since direct reciprocity is dead there and any cooperation is attributable to reputation signals (I copies a new partner's last move toward a third party; J copies the partner's lifetime cooperation average). Mean qBSeen, shuffle, gs=128:

| Mech | pop_1 gs=128 | pop_1 gs=4 | −b/a (pop_1, gs=128) | Limiting axis |
| ---- | ------------ | ---------- | -------------------- | ------------- |
| M | 0.497 | 0.588 | −0.96 | dead under shuffle |
| IM | 0.605 | 0.690 | −0.18 | reward R (S-insensitive) |
| IJM | 0.696 | 0.756 | −0.10 | reward R (S-insensitive) |

Both recover substantial cooperation from M's collapse. Their payoff-axis signatures show they are highly reward-led and insensitive to S (−b/a = −0.18 for IM, −0.10 for IJM). Because these are reciprocity-based mechanisms, they occasionally pay S against defectors, but their long-term payoff is dominated by R. Therefore, like direct reciprocity, they are insensitive to S.

Both mechanisms are stronger in small groups: at gs=4 (shuffle, pop_1), IM rises to 0.690 and IJM to 0.756. A closed four-individual pool makes reputation signals far more relevant (reputation signals circulate in a tight pool and defector signals are less prevalent), so the cooperative cascade propagates reliably. This is the groupsize boost for indirect reciprocity documented in hamilton and prisoners.

## Groupsize 4: direct reciprocity is invariant

Unlike partner choice, M is essentially unchanged at gs=4. Mean qBSeen (pop_1, noshuffle) is 0.599 at both groupsizes, and the risk profile at R = 0.50 is virtually identical:

| S | S − P | gs=128 | gs=4 |
| ---- | ----- | ------ | ----- |
| 0.14 | 0.04 | 0.159 | 0.159 |
| 0.30 | 0.20 | 0.355 | 0.355 |
| 0.46 | 0.36 | 0.486 | 0.486 |

Stable pairings supply the history TFT needs regardless of group size, so the groupsize-invariant M component carries over unchanged. This is why the reciprocity-bearing combinations partially recover at gs=4 where pure partner choice collapses (see **snowdrift_calibration.md**).

## Caveats

- con exports and temporal (movie) exports exist for both gs = 128 and gs = 4.
