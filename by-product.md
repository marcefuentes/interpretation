# By-product Mutualism: Transformations from Dilemma Games

This document explores the biological and game-theoretic transformation of standard dilemmas (Prisoner's Dilemma and Snowdrift) into non-dilemma regimes by varying the cost parameter $c$ into the negative range ($c < 0$).

## 1. From Prisoner's Dilemma (PD)

In a standard PD, payoffs are defined as:
- **T** (Temptation) = $b$
- **R** (Reward) = $b - c$
- **P** (Punishment) = $0$
- **S** (Sucker) = $-c$

Where $b > c > 0$. The ordering is $T > R > P > S$. Natural selection favors defectors.

### Transformation ($c < 0$)
When the cost of cooperation becomes negative, the act of "cooperating" provides a direct, private benefit to the actor. Let $v = |c|$ represent this private benefit.

The payoffs become:
- **R** = $b + v$ (Get group benefit + private benefit)
- **T** = $b$ (Get group benefit only)
- **S** = $v$ (Get private benefit only)
- **P** = $0$ (Get nothing)

**New Ordering:** $R > T > S > P$.
Cooperation becomes the dominant strategy because $R > T$ and $S > P$. There is no conflict between individual and collective interest.

### Biological Examples for $c < 0$ in PD
- **Feeding while Hunting:** A predator that hunts for its group (providing $b$) also consumes small scraps or high-energy organs during the kill that aren't easily shared. The private nutrition gained ($v$) exceeds the caloric cost of the hunt.
- **Waste Removal as Consumption:** In mutualisms where one species "cleans" another (e.g., cleaner fish), the "cost" is the time spent cleaning. If the parasites removed are a primary and high-quality food source, the cost is negative. The cleaner benefits directly from the act of providing the service.

---

## 2. From Snowdrift Game

In the Snowdrift game (Hawk-Dove), the effort $c$ is shared if both players cooperate:
- **T** = $b$
- **R** (Shared Work) = $b - c/2$
- **P** = $0$
- **S** (Unshared Work) = $b - c$

Where $b > c > 0$. The ordering is $T > R > S > P$. This is a dilemma of coordination; individuals prefer to defect if the partner cooperates, but prefer to cooperate if the partner defects.

### Transformation ($c < 0$)
As with the PD, let $v = |c|$ be the private profit of performing the task.

The payoffs become:
- **S** = $b + v$ (Group benefit + full private profit)
- **R** = $b + v/2$ (Group benefit + half private profit)
- **T** = $b$ (Group benefit only)
- **P** = $0$ (Nothing)

**New Ordering:** $S > R > T > P$.
Cooperation is not only the dominant strategy, but the player **prefers to be the sole worker**. Sharing the task ($R$) is actually less desirable than doing it alone ($S$) because the private profit $v$ is diluted by the partner's participation.

### Biological Examples for $c < 0$ in Snowdrift
- **Foraging with "Skimming":** Two animals digging for a shared food patch. If the act of digging uncovers "choice bits" (e.g., larvae) that the digger eats immediately, the digger gains a private profit. If both dig, they must split these immediate finds. The digger would prefer the partner stood back so they could keep all the "skimmings."
- **Parental Care as Training:** A parent hunting to feed offspring. If hunting also serves as necessary physical conditioning or skill-building for the parent, the parent gains a private fitness boost. If the parents share the hunting, each gets less "exercise" or "practice" than if one did it all.
### Why this regime is excluded from social mechanism simulations
In the $c < 0$ Snowdrift regime, the "dilemma" is not just solved; it is inverted. Because $S > R$, the incentives for social evolution change fundamentally:
- **Disassortative Partner Choice:** Natural selection would favor cooperators who seek out *defectors* to avoid the dilution of private profit. This is the opposite of the assortative partner choice (Mechanism P) studied in this project.
- **Anti-Reciprocity:** The optimal strategy is to do the opposite of the partner. "Reciprocity" in the standard sense (imitation) would be maladaptive.

Consequently, this regime is excluded from the active simulation sweep, as it would obscure the social-contract dynamics (partner choice and reciprocity) that the project aims to investigate.

## 3. Asymmetric Prisoner's Dilemma with $c < 0$

When two different species interact (asymmetric payoffs), one population may transition into by-product mutualism ($c < 0$) while the other remains in a standard dilemma ($c > 0$).

### The Scenario
- **Species 1 (By-product Cooperator):** Has $c_1 < 0$. Cooperation is the dominant strategy ($R_1 > T_1$ and $S_1 > P_1$).
- **Species 0 (Standard Dilemma):** Has $c_0 > 0$. Defection is the dominant strategy ($T_0 > R_0$ and $P_0 > S_0$).

### Stable Outcome: The "One-Way Benefit"
In this interaction, Species 1 will evolve to 100% cooperation because it is personally profitable to perform the action. Species 0, seeing a world of reliable cooperators, will evolve to 100% defection to maximize its own payoff ($T_0$).

The result is a stable, asymmetric equilibrium where:
- **Species 1 is an "Obligate Provider."**
- **Species 0 is a "Stable Scrounger."**

Unlike the Snowdrift case, Species 1 still *prefers* that Species 0 cooperates ($R_1 > T_1$), but since cooperation is dominant for Species 1 anyway, it cannot "threaten" to defect to force Species 0 into cooperation.

### Biological Example: The Hunter and the Scavenger
Consider a relationship where Species 1 (the Hunter) kills large prey. The act of hunting provides a private benefit (e.g., immediate access to high-energy organs) that makes $c < 0$. Species 0 (the Scavenger) follows the hunter and consumes the remains.
- The Hunter "cooperates" by killing the prey, which provides $b_1$ to the scavenger.
- The Scavenger "defects" by never helping with the kill (providing no $b_0$ to the hunter).
- This is stable because the Hunter would hunt even if the Scavenger wasn't there, and the Scavenger gains more by waiting than by risking injury in the hunt.

## 4. Biological Case Study: Plant-Pollinator Asymmetry

The plant-pollinator interaction provides a classic example of stable, asymmetric investment where one side is in a dilemma ($c > 0$) while the other acts as a by-product cooperator ($c \approx 0$).

### The Plant (Species 0): The High-Cost Investor
Plants often evolve extreme "cooperative" traits:
- **High Cost ($c_0$):** Production of large quantities of nectar, complex fragrances, and large, colorful petals.
- **Goal:** To ensure the benefit provided to the partner ($b_0$) is high enough that visiting the flower is always the pollinator's best response.
- **The Dilemma:** The plant would be fitter if it could get pollination without paying the cost of nectar (mimicry/cheating), but this is rarely stable at high densities.

### The Pollinator (Species 1): The Zero-Cost Provider
In contrast, pollinators often do "nothing" to foster the benefit they provide:
- **Zero Cost ($c_1 \approx 0$):** The transport of pollen ($b_1$) is often an incidental by-product. If the pollen sticks to the pollinator's head or legs automatically while it drinks, the pollinator pays no additional energy cost to provide the service.
- **The By-product:** The pollinator is not "trying" to help the plant; it is trying to feed. The pollination is a stable by-product of its own selfish activity.

### The Evolution of Asymmetry
This leads to a "ratchet effect" of investment:
1. The **Plant** evolves increasingly higher $c_0$ and $b_0$ to attract pollinators in a competitive market.
2. The **Pollinator** keeps $c_1$ at a minimum and evolves no mechanism to increase $b_1$ (pollen delivery), as it gains no direct fitness from the plant's reproduction beyond ensuring the plant doesn't go extinct.

**## 5. Simulation Strategy: The $c$-Sweep

While conceptually similar to varying $b$ with a fixed $c$, the current simulations in this project utilize a fixed benefit $b$ and vary the cost $c$ from $0$ to $b$. This approach is more biologically intuitive for studying investment effort.

### Parameterization Advantages
- **Fixed Potential:** By fixing $b$, the maximum possible benefit in the system is bounded, avoiding "exploding" fitness values.
- **Investment Effort:** The focus shifts to how much of the potential benefit is "eaten up" by the metabolic cost of providing it.
- **Clean Boundaries:** The transition to By-product Mutualism occurs precisely as $c \to 0$.

### Application across Game Families
- **Hamilton:** Symmetric investment ($c_0 = c_1$). Tests the limits of cooperation as the metabolic burden increases equally for both species.
- **Mutualism (Asymmetric PD):** Differing costs ($c_0 \neq c_1$). Represents "Service for Service" where one side's investment may be significantly cheaper than the other's (e.g., Pollinator vs. Plant).
- **Snowdrift:** Differing costs ($c_0 \neq c_1$). Represents "Shared Tasks" where the cost determines the necessity of coordination versus the stability of one-way provision.

### Exclusion of $c < 0$
In these new sweeps, the range is strictly $0 \leq c \leq b$. While $c < 0$ is theoretically interesting as a non-dilemma regime (as documented in sections 1-3), it is excluded from the active simulations to maintain focus on the social mechanisms (partner choice and reciprocity) that emerge only when cooperation remains a costly dilemma.
