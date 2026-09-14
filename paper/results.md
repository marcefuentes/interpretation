# Results

I first compare mechanisms under equal cooperation cost in one population, then in
two. I next raise information cost when both populations pay alike, then let them
differ in who pays that cost, and finally vary both information costs together.

## 1. Equal cooperation cost in one population

I start with equal cooperation cost in a single population (Fig. S1). In the
prisoner's dilemma, cooperation stays near zero irrespective of cost in the
no-enforcement control (Fig. S1a). Cooperation collapses at successively higher
costs under direct reciprocity M (Fig. S1b), short-memory partner choice P
(Fig. S1c), and the combined mechanism IJMPQ (Fig. S1d), in that order.

Raising c decreases R and S and leaves T and P unchanged (Table 1), so a single
cooperation-cost sweep cannot say which payoff drives the fall in cooperation. I
run a separate set of simulations that vary those payoffs independently
(Table S1). A mechanism is risk-limited if its cooperation tracks P − S across
those sweeps, and reward-limited if it tracks the mutual-cooperation payoff R
rather than the other payoffs. In the prisoner's dilemma, P > S, so mimicking a
defector is the safe reply (it earns P instead of S). Direct reciprocity (M) is
risk-limited: the fall in cooperation as c rises tracks the growing
mutual-defection risk rather than the shrinking R − P. In snowdrift, S > P, so
there is no risk and mimicking a defector is costly (it earns the worst payoff P
instead of S). The same columns (Fig. S1e–h) show more cooperation without
enforcement — unconditional cooperators keep cooperating while reciprocity alleles
are selected against — and the ordering among mechanisms flattens. Partner choice
(P) is limited by the cooperation advantage R − P in both games: it tracks R − P
alone across those independent sweeps, which is why it fails as R − P → 0. The
combined mechanisms MP, MPQ, IMP, and IJMPQ are reward-limited and do not track
the mutual-defection payoff P, which is why they sustain cooperation to the
highest costs (Fig. S1d). Fig. S2 repeats the cost sweep under shuffled
partnerships for M, MP, IM, and IMP: shuffle collapses direct reciprocity, while
short-memory indirect reciprocity and the partner-choice combinations still
sustain cooperation farther. Partner choice alone is nearly unchanged by shuffle,
so that panel is omitted.

## 2. Equal and unequal cooperation cost in two populations

Two coevolving populations often settle into a cooperator role and an exploiter
role, and the population that cooperates more earns less fitness. Which mechanism
they carry decides whether those roles appear; the game decides whether they need
a mechanism at all.

At matched costs (c₀ = c₁, i₀ = i₁) the two games start from opposite baselines.
Without enforcement, prisoner's-dilemma populations both stay near defection and
take no roles (Fig. 1a,c), whereas snowdrift populations split **stochastically**
on the payoffs alone, because S > P leaves no risk in cooperating with a defector
(Fig. 1e,g).
Partner choice splits the prisoner's-dilemma populations the same way: one
cooperates more and is exploited, and the cooperation gap and the fitness gap
correlate at −0.98, so the population that cooperates more earns less (Fig. 1b,d).
In snowdrift, partner choice extends the payoff-driven split to higher cooperation
costs (Fig. 1f,h). Direct reciprocity (M) and IJMPQ leave the two
prisoner's-dilemma populations cooperating at similar frequencies, with no
cooperator/exploiter split: each side cooperates only as much as its partner does
(Fig. S1j,l). In snowdrift, direct reciprocity holds both populations near 0.92
while c ≤ 0.08, where the payoffs alone already split them; above that cost one
population falls behind and the split returns, narrower than without enforcement
(Fig. S1n). IJMPQ holds both populations near 0.96 across the whole cost sweep
(Fig. S1p). Fig. S1 sweeps all four mechanisms in both designs, one population
(Fig. S1a–h) above two (Fig. S1i–p).

**Figure 1: Outcome asymmetry under parameter-symmetric cooperation cost.** Frequency of cooperators and average fitness in two coevolving populations (light green indicates the population with the lower frequency of cooperators; dark green the other). **A–D**, Prisoner's dilemma. **E–H**, Snowdrift game. **A, E**, Frequency of cooperators without enforcement (_). **B, F**, Frequency of cooperators under short-memory partner choice (P). **C, G**, Fitness without enforcement. **D, H**, Fitness under partner choice. Both populations pay identical cooperation costs ($c$, swept from 0 to the partner benefit $b$) and identical information costs ($0.001$). Under matched costs, partner choice generates a stochastic cooperator/exploiter role split in the prisoner's dilemma that is absent without enforcement. In the snowdrift game, the split already exists in the baseline and partner choice primarily extends it to higher costs.

A cooperation-cost gap (c₀ < c₁) makes the role assignment deterministic, again
only where the game leaves it open. Without enforcement, the cheap
prisoner's-dilemma population averages 0.10 cooperation across the c₀ × c₁ grid
and the expensive one 0.03, so the gap alone assigns no roles (Fig. S3), while
snowdrift populations again split on the payoffs (0.96 for the cheap side, 0.09
for the expensive one). Under partner choice the cheap prisoner's-dilemma
population cooperates more in all 210 cells of that grid and earns less fitness in
all of them (cooperation and fitness gaps correlate at −0.99). Fig. 2 follows the
smallest gap in the grid, the strip c₁ = c₀ + 0.02 (Fig. 2a,b). Under M and IJMPQ
on that strip, both populations cooperate at similar frequencies and their fitness
differs only by the 0.02 cost gap (Fig. 2c,d). In snowdrift the mechanisms differ
in how far they close the payoff-driven split: partner choice leaves it nearly
unchanged (0.96 and 0.10), direct reciprocity lifts the expensive population to
0.19, and IJMPQ to 0.61.

The full c₀ × c₁ grid is in Fig. S4, Fig. S5 places the small cost-gap strip
beside the matched-cost sweep on shared axes, and the deterministic split holds at
group size 4 (Fig. S6).

**Figure 2: Deterministic role splits emerge from cooperation-cost asymmetries.** Frequency of cooperators and average fitness for two coevolving populations under the prisoner's dilemma, evaluated along the parameter strip $c_1 = c_0 + 0.02$ (with both populations overlaid). **A, B**, Short-memory partner choice (P). **C, D**, Combined mechanism IJMPQ. Both populations pay identical information costs ($0.001$). A small cooperation-cost gap allows partner choice to convert the cooperation-cost asymmetry into a stable cooperator/exploiter assignment (**A, B**); the more cooperative population earns less. Under IJMPQ both populations cooperate at similar frequencies and earn similar fitness aside from the 0.02 cost gap (**C, D**). In snowdrift the cost gap already splits populations without enforcement, so Fig. 2 is prisoner's-dilemma only.

## 3. Matched information cost

Making the enforcement alleles themselves costly adds a second cost, separate from
cooperation cost. Raising the information cost alone reduces cooperation only
gently where temptation is absent (c = 0, so T = R), because a population can lose the
alleles and keep cooperating for free. Where both costs are positive at once,
information cost selects against the mechanism alleles cooperation cost requires and
lowers the cooperation-cost threshold at which cooperation falls (Fig. S7).

At zero cooperation cost the genotype pattern makes that separation visible (Fig. 3).
As information cost rises, active enforcement alleles are selected out — chooser P1
(Fig. 3a) and tit-for-tat M1 (Fig. 3c) both fall toward zero — while cooperation
remains high on unconditional cooperators that pay no information cost (Fig. 3b,d:
C1P0, C1M0). Cooperation frequency and mechanism-allele frequency diverge. A control
game shows that mechanism alleles decline with or without a social dilemma;
cooperation persists after those alleles are lost only when the dilemma is present, so
the information cost drives the allele loss and the dilemma decides whether losing the
alleles reduces cooperation (Fig. S8).

**Figure 3: Information cost separates cooperation from enforcement alleles when cooperation is free.** Frequency of the active enforcement allele (chooser P1 in **A**; tit-for-tat M1 in **C**) and overall frequency of cooperators (**B, D**) in a single population. **A, B**, Short-memory partner choice (P). **C, D**, Direct reciprocity (M). The cooperation cost is fixed at zero while the information cost is swept from 0 to the partner benefit ($b = 0.4$). Rising information cost selects against active enforcement alleles, but cooperation remains high because populations lose the costly alleles in favor of unconditional cooperation that pays no information cost.

That cost-free high-cooperation outcome is stable only at c = 0. It disappears once
cooperation cost is held above zero. Allele loss and behavioral loss then move
together: losing P1 or M1 no longer leaves a stable high-cooperation outcome behind.
With a fixed cooperation-cost gap, as information cost rises populations cooperate less
and both the cooperation gap and the fitness gap shrink; the more cooperative
population remains less fit while partner choice still functions, then both fall to
the no-enforcement baseline (Fig. S9). Second-order free-riders — cooperators that pay
no information cost for enforcement (C1M0) — and carriers that never choose (C0P1)
accumulate as those alleles are lost.

A symmetric information-cost design cannot separate the cost a population pays from
the burden that cost places on its partner. Losing mechanism alleles while keeping
cooperation looks like a local solution — pay no information cost, keep cooperating —
but that reading is an artifact of applying the same information cost to both sides at
once. Holding one population's information cost at zero and varying the other's
breaks the confound.

## 4. Independent per-population information costs

Under partner choice, with a fixed cooperation-cost gap (c₀ = 0.1, c₁ = 0.2) and
independent per-population information costs, a population barely bears a burden from
its own information cost and cooperates much less under the burden of its partner's
(Fig. 4a,b). Figs. 4–5 cross that cooperation-cost gap with those information costs;
mechanisms are rows and designs are columns. The first two columns of Fig. 4 hold one
population's information cost at zero and sweep the other's, so each column shows
which population's cost places the larger burden on its partner. The third column
holds the total information cost fixed while the split varies.

When the low-cooperation-cost population's information cost rises from i = 0 to
i = 0.20, its frequency of cooperators barely changes (0.602 → 0.585) and its
partner's even rises (0.189 → 0.268). When the high-cooperation-cost population pays
the same rise in information cost, both fall to low cooperation (0.069 in the payer;
0.032 in its partner). The bilateral swap rule is why: a chooser is useless without
a chooser to trade with, so assortment is limited by whichever population has fewest
choosers — and that is already the high-cost side before any information cost is
applied.

Under IJMPQ the pattern reverses (Fig. 4d,e). When the low-cooperation-cost
population's information cost rises from i = 0 to i = 0.20, its partner's frequency of
cooperators falls from 0.957 to 0.268 while the payer itself falls only to 0.734 — the
partner bears a larger burden than the payer. When the high-cost side pays that rise
instead, that side's frequency of cooperators stays near 0.911 (and its partner remains
high). Reciprocity-bearing mechanisms — any mechanism carrying an I, J, or M locus —
protect only their carriers: a population that pays information cost can switch to
unconditional cooperation, which is harmless when that side contributes little
cooperation and destructive when it carries most of it. Here the partner bears a
larger burden when the *low*-cooperation-cost population pays the information cost —
the opposite of partner choice.

Genotype composition confirms the same point: a partner's cost can leave an allele
common yet unused in a population that pays no information cost. At
(i₀, i₁) = (0, 0.20) that population's P1 frequency sits at its mutation-drift value
(P1 = 0.519; inert Q1 = 0.498, M1 = 0.504) because the allele is not expressed and
therefore not under selection, yet little of it is expressed (C1P1 = 0.044, against
0.187 in the same population when it pays the 0.20 information cost itself). With the
partner's choosers selected out there is nobody to swap with; the population falls to
defection and the allele survives only in defector carriers that never choose. Partner
choice therefore assorts at the population level — a residual chooser minority can
still sort both sides — while reciprocity protects only its carriers.

The same total information cost does not yield the same cooperation: equal totals are
neither interchangeable nor additive (Fig. 4c,f). Along a line of constant total
information cost (0.20), every reciprocity-bearing mechanism reaches its *lowest*
total cooperation — the sum of the two populations' frequencies of cooperators, on a
0–2 scale — when the total is split between populations rather than paid by one side
alone. Under IJMPQ populations that place a total of 0.20 on one side reach 1.0–1.65
total cooperation, but only 0.39 when they split it as (0.06, 0.14) (Fig. 4f). Either
end leaves one population still carrying mechanism alleles, which is enough to
sustain cooperation in both; a split reduces both populations' mechanism alleles so
that neither remains above the threshold at which cooperation without those alleles
takes over. Partner choice does not show that interior minimum (Fig. 4c): because
only the high-cooperation-cost population's information cost matters, total
cooperation is highest when that population pays none of the total. That
non-additivity is therefore a property of reciprocity-bearing mechanisms, not of the
total itself. The fitness counterpart of these slices shows the same cross-population
burdens and the same interior minimum under a fixed total (Fig. S10).

The pattern that let a population keep cooperating under information cost under
symmetry (Fig. 3) is what places a burden on its partner under asymmetry: losing
mechanism alleles relieves the payer and removes the assortment or conditional help
the partner needed.

**Figure 4: The relational burden of information cost.** Frequency of cooperators in two coevolving populations under the prisoner's dilemma. One population (orange) has a lower cooperation cost ($c_0 = 0.1$) than the other (red; $c_1 = 0.2$). **A–C**, Short-memory partner choice (P). **D–F**, Combined mechanism IJMPQ. **A, D**, Information cost is applied only to the low-cooperation-cost population ($i_1 = 0$; $i_0$ swept). **B, E**, Information cost is applied only to the high-cooperation-cost population ($i_0 = 0$; $i_1$ swept). **C, F**, The total information cost is fixed at $i_0 + i_1 = 0.2$ while the distribution between populations varies. Under partner choice (**A, B**), populations are robust to their own information costs but cooperate much less under their partner's. Under IJMPQ (**D, E**), this relationship reverses: raising information cost on the low-cost population reduces cooperation more in its high-cost partner than in the payer. Reciprocity-bearing mechanisms also reach their lowest cooperation at an interior split of a fixed total (**F**).

## 5. Both information costs vary

Across the full i₀ × i₁ square behind Figs. 4–5, under partner choice the
lower-cooperation-cost population cooperates more than its partner in 170/176 cells;
under IJMPQ they show role inversion — the expensive population's cooperation above
the cheap one's — locally only on the i₀ ≈ 0 strip (13 cells). That role inversion is
stronger when populations differ only in information cost (Fig. S11 shows the
assignment under P and the inversion under IJMPQ; under IMP at the same design, the
cooperation gap, cheap minus expensive, reaches −0.461 when i₀ = 0 and i₁ = 0.20) and
weaker once a cooperation-cost gap is present (cooperation gap −0.100 at the same
information-cost point). The cooperation-cost gap moves every reciprocity-bearing
mechanism toward the cheap-cooperation-cost population, erasing the inversion
outright for MP and MPQ.

Fig. 5 shows how that inversion shrinks as the low-cooperation-cost population's
information cost rises from zero. Each panel fixes i₀ and sweeps i₁. The inversion —
the expensive population's curve above the cheap one's — holds throughout when
i₀ = 0 (Fig. 5a), survives only past a threshold when i₀ = 0.02 (Fig. 5b), and is
gone by i₀ = 0.04 and 0.1 (Fig. 5c,d). The transition into the state without
mechanism alleles is abrupt and bistable rather than gradual: just inside this
regime, raising population 1's information cost from 0.02 to 0.04 *raises* its
frequency of cooperators by 0.32 as it switches from a defector-heavy mixed state
into near-complete unconditional cooperation that pays no information cost. The
±1 SD bands locate that boundary directly — wide below the threshold (SD ≈ 0.25;
runs diverge to different outcomes) and narrow above it (SD ≈ 0.009).
In the paired fitness panels (Fig. 5e–h), the same cooperation-fitness mismatch holds
in every column: the population with higher cooperation is the one with lower fitness,
even when the color ordering switches as i₀ rises.
In this threshold regime, increasing population 1's own information cost can confer
a fitness benefit on population 0 even while population 1 becomes slightly less fit
(Fig. 5e–h), showing that one population can benefit from a partner that pays more for
enforcement alleles.

The inversion appears only when the reciprocity family is present, not as a simple
effect of how much information cost a mechanism pays. Information cost is incurred
per family carried — one unit for partner choice, one for reciprocity — so a
mechanism pays 0, 1 or 2 units however many loci it enables. At one unit, direct
reciprocity and partner choice pay identically, yet reciprocity inverts in 10 cells of
the i₀ ≈ 0 strip and partner choice in none. At two units, the four combined
mechanisms MP, MPQ, IMP, and IJMPQ pay identically, yet invert in 3, 1, 13 and 13
cells respectively. Every mechanism carrying the reciprocity family inverts somewhere
in that strip; no mechanism lacking it does. Once active reciprocity alleles become
unaffordable, populations fall back on cost-free unconditional cooperators (C1M0) —
the second-order free-rider genotype — whereas partner choice's bilateral swap
collapses when either side loses choosers, so P has no comparable cost-free
high-cooperation outcome. Partner choice's cooperation curve does cross above its
partner's in three cells, but in the opposite corner of the square and while its own
alleles are falling, not through that reciprocity free-rider route.

**Figure 5: Role inversion requires near-zero information costs in the low-cost population.** Frequency of cooperators (**A–D**) and average fitness (**E–H**) under IJMPQ in the prisoner's dilemma. Cooperation costs are fixed asymmetrically ($c_0 = 0.1$, orange; $c_1 = 0.2$, red). Each column holds the information cost of the low-cooperation-cost population ($i_0$) constant while sweeping $i_1$. **A, E**, $i_0 = 0$. **B, F**, $i_0 = 0.02$. **C, G**, $i_0 = 0.04$. **D, H**, $i_0 = 0.1$. The role inversion—where the expensive population cooperates more than the cheap one—survives only when $i_0$ is small. Shaded bands ($\pm 1$ SD over 30 runs) indicate a bistable threshold between mixed states and unconditional cooperation that pays no information cost. In this regime, fitness remains separated from cooperation: the population that cooperates more earns less fitness.

Snowdrift has no risk (S > P) and removes this inversion regime entirely on the same
crossed design, identifying this cross-population burden as a property of game type
rather than of the cost accounting. The control game makes the same point for
cooperation after mechanism alleles are lost (Fig. S8). Shuffled partnerships and
group size 4 leave the main contrasts intact (Figs. S2 and S6).
