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

**Background.** Cooperation is explained with enforcement mechanisms
(reciprocity, partner choice, reputation), but models treat the informational
machinery behind enforcement as free once it exists. I use *information cost* as
shorthand for fixed per-genotype overheads on that machinery — observing or
communicating others' behaviour, keeping it in memory, identifying individuals, and
making decisions — and not for variable costs such as punishment or sanctions. In
two-population mutualisms this omission matters, because the information cost paid
by one population can place a burden — or confer a benefit — on both populations,
not only the payer.

**Methods.** I used an individual-based evolutionary model that separates
cooperation cost (the payoff price of helping) from per-population information cost.
Information cost is charged per machinery family carried (choice family, reciprocity
family), so mechanisms are comparable in their cognitive bill. I varied game
structure (prisoner's dilemma, snowdrift), cooperation-cost and information-cost
asymmetry (each axis assigned independently to each population), ecology (group size,
shuffling), population structure (one vs two populations), and mechanism class, with
payoff-plane calibrations (Table S1) to attribute mechanism limits.

**Results.** The main finding is that a population often bears a larger burden from its
partner's information cost than from its own. When populations differ in cooperation
cost, that gap assigns cooperator and exploiter roles; when they differ in information
cost, that gap shifts those roles and inverts them only if the low-cooperation-cost
population pays near-zero information cost. Under partner choice, a population
cooperates if its partner can afford active choosers. Under reciprocity-bearing
mechanisms, the information cost paid by the low-cooperation-cost population can
burden its high-cost partner more than the payer, whereas the reverse direction is
weaker. This mechanism-specific difference explains why equal total information-cost
budgets are not interchangeable, and why both populations sharing a fixed total can
cooperate less than when one pays it all. Populations that cooperate more often earn
less fitness. Familiar one-population patterns (including shedding machinery when
cooperation cost is zero) still appear, but they miss the cross-population burden
under the prisoner's dilemma. Snowdrift and no-dilemma controls weaken these effects,
showing that they depend on genuine dilemma structure.

**Conclusions.** In mutualisms, paying an information cost and bearing its burden are
different questions. Because enforcement works through partner-dependent interactions,
ask which population bears the burden of an information cost, not only which population
pays it. Models that ignore this can misidentify both stability conditions and who
benefits from cooperation.
