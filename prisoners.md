# Prisoner's Dilemma

Calibration study analysis for the raw PD payoff-plane sweep. Unlike hamilton
and mutualism (which derive payoffs from a single cost c), prisoners fixes
T = 0.90 and S = 0.10 and sweeps R and P independently over an 18 × 18 grid
(172 cells with T > R > P > S). This decouples temptation (T − R), risk
(P − S), and the cooperation advantage (R − P), which hamilton welds onto one
axis — letting us attribute each mechanism's behavior to a specific payoff
gap.

Dilemma 1 (PD) only; payoffs symmetric across populations; pops 1/2/3;
shuffle and noshuffle; gs = 128 and gs = 4 (gs = 128 movie exports available
for temporal dynamics; gs = 4 movie not yet generated); 30 runs per cell.

- **[prisoners_calibration.md](prisoners_calibration.md)** — cross-mechanism
  payoff-axis attribution (which gap limits each mechanism), the shuffle
  decomposition, and cross-checks against hamilton/mutualism
- **[prisoners_partner_choice.md](prisoners_partner_choice.md)** — mechanism P:
  cooperation collapses onto R − P, genotype hitchhiking, pop_2 symmetry
  breaking, pop_3
- **[prisoners_reciprocity.md](prisoners_reciprocity.md)** — mechanisms M, IM,
  IJM: M is risk-limited (sensitive to P), shuffle kills M, indirect
  reciprocity recovers it

## Headline result

Each mechanism is governed by a different payoff axis — invisible in hamilton,
where R and P move together:

| Mechanism family | Limiting payoff axis        | Reading for hamilton/mutualism                   |
| ---------------- | --------------------------- | ------------------------------------------------ |
| M                | risk / defection payoff P   | the c-collapse of M is mostly a rising-risk effect |
| P                | cooperation advantage R − P | the chooser bottleneck is set by R − P            |
| MP, MPQ, IMP, IJMPQ | reward / temptation R    | reputation removes M's risk sensitivity           |

## Role in this project

Prisoners is an auxiliary calibration study used to interpret mechanism
signatures seen in **mutualism** and **hamilton**, not a primary biological
endpoint. Earlier write-ups under the previous parameterization (K = 2, c = 1
fixed) are superseded by these documents; the deprecated cost12/cost3 data are
not part of the current K = 0.5, b = 0.4 study.
