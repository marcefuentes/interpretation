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
mechanisms compare when the same model faces the conditions that vary in nature —
how hard the social dilemma is, how expensive cooperation is, how expensive the
enforcement machinery itself is, and the ecological setting of group size and
partner turnover.

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
interaction is mutually beneficial. I treat the single population as the baseline
and the mutualistic two-population interaction as the central case.

**The cost of enforcement.** Models treat reciprocity, partner choice, and
reputation as free once the loci or strategies are present. That is an idealisation.
Enforcement machinery carries fixed costs — observing or communicating others'
behaviour, keeping it in memory, identifying individuals, and making decisions. I use
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
These literatures establish that enforcement is not free, but they place the cost
on individuals *within* one population. They do not ask whether an information cost
paid by one population can place a burden — or confer a benefit — on its partner.

**Dilemma structure.** Whether cooperation is a prisoner's dilemma or a snowdrift
(chicken) game changes both the baseline incentive to help and which mechanisms can
rescue it [@HauertDoebeli2004; @DoebeliHauert2005]. I keep both games in view so that
claims about information costs can be separated from claims about payoff structure.

## Gap and approach

Three distinctions organise the present study (see
[framework.md](../journal/framework.md)).

First, **cooperation cost** versus **information cost**. Cooperation cost is the
payoff price of helping — temptation and risk in the game. Information cost, as
defined above, is the fixed per-genotype overhead charged for carrying enforcement
loci in the model (a per-round metabolic or cognitive bill, not contingent on
per-round behaviour). Alone, each pressure is survivable; together they compound,
because information cost thins the apparatus that resists temptation. On a symmetric
information-cost design,
that thinning can look like a local escape: active machinery is selected out while
cooperation persists through tax-free unconditional cooperators, decoupling behaviour
from mechanism. Decoupling sits close to established second-order free-rider results
[@Yamagishi1986; @PanchanathanBoyd2004]. What a symmetric design *cannot* do is
separate the cost a population pays from the burden that cost places on its partner.

Second, **cost** versus **burden**. A cost is the parameter a population pays — `c`
or `i`. The burden (or benefit) is the effect of that cost on outcomes: cooperation
or fitness in either population. Population 0 can pay `i₀` while population 1 bears
much of the burden; the reverse can also occur, and sometimes the same cost benefits
a partner. Paying a cost and bearing its burden are therefore different questions.

Third, **parameter symmetry** versus **outcome symmetry**. Parameter symmetry means
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
machinery or an independent information-cost axis. To my knowledge, no model varies
**per-population information cost** in coevolving mutualists and asks which partner
bears the burden of that cost: cognitive-cost and punishment studies are
within-population or do not separate the cost a population pays from the burden that
cost places on its partner.

I therefore vary an individual-based model across social dilemma, cooperation cost,
per-population information cost, group size, partner shuffling, population structure,
and mechanism, and add orthogonal payoff-plane calibration analyses that decouple the
payoff gaps a single cooperation-cost axis welds together. The single-population
equal-cost case is the baseline; the two-population case with independently assigned
costs is the primary biological scenario.

## Contribution

The central result is that **the burden of an information cost need not fall on the
population that pays it**. Enforcement machinery is itself costly, and because it
operates *between* populations, the information cost paid by one population can place
a burden on both — which population bears more of that burden depends on the
mechanism family.
Under partner choice a population barely changes when it pays more information cost,
but collapses when its partner does, because assortment needs active choosers on both
sides. Reciprocity-bearing mechanisms protect only their carriers, so when the
low-cooperation-cost population pays a higher information cost, its partner can bear
a larger burden than the payer. Remove the social dilemma and populations no
longer couple this way: the coupling belongs to the dilemma, not to the accounting.
Throughout, populations that differ in cooperation cost keep their cooperator and
exploiter roles; populations that differ in information cost shift those roles and
invert them only when the low-cooperation-cost population pays near-zero information
cost.

Two consequences follow. Equal enforcement budgets are neither fungible nor additive:
when both populations share a budget they cooperate less in total than when either
one pays it alone. And the escape that lets a population survive information cost under
symmetry — shedding machinery into unconditional cooperation — is what destroys the
partner under asymmetry, because the payer stops supplying the service the partner
needed. Supporting this, I attribute each mechanism's cooperation-cost collapse to a
specific payoff gap (reciprocity risk-limited, partner choice limited by the
cooperation advantage, reputation-rich mechanisms reward-limited), and show that when
both cost axes differ, populations still follow the cooperation-cost gap unless the
low-cooperation-cost population pays near-zero information cost — a thin regime that
vanishes under snowdrift.
