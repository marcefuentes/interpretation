# Mutualism Cost — Information Price on the Asymmetric Branch

asymmetric_c1_Cost extends the information-cost axis to the branch where the
cooperator/exploiter roles are already pinned by payoff asymmetry. It uses the
asymmetric_c0_c1 pop_2 ecology, fixes c0 = 0.10 for the low-cost population, and sweeps
Cost jointly with c1 over the triangle Cost + c1 <= 0.40, c1 > c0. The cell key
is therefore (Cost, c1), with pop_0 the cheap side and pop_1 the expensive side.

This is the missing asymmetric counterpart to symmetric_c_Cost. On the diagonal
c0 = c1, symmetric_c_Cost asks how the price of the machinery interacts with the
demand for that machinery in symmetric populations. asymmetric_c1_Cost asks the same
question when the cheap population is already the natural cooperator and the
expensive one the natural exploiter.

For the cross-study payoff-axis interpretation, see [synthesis.md](synthesis.md).
For the symmetric Cost x c sweep, see [symmetric_c_Cost.md](symmetric_c_Cost.md).

## Design and sanity

- Study pair: asymmetric_c1_Cost (Runs = 30 image summaries) and asymmetric_c1_Cost_1run
  (single-run temporal movies).
- Population structure: pop_2 only.
- Sweep: Cost in {0.00, 0.02, ..., 0.28}; for each Cost, c1 in
  {0.12, 0.14, ..., 0.40 - Cost}. That gives 120 valid (Cost, c1) cells.
- Primary condition below unless noted: PD, noshuffle, gs = 128.

Along sampled Cost = 0 cells the new study reproduces the corresponding mutualism
slice at c0 = 0.10 within the usual noise floor: for mechanism P at c1 = 0.20,
pop_0 is 0.603 here versus 0.599 in mutualism, and pop_1 is 0.178 versus 0.187.
At the low-asymmetry edge c1 = 0.12, the symmetric diagonal remains the right
reference point: M, IMP, and IJMPQ are almost unchanged from symmetric_c_Cost pop_2
at c = 0.10 (for IJMPQ, 0.962 / 0.961 on the diagonal versus 0.961 / 0.961 here),
while P immediately splits into the familiar cooperator/exploiter pair
(0.763 / 0.286).

## Headline: the harmless pure-Cost edge disappears

The key difference from symmetric_c_Cost is simple: there is no c = 0 refuge here.
Even the cheap population always pays c0 = 0.10, so shedding the machinery is
never harmless. On the diagonal, Cost alone only slowly erodes cooperation because
the population can fall back onto tax-free unconditional cooperators. On the
asymmetric branch, Cost is immediately paid in behavior because the game still
demands enforcement.

The PD means over each available c1 column show the contrast:

| Mechanism | Pop | Cost=0 | Cost=0.04 | Cost=0.08 | Cost=0.12 | Cost=0.20 |
| --------- | --- | -----: | --------: | --------: | --------: | --------: |
| M         | 0   | 0.689  | 0.336     | 0.061     | 0.056     | 0.053     |
| M         | 1   | 0.641  | 0.283     | 0.032     | 0.031     | 0.035     |
| P         | 0   | 0.469  | 0.391     | 0.333     | 0.194     | 0.049     |
| P         | 1   | 0.140  | 0.151     | 0.152     | 0.102     | 0.032     |
| IMP       | 0   | 0.655  | 0.579     | 0.353     | 0.263     | 0.058     |
| IMP       | 1   | 0.499  | 0.451     | 0.187     | 0.142     | 0.038     |
| IJMPQ     | 0   | 0.708  | 0.599     | 0.413     | 0.314     | 0.080     |
| IJMPQ     | 1   | 0.549  | 0.430     | 0.225     | 0.163     | 0.053     |

Two features dominate.

First, Cost is much harsher here than on the diagonal. M is the clearest example:
its means start high at Cost = 0 (0.689 / 0.641) but by Cost = 0.08 it is already
at the control floor (0.061 / 0.032). There is no long shallow decline analogous
to symmetric_c_Cost's c = 0 edge, because there is no edge where enforcement can be
shed without consequence.

Second, the combined mechanisms still rank highest, but their advantage is now
about how long they can postpone collapse, not about surviving an otherwise benign
Cost axis. IJMPQ remains the best mechanism at every Cost shown, but even it is
driven to 0.080 / 0.053 by Cost = 0.20.

## Cost lowers the c1 ceiling

The cleanest readout is the maximum c1 each population can tolerate while staying
above qBSeen = 0.5:

| Mechanism | Pop | Cost=0 | Cost=0.04 | Cost=0.08 | Cost=0.12 |
| --------- | --- | -----: | --------: | --------: | --------: |
| M         | 0   | 0.34   | 0.22      | none      | none      |
| M         | 1   | 0.32   | 0.20      | none      | none      |
| P         | 0   | 0.24   | 0.20      | 0.16      | 0.14      |
| P         | 1   | none   | none      | none      | none      |
| IMP       | 0   | 0.30   | 0.26      | 0.16      | 0.12      |
| IMP       | 1   | 0.22   | 0.22      | none      | none      |
| IJMPQ     | 0   | 0.34   | 0.26      | 0.18      | 0.12      |
| IJMPQ     | 1   | 0.22   | 0.18      | 0.12      | none      |

This is the asymmetric version of the price-demand interaction from symmetric_c_Cost:
raising Cost retreats the demand ceiling. But the retreat is steeper here because
the demand never falls to zero. At Cost = 0.12, IJMPQ still has a surviving cheap
side at c1 = 0.12 (pop_0 = 0.570), while the expensive side is already below 0.5
everywhere (0.331 at c1 = 0.12, 0.263 at c1 = 0.14, then lower). The cooperator
side fails first in absolute c1, but the exploiter side loses its high-cooperation
tail sooner.

## Cost compresses the role split and softens exploitation

Under partner choice alone, mutualism at negligible Cost gives the sharpest
deterministic split: the cheap population cooperates more and earns less. That
logic survives here, but Cost steadily compresses both faces of the asymmetry.

For P, the mean cooperation gap and mean fitness gap by Cost are:

| Cost | mean qBSeen gap (pop_0 - pop_1) | mean wmean gap (pop_0 - pop_1) |
| ---: | -------------------------------: | ------------------------------: |
| 0.00 | 0.329                            | -0.148                         |
| 0.04 | 0.240                            | -0.108                         |
| 0.08 | 0.180                            | -0.083                         |
| 0.12 | 0.092                            | -0.043                         |
| 0.20 | 0.017                            | -0.006                         |

The paradox-of-success signal remains essentially perfect while it lasts:
corr(dqBSeen, dwmean) = -0.998, and the higher-cooperation side has lower fitness
in all 120 cells. What Cost changes is not who profits at a given functioning P
cell, but how many functioning P cells remain. The asymmetry collapses mainly
because both populations are pushed toward the control floor.

The same compression appears in the combined mechanisms, only from a higher base.
IJMPQ's mean cooperation gap is 0.159 at Cost = 0, grows slightly at intermediate
Cost while pop_1 loses its tail first (0.188 at Cost = 0.08), then shrinks to
0.027 by Cost = 0.20. Its mean fitness gap follows the same pattern but remains
negative throughout (-0.019 at Cost = 0, -0.086 at Cost = 0.08, -0.011 at
Cost = 0.20).

## Control decomposition: Cost erodes M1 supply-side, the dilemma decides the damage

As in symmetric_c_Cost, the control isolates the pure machinery tax. Mechanism M is
enough to show it:

| Cost | control pop_0 qB | control pop_0 M1 | PD pop_0 qB | PD pop_0 M1 |
| ---: | ---------------: | ---------------: | ----------: | ----------: |
| 0.00 | 0.956            | 0.248            | 0.689       | 0.673       |
| 0.04 | 0.968            | 0.170            | 0.336       | 0.308       |
| 0.08 | 0.972            | 0.098            | 0.061       | 0.069       |
| 0.20 | 0.974            | 0.040            | 0.053       | 0.026       |
| 0.28 | 0.974            | 0.028            | 0.054       | 0.018       |

The machinery story is the same as on the diagonal: M1 is selected out as Cost
rises even in the control, where no enforcement is needed. Across all dilemmas,
groupsizes, shuffle settings, and both populations, M1 under M is below the dummy
baseline in 2,001 cell-conditions. That is the supply-side effect.

What changes on the asymmetric branch is the behavioral consequence. In the
control, qBSeen stays pinned near 0.97 while M1 erodes, because producing b is
still individually favored. In the PD the same erosion removes the very machinery
needed to hold c0 = 0.10 and c1 > 0.10 cooperation together, so behavior collapses
almost immediately.

## There is little behavior-mechanism decoupling here

symmetric_c_Cost's striking result was that cooperation could remain high after the
active enforcement alleles had largely vanished. asymmetric_c1_Cost shows the boundary
of that result: once the cheap side still faces nontrivial demand, machinery loss
and behavioral loss move together.

For P on pop_0 at c1 = 0.20:

| Cell | qBSeen | P1 | C1P0 |
| ---- | -----: | -: | ---: |
| Cost=0.00 | 0.603 | 0.797 | 0.071 |
| Cost=0.08 | 0.415 | 0.374 | 0.098 |
| Cost=0.12 | 0.048 | 0.042 | 0.046 |

For M on the same slice:

| Cell | qBSeen | M1 | C1M0 |
| ---- | -----: | -: | ---: |
| Cost=0.00 | 0.867 | 0.554 | 0.408 |
| Cost=0.08 | 0.062 | 0.068 | 0.060 |
| Cost=0.12 | 0.056 | 0.045 | 0.054 |

The machinery still erodes, but the tax-free unconditional-cooperator niche does
not inherit a stable high-cooperation regime. Once P1 or M1 is mostly gone, the
population falls with it. This is the clean contrast with symmetric_c_Cost: the
diagonal has a harmless-shedding region; the asymmetric branch does not.

## Snowdrift buffers the price only on the cheap side

Snowdrift again raises the floor, but asymmetrically. The low-cost population is
almost Cost-proof, while the high-cost population remains stuck in the role split:

| Mechanism | Pop | Cost=0 | Cost=0.08 | Cost=0.20 | Cost=0.28 |
| --------- | --- | -----: | --------: | --------: | --------: |
| M         | 0   | 0.944  | 0.937     | 0.927     | 0.908     |
| M         | 1   | 0.167  | 0.158     | 0.185     | 0.238     |
| P         | 0   | 0.962  | 0.955     | 0.935     | 0.917     |
| P         | 1   | 0.090  | 0.103     | 0.154     | 0.197     |
| IJMPQ     | 0   | 0.928  | 0.913     | 0.928     | 0.873     |
| IJMPQ     | 1   | 0.597  | 0.325     | 0.238     | 0.335     |

So the snowdrift lesson from symmetric_c_Cost still holds only half-way. High S makes
cooperation individually attractive enough that pop_0 keeps cooperating even when
the machinery is taxed. But because c1 remains structurally higher, pop_1 does not
join it; the role split persists, only with a slightly softer floor.

## Shuffle and groupsize still isolate the same components

The robustness mirrors carry over cleanly.

- Shuffle removes the M contribution. At Cost = 0, MP is 0.598 / 0.422 under
  noshuffle but only 0.467 / 0.142 under shuffle, essentially reverting to the
  partner-choice split. By Cost = 0.12 both ecologies converge near the same low
  floor, because there is little M component left for shuffle to remove.
- gs = 4 removes partner choice almost completely from the outset. P at Cost = 0 is
  already 0.054 / 0.025 at gs = 4 versus 0.469 / 0.140 at gs = 128. M is
  groupsize-invariant under Cost (0.689 / 0.641 versus 0.686 / 0.637 at Cost = 0),
  while IJMPQ keeps its gs = 4 penalty from the mutualism baseline
  (0.708 / 0.549 versus 0.708 / 0.600 at Cost = 0, then 0.413 / 0.225 versus
  0.124 / 0.065 at Cost = 0.08).

## Temporal dynamics: the verdict is set by the first snapshot

The single-run movies show the same absorbing-state pattern as the other studies.
Established cells are already established by the first recorded snapshot, and
collapsed cells are already collapsed.

- P at (Cost, c1) = (0.00, 0.20) reaches 0.593 / 0.180 at t = 131072 and ends at
  0.664 / 0.157. The role split is in place immediately and only wobbles slightly.
- P at (0.12, 0.20) is already collapsed at the first snapshot
  (0.043 / 0.024) and stays there through the run.
- M at (0.00, 0.20) sits in the high-cooperation state from the first snapshot
  onward (about 0.82 / 0.80, ending 0.866 / 0.835).
- IJMPQ at (0.20, 0.20) is already near the floor by the first snapshot
  (0.077 / 0.032) and never recovers.

So the image summaries are representative. The interesting event is not a slow
late erosion but whether a cell establishes a defended state at all.

## One-line reading

symmetric_c_Cost showed that information cost can be shed harmlessly when the game
does not still demand enforcement. asymmetric_c1_Cost shows the complementary case:
once one population is locked at c0 = 0.10 and the other is costlier still, the
price of the machinery is paid directly in behavior. Cost compresses the
cooperator/exploiter split, retreats the c1 ceiling, and largely removes the
behavior-mechanism decoupling that made the diagonal Cost axis look soft.
