# Operator Runbook — 126 M8a V0 Ratification Solo-Dispatch

**Task ID:** T1-SYNTH-M8A-RATIFICATION-SOLO-DISPATCH-126
**Drafted:** 2026-05-09
**Status (this deposit):** PARTIAL — agent has prepared dispatch packet; operator action required to fire Claude.ai conversation and capture verdict.
**Reason for PARTIAL:** Agent terminal cannot directly drive Claude.ai (per the `agent terminal limitations` repo memory: external services requiring browser-based session or human-only interactive auth are not directly drivable from the agent terminal). Per 126 prompt §1, this fire is the agent-side preparation arc; the operator-side dispatch + verdict-capture arc closes the cycle.

---

## §1. PRE-DISPATCH STATE (verified at 126 deposit time)

- 125 substrate-prep:
  - LANDED at bridge HEAD `4f15411`
  - Status: COMPLETE
  - halt_log: `{}`
  - Template path: `sessions/2026-05-09/T2-EXECUTOR-M8A-RATIFICATION-SUBSTRATE-PREP-125/m8a_v0_ratification_template.md`
  - Template SHA-256: `B877DC4FCD2B4A2EEAEC89B5ABEE523DA73578EC154A42B260CD9707BAADB5E7`
  - Template size: 37,776 bytes / 577 lines
- 127 cascade-absorption (prior premature fire):
  - Halted cleanly at Phase 0 STEP 0.2 with `HALT_127_NO_SYNTH_VERDICT` (bundled commit `a8f0919` + addendum `3a86cc9`)
  - Re-fire scheduled post-this-deposit + operator-side dispatch
- 126 dispatch packet:
  - Path: `sessions/2026-05-09/T1-SYNTH-M8A-RATIFICATION-SOLO-DISPATCH-126/dispatch_packet.txt`
  - SHA-256: `3873BE7BCE3A65588E4B603B381C2D5639FA7C43BF856323D712EDF56D1FD4C8`
  - Size: 42,450 bytes / 676 lines
  - Composition: dispatch header (instructions for the synth) + full substrate template (verbatim) + dispatch footer (post-dispatch checklist).

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

When Claude.ai responds, copy the FULL verbatim response (every character, including
formatting markers) and save it to:

```
sessions/2026-05-09/T1-SYNTH-M8A-RATIFICATION-SOLO-DISPATCH-126/synth_verdict_raw.txt
```

Do NOT edit, summarize, or reformat the response. The audit trail requires verbatim
capture.

### Step 5 — Validate format

Confirm the response contains:

- A line beginning `M8A_V0_VERDICT:` followed by one of `{RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}`
- A line beginning `Confidence band:` followed by one of `{HIGH, MEDIUM, LOW}`
- Five `## §N reasoning` sections (N = 1..5)

If any element is missing, re-prompt Claude.ai with the corresponding remediation prompt
listed at the bottom of `dispatch_packet.txt`.

If the verdict is `RATIFY_WITH_AMENDMENT`, also confirm §5 contains a concrete, actionable
amendment specification (not vague advice).

### Step 6 — (Optional) Dual-witness pattern

Per the M7 V0 cascade precedent (123, FIRST observed dual-witness fire on 2026-05-09;
UF-123-1 candidate-memory under deferral until n=3), the operator may run a SECOND
parallel Claude.ai dispatch in a separate tab using the same packet. If used, save
the second verbatim response to:

```
sessions/2026-05-09/T1-SYNTH-M8A-RATIFICATION-SOLO-DISPATCH-126/synth_verdict_raw_R2.txt
```

The cascade absorption (127 re-fire) then aggregates per most-conservative protocol
(see 123 cascade record §3.1 for the canonical aggregation algorithm).

### Step 7 — Re-fire 127 cascade absorption

Once `synth_verdict_raw.txt` (and optionally `synth_verdict_raw_R2.txt`) is captured,
re-fire prompt 127 (cascade-absorption) which:

1. Parses the verdict label.
2. Generates `verdict_packet.md` (structured: label + confidence + reasoning quotations + cites).
3. Updates manuscript-content per the verdict (RATIFY → no edits beyond M8a status table; RATIFY_WITH_AMENDMENT → applies the §5 amendment; DEFER → records additional substrate request as a new SQL todo; OBJECT → halts and routes objection to a separate triage prompt).
4. Closes the M8a axis on the milestone status table.
5. Closes A1-A4 acceptance criteria from this fire's §5 (the prep-arc deferred subset).

The 127 prior-halt deposit at `sessions/2026-05-09/T1-SYNTH-M8A-RATIFICATION-CASCADE-ABSORPTION-127/` documents the Phase 0 gate-trip class B (DEPENDENCY-NOT-LANDED) and its resolution path; the re-fire on this 126 deposit + verdict closes that gate.

## §3. FAILURE MODES + RECOVERY

| Failure | Recovery |
|---|---|
| Claude.ai response truncated mid-section | Re-prompt: "Please re-emit the verdict in full, including all five §1-§5 reasoning sections." |
| Verdict label not in allowed set | Re-prompt: "Please re-emit your verdict label as one of `{RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}`." |
| Claude.ai introduces external citation not in substrate | Re-prompt: "The substrate is closed-set. Please re-emit your reasoning citing only the embedded template. Remove any external references." |
| Claude.ai refuses on safety grounds | Re-prompt with explicit math-research framing; if still refused, log `HALT_126_SYNTH_DECLINED` in `halt_log.json` of cascade-absorption (127 re-fire) and route to alternative synth provider. |

## §4. ALIGNMENT WITH PRIOR SOLO-DISPATCH PATTERNS

This packet structurally mirrors the M7 V0 dispatch (122, bridge session `T1-SYNTH-M7-RATIFICATION-SOLO-DISPATCH-122`, 2026-05-09; commit `24047e0`/parent `f4b6de8`) and the M4 V0 fast-track dispatch (104, `PEER-CONSULT-104-M4-FAST-TRACK`, 2026-05-08) with:

- Same 5-question schema (§1 scope, §2 evidence, §3 questions, §4 verdict label, §5 amendment if applicable).
- Same 4-label verdict alphabet `{RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}`.
- Same closed-substrate constraint (no external references admitted).
- Same operator-side dispatch + agent-side absorption arc separation.

Difference vs M7: M8a's substrate carries the T3-CONTE-MUSETTE 60/60 P_III(D_6) labeling result (663e95c) + UMB-T3-PROBE precursor (bbd1b76) + Picture v1.19 (70d1a48) — a STRUCTURAL-LABELING closure type, distinct from M7's algebraic-combinatorial PSLQ-exhaustion mechanism. The synth should treat M8a as a Painlevé-classification full-coverage closure at d=2 stratum; sibling axes M4 (closed), M7 (closed today), M8b (substrate-prep at 128) are explicitly out of scope.

## §5. POST-DISPATCH SUCCESS SIGNALS

After 127 cascade-absorption (re-fire) lands, the following should be true:

- `synth_verdict_raw.txt` exists and is non-empty (and `synth_verdict_raw_R2.txt` if dual-witness path taken).
- `verdict_packet.md` exists with parsed label + confidence + reasoning.
- One AEAL meta-claim entry in `claims.jsonl` of session 127 (re-fire) referencing this packet's SHA.
- Forbidden-verb scan clean (synth's verbatim response inherits audit-trail / quoted-substrate exemption; agent-authored prose must remain clean).
- M8a status on the milestone table updated per verdict (Picture v1.19 row M8a → `closed (RATIFY) | closed (RATIFY_WITH_AMENDMENT applied) | reopened (DEFER → resubstrate) | halted (OBJECT)`).

## §6. END

End of operator runbook. Once Steps 1-7 complete, the M8a V0 ratification cycle closes.
