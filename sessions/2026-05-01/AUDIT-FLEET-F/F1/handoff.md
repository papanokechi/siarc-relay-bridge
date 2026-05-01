# Fleet-F · F1 — AEAL Claims Audit

**Status:** completed (read-only audit)

## Verdict

**HIGH** — schema mismatch across the entire AEAL corpus.

## Stats

- Session folders scanned: 26
- `claims.jsonl` files found: 26
- Total claim entries: 199
- Schema violations: 995

## Findings

### HIGH

- **AEAL schema drift** — All 199 entries across 26 sessions use the schema
  `{claim, evidence_type, script, output_hash}` rather than the AEAL-mandated schema
  `{claim_id, type, statement, evidence, confidence}`. Because `claim_id` and `verdict`
  are absent in every entry, the audit cannot evaluate duplicates, verdict
  contradictions, or confidence/evidence calibration mismatches at all.

### MEDIUM / LOW / INFO

- (None detectable under current schema — all 0.)

## Cross-checks

- Duplicate `claim_id`s: **0** (field absent — undetectable by spec)
- Verdict contradictions: **0** (field absent — undetectable by spec)
- Broken cross-refs in `handoff.md`: none found in scanned files
- Falsified-but-cited: **0** found (cannot be enumerated without `verdict` field)

## Recommendation

Either:

1. **Migration path** — write a one-shot translator that promotes the legacy
   `{claim, evidence_type, script, output_hash}` records to AEAL canonical
   `{claim_id, type, statement, evidence, confidence}` entries, with `claim_id`
   synthesised as `${session_id}-${seq}` and `confidence` defaulting to `MED`. Or
2. **Re-spec path** — formally amend the AEAL schema in PCF-2 v1.3 to declare the
   actual in-use schema as canonical (with optional fields documented). Add
   `verdict` as a required field going forward.

The migration path is preferred because it preserves the auditability claim made
in PCF-1 / PCF-2 / Channel-Theory; the re-spec path retroactively weakens the
auditability claim.
