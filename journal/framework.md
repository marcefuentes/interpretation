# Analytical Framework — Independent Variables and Outcome Variables

This note fixes the conceptual model the rest of the journal and the paper draft
are organised around. It separates what we *set* (independent variables) from what
we *measure* (outcome variables), so every result can be stated as an outcome as a
function of a position on the independent-variable grid.

The project question: how does cooperation evolve, and how does the presence of a
second, potentially mutualistic population change that evolution, across social
dilemmas, cost constraints, and ecological contexts?

## Independent variables (the knobs we set)

These are the axes of the simulation design. A "cell" of the study is one
combination of them, and every study is a sweep over some subset.

- **Social dilemma.** The payoff ordering of the game: control (no social dilemma,
  folder 0), prisoner's dilemma (folder 1), or snowdrift (folder 2). See
  parameterization.md for the payoff equations.
- **Cooperation cost c.** The cost paid by a focal individual when it helps a
  partner. In asymmetric_c0_c1 the two populations can carry different costs c0 and c1;
  the symmetric_c study sits on the equal-cost diagonal c0 = c1 = c. This is the *demand* for
  enforcement: higher c is higher temptation and higher risk.
- **Information cost Cost.** The per-round metabolic/cognitive overhead of carrying
  reciprocity or partner-choice machinery, charged once for a partner-choice family
  (P/Q loci) and once for a reciprocity family (M/I/J loci), independent of the game
  payoffs. This is information cost. Swept in symmetric_c_i (symmetric
  c0 = c1) and asymmetric_c1_i (fixed c0, swept c1).
- **Ecological context.** Groupsize (4 vs 128 individuals per group), partner
  shuffling (stable pairings vs within-group re-draw each round), and population
  structure (see below).
- **Mechanism.** Which enforcement loci are active: control (_), direct reciprocity
  (M), partner choice (P), and the combined and reputation-rich families
  (MP, MPQ, IMP, IJMPQ, and the shuffle-only IM, IJM).

### Population structure is the axis this project is built around

- **pop_1** — a single population; individuals pair within it.
- **pop_2** — two coevolving populations; all pairing is between populations. This
  is the asymmetric_c0_c1 case, and the one where the second population can genuinely
  change the evolutionary outcome.
- **pop_3** — one evolving population against a fixed partner (held at 25% of each
  genotype). Provably redundant with symmetric_c pop_3 (see synthesis.md and the
  asymmetric_c0_c1_pop_3 checks in ai/verify_claims.py), because the frozen partner gives
  the evolving population's cost the only dynamical role.

The single-population case (pop_1, and its equal-cost (c0 = c1) generalisation, the symmetric_c study) is the
baseline; the two-population case (pop_2, asymmetric_c0_c1) is the biologically central
question. Comparing them is the project's spine.

## Outcome variables (what we measure)

Three outcomes carry the analysis. Each is measured per cell of the
independent-variable grid.

### 1. Level of cooperation

The frequency of cooperative acts, qBSeen. This is the primary readout everywhere:
where each mechanism sustains cooperation, and where it collapses as c (or Cost)
rises. The prisoners and snowdrift calibration sweeps exist to attribute a given
collapse to a specific payoff gap (temptation, risk, or the cooperation advantage
R minus P); see synthesis.md.

### 2. Between-population asymmetry

Only defined for two populations (pop_2, and pop_3's evolving-vs-fixed contrast). It
has two faces that can point at different populations, so we track both:

- **Cooperation asymmetry** — the gap in qBSeen between the two populations.
- **Exploitation / fitness asymmetry** — the gap in fitness (wmean), i.e. which
  population actually profits. The sharper signal: under partner choice in the PD,
  carrying the chooser allele correlates with fitness at roughly minus one (the
  cooperating side is the exploited side, the paradox of success). The snowdrift
  branch can even split the two faces onto different populations.

In symmetric_c pop_2 (symmetric payoffs) the role split is stochastic; in asymmetric_c0_c1
pop_2 (built-in c0 < c1 asymmetry) it is deterministic, with the lower-cost
population taking the cooperator role. Same outcome, two routes.

### 3. Genotype composition / route to cooperation

Not *how much* cooperation but *what produces it* — the genotype frequencies behind
the behaviour. This captures findings invisible to level and asymmetry alone:

- **Behaviour vs machinery decoupling.** Under information cost, cooperation can stay
  high while the enforcement alleles (P1, M1) are selected out, the niche taken over
  by tax-free unconditional cooperators (C1P0, C1M0). See symmetric_c_i.md.
- **Mechanism identity.** Partner choice acts as population-level assortment; direct
  reciprocity acts as individual-level history. A residual chooser minority protects
  the whole population; a residual reciprocator minority protects only itself.
- **Free-riding and silent carriers.** Second-order free-riding (C1M0 riding on the
  punishment C1M1 supplies) and silent carriers (C0P1 accumulating by mutation).

## What we deliberately do not treat as an outcome

- **Temporal regime / oscillations.** The single-run studies show absorbing states
  and one-time tipping events, not cyclic dominance, and this regime does not change
  between one and two populations. The current instrumentation (30-run averaging plus
  nine coarse snapshots) could not resolve oscillation even if present. We keep this
  as an open question, not a measured outcome; resolving it would need dense
  early-time logging on single runs.

## How the studies populate the grid

| Study | Independent-variable coverage | Primary purpose |
| ----- | ----------------------------- | --------------- |
| asymmetric_c0_c1 | pop_2, 2D c0 x c1 triangle, dilemmas 1/2, both groupsizes, shuffle/noshuffle, all mechanisms | Primary: two-population cooperation and asymmetry |
| symmetric_c | pop_1/2/3, c0 = c1 sweep, dilemmas 0/1/2, both groupsizes, shuffle/noshuffle, all mechanisms | The equal-cost special case; single-population baseline |
| symmetric_c_i | adds the Cost axis (Cost x c triangle) to symmetric_c | Information cost vs cooperation cost (symmetric) |
| asymmetric_c1_i | pop_2, fixed c0 = 0.10, Cost x c1 triangle | Price vs demand under exploitation asymmetry |
| prisoners | (R, P) payoff-plane sweep, PD | Attribute c-collapses to temptation / risk / R minus P |
| snowdrift | (R, S) payoff-plane sweep, snowdrift | Confirm the low-risk (high S) attribution from the other side |
| *_1run | single-run variants of the above | Temporal dynamics (limited resolution) |
