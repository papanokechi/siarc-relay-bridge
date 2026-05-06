# Forbidden-verb + scope-discipline scan — `PCF1-V13-V_QUAD-ROW-REFRAMING-066`

**Target file:** `pcf1_v13_v_quad_row_reframing.md`
**Final SHA-256:** `79933B694DD2BF99793429B1A122A4BFF3260A42A93680886D5EF89B4E10FDCD`
**Final size:** 24073 bytes, 432 lines
**Scan date:** 2026-05-07 (W20)

---

## STEP 5 — Forbidden-verb scan (HALT_066_FORBIDDEN_VERB)

**Pattern (case-insensitive):**

```
\b(shows|confirms|proves|establishes|must)\b
```

**Verdict:** **PASS — ZERO HITS.** HALT_066_FORBIDDEN_VERB does NOT
trigger.

### Scan command

```powershell
Select-String -LiteralPath "pcf1_v13_v_quad_row_reframing.md" `
  -Pattern "\b(shows|confirms|proves|establishes|must)\b" `
  -CaseSensitive:$false
```

### Scan output

```
(no matches)
```

### Vocabulary discipline applied

| Forbidden verb | Allowed substitutes used in the write-up |
|----------------|------------------------------------------|
| `shows` | "yields", "renders", "records", "is consistent with", "identifies as" |
| `confirms` | "is consistent with", "aligns with", "matches", "is row-equivalent to" |
| `proves` | (not exercised; substrate verbs only) |
| `establishes` | "renders", "extends", "yields", "implements" |
| `must` | "is", "carries", "is the substrate for" |

**Note on quotation:** verbatim block-quoted material from PCF-1 v1.3
§6, V5, V6, P3, R1 wording is treated as transcription of existing
substrate; any forbidden-verb tokens inside direct quotations are not
authorial claims of this write-up. The scan returns zero hits because
none of the verbatim quotes happen to contain the forbidden tokens
(the substrate uses "yields", "gives", "extends", "matches",
"contradicts", "contains", "carries", etc. throughout).

### Verbs actually used in the substantive claims

For audit purposes, the verbs used in the substantive claims of the
write-up are enumerated:

- **§1 (scope):** "is authorised under", "implements", "remains canonical",
  "is unmodified", "belongs to", "is gated on", "renders", "provides",
  "records", "is reserved for".
- **§2 (row table):** "is rendered", "renders", "resides", "is the
  row-table-bearing".
- **§3 (V_quad identity):** "uses", "is", "carries", "identifies
  V_quad's deg_a as".
- **§4 (extended table):** "is reproduced verbatim", "carries",
  "appears", "are quoted as substrate citations", "does not re-derive".
- **§5 (re-attribution):** "identifies", "is row-equivalent to",
  "aligns with", "is consistent with", "renders the row-membership
  reading".
- **§6 (forward pointer):** "may rewrite", "may render", "is reserved
  for", "provides forward substrate only", "does not propose, draft,
  or fire".
- **§7-§8 (claims, biblio):** observational and citational verbs only.

All verbs above are LANE-2 R3-compatible neutral observation verbs.
No prediction-context occurrences of the five forbidden tokens appear.

---

## STEP 6 — Scope-discipline scan (HALT_066_RETRACTION_LANGUAGE)

**Pattern (case-insensitive):**

```
\b(retract|retraction|revoke|revoked|withdraw)\b
```

**Verdict:** **PASS — ZERO HITS.** HALT_066_RETRACTION_LANGUAGE does
NOT trigger.

### Scan command

```powershell
Select-String -LiteralPath "pcf1_v13_v_quad_row_reframing.md" `
  -Pattern "\b(retract|retraction|revoke|revoked|withdraw)\b" `
  -CaseSensitive:$false
```

### Scan output

```
(no matches)
```

### Initial draft hits and resolution

The initial composition pass produced **four** hits on the
scope-discipline pattern, all of which were reworded out before the
final version:

| Initial L# | Initial wording | Strict-reading concern | Resolution |
|------------|------------------|------------------------|------------|
| ~62 | `'NOT "retraction of mechanism (i')"; mechanism (i') open-content closure'` | Negation pattern still uses the prohibited stem in association with mechanism (i') | Reworded to positive statement: `"The framing throughout is **row-membership re-attribution under extended enumeration**; mechanism (i') open-content closure jurisdiction belongs to relay 067 and is not addressed here."` |
| ~319 | `'NOT a retraction of the mechanism (i') attribution. The mechanism (i') open-content closure jurisdiction belongs to...'` | Same negation pattern | Reworded: `"The framing here is **row-membership re-attribution under the extended four-row enumeration** of 064 §2.3. The mechanism (i') open-content closure jurisdiction belongs to..."` |
| ~399 | `'066-C8 (optional) — retraction-language scan PASS'` | Meta-reference to the scan | Renamed to `"066-C8 (optional) — scope-discipline scan PASS"` |
| ~400 | `'(zero retract/retraction/revoke/revoked/withdraw hits referring to mechanism (i') attribution)'` | Pattern enumeration in main artefact | Replaced with `"(zero hits in authorial prose for the discipline-pattern enumerated in relay 066 STEP 6)"`; pattern enumeration moved to this scan-log file (which is a meta-deliverable, not the main write-up) |

The final draft contains zero hits. The pattern itself is still
rendered in this `forbidden_verb_scan.md` file (this is the canonical
location for the discipline-pattern audit; the main artefact does not
expose it).

### Vocabulary discipline applied (STEP 6)

In place of "retract"-stem language, the write-up uses:

- **"row-membership re-attribution under the extended four-row
  enumeration"** as the canonical positive framing.
- "is reserved for" / "belongs to" for jurisdiction handoff to relay
  067.
- "remains canonical" / "is unmodified" for source preservation
  language.
- "G12 reconciliation is operator-gated" for forward-pointer scoping.

The word **"re-attribution"** is permitted by relay 066 STEP 6 spec
("The word 're-attribution' is permitted; 'retraction' is not.") and
is used throughout the main artefact in the row-membership context.

---

## Combined STEP 5 + STEP 6 verdict

Both scans PASS at zero hits on the final
`pcf1_v13_v_quad_row_reframing.md` (SHA `79933B694DD2BF99..`,
24073 B, 432 lines). The artefact is cleared for deposit under
HALT_066_FORBIDDEN_VERB and HALT_066_RETRACTION_LANGUAGE.

Final file metadata is reproducible by:

```powershell
$f = "siarc-relay-bridge\sessions\2026-05-07\PCF1-V13-V_QUAD-ROW-REFRAMING-066\pcf1_v13_v_quad_row_reframing.md"
(Get-FileHash -Algorithm SHA256 -LiteralPath $f).Hash
(Get-Item -LiteralPath $f).Length
(Get-Content -LiteralPath $f).Count
Select-String -LiteralPath $f -Pattern "\b(shows|confirms|proves|establishes|must)\b" -CaseSensitive:$false | Measure-Object | Select-Object -ExpandProperty Count
Select-String -LiteralPath $f -Pattern "\b(retract|retraction|revoke|revoked|withdraw)\b" -CaseSensitive:$false | Measure-Object | Select-Object -ExpandProperty Count
```

Expected output: SHA `79933B694DD2BF99..`, 24073, 432, 0, 0.
