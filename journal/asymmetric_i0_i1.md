# asymmetric_i0_i1 — Asymmetric Information Cost at Symmetric Cooperation Cost

asymmetric_i0_i1 is Study A of the per-population information-cost programme: both
populations face the same cooperation cost (c0 = c1 = c) while information cost
is asymmetric (Cost0 != Cost1). It asks whether taxing one population's enforcement
machinery more than the other's creates a deterministic cooperator/exploiter split,
and — critically — which population takes which role.

This is the supply-side counterpart to asymmetric_c1_i (demand asymmetry: fixed
c0 < c1 with symmetric Cost) and to symmetric_c_i (symmetric Cost and c). The
Cost0 = Cost1 edge of this triangle nests onto symmetric_c_i pop_2 at the same c;
the diagonal is excluded here because Cost0 < Cost1 strictly.

For the cross-study framework, see [synthesis.md](synthesis.md). For symmetric
Cost x c, see [symmetric_c_i.md](symmetric_c_i.md). For demand-side asymmetry
under Cost, see [asymmetric_c1_i.md](asymmetric_c1_i.md).

## Design

- Study pair: asymmetric_i0_i1 (Runs = 30) and asymmetric_i0_i1_1run (single-run).
- Population structure: pop_2 only.
- Cooperation cost: c0 = c1 = c on a 0.02 grid. **Primary slice c = 0.10**
  (120 triangle cells; `csv_*_filtered_for_image.con`); **secondary c = 0.20**
  (55 cells; `csv_*_c020_for_image.con` — see Secondary slice).
- Information cost: strict triangle Cost0 < Cost1 on a 0.02 grid, each axis capped
  at b - c (Cmax = 0.30 at c = 0.10; 0.20 at c = 0.20). Per-axis cap, not
  Cost0 + Cost1 <= b.
- Primary condition below unless noted: PD (dilemma 1), noshuffle, gs = 128.

The control (_) shows no role split: qBSeen stays near 0.05 across the triangle
(e.g. 0.047 / 0.051 at Cost0 = 0, Cost1 = 0.20). Cost asymmetry alone does not
break symmetry without enforcement machinery.

## Headline: mechanism-dependent role assignment

Asymmetric information cost produces a **deterministic two-population split**, but
**who cooperates and who profits depends on the mechanism family**. The paradox of
success (higher cooperation, lower fitness) holds throughout; what changes is which
population is taxed into which role.

### Partner choice (P) — low-Cost side keeps the apparatus

Under P alone, the **low-Cost population (pop_0) cooperates more** and carries
the chooser allele; the high-Cost side sheds machinery and defects, but **wins
fitness**:

| Metric | Value (triangle mean, c = 0.10) |
| ------ | ------------------------------- |
| mean qBSeen gap (pop_0 - pop_1) | +0.110 |
| mean wmean gap (pop_0 - pop_1) | -0.046 |
| corr(dq, dw) | -0.981 |
| pop_0 cooperates more | 63 / 120 cells |
| pop_1 fitter | 62 / 120 cells |
| fitness-inverted cells | 104 / 120 |

At Cost0 = 0, Cost1 = 0.20: q = 0.331 / 0.153, w = 0.528 / 0.573. Genotypes
confirm the machinery story — pop_0 keeps P1 (0.799 at gap 0.10; 0.681 at gap
0.20) while pop_1 falls toward C1P0.

This mirrors the familiar partner-choice role split seen stochastically in
symmetric_c pop_2 at c = 0.10 (0.811 / 0.327), but Cost asymmetry **locks it in
deterministically** and assigns the cooperator role to the side that can still
afford the chooser locus.

### Combined mechanisms (IMP, IJMPQ) — cross-population hitchhiking

Adding reciprocity **inverts** the cooperation assignment. Under IJMPQ, the
**high-Cost population cooperates more** while the **low-Cost population earns
more**:

| Metric | Value (triangle mean, c = 0.10) |
| ------ | ------------------------------- |
| mean qBSeen gap (pop_0 - pop_1) | -0.201 |
| mean wmean gap (pop_0 - pop_1) | +0.109 |
| corr(Cost gap, dq) | -0.612 |
| corr(dq, dw) | -0.992 |
| pop_1 cooperates more | 85 / 120 cells |
| pop_0 fitter | 102 / 120 cells |
| fitness-inverted cells | 120 / 120 |

At Cost0 = 0, Cost1 = 0.20: q = 0.681 / 0.922, w = 0.801 / 0.642. Pop_1 has
shed active enforcement (P1 = 0.056, M1 ≈ 0.03) and cooperates through tax-free
unconditional carriers (C1P0 = 0.907, C1M0 = 0.936). Pop_0 retains partial
machinery (P1 = 0.526) but cooperates less — it **exploits** pop_1's unconditional
help without paying the information cost.

IMP shows the same sign at (0, 0.20): q = 0.393 / 0.854, dq = -0.461. The flip
from P to MP is immediate: MP at (0, 0.20) gives q = 0.370 / 0.829.

### Reciprocity alone (M) — weak split, mostly collapse

M shows a slight pop_1 cooperation edge (mean dq = -0.041) but **78 / 120** cells
have total q < 0.15. The reciprocity-only apparatus does not sustain a clean
Cost-driven role narrative; pop_0 is fitter in 60 / 120 cells at the control
floor.

## Dose-response: when does the IJMPQ hitchhiking regime turn on?

At Cost0 = 0, increasing Cost1 (c = 0.10):

| Cost1 | q pop_0 / pop_1 | dq (0-1) | dw (0-1) |
| ----- | ---------------- | -------- | -------- |
| 0.02  | 0.962 / 0.963    | -0.001   | +0.025   |
| 0.10  | 0.937 / 0.956    | -0.019   | +0.045   |
| 0.20  | 0.681 / 0.922    | -0.241   | +0.158   |
| 0.30  | 0.506 / 0.907    | -0.401   | +0.236   |

Small Cost gaps barely break symmetry; the cross-population hitchhiking pattern
sharpens from Cost1 ≈ 0.14 onward and is strong by Cost1 = 0.20.

## A third route to the role split

[synthesis.md](synthesis.md) documents two routes to the cooperator/exploiter
outcome: stochastic symmetry breaking under symmetric payoffs (symmetric_c pop_2)
and deterministic splitting via demand asymmetry c0 < c1 (asymmetric_c0_c1).
asymmetric_i0_i1 adds a **third route: supply-side asymmetry via Cost0 != Cost1**
at symmetric c.

The assignment rule is not universal — it depends on whether partner choice or
combined reputation mechanisms carry the cooperation:

| Mechanism | Cooperator (more qBSeen) | Fitter (higher wmean) | Mechanism |
| --------- | ------------------------ | --------------------- | --------- |
| P         | pop_0 (low Cost0)        | pop_1 (high Cost1)    | Affordable chooser on cheap side |
| IJMPQ     | pop_1 (high Cost1)       | pop_0 (low Cost0)     | Tax-free unconditional coop on expensive side |
| IMP       | pop_1                    | pop_0                 | Same hitchhiking logic as IJMPQ |

In both cases the paradox of success holds: the population that cooperates more
earns less. What Cost asymmetry changes is **which side is locked into which role**.

## Robustness

**Shuffle** does not change P (mean dq stays +0.110). For IJMPQ, shuffle
**strengthens** the hitchhiking split (mean dq -0.224 vs -0.201 noshuffle; mean
dw +0.119).

**Groupsize 4** removes the P asymmetry (mean dq ≈ 0.000) — partner choice needs
large groups — while IJMPQ retains a weaker same-sign pattern (mean dq -0.131,
pop_0 fitter in 93 / 120 cells).

**Collapse.** At c = 0.10, cells with q0 + q1 < 0.15: P 54 / 120, M 78 / 120,
IJMPQ 19 / 120. Combined mechanisms remain Cost-robust far longer than single-family
mechanisms.

## Snowdrift: Cost stops locking roles (P), hitchhiking weakens (IJMPQ)

Snowdrift (dilemma 2, c = 0.10, noshuffle, gs = 128) largely **decouples role
assignment from the information-cost axis** for partner choice, while combined
mechanisms retain a Cost-linked direction but at a high cooperation floor.

### Partner choice — stochastic with respect to Cost

Under P in snowdrift, **Cost0 and Cost1 do not predict who cooperates more**:

| Metric | PD | Snowdrift |
| ------ | -- | --------- |
| corr(Cost gap, dq) | -0.225 | **-0.074** |
| pop_0 cooperates more | 63 / 120 | 62 / 120 |
| pop_1 cooperates more | 0 / 120 | **40 / 120** |
| Cost0-rows with both dq signs | 0 / 15 | **12 / 15** |

The split **flips direction** across the triangle: at (Cost0, Cost1) = (0, 0.20)
q = 0.576 / 0.579 (essentially tied), whereas PD gives 0.331 / 0.153. Along
Cost0 = 0, dq wanders from +0.259 to -0.061 with no monotonic Cost1 trend.

Both populations sit at a **moderate, similar cooperation level** (mean q ≈ 0.57,
range 0.568–0.583 across the triangle) — the chooser-driven Cost lock of PD is
gone. This contrasts sharply with **symmetric_c pop_2** at the same c under
snowdrift, where P is strongly asymmetric (0.972 / 0.185): symmetric
information cost there produces a large chooser split, but **asymmetric Cost in
snowdrift washes it out** into ecology-driven, Cost-independent wobble.

The control (_) shows the same pattern without any machinery: dq is uncorrelated
with Cost (corr(gap, dq) = -0.062), with pop_0 cooperating more in 58 / 120 and
pop_1 in 44 / 120 — baseline snowdrift ecology already produces variable
population asymmetry that Cost does not steer.

Fitness under P in snowdrift is also **less paradoxical**: pop_0 is fitter in
56 / 120 cells (versus 2 / 120 in PD), and corr(dq, dw) = -0.695 (weaker than
PD's -0.981).

### IJMPQ — direction persists, magnitude collapses at moderate Cost

IJMPQ in snowdrift is **not** Cost-stochastic in direction: pop_1 cooperates
more in 103 / 120 cells, as in PD. But the **effect size** at moderate Cost is
tiny because both sides cooperate highly:

| Cell (Cost0, Cost1) | PD q₀ / q₁ | SD q₀ / q₁ |
| ------------------- | ---------- | ---------- |
| (0, 0.02)           | 0.962 / 0.963 | 0.961 / 0.961 |
| (0, 0.20)           | 0.681 / 0.922 | **0.928 / 0.963** |
| (0, 0.30)           | 0.506 / 0.907 | 0.905 / 0.963 |

At (0, 0.20) the PD hitchhiking gap (dq = -0.241) shrinks to **dq = -0.035** in
snowdrift; mean |dw| = 0.028 across the triangle. The paradox of success still
holds (120 / 120 fitness-inverted cells), but the **cooperator/exploiter
distinction is nominal** — both populations sit near the cooperation ceiling.

At high total Cost the reciprocity mechanisms (M, IMP, IJMPQ) still show large
Cost-linked dq in snowdrift (mean dq -0.219 to -0.297), driven by collapse
asymmetry at the expensive edge rather than the PD-style hitchhiking regime.

### One-line snowdrift read

Snowdrift restores a **symmetric_c-like** picture for P and IJMPQ at moderate
Cost: roles are either **Cost-independent** (P; direction flips across the
triangle) or **too small to matter** (IJMPQ; both sides ≈ 0.93+). The
supply-side Cost route to deterministic roles is a **PD phenomenon**.

## Secondary slice: c = 0.20

The c = 0.20 triangle (55 cells, Cmax = b − c = 0.20) shows the same qualitative
signs with weaker magnitude — higher cooperation cost compresses the
Cost-asymmetry signal when demand and supply both load the apparatus:

| Mechanism | mean dq (pop₀ − pop₁) | pop₁ cooperates more | corr(dq,dw) |
| --------- | --------------------- | -------------------- | ----------- |
| P         | +0.053                | 0 / 55               | -0.964      |
| MP        | -0.031                | 16 / 55              | -0.973      |
| IMP       | -0.050                | 22 / 55              | -0.988      |
| IJMPQ     | -0.070                | 25 / 55              | -0.993      |
| M         | -0.011                | 11 / 55              | -0.963      |

All five mechanisms show fitness inversion in at least 41 / 55 cells (IJMPQ:
55 / 55). The P low-Cost cooperator assignment and hitchhiking inversion (MP
through IJMPQ) survive at c = 0.20; IMP is intermediate between MP and IJMPQ
as at c = 0.10.

**P collapses at the maximum Cost gap.** At c = 0.20 the Cost cap is
Cmax = 0.20, so (Cost0, Cost1) = (0, 0.20) is already the boundary cell. P
collapses there: q = 0.031 / 0.027 (both populations near zero). By contrast
IJMPQ retains q = 0.463 / 0.696, dq = -0.234 at the same cell — the combined
mechanism is cost-robust at c = 0.20 in a way that partner choice alone is not.
For reference, at (0, 0.10) P gives q = 0.414 / 0.250, dq = +0.164, showing
that the P role split is intact at smaller Cost gaps even at c = 0.20.

Exports: `csv_{fset}_c020_for_image.con` (graphgen `--export-slices`).

### c = 0.20 snowdrift

Under snowdrift at c = 0.20 (55 cells, d = 2), P remains Cost-independent
(mean dq = -0.003), consistent with the c = 0.10 snowdrift picture. IJMPQ
shows a stronger negative gap than at c = 0.10 (mean dq = -0.282 vs -0.245),
likely driven by greater pop₀ collapse at the expensive edge when cooperation
cost is higher. M shows mean dq = -0.170. The PD-only character of
deterministic role assignment therefore persists at c = 0.20.

## Temporal dynamics: roles fixed by the first snapshot

Single-run movies (`asymmetric_i0_i1_1run`, `csv_*_filtered_for_movie.con`,
PD c = 0.10) match the image summaries: the population split is in place by
t = 131072 and then wobbles slightly.

**P at (Cost0, Cost1) = (0, 0.20):** pop₀ 0.243 → 0.338; pop₁ 0.100 → 0.148
— low-Cost side carries chooser-driven cooperation from the first snapshot.

**P at (0, 0.10):** pop₀ 0.599 → 0.524; pop₁ 0.201 → 0.276 — same early lock-in
at a smaller Cost gap.

**IJMPQ at (0, 0.20):** pop₀ ~0.57–0.76; pop₁ ~0.91+ from t = 131072 onward —
hitchhiking regime established immediately; pop₁'s tax-free unconditional
cooperation is present from the first recorded time step.

This mirrors asymmetric_c1_i and symmetric_c_i: the interesting event is whether
a cell establishes a defended state at all, not a slow late erosion.

## Comparison to related studies

- **symmetric_c pop_2** at c = 0.10: P already splits stochastically (0.811 /
  0.327); IMP/IJMPQ are nearly symmetric (0.955 / 0.952; 0.965 / 0.964). Cost
  asymmetry amplifies P's split and **creates** the inverted IJMPQ pattern absent
  under symmetric Cost.
- **symmetric_c_i pop_2** at c = 0.10, Cost0 = Cost1: the diagonal reference this
  study excludes. asymmetric_i0_i asks what happens when Cost is tilted off that
  diagonal at fixed c.
- **asymmetric_c1_i**: demand pins roles (cheap pop cooperates under P); Cost
  compresses that split. asymmetric_i0_i at symmetric c shows supply can **assign
  or invert** roles depending on mechanism, without any c-gap.

## Caveats

- **Primary slice.** Headline numbers are c = 0.10, PD, noshuffle, gs = 128 unless
  stated. Filtered `.con` exports (`csv_*_filtered_for_image.con`) hold c = 0.10;
  the secondary slice uses `csv_*_c020_for_image.con` for both PD and snowdrift
  (regenerate with graphgen `--export-slices --dilemma-type 1` and `--dilemma-type 2`).
- **Strict triangle.** Cost0 = Cost1 cells are excluded (they belong on the
  symmetric_i / symmetric_c_i diagonal). There is no (0, 0) cell in this study;
  the nearest low-asymmetry cells are (0, 0.02).
- **Noise floor.** Per-cell qBSeen differences below ~0.01–0.02 are within
  run-to-run noise; the role-assignment patterns and triangle means are well
  outside it.
- **Temporal.** Movie exports exist for `asymmetric_i0_i1_1run` at c = 0.10
  (`csv_*_filtered_for_movie.con`); c = 0.20 temporal slices are not yet exported.
- **1run companion.** Image and movie `.con` caches for both studies; temporal
  claims above use the 1run movie exports at c = 0.10.

## One-line reading

At symmetric cooperation cost, asymmetric information cost is a third deterministic
route to the cooperator/exploiter split: partner choice assigns the cooperator role
to the low-Cost side, while combined reputation mechanisms invert it — the high-Cost
side sheds its apparatus into tax-free unconditional cooperation and gets exploited
by the low-Cost side. Same paradox of success, opposite Cost-to-role mapping.
