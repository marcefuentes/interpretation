# Results

*Numbers are cited to the journal analyses that derive and regression-check them
(`ai/verify_claims.py`) rather than restated in full. Figures are the locked
main-text set (Figs. 1–5) and supplement (Figs. S1–S11).*

## 1. Mechanism hierarchy and cost thresholds

At equal cooperation cost in a single population, each enforcement architecture
sustains cooperation up to a characteristic cost and then collapses (Fig. S1). The
no-enforcement control (Fig. S1a) stays near the floor across the prisoner's-dilemma
range; direct reciprocity (Fig. S1b), partner choice (Fig. S1c), and the combined
reputation-rich mechanism (Fig. S1d) raise that ceiling in that order. The same
columns under snowdrift (Fig. S1e–h) sit much higher: the elevated sucker payoff
already favours cooperation without enforcement, so the hierarchy softens and the
c-collapse matters far less than in the PD
([synthesis](../journal/synthesis.md)).

A single cooperation-cost axis cannot say *which* payoff gap drives a collapse,
because raising c simultaneously raises temptation (T − R), raises risk (P − S),
and shrinks the cooperation advantage (R − P). Orthogonal payoff-plane calibration
analyses (not shown; Table S1) decouple these
([PD calibration](../journal/prisoners_calibration.md),
[snowdrift calibration](../journal/snowdrift_calibration.md)):

- **Direct reciprocity (M) is risk-limited.** Collapse as c rises tracks the growing
  mutual-defection risk rather than the shrinking R − P — confirmed from the other
  side in snowdrift, where the low sucker gap lets M sustain cooperation it cannot in
  the PD ([direct reciprocity](../journal/symmetric_c_reciprocity.md)).
- **Partner choice (P) is limited by the cooperation advantage R − P.** It tracks
  R − P alone across the orthogonal calibration, which is why it fails at the chooser
  bottleneck as R − P → 0.
- **Combined and reputation-rich mechanisms (MP, MPQ, IMP, IJMPQ) are reward-limited**
  and largely blind to the defection baseline, which is why they hold cooperation to
  the highest costs (Fig. S1d).

These attributions recover a mechanistic distinction that foreshadows the relational
result below. A residual chooser minority sorts the whole population, so even
unconditional cooperators are protected; a residual reciprocator minority protects
only itself ([reciprocity](../journal/symmetric_c_reciprocity.md)). Partner choice
assorts at the population level; reciprocity remembers at the individual level.
Short-memory and shuffle variants shift the direct-reciprocity collapse ordering
relative to Fig. S1 but leave the partner-choice versus combined contrast intact
(Fig. S2).

## 2. The two-population role split

With two coevolving populations the outcome often breaks into a cooperator/exploiter
role split, and the more cooperative side is typically the one that earns less
fitness. We distinguish this **outcome** asymmetry (gaps in cooperation
and fitness) from **parameter** symmetry in the setup (whether c₀ = c₁, i₀ = i₁, and
payoffs match). Mechanism can override the default mapping.

When costs and payoffs match (c₀ = c₁, i₀ = i₁), partner choice produces a
**stochastic** assignment in the prisoner's dilemma that is absent without
enforcement (Fig. 1a–d). One population carries cooperation and is exploited; carrying
the chooser allele correlates with fitness at roughly minus one
([partner choice calibration](../journal/prisoners_partner_choice.md)). In snowdrift
the same split already appears in the no-enforcement columns; partner choice mainly
reshapes high-cooperation-cost outcomes (Fig. 1e–h). Combined reputation mechanisms
at the same parameter point stay nearly outcome-symmetric in the PD.

**Figure 1: Outcome asymmetry under parameter-symmetric cooperation cost.** Frequency of cooperators and average fitness in two coevolving populations (red indicates the population with the lower frequency of cooperators; orange the other). **A–D**, Prisoner's dilemma. **E–H**, Snowdrift game. **A, E**, Baseline without enforcement mechanisms. **B, F**, Short-memory partner choice is the only available mechanism. Both populations pay identical cooperation costs ($c$, swept from 0 to the partner benefit $b$) and identical information costs ($0.001$). Under matched costs, partner choice generates a stochastic cooperator/exploiter role split in the prisoner's dilemma that is absent without enforcement. In the snowdrift game, the split already exists in the baseline and partner choice primarily extends it to higher costs.

A small cooperation-cost gap converts that chance split into a deterministic one.
Along the strip c₁ = c₀ + 0.02, partner choice assigns the lower-cooperation-cost
population as cooperator in every cell and converts the R − P gap into a stable
cooperation gap (Fig. 2a,b;
[partner choice under cooperation-cost asymmetry](../journal/asymmetric_c0_c1_partner_choice.md),
[synthesis](../journal/synthesis.md)). Combined IJMPQ lifts the expensive population
and shrinks the outcome asymmetry on the same axes (Fig. 2c,d), because reward-led
mechanisms no longer route R − P into a cooperation gap
([combined mechanisms](../journal/asymmetric_c0_c1_combined.md)). Fig. 2 is
prisoner's-dilemma only: under no enforcement the cheap population barely cooperates
in the PD (control mean ≈ 0.10), so partner choice is what *creates* the
deterministic split from the parameter gap (Fig. S3; full c₀ × c₁ grid in Fig. S4).
In snowdrift the sucker payoff already sustains high cooperation without machinery
(control ≈ 0.96 vs partner choice ≈ 0.96 for the cheap side), and between-population
asymmetry often appears from payoffs alone (Fig. 1e–h). A parallel asymmetric
snowdrift panel would repeat that floor rather than isolate what enforcement adds.
Fig. S5 contrasts the deterministic and stochastic strips on shared axes; the split
survives small-group stochasticity at group size 4 (Fig. S6).

**Figure 2: Deterministic role splits emerge from cooperation-cost asymmetries.** Frequency of cooperators and average fitness for two coevolving populations under the prisoner's dilemma, evaluated along the parameter strip $c_1 = c_0 + 0.02$ (with both populations overlaid). **A, B**, Short-memory partner choice alone. **C, D**, Combined partner choice and indirect reciprocity. Both populations pay identical information costs ($0.001$). A small cooperation-cost gap allows partner choice to convert the payoff asymmetry into a stable cooperator/exploiter assignment (**A, B**). The combined reputation-rich mechanism lifts the expensive population, shrinking the outcome asymmetry (**C, D**).

Single-run trajectories confirm that these roles are absorbing states locked in by
the first recorded snapshot (t = 131072), not slow late erosions. The temporal
regime does not differ between one and two populations
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

With this cooperation-cost baseline established, we next ask how information-cost
asymmetry reshapes or overrides the role split.

## 3. Costly machinery, decoupling, and why symmetry hides the question

Making the enforcement apparatus itself costly introduces a pressure orthogonal to
cooperation cost
([information cost at equal cooperation cost](../journal/symmetric_c_i.md)). Taxing
the machinery alone erodes cooperation only gently where temptation is absent,
because a population can shed the apparatus and keep cooperating for free. Where the
two costs overlap, information cost thins the defence cooperation cost requires and
pulls the c-collapse threshold downward (Fig. S7).

At zero cooperation cost the genotype route makes the escape visible (Fig. 3). As
information cost rises, active enforcement alleles are selected out — chooser P1
(Fig. 3a) and TFT M1 (Fig. 3c) both fall toward zero — while cooperation remains high
on tax-free unconditional cooperators (Fig. 3b,d: C1P0, C1M0). Behaviour and
mechanism decouple. A dilemma-free control shows that machinery erodes with or
without a social dilemma; cooperation persists through the shed only when the dilemma
is present, so the tax drives the erosion and the dilemma decides whether losing the
machinery drags behaviour down (Fig. S8).

**Figure 3: Information cost decouples cooperation from enforcement machinery when cooperation is free.** Frequency of the active machinery allele (chooser P1 in **A**; tit-for-tat M1 in **C**) and overall frequency of cooperators (**B, D**) in a single population. **A, B**, Short-memory partner choice alone. **C, D**, Direct reciprocity alone. The cooperation cost is fixed at zero while the information cost is swept from 0 to the partner benefit ($b = 0.4$). Rising information cost selects against active enforcement alleles, but cooperation remains high because populations shed the costly machinery in favour of tax-free unconditional cooperation.

That refuge disappears once cooperation cost is held above zero. Machinery loss and
behavioural loss then move together: shedding P1 or M1 no longer leaves a stable
high-cooperation niche behind
([information cost under cooperation-cost asymmetry](../journal/asymmetric_c1_i.md)).
With a fixed cooperation-cost gap, information cost retreats the cooperation ceiling
and steadily compresses both the cooperation gap and the fitness gap; the pattern in
which the more cooperative side is less fit remains while partner choice still functions, then disappears mainly because
the system is driven to the control floor (Fig. S9). Second-order free-riders (C1M0)
and silent carriers (C0P1) accumulate along the same routes
([reciprocity](../journal/symmetric_c_reciprocity.md),
[reciprocity under cooperation-cost asymmetry](../journal/asymmetric_c0_c1_reciprocity.md)).

A symmetric information-cost design cannot separate the cost a population pays from
the burden that cost creates for its partner. The decoupling route looks like a local escape — shed
the tax, keep cooperating — but that reading is an artefact of levying the same tax
on both sides at once. Holding one population's information cost at zero and varying
the other's breaks the confound.

## 4. Information cost is relational

Figs. 4–5 cross a fixed cooperation-cost gap (c₀ = 0.1, c₁ = 0.2) with independent
per-population information costs. The first two columns of Fig. 4 hold one
population's information cost at zero and sweep the other's, so the comparison
shows more clearly which population's information cost creates the larger burden
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

Under partner choice the two strip columns tell opposite stories (Fig. 4a,b). Taxing the
low-cooperation-cost population to i = 0.20 leaves it essentially flat (0.602 → 0.585)
and even raises its partner (0.189 → 0.268). Moving the same tax onto the
high-cooperation-cost population collapses both (0.069 and 0.032). A population under
partner choice is nearly insensitive to its own information cost and collapses under
its partner's. The bilateral swap rule is why: a chooser is useless without a chooser
to trade with, so assortment is rationed by whichever population has fewest choosers
to spare — and that is already the high-cost side before any tax is applied.

Under the combined reputation-rich mechanism the pattern reverses (Fig. 4d,e).
Taxing the low-cooperation-cost population to i = 0.20 drives its partner from 0.957
to 0.268 while the payer itself falls only to 0.734 — the partner is hurt more than
the payer. Taxing the high-cost side instead leaves that side near 0.911. Reciprocity-
bearing mechanisms protect only their carriers: a taxed population can shed into
unconditional cooperation, which is harmless when the taxed side contributes little
cooperation and destructive when it carries most of it. Here the larger burden comes
from the information cost paid by the *low*-cooperation-cost population — the opposite
of partner choice.

Genotype composition confirms that the partner's cost can silence an untaxed
allele. At (i₀, i₁) = (0, 0.20) the untaxed population's chooser frequency sits at
its neutral value (P1 = 0.519; inert Q1 = 0.498, M1 = 0.504), yet almost none of it
is expressed (C1P1 = 0.044, against 0.187 in the same population when it carries the
0.20 tax itself). With the partner's choosers taxed away there is nobody to swap
with; the population collapses to defection and the allele survives only in silent
defector carriers.

The fitness counterpart to these relational slices shows similar cross-population burdens and iso-budget interior penalties (Fig. S10).

The escape route that made information cost survivable under symmetry (Fig. 3) is
what makes it destructive under asymmetry: shedding relieves the payer and withdraws
the service the partner depended on.

**Figure 4: The relational burden of information cost.** Frequency of cooperators in two coevolving populations under the prisoner's dilemma. One population (orange) has a lower cooperation cost ($c_0 = 0.1$) than the other (red; $c_1 = 0.2$). **A–C**, Short-memory partner choice alone. **D–F**, Combined partner choice and indirect reciprocity. **A, D**, Information cost is applied only to the low-cooperation-cost population ($i_1 = 0$; $i_0$ swept). **B, E**, Information cost is applied only to the high-cooperation-cost population ($i_0 = 0$; $i_1$ swept). **C, F**, The total information budget is fixed at $i_0 + i_1 = 0.2$ while the distribution between populations varies. Under partner choice (**A, B**), populations are robust to their own information costs but collapse under their partner's. Under the combined reputation mechanism (**D, E**), this relationship reverses: taxing the low-cost population severely harms its high-cost partner. Furthermore, reciprocity-bearing mechanisms suffer an interior penalty where splitting the budget harms the pair more than concentrating it on one side (**F**).

## 5. Budget non-convexity and boundary conditions

Equal enforcement budgets are neither fungible nor additive (Fig. 4c,f). Along a line of
constant total information cost (0.20), every reciprocity-bearing mechanism reaches
its *lowest* total cooperation in the interior rather than at either end. Under IJMPQ
a budget of 0.20 yields 1.0–1.65 when loaded onto one population but 0.39 when split
as (0.06, 0.14) (Fig. 4f). Either corner leaves one population with an intact
apparatus, which is enough to hold the pair together; a split breaks both and pushes
neither over the threshold where machinery-free cooperation takes over. Partner choice
is monotone instead (Fig. 4c): because only the high-cooperation-cost population's
information cost bites, the best outcome sits at the corner that spares that
population. The non-convexity is therefore a property of reciprocity-bearing
mechanisms, not of the budget itself
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

When both cost axes differ, the cooperation-cost gap remains the default role
assigner. Across the full i₀ × i₁ square behind Figs. 4–5, partner choice assigns the
lower-cooperation-cost population as cooperator in 170/176 cells; IJMPQ inverts
locally only on the i₀ ≈ 0 strip (13 cells). That hitchhiking inversion is stronger
when cooperation costs are equal and only information cost differs (Fig. S11: IMP
dq = −0.461 at Cost0 = 0, Cost1 = 0.20) and is attenuated once the cooperation-cost
gap is present (IMP dq = −0.100 at the same information-cost point). The gap moves
every reciprocity-bearing mechanism toward the cheap-cooperation-cost population,
erasing the inversion outright for MP and MPQ
([per-population information cost](../journal/asymmetric_i0_i1.md),
[crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)).

Fig. 5 shows the near-zero-i₀ inversion regime narrowing. Each panel fixes the information cost on the
low-cooperation-cost population and sweeps the other. The inversion — the expensive
population's curve above the cheap one's — holds throughout when i₀ = 0 (Fig. 5a),
survives only past a threshold when i₀ = 0.02 (Fig. 5b), and is gone by i₀ = 0.04 and
0.1 (Fig. 5c,d). Crossing into the machinery-free state is a bistable threshold, not
a slope: just inside this regime, doubling a population's own information cost *raises*
its cooperation by 0.32 as it tips from a defector-heavy mixed state into near-
complete tax-free unconditional cooperation. Run-to-run variance marks the basin
boundary directly in the ±1 SD bands — wide below the threshold (SD ≈ 0.25; runs
split between two attractors) and collapsed above it (SD ≈ 0.009).
In the paired fitness panels (Fig. 5e–h), the same cooperation-fitness mismatch holds
in every column: the population with higher cooperation is the one with lower fitness,
even when the colour ordering switches as i₀ rises.
In this threshold regime, increasing population 1's own information cost can raise
population 0's fitness substantially even while population 1 becomes slightly less
fit, showing that one population can benefit from interacting with a partner that is
less able to sustain costly enforcement machinery.

**Figure 5: Role inversion requires near-zero information costs in the low-cost population.** Frequency of cooperators (**A–D**) and average fitness (**E–H**) under combined partner choice and indirect reciprocity in the prisoner's dilemma. Cooperation costs are fixed asymmetrically ($c_0 = 0.1$, orange; $c_1 = 0.2$, red). Each column holds the information cost of the low-cooperation-cost population ($i_0$) constant while sweeping $i_1$. **A, E**, $i_0 = 0$. **B, F**, $i_0 = 0.02$. **C, G**, $i_0 = 0.04$. **D, H**, $i_0 = 0.1$. The role inversion—where the expensive population cooperates more than the cheap one—survives only when $i_0$ is small. Shaded bands ($\pm 1$ SD over 30 runs) indicate a bistable threshold between mixed states and tax-free unconditional cooperation. In this regime, fitness remains decoupled from cooperation: the population that cooperates more earns less fitness.

The inversion appears only when the reciprocity family is present, not as a simple
effect of how much information cost a mechanism pays. Information cost is charged per family carried — one unit for partner
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

Snowdrift removes this regime entirely, identifying this cross-population burden as a property
of the dilemma rather than of the cost accounting
([crossed asymmetries](../journal/asymmetric_c1_i0_i1.md)). The dilemma-0 control
makes the same point for the decoupling claim (Fig. S8). Shuffle and group-size
panels locate which loci carry the baseline effects (Figs. S2, S3).
