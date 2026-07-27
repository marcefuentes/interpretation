# asymmetric_c1_i0_i1 — Crossed Asymmetries

asymmetric_c1_i0_i1 is the crossed-asymmetry study of the per-population
information-cost programme:
both asymmetries are present at once. Cooperation cost is fixed at c0 = 0.10,
c1 = 0.20 (the load-bearing gap from asymmetric_c0_c1), while information cost
is swept on the full Cost0 x Cost1 square. The cell key is (Cost0, Cost1),
with pop_0 the cheap-c, cheap-i side when both are low and pop_1 the expensive side.

asymmetric_i0_i1 held c0 = c1 and varied Cost0 < Cost1. asymmetric_c1_i
held c0 < c1 and varied symmetric Cost with c1. This study crosses them: the
central question is whether information-cost asymmetry can **override** the
cooperation-cost role assignment that asymmetric_c0_c1 pins deterministically.

Because the contrast that runs through this entry is against asymmetric_i0_i1,
which is the identical information-cost geometry with the cooperation-cost gap
removed, the two are labelled **equal-c** (asymmetric_i0_i1, c0 = c1 = 0.10) and
**unequal-c** (this study, c0 = 0.10, c1 = 0.20) wherever a table needs short
names. "c-gap" is reserved throughout for the cooperation-cost gap itself.

The full square is what makes this study uniquely informative, and for a reason
beyond the override question. asymmetric_i0_i1 swept only the strict triangle
Cost0 < Cost1
and asymmetric_c1_i held Cost0 = Cost1, so neither could separate the effect of the
information cost a population **pays itself** from the effect of the cost its
**partner** pays. The square contains both matched strips -- (Cost0, 0) and
(0, Cost1) -- so that separation is available here for the first time, and it turns
out to carry more of the story than the override question does.

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

That settles the question the study was designed around, and it is the less
interesting half of the result. What the square adds beyond the override verdict
is that information cost acts across populations rather than within them: which
population pays a given tax matters more than how much is paid, sharing a tax
budget is worse than concentrating it, and the inversion is gated by the presence
of a reciprocity locus. Those three findings occupy the sections below.

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

## Whose information cost matters? One axis binds, and which one flips by family

The square's two axis strips are a matched pair: at (Cost0, 0) only pop_0 pays the
machinery tax, at (0, Cost1) only pop_1 pays it. Comparing them at equal tax
isolates who is hurt by whose information cost. The finding is that in each
mechanism **one of the two costs governs both populations** -- but which one is
decided by mechanism family, and the two families pick opposite axes.

Taxing pop_0 only (Cost1 = 0) versus taxing pop_1 only (Cost0 = 0), both
populations shown:

| Mech  | Cost | tax on pop_0: q0 / q1 | tax on pop_1: q0 / q1 |
| ----- | ---: | --------------------: | --------------------: |
| P     | 0.00 | 0.602 / 0.189         | 0.602 / 0.189         |
| P     | 0.10 | 0.620 / 0.265         | 0.313 / 0.102         |
| P     | 0.20 | 0.585 / 0.268         | 0.069 / 0.032         |
| IJMPQ | 0.00 | 0.957 / 0.957         | 0.957 / 0.957         |
| IJMPQ | 0.10 | 0.750 / 0.298         | 0.923 / 0.947         |
| IJMPQ | 0.20 | 0.734 / 0.268         | 0.741 / 0.911         |
| IMP   | 0.10 | 0.665 / 0.261         | 0.797 / 0.908         |
| IMP   | 0.20 | 0.616 / 0.227         | 0.436 / 0.536         |

Under **P, Cost1 is the binding axis for both populations.** Taxing pop_0 to
Cost0 = 0.20 leaves pop_0 essentially untouched (0.602 -> 0.585, flat within noise
along the whole strip) and actually *raises* pop_1 (0.189 -> 0.268). Taxing pop_1
by the same amount collapses both (0.069 / 0.032). The correlations agree: against
Cost1 they are -0.696 (pop_0) and -0.708 (pop_1); against Cost0, -0.466 and -0.314.
So pop_0 is harmed more by its partner's information cost than by its own, and
pop_1 is harmed more by its own -- both statements meaning the same thing, that
Cost1 is what matters.

Under **IJMPQ and IMP the binding axis is Cost0 instead.** Taxing pop_0 to 0.20
drives pop_1 from 0.957 to 0.268, while taxing pop_1 to 0.20 leaves it at 0.911.
Here it is pop_1 that is harmed more by its partner's cost than its own, at every
tax level. Pop_0 is harmed more by its own cost up to Cost = 0.10 under both
mechanisms, and IMP crosses over at 0.20 (0.616 own versus 0.436 partner) once the
partner tax has pushed pop_1 into the hitchhiking state described below. M sits
between the families and is close to a wash: an iso-budget 0.20 loaded entirely on
either side gives the same total, 0.206.

The genotypes identify P's mechanism as the **partner-choice bottleneck**: a swap
requires C1P1 on both sides, so a chooser is useless without a chooser to trade
with.

| Cell         | Payer  | pop_0 qB | pop_0 P1 | pop_0 C1P1 | pop_1 P1 | pop_1 C1P1 |
| ------------ | ------ | -------: | -------: | ---------: | -------: | ---------: |
| (0.20, 0.00) | pop_0  | 0.585    | 0.202    | 0.187      | 0.659    | 0.243      |
| (0.00, 0.20) | pop_1  | 0.069    | 0.519    | 0.044      | 0.032    | 0.006      |

At (0.20, 0.00) pop_0 has been taxed down to P1 = 0.202, but almost all of that
residue is **active** (C1P1 = 0.187) and pop_1 still supplies 0.243 active
choosers, so swaps keep happening and cooperation holds at 0.585.

At (0.00, 0.20) pop_0 pays nothing, so its P1 = 0.519 is not retention against
pressure -- it is simply the neutral value, and the behaviourally inert loci in
this mechanism sit at the same place (Q1 = 0.498, M1 = 0.504). The informative
number is that only 0.044 of that allele is **expressed**. With pop_1's choosers
taxed out of existence (C1P1 = 0.006) there is nobody to swap with, assortment
fails, pop_0 goes to defection (C0 = 0.931), and by the C0P1 silencing rule its
chooser allele survives only in defectors who never use it. So an untaxed
population ends up with a quarter of the active choosers, and a tenth of the
cooperation, of the same population carrying a 0.20 tax itself -- not because it
lost the allele, but because the allele has nothing to act on.

Why the families choose opposite axes follows from what each does with a taxed
population. Partner choice is bilateral, so it is rationed by whichever side has
fewest choosers to spare -- and that is pop_1, which is short of them before any
tax is applied: at (0, 0) the active-chooser frequencies are already
C1P1 = 0.532 in pop_0 against 0.167 in pop_1, because being the expensive-c side
it is mostly defectors (C0 = 0.811), in which the chooser allele is silent. Taxing
the population holding a third as many choosers is what removes the swap partners.
Reciprocity-bearing mechanisms are not
rationed that way: a taxed population can shed its machinery into tax-free
unconditional cooperation and keep cooperating. That escape is harmless when the
taxed side is pop_1, which contributes little cooperation anyway, and destructive
when it is pop_0, which is carrying most of it. Hence Cost1 binds partner choice
and Cost0 binds the reciprocity family.

## The hitchhiking wedge requires a reciprocity locus

The inversion where pop_1 cooperates more is confined to the **Cost0 <= 0.02 strip**
for every mechanism that shows it, and which mechanisms show it is decided by
whether the **reciprocity family** is present -- not by how much tax the mechanism
pays.

The tax is charged per family, not per allele:
cost = Cost x ((Choose || Choose_lt) + (Mimic || Imimic || Imimic_lt)), so the
choice family (P, Q) costs one unit whether one or both loci are carried, and the
reciprocity family (M, I, J) likewise. A mechanism therefore pays 0, 1 or 2 units
regardless of how many loci it enables.

| Mechanism | Families (tax units) | Reciprocity family | Flips in Cost0 <= 0.02 strip | Flips elsewhere |
| --------- | -------------------: | ------------------ | ---------------------------: | --------------: |
| _         | 0 enabled            | no                 | 0                            | 0               |
| P         | 1                    | no                 | 0                            | 3               |
| M         | 1                    | yes                | 10                           | 0               |
| MP        | 2                    | yes                | 3                            | 0               |
| MPQ       | 2                    | yes                | 1                            | 0               |
| IMP       | 2                    | yes                | 13                           | 0               |
| IJMPQ     | 2                    | yes                | 13                           | 0               |

The comparison is properly controlled in both directions. **At one tax unit**, M
and P pay exactly the same and differ only in which family they carry: M inverts
in 10 cells, P in none. **At two tax units**, MP, MPQ, IMP and IJMPQ all pay the
same and invert in 3, 1, 13 and 13 cells respectively, so the amount paid does not
predict the inversion either. What tracks it is the reciprocity family, which
supplies the second-order-free-rider niche that unconditional cooperation occupies
once active machinery becomes unaffordable.

Because the tax is a family-level OR, shedding part of a family buys nothing --
dropping M while keeping I or J still costs a full unit. Selection therefore
removes the family as a block rather than locus by locus, and the data show exactly
that: at the wedge apex pop_1 has M1 = 0.031, I1 = 0.030 and J1 = 0.035 together,
alongside P1 = 0.047 and Q1 = 0.051. Both families go at once.

All **13 IJMPQ flip cells** lie on the strip with Cost1 >= 0.08. IMP shows the same
13-cell wedge with the same geography (IMP starts flipping at Cost1 >= 0.06).

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

Genotypes at the wedge apex (0, 0.20) confirm the hitchhiking story from
asymmetric_i0_i1:

| Pop | qBSeen | P1    | C1P0  | M1    | C1M0  |
| --- | -----: | ----: | ----: | ----: | ----: |
| 0   | 0.741  | 0.571 | 0.213 | 0.336 | 0.311 |
| 1   | 0.911  | 0.047 | 0.897 | 0.031 | 0.913 |

C1P0 and C1M0 are the conventional single-locus summaries, but under a six-locus
mechanism they are only loose proxies for "pays nothing": a C1M0 individual still
owes a reciprocity unit if it carries I1 or J1. Scoring the genotypes by the
families they actually carry gives the exact version:

| Pop | Carries neither family | Choice only | Reciprocity only | Both  | Mean units | Fully tax-free cooperators |
| --- | ---------------------: | ----------: | ---------------: | ----: | ---------: | -------------------------: |
| 0   | 0.069                  | 0.267       | 0.116            | 0.547 | 1.478      | 0.021                      |
| 1   | 0.822                  | 0.088       | 0.083            | 0.007 | 0.185      | 0.773                      |

Pop_1 has shed **both** families almost entirely: 0.822 of it carries no taxable
machinery at all and 0.773 of it is a fully tax-free cooperator (C1I0J0M0P0Q0),
against 0.021 in pop_0. Measured properly the hitchhiking is therefore stronger
than the single-locus columns suggest, not weaker. Pop_0 keeps its machinery --
it pays Cost0 = 0 here, so nothing is selecting against it -- yet cooperates less
and earns more (w = 0.791 / 0.577).

The paradox of success is **exceptionless inside the wedge**: in all 13 IJMPQ
flip cells, all 13 IMP flip cells, and all 10 M flip cells, the population that
cooperates more is the poorer one.

### The wedge boundary is a bistable threshold, not a gradient

Along Cost0 = 0 the inversion comes on smoothly, but one step in from that edge it
comes on as a jump, and raising a population's **own** information cost can raise
its cooperation. Along the Cost0 = 0.02 row under IJMPQ:

| Cost1 | pop_0 qB | pop_0 SD | pop_1 qB | pop_1 SD | dq     |
| ----: | -------: | -------: | -------: | -------: | -----: |
| 0.00  | 0.855    | 0.095    | 0.680    | 0.249    | +0.175 |
| 0.02  | 0.806    | 0.108    | 0.621    | 0.244    | +0.185 |
| 0.04  | 0.941    | 0.008    | 0.942    | 0.009    | -0.001 |
| 0.06  | 0.928    | 0.013    | 0.940    | 0.011    | -0.012 |
| 0.08  | 0.911    | 0.016    | 0.934    | 0.010    | -0.023 |

Doubling pop_1's own tax from 0.02 to 0.04 **raises** its cooperation by 0.321.
The run-to-run standard deviations identify what is happening: below the threshold
pop_1's SD is 0.24--0.25, enormous for a 30-run mean of a quantity bounded in
[0, 1], so the runs are split between two attractors and the mean is reporting a
mixture rather than a state. Above the threshold SD falls to 0.009 and every run
locks into the same high-cooperation state. For comparison, the smooth Cost0 = 0
edge has SD 0.004--0.044 throughout.

The genotypes confirm which attractor wins:

| Cell         | pop_1 qB | pop_1 P1 | pop_1 C1P0 | pop_1 C0 |
| ------------ | -------: | -------: | ---------: | -------: |
| (0.02, 0.02) | 0.621    | 0.349    | 0.306      | 0.515    |
| (0.02, 0.04) | 0.942    | 0.195    | 0.747      | 0.073    |

The tax tips pop_1 out of a defector-heavy mixed state (C0 = 0.515) into
near-complete tax-free unconditional cooperation (C1P0 0.306 -> 0.747). So the
information cost is not monotonically harmful: crossing the threshold buys entry
to a machinery-free cooperative equilibrium that the population could not reach
while cheap machinery was still worth carrying. IMP shows the same jump on the same
row (pop_1 0.445 -> 0.657 -> 0.892 as Cost1 goes 0 -> 0.02 -> 0.04).

### P also inverts, but in the opposite corner and for a different reason

P's 3 flip cells are at (0.24, 0.00), (0.24, 0.02) and (0.26, 0.00) -- the
high-Cost0, low-Cost1 corner, as far from the hitchhiking wedge as the square
allows. They are not floor noise (the control sits at 0.05 / 0.03 there) but they
are not hitchhiking either. They are a **crossing during pop_0's own collapse**:

| Cost0 | pop_0 qB | pop_0 C1P1 | pop_1 qB | pop_1 P1 | dq     |
| ----: | -------: | ---------: | -------: | -------: | -----: |
| 0.20  | 0.585    | 0.187      | 0.268    | 0.659    | +0.317 |
| 0.22  | 0.473    | 0.191      | 0.348    | 0.715    | +0.125 |
| 0.24  | 0.235    | 0.138      | 0.288    | 0.678    | -0.053 |
| 0.26  | 0.148    | 0.077      | 0.176    | 0.600    | -0.028 |
| 0.28  | 0.061    | 0.011      | 0.042    | 0.498    | +0.019 |

Pop_0's active choosers survive the tax until Cost0 ~ 0.22 and then fall off a
cliff; pop_1, untaxed and still holding P1 ~ 0.68, briefly overtakes it before both
collapse. So partner choice does invert, but only transiently while the cheap-c
population's own machinery is dying -- the opposite causal story to the wedge, where
the inverting population is the one whose machinery has already gone.

### Contrast with the equal-c study at the same information-cost point

asymmetric_i0_i1 is the same information-cost geometry with the c-gap removed
(c0 = c1 = 0.10), so differencing the two isolates what the c-gap does. At
(Cost0, Cost1) = (0, 0.20):

| Mechanism | equal-c q (0 / 1) | unequal-c q (0 / 1) | equal-c dq | unequal-c dq | shift  |
| --------- | ----------------: | ------------------: | ---------: | -----------: | -----: |
| _         | 0.047 / 0.051     | 0.052 / 0.025     | -0.004     | +0.027     | +0.031 |
| M         | 0.116 / 0.284     | 0.090 / 0.115     | -0.168     | -0.025     | +0.143 |
| P         | 0.331 / 0.153     | 0.069 / 0.032     | +0.178     | +0.037     | -0.141 |
| MP        | 0.370 / 0.829     | 0.210 / 0.212     | -0.460     | -0.002     | +0.458 |
| MPQ       | 0.365 / 0.863     | 0.254 / 0.225     | -0.498     | +0.029     | +0.527 |
| IMP       | 0.393 / 0.854     | 0.436 / 0.536     | -0.461     | -0.100     | +0.361 |
| IJMPQ     | 0.681 / 0.922     | 0.741 / 0.911     | -0.241     | -0.171     | +0.070 |

Every M-bearing mechanism shifts **toward pop_0** when the c-gap is added, and for
MP and MPQ the shift is large enough to erase the inversion outright at this cell.
Only IJMPQ and IMP keep it, and only attenuated. P shifts the other way (-0.141),
but that is compression rather than reversal: both populations are near the floor
once the c-gap is present (0.069 / 0.032), so there is little gap left to express.

Counting over each study's whole grid makes the containment quantitative:

| Mechanism | equal-c cells favouring pop_1 | unequal-c cells favouring pop_1 | equal-c mean dq | unequal-c mean dq |
| --------- | ----------------------------: | ------------------------------: | --------------: | ----------------: |
| _         | 0 / 120                       | 0 / 176                       | -0.000    | +0.023    |
| M         | 44 / 120                      | 10 / 176                      | -0.041    | +0.035    |
| P         | 0 / 120                       | 3 / 176                       | +0.110    | +0.116    |
| MP        | 57 / 120                      | 3 / 176                       | -0.144    | +0.118    |
| MPQ       | 62 / 120                      | 1 / 176                       | -0.176    | +0.160    |
| IMP       | 76 / 120                      | 13 / 176                      | -0.186    | +0.118    |
| IJMPQ     | 85 / 120                      | 13 / 176                      | -0.201    | +0.160    |

Without the c-gap the inversion is the **majority** outcome for every M-bearing
mechanism (up to 85 / 120 for IJMPQ) and the mean gap is negative. Adding a 0.10
cooperation-cost gap flips every one of those means positive and cuts the inverted
cells to at most 13 / 176. The two grids are not the same shape, so the counts are
indicative rather than a like-for-like ratio; the sign change in the means is the
robust part.

At (Cost0, Cost1) = (0.10, 0.20), the equal-c study shows IJMPQ dq = -0.302 (strong
inversion), while the unequal-c study shows dq = +0.031 -- the c-gap advantage
is enough to override the hitchhiking inversion once both information costs are
non-zero.

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
floor, and pop_0 keeps the cooperation lead the whole way down. Note that this
strip taxes pop_1, not pop_0: it is the partner-tax collapse analysed above, and
it is far steeper than what pop_0's own tax does to it.

On the diagonal (symmetric information cost), P at (0.10, 0.10) still shows
pop_0 ahead (0.375 / 0.193). By (0.20, 0.20) both sides collapse (0.049 / 0.026).

P loses the lead in only 3 of 176 cells, all of them at Cost0 = 0.24--0.26 during
its own-machinery collapse rather than anywhere in the hitchhiking wedge (see the
opposite-corner section above).

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

This column also gives a clean read on the cost model itself. Under mechanism P
the Q, M, I and J loci are behaviourally inert but still taxable, since the charge
is levied on families carried rather than on machinery used. At Cost0 = 0 they sit
at their neutral values (Q1 = 0.511, M1 = 0.498); at Cost0 = 0.20 the tax alone has
driven them to Q1 = 0.069 and M1 = 0.026. Cost purges dormant machinery just as
effectively as active machinery. It also means C1P0 slightly overstates the
untaxed fraction -- the genuinely cost-free cooperators are 0.359 of pop_0 at
Cost0 = 0.20 against a C1P0 reading of 0.398, the gap being cooperators still
paying a choice unit through Q1.

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

## Iso-budget analysis: information costs are non-fungible and non-additive

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

### Sharing the tax is worse than concentrating it

Total cooperation (q0 + q1) along an iso-budget line is not monotone between the
endpoints: for every M-bearing mechanism the interior of the line is **worse than
either corner**.

| Mechanism | Budget | All on pop_1 | All on pop_0 | Worst split         | Sharing worse |
| --------- | -----: | -----------: | -----------: | ------------------- | ------------- |
| _         | 0.20   | 0.077        | 0.074        | 0.067 (0.08, 0.12)  | no            |
| P         | 0.20   | 0.102        | 0.854        | 0.102 (0.00, 0.20)  | no            |
| M         | 0.20   | 0.206        | 0.206        | 0.084 (0.10, 0.10)  | yes           |
| MP        | 0.20   | 0.423        | 0.892        | 0.209 (0.04, 0.16)  | yes           |
| MPQ       | 0.20   | 0.479        | 0.907        | 0.282 (0.04, 0.16)  | yes           |
| IMP       | 0.20   | 0.972        | 0.843        | 0.288 (0.04, 0.16)  | yes           |
| IJMPQ     | 0.20   | 1.652        | 1.003        | 0.390 (0.06, 0.14)  | yes           |

Under IJMPQ a budget of 0.20 loaded entirely onto one population yields 1.0--1.65
total cooperation, but split as (0.06, 0.14) it yields 0.390 -- worse than either
corner by a factor of 2.6 to 4.2. The reason follows from the two preceding
sections: each corner leaves one population with an intact, untaxed apparatus, and
one intact apparatus is enough to hold the pair together (either pop_0 enforcing,
or pop_1 hitchhiking into unconditional cooperation). A split budget is enough to
break both apparatuses and not enough to push either population over the
hitchhiking threshold, so the pair lands in the gap between the two working
regimes.

P is the exception and for the expected reason: its total cooperation is governed
by Cost1 almost alone (see the own-versus-partner section), so its iso-budget line
is monotone rather than U-shaped, with the best outcome at the corner that spares
pop_1.

A two-way additive fit (q ~ row effect + column effect) leaves maximum residuals of
0.31 (IJMPQ pop_0), 0.37 (M pop_0) and 0.22 (IMP pop_0), so the square is strongly
non-additive: the two information costs interact rather than summing.

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

### The cross-population coupling is created by the dilemma, not by the tax

Dilemma 0 is also the clean control for the own-versus-partner result above,
because it shows what the information tax does with no social dilemma to propagate
it. Under d0, M1 tracks **only** the cost its own population pays:

| pop_0 M1 | Cost1 = 0.00 | Cost1 = 0.04 | Cost1 = 0.10 | Cost1 = 0.20 |
| -------- | -----------: | -----------: | -----------: | -----------: |
| Cost0 = 0.00 | 0.347    | 0.406        | 0.443        | 0.467        |
| Cost0 = 0.04 | 0.144    | 0.172        | 0.194        | 0.187        |
| Cost0 = 0.10 | 0.067    | 0.078        | 0.083        | 0.081        |
| Cost0 = 0.20 | 0.035    | 0.039        | 0.041        | 0.042        |
| Cost0 = 0.30 | 0.024    | 0.026        | 0.027        | 0.026        |

| pop_1 M1 | Cost1 = 0.00 | Cost1 = 0.04 | Cost1 = 0.10 | Cost1 = 0.20 |
| -------- | -----------: | -----------: | -----------: | -----------: |
| Cost0 = 0.00 | 0.430    | 0.152        | 0.064        | 0.033        |
| Cost0 = 0.04 | 0.494    | 0.180        | 0.066        | 0.035        |
| Cost0 = 0.10 | 0.535    | 0.187        | 0.072        | 0.036        |
| Cost0 = 0.20 | 0.522    | 0.201        | 0.073        | 0.034        |
| Cost0 = 0.30 | 0.556    | 0.191        | 0.071        | 0.035        |

Pop_0's M1 varies down columns and is flat across rows; pop_1's does the reverse.
Quantitatively, corr(M1, own Cost) = -0.787 for pop_0 and -0.822 for pop_1, while
corr(M1, partner Cost) = +0.054 and +0.039 -- essentially zero. So the tax itself
is a **purely own-population, supply-side** effect with no cross-population channel.
Every cross-population dependence documented above -- pop_0 collapsing because
pop_1 was taxed, the hitchhiking wedge, the iso-budget U-shape -- is therefore
generated by the dilemma coupling the two populations' behaviour, not by the cost
accounting.

The one residual cross-effect is second-order and of the opposite sign: an untaxed
population retains slightly **more** machinery when its partner is taxed (pop_0 M1
rises 0.347 -> 0.467 across the Cost1 row at Cost0 = 0), presumably because
mimicking a partner that has shed its own machinery is less often punished.

## Snowdrift: c-gap dominates completely

In snowdrift (d = 2) the cooperation-cost asymmetry overwhelms any information-cost
wedge. Pop_0 cooperates more in all or nearly all cells for every mechanism:

| Mechanism | mean dq (PD) | mean dq (SD) | pop_0 coops (PD) |
| --------- | -----------: | -----------: | ---------------: |
| P         | +0.116       | +0.885       | 170 / 176        |
| IJMPQ     | +0.160       | +0.626       | 156 / 176        |
| IMP       | +0.118       | +0.734       | 154 / 176        |
| M         | +0.035       | +0.810       | 150 / 176        |

The hitchhiking wedge is a **PD phenomenon**, as in asymmetric_i0_i1. Cost0-row sign flip
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
- **Bistable cells report mixtures.** In the Cost0 = 0.02--0.04 band the 30-run
  qBSeen SD reaches 0.24--0.25, so the cell mean there is an average over runs that
  settled in different attractors, not a description of any single run. Means in
  that band should not be read as equilibrium levels. Outside it, SD is typically
  0.004--0.05.
- **Allele frequencies in an untaxed population are not evidence of retention.**
  A population facing Cost = 0 has no selection against machinery, so its loci sit
  at or near their neutral values -- under mechanism P at Cost0 = 0 the inert loci
  read Q1 = 0.511 and M1 = 0.498. Comparisons of allele frequency across the
  Cost = 0 boundary are therefore comparisons of tax versus no tax, and only
  expressed combinations (C1P1, C1M1) carry interpretive weight there.
- **Single-locus genotype columns are proxies, not tax accounts.** Because the
  charge is `Cost x ((P||Q) + (M||I||J))`, C1M0 and C1P0 include individuals still
  paying through a sibling locus. The gap is small where the whole family has been
  swept (0.398 versus 0.359 for P at Cost0 = 0.20) but should not be assumed.
- **Grid shapes differ across studies.** asymmetric_i0_i1 is a 120-cell strict
  triangle (Cost0 < Cost1) and this study a 176-cell square, so cross-study cell **counts** are
  indicative only; the like-for-like comparisons are the per-cell values at shared
  (Cost0, Cost1) points and the signs of the mean gaps.
- **Temporal.** Movie exports exist for asymmetric_c1_i0_i1_1run
  (csv_*_filtered_for_movie.con); temporal claims above use those 1run exports.
  Snapshot spacing is coarse (first recorded time t = 131072), so sub-establishment
  ordering is not resolved. In particular the temporal exports cannot show which
  attractor a bistable cell is heading for before t = 131072.

## Cross-study synthesis

This study closes the per-population information-cost triangle:

| Study                       | c asymmetry       | i asymmetry                    | Primary role assigner                        |
| --------------------------- | ----------------- | ------------------------------ | -------------------------------------------- |
| asymmetric_c0_c1            | c0 < c1           | none (Cost symmetric)          | c-gap -> pop_0 coops                         |
| asymmetric_c1_i             | c0 < c1 fixed     | Cost symmetric, c1 varies      | c-gap; Cost compresses                       |
| asymmetric_i0_i1            | c0 = c1           | Cost0 < Cost1                  | i-gap; mechanism-dependent                   |
| **asymmetric_c1_i0_i1**     | **c0 < c1 fixed** | **full Cost0 x Cost1**         | **c-gap globally; i-gap in an M-locus wedge** |

The one-line reading: **cooperation-cost asymmetry is the default role assigner
when both axes are asymmetric; information-cost asymmetry can locally invert
reciprocity-bearing mechanisms in a Cost0 ~ 0 wedge, but cannot globally overturn
the cheap-c population's cooperator role, and cannot do so at all once Cost0 is
non-negligible or the game is snowdrift.**

Three findings here are new to the programme rather than refinements of
asymmetric_i0_i1, and all three come from having the full square rather than a
triangle:

1. **Information cost is mostly a partner's problem.** Under partner choice, a
   population's cooperation is nearly invariant to its own information cost
   (0.602 -> 0.585 as Cost0 goes 0 -> 0.20) and collapses under its partner's
   (0.602 -> 0.069). The swap rule requires C1P1 on both sides, so the binding
   constraint is the chooser supply of whichever population has least of it.
2. **The wedge is gated by the reciprocity family, not by the tax paid.** M and P
   cost the same one unit, yet M inverts in 10 cells and P in none; MP, MPQ, IMP and
   IJMPQ all cost the same two units, yet invert in 3, 1, 13 and 13. No mechanism
   lacking the reciprocity family inverts in the wedge at all.
3. **Concentrating an information-cost budget beats sharing it.** For every
   M-bearing mechanism, total cooperation at an interior split is below both
   iso-budget corners -- by a factor of 2.6--4.2 under IJMPQ at budget 0.20.

The dilemma-0 control ties them together: with no social dilemma the tax has no
cross-population channel at all (corr(M1, partner Cost) = +0.05), so all three
effects are properties of the dilemma coupling the populations, not of the cost
accounting.
