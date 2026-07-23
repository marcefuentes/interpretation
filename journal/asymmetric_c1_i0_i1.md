# asymmetric_c1_i0_i1 — Crossed Asymmetries (Study B)

asymmetric_c1_i0_i1 is Study B of the per-population information-cost programme:
both asymmetries are present at once. Cooperation cost is fixed at c0 = 0.10,
c1 = 0.20 (the load-bearing gap from asymmetric_c0_c1), while information cost
is swept on the full Cost0 x Cost1 square. The cell key is (Cost0, Cost1),
with pop_0 the cheap-c, cheap-i side when both are low and pop_1 the expensive side.

Study A (asymmetric_i0_i1) held c0 = c1 and varied Cost0 < Cost1. asymmetric_c1_i
held c0 < c1 and varied symmetric Cost with c1. This study crosses them: the
central question is whether information-cost asymmetry can **override** the
cooperation-cost role assignment that asymmetric_c0_c1 pins deterministically.

For the parent studies see [asymmetric_i0_i1.md](asymmetric_i0_i1.md),
[asymmetric_c1_i.md](asymmetric_c1_i.md), and [asymmetric_c0_c1.md](asymmetric_c0_c1.md).
For the cross-study framework see [synthesis.md](synthesis.md).

## Design and sanity

- Study pair: asymmetric_c1_i0_i1 (Runs = 30) and asymmetric_c1_i0_i1_1run
  (single-run temporal movies; both complete).
- Population structure: pop_2 only.
- Fixed cooperation costs: c0 = 0.10, c1 = 0.20.
- Information cost: Cost0 in {0.00, 0.02, ..., 0.30} and Cost1 in
  {0.00, 0.02, ..., 0.20}, giving 176 valid cells (each axis capped at b - c_p).
- Primary condition below unless noted: PD (dilemma 1), noshuffle, gs = 128.

At **(Cost0, Cost1) = (0, 0)** the study reproduces asymmetric_c0_c1 at
(c0, c1) = (0.10, 0.20) within noise across all mechanisms:

| Mechanism | pop_0 here / parent | pop_1 here / parent |
| --------- | ------------------: | ------------------: |
| P         | 0.602 / 0.600       | 0.189 / 0.187       |
| M         | 0.866 / 0.869       | 0.829 / 0.830       |
| MP        | 0.741 / 0.729       | 0.487 / 0.465       |
| IMP       | 0.945 / 0.947       | 0.943 / 0.946       |
| IJMPQ     | 0.957 / 0.957       | 0.957 / 0.957       |

Along the **diagonal Cost0 = Cost1**, the slice nests onto asymmetric_c1_i at
symmetric Cost with c1 = 0.20 -- e.g. IJMPQ at Cost = 0.10 gives 0.370 / 0.176
here versus 0.365 / 0.177 in asymmetric_c1_i.

## Headline: the c-gap wins almost everywhere

The square-wide answer to the override question is **no, not globally**. Under
partner choice alone, pop_0 (cheap c, and usually cheap i) cooperates more in
**170 / 176** cells. The mean cooperation gap (pop_0 - pop_1) is +0.116 and the
paradox of success is essentially perfect: corr(dq, dw) = -0.976, with pop_1
fitter in 172 / 176 cells.

Under IJMPQ the same c-gap logic dominates the aggregate: mean dq = +0.160,
pop_0 cooperates more in **156 / 176** cells. IMP shows the same pattern at
mean dq = +0.118 (154 / 176 cells favour pop_0). M is weaker but still
pop_0-leaning (150 / 176).

So when both asymmetries are present, **cooperation-cost structure is the primary
role assigner**. Information cost modulates how strongly the split is expressed
and can locally invert it -- but only in a thin corner of the square.

### Information-gap sensitivity

The correlation between the information gap (Cost1 - Cost0) and the cooperation
gap (dq) is mechanism-dependent. P's cooperation gap is virtually uncorrelated
with the info gap (r = +0.091), confirming that P routes the c-gap directly into
a cooperation gap regardless of information-cost structure. M, IMP, and IJMPQ
show moderate to strong negative correlation: as Cost1 exceeds Cost0, the
cooperation gap shrinks or reverses.

| Mechanism | corr(i-gap, dq) | corr(i-gap, dw) |
| --------- | --------------: | --------------: |
| M         | -0.582          | +0.556          |
| P         | +0.091          | +0.043          |
| IMP       | -0.485          | +0.568          |
| IJMPQ     | -0.626          | +0.685          |

### Paradox of success and fitness dominance

The paradox (the cooperating population is the less fit one) is near-universal:

| Mechanism | Inverted cells (dq * dw < 0) | pop_1 fitter |
| --------- | ---------------------------: | -----------: |
| M         | 167 / 176                    | 147 / 176    |
| P         | 172 / 176                    | 172 / 176    |
| IMP       | 170 / 176                    | 152 / 176    |
| IJMPQ     | 173 / 176                    | 153 / 176    |

## The hitchhiking wedge (combined mechanisms only)

All **13 IJMPQ flip cells** (pop_1 cooperates more) lie on the **Cost0 = 0--0.02
strip** with Cost1 >= 0.08. IMP shows the same 13-cell wedge with the same
geography (IMP starts flipping at Cost1 >= 0.06).

The dose-response along Cost0 = 0 under IJMPQ:

| Cost1 | pop_0 qB | pop_1 qB | dq (0-1) | dw (0-1) |
| ----: | -------: | -------: | -------: | -------: |
| 0.00  | 0.957    | 0.957    | 0.000    | +0.095   |
| 0.02  | 0.953    | 0.953    | -0.001   | +0.119   |
| 0.04  | 0.950    | 0.953    | -0.003   | +0.125   |
| 0.08  | 0.935    | 0.949    | -0.014   | +0.133   |
| 0.10  | 0.923    | 0.947    | -0.023   | +0.138   |
| 0.14  | 0.878    | 0.938    | -0.059   | +0.158   |
| 0.20  | 0.741    | 0.911    | -0.171   | +0.213   |

At (0, 0) both populations sit at mutualistic equilibrium (0.957 / 0.957) -- no
role split when information is free. The inversion **turns on only once Cost1
rises while Cost0 stays at zero**, and it strengthens monotonically with Cost1
along that edge.  The fitness gap also widens monotonically: pop_0 always earns
more, even when it cooperates less.

The override reasserts rapidly once Cost0 is non-zero. Along the Cost1 = 0.20
row under IJMPQ:

| Cost0 | pop_0 qB | pop_1 qB | dq       |
| ----: | -------: | -------: | -------: |
| 0.00  | 0.741    | 0.911    | -0.171   |
| 0.02  | 0.640    | 0.838    | -0.198   |
| 0.04  | 0.165    | 0.122    | +0.043   |
| 0.10  | 0.074    | 0.044    | +0.031   |
| 0.20  | 0.067    | 0.035    | +0.032   |
| 0.30  | 0.068    | 0.031    | +0.037   |

The flip at Cost0 = 0.02 is the largest in magnitude (dq = -0.198), then both
populations collapse by Cost0 = 0.04 and the c-gap takes over.

Genotypes at the wedge apex (0, 0.20) confirm the Study A hitchhiking story:

| Pop | qBSeen | P1    | C1P0  | M1    | C1M0  |
| --- | -----: | ----: | ----: | ----: | ----: |
| 0   | 0.741  | 0.571 | 0.213 | 0.336 | 0.311 |
| 1   | 0.911  | 0.047 | 0.897 | 0.031 | 0.913 |

Pop_1 sheds both P1 and M1 active enforcement into tax-free unconditional
carriers (C1P0, C1M0) and cooperates through them; pop_0 retains partial
machinery but cooperates less and earns more (w = 0.791 / 0.577).

### Contrast with Study A at the same information-cost point

At (Cost0, Cost1) = (0, 0.20) but **symmetric c = 0.10** (Study A):

| Mechanism | Study A q (0 / 1) | Study B q (0 / 1) | Study A dq | Study B dq |
| --------- | ----------------: | ----------------: | ---------: | ---------: |
| P         | 0.331 / 0.153     | 0.069 / 0.032     | +0.178     | +0.037     |
| IJMPQ     | 0.681 / 0.922     | 0.741 / 0.911     | -0.241     | -0.171     |
| IMP       | 0.393 / 0.854     | 0.436 / 0.536     | -0.461     | -0.100     |

The hitchhiking inversion **survives** the c-gap in this corner -- IJMPQ and IMP
still assign more cooperation to pop_1 -- but it is **attenuated** (IMP especially)
and **confined** to the Cost0 ~ 0 strip. P never flips: even at (0, 0.20) the
cheap-c side cooperates more, though both populations are near collapse.

At (Cost0, Cost1) = (0.10, 0.20), Study A shows IJMPQ dq = -0.302 (strong
inversion), while Study B shows dq = +0.031 (c-gap wins) -- the c-gap advantage
is enough to override the hitching inversion once both info costs are non-zero.

## The Cost1 = 0 column: cheap-i cannot override cheap-c

The opposite corner tells the complementary story. Holding Cost1 = 0 while raising
Cost0 taxes only the cheap-c population's information access:

| Cost0 | IJMPQ pop_0 | IJMPQ pop_1 |
| ----: | ----------: | ----------: |
| 0.00  | 0.957       | 0.957       |
| 0.04  | 0.759       | 0.389       |
| 0.08  | 0.755       | 0.314       |
| 0.10  | 0.750       | 0.298       |
| 0.14  | 0.741       | 0.276       |
| 0.20  | 0.734       | 0.268       |
| 0.30  | 0.715       | 0.258       |

Pop_0 keeps cooperating even as its own information cost rises to the axis cap;
pop_1 is pushed into the exploiter role. The c-gap assigns pop_0 as cooperator;
taxing pop_0's machinery erodes but does not invert that assignment.

At (Cost0, Cost1) = (0.30, 0.00): P gives 0.051 / 0.030; IJMPQ gives
0.715 / 0.258 (dq = +0.457).

## Partner choice: c-gap split, Cost erodes both sides

P at (0, 0) restores the familiar asymmetric_c0_c1 picture: 0.602 / 0.189,
w = 0.515 / 0.703. Along Cost0 = 0, rising Cost1 erodes pop_0 monotonically
(0.602 -> 0.510 -> 0.374 -> 0.069 by Cost1 = 0.20) while pop_1 stays near the
floor -- but pop_0 **never** loses the cooperation lead.

On the diagonal (symmetric information cost), P at (0.10, 0.10) still shows
pop_0 ahead (0.375 / 0.193). By (0.20, 0.20) both sides collapse (0.049 / 0.026).

### Collapse census

Collapse is widespread for P and M once any information cost is applied:

| Mechanism   | Cells with q0 + q1 < 0.15 |
| ----------- | ------------------------: |
| _ (control) | 176 / 176                 |
| M           | 131 / 176                 |
| P           | 102 / 176                 |
| MP          | 85 / 176                  |
| IMP         | 74 / 176                  |
| IJMPQ       | 45 / 176                  |

IJMPQ retains substantial cooperation across much of the square -- especially
along Cost1 = 0 and at (0, 0) -- but even it succumbs on the high-i diagonal
(0.068 / 0.031 at (0.30, 0.20)).

## Machinery erosion and genotype route

As information cost rises along the Cost1 = 0 column (isolating the tax on pop_0),
both P1 and M1 alleles are selected out while unconditional cooperators replace them:

P mechanism (pop_0, Cost1 = 0):

| Cost0 | qBSeen | P1    | C1P1  | C1P0  | C0    |
| ----: | -----: | ----: | ----: | ----: | ----: |
| 0.00  | 0.602  | 0.788 | 0.532 | 0.070 | 0.398 |
| 0.04  | 0.611  | 0.584 | 0.485 | 0.126 | 0.389 |
| 0.10  | 0.620  | 0.384 | 0.347 | 0.272 | 0.380 |
| 0.20  | 0.585  | 0.202 | 0.187 | 0.398 | 0.415 |
| 0.30  | 0.051  | 0.021 | 0.004 | 0.048 | 0.949 |

Pop_0 sustains cooperation (0.585 at Cost0 = 0.20) even as P1 drops from 0.788
to 0.202 -- C1P0 unconditional cooperators fill the vacated niche. Collapse only
arrives at Cost0 = 0.30 when the tax also exceeds the net benefit.

M mechanism (pop_0, Cost1 = 0):

| Cost0 | qBSeen | M1    | C1M1  | C1M0  | C0    |
| ----: | -----: | ----: | ----: | ----: | ----: |
| 0.00  | 0.866  | 0.555 | 0.503 | 0.409 | 0.088 |
| 0.04  | 0.705  | 0.477 | 0.422 | 0.443 | 0.134 |
| 0.08  | 0.171  | 0.081 | 0.024 | 0.165 | 0.811 |
| 0.20  | 0.153  | 0.027 | 0.005 | 0.151 | 0.844 |
| 0.30  | 0.146  | 0.017 | 0.003 | 0.145 | 0.852 |

M collapses sharply between Cost0 = 0.04 and 0.08 -- unlike P, reciprocity has
no assortment mechanism to protect free cooperators, so shedding M1 drags
behaviour down immediately.

## Iso-budget analysis: information costs are non-fungible

Along constant total-information-cost lines (Cost0 + Cost1 = budget), cooperation
spans are large, meaning the same total tax yields very different outcomes depending
on which population pays it.

IJMPQ at budget = 0.20:

| Endpoint                    | pop_0 qB | pop_1 qB |
| --------------------------- | -------: | -------: |
| (0.00, 0.20) -- all on pop1 | 0.741    | 0.911    |
| (0.20, 0.00) -- all on pop0 | 0.734    | 0.268    |

Pop_0 spans 0.484 and pop_1 spans 0.778 across the iso-budget line. The
non-fungibility arises because the c-gap (c0 < c1) determines which side's
machinery matters more: taxing pop_1's machinery triggers hitchhiking;
taxing pop_0's machinery shrinks its cooperation advantage.

## Mechanism ranking across the square

IJMPQ ranks first at nearly every cost corner, but at (0.10, 0.10) the ranking
reverses and P tops the list (marginal lead):

| (Cost0, Cost1) | Rank 1       | Rank 2       | Rank 3       |
| --------------- | ------------ | ------------ | ------------ |
| (0.00, 0.00)   | IJMPQ (0.957) | IMP (0.944) | M (0.847)    |
| (0.00, 0.20)   | IJMPQ (0.826) | IMP (0.486) | MPQ (0.239)  |
| (0.30, 0.00)   | IJMPQ (0.487) | MPQ (0.362) | IMP (0.309)  |
| (0.10, 0.10)   | P (0.284)     | MP (0.275)  | IMP (0.275)  |
| (0.30, 0.20)   | All collapsed (~0.04--0.05) |             |              |

The P reversal at (0.10, 0.10) is a moderate-cost regime where the R-P-tracking
single-family mechanism outperforms double-family mechanisms that pay 2x Cost.

## Control dilemma (d = 0): supply-side versus demand-side erosion

Under dilemma 0 (no social dilemma), M1 is eroded by the information-cost tax
but cooperation is unharmed because there is no temptation to exploit:

| Cell         | d0 pop_0 q | d0 M1  | d0 C1M0 | d1 pop_0 q | d1 M1  |
| ------------ | ---------: | -----: | ------: | ---------: | -----: |
| (0.00, 0.00) | 0.958      | 0.347  | 0.636   | 0.866      | 0.555  |
| (0.10, 0.00) | 0.970      | 0.067  | 0.910   | 0.158      | 0.059  |
| (0.20, 0.00) | 0.972      | 0.035  | 0.941   | 0.153      | 0.027  |
| (0.30, 0.00) | 0.971      | 0.024  | 0.950   | 0.146      | 0.017  |
| (0.00, 0.20) | 0.964      | 0.467  | 0.516   | 0.090      | 0.404  |

Under d0, M1 drops from 0.347 to 0.024 as Cost0 rises, while cooperation stays
above 0.97 throughout -- the population simply replaces M1 carriers with C1M0
unconditional cooperators. Under d1 (PD), shedding M1 causes collapse to 0.15
because unconditional cooperators are exploited.

The control mechanism _ confirms that information cost has no effect on the
control itself (q ~ 0.050/0.025 everywhere in d1, q ~ 0.975/0.966 in d0).

## Snowdrift: c-gap dominates completely

In snowdrift (d = 2) the cooperation-cost asymmetry overwhelms any information-cost
wedge. Pop_0 cooperates more in all or nearly all cells for every mechanism:

| Mechanism | mean dq (PD) | mean dq (SD) | pop_0 coops (PD) |
| --------- | -----------: | -----------: | ---------------: |
| P         | +0.116       | +0.885       | 170 / 176        |
| IJMPQ     | +0.160       | +0.626       | 156 / 176        |
| IMP       | +0.118       | +0.734       | 154 / 176        |
| M         | +0.035       | +0.810       | 150 / 176        |

The hitchhiking wedge is a **PD phenomenon**, as in Study A. Cost0-row sign flip
analysis confirms: 0 / 16 rows show mixed dq signs under snowdrift for both P and
IJMPQ. The PD-specific inversion at (0, 0.20) reverses entirely in snowdrift:
IJMPQ gives dq = +0.683 (SD) vs dq = -0.171 (PD).

## Shuffle, groupsize, and shuffle-only mechanisms

- **Shuffle** has no effect on P (mean dq unchanged at +0.116). IJMPQ's split
  is slightly amplified under shuffle (+0.175 vs +0.160). M's split narrows
  slightly (+0.023 vs +0.035), consistent with shuffle disabling reciprocity.
- **gs = 4** largely washes out the role split: P mean dq falls from +0.116 to
  +0.023; IJMPQ from +0.160 to +0.075. Partner choice needs stable pairing to
  sustain the crossed-asymmetry narrative.
- **gs = 4 shuffle** mirrors noshuffle gs = 4 closely (P: +0.023;
  IJMPQ: +0.083).
- **Shuffle-only mechanisms** (IM, IJM) at gs = 128 show c-gap dominance:
  IM mean dq = +0.038, pop_0 cooperates more in 153 / 176 cells.
  IJM mean dq = +0.055, pop_0 cooperates more in 150 / 176 cells.

### Shuffle waste

Under shuffle, M1 is behaviourally inactive (no partner memory) but carriers
still pay the information-cost tax. At (0, 0): M noshuffle gives 0.866; M shuffle
gives 0.048 -- indistinguishable from the control _ (0.050). Shuffle confirms
that M's PD cooperation is entirely reciprocity-dependent.

## Temporal dynamics: roles fixed by the first snapshot

Single-run movies (asymmetric_c1_i0_i1_1run, csv_*_filtered_for_movie.con,
PD, noshuffle, gs = 128) match the image summaries: the population split is in
place by t = 131072 and then wobbles slightly.

**P at (Cost0, Cost1) = (0, 0):** pop_0 0.613 -> 0.568; pop_1 0.164 -> 0.181 --
the asymmetric_c0_c1 role split is present from the first snapshot.

**P at (0, 0.20):** pop_0 0.066 -> 0.091; pop_1 0.022 -> 0.029 -- both sides near
collapse, but pop_0 keeps the cooperation lead throughout.

**IJMPQ at (0, 0):** pop_0 0.949 -> 0.953; pop_1 0.948 -> 0.953 from t = 131072
onward -- mutualistic equilibrium with no role split when information is free on
both sides.

**IJMPQ at (0, 0.20):** pop_0 0.698 -> 0.813; pop_1 0.909 -> 0.937 from t = 131072
onward -- hitchhiking inversion established immediately; pop_1's tax-free unconditional
cooperation is present from the first recorded time step.

**IJMPQ at (0.30, 0):** pop_0 0.804 -> 0.730; pop_1 0.305 -> 0.272 at t = 131072 --
the c-gap cooperator assignment is already in place; taxing pop_0's information access
erodes but does not invert the split.

**IJMPQ at (0.30, 0.20):** pop_0 0.087 -> 0.074; pop_1 0.032 -> 0.032 at t = 131072 --
already collapsed and stable.

**M at (0, 0):** pop_0 0.830 -> 0.871; pop_1 0.756 -> 0.843 from t = 131072 onward --
reciprocity establishes cooperation in both populations with a mild c-gap split.

**M at (0, 0.20):** pop_0 0.091 -> 0.066; pop_1 0.123 -> 0.085 -- both near collapse
with a mild info-gap inversion (pop_1 slightly higher), consistent with the weak
M inversion signal at this cell.

This mirrors asymmetric_c1_i, asymmetric_i0_i1, and symmetric_c_i: the
interesting event is whether a cell establishes a defended state at all, not a
slow late erosion.

## Caveats

- **Primary slice.** Headline numbers are PD, noshuffle, gs = 128 unless stated.
- **Noise floor.** Per-cell qBSeen differences below ~0.01--0.02 are within
  run-to-run noise; the square-wide role-assignment patterns are well outside it.
- **Temporal.** Movie exports exist for asymmetric_c1_i0_i1_1run
  (csv_*_filtered_for_movie.con); temporal claims above use those 1run exports.
  Snapshot spacing is coarse (first recorded time t = 131072), so sub-establishment
  ordering is not resolved.

## Cross-study synthesis

Study B closes the per-population information-cost triangle:

| Study                       | c asymmetry      | i asymmetry                    | Primary role assigner                         |
| --------------------------- | ---------------- | ------------------------------ | --------------------------------------------- |
| asymmetric_c0_c1            | c0 < c1          | none (Cost symmetric)          | c-gap -> pop_0 coops                          |
| asymmetric_c1_i             | c0 < c1 fixed    | Cost symmetric, c1 varies      | c-gap; Cost compresses                        |
| asymmetric_i0_i1            | c0 = c1          | Cost0 < Cost1                  | i-gap; mechanism-dependent                    |
| **asymmetric_c1_i0_i1**     | **c0 < c1 fixed** | **full Cost0 x Cost1**         | **c-gap globally; i-gap in IJMPQ/IMP wedge**  |

The one-line reading: **cooperation-cost asymmetry is the default role assigner
when both axes are asymmetric; information-cost asymmetry can locally invert
IJMPQ/IMP in a Cost0 ~ 0 wedge, but cannot globally overturn the cheap-c
population's cooperator role under P, and cannot do so at all once Cost0 is
non-negligible or the game is snowdrift.**
