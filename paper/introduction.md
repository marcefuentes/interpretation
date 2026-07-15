# Introduction

*Draft scaffold. Conceptual backing: [framework.md](../journal/framework.md).*

## The problem

Cooperation between unrelated individuals is costly to the actor and beneficial to a
partner, so it is vulnerable to defectors who take the benefit without paying the
cost. Several mechanisms are known to stabilise it: direct reciprocity (help those
who helped you), partner choice (leave defectors and re-pair with cooperators), and
indirect reciprocity (help those with a good reputation). What is less settled is how
these mechanisms compare when the same model is pushed across the conditions that
actually vary in nature — how hard the social dilemma is, how expensive cooperation
is, how expensive the enforcement machinery itself is, and the ecological setting of
group size and partner turnover.

## One population versus two

Most theory treats a single well-mixed population. Many biologically important cases
are mutualisms: two distinct populations (or species) that cooperate across the
divide, each with its own cost of helping. We treat the single population as the
baseline and the mutualistic two-population interaction as the central case, and ask what the
second population changes. The equal-cooperation-cost single-population case is the
c0 = c1 special case of the two-population design in which both sides carry the same
cooperation cost.

## What we set out to explain

We organise the study around three outcomes (see
[framework.md](../journal/framework.md)):

1. **The level of cooperation** — where each mechanism sustains cooperation and where
   it collapses as costs rise.
2. **Between-population asymmetry** — when two populations diverge into a cooperator
   and an exploiter, and which one profits (these need not be the same population).
   This is an **outcome** measure (gaps in cooperation and fitness), not a statement
   about how the model is parameterised.
3. **The genotype composition behind the behaviour** — which alleles actually produce
   the cooperation, and whether behaviour and enforcement machinery can come apart.

## Parameter symmetry versus outcome symmetry

Throughout, we keep two levels distinct. **Parameter symmetry** means the two
populations face the same setup: equal cooperation cost (c0 = c1), equal information
cost (i0 = i1), and identical payoffs. **Outcome symmetry** means realised cooperation
and fitness are similar between populations (small q and w gaps). Symmetric
parameters do **not** imply symmetric outcomes, and asymmetric outcomes can arise
without any built-in parameter tilt.

Under partner choice at equal costs, the outcome mapping is **game-dependent**.
In the prisoner's dilemma, partner choice produces a **stochastic** cooperator/exploiter
split that is absent under the no-machinery control (Fig. S6). In snowdrift, a similar
split already appears without enforcement machinery; partner choice mainly reshapes
outcomes at high cooperation cost. A cooperation-cost gap (c0 < c1) seeds a
**deterministic** cooperator/exploiter assignment. Asymmetric information cost at
equal cooperation cost (i0 ≠ i1) also yields a **deterministic** split under P — and
can **invert** it under combined reputation mechanisms — even though cooperation cost
remains parameter-symmetric. Which mapping applies depends on mechanism, game, and which
cost axes are tilted; snowdrift often removes locks that hold in the PD.

## Contribution

By sweeping an individual-based model across social dilemma, cooperation cost,
information cost (including per-population asymmetry i0 ≠ i1), group size, partner
shuffling, population structure, and mechanism,
and by adding two payoff-plane calibration sweeps that decouple the payoff gaps a
single cost axis welds together, we (i) attribute each mechanism's collapse to a
specific payoff gap, (ii) characterise how parameter symmetry and asymmetry map to
outcome splits between populations (stochastic PD split under partner choice at full
parameter symmetry, contrast Fig. 2 with Fig. S6; deterministic under cooperation-cost
or information-cost tilts; mechanism-dependent inversions), and (iii) introduce an
information-cost axis showing that taxing the
machinery erodes the apparatus while cooperation can persist through unconditional
cooperators — an information-cost versus cooperation-cost view of enforcement.
