# Summary

*Draft publication summary. Numbers and derivations: journal/ (regression-checked by
ai/verify_claims.py).*

## Background

Cooperation between unrelated individuals is vulnerable to exploitation unless
enforcement — direct reciprocity, partner choice, or reputation-based mechanisms —
stabilises it. Models typically treat that enforcement machinery as free, and most
theory focuses on a single well-mixed population. In many mutualisms, however, two
distinct populations interact, each with its own cost of helping, and both
cooperation and the cognitive apparatus that sustains it may carry separate costs. It
remains unclear how mechanism choice, cooperation level, between-population asymmetry,
and the genotypes that produce cooperation respond jointly when the social dilemma,
cooperation cost, information cost, and ecological context all vary.

## Methods

We use an individual-based evolutionary model in which agents play repeated pairwise
games, reproduce in proportion to accumulated fitness, and evolve cooperation and
mechanism loci (partner choice, direct and indirect reciprocity, and lifetime
reputation). Information cost is charged per family of loci carried — once for
partner choice, once for reciprocity — so every mechanism owes zero, one or two
units of it regardless of how many loci it enables, which makes mechanisms directly
comparable in what they pay. We sweep cooperation cost, information cost,
dilemma type (prisoner's dilemma and snowdrift), group size, partner shuffling, and
one- versus two-population structure. The single-population equal-cost case provides a
baseline; the two-population case with distinct costs is the primary biological
scenario. Orthogonal payoff-plane calibration sweeps (not shown) identify which payoff
gap limits each mechanism's cost threshold.

## Results

Each enforcement architecture sustains cooperation only up to a characteristic cost
threshold. Direct reciprocity is limited by mutual-defection risk; partner choice by
the cooperation advantage R − P; reputation-rich combined mechanisms by reward alone
and tolerate the highest costs. With two populations, partner choice frequently
produces a cooperator/exploiter role split in which the cooperating side earns less —
the paradox of success. We distinguish parameter symmetry in the setup (equal costs
and payoffs) from outcome symmetry (similar cooperation and fitness): symmetric
parameters do not require symmetric outcomes. Under partner choice, equal costs yield
a stochastic split; a cooperation-cost gap yields a deterministic one. Asymmetric
information cost at equal cooperation cost also assigns roles deterministically (and
can invert them under combined reputation mechanisms). Reward-led combined mechanisms
suppress outcome asymmetry by lifting the exploited population.

Making the machinery itself costly introduces a trade-off between information cost
and cooperation cost. Cooperation cost sets the temptation and risk the apparatus
must resist; information cost is escapable only by shedding the machinery, and only
by shedding a whole family of it at once, since dropping part of a family saves
nothing. Alone each pressure is mild; together they compound, because information
cost thins the defence cooperation cost requires. On the symmetric branch,
information cost erodes enforcement alleles while cooperation can persist through
tax-free unconditional cooperators: behaviour and mechanism decouple. Once one
population is held at nonzero cooperation cost and the second is costlier still,
that refuge at zero cooperation cost disappears — information cost retreats the
cooperation ceiling directly and compresses the cooperator/exploiter split rather
than merely changing the genotype route.

When cooperation cost is parameter-symmetric (c0 = c1) but information cost differs
(i0 ≠ i1), partner choice deterministically assigns the cooperator role to the side
with lower information cost — unlike the stochastic split at i0 = i1 — while combined
reputation mechanisms can invert that assignment via cross-population hitchhiking.
When both cooperation cost and information cost differ between populations, the
built-in cooperation-cost gap is the default role assigner: partner
choice favours the population with lower cooperation cost in almost every cell, and
the hitchhiking inversion survives only in a thin i0 ≈ 0 wedge. What decides whether
a mechanism can be inverted at all is the presence of reciprocity rather than the
information cost it pays: among mechanisms paying identical amounts, only the
reciprocity-bearing ones invert. Single-run trajectories confirm that these role
splits lock in by the first recorded snapshot rather than eroding slowly.

Separating the cost a population pays from the cost its partner pays — which only
the full two-dimensional design allows — shows that information cost acts as a
relational rather than a private burden. Under partner choice a population is nearly
insensitive to its own information cost and collapses under its partner's, because
the exchange requires an active chooser on both sides and is limited by whichever
population supplies fewer. Equal information-cost budgets are therefore neither
fungible nor additive: for every reciprocity-bearing mechanism, splitting a budget
across both populations yields less total cooperation than loading the whole of it
onto either one, since each extreme leaves one population with an intact apparatus
while a split breaks both. Removing the social dilemma removes the cross-population
channel entirely, identifying the coupling as a property of the dilemma rather than
of the cost accounting.

## Conclusions

Cooperation outcomes are jointly shaped by which enforcement mechanism operates, how
costly cooperation and the machinery are, and whether one or two populations
coevolve. Parameter symmetry in the setup does not imply outcome symmetry between
populations. Partner choice is the mechanism most closely tied to between-population
outcome asymmetry: it creates or amplifies a role split that combined reputation-rich
mechanisms partially undo. Treating enforcement as costly reframes cooperation around
two separable costs and reveals that decoupling of behaviour from mechanism is real
but bounded — it requires a refuge where shedding the apparatus is not punished by
the game. The cost of enforcement is also not borne where it is levied: because
mechanisms operate between populations, the burden that limits a population is
frequently the one its partner carries, so the total cost of enforcement in a
mutualism is a poor guide to its outcome and its distribution is the informative
quantity. These results link mechanism attribution, exploitation asymmetry, and the
economics of enforcement in a single sweepable framework.
