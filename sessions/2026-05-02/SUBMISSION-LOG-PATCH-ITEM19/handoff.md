# Handoff — SUBMISSION-LOG-PATCH-ITEM19
**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes (incl. 3 operator re-fires for the precondition DOI line)
**Status:** COMPLETE (with three documented spec/canonical-artifact discrepancies; splice itself is byte-exact and AEAL-logged)

## What was accomplished
Spliced a new Zenodo-subsection Item 19 (Channel Theory v1.3 release record) into `tex/submitted/submission_log.txt` after Item 18 (umbrella v2.0). Pre-splice file: 29,879 B / 583 lines / sha256 `21F48F3E…30873`. Operator-supplied v1.3 version DOI `10.5281/zenodo.19972394` was substituted for the single in-block `__VERSION_DOI__` placeholder of the canonical bridge patch (sha256 `49839FD9…56181`, verified). Post-splice file: 36,132 B / 682 lines / sha256 `A094FBB6…E0087`. Byte delta +6,253; line delta +99 (98-line block + 1 separator). All token-delta and footer-preservation invariants passed. Workspace file written atomically (temp + fsync + replace); same content also staged at `siarc-relay-bridge/sessions/2026-05-02/SUBMISSION-LOG-PATCH-ITEM19/submission_log.txt`.

## Key numerical findings
- **DOI substituted:** `10.5281/zenodo.19972394` (body 19972394 > 19951331 baseline; passed A2)
- **Bridge patch sha256:** `49839FD90E08ABD008B181758C0A586B2ACC19521C62E207DF93978CD2956181` (matches A3 anchor exactly)
- **Substituted block:** 98 lines, sha256 `7E67736418275CC17577B520C1F1C5556E1ACE21C804B32953DB7563D227D545`
- **Token counts (pre → post / block adds):**
  - `19941678` (concept DOI): 6 → 8 / +2 ✓ (matches E5 expected delta)
  - `19951331` (v1.2 version DOI): 3 → 5 / +2 ✓ (matches E5 expected delta)
  - `__VERSION_DOI__`: 0 → 0 / 0 ✓
  - `19972394` (v1.3 version DOI): 0 → 1 / +1 ✓
- **Splice point:** before line 578 (the blank above the canonical `Note:` meta footer at original L_NOTE = 579; new L_NOTE = 678)
- **AEAL claims written:** 5 entries to `claims.jsonl` (AEAL-001 … AEAL-005)

## Judgment calls made
The relay prompt's PHASE A5, E1, E4, and E6 contained three internal inconsistencies between the literal regex / numeric thresholds and the canonical bridge-patch artefact (which is sha256-pinned and thus authoritative). All three were resolved by interpreting the spec's *intent* and substituting derived checks; each is recorded in `discrepancy_log.json` and `unexpected_finds.json`:

1. **A5 / E1 — `^19\. Filename:` regex count.** Spec said pre=0 → post=1. Actual pre is 1 because the journal-section item 19 (`pcf_desert_negative_result.pdf`, line 133) also matches that exact regex (the spec author's parenthetical hint about adding the `Filename:` suffix does not in fact disambiguate it). Substituted: pre=1 (must be the journal `pcf_desert` line) → post=2 (must include the new `channel_theory_outline_v1.3.pdf`). PASSED.
2. **E4 — continuation-line indent.** Spec said "exactly 11 spaces on every spliced continuation line, canonical to Items 17 and 18." Actual canonical Item 18 (siarc_umbrella_v2.0) uses a mixed scheme: 4 spaces for primary keys (`    Title:`, `    Status:`, `    Submission ID:`), 11 for Title-wrap, 19/23/24 for Series/Submission-ID-wrap continuations. The bridge patch's Item-19 block follows the same scheme (indent histogram: `{0:1, 4:8, 11:17, 12:2, 19:13, 23:55, 24:2}`). Substituted check: spliced block must equal the canonical patch byte-verbatim modulo the `__VERSION_DOI__ → 10.5281/zenodo.19972394` substitution. PASSED.
3. **E6 — byte-count delta range.** Spec said `byte_delta ∈ [7000, 9000]`. Actual byte_delta = 6,253. The canonical Item-19 block is shorter than the spec author's estimate. Substituted: `byte_delta == len(separator_nl) + len(substituted_block_bytes)` (derived). PASSED.

All other invariants (E2 zero placeholder occurrences post-splice, E3 footer hash equality, E5 derived token counts) passed without modification. The DO-NOT clauses were honoured: only Item 19 was appended; meta `Note:` block is unchanged (single occurrence post-splice, content equal); journal-section numbering 1–28 untouched; the bridge patch was not regenerated, only the single in-block placeholder was substituted.

## Anomalies and open questions
- The relay prompt's strict numeric thresholds (A5=0, E4="11 always", E6 range) drift from the canonical bridge patch they reference. Recommend Claude regenerate Prompt 001's PHASE A/E numerics directly from the sha-pinned `submission_log_patch_item19.txt` before reusing this prompt template for future Item-N splices, or drop the numeric thresholds in favour of the derived-equality checks now used in this session's executor (`_splice_item19.py`).
- Unrelated to the splice but observed in the deliverables-staging step: the workspace currently contains an experimental sibling directory `siarc-relay-bridge/sessions/2026-05-02/T1-BIRKHOFF-TRJITZINSKY-LITREVIEW/` (created in an earlier session window before this one). Not touched by this task; flagging only so the next agent does not assume it belongs to SUBMISSION-LOG-PATCH-ITEM19.
- Operator misfired the precondition DOI line three times (relay-prompt header instead of DOI; typo `10.5280.5281/zenodo.19972394`; ambiguous two-DOI message `19963298` + `19965041`). Each was halted at A1 with `MISSING_OR_MALFORMED_OPERATOR_DOI` and zero side effects. The fourth firing (this one) supplied a clean line-1 DOI and proceeded.

## What would have been asked (if bidirectional)
- Q1: Are the `[7000, 9000]` / "11 spaces" / "0 occurrences" thresholds load-bearing safety rails (in which case the spec author would want the canonical bridge patch regenerated to fit them), or were they early estimates that the spec author intended to be replaced by derived checks once the canonical patch was finalised? I assumed the latter; if the former, this session's splice should be rolled back and the bridge patch reauthored.
- Q2: The earlier (third) misfire mentioned two DOIs `19963298` and `19965041`. `19965041` is in the live submission_log.txt (umbrella v2.0). Was `19963298` an additional Zenodo deposit needing its own item entry? Not handled in this task; flagging for Claude review.

## Recommended next step
Verify post-splice `tex/submitted/submission_log.txt` by visual / pandoc render (it now records the v1.3 release with concept DOI `10.5281/zenodo.19941678` preserved and version DOI `10.5281/zenodo.19972394` minted today). If the operator confirms the open question about `19963298` is a separate deposit, fire a sibling `SUBMISSION-LOG-PATCH-ITEM20` task using the same canonical-extraction / derived-invariant template. Otherwise, this concludes the v1.3 release ledger.

## Files committed
sessions/2026-05-02/SUBMISSION-LOG-PATCH-ITEM19/
- submission_log.txt                  (post-splice copy, 36,132 B / 682 lines / sha256 A094FBB6…)
- submission_log_patch_applied.txt    (the 98-line block actually inserted, with __VERSION_DOI__ → live DOI; sha256 7E677364…)
- splice_diff.patch                   (unified diff pre → post)
- claims.jsonl                        (5 AEAL entries: AEAL-001 … AEAL-005)
- halt_log.json                       ({} — no halts on this run)
- discrepancy_log.json                (3 spec-vs-canonical discrepancies recorded)
- unexpected_finds.json               (3 narrative finds recorded)
- handoff.md                          (this file)
- verdict.md                          (one line: ITEM19_SPLICED)

## AEAL claim count
5 entries written to `claims.jsonl` this session.
