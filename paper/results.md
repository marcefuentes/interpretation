# Results

*Numbers are cited to the journal analyses that derive and regression-check them
(`ai/verify_claims.py`) rather than restated in full. Figures are the locked
main-text set (Figs. 1–6) and supplement (Figs. S1–S9).*

## 1. Mechanism hierarchy and cost thresholds

At equal cooperation cost in a single population, each enforcement architecture
sustains cooperation up to a characteristic cost and then collapses (Fig. 1). The
no-enforcement control (Fig. 1a) stays near the floor across the prisoner's-dilemma
sweep; direct reciprocity (Fig. 1b), partner choice (Fig. 1c), and the combined
reputation-rich mechanism (Fig. 1d) raise that ceiling in that order. The same
columns under snowdrift (Fig. 1e–h) sit much higher: the elevated sucker payoff
already favours cooperation without enforcement, so the hierarchy softens and the
c-collapse matters far less than in the PD
([synthesis](../journal/synthesis.md)).

A single cooperation-cost axis cannot say *which* payoff gap drives a collapse,
because raising c simultaneously raises temptation (T − R), raises risk (P − S),
and shrinks the cooperation advantage (R − P). Orthogonal payoff-plane calibration
sweeps (not shown; Table S1) decouple these
([PD calibration](../journal/prisoners_calibration.md),
[snowdrift calibration](../journal/snowdrift_calibration.md)):

- **Direct reciprocity (M) is risk-limited.** Collapse as c rises tracks the growing
  mutual-defection risk rather than the shrinking R − P — confirmed from the other
  side in snowdrift, where the low sucker gap lets M sustain cooperation it cannot in
  the PD ([direct reciprocity](../journal/symmetric_c_reciprocity.md)).
- **Partner choice (P) is limited by the cooperation advantage R − P.** It tracks
  R − P alone across the orthogonal sweep, which is why it fails at the chooser
  bottleneck as R − P → 0.
- **Combined and reputation-rich mechanisms (MP, MPQ, IMP, IJMPQ) are reward-limited**
  and largely blind to the defection baseline, which is why they hold cooperation to
  the highest costs (Fig. 1d).

These attributions recover a mechanistic distinction that foreshadows the relational
result below. A residual chooser minority sorts the whole population, so even
unconditional cooperators are protected; a residual reciprocator minority protects
only itself ([reciprocity](../journal/symmetric_c_reciprocity.md)). Partner choice
assorts at the population level; reciprocity remembers at the individual level.
Short-memory and shuffle variants shift the direct-reciprocity collapse ordering
relative to Fig. 1 but leave the partner-choice versus combined contrast intact
(Fig. S2).

## 2. The two-population role split

With two coevolving populations the outcome often breaks into a cooperator/exploiter
role split, and the cooperating side is typically the one that earns less — the
paradox of success. We distinguish this **outcome** asymmetry (gaps in cooperation
and fitness) from **parameter** symmetry in the setup (whether c₀ = c₁, i₀ = i₁, and
payoffs match). Mechanism can override the default mapping.

When costs and payoffs match (c₀ = c₁, i₀ = i₁), partner choice produces a
**stochastic** assignment in the prisoner's dilemma that is absent without
enforcement (Fig. 2a–d). One population carries cooperation and is exploited; carrying
the chooser allele correlates with fitness at roughly minus one
([partner choice calibration](../journal/prisoners_partner_choice.md)). In snowdrift
the same split already appears in the no-enforcement columns; partner choice mainly
reshapes high-cooperation-cost outcomes (Fig. 2e–h). Combined reputation mechanisms
at the same parameter point stay nearly outcome-symmetric in the PD.

A small cooperation-cost gap converts that chance split into a deterministic one.
Along the strip c₁ = c₀ + 0.02, partner choice assigns the lower-cooperation-cost
population as cooperator in every cell and converts the R − P gap into a stable
cooperation gap (Fig. 3a,b;
[partner choice under cooperation-cost asymmetry](../journal/asymmetric_c0_c1_partner_choice.md),
[synthesis](../journal/synthesis.md)). Combined IJMPQ lifts the expensive population
and shrinks the outcome asymmetry on the same axes (Fig. 3c,d), because reward-led
mechanisms no longer route R − P into a cooperation gap
([combined mechanisms](../journal/asymmetric_c0_c1_combined.md)). Fig. 3 is
prisoner's-dilemma only: under no enforcement the cheap population barely cooperates
in the PD (control mean ≈ 0.10), so partner choice is what *creates* the
deterministic split from the parameter gap (Fig. S1; full c₀ × c₁ grid in Fig. S9).
In snowdrift the sucker payoff already sustains high cooperation without machinery
(control ≈ 0.96 vs partner choice ≈ 0.96 for the cheap side), and between-population
asymmetry often appears from payoffs alone (Fig. 2e–h). A parallel asymmetric
snowdrift panel would repeat that floor rather than isolate what enforcement adds.
Fig. S5 contrasts the deterministic and stochastic strips on shared axes; the split
survives small-group stochasticity at group size 4 (Fig. S3).

Single-run trajectories confirm that these roles are absorbing states locked in by
the first recorded snapshot (t = 131072), not slow late erosions. The temporal
regime does not differ between one and two populations
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

## 3. Costly machinery, decoupling, and why symmetry hides the question

Making the enforcement apparatus itself costly introduces a pressure orthogonal to
cooperation cost
([information cost at equal cooperation cost](../journal/symmetric_c_i.md)). Taxing
the machinery alone erodes cooperation only gently where temptation is absent,
because a population can shed the apparatus and keep cooperating for free. Where the
two costs overlap, information cost thins the defence cooperation cost requires and
pulls the c-collapse threshold downward (Fig. S7).

At zero cooperation cost the genotype route makes the escape visible (Fig. 4). As
information cost rises, active enforcement alleles are selected out — chooser P1
(Fig. 4a) and TFT M1 (Fig. 4c) both fall toward zero — while cooperation remains high
on tax-free unconditional cooperators (Fig. 4b,d: C1P0, C1M0). Behaviour and
mechanism decouple. A dilemma-free control shows that machinery erodes with or
without a social dilemma; cooperation persists through the shed only when the dilemma
is present, so the tax drives the erosion and the dilemma decides whether losing the
machinery drags behaviour down (Fig. S4).

That refuge disappears once cooperation cost is held above zero. Machinery loss and
behavioural loss then move together: shedding P1 or M1 no longer leaves a stable
high-cooperation niche behind
([information cost under cooperation-cost asymmetry](../journal/asymmetric_c1_i.md)).
With a fixed cooperation-cost gap, information cost retreats the cooperation ceiling
and steadily compresses both the cooperation gap and the fitness gap; the paradox of
success remains while partner choice still functions, then disappears mainly because
the system is driven to the control floor (Fig. S8). Second-order free-riders (C1M0)
and silent carriers (C0P1) accumulate along the same routes
([reciprocity](../journal/symmetric_c_reciprocity.md),
[reciprocity under cooperation-cost asymmetry](../journal/asymmetric_c0_c1_reciprocity.md)).

A symmetric information-cost design cannot separate the cost a population pays from
the cost its partner pays. The decoupling route looks like a private escape — shed
the tax, keep cooperating — but that reading is an artefact of levying the same tax
on both sides at once. Holding one population's information cost at zero and sweeping
the other's breaks the confound.

## 4. Information cost is relational

Figs. 5–6 cross a fixed cooperation-cost gap (c₀ = 0.1, c₁ = 0.2) with independent
per-population information costs. The first two columns of Fig. 5 hold one
population's information cost at zero and sweep the other's, so the comparison
isolates whose cost bites
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

Under partner choice the two strip columns tell opposite stories (Fig. 5a,b). Taxing the
low-cooperation-cost population to i = 0.20 leaves it essentially flat (0.602 → 0.585)
and even raises its partner (0.189 → 0.268). Moving the same tax onto the
high-cooperation-cost population collapses both (0.069 and 0.032). A population under
partner choice is nearly insensitive to its own information cost and collapses under
its partner's. The bilateral swap rule is why: a chooser is useless without a chooser
to trade with, so assortment is rationed by whichever population has fewest choosers
to spare — and that is already the high-cost side before any tax is applied.

Under the combined reputation-rich mechanism the binding axis swaps (Fig. 5d,e).
Taxing the low-cooperation-cost population to i = 0.20 drives its partner from 0.957
to 0.268 while the payer itself falls only to 0.734 — the partner is hurt more than
the payer. Taxing the high-cost side instead leaves that side near 0.911. Reciprocity-
bearing mechanisms protect only their carriers: a taxed population can shed into
unconditional cooperation, which is harmless when the taxed side contributes little
cooperation and destructive when it carries most of it. The binding axis is therefore
the cost paid by the *low*-cooperation-cost population — the opposite of partner
choice.

Genotype composition confirms that the partner's cost can silence an untaxed
allele. At (i₀, i₁) = (0, 0.20) the untaxed population's chooser frequency sits at
its neutral value (P1 = 0.519; inert Q1 = 0.498, M1 = 0.504), yet almost none of it
is expressed (C1P1 = 0.044, against 0.187 in the same population when it carries the
0.20 tax itself). With the partner's choosers taxed away there is nobody to swap
with; the population collapses to defection and the allele survives only in silent
defector carriers.

The escape route that made information cost survivable under symmetry (Fig. 4) is
what makes it destructive under asymmetry: shedding relieves the payer and withdraws
the service the partner depended on.

## 5. Budget non-convexity and boundary conditions

Equal enforcement budgets are neither fungible nor additive (Fig. 5c,f). Along a line of
constant total information cost (0.20), every reciprocity-bearing mechanism reaches
its *lowest* total cooperation in the interior rather than at either end. Under IJMPQ
a budget of 0.20 yields 1.0–1.65 when loaded onto one population but 0.39 when split
as (0.06, 0.14) (Fig. 5f). Either corner leaves one population with an intact
apparatus, which is enough to hold the pair together; a split breaks both and pushes
neither over the threshold where machinery-free cooperation takes over. Partner choice
is monotone instead (Fig. 5c): because only the high-cooperation-cost population's
information cost bites, the best outcome sits at the corner that spares that
population. The non-convexity is therefore a property of reciprocity-bearing
mechanisms, not of the budget itself
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

When both cost axes differ, the cooperation-cost gap remains the default role
assigner. Across the full i₀ × i₁ square behind Figs. 5–6, partner choice assigns the
lower-cooperation-cost population as cooperator in 170/176 cells; IJMPQ inverts
locally only on the i₀ ≈ 0 strip (13 cells). That hitchhiking inversion is stronger
when cooperation costs are equal and only information cost differs (Fig. S6: IMP
dq = −0.461 at Cost0 = 0, Cost1 = 0.20) and is attenuated once the cooperation-cost
gap is present (IMP dq = −0.100 at the same information-cost point). The gap moves
every reciprocity-bearing mechanism toward the cheap-cooperation-cost population,
erasing the inversion outright for MP and MPQ
([per-population information cost](../journal/asymmetric_i0_i1.md),
[crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

Fig. 6 shows the wedge closing. Each panel fixes the information cost on the
low-cooperation-cost population and sweeps the other. The inversion — the expensive
population's curve above the cheap one's — holds throughout when i₀ = 0 (Fig. 6a),
survives only past a threshold when i₀ = 0.02 (Fig. 6b), and is gone by i₀ = 0.04 and
0.1 (Fig. 6c,d). Crossing into the machinery-free state is a bistable threshold, not
a slope: just inside the wedge, doubling a population's own information cost *raises*
its cooperation by 0.32 as it tips from a defector-heavy mixed state into near-
complete tax-free unconditional cooperation. Run-to-run variance marks the basin
boundary directly in the ±1 SD bands — wide below the threshold (SD ≈ 0.25; runs
split between two attractors) and collapsed above it (SD ≈ 0.009).

The inversion is gated by the reciprocity family, not by how much information cost a
mechanism pays. Information cost is charged per family carried — one unit for partner
choice, one for reciprocity — so a mechanism owes 0, 1 or 2 units however many loci
it enables. At one unit, direct reciprocity and partner choice pay identically, yet
reciprocity inverts in 10 cells of the i₀ ≈ 0 strip and partner choice in none. At
two units, the four combined mechanisms pay identically, yet invert in 3, 1, 13 and
13 cells. Every mechanism carrying the reciprocity family inverts somewhere in that
strip; no mechanism lacking it does. Reciprocity supplies the second-order-free-rider
niche that unconditional cooperation occupies once active machinery becomes
unaffordable. Partner choice does lose the lead in three cells, but in the opposite
corner of the square and by the opposite route: a transient crossing while its *own*
machinery collapses.

Snowdrift removes the wedge entirely, identifying the relational burden as a property
of the dilemma rather than of the cost accounting
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)). The dilemma-0 control
makes the same point for the decoupling claim (Fig. S4). Shuffle and group-size
panels locate which loci carry the baseline effects (Figs. S2, S3).
