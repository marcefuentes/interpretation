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
Runs last 2^20 rounds.

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

Baseline fitness K = 0.5 and benefit b = 0.4 are fixed; cooperation cost c is swept
from 0 to b. Table 1 gives the three payoff structures. In the control, an
individual's payoff does not depend on its partner's behavior. In the prisoner's
dilemma, cooperation delivers benefit b to the partner. In the snowdrift, b is a
shared resource received whenever at least one player cooperates.

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
groups of 4 are in Figs. S2 and S6. Fig. S1 compares no enforcement, M, P, and IJMPQ
at equal cooperation cost; each sustains cooperation to a higher cost before collapse,
in that order. Main-text figures use that four-mechanism set: no enforcement as a
control, M and P for single-family contrasts, and IJMPQ as the combined case that
includes reciprocity.

## Outcome measures

I report the frequency of cooperators: the share of individuals who behave
cooperatively in a given round. This is not the frequency of C1 — a C0M1 reciprocator
counts when it copies a partner's cooperation. Fitness is mean payoff minus
information cost.

## Simulation designs

I report six main designs and two auxiliary payoff-plane calibrations.

Equal cooperation cost (c₀ = c₁) in a single population and in two coevolving
populations, across the control, prisoner's dilemma, and snowdrift, yields the
baseline comparison of cooperation-cost ceilings by mechanism (Fig. S1) and the
stochastic two-population split
(Fig. 1). Unequal cooperation cost in two coevolving populations, with c₀ < c₁ over
210 cost pairs, yields the deterministic role split (Fig. 2; full grid Fig. S4;
no-enforcement control Fig. S3). Jointly varying information cost and cooperation
cost at equal c, under the constraint i + c ≤ b, yields decoupling at c = 0 (Fig. 3)
and the surface on which the two costs compound (Fig. S7), with a dilemma-free control
(Fig. S8). Holding c₀ = 0.10 and jointly varying i with c₁ (i + c₁ ≤ b) shows how the
partner-choice split compresses once the zero-cost refuge is removed (Fig. S9).
Per-population information cost at equal cooperation cost (c₀ = c₁ = 0.10; i₀ < i₁
with each axis capped at b − c) assigns roles and can invert them by hitchhiking
without a cooperation-cost gap (Fig. S11). Crossing both asymmetries (c₀ = 0.10,
c₁ = 0.20 fixed; full i₀ × i₁ square, 176 combinations) separates own from partner
information cost and shows non-additive sharing of a fixed information-cost budget
(Fig. 4), including the near-zero-i₀ hitchhiking regime (Fig. 5).

Auxiliary payoff-plane calibrations hold two payoffs fixed and vary the other two,
decoupling temptation, risk, and R − P. They support the payoff-gap attributions in
the Results and Table S1 but are not published as figures.

Single-run time series record nine snapshots from t = 131072 to 10⁶. That spacing is
enough to confirm that role splits and collapses are already locked in at the first
recorded snapshot, but not to resolve the order in which they first appear.

## Replicates and noise floor

Reported values are means over 30 independent runs, each with its standard
deviation. The practical noise floor is cooperation gaps below
approximately 0.01–0.02 and fitness gaps below approximately 0.002; standard deviation
peaks at bistable transitions (visible as the ±1 SD bands in Fig. 5).
