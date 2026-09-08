# Backlog

Open issues that need an author decision. Verification workflow and data layout:
[harness.md](harness.md). Analytical index: [findings.md](findings.md).

## Open

### asymmetric_c1_i M-suppression census is locked to a partial count

**Symptom.** python3 ai/verify_claims.py reports one failure: "M suppressed below
control in 1006 cell-conditions" returns 2001 against an expected 1006 (exact match,
no tolerance). Every other check passes (352 of 353, 2026-09-08).

**What the check counts.** mc_m1_suppressed_total (ai/verify_claims.py) censuses the
asymmetric_c1_i study for cells where the M1 allele under mechanism M sits below M1
under the no-enforcement control. It iterates 12 condition blocks — shuffle and
noshuffle x groupsize 128 and 4 x dilemmas 0, 1 and 2 — and both file sets, and it
skips any block whose .con exports are missing rather than aborting.

**Current census.** All 12 blocks load, and they total 2001:

| Shuffle   | Group size | Dilemma | Cells |
| --------- | ---------- | ------- | ----- |
| noshuffle | 128        | 0       | 173   |
| noshuffle | 128        | 1       | 109   |
| noshuffle | 128        | 2       | 240   |
| noshuffle | 4          | 0       | 175   |
| noshuffle | 4          | 1       | 115   |
| noshuffle | 4          | 2       | 240   |
| shuffle   | 128        | 0       | 129   |
| shuffle   | 128        | 1       | 109   |
| shuffle   | 128        | 2       | 155   |
| shuffle   | 4          | 0       | 164   |
| shuffle   | 4          | 1       | 155   |
| shuffle   | 4          | 2       | 237   |

**How the expectation drifted.** The check was introduced on 2026-07-07 (85f5b4e)
expecting **2001** — today's full census. Commit 1f6c380 (2026-07-27) lowered it to
1006 in the same diff that added the skip-on-missing-exports branch and a docstring
asserting that the shuffle no-enforcement controls "were never run for this study."
Those exports do exist, with mtimes of 2026-07-07 09:31 to 09:35, so they predate the
edit that declared them absent. The most likely reading is that the 07-27 session ran
against an incomplete or uncached export set, got a partial census, and re-locked the
expectation to the partial number instead of regenerating the missing .con files —
the failure mode harness.md warns about, where a SKIP is treated as a pass, except
here it was frozen into an expected value.

1006 is not reproducible from the skip logic alone. It matches neither the full census
nor the noshuffle-only subtotal (1052), and the only subsets of the 12 blocks that sum
to 1006 require arbitrary combinations (for instance noshuffle groupsize 4 dilemma 0
absent while dilemmas 1 and 2 are present). So either the underlying exports also
moved between 07-27 and now, or the partial run counted blocks that no longer exist in
that form.

**Blast radius: none in prose.** 1006 appears nowhere outside ai/verify_claims.py. No
journal doc, paper section or planning file states an M-suppression count for
asymmetric_c1_i, so no written claim depends on it.

**Recommended resolution.**

1. Restore the expected value to 2001, matching both the original lock and the current
   full census.
2. Delete the "never run for this study" clause from the docstring, which is false for
   the current export set.
3. Replace the silent skip with a census that fails loudly when a block is missing, or
   check each of the 12 blocks separately so a future drift names the block that moved.

**Harness lesson worth generalising.** Any check whose expected value depends on which
optional exports happen to be present will silently change meaning between machines
and sessions. Counts aggregated over condition blocks should either assert the block
count they consumed or be split per block.
