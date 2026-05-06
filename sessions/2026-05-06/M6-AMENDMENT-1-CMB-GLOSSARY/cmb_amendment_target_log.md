# cmb_amendment_target_log.md

**Task:** P-052 M6 spec-amendment #1 — CMB glossary block + 4 inline annotations
**Date:** 2026-05-06 (W19, Wed)
**Status:** HALTED at STEP 2 (HALT_LINE_LOCATION_MISMATCH)
**Baseline:** `tex/submitted/CMB.txt`, 1874 lines, 83963 bytes,
SHA-256 `04F2A0405F7DF5566D6720D6670AAFC26D5E157E78CD51B4B537E95FB689771A`

> NOTE on Get-Content vs ReadAllLines: an initial
> `Get-Content | Measure-Object -Line` reported 1553. The authoritative
> count via `[System.IO.File]::ReadAllLines` is 1874 (matches the
> prompt baseline). The 1553 underreport is consistent with how
> `Measure-Object -Line` (and PS pipeline counts) handle very long
> lines / final-newline edge cases on Windows pwsh; it should not
> be used for line-arithmetic anchoring. All STEP-2 grep results
> below use ReadAllLines.

---

## Verbatim block boundary (P4)

| Marker | Line |
|---|---|
| `----- begin verbatim m6_verdict.md -----` | L1644 |
| `----- end verbatim m6_verdict.md -----` | L1837 |

Annotatable region: **L1–L1643** (pre-verbatim).
Frozen region: **L1644–L1837** (verbatim m6_verdict.md; bit-for-bit
preserved per HALT_VERBATIM_BLOCK_UNMODIFIED).
Post-verbatim region: **L1838–L1874** (also unaffected by this task;
the m6_verdict.md verbatim block is followed by the next CMB entries).

---

## P5 result — HALT_GLOSSARY_ALREADY_PRESENT

PASS. Pre-1644 occurrences of literal `M6.H4 = ` and `M6.CC = ` = 0.
The string `M6.H4` and `M6.CC` do appear inside the verbatim block
(L1641, L1659–L1812 region) but never with the literal ` = ` form
that would indicate a glossary entry, and not in the pre-verbatim
annotatable region.

---

## STEP 2 — Cited vs actual `M6`-token locations

**Verdict cite (m6_verdict.md §"Spec-rollback or spec-amendment
recommendation" §1):**

> CMB §SYNTH-TRACK and §F4 / §U1 / §"P-008 fire" (CMB.txt L930,
> L972, L985-987, L1517-1518) should be amended …
> Concrete amendment: replace `M6` with `M6.CC` in CMB.txt L1518…

**Actual `\bM6\b` token inventory in pre-1644 region:**

| L (actual) | Verbatim line content (truncated) | Context tag | Inferred leg |
|---|---|---|---|
| L404  | `M9 caveat profile (M1/M2/M3/M5/M6/M8 ✅ + M4` | announcement-format pattern-match (UF-038-3 caveat profile) | M6.H4 |
| L941  | `M9 GATING (post-v1.15): {M4, M6} UNCONDITIONALLY. M8b NOT in` | gating | M6.CC |
| L993  | `  - M9 gating: {M4, M6} stands; M8b stays excluded.` | gating (recommendation summary) | M6.CC |
| L1483 | `       (substrate ID'd; needs templates + M6 inconsistency resolved)` | meta / arbitration (refers to the very ambiguity this verdict resolves) | meta — see notes |
| L1517 | `  - M6 ✅-vs-Phase-A/B.5 arbitration (in-tier; required for` | arbitration-flag (operator-visible flag carrier) | M6.CC (per verdict §1 explicit recommendation for L1518) |
| L1528 | `                   M6 arbitration + P-009 caveat` | roadmap label | meta / both legs |
| L1619 | `  - M6 arbitration                        [ ] still in-tier` | task-list label | meta / both legs |
| L1626 | `SYNTH-TRACK  2026-05-06  M6 ARBITRATION VERDICT (relay 047)` | SYNTH-TRACK header for the verdict-deposit itself | meta / both legs |
| L1630 | `resolving the M6 ✅-vs-Phase-A/B.5 status flag carried in` | verdict-deposit summary | meta / both legs |
| L1637 | `  sessions/2026-05-06/M6-ARBITRATION-W19-FRIDAY/` | bridge-anchor URL fragment (only "M6" inside path string `M6-ARBITRATION...`) | not a prose token; ignore |
| L1641 | `(M6.H4 ✅, M6.CC 🟡 PARTIAL) are correct under their respective` | verdict-deposit summary; already disambiguated | n/a — already qualified |
| L1642 | `definitions; the M9-gating clause reads M6 as M6.CC.` | verdict-deposit summary; already disambiguated | n/a — already qualified |

**Cited-line-vs-actual-`M6` mapping:**

| Verdict cite | Has `M6` token? | Nearest pre-1644 `M6` token |
|---|---|---|
| L930      | ❌ | L941 (offset +11) |
| L972      | ❌ | L993 (offset +21) — preceded by L941 (offset −31) |
| L985–987  | ❌ | L993 (offset +6 … +8) |
| L1517–1518 | ✅ at L1517 (exact) | — |

**HALT_LINE_LOCATION_MISMATCH ruling:** 3 of 4 cited locations
(L930, L972, L985–987) contain no `M6` token in the baseline.
The HALT clause fires.

Per prompt: *"If HALT_LINE_LOCATION_MISMATCH fires: do NOT
auto-relocate the target. Halt with substrate (the actual line
numbers of `M6` tokens in pre-1644 region) and surface to
operator/synth for re-spec."*

**Action taken:** STEP 2 completed (substrate gathered above).
STEP 3 (glossary insertion), STEP 4 (4 inline annotations),
STEP 5 (write amended file) are SKIPPED per the explicit
"do NOT auto-relocate" rule. CMB.txt is NOT modified by this
task.

---

## Read-context check on the one matching site (L1517–1518)

The L1517–1518 site is the only verdict-cited location that
matches a baseline `M6` token exactly. The verdict's §1
explicitly names this site as M6.CC ("replace `M6` with `M6.CC`
in CMB.txt L1518"). Note however that the actual `M6` token at
this site is at **L1517**, not L1518; L1518 is the second line
of the same bullet:

```
L1516:   CLI-internal (NOT in queue):
L1517:     - M6 ✅-vs-Phase-A/B.5 arbitration (in-tier; required for
L1518:       045 §7 substrate; pending verdict before 045 fires).
```

So even on the matching site, the verdict's explicit "L1518"
naming is technically off by one line (the `M6` token is at
L1517, the line on which `M6` appears as the leading bullet
entry; L1518 is the continuation line with no `M6` token).
Cosmetic; flagged for synth re-spec for stylistic consistency.

---

## Why "do not auto-relocate" matters here

The cited L930 / L972 / L985–987 are not random misses. They
appear to be drafting-time line-number shifts (verdict was
drafted while CMB.txt was being concurrently edited; line
numbers shifted by ~6–21 lines as later content landed). The
nearest unambiguous mappings are:

- L930 → almost certainly meant L941 (M9-GATING gating context;
  unambiguous → M6.CC)
- L972 → ambiguous between "in F3 picture v1.18 M9 block"
  (L686-696 in CMB / L973-989 in picture v1.18 reference; this
  is a *picture-side* line range cited *inside* a CMB entry)
  and L993 (M9-gating recommendation summary; M6.CC)
- L985–987 → ambiguous; could be picture-side line range
  (CT v1.3 §Implications cited as L1336–1349 in CMB at L1340) or
  L993 (M9-gating, M6.CC)

Note L972 in CMB.txt actually reads:
```
L972:     B.5/W-crosswalk verdict has not yet been substrate-merged.
```
— no `M6` token. This makes plausible that the verdict author
meant **picture v1.18 line numbers** (which the verdict explicitly
references in §"Reasoning" §3 as `picture v1.18 L979-980`) for
some of these citations, not CMB.txt line numbers, despite the
parenthetical `(CMB.txt L930, L972, L985-987, L1517-1518)`
prefix. The exact-match L1517 cite is consistent with CMB.txt
indexing; L930/L972/L985-987 may be picture-v1.18 indexing
mistakenly labeled "CMB.txt".

This ambiguity is exactly the class of issue that the
"do NOT auto-relocate" rule guards against: the executer
cannot reliably know whether to follow CMB.txt indexing,
picture v1.18 indexing, or some other reference frame, and
auto-choosing risks annotating the wrong sites.

---

## Prepared (but not applied) glossary block

The glossary block content was prepared per STEP 3 verbatim spec.
It is NOT inserted into CMB.txt under this halt; it is parked
here for the synth re-spec to pick up:

```
================================================================
GLOSSARY — M6 leg disambiguation (added 2026-05-06 per 047
M6-ARBITRATION verdict; bridge 78c7b16; operator+Claude assent
in-tier 2026-05-06)
================================================================
M6.H4 = alien-amplitude / H4 leg = `op:cc-median-resurgence-
        execute` slot. ✅ DONE 2026-05-02 (verdict
        `H4_EXECUTED_PASS_108_DIGITS`, prompt 005).
M6.CC = canonical-form / CC-VQUAD-PIII-NORMALIZATION-MAP slot
        = the M9-gating clause leg. 🟡 PARTIAL: Phase B
        PINNED 2026-05-02; Phase B.5 INDEX-2 EMBEDDING grade
        (bridge a9d34fd) pending operator+Claude pivot review;
        Phase A/C/D/E/F NOT_YET_FIRED.
Reading rule (047 verdict):
  - Unqualified `M6` in a GATING context = M6.CC
  - Unqualified `M6 ✅` in an ANNOUNCEMENT-FORMAT pattern-
    match context = M6.H4
  - Unqualified `M6` in entries written BEFORE 2026-05-06
    retains its deposit-time ambiguity; inline annotations
    below resolve specific cited cases.
================================================================
```

SHA-256 of this verbatim block (UTF-8, LF line endings, no
trailing newline beyond the closing `===…===` line):
**computed at re-fire time only, since the block is not yet
deposited into CMB.txt.** Recorded as a planned artifact, not
an applied artifact.

---

## Recommended next step (for synth re-spec)

Synth (or operator) issues a re-spec relay prompt that either:

(a) Updates the cited line numbers to actual CMB.txt M6-token
    positions {L941, L993, L1517} with explicit leg assignments
    (e.g. L941 → M6.CC; L993 → M6.CC; L1517 → M6.CC), and
    drops the L972 / L985–987 / L1518 cites that don't resolve
    to a CMB.txt `M6` token; OR

(b) Re-issues the cite as picture-v1.18 line numbers (if that
    was the verdict author's intent), which would make this a
    picture-v1.19 task rather than a CMB.txt task; OR

(c) Issues a mixed cite: glossary insertion in CMB.txt (line-
    independent; STEP 3 alone), plus a picture-v1.19 task
    against picture-v1.18 line numbers for the inline
    annotations.

Choice (a) is the lowest-friction path and matches the verdict's
own L1518 naming convention (CMB.txt-side, even if off by one
line). Choice (a) would also let the glossary block + 3
annotations land in a single re-fire.

This executer recommends (a) but defers to synth.

---

## Files in this halt deposit

- `cmb_amendment_target_log.md` (this file) — substrate
- `claims.jsonl` — AEAL claims for halt state
- `halt_log.json` — HALT_LINE_LOCATION_MISMATCH record
- `handoff.md` — operator/synth handoff
- `discrepancy_log.json` — empty (`{}`)
- `unexpected_finds.json` — empty (`{}`)

`tex/submitted/CMB.txt` is **not modified** by this task.
