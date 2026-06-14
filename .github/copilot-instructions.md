# Copilot Instructions

## Repository Purpose

Documentation and analysis for interpreting TRPS evolutionary simulation outputs.

Current parameterization: K = 0.5, b = 0.4 fixed, c varies 0 to b. Analysis docs at repo root split by mechanism family: *_partner_choice.md (P), *_reciprocity.md (M, IM, IJM), *_combined.md (MP, MPQ, IMP, IJMPQ); hamilton.md and mutualism.md are indexes. Old docs in legacy/ (previous parameterization only).

## Repo Layout

- Keep human-facing analysis and reference docs at the repository root.
- Keep active Copilot instructions in .github/copilot-instructions.md.
- Put any additional agent-only support material under ai/ so it stays separate from the docs intended for human reading.
- legacy/ holds archived docs from the previous parameterization — do not edit or cite those as current.

## Related Repositories (same machine)

- ~/code/graph/graphgen/ (same as ../graph/graphgen/ from this repo) — figure pipeline, study manifests, mech_trait_map.csv. Run **graphgen** here to **regenerate** csv_*_for_image.con (final timestep) and csv_*_for_movie.con (multi-timestep) whenever those exports are missing from ~/results/.
- ../trps/ or ~/code/trps/ — C simulation source code
- ~/results/ — simulation output data

Paths like ../graph/graphgen/... are relative to this repo root.

### Running graphgen to generate .con summary files

graphgen generates the csv_*_for_image.con and csv_*_for_movie.con summary files as a side effect of figure generation. Run it from ~/code/graph/ with the virtualenv activated:

    cd ~/code/graph
    . .venv/bin/activate
    python -m graphgen.main --study STUDY --all --output /tmp/graphgen_out

Use --groupsize 4 or --groupsize 128 to target a specific groupsize (default is 128).
Use --movie to build csv_*_for_movie.con (temporal snapshots); without it, only csv_*_for_image.con (final timestep) are written.
Use --dilemma-type 0|1|2 to target dilemma folders other than the default (1); run once per dilemma type needed.
Use --clean to discard cached .con files and force a rebuild from raw .csv data.
Use --flat-output to write figures directly to --output without appending the study name (e.g. ~/figures/mutualism/pop_3 for mutualism_pop_3).

Examples:

    python -m graphgen.main --study hamilton --all --groupsize 128 --movie --output /tmp/graphgen_out
    python -m graphgen.main --study hamilton --all --groupsize 128 --dilemma-type 2 --movie --output /tmp/graphgen_out
    python -m graphgen.main --study mutualism --all --groupsize 4 --dilemma-type 0 --output /tmp/graphgen_out
    python -m graphgen.main --study mutualism_pop_3 --all --groupsize 128 --dilemma-type 1 --output ~/figures/mutualism/pop_3 --flat-output
    python -m graphgen.main --study prisoners --all --output /tmp/graphgen_out

### Missing summary exports policy (for AI agents)

- Before analysis, verify that required summary exports exist in the target results folder:
  - csv_*_for_image.con for final-state summaries
  - csv_*_for_movie.con for time-series summaries
- If required exports are missing, run graphgen as above before continuing interpretation.
- Treat missing *image.con or *movie.con summary files as a data-prep step, not an analysis failure.

## Architecture

### Study Status

**hamilton**: .con exports complete — gs=128 and gs=4, shuffle and noshuffle, dilemmas 0/1/2, all 9 mechanisms, pop_1/2/3 (image and movie). Analysis: hamilton_partner_choice.md (P), hamilton_reciprocity.md (M, IM, IJM), hamilton_combined.md (MP, MPQ, IMP, IJMPQ); gs=128 primary with dedicated gs=4 sections.

**mutualism**: .con exports complete — gs=128 and gs=4, shuffle and noshuffle, dilemmas 0/1/2, pop_2 only (image and movie). Mechanism coverage differs by shuffle setting: noshuffle has 7 mechanisms (_, M, P, MP, MPQ, IMP, IJMPQ); shuffle adds IM and IJM for 9. Analysis: mutualism_partner_choice.md (P), mutualism_reciprocity.md (M noshuffle; IM, IJM shuffle), mutualism_combined.md (MP, MPQ, IMP, IJMPQ); gs=128 noshuffle primary with dedicated gs=4 sections.

**mutualism pop_3**: raw simulation data present (441 cells per complete folder); .con caches build on first graphgen run. Study mutualism_pop_3 in graphgen renders a full 21×21 square grid (diagonal and lower triangle included). **Redundant with Hamilton pop_3 for interpretation** — see Mutualism Parameter Space below. Data incomplete: noshuffle gs=128 and gs=4 are complete for most mechanisms; shuffle conditions partial. Figures: ~/figures/mutualism/pop_3/ (use --flat-output).

**prisoners**: calibration study, re-run under the current engine (cost0.001, Runs=30) as a raw PD payoff-plane sweep — T=0.9 and S=0.1 fixed, R and P swept independently over an 18x18 grid (172 cells, T>R>P>S). Dilemma 1 (PD) only; symmetric payoffs; pops 1/2/3; shuffle and noshuffle. .con exports: gs=128 and gs=4 image (noshuffle 7 mechanisms, shuffle adds IM/IJM); gs=128 movie via prisoners_1run for temporal dynamics; gs=4 movie not yet generated. Cell key is (R0, P0), not c0/c1. Analysis: prisoners_calibration.md (payoff-axis attribution, gs=4 mirror of shuffle), prisoners_partner_choice.md (P), prisoners_reciprocity.md (M, IM, IJM). The old cost12/cost3 data are deprecated.

**snowdrift**: only single-run (snowdrift_1run, Runs=1) exists in the current parameterization — a snowdrift-ordered payoff sweep (T=0.9, P=0.10 fixed; R and S swept; T>R>S>P), dilemma 2. The multi-run snowdrift/ tree is empty (no 30-run .con), so no doc is written; generate multi-run snowdrift data before analyzing.

### Hamilton Parameter Space

Hamilton is a 1D sweep with **b = 0.4 (fixed)** and **c varying from 0 to b**. The x-axis is therefore c ∈ [0, 0.4]. The baseline fitness is **K = 0.5**.

Payoffs by dilemma type (folder names 0, 1, 2):

| Folder | Role         | T       | R           | P   | S           | Partner dependence                     |
| ------ | ------------ | ------- | ----------- | --- | ----------- | -------------------------------------- |
| 0      | Control (given=0) | K  | K + b - c   | K   | K + b - c   | None: T = P, R = S; partner irrelevant |
| 1      | PD           | K + b   | K + b - c   | K   | K - c       | b only when partner cooperates         |
| 2      | Snowdrift    | K + b   | K + b - c/2 | K   | K + b - c   | b shared whenever anyone cooperates    |

With K = 0.5, b = 0.4: P = 0.5 always. T = 0.5 (folder 0) or 0.9 (folders 1 and 2). R and S vary with c.

Folder 0 (old given=0.0) is a **control**, not a cooperative game: the dominant strategy when c < b is to produce b (cooperate → K + b − c). Partner moves do not enter payoffs, but M1 still induces suboptimal defection when a focal C1M1 copies a mutant partner at qBSeen = 0; C1M0 (always cooperate) avoids this. At d0 noshuffle, M1 under mechanism M (~0.39 mean) is ~0.10 below the dummy baseline under _ (~0.49); shuffle keeps both near 0.5.

In PD, b is a cross-benefit: focal receives it only when the partner cooperates (absent in S). In snowdrift, b is a shared resource: both players receive it as long as at least one cooperates (present in S as well as T and R).

### Mechanisms Available (hamilton)

| Mechanism folder | Active loci                      | Modules enabled                                                   |
| ---------------- | -------------------------------- | ----------------------------------------------------------------- |
| \_               | All 6 (only C expressed)         | None (control)                                                    |
| P                | C, P                             | Partner choice                                                    |
| M                | C, M                             | Direct reciprocity                                                |
| MP               | C, M, P                          | Reciprocity + partner choice                                      |
| MPQ              | C, M, P, Q                       | Reciprocity + partner choice (recent + lifetime)                  |
| IM               | C, I, M                          | Direct + indirect reciprocity (recent)                            |
| IJM              | C, I, J, M                       | Direct + indirect reciprocity (recent + lifetime)                 |
| IMP              | C, I, M, P                       | All three                                                         |
| IJMPQ            | All 6                            | All three, with lifetime variants                                 |

Mechanisms _ and M are run for all three dilemma folders (0, 1, 2). All other mechanisms are run for folders 1 and 2 only.

### Mutualism Parameter Space

Mutualism is a 2D sweep over c0 and c1 with b = 0.4 fixed, K = 0.5.

**pop_2** (study mutualism): strict upper triangle only — c0 ∈ [0, 0.38], c1 ∈ [0.02, 0.40] with c0 < c1 always (210 cells). Heatmaps mask the diagonal (c0 = c1). The role split is deterministic: since c0 < c1 always, pop_0 has higher R−P and cooperates more in every cell for every mechanism tested.

**pop_3** (study mutualism_pop_3): full 21×21 square — all c0, c1 pairs including diagonal and lower triangle (441 cells). One evolving population (_0) vs one fixed population (_1, 25% each genotype). Reads from the same ~/results/mutualism/ tree (results_name=mutualism). Theory overlays (s04) deferred.

**mutualism pop_3 vs Hamilton pop_3 (redundant for interpretation).** The 441-cell square re-simulates what Hamilton pop_3 already captures in a 1D c sweep. Use Hamilton pop_3 for figures and analysis; mutualism_pop_3 heatmaps add little beyond noise.

| Quantity | mutualism pop_3 (c0, c1) | Hamilton pop_3 (c = c0 = c1) |
| -------- | ------------------------ | ---------------------------- |
| Evolving _0 qBSeen / wmean | Depends on c0 only; identical across c1 at fixed c0 (matches Hamilton at c = c0 to ~0.003) | 1D sweep — same story |
| Fixed _1 qBSeen | Flat ~0.50 (genotypes frozen) | Flat ~0.50 |
| Fixed _1 raw wmean | w ≈ a(c0) + b(c1) (max residual ~0.005); each c1 row is the same c0 pattern shifted; c1 effect damped because only 50% (C1 genotypes) pay c1 | Diagonal slice where c0 = c1 |

Figure layout (mutualism_pop_3): top row = evolving _0, bottom row = fixed _1. The top row shows vertical c0 bands only. The bottom row shows the same c0 bands with a modest vertical (c1) offset — easy to miss if the rows are swapped mentally.

pop_2 remains the non-redundant mutualism case: both populations evolve and c0 ≠ c1 cells are essential (210-cell upper triangle).

### Mechanisms Available (mutualism)

| Mechanism folder | Active loci      | Modules enabled                                  | Conditions          |
| ---------------- | ---------------- | ------------------------------------------------ | ------------------- |
| \_               | All 6            | None (control)                                   | shuffle + noshuffle |
| M                | C, M             | Direct reciprocity                               | shuffle + noshuffle |
| P                | C, P             | Partner choice                                   | shuffle + noshuffle |
| MP               | C, M, P          | Reciprocity + partner choice                     | shuffle + noshuffle |
| MPQ              | C, M, P, Q       | Reciprocity + partner choice (recent + lifetime) | shuffle + noshuffle |
| IMP              | C, I, M, P       | All three                                        | shuffle + noshuffle |
| IJMPQ            | All 6            | All three, with lifetime variants                | shuffle + noshuffle |
| IM               | C, I, M          | Direct + indirect reciprocity (recent)           | shuffle only        |
| IJM              | C, I, J, M       | Direct + indirect reciprocity (recent + lifetime)| shuffle only        |

The 7 base mechanisms are run for all three dilemma folders (0, 1, 2) under both shuffle and noshuffle_cost0.001_128. IM and IJM are present only under the shuffle conditions (gs=128 and gs=4).



### AI Writing Rule

- Do not use backticks in Markdown documentation.

### Markdown Table Formatting

When editing Markdown tables, keep raw-source alignment readable in plain text editors (especially Vim with conceal enabled):

- Treat *, **, and backticks as formatting markers, not visible cell content.
- Treat escape backslashes (for example in \_) as visible characters for raw-source alignment unless your editor conceal settings explicitly hide them.
- Pad cells based on the **visible rendered text width**, not raw character count including formatting markers.
- Keep each column width consistent across header, separator, and body rows.
- Prefer simple ASCII separators in table text (- vs −) when alignment is sensitive.
- After editing a table, quickly re-check the raw Markdown in a monospaced editor to confirm columns still line up.

### Data File Layout

Results live at ~/results/{study}/{shuffle}_cost{cost}_{groupsize}/{mechanism}/{dilemma}/{population}/:

- **dilemma**: 0 (control, given=0), 1 (PD), 2 (snowdrift)
- **shuffle**: shuffle or noshuffle
- **cost**: per-module locus-expression cost (currently 0.001), distinct from MutationRate (0.01). Charged every round as globals->cost * ((Choose||Choose_lt) + (Mimic||Imimic||Imimic_lt)) — i.e. 0.001 for expressing any partner-choice locus plus 0.001 for expressing any reciprocity locus (max 0.002). See decide_qB.c / recruits.c.
- **groupsize**: 128 or 4

Example: ~/results/hamilton/shuffle_cost0.001_128/P/1/pop_2/csv_0_for_image.con

| File                  | Contents                                                         |
| --------------------- | ---------------------------------------------------------------- |
| csv_0_for_image.con | Final-timestep data, file_set _0 (one row per parameter cell)    |
| csv_1_for_image.con | Final-timestep data, file_set _1                                 |
| csv_0_for_movie.con | Multi-timestep data, _0 (snapshots from t=1 to t=1048576)        |
| csv_1_for_movie.con | Multi-timestep data, _1                                          |

### Data Format

All studies use **64 genotypes** from **6 loci** (C, I, J, M, P, Q):
- Genotype columns: C0I0J0M0P0Q0 through C1I1J1M1P1Q1 (alphabetical)
- No pre-computed derived trait columns — compute everything from genotypes
- Game parameter columns for hamilton/mutualism: **c0, c1** (cost for each population)

### Computing Derived Traits from Genotypes

Always sum genotypes to get allele frequencies:

python
c1p1_cols = [c for c in df.columns if c.startswith('C1') and 'P1' in c and not c.endswith('SD')]
c0p1_cols = [c for c in df.columns if c.startswith('C0') and 'P1' in c and not c.endswith('SD')]
c1p0_cols = [c for c in df.columns if c.startswith('C1') and 'P0' in c and not c.endswith('SD')]

df['C1P1'] = df[c1p1_cols].sum(axis=1)  # cooperators who choose (P1 active)
df['C0P1'] = df[c0p1_cols].sum(axis=1)  # defectors carrying P1 (P1 silent)
df['C1P0'] = df[c1p0_cols].sum(axis=1)  # cooperators who don't choose
df['P1']   = df['C1P1'] + df['C0P1']    # total P1 allele frequency


Full mechanism → trait mapping: ../graph/graphgen/studies/trps/mech_trait_map.csv

### The C0P1 Silencing Rule

**P1 is phenotypically silent in defectors.** A C0P1 individual carries the partner-choice allele but never uses it. Only C1P1 individuals actually choose partners. This means:
- P1 allele frequency ≠ fraction of choosers
- C0P1 accumulates as a neutral carrier via mutation from C1P1, inflating P1 frequency in the transition zone
- Always use C1P1 (= Choosers) for behavioral analysis, P1 only for genetic analysis

### M locus: dTFT vs dSTFT (C0M1 is not silent)

For mechanism M, graphgen splits genotypes into **dTFT** (C1M1: cooperate by default, then copy partner) and **dSTFT** (C0M1: suspicious TFT — defect on the first round with a partner, then mimic the partner on later rounds with the same oldpartner). C0M1 is **not** a silent carrier unlike C0P1: mimicry is active once age > 0 and partner == oldpartner (see decide_qB.c). M1 allele frequency = dTFT + dSTFT. At folder 0 (given=0), produce-b is dominant; M1 is slightly selected against because C1M1 can copy a mutant defector and forgo b, while C1M0 always cooperates.

### File Set _0/_1 Semantics

| Study              | _0                        | _1                                          |
| ------------------ | ------------------------- | ------------------------------------------- |
| hamilton (pop_2)   | Higher qBSeen             | Lower qBSeen                                |
| hamilton (pop_3)   | Evolving population       | Fixed population (25% each genotype)        |
| mutualism (pop_2)  | Lower-cost pop (c0)       | Higher-cost pop (c1)                        |
| mutualism (pop_3)  | Evolving population       | Fixed population (25% each genotype)        |

### Population Scenario Semantics

- **pop_1**: Single population; individuals pair within the same population
- **pop_2**: Two coevolving populations; all pairing is **between** populations (128 from each per group)
- **pop_3**: One evolving + one fixed; file_set _1 is held at 25% each of C0P0/C0P1/C1P0/C1P1

### Partner Choice Bottleneck

Swaps require C1P1 on **both** sides. The code **mutually** rematches two choosers: each trades a C0 partner for partnership with the **other** C1P1 (not an undirected "abandonment" to a random C1). The two defectors end up paired with each other. When such chooser pairs are rare, swap opportunities are scarce — this creates a positive feedback threshold.

### Group Structure (shuffle)

Groups are fixed memory segments — individuals never move between groups across the simulation. shuffle_partners only redraws pairings within the same fixed group each round. At gs=4 the same 4 individuals share a group for their entire lifetime; at gs=128, the same 128.

The Imimic locus (I, indirect reciprocity recent) copies partner->qBSeen — what the partner did in their previous round with their previous partner (a third party). This IS indirect reciprocity: the focal individual uses reputation information about their new partner's behavior toward someone else. The J locus (Imimic_lt) copies round(partner->qBSeen_lt), the partner's lifetime cooperation average. The Mimic locus (M) by contrast only copies partner->qBSeen when partner == oldpartner — direct reciprocity, no third-party observation.

Groupsize effect on indirect reciprocity: at gs=4 the group is a small closed system of 4 fixed individuals. Reputation signals circulate within this tight pool — cooperation propagates reliably because every signal comes from someone the focal individual also interacts with. At gs=128 the fixed group has 128 members of mixed strategy; defectors produce many qBSeen=0 signals that disrupt the cascade for whoever pairs with them next. Small groups make indirect reciprocity more effective because the reputation signals are more relevant (they concern the same few individuals) and defector signals are less prevalent.



In mutualism **PD** (dilemma 1), cooperation delivers benefit b to the partner (cross-benefit: b appears in T and R but not S). The focal individual pays own cost c. So:
- Pop 0's R−P = b − c0 (receives partner's b, pays c0)
- Pop 1's R−P = b − c1 (receives partner's b, pays c1)

In mutualism **snowdrift** (dilemma 2), b is a shared resource received by both players whenever at least one cooperates (b present in T, R, and S). The cost c is paid by whoever cooperates (split if both cooperate).

In both cases b is fixed and equal for both populations, so the asymmetry between populations is entirely in cost: c1 > c0 by construction, giving pop 0 the higher cooperation incentive.

## Figure Pipeline (graphgen)

Figures are generated by ../graph/graphgen/studies/{study}/manifest.py. Key files:
- ../graph/graphgen/studies/{study}/manifest.py — MAIN_ROWS defines panel layout (row → population, file_set, trait, renderer)
- ../graph/graphgen/studies/mutualism_pop_3/manifest.py — pop_3 full-square grid (reindex_full_square_matrix; no s04 theory)
- ../graph/graphgen/studies/trps/config.py — shared trait definitions
- ../graph/graphgen/studies/common/shared.py — common path template

Renderers: imshow for heatmaps (prisoners/mutualism), plot for line plots (hamilton).
