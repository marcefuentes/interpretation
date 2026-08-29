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
whole population in proportion to fitness; the offspring inherits the parent's
genotype, subject to mutation, fills the vacant slot, and takes the dead individual's
partner. Recruitment is the only route between groups, and an offspring need not
share its parent's group. Mutation rate is 0.01 per locus per reproduction event.
Each run lasts 2^20 rounds.

Each individual carries six loci: a cooperation locus C and five mechanism loci
that control conditional behavior — partner choice on recent (P) or lifetime (Q)
cooperation, and reciprocity that copies a partner's recent act directly (M),
indirectly from a third party (I), or from a lifetime reputation (J). Each locus is
binary — C1 helps its partner, C0 defects; M1 copies its partner, M0 does not; and so
on. An individual behaves according to decision precedence Q1 > P1, and J1 > I1 > M1
when it carries more than one mechanism allele.

Under partner choice, assortment is a bilateral swap: two active choosers (C1P1)
mutually rematch, each trading a non-cooperative partner for the other chooser; the
two abandoned partners end up paired with each other. The partner-choice allele is
phenotypically silent in defectors (C0P1 carries P1 but never chooses). Reciprocity is
not silent in the same way — C0M1 still mimics once a partnership is established.

## Social dilemmas

Cooperation cost c is what a cooperator pays to produce the good at stake in the
dilemma. In the prisoner's dilemma that good is given to the partner; in the
snowdrift it is shared between the pair whenever at least one player cooperates.
Baseline fitness K = 0.5 and benefit b = 0.4 are fixed; c is swept from 0 to b.
Table 1 gives the three payoff structures. In the control, an individual's payoff
does not depend on its partner's behavior.

Table 1. Payoff structures for the three social dilemmas.

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

In two-population designs the rate is per population (i₀, i₁): an individual pays its
own population's rate on the families it carries. Unless otherwise varied, i is held
at a negligible 0.001.

Mechanisms differ in which behaviors are enabled, not in which loci can mutate: under
the no-enforcement control, partner choice and reciprocity do not run, but mechanism
loci still mutate and still incur information cost when carried.

## Timestep order

Per round, fitness is the game payoff minus information cost, w = max(0, payoff − cost),
with payoff from Table 1. Within each time step the order is fixed: compute fitness; if
shuffling is on, redraw pairs within each group; if partner choice is on, rematch
choosers; replace deaths with fitness-weighted offspring; then, if reciprocity is on,
set each survivor's next act toward its current partner. The next time step begins
again with fitness.

## Independent variables and mechanisms

I vary the parameters above together with which conditional behaviors are enabled.
Mechanisms are abbreviated by the loci they enable: no enforcement (none of the
conditional behaviors run); direct reciprocity (M); partner choice (P); and the
combined and reputation-rich families (MP, MPQ, IMP, IJMPQ). Indirect reciprocity with
recent (IM) or lifetime (IJM) reputation is included only when partners are
shuffled. Main-text results use groups of 128 without shuffling; shuffled partners and
groups of 4 are in Figs. S2 and S6. Fig. S1 reports no enforcement, M, P, and IJMPQ
at equal cooperation cost; main-text figures use that four-mechanism set: no
enforcement as a control, M and P for single-family contrasts, and IJMPQ as the
combined case that includes reciprocity.

## Outcome measures

I report the frequency of cooperators: the share of individuals who behave
cooperatively in a given round. This is not the frequency of C1 — a C0M1 reciprocator
counts when it copies a partner's cooperation. Fitness is mean payoff minus
information cost.

## Simulation designs

Six sweeps vary cooperation cost, per-population information cost, or both; two
further sweeps vary the payoffs themselves. All use the ecology above. Unless
noted, group size is 128, partnerships are not shuffled, information cost is
i = 0.001, and two-population designs pair one coevolving population on each side
of the interaction.

Equal cooperation cost (c₀ = c₁) is swept from 0 to b in one population and in two
coevolving populations, for the control, prisoner's dilemma, and snowdrift (Fig. S1;
Fig. 1). Cooperation-cost asymmetry fixes c₀ < c₁ on a grid of 210 ordered pairs with
c₀ ∈ [0, 0.38] and c₁ ∈ [0.02, 0.40] (Fig. 2; full grid Fig. S4; no-enforcement
control Fig. S3). Information cost and cooperation cost are varied jointly at equal c
under i + c ≤ b on a triangular grid of 231 (i, c) cells (Fig. 3; full grid Fig. S7;
dilemma-free control Fig. S8). With c₀ fixed at 0.10, information cost and c₁ are
jointly swept under i + c₁ ≤ b (120 cells; Fig. S9). Per-population information cost
is swept at fixed c₀ = c₁ = 0.10 on a triangle with i₀ < i₁ and each axis capped at
b − c (120 cells; Fig. S11). Both asymmetries are crossed with c₀ = 0.10, c₁ = 0.20,
and all (i₀, i₁) pairs on a 176-cell square with i₀ ≤ 0.30 and i₁ ≤ 0.20 (Figs. 4–5).

The payoff-plane sweeps hold two payoffs fixed and vary the other two, which breaks
the coupling that cooperation cost imposes on the temptation, risk, and
cooperation-advantage gaps at once. The prisoner's-dilemma sweep fixes T = 0.90 and
S = 0.10 and varies R and P over an 18 × 18 grid, keeping the 172 cells that satisfy
T > R > P > S; the snowdrift sweep fixes T = 0.90 and P = 0.10 and varies R and S
over the same grid, keeping the 172 cells that satisfy T > R > S > P. Table S1
reports which payoff gap limits each mechanism family.

Selected cells are re-run with a single replicate and sampled at nine time points from
2^17 to 10⁶ rounds to check temporal stability of the reported equilibria.

## Replicates and noise floor

Reported values are means over 30 independent runs, each with its standard
deviation. The practical noise floor is cooperation gaps below
approximately 0.01–0.02 and fitness gaps below approximately 0.002; standard
deviation peaks at bistable transitions (visible as the ±1 SD bands in Fig. 5).
