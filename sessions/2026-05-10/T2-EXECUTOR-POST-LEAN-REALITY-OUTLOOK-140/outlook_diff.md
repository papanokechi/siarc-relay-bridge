# Outlook diff -- PATH_B_COMPLETE -> POST_LEAN_REALITY (section 5 only)

**Predecessor:** `M1_M12_CLOSURE_OUTLOOK_20260510_PATH_B_COMPLETE.md` (preserved unedited)
**Successor:** `M1_M12_CLOSURE_OUTLOOK_20260510_POST_LEAN_REALITY.md` (this fire's deliverable)
**Diff scope:** section 5 ("Decision matrix") row-level comparison
**Conclusion:** ONLY the M10 status-taxonomy row changes semantically; all other rows are functionally identical (cosmetic ASCII normalization only, logged as `D-140-1` INFO).

---

## 1. Predecessor section 5 (PATH_B_COMPLETE.md)

```
| Decision | Axis | Recommendation | Compression effect |
|---|:---:|---|---|
| ~~PATH_alpha vs PATH_beta for slot 136~~ | ~~M9~~ | ~~PATH_alpha~~ | resolved -- PATH_alpha applied at slot 136 fire   [ROW 1: SLOT-136 RESOLVED]
| **M10 status taxonomy** | M10 | recommend separate axis (clean V0 closure cascade mirroring M7/M8a/M8b 3-arc template) | **unlocks RULE 1 lift gate**   [ROW 2: M10 -- SUPERSEDED]
| Q22 final-disposition note | M2 | recommend collapse-to-no-op given slot 137 substantive absorption | trivial residual close   [ROW 3: Q22]
| `.fleet.yaml` commit timing | meta | recommend standalone commit now (slot-136-landed + slot-137-landed metadata both injected; YAML re-validates clean) | housekeeping; low-risk   [ROW 4: FLEET YAML]
| PCF-2 concept-DOI paste-verify | M2 | confirm `19936297` (NOT `19937196` = PCF-1 v1.3) before any v1.4 Zenodo deposit | prevents publish-with-wrong-DOI failure mode (UF-137-6)   [ROW 5: DOI VERIFY]
```

(Note: predecessor used unicode `alpha` = U+03B1, `beta` = U+03B2, em-dash U+2014, U+2705 check-mark; rendered above as ASCII for diff-readability.)

---

## 2. Successor section 5 (POST_LEAN_REALITY.md)

### Section 5.1 (preserved rows -- functionally unchanged from predecessor)

```
| ~~PATH_alpha vs PATH_beta for slot 136~~ | ~~M9~~ | ~~PATH_alpha~~ | resolved -- PATH_alpha applied at slot 136 fire   [ROW 1: identical semantics; ASCII normalization only]
| Q22 final-disposition note | M2 | recommend collapse-to-no-op given slot 137 substantive absorption | trivial residual close   [ROW 3: identical]
| `.fleet.yaml` commit timing | meta | recommend standalone commit now (slot-136-landed + slot-137-landed metadata both injected; YAML re-validates clean) | housekeeping; low-risk   [ROW 4: identical]
| PCF-2 concept-DOI paste-verify | M2 | confirm `19936297` (NOT `19937196` = PCF-1 v1.3) before any v1.4 Zenodo deposit | prevents publish-with-wrong-DOI failure mode (UF-137-6)   [ROW 5: identical]
```

### Section 5.2 (replacement for ROW 2 = M10 -- three-sub-option matrix)

```
| Sub-option | Definition | RULE 1 lift mechanics | Synth view | Operator action |
|---|---|---|---|---|
| SEPARATE-AXIS-NOW | Fire M10 V0 closure cascade (3-arc template; mirrors M7 / M8a / M8b) before RULE 1 lift | direct lift after closure-statement absorption | NOT recommended (premature; lean/ mid-iteration per section 1) | slot 141 = MOVE_A T2-Executor M10 V0 substrate-prep |
| SEPARATE-AXIS-DEFERRED | M10 V0 closure cascade fires AFTER M9 V0 announcement deposits land; lift authorized via documented commitment | indirect lift via cascade-132 section 5 documented-commitment precedent | reasonable alternative | slot 141 = T2-Executor scaffold m10_documented_commitment.md |
| BUNDLED-DEFERRED-NOTE (== DEFERRED-OUT-OF-M9-SCOPE) | M10 declared post-RULE-1-lift work-stream; operator-issued one-paragraph commitment authorizes lift; no closure cascade fires for M10 in M9 V0 announcement scope | direct lift via documented commitment | RECOMMENDED (slot 139 verdict section 4 MEDIUM-HIGH) | slot 141 = T2-Executor scaffold m10_documented_commitment.md + .fleet.yaml commitments: YAML block |
```

---

## 3. Per-row delta classification

| Row | Predecessor recommendation | Successor recommendation | Semantic change? | Cosmetic change? |
|:---:|---|---|:---:|:---:|
| 1 (slot-136 PATH) | resolved (PATH_alpha applied) | resolved (PATH_alpha applied) | NO | YES (alpha/beta unicode -> ASCII; em-dash -> `--`; check-mark emoji removed) |
| 2 (M10 status) | recommend separate axis | three-sub-option matrix; operator-pending; no pre-selection | **YES** (replaced) | n/a -- replacement |
| 3 (Q22) | collapse-to-no-op | collapse-to-no-op | NO | minor (em-dash -> `--`) |
| 4 (.fleet.yaml) | standalone commit now | standalone commit now | NO | minor (em-dash -> `--`) |
| 5 (PCF-2 DOI) | confirm `19936297` not `19937196` | confirm `19936297` not `19937196` | NO | minor (em-dash -> `--`) |

**Net:** 1 of 5 rows changes semantically (M10 row, replaced with three-sub-option matrix per slot 139 verdict). 4 of 5 rows preserved with cosmetic ASCII normalization only (logged as `D-140-1` INFO; no remediation needed).

---

## 4. Author-tier note

The replacement of the M10 row is the operative content delta this fire produces. The synth view column in section 5.2 records the slot 139 single-witness MEDIUM-HIGH verdict's stance per row (`SEPARATE-AXIS-NOW` -> NOT recommended; `SEPARATE-AXIS-DEFERRED` -> reasonable alternative; `BUNDLED-DEFERRED-NOTE` -> RECOMMENDED). No sub-option is pre-selected by this fire; operator picks at slot 141 fire-time.

The predecessor `_PATH_B_COMPLETE.md` is preserved unedited; supersession is by reference (header SUPERSESSION NOTICE block in successor) per prompt 140 SECTION 3 hard-guardrail "edit M1_M12_CLOSURE_OUTLOOK_20260510_PATH_B_COMPLETE.md (it is preserved as-is; new doc supersedes by reference, not by editing predecessor)".
