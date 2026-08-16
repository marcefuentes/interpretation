# Discussion

*Backing: [synthesis](../journal/synthesis.md) and linked journal analyses
(regression-checked by `ai/verify_claims.py`). Citations:
[references.bib](references.bib).*

## What each mechanism is really limited by

Decoupling the payoff gaps turns three vague "collapses as cost rises" statements into
specific attributions: direct reciprocity is limited by risk (the cost of its own
punishment outcome, mutual defection), partner choice by the cooperation advantage
R − P (the fuel for assortment), and reputation-rich mechanisms by reward alone (they
ignore the defection baseline). This ranking is consistent with the classical contrast
between memory-based reciprocity and market-like partner choice
[@Trivers1971; @NoeHammerstein1994; @Nowak2006], and with the finding that snowdrift
payoffs raise the cooperation floor relative to the prisoner's dilemma
[@HauertDoebeli2004; @DoebeliHauert2005]. It also explains why combined
reputation-rich mechanisms break the ceilings that bound M and P individually: once
reward leads, the defection baseline stops setting the collapse.

## Two populations: what the second one changes

The second population does not change the *dynamical regime* (both single- and two-
population cases settle into absorbing states, not cycles). What it changes is the
*outcome*: two populations can lock into cooperator and exploiter roles even when
their parameters match — spontaneous symmetry breaking. While recently demonstrated
in spatial models with little dispersal [@HauertSzabo2024], and expected when costs
or rates differ [@DoebeliKnowlton1998; @BergstromLachmann2003], here populations
split even under full parameter symmetry via partner choice.

I separate **parameter symmetry** (c₀ = c₁, i₀ = i₁, identical payoffs) from
**outcome symmetry** (similar cooperation and fitness). At matched parameters,
partner-choice populations stochastically split in the prisoner's dilemma (Fig. 1).
When one population pays a lower cooperation cost, that population cooperates and the
other exploits (Fig. 2). I omit a parallel asymmetric snowdrift figure because
populations already cooperate and diverge without enforcement when the sucker payoff
is high (Fig. 1 and Fig. S3). When populations differ only in information cost,
partner choice still locks roles, while IJMPQ can invert them; snowdrift removes these
PD locks. In all cases the more cooperative population earns less fitness, and
reward-led combined mechanisms shrink that gap.

## Information cost versus cooperation cost

Adding an information-cost axis reframes enforcement around two costs. Cooperation
cost sets the temptation and risk the machinery must resist; information cost is
escapable only by shedding the machinery. Alone each is survivable; together they
compound, because information cost thins the apparatus cooperation cost requires.
The genotype-level consequence is that behavior and mechanism decouple:
cooperation can persist through unconditional cooperators after the expensive
conditional machinery has been selected away — but only where the game does not
punish that shed. That pattern is the evolutionary counterpart of second-order free
riding on enforcement [@Yamagishi1986; @PanchanathanBoyd2004; @BoydGintisBowles2003]:
carriers of tax-free unconditional cooperation enjoy assortment or punishment supplied
by others. Once one population sits above zero cooperation cost and the second is
costlier still, populations cannot shed machinery for free at zero cooperation cost,
so as information cost rises they cooperate less and the cooperator/exploiter gap
shrinks instead of only changing which genotypes carry the help.

**Which cost assigns roles?** When c₀ = c₁ but i₀ ≠ i₁, populations that differ only
in information cost still lock or invert roles depending on mechanism (Fig. S11).
When both cost axes differ, populations follow the cooperation-cost gap
(partner choice: the lower-cooperation-cost population cooperates more in 170/176
cells), and hitchhiking inversion survives only on an i₀ ≈ 0 strip (Fig. 5),
weaker than in the equal-c case. Snowdrift removes this regime entirely.
What decides whether a mechanism can be overridden at all is whether populations
carry the reciprocity family, not how large an information bill they pay — a controlled
comparison the per-family tax makes possible, because direct reciprocity and partner
choice pay identically, as do the four combined mechanisms among themselves.

## Cost versus burden across populations

The crossed design separates the cost a population pays from the burden that cost
places on its partner — a question prior work on costly punishment and monitoring
could not ask, because it levies those costs inside one population
[@BoydRicherson1992; @FehrGachter2002; @StevensHauser2004]. Under each mechanism,
both populations bear a burden from one population's information cost, and the two
mechanism families place that burden on opposite populations (Fig. 4a,b,d,e). Under
partner choice, populations bear the burden of the high-cooperation-cost population's
information cost, because a swap needs a chooser on both sides and that population
supplies fewer choosers; under reciprocity-bearing mechanisms, populations bear the
burden of the low-cooperation-cost population's information cost, because shedding
into unconditional cooperation hurts the pair only when the escaping side carries the
cooperation. The clearest case is that an untaxed population can end up with fewer
*active* choosers, and a tenth of the cooperation, of the same population when it
pays a heavy tax itself.

Equal information-cost budgets are therefore neither fungible nor additive (Fig. 4c,f):
both populations share a budget worse than either paying it alone, since each corner
leaves one intact apparatus while a split leaves none.
The dilemma-free control shows that none of this is an artefact of how the tax is
charged — without a social dilemma neither population bears a burden from its
partner's cost, and each sheds machinery only as it pays itself (Fig. S8). Populations couple
through the dilemma, not through the accounting. In that sense the headline result
extends the second-order free-rider literature rather than replacing it: when
individuals shed local enforcement costs, partners across the mutualism can bear the
burden of losing the service those costs once bought.
One consequence is that, in the threshold hitchhiking regime, a population can receive
a benefit from a partner that pays higher information cost, because that partner is
pushed into a more cooperative but less fit state.

## Limitations

- **Calibration is structural, not literal.** The payoff-plane calibration analyses fix
  payoffs that slide with cooperation cost in the main analyses, so the overlays
  identify which payoff variable governs a mechanism, not absolute thresholds (see caveats in
  [synthesis](../journal/synthesis.md)).
- **Temporal resolution.** Single-run snapshots (t = 131072 onward) confirm that
  established role splits and collapsed cells are already in place at the first
  recorded time step. They are too coarse to resolve sub-establishment ordering or to
  rule out low-amplitude cycling within a snapshot interval.
- **Bistable cells report mixtures.** At the edge of the near-zero-i₀ hitchhiking regime the
  across-run standard deviation reaches 0.25, so the cell mean describes no single
  run. Cell means in that narrow band should be read as basin-occupancy fractions, not
  equilibrium levels ([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

- **Cognitive cost is abstracted.** Information cost is a per-family metabolic tax, not
  a process model of memory, perception, or error [@StevensHauser2004; @Dunbar1998].
  That abstraction is what makes mechanisms comparable; it is also a limit on
  psychological realism.

## Future directions

Finer temporal logging to settle the oscillation question; explicit error-prone
perception or reputation updating on top of the per-family tax; and extensions to
mutualisms in which the two sides differ in generation time or group size as well as
in cost [@BergstromLachmann2003; @BsharyGrutter2006]. The relational-budget result
also suggests a practical question: when enforcement is shared across partners, does
concentrating cognitive investment outperform splitting it?
