# Results

I first compare mechanisms under equal cooperation cost in one population, then in
two. I next raise information cost when both populations pay alike, then let them
differ in who pays that cost, and finally vary both information costs together.

## 1. Equal cooperation cost in one population

I start with equal cooperation cost in a single population (Fig. S1). In the
prisoner's dilemma, cooperation stays near zero irrespective of cost in the
no-enforcement control (Fig. S1a). Cooperation collapses at successively higher
costs under direct reciprocity M (Fig. S1c), short-memory partner choice P
(Fig. S1b), and the combined mechanism IJMPQ (Fig. S1d), in that order.

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
instead of S). The same columns under snowdrift (Fig. S2) show more cooperation
without enforcement — unconditional cooperators keep cooperating while reciprocity
alleles are selected against — and the ordering among mechanisms flattens. Partner
choice (P) is limited by the cooperation advantage R − P in both games: it tracks
R − P alone across those independent sweeps, which is why it fails as R − P → 0.
The combined mechanisms MP, MPQ, IMP, and IJMPQ are reward-limited and do not track
the mutual-defection payoff P, which is why they sustain cooperation to the
highest costs (Fig. S1d). Under shuffled partnerships the same cost sweep for M,
MP, IM, and IMP collapses direct reciprocity, while short-memory indirect
reciprocity and the partner-choice combinations still sustain cooperation farther
(in both the prisoner's dilemma and snowdrift); partner choice alone is nearly
unchanged by shuffle. Those shuffle-only branches are not shown as separate
figures.

## 2. Equal and unequal cooperation cost in two populations

Two coevolving populations often settle into a cooperator role and an exploiter
role, and the population that cooperates more earns less fitness. Whether those
roles appear depends on the game and on the enforcement mechanism.

Fig. 1 places matched costs (top row, greens) and a small cooperation-cost gap
c₁ = c₀ + 0.02 (bottom row, orange/red) on shared axes under the prisoner's
dilemma; columns are no enforcement, partner choice (P), direct reciprocity (M),
and combined IJMPQ. Without enforcement, matched-cost populations both stay near
defection and take no roles (Fig. 1a), whereas the gap alone still assigns no
roles (Fig. 1e; cheap-side mean cooperation 0.10 across the full c₀ × c₁ grid,
expensive-side 0.03). Partner choice splits the matched-cost populations
stochastically: one cooperates more and is exploited, and the cooperation gap and
the fitness gap correlate at −0.98, so the population that cooperates more earns
less — the paradox of success (Fig. 1b; fitness Fig. S3). The same gap makes that
assignment deterministic
along the strip (Fig. 1f). Direct reciprocity and IJMPQ leave both populations
cooperating at similar frequencies under matched costs and under the gap, with no
cooperator/exploiter split: each side cooperates only as much as its partner does
(Fig. 1c,d,g,h). Under M and IJMPQ on the gap strip their fitness differs only by
the 0.02 cost gap (Fig. S3g,h). Under partner choice the cheap population cooperates
more in all 210 cells of the full grid and earns less fitness in all of them
(cooperation and fitness gaps correlate at −0.99; Fig. S5). The split also stays
deterministic in groups of 4, where each population samples few partners per round
(Fig. S7).

**Figure 1: Cooperation under symmetric and asymmetric cooperation costs (prisoner's dilemma).** Frequency of cooperators under different cost symmetries and cooperation mechanisms. (**A–D**) Cooperation costs follow $c_1 = c_0$ (light green for the population with the lower frequency of cooperators, dark green for the other). (**E–H**) Cooperation costs follow $c_1 = c_0 + 0.02$ (orange = cheaper population $c_0$; red = expensive $c_1$). (**A, E**) No enforcement. (**B, F**) Short-memory partner choice. (**C, G**) Direct reciprocity. (**D, H**) Combined IJMPQ. Both populations pay identical information costs ($0.001$). Fitness counterpart: Fig. S3. Snowdrift twin: Fig. 2. Full grid: Fig. S5; gs = 4: Fig. S7.

Fig. 2 repeats the same layout under snowdrift. Without enforcement the populations
already split stochastically on the payoffs alone, because S > P leaves no risk in
cooperating with a defector (Fig. 2a), and the asymmetry makes the split largely
deterministic (Fig. 2e–g; 0.96 and 0.09 for the cheap and expensive sides across
the no-enforcement grid). Partner choice extends the payoff-driven split to higher
cooperation costs when costs match and leaves it nearly unchanged under the gap
(0.96 and 0.10; Fig. 2b,f). Direct reciprocity holds both populations near 0.92
while c ≤ 0.08 under matched costs and lifts the expensive side to 0.19 under the
gap; above that cost a narrower split returns, narrower than without enforcement
(Fig. 2c,g). IJMPQ holds both near 0.96 across the matched-cost sweep and lifts the
expensive side to 0.61 under the gap (Fig. 2d,h). Fitness counterpart: Fig. S4; full
grid Fig. S6; gs = 4 Fig. S8.

**Figure 2: Cooperation under symmetric and asymmetric cooperation costs (snowdrift).** Frequency of cooperators under different cost symmetries and cooperation mechanisms (same layout as Fig. 1). Fitness counterpart: Fig. S4. Full grid: Fig. S6; gs = 4: Fig. S8.

## 3. Matched information cost

Individuals pay an information cost for each mechanism family they carry, whether or
not they express it (Methods). Where cooperation is free (c = 0, so T = R), that cost
alone reduces cooperation only gently (Fig. S9b,d); the no-enforcement control stays
near 0.50. The same value as a cooperation cost is harsher: at c = 0.40 with a nearly
free mechanism, partner choice and direct reciprocity both collapse (Fig. S1b,c).
IJMPQ carries both families and so pays two units per round; at an information cost of
0.20 it therefore pays 0.40 per round, the same amount partner choice pays at 0.40,
yet it still cooperates at high frequency while partner choice has fallen
(Fig. S11; Fig. S9b).

Cooperation survives at c = 0 because populations keep cooperating unconditionally.
Across that sweep the chooser allele P1 and the tit-for-tat allele M1 both fall toward
zero (Fig. S9a,c), while cooperators that carry neither locus become more common.
Cooperation frequency and mechanism-allele frequency diverge (Fig. S9b,d).
Snowdrift twin: Fig. S10.

The information cost lowers the cooperation cost a population can withstand. Under
IJMPQ in the prisoner's dilemma, cooperation holds to high c when the mechanism is
nearly free and collapses at far lower c once the information cost is 0.20 (Fig. S11).
Snowdrift removes that interaction: cooperation stays high across the whole
information-cost × c grid, including the cell where the prisoner's dilemma collapses
(Fig. S12). Because S > P, cooperation is favored without enforcement, so losing the
alleles costs little.

Populations keep cooperating after losing the alleles only where cooperation is free.
Once every individual pays a cooperation cost, alleles and behavior fall together.
Fig. S13 holds the cooperation-cost gap of section 2 and raises a shared information
cost: the partner-choice split shrinks as that cost rises, rather than reversing.
Direct reciprocity collapses both prisoner's-dilemma populations together once the
information cost rises, with no residual split. IJMPQ postpones that collapse but
does not restore the free-cooperation outcome. In snowdrift (Fig. S14) the cheap
population stays near full cooperation under partner choice, direct reciprocity, and
IJMPQ even at high information cost, while the expensive population remains the
exploiter; IJMPQ raises that side at low information cost and then loses it as the
cost rises.

A matched information cost cannot separate the cost a population pays from the burden
that cost places on its partner. Both populations pay the same information cost in
every cell above, so a fall in cooperation cannot be assigned to the payer or to its
partner. Holding one population's information cost at zero and sweeping the other's
separates the two.

## 4. Independent per-population information costs

Under partner choice, with a fixed cooperation-cost gap (c₀ = 0.1, c₁ = 0.2) and
independent per-population information costs, a population barely bears a burden from
its own information cost and cooperates much less under the burden of its partner's
(Fig. 3a,b). Figs. 3–4 cross that cooperation-cost gap with those information costs;
mechanisms are rows and designs are columns. The first two columns of Fig. 3 hold one
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

Under IJMPQ the pattern reverses (Fig. 3d,e). When the low-cooperation-cost
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
neither interchangeable nor additive (Fig. 3c,f). Along a line of constant total
information cost (0.20), every reciprocity-bearing mechanism reaches its *lowest*
total cooperation — the sum of the two populations' frequencies of cooperators, on a
0–2 scale — when the total is split between populations rather than paid by one side
alone. Under IJMPQ populations that place a total of 0.20 on one side reach 1.0–1.65
total cooperation, but only 0.39 when they split it as (0.06, 0.14) (Fig. 3f). Either
end leaves one population still carrying mechanism alleles, which is enough to
sustain cooperation in both; a split reduces both populations' mechanism alleles so
that neither remains above the threshold at which cooperation without those alleles
takes over. Partner choice does not show that interior minimum (Fig. 3c): because
only the high-cooperation-cost population's information cost matters, total
cooperation is highest when that population pays none of the total. That
non-additivity is therefore a property of reciprocity-bearing mechanisms, not of the
total itself. The fitness counterpart of these slices shows the same cross-population
burdens and the same interior minimum under a fixed total (Fig. S15; snowdrift
Fig. S16).

The pattern that let a population keep cooperating under information cost under
symmetry (Fig. S9) is what places a burden on its partner under asymmetry: losing
mechanism alleles relieves the payer and removes the assortment or conditional help
the partner needed.

**Figure 3: Who pays the information cost matters more than how much (prisoner's dilemma).** Frequency of cooperators under different information-cost assignments and cooperation mechanisms. (**A–C**) Short-memory partner choice (P). (**D–F**) Combined mechanism IJMPQ. (**A, D**) Information cost falls only on the low-cooperation-cost population ($i_1 = 0$; $i_0$ swept). (**B, E**) Information cost falls only on the high-cooperation-cost population ($i_0 = 0$; $i_1$ swept). (**C, F**) Total information cost is fixed at $i_0 + i_1 = 0.2$ while the split varies. One population (orange) has $c_0 = 0.1$; the other (red) has $c_1 = 0.2$. Full grid: Figs. S17–S18. Snowdrift: Fig. S19. Fitness: Fig. S15.

## 5. Both information costs vary

Across the full i₀ × i₁ square (Fig. S17; snowdrift Fig. S18), under partner choice the
lower-cooperation-cost population cooperates more than its partner in 170/176 cells;
under IJMPQ they show role inversion — the expensive population's cooperation above
the cheap one's — locally only on the i₀ ≈ 0 strip (13 cells). That role inversion is
stronger when populations differ only in information cost (Fig. S20 shows the
assignment under P and the inversion under IJMPQ; under IMP at the same design, the
cooperation gap, cheap minus expensive, reaches −0.461 when i₀ = 0 and i₁ = 0.20;
snowdrift counterpart Fig. S21) and weaker once a cooperation-cost gap is present
(cooperation gap −0.100 at the same information-cost point). The cooperation-cost
gap moves every reciprocity-bearing mechanism toward the cheap-cooperation-cost
population, erasing the inversion outright for MP and MPQ.

Fig. 4 shows how that inversion shrinks as the low-cooperation-cost population's
information cost rises from zero. Each panel fixes i₀ and sweeps i₁. The inversion —
the expensive population's curve above the cheap one's — holds throughout when
i₀ = 0 (Fig. 4a), survives only past a threshold when i₀ = 0.02 (Fig. 4b), and is
gone by i₀ = 0.04 and 0.1 (Fig. 4c,d). The snowdrift twin (Fig. S22) does not show
this near-zero-i₀ inversion regime. The transition into the state without
mechanism alleles is abrupt and bistable rather than gradual: just inside this
regime, raising population 1's information cost from 0.02 to 0.04 *raises* its
frequency of cooperators by 0.32 as it switches from a defector-heavy mixed state
into near-complete unconditional cooperation that pays no information cost. The
±1 SD bands locate that boundary directly — wide below the threshold (SD ≈ 0.25;
runs diverge to different outcomes) and narrow above it (SD ≈ 0.009).
In the paired fitness panels (Fig. 4e–h), the same cooperation-fitness mismatch holds
in every column: the population with higher cooperation is the one with lower fitness,
even when the color ordering switches as i₀ rises.
In this threshold regime, increasing population 1's own information cost can confer
a fitness benefit on population 0 even while population 1 becomes slightly less fit
(Fig. 4e–h), showing that one population can benefit from a partner that pays more for
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

**Figure 4: The expensive population cooperates more only when the cheap one's information is nearly free (prisoner's dilemma).** Frequency of cooperators and average fitness under the combined mechanism IJMPQ, for different information costs on the cheap population. (**A–D**) Frequency of cooperators. (**E–H**) Average fitness. (**A, E**) $i_0 = 0$. (**B, F**) $i_0 = 0.02$. (**C, G**) $i_0 = 0.04$. (**D, H**) $i_0 = 0.1$. Cooperation costs $c_0 = 0.1$ (orange) and $c_1 = 0.2$ (red); each column holds $i_0$ constant while sweeping $i_1$. Shaded bands are $\pm 1$ SD over 30 runs. Snowdrift: Fig. S22. Equal-c contrast: Fig. S20. Full grid: Figs. S17–S18.

Snowdrift has no risk (S > P) and removes this inversion regime entirely on the same
crossed design, identifying this cross-population burden as a property of game type
rather than of the cost accounting. Shuffled partnerships leave the main contrasts
intact (Results §1). The cooperator/exploiter split also stays deterministic in
groups of 4 (Fig. S7).
