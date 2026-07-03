# Figure Manifest

Specification and provenance for the manuscript figures. **No image binaries live in
this repo** — figures are generated artifacts. This manifest records, per planned
figure, what it shows, the exact graphgen command that produces it, where the output
lands, a draft caption, and the journal doc backing it, so the figure set is fully
reproducible from text.

Regenerate any figure from `~/code/graph` with the venv active:

```bash
cd ~/code/graph && . .venv/bin/activate
python -m graphgen.main --study STUDY --figure FIG --groupsize 128 --output ~/figures
```

Flags: `--figure main1` (single) or `--all`; `--dilemma-type 0|1|2` (default 1);
`--groupsize 4|128` (default 128); `--movie` for the temporal MP4; `--flat-output`
to skip appending the study name. Default output root is `~/figures/<study>/`.
graphgen figure ids (from `../graph/graphgen/studies/trps/config.py`): main1 = P,
main3 = M, main5 = IM (indirect), main6 = control fitness deficit, main7 = IJMPQ;
supplementary s04/s06/s07/s12/s19/s26/s35/s36.

Status: provisional selection — the final figure set is not fixed. Rows marked
(candidate) are plausible manuscript figures; adjust as the paper firms up.

## Results 1 — level of cooperation and what limits it

| Fig | Message | graphgen command | Output | Journal backing |
| --- | ------- | ---------------- | ------ | --------------- |
| 1 (candidate) | Payoff-axis attribution: each mechanism's c-collapse maps to temptation / risk / R−P | `--study prisoners --figure main1 --groupsize 128` and `--figure main3` | `~/figures/prisoners/` | prisoners_calibration.md, synthesis.md |
| 2 (candidate) | Cooperation vs c per mechanism (hamilton diagonal), showing the mechanism hierarchy | `--study hamilton --figure main7 --groupsize 128 --dilemma-type 1` | `~/figures/hamilton/` | hamilton_combined.md, hamilton_reciprocity.md |
| 3 (candidate) | Information cost is soft alone but lowers the c-collapse threshold (Cost × c landscape) | `--study hamilton_cost --figure main7 --groupsize 128 --dilemma-type 1` | `~/figures/hamilton_cost/` | hamilton_cost.md |
| S (candidate) | Snowdrift raises the floor: control cooperation high without mechanisms | `--study snowdrift --figure main6 --groupsize 128 --dilemma-type 2` | `~/figures/snowdrift/` | snowdrift_calibration.md |

## Results 2 — between-population asymmetry

| Fig | Message | graphgen command | Output | Journal backing |
| --- | ------- | ---------------- | ------ | --------------- |
| 4 (candidate) | Deterministic role split in mutualism: lower-cost pop cooperates, is exploited (cooperation vs fitness) | `--study mutualism --figure main1 --groupsize 128 --dilemma-type 1` | `~/figures/mutualism/` | mutualism_partner_choice.md, synthesis.md |
| 5 (candidate) | Combined mechanisms suppress the split / lift the exploited population | `--study mutualism --figure main7 --groupsize 128 --dilemma-type 1` | `~/figures/mutualism/` | mutualism_combined.md |
| S (candidate) | Symmetric payoffs split stochastically (prisoners pop_2 paradox of success) | `--study prisoners --figure main1 --groupsize 128 --dilemma-type 1` | `~/figures/prisoners/` | prisoners_partner_choice.md |

## Results 3 — genotype composition / route to cooperation

| Fig | Message | graphgen command | Output | Journal backing |
| --- | ------- | ---------------- | ------ | --------------- |
| 6 (candidate) | Behaviour/machinery decoupling: P1 and M1 alleles erode under Cost while cooperation persists | `--study hamilton_cost --figure main1 --groupsize 128 --dilemma-type 1` and `--figure main3` | `~/figures/hamilton_cost/` | hamilton_cost.md |
| 7 (candidate) | Control (dilemma 0) decomposition: machinery erodes at ~same rate with/without a dilemma | `--study hamilton_cost --figure main3 --groupsize 128 --dilemma-type 0` | `~/figures/hamilton_cost/` | hamilton_cost.md |

## Draft captions

Fill in as the figure set is finalized; keep each caption's quantitative claims
traceable to the backing journal doc (and therefore to a verify_claims.py check).
