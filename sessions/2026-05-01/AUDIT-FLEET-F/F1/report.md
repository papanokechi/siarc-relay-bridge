# F1 — AEAL claims consistency

**Scope:** all `sessions/2026-05-01/*/claims*.jsonl` (excluding AUDIT-FLEET-F itself).

## Summary

- Session folders scanned: **22**
- claims*.jsonl files found: **36**
- Total claim entries: **305**
- Unique claim_ids: **257**
- Cross-session duplicate claim_ids: **0**
- Verdict contradictions (same stmt, opposing verdict): **0**
- Schema violations (missing claim_id/statement): **101**
- JSON parse errors: **0**
- Broken handoff xrefs (claim_id cited but not defined): **0**
- FALSIFIED-but-still-cited in published tex: **0**

## Severity counts

{
  "MEDIUM": 101
}

## Notes

- "Cross-session duplicate claim_id" treats the session folder under
  `sessions/2026-05-01/<NAME>/` as the namespace boundary; multiple
  `claims_phase_*.jsonl` files in the *same* folder are not flagged.
- "Verdict contradiction" uses normalised lower-case statement string
  (first 160 chars); only fires when both POS and NEG token sets hit.
- "Broken claim xref" is heuristic: an ID is flagged only if its prefix
  family exists elsewhere in `claims*.jsonl` but the specific ID does not.
- Findings are listed in `findings.jsonl`.
