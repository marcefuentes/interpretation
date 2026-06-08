I have changed all hamilton and mutualism simulation data. Now we have K = 0.5 and b = 0.4. b is fixed. c varies from 0 to b

Hamilton/mutualism pd: T = K + b, R = K + b - c, P = K, S = K - c
Hamilton/mutualism sd: T = K + b, R = K + b - c/2, P = K, S = K + b - c

The legacy folder has interpretations of deprecated data using different values of b and c. It may provide a blueprint for your analysis, but don't let it pollute your thinking.

As you see, I have completely dropped "given". Folders in results are now named 0, 1, and 2 instead of 0.0, 0.5, 1.0, and 1.5:

- **0** (old given=0.0) — control: T = P, R = S; partner behavior does not affect focal payoffs; interactive cooperation is not in the game
- **1** (old given=1.0, PD family) — prisoner's dilemma: T = K + b, R = K + b − c, P = K, S = K − c
- **2** (old given=1.5, snowdrift branch) — snowdrift: T = K + b, R = K + b − c/2, P = K, S = K + b − c

The old given=0.5 mixed regime is not carried forward as a separate folder.
