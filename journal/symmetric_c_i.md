# Diagonal Cost — The Price of the Enforcement Apparatus

Standard diagonal fixes the per-round module tax at Cost = 0.001 (negligible)
and sweeps the cooperation cost c from 0 to b = 0.4. **symmetric_c_i** adds a
second axis: it sweeps Cost jointly with c over a triangular grid, so we can ask
what happens when carrying reciprocity or partner-choice machinery is itself
expensive. Cost is the *information cost* of a mechanism — the metabolic or
cognitive overhead of being a reciprocator or a partner chooser — as opposed to
c, the *cooperation cost* paid when you actually help a partner.

Everything else matches diagonal: the diagonal special case of mutualism
(c0 = c1 = c), K = 0.5, b = 0.4, pops 1/2/3, shuffle and noshuffle, gs = 128 and
gs = 4, dilemmas 0/1/2, Runs = 30. The companion symmetric_c_i_1run is the
single-run variant for temporal dynamics.

For how the information-cost axis sits alongside the payoff-axis attributions
(prisoners/snowdrift) and the cooperation-cost thresholds (diagonal/mutualism),
see **[synthesis.md](synthesis.md)**.

## What Cost does in the model

From the simulation source (recruits.c), each individual pays, per round,
cost = Cost × ((Choose or Choose_lt) + (Mimic or Imimic or Imimic_lt)), and
fitness is w = max(0, payoff − cost). So Cost is charged **once for being a
partner chooser** (carrying any P/Q locus) and **once for being a reciprocator**
(carrying any M/I/J locus). The consequences:

- The control \_ carries no modules and pays nothing — it is the Cost-invariant baseline.
- Single-family mechanisms (M; P) pay one unit of Cost per round.
- Combined mechanisms (MP, MPQ, IMP, IJMPQ) touch both families and pay two units of Cost.
- Only carriers of an **active** locus pay; a cooperator that has shed the
  machinery (C1P0, C1M0 — cooperate unconditionally, no chooser/mimic locus)
  pays nothing.

That last point drives most of the results below.

## The grid

Triangular: Cost runs over {0, 0.02, ..., 0.40} and, for each Cost, c runs
0 ... (0.40 − Cost) in 0.02 steps — that is, Cost + c ≤ b. 231 cells. The
constraint keeps the combined burden within the cooperation benefit b; it also
means the two axes are only ever explored together up to their shared ceiling.

**Sanity check.** The Cost = 0 edge reproduces standard diagonal (Cost = 0.001)
cell for cell: across all seven mechanisms at c = 0.0/0.1/0.2/0.4 (pop_1, PD,
noshuffle, gs = 128) the two studies agree to within ±0.008 (the noise floor).
The new axis is a clean extension, not a reparameterization.

## Headline: information cost is real but soft, and it acts through the machinery

Primary condition throughout: pop_1, PD (dilemma 1), noshuffle, gs = 128,
fset_0. Cell key is (Cost, c).

Along the **pure information-cost axis** (c = 0, so no temptation — the only
thing biting is the module tax), cooperation erodes gently and the mechanism
ordering is preserved:

| Mechanism | families | Cost=0 | Cost=0.08 | Cost=0.20 | Cost=0.40 |
| --------- | :------: | -----: | --------: | --------: | --------: |
| \_        | 0        | 0.498  | 0.495     | 0.488     | 0.517     |
| M         | 1        | 0.942  | 0.836     | 0.686     | 0.627     |
| P         | 1        | 0.963  | 0.878     | 0.701     | 0.539     |
| MP        | 2        | 0.962  | 0.907     | 0.781     | 0.654     |
| MPQ       | 2        | 0.970  | 0.930     | 0.841     | 0.715     |
| IMP       | 2        | 0.963  | 0.925     | 0.843     | 0.719     |
| IJMPQ     | 2        | 0.968  | 0.944     | 0.886     | 0.810     |

Two things stand out.

**Information cost is far gentler than cooperation cost.** A cost of 0.40 on the
Cost axis leaves IJMPQ at 0.810; the same 0.40 on the c axis collapses it to
0.378 (and P to 0.066, M to 0.079). The reason is structural: c injects
temptation and risk into every interaction for everyone, whereas Cost only taxes
the machinery carriers — and at c = 0 there is no temptation, so a population can
shed the expensive apparatus and keep cooperating for free.

**Family count does not predict the collapse.** The naive prediction — a
two-family mechanism pays double, so it should fail first — is wrong. The
combined mechanisms are the most Cost-robust despite paying the double tax. If
the per-round tax alone governed the outcome, a two-family mechanism at Cost = X
should match a one-family mechanism at Cost = 2X; it does not (MP at Cost = 0.08
is 0.907, whereas P at Cost = 0.16 is only 0.589). The tax is not the whole
story — the enforcement architecture is.

## Why the machinery erodes but cooperation survives

The mechanism is visible in the genotype frequencies. Along the pure-Cost axis
(c = 0), the active enforcement allele is selected out, while cooperation is
carried by tax-free unconditional cooperators:

| Mechanism | metric           | Cost=0 | Cost=0.08 | Cost=0.20 | Cost=0.40 |
| --------- | ---------------- | -----: | --------: | --------: | --------: |
| P         | qBSeen           | 0.963  | 0.878     | 0.701     | 0.539     |
| P         | P1 (chooser)     | 0.671  | 0.193     | 0.060     | 0.020     |
| P         | C1P0 (free coop) | 0.316  | 0.704     | 0.653     | 0.527     |
| M         | qBSeen           | 0.942  | 0.836     | 0.686     | 0.627     |
| M         | M1 (TFT)         | 0.438  | 0.105     | 0.040     | 0.018     |
| M         | C1M0 (free coop) | 0.534  | 0.748     | 0.659     | 0.616     |

As Cost rises the chooser allele P1 falls from 0.67 to 0.02 and the TFT allele M1
from 0.44 to 0.02 — the machinery is almost entirely shed. Cooperation does not
track that collapse because the vacated niche is filled by C1P0 / C1M0 genotypes
that cooperate unconditionally and pay no module tax. **Behavior and mechanism
decouple:** the population keeps cooperating while abandoning the apparatus that
produced the cooperation — because at c = 0 there is no temptation for the
apparatus to defend against. (In the PD at c = 0, T = R and P = S, so an
individual's own move is payoff-neutral; fitness is set entirely by the partner,
and cooperators simply do well by association.)

## The control decomposes cost from demand

Dilemma 0 (the control) has no social dilemma at all — produce-b is dominant, so
cooperation is favored no matter what anyone does. It therefore isolates the pure
module tax with **zero demand** for enforcement, which lets us separate two things
the PD alone conflates. The M mechanism, c = 0, noshuffle, gs = 128, pop_1:

| Cost | control qBSeen | control M1 | control C1M0 | PD qBSeen | PD M1 |
| ---: | -------------: | ---------: | -----------: | --------: | ----: |
| 0.00 | 0.968          | 0.383      | 0.603        | 0.942     | 0.438 |
| 0.08 | 0.977          | 0.113      | 0.868        | 0.836     | 0.105 |
| 0.20 | 0.978          | 0.043      | 0.936        | 0.686     | 0.040 |
| 0.40 | 0.978          | 0.023      | 0.956        | 0.627     | 0.018 |

Two readings, one on each side of the ledger:

**The machinery erodes at nearly the same rate with or without a dilemma.** M1
falls 0.38 → 0.02 in the control and 0.44 → 0.02 in the PD — essentially the same
trajectory. Erosion is a **supply-side** effect: the tax removes the M locus at a
rate set by Cost, almost independent of whether reciprocity is actually needed.
The PD sits a hair above the control at low Cost (residual demand keeps a few more
TFT carriers around), but the curves converge and the cost dominates.

**The dilemma decides whether that erosion matters for behavior.** In the control,
qBSeen is pinned at the ~0.978 ceiling across the entire Cost range while M1
collapses — behavior and mechanism decouple *trivially*, because no enforcement is
needed. In the PD the identical machinery loss drags cooperation from 0.94 down to
0.63. This is the **demand-side** half: shedding the apparatus is free when the
game does not punish cooperation and costly when it does.

So Cost sets the erosion rate of the apparatus; the dilemma sets the consequence of
shedding it. The control is the clean null for "machinery erodes but cooperation
survives" — it shows the erosion is not a demand-side artifact, and it exhibits the
unconditional-cooperator niche directly: as M1 vanishes, control C1M0 climbs to
0.956, the tax-free cooperators that inherit the population.

## The interaction: information cost lowers the cooperation-cost ceiling

The two axes are benign in isolation but compound in the interior. Cost thins the
enforcement machinery; c is exactly what that machinery exists to resist. So
raising Cost pulls the c-collapse threshold downward — the apparatus fails at
lower temptation because there is less of it. The IJMPQ landscape (qBSeen; blank
= outside the triangle):

| Cost \ c | 0.00 | 0.04 | 0.08 | 0.16 | 0.24 | 0.32 | 0.40 |
| -------: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.00     | 0.968 | 0.966 | 0.967 | 0.957 | 0.945 | 0.909 | 0.378 |
| 0.04     | 0.962 | 0.956 | 0.952 | 0.926 | 0.888 | 0.780 |       |
| 0.08     | 0.944 | 0.933 | 0.915 | 0.818 | 0.750 | 0.023 |       |
| 0.12     | 0.930 | 0.900 | 0.838 | 0.684 | 0.454 |       |       |
| 0.20     | 0.886 | 0.791 | 0.533 | 0.049 |       |       |       |
| 0.30     | 0.845 | 0.501 | 0.083 |       |       |       |       |
| 0.40     | 0.810 |       |       |       |       |       |       |

Reading down any column (rising Cost at fixed c) the decline is gradual; reading
across any row (rising c at fixed Cost) there is a cliff, and the cliff moves left
as Cost grows. The c-threshold where cooperation crosses 0.5 retreats steadily:

| Cost | IJMPQ | IMP  | MP   | P    | M    |
| ---: | ----: | ---: | ---: | ---: | ---: |
| 0.00 | 0.38  | 0.38 | 0.36 | 0.36 | 0.34 |
| 0.08 | 0.30  | 0.24 | 0.24 | 0.22 | 0.02 |
| 0.12 | 0.22  | 0.18 | 0.18 | 0.16 | 0.02 |
| 0.20 | 0.08  | 0.04 | 0.04 | 0.04 | 0.00 |

For the robust mechanisms the exchange rate is roughly 1.5 units of tolerable c
lost per unit of Cost added. This is not an equal-budget effect: cells with the
same Cost + c differ enormously (at Cost + c = 0.4, IJMPQ ranges from 0.378 at
all-c to 0.810 at all-Cost). Per unit, c is far more destructive than Cost; the
two simply interact where they overlap.

The one-line reading: **c is the demand for enforcement (temptation to defect);
Cost is the price of enforcement (the module tax). Cooperation persists where the
population can afford the machinery the game demands.** With no demand (c = 0) any
price is survivable — the apparatus is shed harmlessly. With free machinery
(Cost = 0) the standard diagonal c-profile returns. The interior is where a
rising price starves the defense that a rising demand requires.

## Reciprocity vs partner choice split two ways under cost

The two single-family mechanisms swap places depending on which axis is active:

- **Pure information cost (c = 0):** at high Cost, M holds up better than P
  (0.627 vs 0.539 at Cost = 0.40). With no temptation, noshuffle's stable
  pairings keep unconditional cooperators (C1M0) locked into cooperative dyads,
  whereas partner choice needs active, taxed re-sampling to assort — so shedding
  P1 drifts P back toward the control floor faster.
- **With temptation (c > 0):** P defends cooperation to a much higher c than M at
  the same Cost (at Cost = 0.08, P holds qBSeen ≥ 0.5 up to c = 0.22 vs M's
  0.02). A residual chooser minority sorts the whole population — defectors are
  abandoned and paired together — so even cheap C1P0 cooperators are protected. A
  residual TFT minority only protects itself; the C1M0 unconditional cooperators
  it leaves behind are exploited the moment temptation appears.

This is the information-cost face of the synthesis attribution: **P is an
assortment (population-level) mechanism, M is a history (individual-level)
mechanism.** Cost reveals it by stripping each down to its residual and showing
what the residual can still protect.

## Snowdrift buffers the information cost

In the snowdrift-ordered payoffs (dilemma 2, high S), cooperation is nearly
Cost-proof (c = 0, pop_1, noshuffle, gs = 128):

| Mechanism | d1 (PD) Cost=0.40 | d2 (SD) Cost=0.40 |
| --------- | ----------------: | ----------------: |
| M         | 0.627             | 0.870             |
| P         | 0.539             | 0.870             |
| IJMPQ     | 0.810             | 0.892             |

Snowdrift's high floor means cooperation is individually favored even without
enforcement, so shedding the machinery under information cost costs almost no
cooperation. This is the same low-risk / high-floor result from **snowdrift.md**
and **synthesis.md**, now seen on the information-cost axis: **when the game
rewards cooperation on its own, the enforcement apparatus is optional, so taxing
it barely matters.**

## Groupsize: partner choice is penalized twice

At gs = 4 the chooser bottleneck and the information cost stack (c = 0, PD,
noshuffle):

| Mechanism | gs128 Cost=0 | gs128 Cost=0.08 | gs4 Cost=0 | gs4 Cost=0.08 |
| --------- | -----------: | --------------: | ---------: | ------------: |
| M         | 0.942        | 0.836           | 0.940      | 0.835         |
| P         | 0.963        | 0.878           | 0.856      | 0.522         |
| IJMPQ     | 0.968        | 0.944           | 0.960      | 0.926         |

M is groupsize-invariant under Cost (stable pairings do not care about group
size); P is already depressed at gs = 4 (fewer mutual-swap opportunities) and a
small Cost then knocks it to the control floor. This mirrors the gs = 4 findings
in diagonal and synthesis: small groups remove the P component, and information
cost finishes it off.

## Temporal dynamics (symmetric_c_i_1run)

Single-run trajectories (nine snapshots, t = 1 ... 1.05M) show that the image
(steady-state) values are representative:

- Established cells stay put: Cost = 0, c = 0 holds about 0.96–0.97 throughout;
  the pure high-cost corner Cost = 0.40, c = 0 sits near 0.80 (IJMPQ) with mild
  run-to-run wobble for the machinery-depleted single-family mechanisms (P
  bounces 0.50–0.65), consistent with the near-neutral selection there.
- Interior collapse cells (Cost = 0.20, c = 0.16, and similar) are already
  collapsed at the first snapshot and never recover — the collapse is not a slow
  erosion of machinery visible at this resolution but is set during
  establishment.

As with the hitchhiking analysis (see ai/findings.md), the sub-establishment
order (does cooperation rise first, then the machinery shed, or simultaneously?)
falls below the 131072-step snapshot spacing and would need finer early logging
to resolve.

## pop_2: information cost alone barely breaks symmetry

The symmetric_c pop_2 role split (one population ends up the cooperator, the other
the exploiter) is a temptation-driven, paradox-of-success phenomenon. Along the
pure information-cost axis (c = 0) it is weak — the fset_0 minus fset_1
cooperation gap grows only mildly with Cost (P: +0.03 to +0.07; IJMPQ: +0.00 to
+0.03 as Cost goes 0 to 0.40). With no temptation there is no strong role
asymmetry for Cost to amplify; the split needs c, consistent with the "symmetric
payoffs split stochastically only under temptation" reading in **synthesis.md**.

## Caveats

- **Primary slice.** Numbers above are pop_1, PD, noshuffle, gs = 128, fset_0
  unless stated. Other conditions were checked for the qualitative claims
  (shuffle, gs = 4, dilemma 2, pop_2) and are reported where they differ.
- **Noise floor.** Per-cell qBSeen differences below about 0.01–0.02 and
  c-threshold differences of one grid step (0.02) are within run-to-run noise;
  the mechanism ordering and the frontier retreat are well outside it.
- **Triangular grid.** Because Cost + c ≤ 0.4, the extreme corners of a full
  square are not sampled; the iso-budget comparison is therefore made along the
  hypotenuse and shorter interior diagonals, not a full square.
- **Role in the project.** symmetric_c_i is an extension of the primary diagonal
  study, not a separate calibration. It answers "how expensive can the mechanism
  be before it stops paying for itself," which the fixed-Cost studies cannot.
