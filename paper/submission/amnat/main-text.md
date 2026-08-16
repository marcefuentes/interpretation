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
behavior, keeping it in memory, identifying individuals, and making decisions. I use
*information cost* as shorthand for these per-genotype overheads throughout the paper,
and not for variable costs such as punishment or sanctions. Sanctioning and monitoring
are themselves public-goods problems: second-order free riders enjoy the benefits of
enforcement without paying for it
[@Yamagishi1986; @BoydRicherson1992; @PanchanathanBoyd2004], and altruistic
punishment is costly to the punisher [@FehrGachter2002; @BoydGintisBowles2003;
@SigmundHauertNowak2001]. Cognitive and psychological constraints further limit how
much conditional behavior animals can sustain [@StevensHauser2004; @Dunbar1998],
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
per-round behavior). Alone, each pressure is survivable; together they compound,
because information cost thins the apparatus that resists temptation. On a symmetric
information-cost design,
that thinning can look like a local escape: active machinery is selected out while
cooperation persists through tax-free unconditional cooperators, decoupling behavior
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


# Methods

*Constants and payoff equations:
[parameterization](../journal/parameterization.md). Design grid and outcome
definitions: [framework](../journal/framework.md). Numbers cited elsewhere in the
manuscript are regression-checked by `ai/verify_claims.py`.*

## Model

I use an individual-based evolutionary model. Individuals live in fixed groups,
interact in pairs over repeated rounds, and reproduce in proportion to accumulated
fitness. Mutation rate is 0.01 per locus per reproduction event. Each individual
carries six loci: a cooperation locus C and five mechanism loci that control
conditional behavior — partner choice on recent (P) or lifetime (Q) cooperation, and
reciprocity that copies a partner's recent act directly (M), indirectly from a third
party (I), or from a lifetime reputation (J). Each locus is binary — C1 helps its
partner, C0 defects; M1 copies its partner, M0 does not; and so on. An individual
behaves according to decision precedence Q1 > P1, and J1 > I1 > M1 when more than one
mechanism allele is carried. Per round, fitness is the game payoff minus information
cost, w = max(0, payoff − cost).

Under partner choice, assortment is a bilateral swap: two active choosers (C1P1)
mutually rematch, each trading a non-cooperative partner for the other chooser; the
two abandoned partners end up paired with each other. The partner-choice allele is
phenotypically silent in defectors (C0P1 carries P1 but never chooses). Reciprocity is
not silent in the same way — C0M1 still mimics once a partnership is established.
Mechanisms differ in which behaviors are enabled, not in which loci can mutate: under
the no-enforcement control (_), partner choice and reciprocity do not run, but mechanism
loci still mutate and still incur information cost when carried.

## Social dilemmas

Baseline fitness K = 0.5 and benefit b = 0.4 are fixed; cooperation cost c is swept
from 0 to b ([parameterization](../journal/parameterization.md)). The three payoff
structures are:

- **Control (no social dilemma):** An individual's payoff does not depend on its partner's behavior.
- **Prisoner's dilemma:** Delivers benefit b to the partner.
- **Snowdrift:** Treats b as a shared resource received whenever at least one player cooperates.

| Game Structure           | T (Temptation) | R (Reward)  | P (Penalty) | S (Sucker) | T − R (Temptation gap) | P − S (Risk)  | R − P (Cooperation advantage)  |
| ------------------------ | -------------- | ----------- | ----------- | ---------- | ---------------------- | ------------- | ------------------------ |
| **Control (No dilemma)** | K              | K + b − c   | K           | K + b − c  | c − b (rises)          | c − b (rises) | b − c (shrinks)          |
| **Prisoner's dilemma**   | K + b          | K + b − c   | K           | K − c      | c (rises)              | c (rises)     | b − c (shrinks)          |
| **Snowdrift**            | K + b          | K + b − c/2 | K           | K + b − c  | c/2 (rises slowly)     | c − b (rises) | b − c/2 (shrinks slowly) |

In the two-population form each population pays its own cooperation cost (c₀, c₁), with c₀ < c₁ in every asymmetric cell, so the lower-cost population always has the larger R − P.

## Information cost

Information cost is charged every round on the *families* of mechanism loci carried,
not per locus and not on machinery used:

cost = i × ( (P ∨ Q) + (M ∨ I ∨ J) ).

An individual therefore owes 0, 1 or 2 units of i. Carrying both partner-choice loci
costs the same as carrying one; carrying all three reciprocity loci costs the same as
carrying one. Two consequences matter for interpretation. First, mechanisms are
directly comparable in what they pay: direct reciprocity and partner choice both cost
one unit, and every combined mechanism costs two, however many loci it enables — so
contrasts within those matched sets isolate mechanism identity from expense. Second,
loci that are behaviorally inert under a given mechanism are still taxed, and
shedding part of a family saves nothing, so families disappear as blocks rather than
locus by locus. The genuinely untaxed cooperator is the full null C1I0J0M0P0Q0;
single-locus proxies such as C1P0 or C1M0 remain taxed if a sibling locus in the same
family is carried.

In two-population sweeps the rate is per population (i₀, i₁): an individual pays its
own population's rate on the families it carries. Unless otherwise swept, i is held at
a negligible 0.001.

## Population structure and ecology

Two population structures are available. In a single population (pop₁), individuals
pair within the population. In two coevolving populations (pop₂), all pairing is
between populations — the biologically central mutualism case, and the structure used
for every two-population result in the main text.

Ecological context is group size (4 or 128 individuals per group) and partner
shuffling. Groups are fixed memory segments for the whole run; shuffling only redraws
pairings within the same group each round, whereas noshuffle keeps partnerships stable
across rounds. Primary results use noshuffle and group size 128; shuffle and group size
4 appear as robustness (Figs. S2, S3).

## Independent variables and mechanisms

The design grid is the Cartesian product of social dilemma, cooperation cost (c, or
c₀ and c₁), information cost (i, or i₀ and i₁), group size, partner shuffling,
population structure, and mechanism
([framework](../journal/framework.md)). Mechanisms enable subsets of the conditional
behaviors: no enforcement (_); direct reciprocity (M); partner choice (P); and the
combined and reputation-rich families (MP, MPQ, IMP, IJMPQ), plus shuffle-only IM and
IJM. Main-text figures feature _, M, P, and IJMPQ as the hierarchy and the
reciprocity-bearing combined case.

## Simulation sweeps

The manuscript is built from six headline sweeps and two auxiliary calibration
planes:

1. **Equal cooperation cost** — single population and two coevolving populations;
   c₀ = c₁; dilemmas 0/1/2. Baseline hierarchy (Fig. S1) and stochastic two-population
   split (Fig. 1).
2. **Unequal cooperation cost** — two coevolving populations; upper-triangular
   c₀ < c₁ (210 cells); dilemmas 1/2. Deterministic role split (Fig. 2; full grid
   Fig. S4; no-enforcement control Fig. S3).
3. **Information cost × cooperation cost at equal c** — triangular i + c ≤ b grid.
   Decoupling at c = 0 (Fig. 3) and the soft-versus-compounding Cost × c surface
   (Fig. S7); dilemma-0 control (Fig. S8).
4. **Information cost under fixed cooperation-cost asymmetry** — c₀ = 0.10, i swept
   jointly with c₁ (i + c₁ ≤ b). Compression of the partner-choice split when the
   zero-cost refuge is removed (Fig. S9).
5. **Per-population information cost at equal cooperation cost** — c₀ = c₁ = 0.10;
   strict triangle i₀ < i₁ (per-axis cap b − c). Deterministic role assignment and
   hitchhiking inversion without a cooperation-cost gap (Fig. S11).
6. **Both costs asymmetric** — c₀ = 0.10, c₁ = 0.20 fixed; full i₀ × i₁ square
   (176 cells). Own-versus-partner cost and iso-budget non-convexity (Fig. 4),
   and the near-zero-i₀ hitchhiking regime (Fig. 5).

Auxiliary **payoff-plane calibration sweeps** hold two payoffs fixed and vary the
other two, decoupling temptation, risk, and R − P. They support the payoff-gap
attributions in the Results and Table S1 but are not published as figures
([supplement](supplement.md)).
([PD calibration](../journal/prisoners_calibration.md),
[snowdrift calibration](../journal/snowdrift_calibration.md)).

Single-run companions record nine snapshots from t = 131072 to 10⁶. Coarse spacing is
enough to confirm that role splits and collapses are already locked in at the first
recorded snapshot, but not to resolve sub-establishment ordering
([framework](../journal/framework.md)).

## Outcome measures

Cooperation level is the frequency of cooperative acts (qBSeen). Fitness is mean
payoff net of information cost (wmean). Genotype composition is read from
per-genotype frequencies aggregated to the relevant alleles and composites (e.g. C1P1
active choosers, C1P0 / C1M0 unconditional cooperators, C0P1 silent carriers, C1M1 /
C0M1 reciprocity carriers).

**Between-population asymmetry** is the qBSeen gap (who cooperates) and the wmean gap
(who profits) between the two coevolving populations. These are **outcome** variables,
distinct from **parameter** symmetry or asymmetry in c₀, c₁, i₀, i₁, and payoffs. The
two faces need not point at the same population: under partner choice in the
prisoner's dilemma the more cooperative side is the less fit one.

## Replicates, noise floor, and verification

Main-study values are means over 30 independent runs, with a companion standard-
deviation column per statistic. The practical noise floor is qBSeen gaps below
approximately 0.01–0.02 and fitness gaps below approximately 0.002; standard deviation
peaks in bistable transition cells (visible as the ±1 SD bands in Fig. 5). Every
headline number cited from the journal is regression-checked against the exported
simulation summaries by `ai/verify_claims.py`.


# Results

*Numbers are cited to the journal analyses that derive and regression-check them
(`ai/verify_claims.py`) rather than restated in full. Figures are the locked
main-text set (Figs. 1–5) and supplement (Figs. S1–S11).*

## 1. Mechanism hierarchy and cost thresholds

At equal cooperation cost in a single population, each enforcement architecture
sustains cooperation up to a characteristic cost and then collapses (Fig. S1). The
no-enforcement control (Fig. S1a) stays near the floor across the prisoner's-dilemma
range; direct reciprocity (Fig. S1b), partner choice (Fig. S1c), and the combined
reputation-rich mechanism (Fig. S1d) raise that ceiling in that order. The same
columns under snowdrift (Fig. S1e–h) sit higher: the elevated sucker payoff
already favours cooperation without enforcement, so the hierarchy softens and the
c-collapse matters less than in the PD
([synthesis](../journal/synthesis.md)).

A single cooperation-cost axis cannot say *which* payoff gap drives a collapse,
because raising c simultaneously raises temptation (T − R), raises risk (P − S),
and shrinks the cooperation advantage (R − P). Orthogonal payoff-plane calibration
analyses (not shown; Table S1) decouple these
([PD calibration](../journal/prisoners_calibration.md),
[snowdrift calibration](../journal/snowdrift_calibration.md)):

- **Direct reciprocity (M) is risk-limited.** Collapse as c rises tracks the growing
  mutual-defection risk rather than the shrinking R − P — confirmed from the other
  side in snowdrift, where the low sucker gap lets M sustain cooperation it cannot in
  the PD ([direct reciprocity](../journal/symmetric_c_reciprocity.md)).
- **Partner choice (P) is limited by the cooperation advantage R − P.** It tracks
  R − P alone across the orthogonal calibration, which is why it fails at the chooser
  bottleneck as R − P → 0.
- **Combined and reputation-rich mechanisms (MP, MPQ, IMP, IJMPQ) are reward-limited**
  and blind to the defection baseline, which is why they hold cooperation to the
  highest costs (Fig. S1d).

These attributions recover a mechanistic distinction that foreshadows the relational
result below. A residual chooser minority sorts the whole population, so even
unconditional cooperators are protected; a residual reciprocator minority protects
only itself ([reciprocity](../journal/symmetric_c_reciprocity.md)). Partner choice
assorts at the population level; reciprocity remembers at the individual level.
Short-memory and shuffle variants shift the direct-reciprocity collapse ordering
relative to Fig. S1 but leave the partner-choice versus combined contrast intact
(Fig. S2).

## 2. The two-population role split

With two coevolving populations, one population often cooperates while the other
exploits it, and the more cooperative population earns less fitness. I distinguish
this **outcome** asymmetry (gaps in cooperation and fitness) from **parameter**
symmetry in the setup (whether c₀ = c₁, i₀ = i₁, and payoffs match). Mechanism can
override the default mapping.

When costs and payoffs match (c₀ = c₁, i₀ = i₁), partner-choice populations
**stochastically** split into cooperators and exploiters in the prisoner's dilemma —
a split that does not appear without enforcement (Fig. 1a–d). One population carries
cooperation and is exploited; carrying the chooser allele correlates with fitness at
roughly minus one
([partner choice calibration](../journal/prisoners_partner_choice.md)). In snowdrift
populations already split without enforcement; partner choice then reshapes
high-cooperation-cost outcomes (Fig. 1e–h). Combined reputation mechanisms at the
same parameter point leave the two populations nearly matched in the PD.

**Figure 1: Outcome asymmetry under parameter-symmetric cooperation cost.** Frequency of cooperators and average fitness in two coevolving populations (light green indicates the population with the lower frequency of cooperators; dark green the other). **A–D**, Prisoner's dilemma. **E–H**, Snowdrift game. **A, E**, Baseline without enforcement mechanisms. **B, F**, Short-memory partner choice is the only available mechanism. Both populations pay identical cooperation costs ($c$, swept from 0 to the partner benefit $b$) and identical information costs ($0.001$). Under matched costs, partner choice generates a stochastic cooperator/exploiter role split in the prisoner's dilemma that is absent without enforcement. In the snowdrift game, the split already exists in the baseline and partner choice primarily extends it to higher costs.

When one population pays a slightly lower cooperation cost, that chance split becomes
deterministic. Along the strip c₁ = c₀ + 0.02, the lower-cooperation-cost population
cooperates in every cell under partner choice, and the R − P gap becomes a stable
cooperation gap (Fig. 2a,b;
[partner choice under cooperation-cost asymmetry](../journal/asymmetric_c0_c1_partner_choice.md),
[synthesis](../journal/synthesis.md)). Under combined IJMPQ the expensive population
cooperates more and the outcome gap shrinks on the same axes (Fig. 2c,d), because
reward-led mechanisms no longer route R − P into a cooperation gap
([combined mechanisms](../journal/asymmetric_c0_c1_combined.md)). Fig. 2 is
prisoner's-dilemma only: without enforcement the cheap population barely cooperates
in the PD (control mean ≈ 0.10), so partner choice is what lets populations lock the
parameter gap into a deterministic split (Fig. S3; full c₀ × c₁ grid in Fig. S4).
In snowdrift the sucker payoff already lets populations cooperate highly without
machinery (control ≈ 0.96 vs partner choice ≈ 0.96 for the cheap side), and
populations often diverge from payoffs alone (Fig. 1e–h). A parallel asymmetric snowdrift
panel would repeat that floor rather than isolate what enforcement adds.
Fig. S5 contrasts the deterministic and stochastic strips on shared axes; the split
survives small-group stochasticity at group size 4 (Fig. S6).

**Figure 2: Deterministic role splits emerge from cooperation-cost asymmetries.** Frequency of cooperators and average fitness for two coevolving populations under the prisoner's dilemma, evaluated along the parameter strip $c_1 = c_0 + 0.02$ (with both populations overlaid). **A, B**, Short-memory partner choice alone. **C, D**, Combined partner choice and indirect reciprocity. Both populations pay identical information costs ($0.001$). A small cooperation-cost gap allows partner choice to convert the payoff asymmetry into a stable cooperator/exploiter assignment (**A, B**). The combined reputation-rich mechanism lifts the expensive population, shrinking the outcome asymmetry (**C, D**).

Single-run trajectories confirm that these roles are absorbing states locked in by
the first recorded snapshot (t = 131072), not slow late erosions. The temporal
regime does not differ between one and two populations
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

With this cooperation-cost baseline established, I next ask how populations respond
when they differ in information cost.

## 3. Costly machinery, decoupling, and why symmetry hides the question

Making the enforcement apparatus itself costly introduces a pressure orthogonal to
cooperation cost
([information cost at equal cooperation cost](../journal/symmetric_c_i.md)). Taxing
the machinery alone erodes cooperation only gently where temptation is absent,
because a population can shed the apparatus and keep cooperating for free. Where the
two costs overlap, information cost thins the defence cooperation cost requires and
pulls the c-collapse threshold downward (Fig. S7).

At zero cooperation cost the genotype route makes the escape visible (Fig. 3). As
information cost rises, active enforcement alleles are selected out — chooser P1
(Fig. 3a) and TFT M1 (Fig. 3c) both fall toward zero — while cooperation remains high
on tax-free unconditional cooperators (Fig. 3b,d: C1P0, C1M0). Behavior and
mechanism decouple. A dilemma-free control shows that machinery erodes with or
without a social dilemma; cooperation persists through the shed only when the dilemma
is present, so the tax drives the erosion and the dilemma decides whether losing the
machinery drags behavior down (Fig. S8).

**Figure 3: Information cost decouples cooperation from enforcement machinery when cooperation is free.** Frequency of the active machinery allele (chooser P1 in **A**; tit-for-tat M1 in **C**) and overall frequency of cooperators (**B, D**) in a single population. **A, B**, Short-memory partner choice alone. **C, D**, Direct reciprocity alone. The cooperation cost is fixed at zero while the information cost is swept from 0 to the partner benefit ($b = 0.4$). Rising information cost selects against active enforcement alleles, but cooperation remains high because populations shed the costly machinery in favour of tax-free unconditional cooperation.

That refuge disappears once cooperation cost is held above zero. Machinery loss and
behavioral loss then move together: shedding P1 or M1 no longer leaves a stable
high-cooperation niche behind
([information cost under cooperation-cost asymmetry](../journal/asymmetric_c1_i.md)).
With a fixed cooperation-cost gap, as information cost rises populations cooperate less
and both the cooperation gap and the fitness gap shrink; the more cooperative
population remains less fit while partner choice still functions, then both fall to
the control floor (Fig. S9). Second-order free-riders (C1M0)
and silent carriers (C0P1) accumulate along the same routes
([reciprocity](../journal/symmetric_c_reciprocity.md),
[reciprocity under cooperation-cost asymmetry](../journal/asymmetric_c0_c1_reciprocity.md)).

A symmetric information-cost design cannot separate the cost a population pays from
the burden that cost places on its partner. The decoupling route looks like a local escape — shed
the tax, keep cooperating — but that reading is an artefact of levying the same tax
on both sides at once. Holding one population's information cost at zero and varying
the other's breaks the confound.

## 4. Information cost is relational

Figs. 4–5 cross a fixed cooperation-cost gap (c₀ = 0.1, c₁ = 0.2) with independent
per-population information costs. The first two columns of Fig. 4 hold one
population's information cost at zero and sweep the other's, so I can see which
population's cost places the larger burden on its partner
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

Under partner choice the two strip columns tell opposite stories (Fig. 4a,b). When the
low-cooperation-cost population pays i = 0.20 it barely changes (0.602 → 0.585)
and its partner even rises (0.189 → 0.268). When the high-cooperation-cost population
pays the same tax, both collapse (0.069 and 0.032). Under partner choice a population
barely bears a burden from its own information cost and collapses under the burden of
its partner's. The bilateral swap rule is why: a chooser is useless without a chooser
to trade with, so assortment is rationed by whichever population has fewest choosers
to spare — and that is already the high-cost side before any tax is applied.

Under the combined reputation-rich mechanism the pattern reverses (Fig. 4d,e).
When the low-cooperation-cost population pays i = 0.20 its partner falls from 0.957
to 0.268 while the payer itself falls only to 0.734 — the partner bears a larger
burden than the payer. When the high-cost side pays instead, that side stays near
0.911. Reciprocity-bearing mechanisms protect only their carriers: a taxed population
can shed into unconditional cooperation, which is harmless when the taxed side
contributes little cooperation and destructive when it carries most of it. Here the
partner bears a larger burden when the *low*-cooperation-cost population pays the
information cost — the opposite of partner choice.

Genotype composition confirms that a partner's cost can silence an untaxed
allele. At (i₀, i₁) = (0, 0.20) the untaxed population's chooser frequency sits at
its neutral value (P1 = 0.519; inert Q1 = 0.498, M1 = 0.504), yet little of it
is expressed (C1P1 = 0.044, against 0.187 in the same population when it pays the
0.20 tax itself). With the partner's choosers taxed away there is nobody to swap
with; the population collapses to defection and the allele survives only in silent
defector carriers.

The fitness counterpart to these relational slices shows similar cross-population
burdens and iso-budget interior penalties (Fig. S10).

The escape that let a population survive information cost under symmetry (Fig. 3) is
what places a burden on its partner under asymmetry: shedding relieves the payer and
withdraws the service the partner needed.

**Figure 4: The relational burden of information cost.** Frequency of cooperators in two coevolving populations under the prisoner's dilemma. One population (orange) has a lower cooperation cost ($c_0 = 0.1$) than the other (red; $c_1 = 0.2$). **A–C**, Short-memory partner choice alone. **D–F**, Combined partner choice and indirect reciprocity. **A, D**, Information cost is applied only to the low-cooperation-cost population ($i_1 = 0$; $i_0$ swept). **B, E**, Information cost is applied only to the high-cooperation-cost population ($i_0 = 0$; $i_1$ swept). **C, F**, The total information budget is fixed at $i_0 + i_1 = 0.2$ while the distribution between populations varies. Under partner choice (**A, B**), populations are robust to their own information costs but collapse under their partner's. Under the combined reputation mechanism (**D, E**), this relationship reverses: taxing the low-cost population severely harms its high-cost partner. Furthermore, reciprocity-bearing mechanisms suffer an interior penalty where splitting the budget harms the pair more than concentrating it on one side (**F**).

## 5. Budget non-convexity and boundary conditions

Equal enforcement budgets are neither fungible nor additive (Fig. 4c,f). Along a line of
constant total information cost (0.20), every reciprocity-bearing mechanism reaches
its *lowest* total cooperation in the interior rather than at either end. Under IJMPQ
populations that load a budget of 0.20 onto one side reach 1.0–1.65 total cooperation,
but only 0.39 when they split it as (0.06, 0.14) (Fig. 4f). Either corner leaves one
population with an intact apparatus, which is enough to hold the pair together; a
split breaks both and pushes neither over the threshold where machinery-free
cooperation takes over. Partner choice is monotone instead (Fig. 4c): because only the
high-cooperation-cost population's information cost bites, the best outcome sits at
the corner that spares that population. The non-convexity is therefore a property of
reciprocity-bearing mechanisms, not of the budget itself
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

When both cost axes differ, populations still follow the cooperation-cost gap.
Across the full i₀ × i₁ square behind Figs. 4–5, under partner choice the
lower-cooperation-cost population cooperates in 170/176 cells; under IJMPQ they invert
locally only on the i₀ ≈ 0 strip (13 cells). That hitchhiking inversion is stronger
when populations differ only in information cost (Fig. S11: IMP
dq = −0.461 at Cost0 = 0, Cost1 = 0.20) and weaker once a cooperation-cost
gap is present (IMP dq = −0.100 at the same information-cost point). The gap moves
every reciprocity-bearing mechanism toward the cheap-cooperation-cost population,
erasing the inversion outright for MP and MPQ
([per-population information cost](../journal/asymmetric_i0_i1.md),
[crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

Fig. 5 shows the near-zero-i₀ inversion regime narrowing. Each panel fixes the information cost on the
low-cooperation-cost population and sweeps the other. The inversion — the expensive
population's curve above the cheap one's — holds throughout when i₀ = 0 (Fig. 5a),
survives only past a threshold when i₀ = 0.02 (Fig. 5b), and is gone by i₀ = 0.04 and
0.1 (Fig. 5c,d). Crossing into the machinery-free state is a bistable threshold, not
a slope: just inside this regime, doubling a population's own information cost *raises*
its cooperation by 0.32 as it tips from a defector-heavy mixed state into near-
complete tax-free unconditional cooperation. Run-to-run variance marks the basin
boundary directly in the ±1 SD bands — wide below the threshold (SD ≈ 0.25; runs
split between two attractors) and collapsed above it (SD ≈ 0.009).
In the paired fitness panels (Fig. 5e–h), the same cooperation-fitness mismatch holds
in every column: the population with higher cooperation is the one with lower fitness,
even when the colour ordering switches as i₀ rises.
In this threshold regime, increasing population 1's own information cost can confer
a fitness benefit on population 0 even while population 1 becomes slightly less fit,
showing that one population can benefit from a partner that pays more for enforcement
machinery.

**Figure 5: Role inversion requires near-zero information costs in the low-cost population.** Frequency of cooperators (**A–D**) and average fitness (**E–H**) under combined partner choice and indirect reciprocity in the prisoner's dilemma. Cooperation costs are fixed asymmetrically ($c_0 = 0.1$, orange; $c_1 = 0.2$, red). Each column holds the information cost of the low-cooperation-cost population ($i_0$) constant while sweeping $i_1$. **A, E**, $i_0 = 0$. **B, F**, $i_0 = 0.02$. **C, G**, $i_0 = 0.04$. **D, H**, $i_0 = 0.1$. The role inversion—where the expensive population cooperates more than the cheap one—survives only when $i_0$ is small. Shaded bands ($\pm 1$ SD over 30 runs) indicate a bistable threshold between mixed states and tax-free unconditional cooperation. In this regime, fitness remains decoupled from cooperation: the population that cooperates more earns less fitness.

The inversion appears only when the reciprocity family is present, not as a simple
effect of how much information cost a mechanism pays. Information cost is charged per family carried — one unit for partner
choice, one for reciprocity — so a mechanism owes 0, 1 or 2 units however many loci
it enables. At one unit, direct reciprocity and partner choice pay identically, yet
reciprocity inverts in 10 cells of the i₀ ≈ 0 strip and partner choice in none. At
two units, the four combined mechanisms pay identically, yet invert in 3, 1, 13 and
13 cells. Every mechanism carrying the reciprocity family inverts somewhere in that
strip; no mechanism lacking it does. Reciprocity supplies the second-order-free-rider
niche that unconditional cooperation occupies once active machinery becomes
unaffordable. Partner choice does lose the lead in three cells, but in the opposite
corner of the square and by the opposite route: a transient crossing while its *own*
machinery collapses.

Snowdrift removes this regime entirely, identifying this cross-population burden as a property
of the dilemma rather than of the cost accounting
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)). The dilemma-0 control
makes the same point for the decoupling claim (Fig. S8). Shuffle and group-size
panels locate which loci carry the baseline effects (Figs. S2, S3).


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


