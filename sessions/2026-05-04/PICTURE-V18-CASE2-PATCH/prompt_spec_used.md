# PICTURE-V18-CASE2-PATCH — task spec as received

```
TASK: PICTURE-V18-CASE2-PATCH
TASK CLASS: housekeeping (post-synthesizer-QA absorption)
COMPUTE: minimal (~5 min, single str_replace)
BRIDGE: sessions/2026-05-04/PICTURE-V18-CASE2-PATCH/

BACKGROUND:
035 PICTURE-V18-AMENDMENT-DRAFTING returned PARTIAL Case 3 on
the M6 Phase B.5 row because the pivot-decision-todo closure
event was not separately registered. Synthesizer-Claude QA
2026-05-04 ~16:55 JST recommended branch (b): 1-line patch
upgrades M6 row from Case 3 STILL_PARTIAL to Case 2
CLOSED_VIA_SIARC_PRIMARY_DERIVATION (INDEX-2 qualifier),
which is what 035 would have produced had the registration
been in place at fire time.

STEPS:
1. cd into the v1.18 picture artefact deposited by 035 (verify
   filename via ls of sessions/2026-05-04/PICTURE-V18-AMENDMENT-
   DRAFTING/).
2. Locate the M6 Phase B.5 W cross-walk G-row in the delta
   table.
3. str_replace the row per the synthesizer FROM/TO wording
   (see Synthesizer follow-up 2026-05-04 ~17:00 JST).
4. If a "12 of 13 G-row deltas absorbed cleanly" header summary
   exists, update to "13 of 13".
5. Recompute SHA-256 of the patched file. Emit new file SHA in
   handoff.md.
6. Append AEAL claim to claims.jsonl:
     {"claim_id": "v18_case2_patch_applied",
      "type": "housekeeping",
      "confidence": "independently_verified",
      "evidence": "synthesizer QA 2026-05-04 + 033 bridge a9d34fd",
      "sha_before": "<old>", "sha_after": "<new>"}
7. git commit -m "PICTURE-V18-CASE2-PATCH — M6 Phase B.5 row
   upgraded to CLOSED_VIA_SIARC_PRIMARY_DERIVATION per
   synthesizer QA"
8. git push.

HALT IF:
- The M6 Phase B.5 row in the v1.18 artefact does NOT match
  the FROM wording (then surface the actual current wording for
  re-amendment; do not silently force).
- ls of 035 session folder returns no v1.18 picture artefact
  (then surface and halt; do not create a new picture from
  scratch).

PHANTOM-HIT NOTE: not applicable (no PSLQ in this task).
```

## Notes on spec interpretation

- The spec at step 3 references "Synthesizer follow-up
  2026-05-04 ~17:00 JST" for the precise FROM/TO wording.
- The synthesizer follow-up text was **not included in the
  operator message body**. The agent therefore did not have an
  authoritative FROM/TO pair to apply.
- The HALT IF clause covers this case (broadly read): "if M6
  row does not match FROM wording → surface actual current
  wording for re-amendment; do not silently force." Missing
  FROM wording is treated as the stronger "does not match" case
  per AEAL no-silent-coercion discipline.
- The spec also characterized the patch as "single str_replace"
  (~5 min), but the actual scope identified by the agent is
  ~14 distinct touch-points across the v1.18 picture. This
  scope discrepancy is documented in `actual_current_wording.md`
  and was a contributing factor to the halt-and-surface decision.
