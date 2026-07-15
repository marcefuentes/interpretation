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

**Snowdrift raises the floor.** Its high sucker payoff makes cooperation individually
favoured even without enforcement, so both the c-collapse and the information-cost
tax matter far less than in the PD.

## 2. Between-population asymmetry

With two populations, cooperation frequently breaks into a cooperator/exploiter role
split, and the cooperating side is typically the one that earns less — the paradox of
success. The two faces of the asymmetry (who cooperates, who profits) can diverge.

- **Symmetric payoffs split stochastically.** With two identical coevolving
  populations, partner choice breaks symmetry by chance: the cooperating side is
  exploited, and carrying the chooser allele correlates with fitness at roughly minus
  one ([partner choice calibration](../journal/prisoners_partner_choice.md)).
- **Asymmetric payoffs split deterministically.** When c0 < c1, the lower-cooperation-cost
  population has the larger cooperation advantage and takes the cooperator role in
  every cell — partner choice converts the R − P gap directly into a cooperation gap
  ([partner choice under cooperation-cost asymmetry](../journal/asymmetric_c0_c1_partner_choice.md),
  [synthesis](../journal/synthesis.md)).
- **Reward-led mechanisms suppress the split.** Combined mechanisms lift the exploited
  high-cooperation-cost population and shrink the asymmetry, because being reward-led
  they no longer route the R − P gap into a cooperation gap
  ([combined mechanisms](../journal/asymmetric_c0_c1_combined.md)).
- **Information cost compresses the split by collapsing both sides.** When one
  population's cooperation cost is fixed above zero and the other's is swept, information
  cost retreats the cooperation-cost ceiling and steadily shrinks both the cooperation
  gap and the fitness gap; the paradox of success remains while partner choice still
  functions, then disappears mainly because the system is driven to the control floor
  ([information cost under cooperation-cost asymmetry](../journal/asymmetric_c1_i.md)).
- **Information-cost asymmetry at symmetric cooperation cost.** When c0 = c1 but
  i0 < i1, partner choice assigns the cooperator role to the population with
  lower information cost, while IJMPQ inverts via cross-population hitchhiking — the
  high-information-cost side sheds its apparatus into tax-free unconditional
  cooperation ([per-population information cost](../journal/asymmetric_i0_i1.md)).
  Snowdrift largely removes this lock, so the pattern is PD-specific.
- **When both costs differ, the cooperation-cost gap dominates.** With c0 < c1 fixed
  and the full i0 × i1 square swept, partner choice assigns the
  lower-cooperation-cost population as cooperator in 170/176 cells; IJMPQ can invert
  locally only on the i0 ≈ 0 strip (13 cells), where hitchhiking survives but is
  attenuated relative to the symmetric-cooperation-cost case. Snowdrift removes the
  wedge entirely ([both costs asymmetric](../journal/asymmetric_c1_i0_i1.md)).

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
- **Cross-population hitchhiking under information-cost asymmetry.** At symmetric
  cooperation cost, IJMPQ can invert the role split: the population with higher
  information cost sheds active enforcement into tax-free unconditional carriers
  (C1P0) and cooperates more, while the population with lower information cost
  retains partial machinery but earns more — the same behaviour–mechanism decoupling
  route, now routed through between-population assortment
  ([per-population information cost](../journal/asymmetric_i0_i1.md),
  [both costs asymmetric](../journal/asymmetric_c1_i0_i1.md)). When both
  cooperation-cost and information-cost asymmetry are present, the hitchhiking wedge
  survives only where i0 ≈ 0; elsewhere the cooperation-cost gap reasserts control.
- **Partner choice assorts, reciprocity remembers.** A residual chooser minority sorts
  the whole population so even unconditional cooperators are protected; a residual
  reciprocator minority protects only itself. This population-level vs individual-level
  distinction is the same one the payoff-axis fits recover.
- **Free-riding and silent carriers.** Second-order free-riders (C1M0) ride on the
  punishment supplied by reciprocators, and silent carriers (C0P1) accumulate by
  mutation without expressing choice
  ([reciprocity](../journal/symmetric_c_reciprocity.md),
  [reciprocity under cooperation-cost asymmetry](../journal/asymmetric_c0_c1_reciprocity.md)).
