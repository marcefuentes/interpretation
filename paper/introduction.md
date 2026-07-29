# Introduction

*Conceptual backing: [framework.md](../journal/framework.md). Citations resolve
against [references.bib](references.bib); see [citing.md](citing.md).*

## The problem

Cooperation between unrelated individuals is costly to the actor and beneficial to a
partner, so it is vulnerable to defectors who take the benefit without paying the cost
[@Hamilton1964; @WestGriffinGardner2007]. Several mechanisms can stabilise it when
encounters are structured: direct reciprocity (help those who helped you)
[@Trivers1971; @AxelrodHamilton1981; @Axelrod1984], partner choice (leave defectors
and re-pair with cooperators) [@BullRice1991; @NoeHammerstein1994; @Aktipis2004], and
indirect reciprocity or reputation (help those with a good standing)
[@NowakSigmund1998; @NowakSigmund2005; @LeimarHammerstein2001]. Comparative reviews
place these beside kinship and other routes to cooperation
[@Nowak2006; @LehmannKeller2006; @Sachs2004]. What remains less settled is how the
mechanisms compare when the same model is pushed across the conditions that actually
vary in nature — how hard the social dilemma is, how expensive cooperation is, how
expensive the enforcement machinery itself is, and the ecological setting of group
size and partner turnover.

## Related work

**Reciprocity and reputation.** Direct reciprocity works when partners interact
repeatedly and can condition on recent history [@Trivers1971; @Axelrod1984;
@NowakSigmund1992]. Indirect reciprocity extends conditioning to third-party
information and lifetime standing, at the price of greater cognitive and
informational demand [@NowakSigmund1998; @OhtsukiIwasa2004; @NowakSigmund2005].
Empirical and theoretical work on reputation shows that image scoring and related
rules can sustain public goods, but also that assessment strategies matter
[@MilinskiSemmannKrambeck2002; @LeimarHammerstein2001].

**Partner choice and biological markets.** When individuals can choose or switch
partners, cooperators can assort without remembering a long personal history
[@BullRice1991; @NoeHammerstein1994; @NoeHammerstein1995]. Walk-away and choosiness
models make the same point in evolutionary games [@Aktipis2004;
@McNamaraBartaHouston2004]. In interspecific mutualisms, partner choice and sanctions
are among the main proposed stabilisers [@Bronstein1994; @Sachs2004;
@Kiers2003; @BsharyGrutter2006].

**One population versus two.** Most formal theory treats a single well-mixed
population. Many biologically important cases are mutualisms: two distinct
populations or species that exchange help across the divide, each with its own cost
of cooperating [@DoebeliKnowlton1998; @BergstromLachmann2003; @Sachs2004]. Relative
evolutionary rates and cost asymmetries can then assign roles even when the
interaction is mutually beneficial. We treat the single population as the baseline
and the mutualistic two-population interaction as the central case.

**The cost of enforcement.** Models usually treat reciprocity, partner choice, and
reputation as free once the loci or strategies are present. That is an idealisation.
Enforcement machinery carries fixed costs — observing or communicating others'
behaviour, keeping it in memory, identifying individuals, and making decisions. We use
*information cost* as shorthand for these per-genotype overheads throughout the paper,
and not for variable costs such as punishment or sanctions. Sanctioning and monitoring
are themselves public-goods problems: second-order free riders enjoy the benefits of
enforcement without paying for it
[@Yamagishi1986; @BoydRicherson1992; @PanchanathanBoyd2004], and altruistic
punishment is costly to the punisher [@FehrGachter2002; @BoydGintisBowles2003;
@SigmundHauertNowak2001]. Cognitive and psychological constraints further limit how
much conditional behaviour animals can sustain [@StevensHauser2004; @Dunbar1998],
and maintaining the required informational or learning machinery carries direct
metabolic and fitness costs even outside primates [@MeryKawecki2003].
These literatures establish that enforcement is not free, but they typically place
the cost on individuals *within* one population. They do not ask whether the burden
created by one population's information cost can fall mainly on its partner when two
populations interact and each pays its own cognitive bill.

**Dilemma structure.** Whether cooperation is a prisoner's dilemma or a snowdrift
(chicken) game changes both the baseline incentive to help and which mechanisms can
rescue it [@HauertDoebeli2004; @DoebeliHauert2005]. We keep both games in view so that
claims about information costs can be separated from claims about payoff structure.

## Gap and approach

Two distinctions organise the present study (see
[framework.md](../journal/framework.md)).

First, **cooperation cost** versus **information cost**. Cooperation cost is the
payoff price of helping — temptation and risk in the game. Information cost, as
defined above, is the fixed per-genotype overhead charged for carrying enforcement
loci in the model (a per-round metabolic or cognitive bill, not contingent on
per-round behaviour). Alone,
each pressure is often survivable; together they compound, because information cost
thins the apparatus that resists temptation. On a symmetric information-cost design,
that thinning can look like a local escape: active machinery is selected out while
cooperation persists through tax-free unconditional cooperators, decoupling behaviour
from mechanism. Decoupling sits close to established second-order free-rider results
[@Yamagishi1986; @PanchanathanBoyd2004]. What a symmetric design *cannot* do is
separate the cost a population pays from the burden that cost creates for its partner.

Second, **parameter symmetry** versus **outcome symmetry**. Parameter symmetry means
the two populations face the same setup (equal cooperation cost, equal information
cost, identical payoffs). Outcome symmetry means realised cooperation and fitness are
similar between them. Symmetric parameters do not imply symmetric outcomes: partner
choice at equal costs can produce a stochastic cooperator/exploiter split, and cost
asymmetries can pin or invert that split depending on mechanism and game. Because
each population carries its own cooperation cost and information cost, both axes
can be varied independently and their relative roles compared.

Prior work on asymmetric **cooperation costs** in mutualisms shows that unequal costs
or evolutionary rates can assign cooperator and exploiter roles
[@DoebeliKnowlton1998; @BergstromLachmann2003], but rarely with explicit enforcement
machinery or an independent information-cost axis. To our knowledge, no model varies
**per-population information cost** in coevolving mutualists and asks which partner
bears the burden of enforcement: cognitive-cost and punishment studies are largely
within-population or do not separate the cost a population pays from the burden that
cost creates for its partner.

We therefore vary an individual-based model across social dilemma, cooperation cost,
per-population information cost, group size, partner shuffling, population structure,
and mechanism, and add orthogonal payoff-plane calibration analyses that decouple the
payoff gaps a single cooperation-cost axis welds together. The single-population
equal-cost case is the baseline; the two-population case with independently assigned
costs is the primary biological scenario.

## Contribution

The central result is that **the burden created by information cost often does not
stay with the payer**. Enforcement machinery is itself costly, and because it
operates *between* populations, one population's information cost can determine the
cooperation of both — which population matters most depends on the mechanism family.
Under partner choice a population is nearly insensitive to its own information cost
and collapses under its partner's, because assortment needs active choosers on both
sides. Reciprocity-bearing mechanisms protect only their carriers, so raising the
information cost paid by the low-cooperation-cost population can impose a larger
burden on its partner than on the payer. Removing the social dilemma removes this
coupling, identifying it as a property of the dilemma rather than of the accounting.
Throughout, cooperation-cost asymmetry remains the default role assigner;
information-cost asymmetry mostly modulates that baseline and inverts roles only when
the low-cooperation-cost population's information cost is near zero.

Two consequences follow. Equal enforcement budgets are neither fungible nor additive:
splitting a budget across both populations yields less total cooperation than loading
it on either one. And the escape route that makes information cost survivable under
symmetry — shedding the machinery into unconditional cooperation — is what makes it
destructive under asymmetry, because relieving the payer withdraws the service the
partner depended on. Supporting this, we attribute each mechanism's cooperation-cost
collapse to a specific payoff gap (reciprocity risk-limited, partner choice limited by
the cooperation advantage, reputation-rich mechanisms reward-limited), and show that
when both cost axes differ the cooperation-cost gap remains the default role assigner,
with information cost inverting roles only in a thin near-zero-i₀ regime that vanishes under
snowdrift.
