# Project Framing and Modeling Justification

## Purpose

This note states the biological and methodological rationale for the study hierarchy used in this repository.

## Core framing

- **Primary object**: `mutualism`
- **Special case**: `hamilton` as the diagonal slice of mutualism (`b0 - c0 = b1 - c1`)
- **Calibration studies**: `prisoners` and `snowdrift` as auxiliary comparisons used to interpret mechanism signatures, not as primary biological endpoints

## Biological rationale

The project concerns mutualistic interactions between two species. In real systems, there is no strong biological reason to assume both species share identical payoff parameters. Asymmetry in costs, benefits, and ecological context is expected.

For that reason, the most biologically relevant model is the asymmetric two-population formulation (`mutualism`), where species can differ in net benefit terms.

The Hamilton setup remains essential, but as a controlled reference: it is the symmetric/equal-parameter slice of the same conceptual space. This makes Hamilton useful for diagnosing core dynamics before adding biologically expected asymmetry.

## Why parameterize mutualism via b and c

In the mutualism branch, payoffs are written through biologically interpretable quantities (`b`, `c`, and related derived terms), which constrains the implied `T, R, P, S` combinations.

This restriction is intentional and desirable:

1. It keeps the model tied to biologically interpretable mechanisms instead of arbitrary independent payoff entries.
2. It defines a structured subset of game space that can be analyzed causally and compared across populations.
3. It avoids an intractable parameter explosion for two asymmetric species.

## Tractability argument

Allowing a wide independent sweep of `T, R, P, S` for **each** of two asymmetric populations would create a very high-dimensional space. Even if computationally feasible, interpretation would be difficult because:

- many parameter combinations would be weakly constrained biologically,
- causal signatures would be harder to isolate,
- cross-population comparisons would become less transparent.

So the project uses a principled reduction:

- **Main analysis** on a biologically grounded, constrained manifold (`mutualism`, with Hamilton as its diagonal),
- **Auxiliary calibration** from broader game families (`prisoners`, `snowdrift`) to identify which observed signatures are mechanism-general versus payoff-structure-specific.

## Interpretation value of calibration studies

`prisoners` and `snowdrift` are not treated as direct biological targets for this project. Their role is to stress-test interpretation logic:

- partner-choice bottlenecks,
- exploitation asymmetries,
- chooser/hitchhiking genotype patterns,
- transition shape differences across payoff families.

If a pattern appears in both calibration studies and in mutualism, confidence increases that the pattern reflects robust mechanism behavior. If it appears only in certain game families, that helps identify payoff-structure dependence.

## Cross-g mapping note

The interpretation docs now include an explicit regime map across `given` folders:

- see `mutualism.md` (`Regime map across given folders`)
- see `hamilton.md` (`Regime map across given folders`)

Operationally in this repository:

- `given = 1.0` is the main PD-family readout,
- `given = 0.5` is a mixed PD/harmony diagnostic regime,
- `given = 1.5` is used as the snowdrift-branch folder/branch marker (`given >= 1.5`), not as the same biological meaning of `g` used in the Hamilton-benefit branch.

## Summary statement

The study design is intentionally hierarchical:

- biologically central inference comes from asymmetric `mutualism`,
- `hamilton` provides the symmetric reference slice,
- `prisoners` and `snowdrift` provide comparative calibration.

This achieves a practical balance between biological realism, computational tractability, and interpretability.
