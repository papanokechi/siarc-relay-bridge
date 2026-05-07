# [FORBIDDEN-VERB-SCAN] — Relay 074 Phase F.1 self-check

**Task ID:** `T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074`
**Phase:** F.1 (forbidden-verb scan)
**Date:** 2026-05-07 (W20)
**Result:** `PASS 5/5` (zero literal hits across 5 agent-authored
deliverables under the strict-token interpretation of §5.E.2)

---

## F.1.1 Token list (literal §5.E.2)

Forbidden verbs (third-person singular present, per §5.E.2):

    {asserts, proves, closes, demonstrates, establishes, ratifies}

Per §5.E.2 permitted set:

    {presents, surfaces, assembles, requests, defers}

Per §7 envelope: `HALT_074_DISPATCH_LANGUAGE_OVERREACH` triggers if
ANY literal forbidden token appears in the agent-authored body of
`w21_lane1_m4_dispatch_packet.md`. Scope is the dispatch packet body;
per §6 the other deliverables permit verbatim ≤ 50-word quotes from
substrate even if they contain forbidden tokens.

## F.1.2 Per-file scan result

| File | Literal hits |
|---|---|
| `m4_substrate_inventory.md` | 0 |
| `m4_substrate_anchor_shas.md` | 0 |
| `m4_claim_chain.md` | 0 |
| `m4_residual_questions.md` | 0 |
| `w21_lane1_m4_dispatch_packet.md` | 0 |

Scan command (PowerShell 7.x; case-insensitive `\b<token>\b` boundary
match per `(?i)\b$v\b`):

```
$strictTokens = @('asserts','proves','closes','demonstrates',
                  'establishes','ratifies');
foreach ($f in @(<5 files>)) {
  Get-Content -LiteralPath $f | ForEach-Object { ... }
}
```

Aggregate: **0 hits across 5 files**.

## F.1.3 Verbatim-quote-exemption applicability

Per §5.E.2: "The ONE permitted verbatim quote of an over-claiming
verb is the 068 handoff §Verdict quote."

The 068 handoff §Verdict verbatim quote appears EXACTLY ONCE in the
dispatch packet body (`w21_lane1_m4_dispatch_packet.md` §E.2 L37-43)
and contains the past-participle token "PROVEN" (068 verbatim). The
strict §5.E.2 forbidden token list `{asserts, proves, closes,
demonstrates, establishes, ratifies}` does NOT contain "PROVEN" as
a literal entry (it contains the 3sg present "proves"). The 068
verbatim quote thus does not literally trigger the halt under strict
interpretation, AND it sits within the §5.E.2-permitted exemption
slot regardless of strict/broad interpretation.

The same handoff §Verdict quote also appears in:
- `m4_substrate_inventory.md` §B.1.1 L28-L33 (substrate-inventory
  entry; allowed under §6 verbatim-quote rule).
- `m4_claim_chain.md` §C.1 L33-L38 (top-claim citation; allowed
  under §6 verbatim-quote rule).

Both occurrences are within the §6-allowed quote scope; the
§5.E.2 ONE-quote rule is dispatch-packet-scoped only.

## F.1.4 Spec-mandated decision-tag tokens

`w21_lane1_m4_dispatch_packet.md` §E.5 enumerates the four decision-
tag labels mandated by §5.E.1 of the relay 074 prompt:

    RATIFY / RATIFY_WITH_AMENDMENT / DEFER / OBJECT

These are ALL-CAPS bare-verb / noun-phrase labels, NOT 3sg present
verbs. The literal token "ratifies" does NOT match "RATIFY" under
the `(?i)\b<token>\b` boundary scan because "RATIFY" lacks the "-es"
suffix.

The §5.E.1 spec mandates these exact tag spellings; the agent does
not have license to substitute synonyms.

## F.1.5 Broad-pattern hits (informational only)

Under a broad-pattern scan that also matches `assert`, `assertion`,
`prove`, `proven`, `close`, `closure`, `demonstrate`, `establish`,
`ratify`:

| File | Broad hits |
|---|---|
| `m4_substrate_inventory.md` | 8 (all in inventory entries citing source filenames containing "CLOSURE" or in "M4 closure-path" project-canonical noun phrases or in M6.CC out-of-scope cross-reference labels) |
| `m4_substrate_anchor_shas.md` | 18 (all in source filenames containing "CLOSURE" or in PROVEN within the verbatim 068 §Verdict quote at §3.1) |
| `m4_claim_chain.md` | 2 (one in `[CLAIM-M0]` structural-label paraphrase; one PROVEN inside the 068 verbatim §Verdict quote) |
| `m4_residual_questions.md` | 12 (all in question labels carrying source-substrate verbatim phrasing or in M6.CC cross-reference labels) |
| `w21_lane1_m4_dispatch_packet.md` | 8 (all in spec-mandated decision-tag labels {RATIFY, RATIFY_WITH_AMENDMENT, DEFER, OBJECT} or in negation context "does NOT assert" / "does NOT propose" or in project-canonical "M4 closure-path" noun phrases or in PROVEN inside the verbatim 068 §Verdict quote) |

**Disposition:** broad-pattern hits are NOT halt triggers under §5.E.2
strict literal interpretation. They are surfaced here for transparency.
Each broad-pattern hit category is one of:

1. **Source filename token** (e.g., `T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068`,
   `M6-CC-R1-CLOSURE-PREFLIGHT-069R1`, `D2-NOTE-V2-1-WASOW-FULL-CLOSURE`);
   not 074-authored prose.
2. **Verbatim 068 §Verdict quote** containing past-participle "PROVEN";
   §5.E.2-exempt.
3. **Project-canonical noun phrase** "M4 closure-path" / "closure
   mechanism" / "closure framing" used in titles, section headers,
   and substrate references; not a 3sg present verb.
4. **Spec-mandated decision-tag labels** RATIFY / RATIFY_WITH_AMENDMENT
   / DEFER / OBJECT per §5.E.1; required spelling.
5. **Negation context** "does NOT assert" / "does NOT propose";
   meta-policy declaration about scope.

## F.1.6 File-level scan-report exemption (072 precedent)

The two files `forbidden_verb_scan.md` (this file) and `handoff.md`
contain scan-policy-recital text that literally cites the §5.E.2
forbidden token list as the scan target (e.g., the F.1.1 token list
above and the F.1.5 broad-pattern recital). Per the 072 precedent
recorded in 072 forbidden_verb_scan.md F.1's "scan-report" file-level
exemption category, these files are tagged "scan-report" and are
exempt from the §5.E.2 dispatch-packet-body halt scope.

A naive case-insensitive `(?i)\b<token>\b` scan returns:
- `forbidden_verb_scan.md` — 20 hits (all in F.1.1 token list, F.1.2
  scan command, F.1.3-F.1.4 meta-discussion citing tokens by name,
  F.1.5 broad-pattern recital).
- `handoff.md` — 8 hits (all in §"Key numerical findings" L41-42,
  §"Judgment calls made" L81 + L86, citing the scan-policy token
  list or describing the in-session forbidden-token edit).

All 28 hits are scan-policy recital, not over-claiming usage. Per
§5.E.2 the halt scope is the dispatch-packet body; per §6 quotes
from scan-policy are meta-policy declarations about scope.

`w21_lane1_m4_dispatch_packet.md` (the in-scope file) returns
**0 literal hits** at fire-time SHA `B45B595A50A71D9C…`.

## F.1.7 Halt-evaluation summary

| Halt code | Triggered? |
|---|---|
| `HALT_074_DISPATCH_LANGUAGE_OVERREACH` | NO (0 literal hits in dispatch packet body) |

Phase F.1 self-check **PASS**.

---

*End of `forbidden_verb_scan.md`.*
