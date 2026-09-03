# Methods

## Model

I use an individual-based evolutionary model with two population structures. In a
single population, individuals pair within the population. In two coevolving
populations, pairing is between populations.

Individuals live in fixed groups of 4 or 128. Groups bound local interaction in two
ways. When partner choice is on, a chooser can rematch only within its group. When
shuffling is on, pairs are redrawn within the group each round; without it,
partnerships persist until death or a partner-choice swap. In a single population a
group holds that many individuals from the population. In the two-population case it
holds that many from each population, so each individual faces that many potential
partners from the other side.

Each population holds 4096 individuals — a size divisible by both group sizes.
Adults never change group. Every round each individual dies with probability 2^−7.
That mortality is low enough that lasting partners meet many times (about 64 rounds on
average when individuals do not change partners), yet high enough that runs reach
equilibrium in a tractable time. Dead adults are replaced by offspring drawn from the
whole population in proportion to fitness via roulette-wheel selection on cumulative
round fitness. Reproduction is asexual and haploid: the offspring clones one parent's
genotype, subject to mutation, fills the vacant slot, and takes the dead individual's
partner. Recruitment is the only route between groups, and an offspring need not
share its parent's group. Mutation rate is 0.01 per locus per reproduction event.
Each run lasts 2^20 rounds.

Each individual carries six binary loci: a cooperation locus C and five
mechanism loci that control conditional behavior. Allele C1 is the default act
— cooperate unconditionally when no mechanism overrides it; C0 defects. The
mechanism loci are partner choice on recent cooperation (P) or lifetime
cooperation rate (Q), and reciprocity — including tit-for-tat, third-party
indirect reciprocity, and image scoring — that copies a partner's previous-round
act when the partnership is unbroken (M), copies the current partner's
previous-round act without requiring partnership continuity (I), or adopts that
partner's lifetime reputation as its act by rounding the rate to cooperate or
defect (J). M1 copies, M0 does not; and so on for the other mechanism alleles.
Recent cooperation is the last act played; lifetime reputation is the running
mean of those acts since birth. An individual behaves according to decision
precedence Q1 > P1 within partner choice and J1 > I1 > M1 within reciprocity
when it carries more than one mechanism allele in the same family. Partner
choice and reciprocity are applied at separate stages of each round (below), so
precedence across families never arises.

Under partner choice, P1 rematches only if it cooperated while its current partner
defected in the previous round; Q1 rematches when each of two individuals prefers
the other on lifetime cooperation rate. Assortment is a bilateral swap. For P,
active choosers within a group are shuffled and paired in adjacent pairs; if their
number is odd, one does not rematch that round; each trades a non-cooperative
partner for the other chooser, and the two abandoned partners end up paired with
each other. The partner-choice allele is phenotypically silent in defectors (C0P1
carries P1 but never chooses). Reciprocity is not silent in the same way — C0M1
still mimics once a partnership is established.

At run start every individual carries the null allele at all six loci and defects.
Pairs are assigned within groups (and across populations in the two-population form)
before the first round. Diversity enters only through mutation; there is no external
seeding of cooperative or mechanism alleles.

## Social dilemmas

Cooperation cost c is what a cooperator pays to produce the good at stake in
the dilemma. In the prisoner's dilemma that good is given to the partner; in
the snowdrift it is shared between the pair whenever at least one player
cooperates. Under the control payoff structure, nothing is shared and an
individual's payoff does not depend on its partner's behavior. Baseline fitness
K = 0.5 and benefit b = 0.4 are fixed; c is swept from 0 to b. Table 1 gives
the three payoff structures. 

Table 1. Payoff structures for the three social settings.

| Game structure           | T (temptation) | R (reward)  | P (penalty) | S (sucker) | T − R (temptation gap) | P − S (risk)  | R − P (cooperation advantage)  |
| ------------------------ | -------------- | ----------- | ----------- | ---------- | ---------------------- | ------------- | ------------------------ |
| Control (no dilemma)     | K              | K + b − c   | K           | K + b − c  | c − b (rises)          | c − b (rises) | b − c (shrinks)          |
| Prisoner's dilemma       | K + b          | K + b − c   | K           | K − c      | c (rises)              | c (rises)     | b − c (shrinks)          |
| Snowdrift                | K + b          | K + b − c/2 | K           | K + b − c  | c/2 (rises slowly)     | c − b (rises) | b − c/2 (shrinks slowly) |

Note: Columns T − R, P − S, and R − P show how each gap changes as cooperation cost c
rises.

In the two-population form each population pays its own cooperation cost (c₀, c₁), with
c₀ < c₁ whenever they are asymmetrical. The lower-cost population always has the
larger cooperation advantage (R − P).

## Information cost

Information cost is charged every round on the *families* of mechanism loci carried,
not per locus and not on machinery used:

cost = i × ( (P ∨ Q) + (M ∨ I ∨ J) ).

An individual therefore owes 0, 1 or 2 units of i. Carrying both partner-choice
loci costs the same as carrying one; carrying all three reciprocity loci costs
the same as carrying one. Direct reciprocity and partner choice each cost one
unit; carrying at least one partner-choice family allele and at least one
reciprocity family allele costs two units (one per family), however many loci
each family enables — so contrasts within those matched sets isolate mechanism
identity from expense. Loci that are behaviorally inert under a given mechanism
are still taxed, and shedding part of a family saves nothing, so families
disappear as blocks rather than locus by locus. The genuinely untaxed
cooperator is the full null C1I0J0M0P0Q0; single-locus proxies such as C1P0 or
C1M0 remain taxed if a sibling locus in the same family is carried.

In two-population designs the rate is per population (i₀, i₁): an individual pays its
own population's rate on the families it carries. Unless otherwise varied, i is held
at a negligible 0.001.

Different runs enable different sets of conditional behaviors. A P1 individual
rematches only when partner choice is on for that run; an M1, I1, or J1
individual copies only when reciprocity is on. Under the no-enforcement
mechanism neither family runs. Enabling behaviors independently lets me test
each mechanism and combinations of them.

## Timestep order

Per round, an individual's act toward its current partner is the value set at the end
of the previous round — or, for a newborn, its inherited C allele at replacement.
Fitness is the game payoff minus information cost, w = max(0, payoff − cost), with
payoff from Table 1 evaluated on that act and the partner's act. Within each time step
the order is fixed: compute fitness from current acts; if shuffling is on, redraw
pairs within each group; if partner choice is on, rematch choosers; replace deaths
with fitness-weighted offspring (each newborn's act is reset to its inherited C
allele); then, if reciprocity is on, set each survivor's act toward its current
partner for the next round. The next time step begins again with fitness.

When reciprocity is disabled, an individual's act equals its C allele, fixed at birth
and unchanged until death. When reciprocity is enabled, each round's act starts from
C and is overridden only by active M, I, or J alleles.

## Independent variables and mechanisms

I vary the parameters above together with which conditional behaviors are enabled.
Mechanisms are abbreviated by the loci they enable: direct reciprocity (M); partner
choice (P); combined and reputation-rich families (MP, MPQ, IMP, IJMPQ); and no
enforcement, where conditional behaviors are disabled while loci still mutate.
Combined labels name which locus families are enabled; Table S1 lists the compositions
used in the payoff-plane attributions. Indirect reciprocity with recent (IM) or
lifetime (IJM) reputation is included only when partners are shuffled. The control
payoff structure (Table 1, first row) is separate from mechanism choice: under it, a
partner's behavior does not change payoffs. Main-text results use groups of 128
without shuffling; shuffled partners and groups of 4 are in Figs. S2 and S6. Fig. S1
reports no enforcement, M, P, and IJMPQ at equal cooperation cost; main-text figures
use that four-mechanism set. Fig. 3 compares P and M only; Fig. S8 pairs M with the
control payoff structure to test whether machinery erosion requires a dilemma.

## Outcome measures

I report the frequency of cooperators: the share of individuals who behave
cooperatively in a given round. This is not the frequency of C1 — a C0M1 reciprocator
counts when it copies a partner's cooperation. Fitness is mean payoff minus
information cost.

## Simulation designs

Six sweeps vary cooperation cost, per-population information cost, or both; two
further sweeps vary the payoffs themselves. Unless noted, group size is 128,
partnerships are not shuffled, and information cost is i = 0.001. The constraint
i + c ≤ b (and i + c₁ ≤ b where c₁ is swept) keeps total cost from exceeding the
cooperation benefit.

### Equal cooperation cost

Equal cooperation cost (c₀ = c₁) is swept from 0 to b in one population and in two
coevolving populations, for the control payoff structure, prisoner's dilemma, and
snowdrift (Fig. S1; Fig. 1).

### Cooperation-cost asymmetry

Cooperation-cost asymmetry fixes c₀ < c₁ on a grid of 210 ordered pairs with
c₀ ∈ [0, 0.38] and c₁ ∈ [0.02, 0.40] (Fig. 2; full grid Fig. S4; no-enforcement
mechanism Fig. S3).

### Information cost and cooperation cost

Information cost and cooperation cost are varied jointly at equal c under i + c ≤ b
on a triangular grid of 231 (i, c) cells (Fig. 3; full grid Fig. S7; M under the
control payoff structure Fig. S8).

### Information cost under cooperation-cost asymmetry

With c₀ fixed at 0.10, information cost and c₁ are jointly swept under i + c₁ ≤ b
(120 cells; Fig. S9).

### Per-population information cost

Per-population information cost is swept at fixed c₀ = c₁ = 0.10 on a triangle with
i₀ < i₁ and each axis capped at b − c (120 cells; Fig. S11).

### Crossed asymmetries

Both asymmetries are crossed with c₀ = 0.10, c₁ = 0.20, and all (i₀, i₁) pairs on a
176-cell square with i₀ ≤ 0.30 and i₁ ≤ 0.20 (Figs. 4–5).

### Payoff-plane sweeps

The payoff-plane sweeps hold two payoffs fixed and vary the other two, which breaks
the coupling that cooperation cost imposes on the temptation, risk, and
cooperation-advantage gaps at once. Each runs in a single population (30 runs per
cell) over the mechanism families in Table S1. The prisoner's-dilemma sweep fixes
T = 0.90 and S = 0.10 and varies R and P over an 18 × 18 grid, keeping the 172 cells
that satisfy T > R > P > S; the snowdrift sweep fixes T = 0.90 and P = 0.10 and
varies R and S over the same grid, keeping the 172 cells that satisfy T > R > S > P.
Table S1 reports which payoff gap limits each mechanism family.

### Temporal companions

Each main sweep has a single-replicate companion over the same parameter grid,
logged at nine evenly spaced snapshots (t = 1, 2^17, …, 2^20 rounds). These
trajectories check that reported equilibria are stable once established rather than
late erosions, and under matched costs in two populations they distinguish
early-locking role assignment and within-run metastability from slow drift. Which
population becomes cooperator under parameter symmetry is a 30-run question; a
single companion shows only one realized split.

## Replicates and variation

Reported values are means over 30 independent runs. I also computed standard
deviations but plotted them only in Fig. 5, where run-to-run spread is largest;
elsewhere they are typically too small to read on the figure scales (median
cooperation SD ≈ 0.01–0.04; fitness SD ≈ 0.001–0.01). Spread peaks where runs split
between attractors (Fig. 5). Cooperation differences below about 0.01–0.02 and fitness
differences below about 0.002 fall within run-to-run variation and are not treated as
meaningful effects.
