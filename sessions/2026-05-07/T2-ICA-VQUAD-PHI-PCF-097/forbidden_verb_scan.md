# Forbidden-verb deposit-gate scan — 097 deliverables

**Relay:** 097 T2-ICA-VQUAD-PHI-PCF

**Scan scope:** the 5 substrate-claim-bearing production `.md`
files (`audit_verdict.md`, `compositional_error_budget.md`,
`pcf_identity_cross_walk.md`, `phi_cross_walk.md`,
`vquad_cross_walk.md`) plus `handoff.md`. This scan summary file
(`forbidden_verb_scan.md`) is **excluded** from the scan target
because it necessarily reproduces the forbidden-verb set as data
(regex pattern + per-set listing) for the audit record.

**Scan command:**
```powershell
$pat = '\b(shows|confirms|proves|establishes|ratifies|demonstrates|discharges)\b'
Get-ChildItem *.md | ForEach-Object {
    Select-String -Path $_.FullName -Pattern $pat -CaseSensitive:$false
}
```

**Forbidden-verb set:** `{shows, confirms, proves, establishes, ratifies, demonstrates, discharges}` (case-insensitive, word-boundary, present-tense -s forms only per `.github/copilot-instructions.md` §STANDING).

---

## Per-file results

| File | Status |
|---|---|
| `audit_verdict.md` | PASS (0 hits) |
| `compositional_error_budget.md` | PASS (0 hits) |
| `handoff.md` | PASS (0 hits) |
| `pcf_identity_cross_walk.md` | PASS (0 hits) |
| `phi_cross_walk.md` | PASS (0 hits) |
| `vquad_cross_walk.md` | PASS (0 hits) |

**Aggregate:** **6 of 6 PASS, 0 hits.**

`HALT_097_FORBIDDEN_VERB_DETECTED`: **NOT TRIGGERED.**

## Quote-length scan

Cross-walk inspection (manual): longest verbatim quote across the
5 production .md files is the PCF-1 v1.3 §6 Theorem 5 leading-term
identity reproduced in `pcf_identity_cross_walk.md` §1.5 (the
$\log|\delta_n| = \ldots$ block and adjacent prose; ~33 words
including the math display).

**50-word threshold:** under by 17 words.
`HALT_097_QUOTE_LENGTH_VIOLATION`: **NOT TRIGGERED.**

End forbidden_verb_scan.md.
