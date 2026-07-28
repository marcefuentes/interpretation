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
*outcome*: two populations can lock into a cooperator/exploiter role split even when
their parameters match — spontaneous symmetry breaking. While recently demonstrated
in spatial models assuming almost no dispersal [@HauertSzabo2024], and expected when
costs or rates differ [@DoebeliKnowlton1998; @BergstromLachmann2003], here it emerges
even under full parameter symmetry in mixed populations via partner choice.

We separate **parameter symmetry** (c₀ = c₁, i₀ = i₁, identical payoffs) from
**outcome symmetry** (similar cooperation and fitness). Partner choice at parameter
symmetry produces a stochastic outcome split in the prisoner's dilemma (Fig. 1). A
cooperation-cost gap seeds a deterministic assignment (Fig. 2). We omit a parallel
asymmetric snowdrift figure because the sucker payoff already sustains cooperation and
between-population splits without enforcement (Fig. 1 and Fig. S1). Information-cost
asymmetry at equal cooperation cost also assigns roles deterministically under P, while
IJMPQ can invert the mapping; snowdrift often removes these PD locks. In all cases the
more cooperative side is typically the less fit one, and reward-led combined
mechanisms soften the outcome gap.

## Information cost versus cooperation cost

Adding an information-cost axis reframes enforcement around two costs. Cooperation
cost sets the temptation and risk the machinery must resist; information cost is
escapable only by shedding the machinery. Alone each is survivable; together they
compound, because information cost thins the apparatus cooperation cost requires.
The striking genotype-level consequence is that behaviour and mechanism decouple:
cooperation can persist through unconditional cooperators after the expensive
conditional machinery has been selected away — but only where the game does not
punish that shed. That pattern is the evolutionary counterpart of second-order free
riding on enforcement [@Yamagishi1986; @PanchanathanBoyd2004; @BoydGintisBowles2003]:
carriers of tax-free unconditional cooperation enjoy assortment or punishment supplied
by others. Once one population is held above zero cooperation cost and the second is
costlier still, there is no harmless information-cost edge at zero cooperation cost,
so information cost retreats the cooperation-cost ceiling directly and compresses the
cooperator/exploiter split rather than merely changing the genotype route.

**Which cost assigns roles?** When c₀ = c₁ but i₀ ≠ i₁, per-population information-cost
asymmetry alone assigns or inverts the role split depending on mechanism (Fig. S6).
When both cost axes differ, the cooperation-cost gap is the default outcome assigner
(partner choice: the lower-cooperation-cost population cooperates more in 170/176
cells), and the hitchhiking inversion survives only on an i₀ ≈ 0 strip (Fig. 5),
attenuated relative to the equal-c case. Snowdrift removes this regime entirely.
What decides whether a mechanism can be overridden at all is the presence of the
reciprocity family rather than the size of the information bill it pays — a controlled
comparison the per-family tax makes possible, because direct reciprocity and partner
choice pay identically, as do the four combined mechanisms among themselves.

## The information cost of enforcement can burden both populations

The crossed design separates the cost a population pays from the burden that cost
creates for its partner — a question prior work on costly punishment and monitoring
could not ask, because it levies those costs inside one population
[@BoydRicherson1992; @FehrGachter2002; @StevensHauser2004]. Each mechanism turns out
to depend mainly on one population's information cost, for both populations at once,
and the two mechanism families depend on opposite populations (Fig. 4a,b,d,e).
Partner choice depends mainly on the high-cooperation-cost population's information cost,
because a swap requires a chooser on both sides and that population is the
chooser-poor one; the reciprocity-bearing mechanisms depend mainly on the
low-cooperation-cost population's information cost, because shedding into unconditional cooperation
only costs the system when the escaping side carries the cooperation. The sharpest
illustration is that an untaxed population can end up with fewer *active* choosers,
and a tenth of the cooperation, of the same population carrying a heavy tax itself.

Equal information-cost budgets are therefore neither fungible nor additive (Fig. 4c,f):
splitting a budget across both populations is worse than loading it entirely onto
either one, since each corner leaves one intact apparatus while a split leaves none.
The dilemma-free control shows that none of this is an artefact of how the tax is
charged — without a social dilemma the tax has no cross-population effect, and
machinery loss tracks only the cost a population pays itself (Fig. S4). The coupling
is created by the dilemma, not by the accounting. In that sense the headline result
extends, rather than replaces, the second-order free-rider literature: decoupling is
the process by which a cost that looks local in one population becomes a burden shared
across populations once enforcement is a between-population service.
One consequence is that, in the threshold hitchhiking regime, a population can gain
fitness from interacting with a partner whose information cost is higher, because the
partner is pushed into a more cooperative but less fit state.

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
- **Evolving-vs-fixed control redundancy.** The design in which one side does not
  evolve adds nothing over the equal-cooperation-cost baseline and is excluded from
  interpretation ([synthesis](../journal/synthesis.md)).
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
