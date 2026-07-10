# Prisoner's Dilemma

Calibration study analysis for the raw PD payoff-plane sweep. Unlike diagonal
and mutualism (which derive payoffs from a single cost c), prisoners fixes
T = 0.90 and S = 0.10 and sweeps R and P independently over an 18 × 18 grid
(172 cells with T > R > P > S). This decouples temptation (T − R), risk
(P − S), and the cooperation advantage (R − P), which diagonal welds onto one
axis — letting us attribute each mechanism's behavior to a specific payoff
gap.

The main analysis here is the dilemma 1 (PD) payoff plane; a no-social-
dilemma control rerun (folder 0) now also exists for the dummy control
mechanism \_. Payoffs are symmetric across populations; pops 1/2/3; shuffle
and noshuffle; gs = 128 and gs = 4 (movie exports available for temporal
dynamics at both groupsizes); 30 runs per cell in the
multi-run sweep.

- **[prisoners_calibration.md](prisoners_calibration.md)** — cross-mechanism
  payoff-axis attribution (which gap limits each mechanism), the shuffle
  decomposition, and cross-checks against symmetric_c/asymmetric_c0_c1
- **[prisoners_partner_choice.md](prisoners_partner_choice.md)** — mechanism P:
  cooperation collapses onto R − P, genotype hitchhiking, pop_2 symmetry
  breaking, pop_3
- **[prisoners_reciprocity.md](prisoners_reciprocity.md)** — mechanisms M, IM,
  IJM: M is risk-limited (sensitive to P), shuffle kills M, indirect
  reciprocity recovers it

For how these payoff-axis attributions map back onto the diagonal and mutualism
thresholds, see **[synthesis.md](synthesis.md)**.

## Headline result

Each mechanism is governed by a different payoff axis — invisible in diagonal,
where R and P move together:

| Mechanism family | Limiting payoff axis        | Reading for symmetric_c/asymmetric_c0_c1                   |
| ---------------- | --------------------------- | ------------------------------------------------ |
| M                | risk / defection payoff P   | the c-collapse of M is mostly a rising-risk effect |
| P                | cooperation advantage R − P | the chooser bottleneck is set by R − P            |
| MP, MPQ, IMP, IJMPQ | reward / temptation R    | reputation removes M's risk sensitivity           |

## Replicates and noise floor

Every value here is a mean over 30 independent runs (Runs = 30 in the .glo
metadata). The csv_*_for_image.con files carry a companion SD column per
statistic (qBSeenSD, wmeanSD, …); the standard error of a cell mean is SD / √30.

Typical noise floor (gs = 128, pop_1, noshuffle): median qBSeenSD ≈ 0.002
(control) to 0.016 (M), i.e. SE ≈ 0.0004–0.003; median wmeanSD ≈ 0.001
(control) to 0.005 (M), i.e. SE ≈ 0.0002–0.001. SD spikes in transition cells
where R ≈ P (max qBSeenSD ≈ 0.40 for M), where individual runs split between a
cooperative and a collapsed fixed point — multi-run means there reflect a mix
of bistable outcomes rather than a single equilibrium. Bistability is localized,
though: only 6 of the 172 M cells (pop_1, noshuffle) have qBSeenSD > 0.1, so
almost every cited mean sits on a single stable equilibrium.

Practical reading guide: per-cell qBSeen gaps below ~0.01–0.02 are within
run-to-run noise. The payoff-axis −b/a ratios and mean-qBSeen figures are
fitted/averaged over all 172 cells, so they are far tighter than any single
cell; treat −b/a differences below ~0.03 as not meaningful.

## Role in this project

Prisoners is an auxiliary calibration study used to interpret mechanism
signatures seen in **asymmetric_c0_c1** and **symmetric_c**, not a primary biological
endpoint. Earlier write-ups under the previous parameterization (K = 2, c = 1
fixed) are superseded by these documents and are not part of the current
K = 0.5, b = 0.4 study.
