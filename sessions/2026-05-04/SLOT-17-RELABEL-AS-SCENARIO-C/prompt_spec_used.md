# Prompt spec used — SLOT-17-RELABEL-AS-SCENARIO-C

**Operator dispatch:** 2026-05-04 ~17:40 JST chat command "option A"
following Copilot's surfacing of two paste-ready paths for the slot 17
relabel task.

**Synthesizer arbitration:** 2026-05-04 ~16:55 JST recommended slot 17
be recorded as a SCENARIO_C analogue per 031 WITTE-FORRESTER-2010-
ACQUISITION verdict pattern. Synthesizer characterized this as a "one-
line manifest edit" — Option A executes that minimum-cost path
(annotation block + SHA line in `SHA256SUMS.txt`, no PDF copy into
workspace).

## Task scope

**Target file:** `tex/submitted/control center/literature/g3b_2026-05-03/SHA256SUMS.txt`

**Action:** append `# Slot 17 - ...` annotation block (mirroring slots
14/15/16 negative-finding precedent + slots 06/09 SCENARIO_C precedent),
followed by SHA-256 + bridge-relative path of the FW 2005 substitute
artefact.

**Substitute artefact:** `siarc-relay-bridge/sessions/2026-05-04/WITTE-FORRESTER-2010-ACQUISITION/substitute_FW_2005_PIIIp_boundary.pdf`
- Acquired by 031 verdict (commit 4338cee) as graceful-degradation
  substitute after Witte-Forrester 2010 spec identifiers (DOI +
  arXiv:0911.1762) resolved to unrelated 2010 papers.
- Forrester-Witte 2005 "Boundary conditions associated with the
  Painlevé III' and V evaluations of some random matrix averages"
  arXiv:math/0512142, J. Phys. A 39 (2006) 8983-8995.
- 0 occurrences of B_2 / (2A_1) / Sakai / Weyl / homomorphism /
  D_6 / surface / Dynkin per 031 readback (full-text search).

## Decision: Option A vs Option B (operator selected A)

| | Option A (selected) | Option B |
|---|---|---|
| PDF location | bridge only | copy into workspace literature folder |
| Manifest SHA-line path | `siarc-relay-bridge/sessions/.../substitute_FW_2005_PIIIp_boundary.pdf` | `tex/submitted/control center/literature/g3b_2026-05-03/17_forrester_witte_2005_PIIIp_boundary.pdf` |
| Symmetry with slots 1-16 | breaks (path not under literature/) | matches |
| AEAL provenance | preserves bridge colocation with 031 verdict + claims.jsonl + readback | duplicates artefact across two locations |
| Synthesizer framing | "one-line manifest edit" (matches) | broader |

Option A chosen by operator at 2026-05-04 ~17:40 JST.

## Steps executed (per Standing Final Step + this spec)

1. Compute SHA-256 of FW 2005 substitute PDF in bridge: confirmed
   `80e050092174159a4d7dce3f5e8436daa0c3a5502830178fe3accab8af83cb61`
   matches 031 verdict commit 4338cee declaration.
2. Capture pre-amend SHA-256 of `SHA256SUMS.txt`: `9CF86B47...BE9E2`
   (size 11,895 B / 167 lines).
3. Append annotation block (24 lines of `# ...` comments + 1 SHA line)
   using LF line endings (matches dominant pattern in file).
4. Capture post-amend SHA-256: `0518E111...A0A190` (size 13,744 B /
   192 lines; delta +1,849 B / +25 lines).
5. Verify last 6 lines render cleanly; SHA line trailing-newline present.
6. Bridge deposit: claims.jsonl (4 entries), prompt_spec_used.md (this
   file), handoff.md, before/after SHA capture files, empty
   halt_log.json + discrepancy_log.json + unexpected_finds.json.
7. Bridge git add + commit + push.
8. Workspace `_INDEX.txt` header line update (no commit; agent does not
   push wallis-pcf-lean4).
9. SQL: close `slot-17-fw2005-substitute-accept` and
   `literature-slot-17-deposit-decision` as done.

## Halt conditions (none triggered)

- Annotation block appended cleanly; no merge conflicts.
- FW 2005 substitute PDF SHA matches 031 verdict declaration exactly.
- No stray characters or encoding issues observed in last-6-lines tail.

## Phantom-hit / hallucinated-identifier note

Not applicable to this task (no PSLQ; no new identifiers cited beyond
those already verified by 031 verdict). The DOI + arXiv IDs included in
the annotation block are explicitly flagged AS hallucinated — they are
present for AEAL provenance, not as live targets.
