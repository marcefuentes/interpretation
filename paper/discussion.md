# Discussion

*Draft scaffold. Backing: [synthesis.md](../journal/synthesis.md),
[symmetric_c_i.md](../journal/symmetric_c_i.md),
[framework.md](../journal/framework.md).*

## What each mechanism is really limited by

Decoupling the payoff gaps turns three vague "collapses as cost rises" statements into
specific attributions: direct reciprocity is limited by risk (the cost of its own
punishment outcome, mutual defection), partner choice by the cooperation advantage
R − P (the fuel for assortment), and reputation-rich mechanisms by reward alone (they
ignore the defection baseline). This explains why the mechanisms rank as they do, why
snowdrift rescues reciprocity, and why the combined mechanisms break the ceilings that
bound M and P individually.

## Two populations: what the second one changes

The second population does not change the *dynamical regime* (both single and two
population cases settle into absorbing states, not cycles). What it changes is the
*outcome*: two populations can lock into a cooperator/exploiter role split. When the
populations are symmetric the split is a spontaneous symmetry breaking; when they
differ in cost it is seeded deterministically by the payoff asymmetry. In both, the
cooperating side is typically exploited — a robust paradox of success — and the
reward-led combined mechanisms are what soften it.

## Price versus demand for enforcement

Adding an information-cost axis reframes enforcement as supply and demand. The
cooperation cost c is the demand (temptation and risk the machinery must resist); the
information cost Cost is the price (a per-round tax escapable only by shedding the
machinery). Alone each is survivable; together they compound, because the price thins
the apparatus the demand requires. The striking consequence is that behaviour and
mechanism decouple: cooperation can persist through unconditional cooperators after
the expensive conditional machinery has been selected away — cooperation without
active enforcement, but only where the game does not punish it. The new
asymmetric_c1_i branch fixes the boundary of that result: once one population is
held at c0 = 0.10 and the second is costlier still, there is no harmless Cost edge,
so information cost retreats the c1 ceiling directly and compresses the
cooperator/exploiter split rather than merely changing the genotype route.

## Limitations

- **Calibration is structural, not literal.** The prisoners/snowdrift sweeps fix a
  payoff that slides with cost in diagonal, so the overlays identify which axis governs
  a mechanism, not absolute thresholds (see caveats in
  [synthesis.md](../journal/synthesis.md)).
- **Temporal resolution.** Single-run snapshots are too coarse to resolve
  sub-establishment ordering or to rule out low-amplitude cycling; we therefore treat
  temporal dynamics as an open question rather than a measured outcome. Testing it
  would require dense early-time logging.
- **pop_3 redundancy.** The evolving-vs-fixed structure adds nothing over the diagonal
  diagonal and is excluded from interpretation (shown, and regression-locked, in
  [synthesis.md](../journal/synthesis.md) and ai/verify_claims.py).

## Future directions

Finer temporal logging to settle the oscillation question; a targeted c0 sweep on
the asymmetric Cost branch if we later want to test how broadly the asymmetric_c1_i
boundary generalizes; and fuller related-work positioning around costly
enforcement machinery.
