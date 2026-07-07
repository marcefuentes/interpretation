# Results

*Draft scaffold, organised by the three outcome variables of
[framework.md](../journal/framework.md). Numbers are cited to the journal doc that
derives and regression-checks them rather than restated in full.*

## 1. The level of cooperation and what limits it

Each mechanism sustains cooperation up to a cost threshold and then collapses. The
single cost axis of hamilton/mutualism cannot say *which* payoff gap drives a
collapse, because raising c simultaneously raises temptation (T − R), raises risk
(P − S), and shrinks the cooperation advantage (R − P). The prisoners and snowdrift
calibration sweeps decouple these, and the attribution is clean and stable
([synthesis.md](../journal/synthesis.md),
[prisoners_calibration.md](../journal/prisoners_calibration.md),
[snowdrift_calibration.md](../journal/snowdrift_calibration.md)):

- **Direct reciprocity (M) is risk-limited.** Its collapse as c rises is mostly the
  growing mutual-defection risk, not the shrinking R − P — confirmed from the other
  side by snowdrift, where the low sucker gap lets M sustain cooperation it cannot in
  the PD ([hamilton_reciprocity.md](../journal/hamilton_reciprocity.md)).
- **Partner choice (P) is limited by the cooperation advantage R − P.** It tracks
  R − P alone across the orthogonal sweep, which is why it fails at the chooser
  bottleneck as R − P → 0.
- **Combined and reputation-rich mechanisms (MP, MPQ, IMP, IJMPQ) are reward-limited**
  and largely blind to the defection baseline, which is why they hold cooperation to
  the highest costs.

**Information cost is a softer, orthogonal pressure**
([hamilton_cost.md](../journal/hamilton_cost.md)). Taxing the machinery alone (c = 0)
erodes cooperation only gently, because with no temptation a population can shed the
apparatus and keep cooperating for free. But because information cost thins the very
apparatus that resists temptation, it pulls the c-collapse threshold downward where
the two costs overlap — a price (Cost) that starves the defence a demand (c)
requires.

**Snowdrift raises the floor.** Its high sucker payoff makes cooperation individually
favoured even without enforcement, so both the c-collapse and the information-cost
tax matter far less than in the PD.

## 2. Between-population asymmetry

With two populations, cooperation frequently breaks into a cooperator/exploiter role
split, and the cooperating side is typically the one that earns less — the paradox of
success. The two faces of the asymmetry (who cooperates, who profits) can diverge.

- **Symmetric payoffs split stochastically.** In hamilton pop_2 (and the symmetric
  prisoners pop_2) two identical populations diverge by chance, the cooperating side
  exploited; carrying the chooser allele correlates with fitness at roughly minus one
  ([prisoners_partner_choice.md](../journal/prisoners_partner_choice.md)).
- **Asymmetric payoffs split deterministically.** In mutualism pop_2 the built-in
  c0 < c1 gives the lower-cost population the larger cooperation advantage, so it takes
  the cooperator role in every cell — partner choice converts the R − P gap directly
  into a cooperation gap ([mutualism_partner_choice.md](../journal/mutualism_partner_choice.md),
  [synthesis.md](../journal/synthesis.md)).
- **Reward-led mechanisms suppress the split.** Combined mechanisms lift the exploited
  high-cost population and shrink the asymmetry, because being reward-led they no
  longer route the R − P gap into a cooperation gap
  ([mutualism_combined.md](../journal/mutualism_combined.md)).
- **Information cost compresses the split by collapsing both sides.** On the
  asymmetric Cost x c1 sweep, taxing the machinery retreats the c1 ceiling and
  steadily shrinks both the cooperation gap and the fitness gap between the two
  populations; the paradox of success remains while partner choice still functions,
  then disappears mainly because the system is driven to the control floor
  ([mutualism_cost.md](../journal/mutualism_cost.md)).

The temporal regime of this split is an absorbing state (roles lock in), and it does
not differ between one and two populations; this is why temporal dynamics is not
treated as a separate outcome.

## 3. Genotype composition — the route to cooperation

The same cooperation level can be produced by different genotypes, and this is where
some of the strongest results sit ([hamilton_cost.md](../journal/hamilton_cost.md),
[synthesis.md](../journal/synthesis.md)).

- **Behaviour and machinery decouple under information cost.** As Cost rises at c = 0,
  the active enforcement alleles are selected out (chooser P1 and TFT M1 both fall to
  near zero) while cooperation is carried by tax-free unconditional cooperators (C1P0,
  C1M0). A dilemma-free control confirms the erosion is a supply-side effect of the
  tax; the dilemma only decides whether losing the machinery drags behaviour down.
- **The decoupling has a boundary.** On the asymmetric branch with c0 fixed at 0.10,
  machinery loss and behavioural loss move together much more tightly: there is no
  harmless pure-Cost edge, so shedding P1 or M1 no longer leaves a stable
  high-cooperation niche behind ([mutualism_cost.md](../journal/mutualism_cost.md)).
- **Partner choice assorts, reciprocity remembers.** A residual chooser minority sorts
  the whole population so even unconditional cooperators are protected; a residual
  reciprocator minority protects only itself. This population-level vs individual-level
  distinction is the same one the payoff-axis fits recover.
- **Free-riding and silent carriers.** Second-order free-riders (C1M0) ride on the
  punishment supplied by reciprocators, and silent carriers (C0P1) accumulate by
  mutation without expressing choice
  ([hamilton_reciprocity.md](../journal/hamilton_reciprocity.md),
  [mutualism_reciprocity.md](../journal/mutualism_reciprocity.md)).
