# Mutualism Cost — Information Price Meets Exploitation Asymmetry

**Status: partial data** — mutualism_cost_1run is ~73% complete on the primary slice
(noshuffle, gs = 128; MPQ and IJMPQ still missing); mutualism_cost (Runs = 30) not
yet started. This document records the study design, open questions, and manuscript role.

## The gap hamilton_cost leaves open

hamilton_cost answers the **price–demand** question for symmetric populations:
c0 = c1 = c, pops 1/2/3. It shows that information cost Cost (the *price* of
carrying enforcement machinery) and cooperation cost c (the *demand* for that
machinery) interact non-additively — machinery erodes supply-side when Cost rises,
while the social dilemma sets whether losing the apparatus drags behaviour down
(see hamilton_cost.md, especially the dilemma-0 control decomposition).

That sweep cannot tell us what happens when **asymmetry is built in**. In mutualism
pop_2 the lower-cost population (c0) is the natural cooperator and the higher-cost
population (c1) the exploiter. hamilton_cost pop_2 only covers the diagonal c0 = c1,
where the role split is stochastic. We therefore have no data on:

- whether taxing the machinery **widens or narrows** the cooperation and fitness gaps
  between the two populations;
- whether behaviour–machinery decoupling (C1P0 / C1M0 niches) appears on the
  **cooperator side, the exploiter side, or both**;
- whether the price–demand interaction is the same when enforcement must sustain
  **cross-population** cooperation rather than within-population assortment.

mutualism_cost closes that gap with the same Cost axis, but on the asymmetric
c0 < c1 branch mutualism already uses.

## What we are waiting for

Two studies, mirroring the hamilton_cost pair:

| Study | Runs | Purpose |
| ----- | ---- | ------- |
| mutualism_cost_1run | 1 | Temporal dynamics; run first |
| mutualism_cost | 30 | Equilibrium averages for the paper |

**Population structure:** pop_2 only (two coevolving populations). Same mechanism
layout as mutualism: mutualism_short + mutualism_long layouts (9 mechanisms, dilemmas
0/1/2 for _ and M, 1/2 for the rest, gs = 4 and 128, shuffle and noshuffle).

**Fixed cooperation cost for population 0:**

- c0 = **0.10** (the lower-cost, cooperator-role population)

**Swept axes (120 valid cells per leaf directory):**

- **Cost** — information cost of the machinery, same 21-point ladder as hamilton_cost:
  {0.00, 0.02, 0.04, …, 0.40}
- **c1** — cooperation cost of population 1 (the higher-cost, exploiter-role side),
  values with c1 > c0: {0.12, 0.14, …, 0.40}

**Triangular constraint:** Cost + c1 ≤ b = 0.40 (equivalently Cost ≤ b − c1), so the
costlier population still profits from cooperation. Cost values ≥ 0.30 yield no valid
pairs. Total: 120 (Cost, c1) combinations per mechanism × dilemma × ecology cell;
~8,640 input files across both layouts (vs ~111k for a full c0 × c1 × Cost sweep).

**Everything else** matches mutualism / hamilton_cost: K = 0.5, b = 0.4,
MutationRate = 0.01, Time = 20, Periods = 3.

## The price–demand questions this sweep is designed to answer

### 1. Supply vs demand under asymmetry

At fixed c0 = 0.10, raising c1 increases *demand* on the exploiter side; raising
Cost increases *price* on both sides' machinery carriers. We can ask:

- Does cooperation collapse on the **c1 axis**, the **Cost axis**, or their
  **interaction** — and is the collapse threshold on c1 shifted by Cost the same
  ~1.5 c-units per Cost-unit seen on the hamilton diagonal?
- Does the dilemma-0 control (no social dilemma) again isolate pure supply-side
  erosion, with asymmetry pinned by c0 < c1 rather than temptation?

### 2. Between-population asymmetry (outcome 2)

With c0 fixed below c1, mutualism already gives a deterministic cooperator/exploiter
split. Under information cost we can measure:

- **Cooperation gap** — does Cost widen the qBSeen difference between populations,
  or does decoupling (unconditional cooperators on the cheap side) compress it?
- **Fitness gap** — does taxing partner-choice machinery on the cooperator side
  change who profits, or only how much?

Compare directly to hamilton_cost pop_2 at c0 = c1 = 0.10 (symmetric diagonal point)
and to mutualism at Cost = 0.001 (no information tax).

### 3. Genotype composition / decoupling (outcome 3)

hamilton_cost shows machinery alleles (P1, M1) erode while C1P0 / C1M0 rise, but only
when c is low enough that unconditional cooperation is viable. With asymmetry:

- Does decoupling appear **only on the low-c0 cooperator side**, or also on the
  high-c1 exploiter side?
- Does partner choice still act as population-level assortment (residual choosers
  protecting both populations) when the two populations face different c?

### 4. Manuscript scope (decision locked 2026-07)

We originally considered two articles:

- **Price–demand** — hamilton + hamilton_cost: Cost versus c, behaviour–machinery
  decoupling, symmetric populations.
- **Asymmetry / exploitation** — mutualism + hamilton (diagonal): cooperator/exploiter
  role split, cooperation and fitness gaps at negligible Cost.

mutualism_cost belongs with the **price–demand** thesis, not as a separate asymmetry
paper: it is the same Cost axis on the branch where roles are pinned by c0 < c1. A
price–demand article that used only hamilton data could not test that interaction
without extrapolating from the stochastic role split on the c0 = c1 diagonal; an
asymmetry-only article at Cost ≈ 0 could not say how taxing enforcement modulates
exploitation.

**Decision:** one manuscript covering everything — baseline demand (hamilton +
mutualism), built-in roles (mutualism; hamilton as the symmetric special case), then
price–demand in one and two populations (hamilton_cost + mutualism_cost). See
paper/roadmap.md for the narrative arc.

Provisional 1-run preview (noshuffle, gs = 128, PD): Cost = 0 matches mutualism within
noise; cooperation and fitness gaps between populations compress as Cost rises; c1-collapse
thresholds retreat with Cost similarly to hamilton_cost. Full claims await the 30-run study.

## When results arrive

1. Run graphgen on mutualism_cost_1run then mutualism_cost (image .con first;
   movies if needed for temporal claims).
2. Write ai/analyze_mutualism_cost.py (mirror analyze_hamilton_cost.py structure:
   Cost × c1 grid at fixed c0, control decomposition, asymmetry panels).
3. Add verify_claims.py regression checks for headline numbers.
4. Update synthesis.md, framework.md, and paper/results.md.

## Pipeline location

Study definitions live in ~/code/cesga/python/studies/mutualism_cost/ and
mutualism_cost_1run/. Generate with:

```
python create.py --study mutualism_cost_1run --layout mutualism_short
python create.py --study mutualism_cost_1run --layout mutualism_long
```

(same with mutualism_cost for the 30-run study).
