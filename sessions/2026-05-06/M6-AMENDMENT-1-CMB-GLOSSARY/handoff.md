# Handoff — M6-AMENDMENT-1-CMB-GLOSSARY
**Date:** 2026-05-06
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** HALTED (HALT_LINE_LOCATION_MISMATCH at STEP 2)

## What was accomplished

Relay 052 fired the M6 spec-amendment #1 task: add a permanent
glossary block to `tex/submitted/CMB.txt` defining `M6.H4` and
`M6.CC` per the 047 M6-arbitration verdict, plus inline annotations
at four cited locations (L930, L972, L985-987, L1517-1518). The
executer completed STEP 1 (SHA-256 anchor + line-count baseline) and
STEP 2 (locate cited line ranges + verbatim-block boundary), then
halted at HALT_LINE_LOCATION_MISMATCH because 3 of 4 cited locations
contain no `M6` token in the baseline. Per the relay-052 prompt's
explicit rule, the executer did NOT auto-relocate the targets.
`tex/submitted/CMB.txt` is **not modified** by this task. Substrate
for synth re-spec is staged in this session directory.

## Key numerical findings

(no numerical claims — PERMANENT-RECORD-EDIT class; AEAL grounding is
file-anchor SHA-256s only)

- `tex/submitted/CMB.txt` baseline: 1874 lines, 83963 bytes,
  SHA-256 `04F2A0405F7DF5566D6720D6670AAFC26D5E157E78CD51B4B537E95FB689771A` (claim C1)
- `m6_verdict.md` source: SHA-256
  `C9BBAB60FF1ACCE428A21A806D8DF0350C9756A58A9F5C4799E1D6D8EBF3263F` (claim C2)
- Verbatim block in CMB.txt: L1644 (`----- begin verbatim m6_verdict.md -----`)
  through L1837 (`----- end verbatim m6_verdict.md -----`) (claim C3)
- P5 (HALT_GLOSSARY_ALREADY_PRESENT): PASS, 0/0 hits in pre-1644 (claim C4)
- Pre-1644 `M6` token inventory: L404, L941, L993, L1483, L1517,
  L1528, L1619, L1626, L1630, L1641, L1642 (the latter three are
  inside the post-047 SYNTH-TRACK intro paragraph immediately
  preceding the verbatim block; L1641-L1642 are already
  leg-qualified) (claim C5)

## Cited-location mapping

| m6_verdict.md \u00a71 cite | Has `M6` token in baseline CMB.txt? | Nearest baseline `M6` token |
|---|---|---|
| L930          | NO  | L941 (+11) |
| L972          | NO  | L941 (\u201331) or L993 (+21) \u2014 ambiguous |
| L985\u2013987   | NO  | L993 (+6\u2026+8) |
| L1517\u20131518 | YES (L1517 exact); verdict explicitly names M6.CC | (verdict cite is L1518, off by one line; M6 token at L1517) |

Only 1 of 4 cited locations resolves cleanly to a baseline `M6`
token, and that one (L1517) is off by one line in the verdict's
own naming (it says L1518). The other three cited locations
(L930, L972, L985\u2013987) have no plausible single-target
unambiguous re-mapping.

## Judgment calls made

1. **Authoritative line count via `[System.IO.File]::ReadAllLines`,
   not `Measure-Object -Line`.** An initial PowerShell pipeline
   reported 1553 lines; the true count is 1874 (matches prompt
   baseline). The 1553 was an artifact of how `Measure-Object -Line`
   handles certain unicode glyphs / final-newline conditions. All
   subsequent line-arithmetic uses the ReadAllLines count.
   Documented in `cmb_amendment_target_log.md` opening note. No
   downstream impact.

2. **No auto-relocation.** The cited L930 is offset +11 from L941
   and L985\u2013987 is offset +6\u20138 from L993, both pointing to
   M9-gating contexts that the verdict\u2019s reading rule classifies
   unambiguously as M6.CC. The temptation to silently relocate to
   {L941, L993, L1517} and proceed is real but explicitly forbidden
   by the relay-052 prompt's HALT_LINE_LOCATION_MISMATCH rule
   ("do NOT auto-relocate the target. Halt with substrate ... and
   surface to operator/synth for re-spec"). Honoring the rule.

3. **Glossary block prepared verbatim and parked in
   `cmb_amendment_target_log.md`, not applied.** The glossary block
   text from STEP 3 is line-number-independent and could in
   principle have been inserted unilaterally even under the line-
   location halt. Did not do so because the standing-instruction
   halt rule ("Do not continue past a halt condition") is broader
   than the prompt-specific HALT_LINE_LOCATION_MISMATCH wording, and
   the cleanest re-fire posture is to deliver glossary + corrected
   annotations atomically. Block content is preserved verbatim for
   re-fire pickup.

4. **C7 / C8 claims classified as halt-state vacuous.** Claim C7
   records the prepared-but-not-applied glossary block; claim C8
   marks self-checks (HALT_DEPOSIT_TIME_PRESERVATION,
   HALT_VERBATIM_BLOCK_MODIFIED) as vacuous-pass because no edits
   were applied. Documented this stance explicitly in claims.jsonl.

## Anomalies and open questions

**(THIS IS THE MOST IMPORTANT SECTION.)**

1. **Cited line numbers L930 / L972 / L985\u2013987 do not resolve to
   CMB.txt `M6` tokens.** The three plausible explanations:

   (a) **Concurrent-edit drift.** The verdict was drafted while
       CMB.txt was being edited; line numbers shifted by ~6\u201311 lines
       as content was appended between draft and post-047
       SYNTH-TRACK landing. A consistent positive offset
       (cited \u2192 actual: +11, +21, +6\u20138) supports this. Under
       this hypothesis, the intended targets are {L941, L993,
       L1517}, all M6.CC under the gating-context reading rule.

   (b) **Picture-v1.18 / CMB.txt cite confusion.** The verdict\u2019s
       \u00a7Reasoning \u00a73 explicitly cites picture-v1.18 line numbers
       (`picture v1.18 L979-980`). L972 / L985\u2013987 are numerically
       close to where the M9-gating clause sits inside picture v1.18,
       and could be picture-side line numbers mistakenly labeled
       `(CMB.txt L\u2026)` in \u00a71. The exact-match L1517 cite
       constrains \u00a71 to be at minimum partially CMB.txt-side, so
       this would mean \u00a71's parenthetical is mixed-frame.

   (c) **Verdict author was citing semantic regions, not exact
       lines.** Possible but the prompt and verdict both treat the
       line numbers as targets, so this seems unlikely.

   The executer cannot determine (a) vs (b) vs (c) from CMB.txt +
   m6_verdict.md alone. Synth/operator decision needed.

2. **Even L1518 is off by one line.** The verdict\u2019s explicit
   "replace `M6` with `M6.CC` in CMB.txt L1518" recommendation
   names L1518, but the actual `M6` token is at L1517 (L1518 is
   the continuation line of the same bullet, with no `M6` token).
   Cosmetic, but indicates that even the one matching cite was not
   verified against the baseline at draft time.

3. **The glossary block is line-number-independent.** STEP 3 alone
   could be split off into a smaller follow-up that doesn\u2019t depend
   on cited line numbers. If synth wants partial progress before
   resolving the line-number issue, glossary-only would be a valid
   sub-task. Not done unilaterally because the relay frames the
   amendment as a single deposit.

4. **`M6` tokens at L404 (announcement-format pattern-match) and
   L1483 (meta / arbitration-substrate reference) are not in the
   verdict\u2019s cite list.** L404 would map to M6.H4 under the
   verdict\u2019s reading rule (`M9 caveat profile (M1/M2/M3/M5/M6/M8
   \u2705 + M4 ...)`); L1483 is meta. Whether these should also receive
   inline annotations under amendment #1 (or under a future
   amendment) is a synth call.

5. **Missing recommendation in the verdict for `cli_log/2026-05-05.md`
   L1166 + L1234\u20131235.** The verdict references these as the
   operator-visible flag carrier (\u00a7"Reasoning" intro), but doesn\u2019t
   recommend a parallel CMB-style amendment for the cli_log itself.
   Out of scope for this task; flagged here in case the synth re-spec
   wants to bundle cli_log annotations.

## What would have been asked (if bidirectional)

> "The 4 cited line numbers in your \u00a71 don\u2019t match CMB.txt baseline.
> Are they (a) drift from concurrent editing (intended targets
> {L941, L993, L1517}, all M6.CC), or (b) picture-v1.18 line numbers
> mixed into a CMB.txt-labeled cite, or (c) something else? Also:
> the L1518 in your \u00a71 should be L1517."

If the answer were (a), this task would have proceeded with
{L941, L993, L1517} and three M6.CC annotations.

If the answer were (b), this task would have aborted in favor of a
picture-v1.19 task (with the glossary block possibly split off as a
small CMB.txt-only sub-task).

## Recommended next step

Synth re-spec relay (suggested ID: 052R) that:

(i)  Confirms the cited line numbers were drift, not picture-v1.18
     references, and updates them to the actual baseline `M6` token
     positions: L941, L993, L1517 (all M6.CC by the gating-context
     reading rule).
(ii) Drops the L972 / L985\u2013987 / L1518 cites as either redundant
     (L1518 \u2192 L1517) or unresolvable (L972, L985\u2013987 do not point
     at a CMB.txt `M6` token).
(iii) Optionally extends to L404 (M6.H4 by announcement-format
      reading rule) and L1483 (meta) if synth wants full pre-1644
      coverage.
(iv) Re-fires the glossary block (verbatim from this deposit\u2019s
     `cmb_amendment_target_log.md` \u00a7"Prepared (but not applied)
     glossary block") + the corrected inline annotations as a
     single atomic CMB.txt edit.

Friction: low. Single re-fire delivers everything 052 was supposed
to deliver, with corrected substrate.

## Files committed

- `cmb_amendment_target_log.md` \u2014 substrate for synth re-spec
  (verbatim baseline content of all relevant `M6` token lines,
  cited-vs-actual mapping, prepared glossary block parked here
  for re-fire pickup, executer recommendations)
- `claims.jsonl` \u2014 8 AEAL claims (C1 baseline anchor, C2 verdict
  source anchor, C3 verbatim-block boundary, C4 P5 PASS, C5 token
  inventory, C6 HALT ruling, C7 glossary-parked, C8 self-checks-
  vacuous-pass)
- `halt_log.json` \u2014 HALT_LINE_LOCATION_MISMATCH formal record
  with cited-vs-actual mapping + candidate resolution paths
- `discrepancy_log.json` \u2014 empty `{}`
- `unexpected_finds.json` \u2014 4 entries (U1 spec-line-stale, U2
  verdict-off-by-one, U3 cross-file-cite hypothesis, U4 drift
  hypothesis)
- `handoff.md` \u2014 this file

## AEAL claim count

8 entries written to claims.jsonl this session (C1\u2013C8). All
PERMANENT-RECORD-EDIT class. Zero numerical claims (file-anchor
SHA-256s + ruling claims only).
