# Interpretation of Snowdrift Partner Choice Results

## Overview

This document summarizes the current `snowdrift` study outputs generated via:

- `python -m graphgen.main --study snowdrift --figure s07`

Focus here is mechanism `P` at `shuffle_cost12_128`, using the finalized summary exports in `~/results/snowdrift/.../csv_*_for_image.con`.

Role in this project: **snowdrift is a calibration study**, not the primary object. It is used to benchmark which partner-choice patterns generalize across game families when interpreting **mutualism** (main target) and **Hamilton** (equal-parameter special case within mutualism).

## Payoff Structure in Exported Data

The generated snowdrift dataset used here has:

- `T = 1.0` (constant)
- `P = 0.1` (constant)
- `R` and `S` varying over valid cells with `T > R > S > P`

In the `pop_1` export, all 210 cells satisfy `T > R > S > P`. The observed ranges are:

- `R`: 0.182 to 0.959
- `S`: 0.141 to 0.918

So this study behaves as a snowdrift/Hawk-Dove ordering sweep (not the PD ordering `T > R > P > S`).

## Baseline vs Partner Choice

Control mechanism (`_`) already sustains substantial cooperation in this game family:

- `pop_1` mean `qBSeen`: 0.491
- `pop_2` mean `qBSeen` (averaged across both file sets): 0.520
- `pop_3` evolving mean `qBSeen`: 0.496

With mechanism `P`, cooperation increases strongly above that baseline:

- `pop_1`: mean `qBSeen` = 0.947 (min 0.576, max 0.977)
- `pop_2` higher-cooperation file set (`_0`): mean `qBSeen` = 0.983
- `pop_3` evolving (`_0`): mean `qBSeen` = 0.813

## Population-Specific Conclusions

### pop_1 (single population)

- Cooperation is high across the full grid (`qBSeen` 0.576-0.977), with no defection basin.
- `qBSeen` increases with `R` (corr 0.73) and decreases with `T-R` (corr -0.73).
- At the weakest payoff cell (`R=0.182`, `S=0.141`), cooperation remains substantial (`qBSeen=0.576`).

Interpretation: in this snowdrift ordering, cooperation is already favorable enough that partner choice amplifies an already cooperative baseline rather than creating a sharp invasion threshold.

### pop_2 (two coevolving populations; file sets sorted by cooperation)

- `csv_0` is near-all cooperation (`qBSeen` mean 0.983, min 0.961).
- `csv_1` is mostly low-cooperation (`qBSeen` mean 0.065, min 0.012, max 0.263).
- Fitness is strongly asymmetric: `wmean_0 - wmean_1` mean = -0.555 (the more cooperative side has lower fitness).

Representative extreme:

- `R=0.182`, `S=0.141`: `qBSeen_0=0.961`, `qBSeen_1=0.241`, `wmean_0=0.140`, `wmean_1=0.976` (fitness ratio ~6.99x).

Interpretation: as in Hamilton/prisoners, the high-cooperation side is exploited by defectors on the opposite side, but snowdrift payoffs make this asymmetry persist even where cooperation remains high.

### pop_3 (evolving vs fixed)

- Evolving population (`_0`) mean `qBSeen` = 0.813 (range 0.014-0.985).
- Fixed population (`_1`) remains at ~0.5 cooperation by construction.
- Evolving side is more cooperative than fixed in 82.9% of cells, but fitter than fixed in only 18.1% of cells.

Interpretation: partner choice raises cooperation in the evolving population across most of the grid, but higher cooperation often carries a fitness cost when paired against a mixed fixed partner pool.

## P1 vs Chooser Dynamics (Hitchhiking Pattern)

The same separation seen in other studies appears here:

- `P1` peaks before `C1P1` in payoff-gap space.

For `pop_1`:

- `P1` max: 0.858 at `R=0.223`, `S=0.141` (`R-S=0.082`)
- `C1P1` max: 0.764 at `R=0.305`, `S=0.141` (`R-S=0.164`)

For `pop_3` evolving:

- `P1` max: 0.846 at `R=0.509`, `S=0.141` (`R-S=0.368`)
- `C1P1` max: 0.730 at `R=0.550`, `S=0.141` (`R-S=0.409`)

Interpretation: neutral `C0P1` carriers still inflate total `P1` in the transition region, so the allele peak occurs earlier than the active chooser peak.

## Final Conclusion

The updated snowdrift data supports a stable interpretation:

1. Snowdrift payoffs (`T > R > S > P`) produce a cooperative baseline even without partner choice.
2. Partner choice (`P`) significantly amplifies cooperation in all population scenarios.
3. Cross-population settings still show strong exploitation asymmetry: more cooperation does not imply higher fitness.
4. The `P1`-vs-`C1P1` offset remains robust, consistent with neutral carriage of `P1` in defectors.
