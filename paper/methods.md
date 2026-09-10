# Methods

## Model

I use an individual-based evolutionary model with two population structures. In a
single population, individuals pair within the population. In two coevolving
populations, pairing is between populations.

Individuals live in fixed groups of 4 or 128. Groups restrict interaction in two
ways. When partner choice is on, a chooser can rematch only within its group. When
shuffling is on, pairs are redrawn within the group each round; without it,
partnerships persist until death or a partner-choice swap. A group in a single
population holds 4 or 128 members of that population. In the two-population case it
holds the same number from each side, so every individual faces 4 or 128 potential
partners.

Each population holds 4096 individuals — a size divisible by both group sizes, which
splits it into 1024 small groups or 32 large ones. Adults never change group. Each
round every adult dies with probability 2^−7: I draw the number of deaths from a
binomial distribution, then choose that many individuals uniformly among those born in
an earlier round, so a newborn never dies before it has played once. That mortality is
low enough that lasting partners meet many times (about 64 rounds on average when
individuals do not change partners), yet high enough that frequencies stabilize well
before runs end (snapshots below).

Selection acts only through parentage; mortality ignores fitness. Each death is filled
by one offspring whose parent I draw from the whole population with probability
proportional to each candidate's fitness in the current round rather than to payoff
accumulated over its life. Reproduction is asexual and haploid: the offspring clones
its parent's genotype, subject to mutation, replaces the dead individual, and inherits
that individual's partner.
Only recruitment moves individuals between groups, and an offspring need not share its
parent's group. Mutation rate is 0.01 per locus per reproduction event. Each run lasts
2^20 rounds, about 8000 average lifetimes.

Each individual carries six binary loci: a cooperation locus C and five mechanism
loci that control conditional behavior. Throughout, upright capitals name loci and
alleles (C, C1, IJMPQ) and italic lowercase names parameters (b, c, i). Allele C1
sets the default act — cooperate unless a mechanism overrides it; C0 defects.

Two loci choose partners, on recent cooperation (P) or on lifetime cooperation rate
(Q). Three loci copy a partner's behavior. M copies the partner's previous act, but
only while the partnership is unbroken, which makes it tit-for-tat. I copies the
partner's previous act whether or not the pair has met before. J adopts the partner's
lifetime reputation, rounding that rate to cooperate or defect, as in image scoring.
Whose record I and J use depends on partner turnover. While a partnership
persists, the partner's last act was directed at the focal individual, so I reduces to
direct reciprocity; once pairs are redrawn, that act was directed at a third party, and
copying it becomes indirect reciprocity. Recent cooperation is the last act played;
lifetime reputation is the running mean of those acts since birth. M1 copies, M0 does
not; and so on for the other mechanism alleles.

An individual behaves according to decision precedence Q1 > P1 within partner choice
and J1 > I1 > M1 within reciprocity when it carries more than one mechanism allele in
the same family. Partner choice and reciprocity are applied at separate stages of each
round (below), so precedence across families never arises.

Under partner choice, an individual becomes an active chooser when its own last act
was to cooperate and its current partner defected. Assortment is then a bilateral
swap: I shuffle the active choosers within a group and pair them in adjacent pairs, so
one does not rematch that round when their number is odd. Each chooser exchanges a
non-cooperative partner for the other chooser, and the two partners left unpaired end
up paired with each other.

The lifetime locus Q replaces that rule rather than supplementing it. Where Q is
enabled, a chooser is active whenever it carries P1 or Q1, and two choosers swap only
if each ranks the other above its own current partner — on lifetime cooperation rate
for a Q1 chooser, on the last act for a P1 chooser. A contrast between MP and MPQ
therefore changes the partner-choice rule as well as adding a locus.

Whether an individual can choose depends on its recent act, not on the C allele. A
defector by default that cooperated through reciprocity can choose, and a C1
individual that copied a defecting partner cannot. So under partner choice alone,
where the act follows C directly, C0P1 carries the allele and never chooses.
Reciprocity has no comparable restriction — C0M1 still copies once a partnership is
established.

At run start every individual carries the null allele at all six loci and defects.
Pairs are assigned within groups (and across populations in the two-population form)
before the first round. Allelic diversity arises only by mutation; cooperative and
mechanism alleles are not introduced at initialization.

## Social dilemmas

Cooperation cost c is what a cooperator pays to produce the benefit in
the dilemma. In the prisoner's dilemma that benefit is given to the partner; in
the snowdrift it is shared between the pair whenever at least one player
cooperates. Under the control payoff structure nothing is shared, and an
individual's payoff does not depend on its partner's behavior: producing the benefit
pays b − c whatever the partner does, so cooperation dominates while c < b. Baseline
fitness K = 0.5 and benefit b = 0.4 are fixed; c is swept from 0 to b. Table 1 gives
the three payoff structures.

Table 1. Payoff structures for the three social settings.

| Game structure           | T (temptation) | R (reward)  | P (penalty) | S (sucker) | T − R (temptation gap) | P − S (risk)  | R − P (cooperation advantage)  |
| ------------------------ | -------------- | ----------- | ----------- | ---------- | ---------------------- | ------------- | ------------------------ |
| Control (no dilemma)     | K              | K + b − c   | K           | K + b − c  | c − b (increases)      | c − b (increases) | b − c (decreases)      |
| Prisoner's dilemma       | K + b          | K + b − c   | K           | K − c      | c (increases)          | c (increases) | b − c (decreases)          |
| Snowdrift                | K + b          | K + b − c/2 | K           | K + b − c  | c/2 (increases slowly) | c − b (increases) | b − c/2 (decreases slowly) |

Note: Columns T − R, P − S, and R − P show how each gap changes as cooperation cost c
rises. In the control row R exceeds T and S exceeds P, so the first two gaps are
negative and neither temptation nor risk applies.

In the two-population form each population pays its own cooperation cost (c₀, c₁), with
c₀ < c₁ whenever they are asymmetrical. The lower-cost population always has the
larger cooperation advantage (R − P).

## Information cost

An individual incurs an information cost every round for the *families* of mechanism
loci it carries, not per locus and not only for alleles that affect its current
behavior:

cost = i × ( partner-choice family carried + reciprocity family carried ),

where each term counts 1 if the individual carries any allele of that family — P1 or
Q1 for partner choice, M1, I1 or J1 for reciprocity — and 0 otherwise.

An individual therefore pays 0, 1 or 2 units of i. One family costs one unit however
many of its loci the individual carries, so a mechanism drawn from a single family
costs one unit and any combined mechanism costs two, whatever its locus count — which
lets contrasts within those matched sets isolate mechanism identity from expense.
Loci that are behaviorally inert under a given mechanism still incur the cost, and
losing part of a family saves nothing, so families are eliminated only as whole
families rather than locus by locus. An individual pays no information cost only if it
carries the full null C1I0J0M0P0Q0; single-locus proxies such as C1P0 or C1M0 still
pay if another locus in the same family is carried.

Each population has its own rate (i₀, i₁), and an individual pays its own
population's rate for the families it carries. Two designs sweep those rates apart;
elsewhere the two populations pay alike. Unless a design varies it, i is held at
0.001, so even a carrier of both families pays under half a percent of baseline
fitness.

## Timestep order

Fitness is the game payoff minus information cost, floored at zero:
w = max(0, payoff − cost), with payoff from Table 1 evaluated on each individual's
current act and its partner's. Fitness is zero only where information cost exceeds the
payoff, which happens for carriers of both families in the most expensive cells of the
information-cost sweeps.

Within each time step the order is fixed: if shuffling is on, redraw pairs within each
group; if partner choice is on, rematch choosers; replace deaths with offspring weighted
by the previous round's fitness (each newborn's act is reset to its inherited C
allele); then, if reciprocity is on, set each survivor's act toward its current partner;
finally compute fitness from those acts.

When reciprocity is disabled, an individual's act equals its C allele, fixed at birth
and unchanged until death. When reciprocity is enabled, each round's act starts from
C and is overridden only by active M, I, or J alleles.

## Independent variables and mechanisms

I vary the parameters above together with which conditional behaviors may determine
acts and rematching. Each mechanism label names the loci a run allows to act: direct
reciprocity (M); partner choice (P); the combined mechanisms and those that include
lifetime reputation (MP, MPQ, IMP, IJMPQ); and no enforcement, where none of those
behaviors run while the loci still mutate and still cost. Alleles at loci a run does
not enable do not affect behavior but remain costly. Enabling loci independently lets
me test each mechanism and combinations of them.

Indirect reciprocity stands alone as a mechanism (IM, IJM) only under shuffling,
because persistent pairs leave I copying the partner's act toward the focal individual
itself, which is direct reciprocity; alongside partner choice it appears in the
combined mechanisms IMP and IJMPQ. Table S1 reports which payoff gap limits each
mechanism family in the payoff-plane attributions. The control payoff structure
(Table 1, first row) is separate from mechanism choice: under it, a partner's behavior
does not change payoffs.

## Outcome measures

Outside the temporal comparisons, I record every reported value at the last logged
round (t = 2^20), from the state at the end of that round after payoffs.

I use three measures. The frequency of cooperators is the share of
individuals who behave cooperatively in that round. This is not the frequency of C1 —
a C0M1 reciprocator counts when it copies a partner's cooperation. Fitness is mean w,
the floored payoff net of information cost. Allele and genotype frequencies give the
third measure, which shows what produces the cooperation: active choosers (C1P1),
unconditional cooperators that pay no information cost (C1P0, C1M0), and carriers that
never choose (C0P1).

For two populations I report each measure per population and the gap between them.
To summarize who profits, I correlate the two gaps across the cells of a sweep — the
Pearson correlation between the cooperation gap and the fitness gap. A value near
minus one means the population that cooperates more earns less.

Where costs and payoffs match, the two populations start interchangeable, so I label
them by outcome: within each run and snapshot, the more cooperative population is
reported first. That prevents role differences from canceling when averaged across
runs, but it also makes the reported gap a rank statistic, which cannot be zero even
without a real split. I therefore read symmetric-case asymmetry against the
no-enforcement column, labeled the same way, rather than against zero. Single-replicate
runs keep their original labels, so their two curves are not rank-ordered. Where costs
or payoffs differ, the labels follow the parameters.

## Simulation designs

Unless noted, group size is 128 and partnerships are not shuffled; shuffled partners
and groups of 4 appear in the supplement. The constraint i + c ≤ b (and i + c₁ ≤ b
where c₁ is swept) keeps total cost from exceeding the cooperation benefit.

I first establish baselines under equal cooperation cost. In a single population,
sweeping c from 0 to b across mechanisms and payoff structures shows how high each
mechanism can raise cooperation before cooperation falls, and whether that
ordering depends on the dilemma (Fig. S1). The same equal-cost sweep in two
coevolving populations asks whether matched parameters produce matched outcomes, or
whether mechanisms themselves can create cooperator and exploiter roles (Fig. 1).

I then vary parameters asymmetrically along one axis at a time. Cooperation-cost
asymmetry (c₀ < c₁ on a grid of 210 ordered pairs with c₀ ∈ [0, 0.38] and
c₁ ∈ [0.02, 0.40]) tests whether unequal helping costs determine cooperator/exploiter
roles (Fig. 2; full grid Fig. S4; no-enforcement control Fig. S3). Information
cost is introduced next at equal c on a triangular grid of 231 (i, c) cells under
i + c ≤ b (Fig. 3; full grid Fig. S7), to separate loss of mechanism alleles from
the payoff cost of helping, including under the control payoff structure where a
partner's act does not affect payoffs (Fig. S8).

The central designs ask who bears the burden of an information cost. Holding a
cooperation-cost gap and sweeping information cost (c₀ = 0.10, i and c₁ joint under
i + c₁ ≤ b; 120 cells; Fig. S9), holding equal cooperation cost and sweeping
per-population information cost (c₀ = c₁ = 0.10, i₀ < i₁, each axis capped at
b − c; 120 cells; Fig. S11), and crossing both asymmetries (c₀ = 0.10, c₁ = 0.20,
176-cell square with i₀ ≤ 0.30 and i₁ ≤ 0.20; Figs. 4–5) compare own-cost versus
partner-cost effects and whether equal information-cost totals have the same effect
regardless of how they are split between populations.

To attribute each mechanism's loss of cooperation along the cooperation-cost axis, I
also ran orthogonal payoff-plane sweeps in a single population that vary payoffs
independently of c. The prisoner's-dilemma plane fixes T = 0.90 and S = 0.10 and
varies R and P (172 cells with T > R > P > S); the snowdrift plane fixes T = 0.90 and
P = 0.10 and varies R and S (172 cells with T > R > S > P). Attributions are in
Table S1; the heatmaps are not published.

Every run is logged at nine snapshots: the first round, then eight points spaced
2^17 rounds apart up to 2^20. Both the 30-run series and the single-replicate
trajectories can therefore show whether outcomes are already stable by mid-run or
still changing late. Single-replicate companions over the same grids show one
trajectory without averaging — under matched costs in two populations, which
population becomes the cooperator is a 30-run question, and a companion shows only
one realized split.

The simulation is written in C and draws random numbers from a Tausworthe generator
seeded from the clock, so runs replicate in distribution rather than exactly.
Simulation code, analysis scripts, and the summary exports behind every figure are
archived in the repository cited on the title page.

## Replicates and variation

Reported values are means over 30 independent runs. I also computed standard
deviations but plotted them only in Fig. 5, where run-to-run spread is largest;
elsewhere they are too small to read on the figure scales. Taken over the cells of a
sweep, median standard deviations are about 0.01–0.04 for cooperation and 0.001–0.01
for fitness. Spread is largest where runs diverge to different outcomes (Fig. 5).

I run no hypothesis tests. The design is a grid rather than a sample, so I judge
differences against that run-to-run spread: cooperation differences below about
0.01–0.02 and fitness differences below about 0.002 fall within it and are not
treated as meaningful effects. Gaps between rank-labeled populations under matched
parameters carry a bias of the same order, which is why the parameter-symmetric
claims depend on the contrast with no enforcement rather than on the size of the gap
alone.
