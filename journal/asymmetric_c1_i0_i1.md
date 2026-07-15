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
  (single-run temporal movies; **IJMPQ not yet run** at time of writing).
- Population structure: pop_2 only.
- Fixed cooperation costs: c0 = 0.10, c1 = 0.20.
- Information cost: Cost0 in {0.00, 0.02, ..., 0.30} and Cost1 in
  {0.00, 0.02, ..., 0.20}, giving 176 valid cells (each axis capped at b − c_p).
- Primary condition below unless noted: PD (dilemma 1), noshuffle, gs = 128.

At **(Cost0, Cost1) = (0, 0)** the study reproduces asymmetric_c0_c1 at
(c0, c1) = (0.10, 0.20) within noise: P gives 0.602 / 0.189 here versus
0.600 / 0.187 in the parent study.

Along the **diagonal Cost0 = Cost1**, the slice nests onto asymmetric_c1_i at
symmetric Cost with c1 = 0.20 — e.g. IJMPQ at Cost = 0.10 gives 0.370 / 0.176
here versus 0.365 / 0.177 in asymmetric_c1_i.

## Headline: the c-gap wins almost everywhere

The square-wide answer to the override question is **no, not globally**. Under
partner choice alone, pop_0 (cheap c, and usually cheap i) cooperates more in
**170 / 176** cells. The mean cooperation gap (pop_0 − pop_1) is +0.116 and the
paradox of success is essentially perfect: corr(dq, dw) = −0.976, with pop_1
fitter in 172 / 176 cells.

Under IJMPQ the same c-gap logic dominates the aggregate: mean dq = +0.160,
pop_0 cooperates more in **156 / 176** cells. IMP shows the same pattern at
mean dq = +0.118 (154 / 176 cells favour pop_0). M is weaker but still
pop_0-leaning (150 / 176).

So when both asymmetries are present, **cooperation-cost structure is the primary
role assigner**. Information cost modulates how strongly the split is expressed
and can locally invert it — but only in a thin corner of the square.

## The hitchhiking wedge (combined mechanisms only)

All **13 IJMPQ flip cells** (pop_1 cooperates more) lie on the **Cost0 = 0–0.02
strip** with Cost1 ≥ 0.08. IMP shows the same 13-cell wedge with the same
geography.

The dose-response along Cost0 = 0 under IJMPQ:

| Cost1 | pop_0 qB | pop_1 qB | dq (0−1) |
| ----: | -------: | -------: | -------: |
| 0.00  | 0.957    | 0.957    | 0.000    |
| 0.08  | 0.935    | 0.949    | −0.014   |
| 0.10  | 0.923    | 0.947    | −0.023   |
| 0.14  | 0.878    | 0.938    | −0.059   |
| 0.20  | 0.741    | 0.911    | −0.171   |

At (0, 0) both populations sit at mutualistic equilibrium (0.957 / 0.957) — no
role split when information is free. The inversion **turns on only once Cost1
rises while Cost0 stays at zero**, and it strengthens monotonically with Cost1
along that edge.

Genotypes at the wedge apex (0, 0.20) confirm the Study A hitchhiking story:

| Pop | qBSeen | P1   | C1P0 |
| --- | -----: | ---: | ---: |
| 0   | 0.741  | 0.571 | 0.213 |
| 1   | 0.911  | 0.047 | 0.897 |

Pop_1 sheds active enforcement and cooperates through tax-free unconditional
carriers; pop_0 retains partial machinery but cooperates less and earns more
(w = 0.791 / 0.577).

Once Cost0 ≥ 0.04 the c-gap reasserts control. Along the Cost1 = 0.20 row,
dq is already +0.031 at Cost0 = 0.10 and stays positive through Cost0 = 0.30.

### Contrast with Study A at the same information-cost point

At (Cost0, Cost1) = (0, 0.20) but **symmetric c = 0.10** (Study A):

| Mechanism | Study A q (0 / 1) | Study B q (0 / 1) | Study A dq | Study B dq |
| --------- | ----------------: | ----------------: | ---------: | ---------: |
| P         | 0.331 / 0.153     | 0.069 / 0.032     | +0.178     | +0.037     |
| IJMPQ     | 0.681 / 0.922     | 0.741 / 0.911     | −0.241     | −0.171     |
| IMP       | 0.393 / 0.854     | 0.436 / 0.536     | −0.461     | −0.100     |

The hitchhiking inversion **survives** the c-gap in this corner — IJMPQ and IMP
still assign more cooperation to pop_1 — but it is **attenuated** (IMP especially)
and **confined** to the Cost0 ≈ 0 strip. P never flips: even at (0, 0.20) the
cheap-c side cooperates more, though both populations are near collapse.

## The Cost1 = 0 column: cheap-i cannot override cheap-c

The opposite corner tells the complementary story. Holding Cost1 = 0 while raising
Cost0 taxes only the cheap-c population's information access:

| Cost0 | IJMPQ pop_0 | IJMPQ pop_1 |
| ----: | ----------: | ----------: |
| 0.00  | 0.957       | 0.957       |
| 0.10  | 0.750       | 0.298       |
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
(0.602 → 0.069 by Cost1 = 0.20) while pop_1 stays near the floor — but pop_0
**never** loses the cooperation lead.

On the diagonal (symmetric information cost), P at (0.10, 0.10) still shows
pop_0 ahead (0.375 / 0.193). By (0.20, 0.20) both sides collapse (0.049 / 0.026).

Collapse is widespread for P and M once any information cost is applied:

| Mechanism | Cells with q0 + q1 < 0.15 |
| --------- | ------------------------: |
| _ (control) | 176 / 176               |
| M           | 131 / 176               |
| P           | 102 / 176               |
| IJMPQ       | 45 / 176                |

IJMPQ retains substantial cooperation across much of the square — especially
along Cost1 = 0 and at (0, 0) — but even it succumbs on the high-i diagonal
(0.068 / 0.031 at (0.30, 0.20)).

## Snowdrift: c-gap dominates completely

In snowdrift (d = 2) the cooperation-cost asymmetry overwhelms any information-cost
wedge. Pop_0 cooperates more in all or nearly all cells for every mechanism:

| Mechanism | mean dq (PD) | mean dq (SD) | pop_0 coops (PD) |
| --------- | -----------: | -----------: | ---------------: |
| P         | +0.116       | +0.885       | 170 / 176        |
| IJMPQ     | +0.160       | +0.626       | 156 / 176        |
| IMP       | +0.118       | +0.734       | 154 / 176        |
| M         | +0.035       | +0.810       | 150 / 176        |

The hitchhiking wedge is a **PD phenomenon**, as in Study A.

## Shuffle and groupsize

- **Shuffle** has no effect on P (mean dq unchanged at +0.116). IJMPQ's split
  is slightly amplified under shuffle (+0.175 vs +0.160).
- **gs = 4** largely washes out the role split: P mean dq falls from +0.116 to
  +0.023; IJMPQ from +0.160 to +0.075. Partner choice needs stable pairing to
  sustain the crossed-asymmetry narrative.

## Temporal dynamics

Single-run movies for IJMPQ are **not yet available** (1run jobs pending). P 1run
data exist but are not integrated here. Image summaries are expected to be
representative given the early lock-in pattern seen in the parent studies.

## Cross-study synthesis

Study B closes the per-population information-cost triangle:

| Study | c asymmetry | i asymmetry | Primary role assigner |
| ----- | ----------- | ----------- | --------------------- |
| asymmetric_c0_c1 | c0 < c1 | none (Cost symmetric) | c-gap → pop_0 coops |
| asymmetric_c1_i | c0 < c1 fixed | Cost symmetric, c1 varies | c-gap; Cost compresses |
| asymmetric_i0_i1 | c0 = c1 | Cost0 < Cost1 | i-gap; mechanism-dependent |
| **asymmetric_c1_i0_i1** | **c0 < c1 fixed** | **full Cost0 x Cost1** | **c-gap globally; i-gap in IJMPQ/IMP wedge** |

The one-line reading: **cooperation-cost asymmetry is the default role assigner
when both axes are asymmetric; information-cost asymmetry can locally invert
IJMPQ/IMP in a Cost0 ≈ 0 wedge, but cannot globally overturn the cheap-c
population's cooperator role under P, and cannot do so at all once Cost0 is
non-negligible or the game is snowdrift.**
