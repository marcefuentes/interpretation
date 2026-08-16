# Methods

*Constants and payoff equations:
[parameterization](../journal/parameterization.md). Design grid and outcome
definitions: [framework](../journal/framework.md). Numbers cited elsewhere in the
manuscript are regression-checked by `ai/verify_claims.py`.*

## Model

I use an individual-based evolutionary model. Each population holds 4096
individuals — a size divisible by both group sizes used below. Individuals live in
fixed groups, interact in pairs over repeated rounds, and reproduce in proportion to
fitness. Every round each individual dies with probability 2^−7. That mortality is
low enough that lasting partners meet many times (about 64 rounds on average under
noshuffle with partner choice off), yet high enough that runs reach equilibrium in a
tractable time. Dead adults are replaced by offspring sampled from the whole
population in proportion to fitness, so a recruit need not share its parent's group.
The recruit inherits the parent's genotype, subject to mutation, and takes the dead
individual's partner. Mutation rate is 0.01 per locus per reproduction event. Main
runs last 2^20 rounds.

Within each time step the order is fixed: compute fitness; if shuffling is on,
redraw pairs within each group; if partner choice is on, rematch choosers; replace
deaths with fitness-weighted recruits; then, if reciprocity is on, set each
survivor's next act toward its current partner. The next time step begins again with
fitness.

Each individual carries six loci: a cooperation locus C and five mechanism loci
that control conditional behaviour — partner choice on recent (P) or lifetime (Q)
cooperation, and reciprocity that copies a partner's recent act directly (M),
indirectly from a third party (I), or from a lifetime reputation (J). Each locus is
binary — C1 helps its partner, C0 defects; M1 copies its partner, M0 does not; and so
on. An individual behaves according to decision precedence Q1 > P1, and J1 > I1 > M1
when more than one mechanism allele is carried. Per round, fitness is the game payoff
minus information cost, w = max(0, payoff − cost).

Under partner choice, assortment is a bilateral swap: two active choosers (C1P1)
mutually rematch, each trading a non-cooperative partner for the other chooser; the
two abandoned partners end up paired with each other. The partner-choice allele is
phenotypically silent in defectors (C0P1 carries P1 but never chooses). Reciprocity is
not silent in the same way — C0M1 still mimics once a partnership is established.
Mechanisms differ in which behaviours are enabled, not in which loci can mutate: under
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
loci that are behaviourally inert under a given mechanism are still taxed, and
shedding part of a family saves nothing, so families disappear as blocks rather than
locus by locus. The genuinely untaxed cooperator is the full null C1I0J0M0P0Q0;
single-locus proxies such as C1P0 or C1M0 remain taxed if a sibling locus in the same
family is carried.

In two-population sweeps the rate is per population (i₀, i₁): an individual pays its
own population's rate on the families it carries. Unless otherwise swept, i is held at
a negligible 0.001.

## Population structure and ecology

Two population structures are available. In a single population (pop₁), individuals
pair within the population. In two coevolving populations (pop₂), each side has its
own 4096 individuals and all pairing is between populations — the biologically
central mutualism case, and the structure used for every two-population result in the
main text.

Ecological context is group size (4 or 128 individuals per group) and partner
shuffling. Groups are fixed memory segments for the whole run; an individual never
moves to another group. Shuffling only redraws pairings within the same group each
round, whereas noshuffle keeps partnerships stable across rounds until death or a
partner-choice swap. Primary results use noshuffle and group size 128; shuffle and
group size 4 appear as robustness (Figs. S2, S3).

## Independent variables and mechanisms

The design grid is the Cartesian product of social dilemma, cooperation cost (c, or
c₀ and c₁), information cost (i, or i₀ and i₁), group size, partner shuffling,
population structure, and mechanism
([framework](../journal/framework.md)). Mechanisms enable subsets of the conditional
behaviours: no enforcement (_); direct reciprocity (M); partner choice (P); and the
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
