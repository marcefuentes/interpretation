# Discussion

*Draft scaffold. Backing: [synthesis](../journal/synthesis.md) and linked journal
analyses (regression-checked by ai/verify_claims.py).*

## What each mechanism is really limited by

Decoupling the payoff gaps turns three vague "collapses as cost rises" statements into
specific attributions: direct reciprocity is limited by risk (the cost of its own
punishment outcome, mutual defection), partner choice by the cooperation advantage
R − P (the fuel for assortment), and reputation-rich mechanisms by reward alone (they
ignore the defection baseline). This explains why the mechanisms rank as they do, why
snowdrift rescues reciprocity, and why the combined mechanisms break the ceilings that
bound M and P individually.

## Two populations: what the second one changes

The second population does not change the *dynamical regime* (both single- and two-
population cases settle into absorbing states, not cycles). What it changes is the
*outcome*: two populations can lock into a cooperator/exploiter role split even when
their parameters match.

We separate **parameter symmetry** (c0 = c1, i0 = i1, identical payoffs) from
**outcome symmetry** (similar cooperation and fitness). Partner choice at parameter
symmetry produces spontaneous symmetry breaking — a stochastic outcome split. A
cooperation-cost gap seeds a deterministic assignment in the prisoner's dilemma
(Fig. 3). We omit a parallel asymmetric snowdrift figure because the sucker payoff
already sustains cooperation and between-population splits without enforcement
(Fig. 2 and Fig. S1); partner choice under c0 ≠ c1 then adds little beyond that
floor. Information-cost asymmetry at
equal cooperation cost also assigns roles deterministically under P, while IJMPQ can
invert the mapping; snowdrift often removes these PD locks. In all cases the
cooperating side is typically exploited — the paradox of success — and reward-led
combined mechanisms soften the outcome gap.

## Information cost versus cooperation cost

Adding an information-cost axis reframes enforcement around two costs. Cooperation
cost sets the temptation and risk the machinery must resist; information cost is
escapable only by shedding the machinery. Alone each is survivable; together they
compound, because information cost thins the apparatus cooperation cost requires.
The striking consequence is that behaviour and mechanism decouple: cooperation can
persist through unconditional cooperators after the expensive conditional machinery
has been selected away — cooperation without active enforcement, but only where the
game does not punish it. Once one population is held at c0 = 0.10 and the second is
costlier still, there is no harmless information-cost edge at zero cooperation cost,
so information cost retreats the cooperation-cost ceiling directly and compresses the
cooperator/exploiter split rather than merely changing the genotype route.

**Which cost assigns roles?** Parameter symmetry in cooperation cost does not imply
outcome symmetry. When c0 = c1 but i0 ≠ i1, per-population information-cost
asymmetry alone assigns or inverts the role split depending on mechanism — partner
choice to the side with lower information cost (deterministic), IJMPQ inverted via
hitchhiking. When both cooperation cost and information cost differ between
populations, the cooperation-cost gap is the default outcome assigner (partner
choice: the lower-cooperation-cost population cooperates more in 170/176 cells), and
the hitchhiking inversion survives only on an i0 ≈ 0 strip (13 cells), attenuated
relative to the c0 = c1, i0 ≠ i1 case. Snowdrift removes the wedge entirely.
Cooperation cost therefore sets the baseline; information cost can locally override
combined mechanisms only where the population with lower cooperation cost pays no
information cost. What decides whether a mechanism can be overridden at all is the
presence of the reciprocity family rather than the size of the information bill it
pays. Because the tax is levied once per family carried rather than once per locus,
direct reciprocity and partner choice pay exactly the same amount, and the four
combined mechanisms pay exactly the same amount as each other; in both matched pairs
the inversion follows reciprocity and not the amount paid. Every reciprocity-bearing
mechanism inverts somewhere in that strip and no mechanism without one does, because
reciprocity is what supplies the second-order-free-rider niche the inversion runs
through.

**Information cost is a relational cost, not a private one.** The crossed square makes
a distinction the single-axis sweeps could not: it separates the cost a population pays
from the cost its partner pays. Each mechanism turns out to be governed by just one of
the two, for both populations at once, and the families pick opposite axes. Partner
choice is bound by the high-cooperation-cost population's information cost, because a
swap requires a chooser on both sides and that population is the chooser-poor one; the
reciprocity-bearing mechanisms are bound by the low-cooperation-cost population's,
because shedding machinery into unconditional cooperation is an escape that only costs
the system when the escaping side is the one carrying the cooperation. The sharpest
illustration is that an untaxed population can end up with fewer *active* choosers, and
a tenth of the cooperation, of the same population carrying a heavy tax itself. This
also makes equal information-cost budgets non-fungible and, more surprisingly,
non-convex: splitting a budget across both populations is worse than loading it entirely
onto either one, since each corner leaves one intact apparatus while a split leaves
none. The
dilemma-free control shows that none of this is an artefact of how the tax is charged —
without a social dilemma the tax has no cross-population channel at all, and machinery
loss tracks only the cost a population pays itself. The coupling is created by the
dilemma, not by the accounting.

## Limitations

- **Calibration is structural, not literal.** The payoff-plane calibration sweeps fix
  payoffs that slide with cooperation cost in the main sweeps, so the overlays
  identify which axis governs a mechanism, not absolute thresholds (see caveats in
  [synthesis](../journal/synthesis.md)).
- **Temporal resolution.** Single-run snapshots (t = 131072 onward) confirm that
  established role splits and collapsed cells are already in place at the first
  recorded time step across the per-population information-cost sweeps. They are too
  coarse, however, to resolve sub-establishment ordering or to rule out low-amplitude
  cycling within a snapshot interval.
- **Bistable cells report mixtures.** At the edge of the hitchhiking wedge the
  across-run standard deviation reaches 0.25, meaning runs settle in different
  attractors and the cell mean describes no single run. Cell means in that narrow band
  should be read as basin-occupancy fractions, not equilibrium levels; elsewhere the
  across-run spread is an order of magnitude smaller
  ([both costs asymmetric](../journal/asymmetric_c1_i0_i1.md)).
- **Evolving-vs-fixed control redundancy.** The three-population design in which one
  side does not evolve adds nothing over the equal-cooperation-cost baseline and is
  excluded from interpretation (regression-locked in
  [synthesis](../journal/synthesis.md) and ai/verify_claims.py).

## Future directions

Finer temporal logging to settle the oscillation question; a targeted cooperation-cost
sweep on the branch where one population's cost is fixed if we later want to test how
broadly the decoupling boundary generalizes; and fuller related-work positioning
around costly enforcement machinery.
