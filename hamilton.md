# Hamilton — Equal-Cost Partner Choice

## Overview

Hamilton is the equal-cost diagonal of the mutualism parameter space: both
populations share the same cost c, so c0 = c1 = c throughout. The x-axis is
c ∈ [0, 0.40], with benefit b = 0.40 fixed and baseline fitness K = 0.50.
As c increases from 0 to b, the cooperation incentive (R − P) falls from 0.40
to 0. The x-axis therefore runs from a trivially cooperative regime (c = 0,
no real dilemma) to the hardest regime (c = b = 0.40, where R = P and mutual
cooperation gives no payoff advantage over mutual defection).

Mutualism.md develops the shared conceptual framework (cross-benefit payoffs,
chooser bottleneck, exploitation). This file documents Hamilton-specific
quantitative patterns: cooperation profiles across c, genotype structure,
population-structure contrasts, and temporal dynamics. Analysis covers
groupsize 128 (primary) and groupsize 4 (dedicated section plus comparison).

## Game parameters

| Parameter | Value         | Description                              |
| --------- | ------------- | ---------------------------------------- |
| b         | 0.40          | Benefit (fixed)                          |
| c         | 0.00 – 0.40   | Cost (x-axis; 21 values in steps of 0.02) |
| K         | 0.50          | Baseline fitness (T and P floor)         |
| groupsize | 4 and 128     | Individuals per group from each population (4 = closed pool) |

## Payoff structure

Three dilemma folders are present for all Hamilton runs.

| Folder | Dilemma    | T        | R          | P    | S          | R - P      |
| ------ | ---------- | -------- | ---------- | ---- | ---------- | ---------- |
| 0      | No dilemma | K = 0.50 | K+b-c      | 0.50 | K+b-c      | b-c        |
| 1      | PD         | K+b=0.90 | K+b-c      | 0.50 | K-c        | b-c        |
| 2      | Snowdrift  | K+b=0.90 | K+b-c/2    | 0.50 | K+b-c      | b-c/2      |

Payoff values at selected c (K = 0.50, b = 0.40):

| c    | Dilemma | T    | R    | P    | S    | R-P  | T-R  |
| ---- | ------- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0.00 | 0       | 0.50 | 0.90 | 0.50 | 0.90 | 0.40 | 0.00 |
| 0.00 | 1       | 0.90 | 0.90 | 0.50 | 0.50 | 0.40 | 0.00 |
| 0.00 | 2       | 0.90 | 0.90 | 0.50 | 0.90 | 0.40 | 0.00 |
| 0.10 | 1       | 0.90 | 0.80 | 0.50 | 0.40 | 0.30 | 0.10 |
| 0.20 | 1       | 0.90 | 0.70 | 0.50 | 0.30 | 0.20 | 0.20 |
| 0.30 | 1       | 0.90 | 0.60 | 0.50 | 0.20 | 0.10 | 0.30 |
| 0.40 | 1       | 0.90 | 0.50 | 0.50 | 0.10 | 0.00 | 0.40 |
| 0.10 | 2       | 0.90 | 0.85 | 0.50 | 0.80 | 0.35 | 0.05 |
| 0.20 | 2       | 0.90 | 0.80 | 0.50 | 0.70 | 0.30 | 0.10 |
| 0.40 | 2       | 0.90 | 0.70 | 0.50 | 0.50 | 0.20 | 0.20 |

Key observations on the payoff geometry:

- At c = 0: T = R for both dilemma 1 and 2. There is no temptation to defect.
  The game is already cooperative and mechanisms have little marginal effect.
- For dilemma 1 (PD): T − R = c increases with c. At c = 0.40, T − R = 0.40
  and R − P = 0, the most extreme prisoner's dilemma possible in this space.
- For dilemma 2 (snowdrift): S > P for all c < 0.40 (since S = K+b-c > K = P).
  The snowdrift property makes cooperation robust even without mechanisms.
- No-dilemma folder (0): T = P always, so defection is never advantageous.
  All cooperation is sustained without mechanisms.

## Mechanisms and dilemma availability

Mechanisms _ and M are present for all three dilemma folders (0, 1, 2).
All other mechanisms (P, MP, MPQ, IM, IJM, IMP, IJMPQ) are present for
dilemma folders 1 and 2 only.

Conditions: shuffle and noshuffle × groupsize 128 and 4 × pop_1, pop_2, pop_3.
All .con summary files (image and movie) are present under ~/results/hamilton/ for both groupsizes.

## Cooperation profiles

### Dilemma 1 (PD), shuffle, groupsize 128, pop_2 fset_0

qBSeen at selected c values (pop_2 file_set 0 = higher-cooperating population):

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| \_     | 0.535  | 0.066  | 0.034  | 0.022  | 0.017  | 0.014  |
| M      | 0.541  | 0.068  | 0.035  | 0.023  | 0.017  | 0.014  |
| P      | 0.963  | 0.849  | 0.728  | 0.630  | 0.553  | 0.022  |
| MP     | 0.961  | 0.847  | 0.728  | 0.651  | 0.553  | 0.023  |
| MPQ    | 0.967  | 0.872  | 0.737  | 0.643  | 0.563  | 0.036  |
| IM     | 0.944  | 0.909  | 0.676  | 0.148  | 0.051  | 0.032  |
| IJM    | 0.973  | 0.968  | 0.961  | 0.141  | 0.076  | 0.043  |
| IMP    | 0.963  | 0.951  | 0.939  | 0.776  | 0.805  | 0.170  |
| IJMPQ  | 0.975  | 0.972  | 0.967  | 0.958  | 0.923  | 0.672  |

Key patterns:

- Control (\_ and M with shuffle): near-zero cooperation for all c > 0. The
  single high value at c = 0 (0.53–0.54) reflects the T = R boundary
  condition, not genuine mechanism-driven cooperation.

- Partner choice (P, MP, MPQ): sustained high cooperation at low to moderate c,
  then a sharp drop between c = 0.34 and c = 0.36 (qBSeen falls from 0.41 to
  0.036 for P). This threshold is the chooser bottleneck: at high c, defection
  so dominates that insufficient C1P1 individuals exist to sustain swaps.

- Direct reciprocity alone (M with shuffle): indistinguishable from control.
  Shuffling destroys repeated interactions. See noshuffle section for a
  fundamentally different result.

- Direct reciprocity alone (IM): drops sharply at c ≈ 0.20 (0.676 → 0.148 at
  c = 0.24). When repeated interactions are allowed (shuffle) they are still
  unstable at high cost in the PD.

- IJM (direct + lifetime indirect reciprocity): maintains high cooperation
  through c = 0.16 (0.961), then drops at c = 0.24 (0.141). Longer memory
  extends the cooperation window but does not change the qualitative threshold.

- IMP (all three mechanisms combined): extends cooperation noticeably above P
  alone; at c = 0.40, qBSeen = 0.170 vs 0.022 for P.

- IJMPQ (all mechanisms with lifetime variants): most robust. Cooperation
  remains above 0.92 through c = 0.32, and reaches 0.672 even at c = 0.40.
  The combination of all mechanisms eliminates the threshold collapse seen in
  simpler combinations.

### Dilemma 2 (snowdrift), shuffle, groupsize 128, pop_2 fset_0

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| \_     | 0.881  | 0.968  | 0.964  | 0.954  | 0.917  | 0.184  |
| M      | 0.888  | 0.963  | 0.960  | 0.949  | 0.916  | 0.182  |
| P      | 0.955  | 0.970  | 0.969  | 0.958  | 0.930  | 0.679  |
| MPQ    | 0.964  | 0.970  | 0.965  | 0.957  | 0.935  | 0.780  |
| IJMPQ  | 0.973  | 0.971  | 0.969  | 0.966  | 0.962  | 0.960  |

For snowdrift (folder 2), cooperation is high across the board because S > P
forces cooperation at a game-theoretic level. The control (\_ mechanism) shows
qBSeen ≈ 0.96 at moderate c without any mechanism, confirming that snowdrift
self-sustains cooperation. Mechanisms provide modest additional benefit at
moderate c but the main benefit is at c = 0.40, where IJMPQ reaches 0.960 vs
0.184 for the control.

### No-dilemma folder (0), shuffle, groupsize 128, pop_2 fset_0

| c    | \_ (d0) | \_ (d1) | \_ (d2) |
| ---- | ------- | ------- | ------- |
| 0.00 | 0.979   | 0.535   | 0.881   |
| 0.08 | 0.977   | 0.066   | 0.968   |
| 0.24 | 0.965   | 0.022   | 0.954   |
| 0.40 | 0.528   | 0.014   | 0.184   |

The no-dilemma folder (T = P always) shows near-complete cooperation for all
c < 0.40 without any mechanism, confirming that the simulation produces the
correct baseline: when defection is never advantageous, cooperation dominates.

## Groupsize 4

Groupsize 4 means four individuals per group from each population (four total
in pop_1). Each group is a fixed memory segment for the whole run; shuffle only
redraws pairings within that pool. The patterns below are PD (dilemma 1),
shuffle, pop_2 fset_0 unless noted — the same reference condition as the
gs=128 cooperation profiles above.

### Cooperation profiles (gs=4)

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| \_     | 0.516  | 0.065  | 0.033  | 0.023  | 0.017  | 0.013  |
| M      | 0.851  | 0.169  | 0.053  | 0.031  | 0.022  | 0.017  |
| P      | 0.878  | 0.812  | 0.038  | 0.024  | 0.018  | 0.014  |
| MP     | 0.904  | 0.858  | 0.670  | 0.116  | 0.036  | 0.024  |
| MPQ    | 0.932  | 0.903  | 0.763  | 0.337  | 0.076  | 0.036  |
| IM     | 0.944  | 0.923  | 0.841  | 0.340  | 0.074  | 0.040  |
| IJM    | 0.970  | 0.967  | 0.956  | 0.930  | 0.176  | 0.059  |
| IMP    | 0.951  | 0.935  | 0.900  | 0.801  | 0.555  | 0.065  |
| IJMPQ  | 0.967  | 0.961  | 0.954  | 0.940  | 0.892  | 0.342  |

Compared with gs=128 on the same table:

- **Control and P**: P holds cooperation through c ≈ 0.08 (0.812) then collapses
  by c = 0.16 (0.038), versus gs=128 where P stays above 0.55 through c = 0.32.
  The chooser bottleneck bites much earlier in small groups.

- **IJM reversal**: IJM remains above 0.93 through c = 0.24 and only falls to
  0.176 at c = 0.32. At gs=128, IJM collapses near c = 0.20. In gs=4 the closed
  reputation pool sustains indirect reciprocity far longer.

- **IJMPQ**: Still the most robust combined mechanism (0.892 at c = 0.32, 0.342
  at c = 0.40), but the high-c tail is much weaker than gs=128 (0.672 at c = 0.40).

- **M with shuffle**: Not identical to control at gs=4 — qBSeen = 0.851 at c = 0
  and 0.169 at c = 0.08, whereas gs=128 M shuffle tracks control throughout.
  Small fixed groups allow residual reciprocity-like signal even under shuffle.

### Snowdrift at gs=4

| Mech   | c=0.00 | c=0.08 | c=0.16 | c=0.24 | c=0.32 | c=0.40 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| \_     | 0.880  | 0.966  | 0.964  | 0.954  | 0.920  | 0.179  |
| M      | 0.891  | 0.919  | 0.914  | 0.895  | 0.832  | 0.690  |
| IJMPQ  | 0.960  | 0.957  | 0.955  | 0.953  | 0.949  | 0.933  |

Snowdrift cooperation remains high through moderate c at gs=4, similar to gs=128.
IJMPQ reaches 0.933 at c = 0.40 (vs 0.960 at gs=128). Direct reciprocity (M)
also sustains much higher cooperation at high c in snowdrift than in PD
(0.690 vs 0.017 at c = 0.40).

### Shuffle vs noshuffle at gs=4

| Mech  | Condition | c=0.00 | c=0.10 | c=0.20 | c=0.30 | c=0.40 |
| ----- | --------- | ------ | ------ | ------ | ------ | ------ |
| M     | shuffle   | 0.851  | 0.112  | 0.040  | 0.023  | 0.017  |
| M     | noshuffle | 0.944  | 0.912  | 0.857  | 0.740  | 0.082  |
| P     | shuffle   | 0.878  | 0.698  | 0.029  | 0.019  | 0.014  |
| P     | noshuffle | 0.886  | 0.749  | 0.029  | 0.018  | 0.014  |
| IJMPQ | shuffle   | 0.967  | 0.958  | 0.948  | 0.914  | 0.342  |
| IJMPQ | noshuffle | 0.962  | 0.956  | 0.942  | 0.900  | 0.363  |

The M mechanism still shows the largest shuffle effect: noshuffle sustains
0.857 at c = 0.20 versus 0.040 with shuffle. Partner choice (P) collapses by
c = 0.20 under both conditions at gs=4. IJMPQ is less sensitive to shuffle than
M but still benefits from stable pairings at moderate c.

### pop_2 symmetry breaking at gs=4

With the P mechanism, symmetry breaks sharply at low c before both populations
collapse together:

| c    | fset_0 | fset_1 | ΔqBSeen |
| ---- | ------ | ------ | ------- |
| 0.08 | 0.812  | 0.367  | +0.445  |
| 0.10 | 0.698  | 0.339  | +0.359  |
| 0.16 | 0.038  | 0.031  | +0.007  |

The higher-cooperating population cannot sustain the chooser bottleneck once
c exceeds ≈ 0.10. With IJMPQ, symmetry is maintained throughout (ΔqBSeen < 0.01
through c = 0.30; both populations fall together to ≈ 0.34 at c = 0.40).

## Shuffle vs noshuffle

The most striking shuffle effect is on direct reciprocity (M mechanism):

| Mech  | Condition    | c=0.00 | c=0.10 | c=0.20 | c=0.30 | c=0.40 |
| ----- | ------------ | ------ | ------ | ------ | ------ | ------ |
| \_    | shuffle      | 0.535  | 0.055  | 0.028  | 0.018  | 0.014  |
| \_    | noshuffle    | 0.528  | 0.054  | 0.029  | 0.019  | 0.013  |
| M     | shuffle      | 0.541  | 0.053  | 0.028  | 0.019  | 0.014  |
| M     | noshuffle    | 0.941  | 0.915  | 0.859  | 0.754  | 0.084  |
| P     | shuffle      | 0.963  | 0.833  | 0.667  | 0.566  | 0.022  |
| P     | noshuffle    | 0.961  | 0.811  | 0.688  | 0.569  | 0.023  |
| IJMPQ | shuffle      | 0.975  | 0.971  | 0.964  | 0.939  | 0.672  |
| IJMPQ | noshuffle    | 0.969  | 0.965  | 0.953  | 0.921  | 0.382  |

Direct reciprocity (M) with shuffle is identical to the control — without
repeated interactions with the same partner, TFT-style strategies cannot
accumulate credit. Without shuffling, M becomes the strongest individual
mechanism at moderate c (0.915 at c = 0.10) but collapses at high c
(0.084 at c = 0.40), consistent with the PD iterated game theory: at
extreme T − R ratios, defection eventually invades TFT.

Partner choice (P) is largely insensitive to shuffle: cooperation levels
differ by less than 0.03 across the cooperation range. The chooser bottleneck
determines P mechanism outcomes, not partner continuity.

IJMPQ with shuffle outperforms noshuffle at high c (0.672 vs 0.382), suggesting
that partner choice components leverage shuffling by maintaining more diverse
interaction opportunities.

## Population structure

### Single population (pop_1)

Pop_1 pairs individuals within the same population. Key data for the P
mechanism (shuffle, PD):

| c    | qBSeen | C1P1  | C1P0  | C0P1  | P1    | C1P0/qBSeen |
| ---- | ------ | ----- | ----- | ----- | ----- | ----------- |
| 0.00 | 0.961  | 0.632 | 0.329 | 0.024 | 0.656 | 34%         |
| 0.10 | 0.949  | 0.669 | 0.280 | 0.035 | 0.704 | 29%         |
| 0.20 | 0.929  | 0.748 | 0.181 | 0.054 | 0.802 | 19%         |
| 0.30 | 0.864  | 0.774 | 0.090 | 0.109 | 0.883 | 10%         |
| 0.36 | 0.668  | 0.639 | 0.029 | 0.242 | 0.881 |  4%         |
| 0.38 | 0.346  | 0.334 | 0.012 | 0.379 | 0.713 |  3%         |
| 0.40 | 0.056  | 0.049 | 0.007 | 0.463 | 0.511 | 13%         |

Pop_1 maintains higher cooperation than pop_2 at most c values because the
chooser bottleneck is weaker: in a single population, both partners for a
potential swap are drawn from the same pool, so C1P1 individuals can find
swap partners from their own cooperating subgroup.

As c increases, C1P1 rises while C1P0 falls. At high c (≈ 0.30), cooperators
who can choose (C1P1) dominate the cooperation pool; non-chooser cooperators
(C1P0) become rare because the cost makes cooperation unsustainable without
the sorting benefit of partner choice.

The P1 allele peaks at c ≈ 0.34 (P1 = 0.898) before cooperation collapses.
P1 peaks later than C1P1 because C0P1 (defectors carrying P1 silently)
accumulates via mutation from the C1P1 pool. At c = 0.40 after cooperation
collapses, C0P1 = 0.463 dominates P1 = 0.511 — a large reservoir of neutral
P1 carriers persists even when cooperation itself is near zero.

## P1 hitchhiking

### The pattern

The P1 allele peaks at a lower c than the C1P1 allele. This occurs across all
three population structures:

| Population       | P1 max c | P1    | C1P1 max c | C1P1  |
| ---------------- | -------- | ----- | ---------- | ----- |
| pop_1            | 0.34     | 0.898 | 0.30       | 0.774 |
| pop_2 (fset_0)   | 0.18     | 0.858 | 0.10       | 0.687 |
| pop_3 (evolving) | 0.14     | 0.821 | 0.08       | 0.666 |

### The mechanism

The P1 allele is phenotypically silent in defectors: C0P1 individuals carry P1
but never activate partner choice. The P1 maximum occurs in the transition
zone where:

1. C1P1 is still substantial (partner choice is under positive selection)
2. Enough defectors persist to serve as neutral P1 carriers
3. Mutation from C1P1 to C0P1 creates a reservoir of silent P1 carriers

At the P1 maximum in pop_1 (c = 0.34): C1P1 = 0.735, C0P1 = 0.163. At the
C1P1 maximum (c = 0.30): C1P1 = 0.774, C0P1 = 0.109. Moving from the P1 max
to the C1P1 max, C1P1 gains only 0.039 while C0P1 loses 0.054 — the net P1
falls because neutral carriers are suppressed faster than selected carriers
grow.

### Why the P1 max shifts across population structures

In pop_1 the P1 maximum is at c = 0.34 — high, because cooperation remains
strong through c = 0.30 in a single population. In pop_2 the maximum shifts
to c = 0.18, and in pop_3 to c = 0.14, because between-population pairing
requires higher R − P to establish cooperation, so the transition zone where
C1P1 is abundant but defection persists occurs at lower c. The P1 peak always
occurs in the transition zone; the location of that zone shifts with population
structure.

### Two coevolving populations (pop_2)

Pop_2 pairs individuals from two separate populations. The two populations
evolve independently but interact with each other. In Hamilton they start
symmetric (same c) but break symmetry: one population cooperates more (fset_0)
and the other defects more (fset_1).

Symmetry breaking under P mechanism (shuffle, PD):

| c    | qBSeen_0 | qBSeen_1 | ΔqBSeen | w\_0  | w\_1  | Δw     |
| ---- | -------- | -------- | ------- | ----- | ----- | ------ |
| 0.00 | 0.963    | 0.932    | +0.031  | 0.871 | 0.883 | -0.012 |
| 0.02 | 0.956    | 0.753    | +0.203  | 0.780 | 0.866 | -0.085 |
| 0.04 | 0.928    | 0.405    | +0.523  | 0.623 | 0.853 | -0.230 |
| 0.06 | 0.891    | 0.330    | +0.562  | 0.577 | 0.835 | -0.258 |
| 0.10 | 0.833    | 0.315    | +0.518  | 0.541 | 0.800 | -0.259 |
| 0.20 | 0.667    | 0.389    | +0.278  | 0.520 | 0.687 | -0.167 |
| 0.30 | 0.566    | 0.475    | +0.091  | 0.518 | 0.582 | -0.064 |
| 0.34 | 0.408    | 0.387    | +0.021  | 0.514 | 0.530 | -0.016 |
| 0.36 | 0.036    | 0.033    | +0.004  | 0.498 | 0.501 | -0.003 |
| 0.40 | 0.022    | 0.020    | +0.002  | 0.497 | 0.499 | -0.002 |

The asymmetry is largest at c ≈ 0.04–0.08 (ΔqBSeen ≈ 0.52–0.56). At the
transition near c = 0.36, the asymmetry collapses to near zero as both
populations lose cooperation. The correlation between cooperation advantage and
fitness deficit is −0.984: the cooperating population consistently earns less
fitness. This is the paradox of success — the more efficiently one population
cooperates, the more it can be exploited by the other, whose defectors receive
benefits without paying.

At c = 0.06–0.10, the defecting population earns ≈1.4–1.5× the fitness of
the cooperating population despite cooperating at only 35–38% of its level.
As c increases, exploitation narrows: by c = 0.30–0.34, the gap shrinks
(Δw ≈ 0.06–0.02) as both populations approach similar low cooperation and
similar low payoffs.

For IJMPQ (all mechanisms), the symmetry breaking is almost absent:

| c    | qBSeen_0 | qBSeen_1 | ΔqBSeen | w\_0  | w\_1  | Δw     |
| ---- | -------- | -------- | ------- | ----- | ----- | ------ |
| 0.00 | 0.975    | 0.974    | +0.002  | 0.888 | 0.888 | -0.001 |
| 0.20 | 0.964    | 0.962    | +0.002  | 0.690 | 0.691 | -0.001 |
| 0.40 | 0.672    | 0.664    | +0.009  | 0.495 | 0.502 | -0.007 |

IJMPQ suppresses symmetry breaking through c = 0.38. Both populations converge
to nearly identical high cooperation, and the fitness disadvantage of the
cooperating population essentially vanishes. The combination of all mechanisms
eliminates the exploitation trap that plagues simpler mechanism combinations.

### Pop_3: evolving population against fixed partner

Pop_3 pairs the evolving population (fset_0) against a fixed population held
at 25% each of C0P0, C0P1, C1P0, C1P1. This tests how well cooperation can
develop when one side is a constant environment.

P mechanism, shuffle, PD:

| c    | qBSeen (evolving) | C1P1  | C1P0  | C0P1  |
| ---- | ----------------- | ----- | ----- | ----- |
| 0.00 | 0.936             | 0.608 | 0.328 | 0.040 |
| 0.08 | 0.856             | 0.666 | 0.190 | 0.103 |
| 0.16 | 0.604             | 0.548 | 0.056 | 0.263 |
| 0.24 | 0.392             | 0.368 | 0.024 | 0.370 |
| 0.26 | 0.073             | 0.059 | 0.014 | 0.476 |
| 0.30 | 0.043             | 0.031 | 0.012 | 0.474 |

The transition occurs near c = 0.24–0.26: cooperation drops from 0.392 to
0.073. Below the transition, C1P1 dominates (choosers drive cooperation).
Above it, C0P1 (neutral P1 carriers) reaches ≈ 0.47, the largest it can
be (= 25% from the fixed population × 2 from mutation into the evolving
population side). The fixed fset_1 remains at qBSeen ≈ 0.500 (25% C1P0 +
25% C1P1) throughout, confirming it is not evolving.

The pop_3 transition is sharper than pop_2 (which shows gradual decline) but
occurs at a lower c than the pop_1 collapse (c ≈ 0.36–0.38 in pop_1). The
fixed partner provides a constant supply of C1P1 swap candidates, giving the
evolving population a slight boost over pop_2 at low to moderate c, but the
fixed 25% C1P1 in the partner also limits the swap pool. Pop_1, by contrast,
keeps all its cooperators in the same pool and can execute swaps whenever two
C1P1 individuals are both stuck with defectors, which happens at any cooperator
frequency. Pop_3 needs its evolving C1P1 to match against the fixed 25% C1P1,
a weaker boost.

### Exploitation crossover in pop_3

The direction of exploitation reverses as cooperation grows:

| c    | q\_evolv | w\_evolv | w\_fixed | Δw (evolv−fixed) |
| ---- | -------- | -------- | -------- | ---------------- |
| 0.00 | 0.936    | 0.699    | 0.873    | -0.174           |
| 0.04 | 0.910    | 0.662    | 0.842    | -0.180           |
| 0.10 | 0.796    | 0.618    | 0.767    | -0.149           |
| 0.16 | 0.604    | 0.602    | 0.660    | -0.058           |
| 0.18 | 0.541    | 0.600    | 0.625    | -0.025           |
| 0.20 | 0.491    | 0.601    | 0.594    | +0.006           |
| 0.24 | 0.392    | 0.604    | 0.536    | +0.068           |
| 0.26 | 0.073    | 0.680    | 0.397    | +0.282           |
| 0.30 | 0.043    | 0.686    | 0.365    | +0.321           |
| 0.40 | 0.025    | 0.689    | 0.308    | +0.381           |

At low c (c < 0.18), the evolving population cooperates far more (0.54–0.94)
than the fixed average (0.50). The fixed population's defectors (50%) receive
benefits from the cooperating evolving individuals without paying — the fixed
population has higher fitness. The crossover occurs near c = 0.18–0.20, where
the evolving population's cooperation level approaches the fixed 0.50. Above
c = 0.26, the evolving population has collapsed to near-defection, so the fixed
population's cooperators are now paying costs to benefit the evolving defectors.
The fitness advantage now belongs to the evolving population.

Note that the fixed population's fitness falls monotonically across the full c
range (0.873 → 0.308). This reflects the overall payoff decline as c rises for
the fixed population's cooperating individuals (25% C1P0 + 25% C1P1).

## Temporal dynamics (hamilton_1run)

Single-run data (hamilton_1run, shuffle, PD, P mechanism, pop_2, 9 timesteps)
shows that cooperation at intermediate c values (0.04–0.34) is genuinely
variable across time, not a stable equilibrium:

| c    | Range (max−min over timesteps) | Representative trajectory     |
| ---- | ------------------------------ | ----------------------------- |
| 0.02 | 0.341                          | 0.961 → 0.700 → 0.910 → 0.969 |
| 0.04 | 0.165                          | 0.455 → 0.372 → 0.457 → 0.363 |
| 0.08 | 0.104                          | 0.851 → 0.801 → 0.905 → 0.899 |
| 0.16 | 0.063                          | 0.733 → 0.760 → 0.747 → 0.708 |
| 0.32 | 0.219                          | 0.569 → 0.483 → 0.367 → 0.563 |
| 0.36 | 0.024                          | 0.031 → 0.027 → 0.029 → 0.036 |

The wide ranges at intermediate c (0.04–0.34) reflect genuine metastability:
the cooperating and defecting roles of the two populations cycle or fluctuate.
The averaging of many replicates (multi-run data) smooths this to a stable
intermediate cooperation level that is not present in individual runs.

At c ≤ 0.00 and c ≥ 0.36, the trajectories are stable (range < 0.10),
confirming stable absorbing states at the extremes. The instability is
specific to the cooperation transition zone.

## Comparison across mechanisms

The mechanisms form a clear hierarchy in the PD at high c (c = 0.30–0.40):

1. IJMPQ: 0.939 at c = 0.30, 0.672 at c = 0.40 — sustains cooperation throughout.
2. IMP: 0.804 at c = 0.30, 0.170 at c = 0.40 — good but lower than IJMPQ.
3. P / MP / MPQ: 0.55–0.57 at c = 0.30, collapse to 0.022–0.036 at c = 0.40.
4. IJM: 0.084 at c = 0.30 (drops sharply near c = 0.24).
5. IM: 0.062 at c = 0.30 (drops near c = 0.20).
6. M (shuffle) / \_: near zero throughout.

The IJMPQ advantage over IMP at high c comes from the Q locus (lifetime partner
choice memory) and J locus (lifetime indirect reciprocity), which extend the
temporal horizon over which cooperation can be sustained.

For snowdrift (folder 2), the ranking is similar but all mechanisms perform
better: IJMPQ reaches 0.960 at c = 0.40 compared to 0.672 in PD. The snowdrift
property (S > P) provides a cooperation floor that mechanisms build upon.

## Groupsize comparison (gs=4 vs gs=128)

Groupsize has mechanism-specific effects that in some cases reverse the
ranking completely. All comparisons below are PD (dilemma 1), shuffle, pop_1.
Groupsize 4 means 4 individuals per group from each population (or 4 total
in pop_1); groupsize 128 means 128 per population.

### Summary table at selected c values (qBSeen)

| Mechanism | c=0.10 gs=4 | c=0.10 gs=128 | c=0.20 gs=4 | c=0.20 gs=128 | c=0.30 gs=4 | c=0.30 gs=128 |
| --------- | ----------- | ------------- | ----------- | ------------- | ----------- | ------------- |
| \_        | 0.974       | 0.973         | 0.965       | 0.968         | 0.941       | 0.942         |
| M shuffle | 0.164       | 0.049         | 0.040       | 0.026         | 0.023       | 0.017         |
| P         | 0.058       | 0.949         | 0.026       | 0.929         | 0.017       | 0.864         |
| MP        | 0.838       | 0.951         | 0.708       | 0.929         | 0.039       | 0.867         |
| MPQ       | 0.890       | 0.959         | 0.795       | 0.936         | 0.521       | 0.881         |
| IM        | 0.911       | 0.901         | 0.699       | 0.404         | 0.180       | 0.062         |
| IJM       | 0.947       | 0.965         | 0.923       | 0.195         | 0.790       | 0.079         |
| IMP       | 0.933       | 0.950         | 0.900       | 0.933         | 0.777       | 0.873         |
| IJMPQ     | 0.950       | 0.971         | 0.943       | 0.960         | 0.900       | 0.939         |

### Partner choice (P) — threshold collapses at gs=4

The P mechanism threshold shifts from c ≈ 0.34 (gs=128) to c ≈ 0.08 (gs=4).
With only a few individuals per group, the probability of two C1P1 choosers
being co-assigned to the same group is too low to sustain the mutual-swap
bottleneck except at very low c, where C1P1 is still common.

| c    | gs=4  | gs=128 |
| ---- | ----- | ------ |
| 0.06 | 0.763 | 0.955  |
| 0.08 | 0.728 | 0.950  |
| 0.10 | 0.058 | 0.949  |
| 0.12 | 0.047 | 0.950  |
| 0.20 | 0.026 | 0.929  |
| 0.30 | 0.017 | 0.864  |
| 0.36 | 0.014 | 0.668  |

MP and MPQ partially recover at gs=4 by using the reciprocity component (M
locus) to sustain cooperation where P alone collapses. MPQ reaches 0.521 at
c = 0.30 (gs=4) vs 0.039 for MP alone, because lifetime memory (Q locus)
compensates for the loss of partner choice.

### Indirect reciprocity (IJM) — dramatic reversal

IJM is one of the weakest mechanisms at gs=128 (collapses sharply near
c = 0.18-0.20) but becomes one of the strongest at gs=4.

| c    | IJM gs=4 | IJM gs=128 | IM gs=4 | IM gs=128 |
| ---- | -------- | ---------- | ------- | --------- |
| 0.16 | 0.936    | 0.962      | 0.831   | 0.769     |
| 0.18 | 0.928    | 0.858      | 0.787   | 0.664     |
| 0.20 | 0.923    | 0.195      | 0.699   | 0.404     |
| 0.24 | 0.895    | 0.141      | 0.481   | 0.164     |
| 0.30 | 0.790    | 0.079      | 0.180   | 0.062     |
| 0.34 | 0.267    | 0.060      | 0.083   | 0.043     |

In the shuffle condition, Imimic copies partner->qBSeen after each reshuffle —
what the partner did with their previous partner, a third party. This is
indirect reciprocity: reputation travels with the individual and new partners
react to it. Groups are fixed memory segments (individuals never move between
groups); the shuffle only redraws pairings within the same fixed group. At
gs=4 the group is a closed pool of 4 individuals, so reputation signals
circulate among the same few known players — cooperation propagates reliably.
At gs=128 the fixed group has 128 members of mixed strategy; defectors produce
many qBSeen=0 signals that disrupt the cascade for whoever pairs with them.
Smaller groups make indirect reciprocity more effective because signals concern
the same few individuals and defector signals are less prevalent.

### Direct reciprocity (M noshuffle) — groupsize invariant

The M mechanism with noshuffle is almost perfectly invariant to groupsize.
Stable pairings give each partner sufficient interaction history regardless
of group size.

| c    | M noshuffle gs=4 | M noshuffle gs=128 |
| ---- | ---------------- | ------------------ |
| 0.10 | 0.906            | 0.910              |
| 0.20 | 0.867            | 0.858              |
| 0.30 | 0.759            | 0.741              |
| 0.40 | 0.075            | 0.080              |

### IJMPQ — weaker at high c with gs=4

IJMPQ is slightly lower than gs=128 at all c and noticeably weaker at high c,
because the partner-choice component (P, Q) that sustains cooperation near
c = 0.40 in gs=128 collapses at gs=4. At c = 0.40: gs=4 gives 0.341 vs 0.676
for gs=128. The indirect reciprocity components (I, J) continue to help at
moderate c but cannot fully compensate at the extreme end.

### pop_2 symmetry breaking at gs=4

With P mechanism: symmetry breaks at c = 0.10 (fset_0 = 0.698, fset_1 = 0.339)
but both populations collapse to near zero by c = 0.20. The population with the
higher frequency of choosers cannot sustain the bottleneck long enough.

With IJMPQ: both populations remain high (>0.90) through c = 0.30 but fall to
0.342/0.337 at c = 0.40, compared to 0.672/0.664 at gs=128. Symmetry is
maintained (very small fset_0/fset_1 gap) at both groupsizes throughout.

### Revised mechanism hierarchy at gs=4

At gs=4 the PD hierarchy (c = 0.20-0.30) reorders substantially:

1. IJM: 0.923 / 0.790 — best at moderate-to-high c (reversed from gs=128 rank 6)
2. IJMPQ: 0.943 / 0.900 — still strong but lower than gs=128
3. IM: 0.699 / 0.180 — better than gs=128 at these values
4. IMP: 0.900 / 0.777 — broadly similar to gs=128
5. MPQ: 0.795 / 0.521 — benefits from lifetime reciprocity memory
6. MP: 0.708 / 0.039 — loses partner choice prematurely
7. P: 0.026 / 0.017 — effectively fails at gs=4 beyond c ≈ 0.08

## Summary

| Topic                          | Key finding                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| Payoff structure (PD)          | T = K+b = 0.90 fixed; R-P = b-c falls from 0.40 (c=0) to 0 (c=0.40)               |
| Payoff structure (snowdrift)   | S = K+b-c > P always; cooperation floor present without mechanisms                  |
| Control (\_ mechanism)         | qBSeen collapses to < 0.07 for c > 0 in PD; 0.96 in snowdrift at moderate c        |
| P mechanism threshold          | Sharp collapse at c = 0.34-0.36 (gs=128); c ≈ 0.08 at gs=4                         |
| Best mechanism (gs=128, PD)    | IJMPQ: 0.923 at c=0.32, 0.672 at c=0.40 — never collapses in tested range          |
| Shuffle effect on M            | M shuffle = control; M noshuffle = 0.915 at c=0.10, collapses at c=0.40            |
| P1 hitchhiking                 | P1 peaks at lower c than C1P1 in all pop structures (neutral C0P1 accumulation)    |
| Pop_2 symmetry breaking        | Stochastic; ΔqBSeen up to 0.56 at c=0.06; corr(Δq, Δw) = -0.984 (exploitation)   |
| Pop_2 IJMPQ                    | Symmetry breaking suppressed; ΔqBSeen < 0.010 through c = 0.38                    |
| Pop_3 transition               | Sharp collapse at c = 0.24-0.26; sharper than pop_2, earlier than pop_1            |
| Pop_3 crossover                | Evolving pop exploited at c < 0.18; exploits fixed pop at c > 0.20                 |
| Snowdrift (folder 2)           | All mechanisms near ceiling; IJMPQ = 0.960 even at c = 0.40                        |
| gs=4 P mechanism               | Collapses by c ≈ 0.08 — chooser bottleneck catastrophic in small groups            |
| gs=4 IJM reversal              | Weakest at gs=128 → near top at gs=4 (closed reputation pool favors indirect recip) |
| gs=4 M noshuffle               | Invariant to groupsize — stable pairings give sufficient history at any group size  |
