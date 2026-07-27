# Results

*Draft scaffold, organised by the three outcome variables of
[framework.md](../journal/framework.md). Numbers are cited to the journal doc that
derives and regression-checks them rather than restated in full.*

## 1. The level of cooperation and what limits it

Each mechanism sustains cooperation up to a cost threshold and then collapses. A
single cooperation-cost axis cannot say *which* payoff gap drives a collapse, because
raising c simultaneously raises temptation (T − R), raises risk (P − S), and shrinks
the cooperation advantage (R − P). Orthogonal payoff-plane calibration sweeps
decouple these, and the attribution is clean and stable
([synthesis](../journal/synthesis.md),
[PD calibration](../journal/prisoners_calibration.md),
[snowdrift calibration](../journal/snowdrift_calibration.md)):

- **Direct reciprocity (M) is risk-limited.** Its collapse as c rises is mostly the
  growing mutual-defection risk, not the shrinking R − P — confirmed from the other
  side in snowdrift, where the low sucker gap lets M sustain cooperation it cannot in
  the PD ([direct reciprocity](../journal/symmetric_c_reciprocity.md)).
- **Partner choice (P) is limited by the cooperation advantage R − P.** It tracks
  R − P alone across the orthogonal sweep, which is why it fails at the chooser
  bottleneck as R − P → 0.
- **Combined and reputation-rich mechanisms (MP, MPQ, IMP, IJMPQ) are reward-limited**
  and largely blind to the defection baseline, which is why they hold cooperation to
  the highest costs.

**Information cost is a softer, orthogonal pressure**
([information cost at equal cooperation cost](../journal/symmetric_c_i.md)). Taxing
the machinery alone (c = 0) erodes cooperation only gently, because with no temptation
a population can shed the apparatus and keep cooperating for free. But because
information cost thins the very apparatus that resists temptation, it pulls the
c-collapse threshold downward where the two costs overlap — information cost starves
the defence cooperation cost requires.

**Which population pays matters more than how much is paid — and the mechanisms
disagree about which one.** With two populations paying independent information costs,
each mechanism turns out to be governed by *one* of the two costs, for both populations
at once, but partner choice and the reciprocity-bearing mechanisms pick opposite axes
([both costs asymmetric](../journal/asymmetric_c1_i0_i1.md)). Partner choice is bound by
the cost paid by the *high*-cooperation-cost population: taxing the low-cost side to
i = 0.20 leaves it at 0.585 and even lifts its partner, while moving the same tax onto
the high-cost side collapses both to 0.069 and 0.032. The reason is the bilateral swap
rule — a chooser is useless without a chooser to trade with — so assortment is rationed
by whichever population has fewest choosers to spare, and that is the high-cost side
before any tax is applied. The reciprocity-bearing mechanisms are bound by the opposite
cost, the one paid by the *low*-cooperation-cost population, because a taxed population
can always shed its machinery into unconditional cooperation: harmless when the taxed
side contributes little cooperation, destructive when it is the side carrying most of
it.

**A shared information-cost budget is worse than a concentrated one.** Along lines of
constant total information cost, every mechanism carrying the reciprocity locus reaches
its *lowest* total cooperation in the interior rather than at either end: under IJMPQ a
budget of 0.20 yields 1.0–1.65 loaded onto one population but 0.39 split as
(0.06, 0.14). Either corner leaves one population with an intact apparatus, which is
enough to hold the pair together; a split budget breaks both and pushes neither over the
threshold where machinery-free cooperation takes over. Partner choice is the exception:
because only the high-cooperation-cost population's information cost bites, its
iso-budget line is monotone and the best outcome sits at the corner that spares that
population.

**Snowdrift raises the floor.** Its high sucker payoff makes cooperation individually
favoured even without enforcement, so both the c-collapse and the information-cost
tax matter far less than in the PD.

## 2. Between-population asymmetry

With two populations, cooperation frequently breaks into a cooperator/exploiter role
split, and the cooperating side is typically the one that earns less — the paradox of
success. The two faces of the asymmetry (who cooperates, who profits) can diverge.

We measure this as an **outcome** (cooperation and fitness gaps between populations),
separate from **parameter** symmetry in the setup (whether c0 = c1, i0 = i1, and
payoffs match). The bullets below pair parameter conditions with the outcome pattern
they typically produce; mechanism can override the default mapping.

- **Parameter-symmetric cooperation cost → outcome split (game- and mechanism-dependent).**
  With c0 = c1 and i0 = i1, two coevolving populations under partner choice show a
  **stochastic** cooperator/exploiter assignment in the prisoner's dilemma: one side
  carries cooperation, is exploited, and carrying the chooser allele correlates with
  fitness at roughly minus one — a pattern absent under the no-machinery control
  (Fig. 2 control columns versus partner choice;
  [partner choice calibration](../journal/prisoners_partner_choice.md)). In snowdrift,
  a similar split already appears without enforcement machinery; partner choice mainly
  reshapes high-cooperation-cost outcomes. Combined reputation mechanisms at the same
  parameter point stay nearly outcome-symmetric in the PD.
- **Cooperation-cost parameter asymmetry → deterministic outcome (P, PD).** When c0 < c1,
  the lower-cooperation-cost population has the larger cooperation advantage and takes
  the cooperator role in every cell — partner choice converts the R − P gap directly
  into a cooperation gap (Fig. 3;
  [partner choice under cooperation-cost asymmetry](../journal/asymmetric_c0_c1_partner_choice.md),
  [synthesis](../journal/synthesis.md)). Fig. 3 is prisoner's-dilemma only because that
  is where the attribution is clean: under no enforcement the cheap population barely
  cooperates (control mean qBSeen ≈ 0.10), so the full c0 × c1 heatmap shows partner
  choice *creating* a deterministic cooperator/exploiter split from the parameter gap.
  In snowdrift the sucker payoff already sustains high cooperation without machinery
  (control ≈ 0.96 vs partner choice ≈ 0.96 for the cheap side), and outcome asymmetry
  often appears from payoffs alone (Fig. 2 snowdrift row; Fig. S1). A parallel
  asymmetric snowdrift panel would largely repeat that payoff-floor story rather than
  isolate what enforcement adds; the snowdrift between-population pattern is covered in
  those figures and in the journal asymmetric analyses.
- **Reward-led mechanisms suppress the split.** Combined mechanisms lift the exploited
  high-cooperation-cost population and shrink the outcome asymmetry, because being
  reward-led they no longer route the R − P gap into a cooperation gap
  ([combined mechanisms](../journal/asymmetric_c0_c1_combined.md)).
- **Information cost compresses the split by collapsing both sides.** When one
  population's cooperation cost is fixed above zero and the other's is swept, information
  cost retreats the cooperation-cost ceiling and steadily shrinks both the cooperation
  gap and the fitness gap; the paradox of success remains while partner choice still
  functions, then disappears mainly because the system is driven to the control floor
  ([information cost under cooperation-cost asymmetry](../journal/asymmetric_c1_i.md)).
- **Information-cost parameter asymmetry at equal cooperation cost → deterministic
  outcome.** When c0 = c1 but i0 < i1, partner choice assigns the cooperator role to
  the population with lower information cost — not a chance split, despite
  parameter-symmetric cooperation cost. IJMPQ inverts via cross-population hitchhiking:
  the high-information-cost side sheds its apparatus into tax-free unconditional
  cooperation ([per-population information cost](../journal/asymmetric_i0_i1.md)).
  Snowdrift largely removes this lock, so the pattern is PD-specific.
- **When both cost axes differ parameter-asymmetrically, cooperation cost dominates
  the outcome.** With c0 < c1 fixed and the full i0 × i1 square swept, partner choice
  assigns the lower-cooperation-cost population as cooperator in 170/176 cells; IJMPQ
  can invert locally only on the i0 ≈ 0 strip (13 cells), where hitchhiking survives
  but is attenuated relative to the c0 = c1, i0 ≠ i1 case (IMP dq = −0.100 vs −0.461 at
  Cost0 = 0, Cost1 = 0.20). Differencing the two studies at shared information-cost
  points shows the cooperation-cost gap moving every reciprocity-bearing mechanism
  toward the cheap-cooperation-cost population, by enough to erase the inversion
  outright for MP and MPQ. Snowdrift removes the wedge entirely
  ([both costs asymmetric](../journal/asymmetric_c1_i0_i1.md)).
- **The inversion is gated by the reciprocity family, not by the information cost the
  mechanism pays.** Information cost is charged per family carried — one unit for
  partner choice, one for reciprocity — so a mechanism owes 0, 1 or 2 units however many
  loci it enables. That makes the comparison controlled in both directions. At one unit,
  direct reciprocity and partner choice pay identically, yet reciprocity inverts in 10
  cells of the i0 ≈ 0 strip and partner choice in none. At two units, the four combined
  mechanisms pay identically, yet invert in 3, 1, 13 and 13 cells. Across the crossed
  square every mechanism carrying the reciprocity family inverts somewhere in that strip
  and no mechanism lacking it does. Reciprocity supplies
  the second-order-free-rider niche that unconditional cooperation occupies once active
  machinery becomes unaffordable, and the inversion runs through that niche. Partner
  choice does lose the lead in 3 cells, but in the opposite corner of the square and by
  the opposite route: a transient crossing while its *own* machinery collapses
  ([both costs asymmetric](../journal/asymmetric_c1_i0_i1.md)).

Single-run movies across the information-cost sweeps confirm that these splits are
absorbing states established by the first recorded snapshot (t = 131072), not slow
late erosions ([journal temporal analyses](../journal/asymmetric_c1_i0_i1.md)). The
temporal regime does not differ between one and two populations; this is why temporal
dynamics is not treated as a separate outcome variable.

## 3. Genotype composition — the route to cooperation

The same cooperation level can be produced by different genotypes, and this is where
some of the strongest results sit
([information cost at equal cooperation cost](../journal/symmetric_c_i.md),
[synthesis](../journal/synthesis.md)).

- **Behaviour and machinery decouple under information cost.** As information cost
  rises at c = 0, the active enforcement alleles are selected out (chooser P1 and TFT
  M1 both fall to near zero) while cooperation is carried by tax-free unconditional
  cooperators (C1P0, C1M0). A dilemma-free control confirms the erosion is driven by
  the information-cost tax itself; the dilemma only decides whether losing the
  machinery drags behaviour down.
- **The decoupling has a boundary.** When one population's cooperation cost is fixed
  above zero, machinery loss and behavioural loss move together much more tightly:
  there is no refuge at zero cooperation cost, so shedding P1 or M1 no longer leaves
  a stable high-cooperation niche behind
  ([information cost under cooperation-cost asymmetry](../journal/asymmetric_c1_i.md)).
- **Cross-population hitchhiking under information-cost asymmetry.** At c0 = c1
  (parameter-symmetric cooperation cost), IJMPQ can invert the outcome split: the
  population with higher information cost sheds active enforcement into tax-free
  unconditional carriers (C1P0) and cooperates more, while the population with lower
  information cost retains partial machinery but earns more — the same
  behaviour–mechanism decoupling route, now routed through between-population assortment
  ([per-population information cost](../journal/asymmetric_i0_i1.md),
  [both costs asymmetric](../journal/asymmetric_c1_i0_i1.md)). When both
  cooperation-cost and information-cost parameters are asymmetric, the hitchhiking wedge
  survives only where i0 ≈ 0; elsewhere the cooperation-cost gap reasserts control in
  the outcome.
- **An allele can be present at full frequency and still be silent.** The clearest
  genotype evidence that partner choice is limited by the *partner's* information cost
  is a population that pays nothing yet loses its choosers. At (i0, i1) = (0, 0.20) the
  untaxed population's chooser allele sits at its neutral frequency, as it must with no
  tax selecting against it (P1 = 0.519, alongside inert Q1 = 0.498 and M1 = 0.504), but
  almost none of it is expressed: C1P1 = 0.044, against 0.187 in the same population
  when it is the one carrying a 0.20 tax. With the partner's choosers taxed away there
  is nobody to swap with, the population collapses to defection, and the allele survives
  only in silent defector carriers ([both costs
  asymmetric](../journal/asymmetric_c1_i0_i1.md)).
- **Crossing into the machinery-free state is a threshold, not a slope.** Just inside
  the wedge, doubling a population's own information cost *raises* its cooperation by
  0.32 as it tips from a defector-heavy mixed state into near-complete tax-free
  unconditional cooperation. Run-to-run variance identifies the transition as a basin
  boundary: below it the 30-run standard deviation reaches 0.25 (runs split between two
  attractors), above it 0.009 (every run locks into the same state).
- **Partner choice assorts, reciprocity remembers.** A residual chooser minority sorts
  the whole population so even unconditional cooperators are protected; a residual
  reciprocator minority protects only itself. This population-level vs individual-level
  distinction is the same one the payoff-axis fits recover.
- **Free-riding and silent carriers.** Second-order free-riders (C1M0) ride on the
  punishment supplied by reciprocators, and silent carriers (C0P1) accumulate by
  mutation without expressing choice
  ([reciprocity](../journal/symmetric_c_reciprocity.md),
  [reciprocity under cooperation-cost asymmetry](../journal/asymmetric_c0_c1_reciprocity.md)).
