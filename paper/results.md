# Results

## 1. Mechanism cost thresholds

At equal cooperation cost in a single population, each mechanism sustains cooperation
up to a characteristic cost and then cooperation falls (Fig. S1). The no-enforcement
control (Fig. S1a) stays near zero across the prisoner's-dilemma range; direct
reciprocity (Fig. S1b), partner choice (Fig. S1c), and the combined mechanism that
includes lifetime reputation (Fig. S1d) raise that cost threshold in that order. The
same columns under snowdrift (Fig. S1e–h) sit higher: the elevated sucker payoff
already favors cooperation without enforcement, so the threshold ordering flattens
and the fall in cooperation as c rises matters less than in the PD.

A single cooperation-cost axis cannot say *which* payoff gap drives the fall in
cooperation, because raising c simultaneously raises temptation (T − R), raises risk
(P − S), and shrinks the cooperation advantage (R − P). Orthogonal payoff-plane
calibration analyses (Table S1) separate these gaps. Direct reciprocity (M) is
risk-limited: the fall in cooperation as c rises tracks the growing mutual-defection
risk rather than the shrinking R − P — confirmed from the other side in snowdrift,
where the low sucker gap lets M sustain cooperation it cannot in the PD. Partner
choice (P) is limited by the cooperation advantage R − P: it tracks R − P alone
across the orthogonal calibration, which is why it fails at the chooser bottleneck as
R − P → 0. Combined mechanisms and those that include lifetime reputation (MP, MPQ,
IMP, IJMPQ) are reward-limited and unaffected by the defection baseline, which is why
they hold cooperation to the highest costs (Fig. S1d).

These attributions recover a mechanistic distinction that matters again when
information cost is relational. A residual chooser minority sorts the whole
population, so even unconditional cooperators are protected; a residual reciprocator
minority protects only itself. Partner choice assorts at the population level;
reciprocity remembers at the individual level.
Short-memory and shuffle variants shift the direct-reciprocity ordering
relative to Fig. S1 but leave the partner-choice versus combined contrast intact
(Fig. S2).

## 2. The two-population role split

With two coevolving populations, one population often cooperates while the other
exploits it, and the more cooperative population earns less fitness. I distinguish
this **outcome** asymmetry (gaps in cooperation and fitness) from **parameter**
symmetry in the setup (whether c₀ = c₁, i₀ = i₁, and payoffs match). Mechanism can
override the default mapping.

When costs and payoffs match (c₀ = c₁, i₀ = i₁), partner-choice populations
**stochastically** split into cooperators and exploiters in the prisoner's dilemma —
a split that does not appear without enforcement (Fig. 1a–d). One population carries
cooperation and is exploited; carrying the chooser allele correlates with fitness at
roughly minus one. In snowdrift
populations already split without enforcement; partner choice then reshapes
high-cooperation-cost outcomes (Fig. 1e–h). Combined reputation mechanisms at the
same parameter point leave the two populations nearly matched in the PD.

**Figure 1: Outcome asymmetry under parameter-symmetric cooperation cost.** Frequency of cooperators and average fitness in two coevolving populations (light green indicates the population with the lower frequency of cooperators; dark green the other). **A–D**, Prisoner's dilemma. **E–H**, Snowdrift game. **A, E**, Baseline without enforcement mechanisms. **B, F**, Short-memory partner choice is the only available mechanism. Both populations pay identical cooperation costs ($c$, swept from 0 to the partner benefit $b$) and identical information costs ($0.001$). Under matched costs, partner choice generates a stochastic cooperator/exploiter role split in the prisoner's dilemma that is absent without enforcement. In the snowdrift game, the split already exists in the baseline and partner choice primarily extends it to higher costs.

When one population pays a slightly lower cooperation cost, that chance split becomes
deterministic. Along the strip c₁ = c₀ + 0.02, the lower-cooperation-cost population
cooperates in every cell under partner choice, and the R − P gap becomes a stable
cooperation gap (Fig. 2a,b). Under combined IJMPQ the expensive population
cooperates more and the outcome gap shrinks on the same axes (Fig. 2c,d), because
reward-led mechanisms no longer map R − P into a cooperation gap. Fig. 2 is
prisoner's-dilemma only: without enforcement the cheap population barely cooperates
in the PD (control mean ≈ 0.10), so partner choice is what lets populations lock the
parameter gap into a deterministic split (Fig. S3; full c₀ × c₁ grid in Fig. S4).
In snowdrift the sucker payoff already lets populations cooperate highly without
mechanism alleles (control ≈ 0.96 vs partner choice ≈ 0.96 for the cheap side), and
populations often diverge from payoffs alone (Fig. 1e–h). A parallel asymmetric snowdrift
panel would repeat that already-high cooperation rather than isolate what enforcement adds.
Fig. S5 contrasts the deterministic and stochastic strips on shared axes; the split
survives small-group stochasticity at group size 4 (Fig. S6).

**Figure 2: Deterministic role splits emerge from cooperation-cost asymmetries.** Frequency of cooperators and average fitness for two coevolving populations under the prisoner's dilemma, evaluated along the parameter strip $c_1 = c_0 + 0.02$ (with both populations overlaid). **A, B**, Short-memory partner choice alone. **C, D**, Combined partner choice and indirect reciprocity. Both populations pay identical information costs ($0.001$). A small cooperation-cost gap allows partner choice to convert the payoff asymmetry into a stable cooperator/exploiter assignment (**A, B**). The combined mechanism that includes lifetime reputation raises cooperation in the expensive population, shrinking the outcome asymmetry (**C, D**).

Single-run trajectories confirm that these roles are stable end states: cooperation
and fitness at t = 2^17 already match the final snapshot at t = 2^20, not slow
late declines. The temporal regime does not differ between one and two populations.

With this cooperation-cost baseline established, I next ask how populations respond
when they differ in information cost.

## 3. Costly enforcement alleles, and why symmetry hides the question

Making the enforcement alleles themselves costly introduces a pressure orthogonal to
cooperation cost. Raising the information cost alone reduces cooperation only
gently where temptation is absent, because a population can lose the alleles and keep
cooperating for free. Where the two costs overlap, information cost selects against
the mechanism alleles cooperation cost requires and lowers the cooperation-cost
threshold at which cooperation falls (Fig. S7).

At zero cooperation cost the genotype pattern makes that separation visible (Fig. 3).
As information cost rises, active enforcement alleles are selected out — chooser P1
(Fig. 3a) and TFT M1 (Fig. 3c) both fall toward zero — while cooperation remains high
on unconditional cooperators that pay no information cost (Fig. 3b,d: C1P0, C1M0).
Cooperation frequency and mechanism-allele frequency diverge. A dilemma-free control
shows that mechanism alleles decline with or without a social dilemma; cooperation
persists after those alleles are lost only when the dilemma is present, so the
information cost drives the allele loss and the dilemma decides whether losing the
alleles reduces cooperation (Fig. S8).

**Figure 3: Information cost separates cooperation from enforcement alleles when cooperation is free.** Frequency of the active enforcement allele (chooser P1 in **A**; tit-for-tat M1 in **C**) and overall frequency of cooperators (**B, D**) in a single population. **A, B**, Short-memory partner choice alone. **C, D**, Direct reciprocity alone. The cooperation cost is fixed at zero while the information cost is swept from 0 to the partner benefit ($b = 0.4$). Rising information cost selects against active enforcement alleles, but cooperation remains high because populations lose the costly alleles in favor of unconditional cooperation that pays no information cost.

That refuge disappears once cooperation cost is held above zero. Allele loss and
behavioral loss then move together: losing P1 or M1 no longer leaves a stable
high-cooperation outcome behind.
With a fixed cooperation-cost gap, as information cost rises populations cooperate less
and both the cooperation gap and the fitness gap shrink; the more cooperative
population remains less fit while partner choice still functions, then both fall to
the no-enforcement baseline (Fig. S9). Second-order free-riders (C1M0)
and carriers that never choose (C0P1) accumulate along the same paths.

A symmetric information-cost design cannot separate the cost a population pays from
the burden that cost places on its partner. Losing mechanism alleles while keeping
cooperation looks like a local solution — pay no information cost, keep cooperating —
but that reading is an artifact of applying the same information cost to both sides at
once. Holding one population's information cost at zero and varying the other's
breaks the confound.

## 4. Information cost is relational

Figs. 4–5 cross a fixed cooperation-cost gap (c₀ = 0.1, c₁ = 0.2) with independent
per-population information costs. The first two columns of Fig. 4 hold one
population's information cost at zero and sweep the other's, so I can see which
population's cost places the larger burden on its partner.

Under partner choice the two strip columns show opposite patterns (Fig. 4a,b). When the
low-cooperation-cost population pays i = 0.20 it barely changes (0.602 → 0.585)
and its partner even rises (0.189 → 0.268). When the high-cooperation-cost population
pays the same information cost, both fall to low cooperation (0.069 and 0.032). Under
partner choice a population barely bears a burden from its own information cost and
cooperates much less under the burden of its partner's. The bilateral swap rule is
why: a chooser is useless without a chooser to trade with, so assortment is limited by
whichever population has fewest choosers to spare — and that is already the high-cost
side before any information cost is applied.

Under the combined mechanism that includes lifetime reputation the pattern reverses
(Fig. 4d,e). When the low-cooperation-cost population pays i = 0.20 its partner falls
from 0.957 to 0.268 while the payer itself falls only to 0.734 — the partner bears a
larger burden than the payer. When the high-cost side pays instead, that side stays
near 0.911. Reciprocity-bearing mechanisms protect only their carriers: a population
that pays information cost can switch to unconditional cooperation, which is harmless
when that side contributes little cooperation and destructive when it carries most of
it. Here the partner bears a larger burden when the *low*-cooperation-cost population
pays the information cost — the opposite of partner choice.

Genotype composition confirms that a partner's cost can leave an allele unused in a
population that pays no information cost. At (i₀, i₁) = (0, 0.20) that population's
chooser frequency sits at its neutral value (P1 = 0.519; inert Q1 = 0.498,
M1 = 0.504), yet little of it is expressed (C1P1 = 0.044, against 0.187 in the same
population when it pays the 0.20 information cost itself). With the partner's choosers
selected out there is nobody to swap with; the population falls to defection and the
allele survives only in defector carriers that never choose.

The fitness counterpart to these relational slices shows similar cross-population
burdens and interior penalties when total information cost is held fixed (Fig. S10).

The pattern that let a population keep cooperating under information cost under
symmetry (Fig. 3) is what places a burden on its partner under asymmetry: losing
mechanism alleles relieves the payer and removes the assortment or conditional help
the partner needed.

**Figure 4: The relational burden of information cost.** Frequency of cooperators in two coevolving populations under the prisoner's dilemma. One population (orange) has a lower cooperation cost ($c_0 = 0.1$) than the other (red; $c_1 = 0.2$). **A–C**, Short-memory partner choice alone. **D–F**, Combined partner choice and indirect reciprocity. **A, D**, Information cost is applied only to the low-cooperation-cost population ($i_1 = 0$; $i_0$ swept). **B, E**, Information cost is applied only to the high-cooperation-cost population ($i_0 = 0$; $i_1$ swept). **C, F**, The total information cost is fixed at $i_0 + i_1 = 0.2$ while the distribution between populations varies. Under partner choice (**A, B**), populations are robust to their own information costs but cooperate much less under their partner's. Under the combined reputation mechanism (**D, E**), this relationship reverses: raising information cost on the low-cost population reduces cooperation more in its high-cost partner than in the payer. Reciprocity-bearing mechanisms also suffer an interior penalty where splitting the total harms the pair more than concentrating it on one side (**F**).

## 5. Non-additivity of shared information cost and boundary conditions

Equal information-cost totals are neither interchangeable nor additive (Fig. 4c,f).
Along a line of constant total information cost (0.20), every reciprocity-bearing
mechanism reaches its *lowest* total cooperation in the interior rather than at either
end. Under IJMPQ populations that place a total of 0.20 on one side reach 1.0–1.65
total cooperation, but only 0.39 when they split it as (0.06, 0.14) (Fig. 4f). Either
corner leaves one population still carrying mechanism alleles, which is enough to
sustain cooperation in both; a split reduces both and leaves neither past the
threshold where cooperation without mechanism alleles takes over. Partner choice is
monotone instead (Fig. 4c): because only the high-cooperation-cost population's
information cost matters, the best outcome sits at the corner that spares that
population. The non-convexity is therefore a property of reciprocity-bearing
mechanisms, not of the total itself.

When both cost axes differ, populations still follow the cooperation-cost gap.
Across the full i₀ × i₁ square behind Figs. 4–5, under partner choice the
lower-cooperation-cost population cooperates in 170/176 cells; under IJMPQ they invert
locally only on the i₀ ≈ 0 strip (13 cells). That role inversion is stronger
when populations differ only in information cost (Fig. S11: under IMP, the
cooperation gap reaches −0.461 when i₀ = 0 and i₁ = 0.20) and weaker once a
cooperation-cost gap is present (cooperation gap −0.100 at the same
information-cost point). The gap moves
every reciprocity-bearing mechanism toward the cheap-cooperation-cost population,
erasing the inversion outright for MP and MPQ.

Fig. 5 shows the near-zero-i₀ inversion regime narrowing. Each panel fixes the information cost on the
low-cooperation-cost population and sweeps the other. The inversion — the expensive
population's curve above the cheap one's — holds throughout when i₀ = 0 (Fig. 5a),
survives only past a threshold when i₀ = 0.02 (Fig. 5b), and is gone by i₀ = 0.04 and
0.1 (Fig. 5c,d). Crossing into the state without mechanism alleles is a bistable
threshold, not a slope: just inside this regime, doubling a population's own
information cost *raises* its cooperation by 0.32 as it tips from a defector-heavy
mixed state into near-complete unconditional cooperation that pays no information
cost. Run-to-run variance marks the boundary between outcomes directly in the ±1 SD
bands — wide below the threshold (SD ≈ 0.25; runs diverge to different outcomes) and
narrow above it (SD ≈ 0.009).
In the paired fitness panels (Fig. 5e–h), the same cooperation-fitness mismatch holds
in every column: the population with higher cooperation is the one with lower fitness,
even when the color ordering switches as i₀ rises.
In this threshold regime, increasing population 1's own information cost can confer
a fitness benefit on population 0 even while population 1 becomes slightly less fit,
showing that one population can benefit from a partner that pays more for enforcement
alleles.

**Figure 5: Role inversion requires near-zero information costs in the low-cost population.** Frequency of cooperators (**A–D**) and average fitness (**E–H**) under combined partner choice and indirect reciprocity in the prisoner's dilemma. Cooperation costs are fixed asymmetrically ($c_0 = 0.1$, orange; $c_1 = 0.2$, red). Each column holds the information cost of the low-cooperation-cost population ($i_0$) constant while sweeping $i_1$. **A, E**, $i_0 = 0$. **B, F**, $i_0 = 0.02$. **C, G**, $i_0 = 0.04$. **D, H**, $i_0 = 0.1$. The role inversion—where the expensive population cooperates more than the cheap one—survives only when $i_0$ is small. Shaded bands ($\pm 1$ SD over 30 runs) indicate a bistable threshold between mixed states and unconditional cooperation that pays no information cost. In this regime, fitness remains separated from cooperation: the population that cooperates more earns less fitness.

The inversion appears only when the reciprocity family is present, not as a simple
effect of how much information cost a mechanism pays. Information cost is incurred
per family carried — one unit for partner choice, one for reciprocity — so a
mechanism pays 0, 1 or 2 units however many loci it enables. At one unit, direct
reciprocity and partner choice pay identically, yet reciprocity inverts in 10 cells of
the i₀ ≈ 0 strip and partner choice in none. At two units, the four combined
mechanisms pay identically, yet invert in 3, 1, 13 and 13 cells. Every mechanism
carrying the reciprocity family inverts somewhere in that strip; no mechanism lacking
it does. Reciprocity supplies the second-order-free-rider outcome that unconditional
cooperation occupies once active alleles become unaffordable. Partner choice does lose
the lead in three cells, but in the opposite corner of the square and by the opposite
route: a transient crossing while its *own* alleles fall.

Snowdrift removes this regime entirely, identifying this cross-population burden as a
property of the dilemma rather than of the cost accounting. The dilemma-free control
makes the same point for the claim that cooperation can persist after mechanism
alleles are lost (Fig. S8). Shuffled partnerships and group size 4 are reported in
Figs. S2 and S6.
