# Operator Runbook — 129 M8b V0 Ratification Solo-Dispatch

**Task ID:** T1-SYNTH-M8B-RATIFICATION-SOLO-DISPATCH-129
**Drafted:** 2026-05-09
**Status (this deposit):** PARTIAL — agent has prepared dispatch packet; operator action required to fire Claude.ai conversation and capture verdict.
**Reason for PARTIAL:** Agent terminal cannot directly drive Claude.ai (per `agent terminal limitations` repo memory). This fire is the agent-side preparation arc; operator-side dispatch + verdict-capture closes the cycle via 130 re-fire.

---

## §1. PRE-DISPATCH STATE (verified at 129 deposit time)

- 128 substrate-prep:
  - LANDED at bridge HEAD `f02ab5d`
  - Status: COMPLETE
  - halt_log: `{}`
  - Template path: `sessions/2026-05-09/T2-EXECUTOR-M8B-RATIFICATION-SUBSTRATE-PREP-128/m8b_v0_ratification_template.md`
  - Template SHA-256: `06FD8AC2B9A6ECDF89A17351FAD909830FFB3ED6FC650B7EAE37A153AC35882A`
  - Template size: 46,109 bytes / 691 lines
  - Closure type: NUMERICAL-FORECLOSURE via Borel-Padé S_2 acceleration (092=`14e6b09`) + d≥3 caveat carry-forward (P-009=`1873538`)
- 130 cascade-absorption (prior premature fire):
  - Halted cleanly at Phase 0 STEP 0.2 with `HALT_130_NO_SYNTH_VERDICT` (commit `a8f0919` bundled with 127-halt)
  - Re-fire scheduled post-this-deposit + operator-side dispatch
- 129 dispatch packet:
  - Path: `sessions/2026-05-09/T1-SYNTH-M8B-RATIFICATION-SOLO-DISPATCH-129/dispatch_packet.txt`
  - SHA-256: `9B5A033461F656B23AFF98523FDEDD3931F7D88E06E2C5045A8A96D953F30F68`
  - Size: 51,295 bytes / 795 lines
  - Composition: dispatch header (instructions for the synth + explicit P-009 d≥3-caveat scope-fence) + full substrate template (verbatim) + dispatch footer (post-dispatch checklist + (NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD) annotation guidance).

## §2. OPERATOR ACTION REQUIRED

### Step 1 — Open Claude.ai

Open a fresh Claude.ai conversation tab. (Avoid contaminating an existing conversation.)

### Step 2 — Copy the paste-block

Open `dispatch_packet.txt` in this folder. Inside the file, locate the lines:

```
===PASTE FROM HERE===
```

and:

```
===END PASTE===
```

Select EVERYTHING between (and INCLUDING) these two markers. The header above
`===PASTE FROM HERE===` (which contains operator metadata) MUST NOT be pasted.

### Step 3 — Submit to Claude.ai

Paste the selection into the Claude.ai conversation and submit.

### Step 4 — Capture the verbatim response

When Claude.ai responds, copy the FULL verbatim response and save it to:

```
sessions/2026-05-09/T1-SYNTH-M8B-RATIFICATION-SOLO-DISPATCH-129/synth_verdict_raw.txt
```

Do NOT edit, summarize, or reformat. Audit trail requires verbatim capture.

### Step 5 — Validate format

Confirm the response contains:

- A line beginning `M8B_V0_VERDICT:` followed by one of `{RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}`
- A line beginning `Confidence band:` followed by one of `{HIGH, MEDIUM, LOW}`
- Five `## §N reasoning` sections (N = 1..5)

If any element is missing, re-prompt per the bottom of `dispatch_packet.txt`.

### Step 6 — (RECOMMENDED) Dual-witness pattern

Per UF-128-3 (closure-type novelty: NUMERICAL-FORECLOSURE-by-residual-acceptance + d≥3 caveat carry-forward) flagged in 128 substrate-prep handoff, **dual-witness is RECOMMENDED for M8b** (vs optional for M7 / M8a) given the closure-type novelty. Run a SECOND parallel Claude.ai dispatch in a separate tab using the same packet. Save the second verbatim response to:

```
sessions/2026-05-09/T1-SYNTH-M8B-RATIFICATION-SOLO-DISPATCH-129/synth_verdict_raw_R2.txt
```

The cascade absorption (130 re-fire) aggregates per most-conservative protocol (see 123 cascade record §3.1 for canonical aggregation algorithm). Dual-witness on M8b would also bring the dual-witness pattern observation count to n=3 (after M7 / M8a / M8b), enabling promotion of the `dual_witness_cascade_pattern` candidate-memory.

### Step 7 — Re-fire 130 cascade absorption

Once `synth_verdict_raw.txt` (and `synth_verdict_raw_R2.txt` if dual-witness) is captured, re-fire prompt 130 (cascade-absorption) which:

1. Parses the verdict label.
2. Generates `verdict_packet.md` (structured: label + confidence + reasoning quotations + cites).
3. Updates manuscript-content per the verdict (RATIFY → no edits beyond M8b status table; RATIFY_WITH_AMENDMENT → applies the §5 amendment; DEFER → records additional substrate request as a new SQL todo; OBJECT → halts and routes objection to a separate triage prompt).
4. Closes the M8b axis on the milestone status table at d=2 stratum (d≥3 explicitly remains open per P-009 caveat).
5. Closes A1-A4 acceptance criteria from this fire's §5 (the prep-arc deferred subset).

The 130 prior-halt deposit at `sessions/2026-05-09/T1-SYNTH-M8B-RATIFICATION-CASCADE-ABSORPTION-130-HALT-NO-VERDICT/` documents the Phase 0 gate-trip class B (DEPENDENCY-NOT-LANDED); the re-fire on this 129 deposit + verdict closes that gate.

## §3. FAILURE MODES + RECOVERY

| Failure | Recovery |
|---|---|
| Claude.ai response truncated mid-section | Re-prompt: "Please re-emit the verdict in full, including all five §1-§5 reasoning sections." |
| Verdict label not in allowed set | Re-prompt: "Please re-emit your verdict label as one of `{RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}`." |
| Claude.ai introduces external citation not in substrate | Re-prompt: "The substrate is closed-set. Please re-emit your reasoning citing only the embedded template. Remove any external references." |
| Claude.ai treats d≥3 carry-forward as OBJECT-grounds | Re-prompt: "The d≥3 carry-forward is an INTENTIONAL caveat per P-009 substrate-of-record. The V0 ratification target is d=2 only. Please re-evaluate Q4 with d≥3 explicitly out of scope per the dispatch-header scope-fence." |
| Claude.ai refuses on safety grounds | Re-prompt with explicit math-research framing; if still refused, log `HALT_129_SYNTH_DECLINED` in `halt_log.json` of cascade-absorption (130 re-fire) and route to alternative synth provider. |

## §4. ALIGNMENT WITH PRIOR SOLO-DISPATCH PATTERNS

This packet structurally mirrors the M7 V0 dispatch (122) and M8a V0 dispatch (126, this same session) with:

- Same 5-question schema (§1 scope, §2 evidence, §3 questions, §4 verdict label, §5 amendment if applicable).
- Same 4-label verdict alphabet `{RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}`.
- Same closed-substrate constraint (no external references admitted).
- Same operator-side dispatch + agent-side absorption arc separation.

**Difference vs M7 / M8a:** M8b is the FIRST NUMERICAL-FORECLOSURE closure type in the M-axis ratification series. The substrate (128) carries:
- 4 substrate SHA-verified bridge references: 092 (`14e6b09`, Borel-Padé S_2 foreclosure at d=2), P-009 (`1873538`, M8b caveat-final), 038 (`a26ab27`, milestone gap survey), picture-v1.19 (`70d1a48`).
- P-009 caveat threading: M8b only forecloses S_2 at d=2 stratum; d≥3 stratum is explicitly UNREACHED and the closure makes no claim about d≥3.
- `(NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)` annotation pattern in §1 / §4 of substrate.

Sibling axes M4 (closed) / M7 (closed) / M8a (substrate-prep + dispatch done; cascade pending) are explicitly out of scope for this dispatch.

## §5. POST-DISPATCH SUCCESS SIGNALS

After 130 re-fire cascade-absorption lands, the following should be true:

- `synth_verdict_raw.txt` exists and is non-empty (and `synth_verdict_raw_R2.txt` if dual-witness).
- `verdict_packet.md` exists with parsed label + confidence + reasoning.
- One AEAL meta-claim entry in `claims.jsonl` of session 130 re-fire referencing this packet's SHA.
- Forbidden-verb scan clean.
- M8b status on the milestone table updated per verdict at d=2 stratum (Picture v1.19 row M8b → `closed-at-d=2 (RATIFY) | closed-at-d=2-with-amendment (RATIFY_WITH_AMENDMENT) | reopened (DEFER) | halted (OBJECT)`; d≥3 remains explicitly open).

## §6. END

End of operator runbook. Once Steps 1-7 complete, the M8b V0 ratification cycle (d=2 only) closes.
