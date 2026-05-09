# Operator Runbook — 122 M7 V0 Ratification Solo-Dispatch

**Task ID:** T1-SYNTH-M7-RATIFICATION-SOLO-DISPATCH-122
**Drafted:** 2026-05-09
**Status (this deposit):** PARTIAL — agent has prepared dispatch packet; operator action required to fire Claude.ai conversation and capture verdict.
**Reason for PARTIAL:** Agent terminal cannot directly drive Claude.ai (parallel to gh-auth-agent-terminal-limitation and zenodo-deposit-agent-limitation-2026-05-09 patterns). Per 122 prompt §4, "the agent (or operator) absorbs it into bridge" — this fire is the agent-side preparation arc; the operator-side dispatch + verdict-capture arc closes the cycle.

---

## §1. PRE-DISPATCH STATE (verified at 122 deposit time)

- 121 substrate-prep:
  - LANDED at bridge HEAD `f4b6de8`
  - Status: COMPLETE
  - halt_log: `{}`
  - Template path: `sessions/2026-05-09/T2-EXECUTOR-M7-RATIFICATION-SUBSTRATE-PREP-121/m7_v0_ratification_template.md`
  - Template SHA-256: `72D855F7B05D3F209340FBF57E7CAFD793BF1E8FA283502CF9889124E1BB6BE5`
  - Template size: 27,153 bytes / 452 lines
- 122 dispatch packet:
  - Path: `sessions/2026-05-09/T1-SYNTH-M7-RATIFICATION-SOLO-DISPATCH-122/dispatch_packet.txt`
  - SHA-256: `B9424DE21F90C602091F84376AA97D46F474AB33156055DBB672A52B758A4BCC`
  - Size: 31,692 bytes / 550 lines
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
sessions/2026-05-09/T1-SYNTH-M7-RATIFICATION-SOLO-DISPATCH-122/synth_verdict_raw.txt
```

Do NOT edit, summarize, or reformat the response. The audit trail requires verbatim
capture.

### Step 5 — Validate format

Confirm the response contains:

- A line beginning `M7_V0_VERDICT:` followed by one of `{RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}`
- A line beginning `Confidence band:` followed by one of `{HIGH, MEDIUM, LOW}`
- Five `## §N reasoning` sections (N = 1..5)

If any element is missing, re-prompt Claude.ai with the corresponding remediation prompt
listed at the bottom of `dispatch_packet.txt`.

If the verdict is `RATIFY_WITH_AMENDMENT`, also confirm §5 contains a concrete, actionable
amendment specification (not vague advice).

### Step 6 — Fire 123 cascade absorption

Once `synth_verdict_raw.txt` is captured, fire prompt 123 (cascade-absorption) which:

1. Parses the verdict label.
2. Generates `verdict_packet.md` (structured: label + confidence + reasoning quotations + cites).
3. Updates manuscript-content per the verdict (RATIFY → no edits beyond M7 status table; RATIFY_WITH_AMENDMENT → applies the §5 amendment; DEFER → records additional substrate request as a new SQL todo; OBJECT → halts and routes objection to a separate triage prompt).
4. Closes the M7 axis on the milestone status table.

## §3. FAILURE MODES + RECOVERY

| Failure | Recovery |
|---|---|
| Claude.ai response truncated mid-section | Re-prompt: "Please re-emit the verdict in full, including all five §1-§5 reasoning sections." |
| Verdict label not in allowed set | Re-prompt: "Please re-emit your verdict label as one of `{RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}`." |
| Claude.ai introduces external citation not in substrate | Re-prompt: "The substrate is closed-set. Please re-emit your reasoning citing only the embedded template. Remove any external references." |
| Claude.ai refuses on safety grounds | Re-prompt with explicit math-research framing; if still refused, log `HALT_122_SYNTH_DECLINED` in `halt_log.json` of cascade-absorption (123) and route to alternative synth provider. |

## §4. ALIGNMENT WITH PRIOR SOLO-DISPATCH PATTERNS

This packet structurally mirrors the M4 V0 fast-track dispatch (104, bridge session `PEER-CONSULT-104-M4-FAST-TRACK`, 2026-05-08) with:

- Same 5-question schema (§1 scope, §2 evidence, §3 questions, §4 verdict label, §5 amendment if applicable).
- Same 4-label verdict alphabet `{RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT}`.
- Same closed-substrate constraint (no external references admitted).
- Same operator-side dispatch + agent-side absorption arc separation.

## §5. POST-DISPATCH SUCCESS SIGNALS

After 123 cascade-absorption lands, the following should be true:

- `synth_verdict_raw.txt` exists and is non-empty.
- `verdict_packet.md` exists with parsed label + confidence + reasoning.
- One AEAL meta-claim entry in `claims.jsonl` of session 123 referencing this packet's SHA.
- Forbidden-verb scan clean (synth's verbatim response is exempt under audit-trail clause; agent-authored prose must remain clean).
- M7 status on the milestone table updated per verdict.

## §6. END

End of operator runbook. Once Steps 1-6 complete, the M7 V0 ratification cycle closes.
