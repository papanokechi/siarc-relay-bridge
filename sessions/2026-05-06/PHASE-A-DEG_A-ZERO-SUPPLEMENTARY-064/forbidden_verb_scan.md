# Forbidden-verb scan — `PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064`

**Target file:** `phase_a_supplementary_deg_a_zero.md`
**Scan date:** 2026-05-06 (W20)
**Pattern (case-insensitive):** `\b(shows|confirms|proves|establishes|must)\b`
**Verdict:** **PASS — ZERO HITS.** HALT_064_FORBIDDEN_VERB does NOT
trigger.

---

## Scan command

```powershell
Select-String -LiteralPath "phase_a_supplementary_deg_a_zero.md" `
  -Pattern "\b(shows|confirms|proves|establishes|must)\b" `
  -CaseSensitive:$false
```

## Scan output

```
(no matches)
```

---

## Vocabulary discipline applied

The following replacement vocabulary was used in place of the
forbidden verbs throughout the supplement:

| Forbidden verb | Allowed substitutes used |
|----------------|---------------------------|
| `shows` | "yields", "renders", "records", "is consistent with" |
| `confirms` | "is consistent with", "aligns with", "matches" |
| `proves` | "yields", "computes", "derives" (in V6 verbatim quote only — quotation, not authorial verb) |
| `establishes` | "renders", "extends", "yields" |
| `must` | "is", "carries", "is the substrate for" |

**Note on quotation:** verbatim block-quoted material from V6 + P2 +
the LANE-2 meta-verdict R3 wording is treated as transcription of
existing substrate; any forbidden-verb tokens that appear inside
direct quotations are not authorial claims of this supplement.
The scan above returns zero hits because none of the verbatim
quotes happen to contain the forbidden tokens (V6 + P2 + R3 use
"yields", "gives", "extends", "closes", "matches", and similar
neutral verbs throughout).

## Scope of permitted empirical "shows" usage (per relay 064 STEP 4)

Per relay 064 STEP 4: hits in EMPIRICAL contexts of the form "the
row-membership shows V_quad lies at deg_a=0" would be permitted, since
V_quad's identity ($a(n) = 1$, deg_a = 0) is directly observable from
`algebraic_independence_audit.py` L37 source code via
`VQUAD_ALPHA = [1]`. The supplement does not exercise this allowance
(the scan returns zero hits regardless), so no exception logging is
required.

---

## Verbs actually used in §4 row-membership claims

For audit purposes, the verbs used in the substantive claims of the
supplement are enumerated:

- §1: "extends", "remains canonical", "carries", "implemented",
  "renders", "follows from".
- §2.1: "is rendered", "are reproduced verbatim", "enumerate".
- §2.2: "yields", "records", "is the substrate".
- §2.3: "extends", "is", "ranges over", "equals".
- §3: "are derived in" (referring to V6 substrate, not authorial
  derivation), "carries", "is the rubber-duck-corrected leading-order
  observation recorded in V6".
- §4: "records", "align with", "is consistent with", "explains",
  "closes", "is the operative framing".
- §5: "has", "matching", "follows from", "sits", "aligns",
  "is the substrate for".

All verbs above are LANE-2 R3-compatible neutral observation verbs.
No prediction-context occurrences of the five forbidden tokens
appear in the supplement.

---

**STEP 4 verdict:** PASS. The supplement is cleared for deposit
under HALT_064_FORBIDDEN_VERB.
