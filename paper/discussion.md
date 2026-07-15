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
*outcome*: two populations can lock into a cooperator/exploiter role split. When the
populations are symmetric the split is a spontaneous symmetry breaking; when they
differ in cooperation cost it is seeded deterministically by the payoff asymmetry. In
both, the cooperating side is typically exploited — a robust paradox of success — and
the reward-led combined mechanisms are what soften it.

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

**Which cost assigns roles?** When cooperation cost is symmetric but information cost
differs between populations, per-population information-cost asymmetry alone can assign
or invert the role split depending on mechanism — partner choice to the side with
lower information cost, IJMPQ inverted via hitchhiking. When both cooperation cost and
information cost differ, the cooperation-cost gap is the default role assigner (partner
choice: the lower-cooperation-cost population cooperates more in 170/176 cells), and
the hitchhiking inversion survives only on an i0 ≈ 0 strip (13 cells), attenuated
relative to the symmetric-cooperation-cost case. Snowdrift removes the wedge entirely.
Cooperation cost therefore sets the baseline; information cost can locally override
combined mechanisms only where the population with lower cooperation cost pays no
information cost.

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
- **Evolving-vs-fixed control redundancy.** The three-population design in which one
  side does not evolve adds nothing over the equal-cooperation-cost baseline and is
  excluded from interpretation (regression-locked in
  [synthesis](../journal/synthesis.md) and ai/verify_claims.py).

## Future directions

Finer temporal logging to settle the oscillation question; a targeted cooperation-cost
sweep on the branch where one population's cost is fixed if we later want to test how
broadly the decoupling boundary generalizes; and fuller related-work positioning
around costly enforcement machinery.
