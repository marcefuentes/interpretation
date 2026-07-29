# Summary

**Internal planning document** — structured abstract for drafting. **Not** American
Naturalist format (Am Nat requires a single ≤200-word narrative abstract in
[paper/submission/amnat/abstract.md](../paper/submission/amnat/abstract.md)).

Submission bundle: [paper/README.md](../paper/README.md). Planning:
[planning/README.md](../planning/README.md). Numbers: journal/ (regression-checked by
`ai/verify_claims.py`).

## Title

Canonical submission title: [paper/submission/amnat/title-page.md](../paper/submission/amnat/title-page.md).

## Structured abstract

**Background.** Cooperation is often explained with enforcement mechanisms
(reciprocity, partner choice, reputation), but models usually treat the informational
machinery behind enforcement as free once it exists. We use *information cost* as
shorthand for fixed per-genotype overheads on that machinery — observing or
communicating others' behaviour, keeping it in memory, identifying individuals, and
making decisions — and not for variable costs such as punishment or sanctions. In
two-population mutualisms this omission is especially consequential, because the same
information cost can affect both populations, not only the one that pays it.

**Methods.** We used an individual-based evolutionary model that separates
cooperation cost (the payoff price of helping) from per-population information cost.
Information cost is charged per machinery family carried (choice family, reciprocity
family), so mechanisms are directly comparable in their cognitive bill. We varied game
structure (prisoner's dilemma, snowdrift), cooperation-cost and information-cost
asymmetry (each axis assigned independently to each population), ecology (group size,
shuffling), population structure (one vs two populations), and mechanism class, with
payoff-plane calibrations (Table S1) to attribute mechanism limits.

**Results.** The main finding is that how a population behaves often depends more on
its partner's information cost than on its own. Cooperation-cost asymmetry remains the
primary role assigner across mechanisms; information-cost asymmetry mostly modulates
that baseline, and role inversion appears only when the low-cooperation-cost
population's information cost is near zero. Under partner choice, cooperation is set
mainly by whether the partner population can afford enough active choosers. Under
reciprocity-bearing mechanisms, the cross-population burden becomes asymmetric: it is
specifically the information cost paid by the low-cooperation-cost population that can
damage its high-cost partner more than the payer, whereas the reverse direction is
weaker. This mechanism-specific difference explains why equal total information-cost
budgets are not equivalent to different allocations of the same budget, and why
splitting a fixed total between populations can be worse than concentrating it on one
side. Cooperation and fitness repeatedly decouple: the more cooperative population is
often the less fit one. Familiar one-population patterns (including machinery
shedding when cooperation cost is zero) still appear, but they miss the cross-population
burden that dominates in two-population prisoner's dilemma interactions. Snowdrift and
no-dilemma controls weaken these effects, showing that they depend on genuine dilemma
structure.

**Conclusions.** In mutualisms, enforcement is not just a property of the population
that pays for it. Because enforcement works through partner-dependent interactions,
the decisive variable is often how the burden created by information costs is
distributed across populations, not only the size of those costs. Models that ignore
this can misidentify both stability conditions and who benefits from cooperation.
