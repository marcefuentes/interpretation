# Methods

## Model

### Population and groups

I use an individual-based evolutionary model with two population structures. In a
single population, individuals pair within the population. In two coevolving
populations, pairing is between populations.

Individuals live in fixed groups of 4 or 128. Groups restrict interaction in two
ways. When partner choice is on, a chooser can rematch only within its group. When
shuffling is on, pairs are redrawn within the group each round; without it,
partnerships persist until a partner-choice swap, with a dead partner replaced by
its offspring. A group in a single population holds 4 or 128 members of that
population, so each individual faces 3 or 127 other group members as potential
partners. In the two-population case it holds the same number from each side, so
every individual faces 4 or 128 potential partners from the other population.

Each population holds 4096 individuals — a size divisible by both group sizes, which
splits it into 1024 small groups or 32 large ones. Adults never change group.

### Demography

Each round every adult dies with probability 2^−7: I draw the number of deaths from a
binomial distribution with n = 4096, then choose that many individuals uniformly among
those born in an earlier round, resampling if a draw hits a newborn, so a newborn never
dies before it has played once. That mortality is low enough that a given pairing of
individuals lasts about 64 rounds on average when they do not rematch, yet high enough
that frequencies stabilize well before runs end (snapshots below).

### Reproduction and inheritance

Selection acts only through parentage; mortality ignores fitness (defined under
Timestep order below). Each death is filled by one offspring whose parent I draw from
the dead individual's own population with probability proportional to each candidate's
fitness from the previous round rather than to payoff accumulated over its life.
Reproduction is asexual and haploid: the offspring clones its parent's genotype,
subject to mutation, replaces the dead individual in that individual's group slot, and
inherits that individual's partner. Only recruitment moves individuals between groups,
so an offspring need not share its parent's group. Mutation flips each locus
symmetrically with probability 0.01 per locus per reproduction event. Each run lasts
2^20 rounds, about 8000 average lifetimes.

### Loci and alleles

Each individual carries six binary loci: a cooperation locus C and five mechanism
loci that control conditional behavior. Throughout, upright capitals name loci and
alleles (C, C1, P1) and italic lowercase names parameters (b, c, i). Mechanism labels
concatenate the loci a run allows to act (M, P, MP, IJMPQ). Allele C1 sets the
default act — cooperate unless a mechanism overrides it; C0 defects.

Two loci choose partners, on recent cooperation (P) or on lifetime cooperation rate
(Q). Three loci copy a partner's behavior. M copies the partner's previous act only
when the current partner is the same individual as in the previous round, which makes
it tit-for-tat. I copies the partner's previous act whether or not the pair has met
before. J adopts the partner's lifetime reputation, rounding that rate to cooperate or
defect, as in image scoring. Whose record I and J use depends on partner turnover.
While a partnership persists, the partner's last act was directed at the focal
individual, so I reduces to direct reciprocity; once pairs are redrawn, that act was
directed at a third party, and copying it becomes indirect reciprocity. Recent
cooperation is the last act played; lifetime reputation is the running mean of those
acts since birth. M1 copies, M0 does not; and so on for the other mechanism alleles.

### Behavioral rules

An individual behaves according to decision precedence Q1 > P1 within partner choice
and J1 > I1 > M1 within reciprocity when it carries more than one mechanism allele in
the same family. Partner choice and reciprocity are applied at separate stages of each
round (below), so precedence across families never arises.

Under partner choice, an individual becomes an active chooser when its own last act
was to cooperate and its current partner defected. Assortment is then a bilateral
swap. In a single population I shuffle the active choosers within a group and pair
them in adjacent pairs, so one does not rematch that round when their number is odd.
In two populations I shuffle each side's active choosers within the group and match
min(n₀, n₁) cross-population pairs; surplus choosers on the larger side remain
unmatched that round. Each matched chooser exchanges a non-cooperative partner for
the other chooser, and the two partners left unpaired end up paired with each other.

The lifetime locus Q replaces that rule rather than supplementing it. Where Q is
enabled, a chooser is active whenever it carries P1 or Q1, and two choosers swap only
if each ranks the other above its own current partner — on lifetime cooperation rate
for a Q1 chooser, on the last act for a P1 chooser. Equal ranks do not improve on the
current partner and do not trigger a swap. Short-memory partner choice means ranking
on the last act only (P enabled, Q not); main-text figures use it unless noted. A
contrast between MP and MPQ therefore changes three things at once: it adds the Q
locus, drops the cooperate-against-defector activation condition, and makes the swap
mutually consented. No MP/MPQ difference can be attributed to the Q locus alone.

Whether an individual can choose depends on its recent act, not on the C allele. A
defector by default that cooperated through reciprocity can choose, and a C1
individual that copied a defecting partner cannot. So under partner choice alone,
where the act follows C directly, C0P1 carries the allele and never chooses.
Reciprocity has no comparable restriction — C0M1 still copies once a partnership is
established.

### Initialization

At run start every individual carries the null allele at all six loci and defects.
Pairs are assigned within groups (and across populations in the two-population form)
before the first round. Allelic diversity arises only by mutation; cooperative and
mechanism alleles are not introduced at initialization.

## Game types

I study three game types: the prisoner's dilemma, the snowdrift, and a control with
no dilemma. Cooperation cost c sets the payoffs within a type. In the prisoner's
dilemma a cooperator pays c to give benefit b to the partner; in the snowdrift both
players receive b whenever at least one cooperates, and two cooperators split c.
Under the control game nothing is shared, and an individual's payoff does not depend
on its partner's behavior: producing the benefit pays b − c whatever the partner does,
so cooperation dominates while c < b. Baseline fitness K = 0.5 and benefit b = 0.4 are
fixed; c is swept from 0 to b. At c = 0 the prisoner's dilemma is not strict (T = R
and P = S); at c = b the snowdrift loses S > P. Table 1 gives the three game types and
how their payoffs move with c.

Table 1. Game types and payoffs.

| Game type                | T (temptation) | R (reward)  | P (penalty) | S (sucker) | T − R (temptation gap) | P − S (risk)  | R − P (cooperation advantage)  |
| ------------------------ | -------------- | ----------- | ----------- | ---------- | ---------------------- | ------------- | ------------------------------ |
| Control (no dilemma)     | K              | K + b − c   | K           | K + b − c  | c − b (increases)      | c − b (increases) | b − c (decreases)              |
| Prisoner's dilemma       | K + b          | K + b − c   | K           | K − c      | c (increases)          | c (increases) | b − c (decreases)              |
| Snowdrift                | K + b          | K + b − c/2 | K           | K + b − c  | c/2 (increases slowly) | c − b (increases) | b − c/2 (decreases slowly) |

Note: Columns T − R, P − S, and R − P show how each gap changes as cooperation cost c
rises. Temptation applies only when T > R, and risk only when P > S. In the control
row both gaps are negative, so neither applies. In snowdrift S > P for all c < b, so
there is no risk on the interior of the sweep even though P − S = c − b rises toward
zero. In the prisoner's dilemma both temptation and risk are positive for c > 0 and
rise with c.

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
information-cost sweeps. In those cells individuals that differ in payoff can share a
fitness of zero, so selection differentials vanish rather than merely shrink.

Within each time step the order is fixed: if shuffling is on, redraw pairs within each
group; if partner choice is on, rematch choosers; replace deaths with offspring weighted
by the previous round's fitness (each newborn's act is reset to its inherited C
allele); then, if reciprocity is on, set each individual's act toward its current
partner; finally compute fitness from those acts. Reciprocity applies only when both
partners have age greater than zero, so a newborn and its surviving partner act on
their C alleles in the newborn's first round; M then requires that the current partner
match the previous round's partner, so a replacement also breaks direct reciprocity
for that first shared round.

When reciprocity is disabled, an individual's act equals its C allele, fixed at birth
and unchanged until death. When reciprocity is enabled, each round's act starts from
C and is overridden only by active M, I, or J alleles.

## Independent variables and mechanisms

I vary population number (one or two), group size, whether partnerships shuffle,
game type, cooperation cost, and information cost, together with which
conditional behaviors may determine acts and rematching. Each mechanism label names
the loci a run allows to act (Table 2). Alleles at loci a run does not enable do not
affect behavior but remain costly. Frequencies near one-half are the mutation-only
expectation for such unused alleles, because mutation flips symmetrically. Enabling
loci independently lets me test each mechanism and combinations of them.

Table 2. Mechanisms.

| Label | Loci enabled     | Info-cost units | Structures                        | Where reported                        |
| ----- | ---------------- | --------------- | --------------------------------- | ------------------------------------- |
| \_    | none behavioral  | 0-2 if carried  | one or two pops; shuffle optional | baselines; Fig. S1a,e; Fig. S3        |
| M     | C, M             | 1               | one or two pops; shuffle optional | Figs. S1-S2; Fig. 3c,d                |
| P     | C, P             | 1               | one or two pops; shuffle optional | main short-memory figures; Fig. S1c,g |
| MP    | C, M, P          | 2               | one or two pops; shuffle optional | matched contrasts; Fig. S2            |
| MPQ   | C, M, P, Q       | 2               | one or two pops; shuffle optional | matched contrasts                     |
| IM    | C, I, M          | 1               | shuffle only                      | Fig. S2; not in main noshuffle panels |
| IJM   | C, I, J, M       | 1               | shuffle only                      | Fig. S2; not in main noshuffle panels |
| IMP   | C, I, M, P       | 2               | one or two pops; shuffle optional | equal-c i design; unit-accounting     |
| IJMPQ | C, I, J, M, P, Q | 2               | one or two pops; shuffle optional | Figs. 2, 4-5; Fig. S1d,h; Fig. S11    |

No enforcement (_) disables partner choice and reciprocity while the loci still mutate
and still cost. Indirect reciprocity stands alone as a mechanism (IM, IJM) only under
shuffling, because persistent pairs leave I copying the partner's act toward the focal
individual itself, which is direct reciprocity; alongside partner choice it appears in
the combined mechanisms IMP and IJMPQ. Table S1 reports which payoff gap limits each
mechanism family in the payoff-plane attributions. The control row of Table 1 is a
game type, not a mechanism: under it a partner's act does not change payoffs, while
mechanisms may still be enabled or disabled as in the other games.

## Outcome measures

Outside the temporal comparisons, I record every reported value at the last logged
round (t = 2^20), from the state at the end of that round after payoffs. I use three
measures. The frequency of cooperators is the share of individuals who behave
cooperatively in that round. This is not the frequency of C1 — a C0M1 reciprocator
counts when it copies a partner's cooperation. Fitness is mean w, the floored payoff
net of information cost. Allele and genotype frequencies give the third measure —
active choosers (C1P1), reciprocators that copy a partner (C0M1), unconditional
cooperators that pay no information cost (C1P0, C1M0; C1M0 is the second-order
free-rider under reciprocity), and carriers that never choose (C0P1).

For two populations I report each measure per population and the gap between them.
Where costs differ, the gap is the lower-cooperation-cost population minus the higher;
where costs match and populations are labeled by outcome, it is the more cooperative
minus the less. To summarize who profits, I correlate the two gaps across the cells of
a sweep — the Pearson correlation between the cooperation gap and the fitness gap.
These associations are between-cell relationships across a parameter grid, not
within-cell relationships. A value near minus one means the population that cooperates
more earns less. Under partner choice I also correlate P1 allele frequency with
fitness across cells of a sweep.

Where costs match and both populations play the same game, the two populations start
interchangeable, so I label them by outcome: within each run and snapshot, the more
cooperative population is reported first. That prevents role differences from canceling when averaged across
runs, but it also makes the reported gap a rank statistic, which cannot be zero even
without a real split. To separate that labeling artifact from a true role assignment,
I compare each mechanism's matched-parameter gap to the gap under no enforcement,
ranked the same way, rather than asking whether the gap differs from zero.
Single-replicate runs keep their original labels, so their two curves are not
rank-ordered. Where costs differ, the labels follow the parameters. In the
figures, orange and red curves mark parameter-asymmetric designs (orange for the
lower-cost population, red for the higher-cost population when costs differ).
Green curves mark parameter-symmetric designs or a single population; when two
populations are labeled by outcome, light green is the population with the lower
frequency of cooperators and dark green the other.

## Simulation designs

Unless noted, group size is 128 and partnerships are not shuffled; shuffled partners
and groups of 4 appear in the supplement. All parameter sweeps step by 0.02. The
constraint i + c ≤ b (and i + c₁ ≤ b where c₁ is swept) keeps total cost from exceeding
the cooperation benefit, beyond which cooperation cannot pay even when fully
reciprocated; that bound is what makes those grids triangular. Table 3 lists the
designs; the paragraphs below give the narrative order.

Table 3. Simulation designs.

| Design                      | Pops | Mechanisms (typical)   | Axes / ranges                                      | Step | Cells | Figures        |
| --------------------------- | ---- | ---------------------- | -------------------------------------------------- | ---- | ----- | -------------- |
| Equal-c baseline, one pop   | 1    | \_, M, P, IJMPQ       | c ∈ [0, b]                                         | 0.02 | 21    | Fig. S1; S2    |
| Equal-c baseline, two pops  | 2    | \_, P                 | c₀ = c₁ ∈ [0, b]                                   | 0.02 | 21    | Fig. 1         |
| Cooperation-cost asymmetry  | 2    | \_, P, IJMPQ          | c₀ < c₁; c₀ ∈ [0, 0.38], c₁ ∈ [0.02, 0.40]         | 0.02 | 210   | Figs. 2, S3–S6 |
| Symmetric information cost  | 1    | P, M                   | i + c ≤ b                                          | 0.02 | 231   | Figs. 3, S7–S8 |
| Fixed c-gap × shared i      | 2    | P                      | c₀ = 0.10; i + c₁ ≤ b                              | 0.02 | 120   | Fig. S9        |
| Per-population i, equal c   | 2    | P, IMP, IJMPQ          | c₀ = c₁ = 0.10; i₀ < i₁; each axis ≤ b − c         | 0.02 | 120   | Fig. S11       |
| Crossed c and i asymmetries | 2    | P, MP, MPQ, IMP, IJMPQ | c₀ = 0.10, c₁ = 0.20; i₀ ≤ 0.30, i₁ ≤ 0.20         | 0.02 | 176   | Figs. 4–5, S10 |
| PD payoff plane             | 1    | M, P, combined         | T = 0.90, S = 0.10; R, P with T > R > P > S        | 0.02 | 172   | Table S1       |
| Snowdrift payoff plane      | 1    | M, P, combined         | T = 0.90, P = 0.10; R, S with T > R > S > P        | 0.02 | 172   | Table S1       |

I first establish baselines under equal cooperation cost (Fig. S1; shuffled
short-memory variants in Fig. S2; two-population equal-cost sweep in Fig. 1). I then
vary parameters asymmetrically along one axis at a time: cooperation-cost asymmetry
(Fig. 2 reports the strip c₁ = c₀ + 0.02; full grid Fig. S4; no-enforcement control
Fig. S3; Fig. S5 places that strip beside the matched-cost case of Fig. 1), then
information cost at equal c (Fig. 3; full grid Fig. S7; control game Fig. S8).

The central designs vary who pays an information cost (Fig. S9; Fig. S11; Figs. 4–5
with fitness counterpart Fig. S10). Fig. 4's first two columns hold one population's
information cost at zero and sweep the other's; the third holds total information cost
fixed while the split varies. I also run that crossed design under snowdrift.

Along the cooperation-cost axis, raising c changes several payoff gaps at once. The
orthogonal payoff-plane sweeps vary payoffs independently of c; Table S1 reports the
payoff-gap attribution for each mechanism family rather than publishing the heatmaps.

Every run is logged at nine snapshots: the first round, then eight points spaced
2^17 rounds apart up to 2^20. The 30-run series and the single-replicate companions
over the same grids use those snapshots; each companion is one unaveraged trajectory.

The simulation is written in C and uses the GSL Tausworthe random-number generator,
seeded from the run configuration or from the clock when no seed is supplied.
Simulation code, analysis scripts, and the summary exports behind every figure are
archived in the repository cited on the title page.

## Replicates and variation

Reported values are means over 30 independent runs. Comparisons are descriptive:
I report those means and, where useful, standard deviations, without formal
hypothesis tests. I plotted standard deviations only in Fig. 5; elsewhere median
standard deviations over the cells of a sweep are about 0.01–0.04 for cooperation and
0.001–0.01 for fitness, too small to read on the figure scales, except near bistable
boundaries where run-to-run SD reaches about 0.25 (Fig. 5).
