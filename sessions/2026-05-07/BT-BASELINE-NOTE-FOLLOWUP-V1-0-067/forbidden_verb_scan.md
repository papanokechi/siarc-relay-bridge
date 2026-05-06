# Forbidden-verb / retraction-language / W21-vocab self-check log
# Relay 067 — BT-BASELINE-NOTE-FOLLOWUP-V1-0
# Date: 2026-05-07

## STEP 4 — HALT_067_FORBIDDEN_VERB

**Regex:** `\b(shows|confirms|proves|establishes|must)\b` (case-sensitive)

**Target file:** `bt_baseline_note_followup_v1_0.tex`
(SHA-256 `F11F8A6519D6FE65720F6E1789E7D4CE456AF4A9A0F9C431072F2C148F60B023`,
18161 bytes)

**Tool:** PowerShell `Select-String -Pattern '\b(shows|confirms|proves|establishes|must)\b' -CaseSensitive`

**Result:** **PASS — 0 hits.**

```
PS> Select-String -Path "bt_baseline_note_followup_v1_0.tex" \
       -Pattern '\b(shows|confirms|proves|establishes|must)\b' -CaseSensitive
(no output)
```

The conservative discipline (zero total hits, not just zero
prediction-context hits) was applied per J5; no ambiguity over
"prediction context" classification is possible.

Substituted verbs used in 067 (records / states / observes /
captures / asserts / identifies / reads / takes / carries /
aligns / admits / addresses / supports). Same scan discipline
as 066 STEP 5 PASS-at-0-hits.

## STEP 5 — HALT_067_RETRACTION_LANGUAGE

**Regex:** `\b(retract|retraction|revoke|revoked|withdraw|supersede|superseded|deprecate|deprecated|wrong|incorrect)\b` (case-sensitive)

**Target file:** `bt_baseline_note_followup_v1_0.tex`

**Tool:** PowerShell `Select-String -Pattern <regex> -CaseSensitive`

**Result:** **PASS — 0 hits.**

```
PS> Select-String -Path "bt_baseline_note_followup_v1_0.tex" \
       -Pattern '\b(retract|retraction|revoke|revoked|withdraw|\
                  supersede|superseded|deprecate|deprecated|\
                  wrong|incorrect)\b' -CaseSensitive
(no output)
```

Non-retraction discipline maintained: bt_baseline_note v1.0
Theorem 1.1 framing in 067 §1 reads "canonical as stated for
the band $\dega \in \{d-1, d, d+1\}$" and the additive content
is described as "additive extension", "row-membership
re-attribution under extended enumeration", "open-content
closure under deg_a = 0 row reading". v1.0 §4.2 mechanism (i')
prose is described as "forward-looking open-conjecture
content as v1.0 itself flags it" with the closure resolved
"via a row-membership reading", not as a correction.

## STEP 6 — HALT_067_W21_VOCAB_DRIFT

**Tool:** PowerShell `Select-String -Pattern 'protocol-to-stratum mismatch'`

**Target file:** `bt_baseline_note_followup_v1_0.tex`

**Result:** **PASS — 1 occurrence + 1 footnote.**

```
PS> Select-String -Path "bt_baseline_note_followup_v1_0.tex" \
       -Pattern 'protocol-to-stratum mismatch'
LineNumber Line
---------- ----
       337 The descriptive term ``protocol-to-stratum mismatch'' (the gap

PS> Select-String -Path "bt_baseline_note_followup_v1_0.tex" \
       -Pattern 'pending W21'
LineNumber Line
---------- ----
       343 pending W21 canonical T1-Synth (LANE-1) rule5-vocabulary
```

The single occurrence at L337 is followed (on the same source
paragraph) by an explicit `\footnote` block at L342–344
reading verbatim:

> "Term pending W21 canonical T1-Synth (LANE-1)
> rule5-vocabulary ratification per LANE-2 Item 4 verdict
> `DEFER_TO_W21`."

The footnote citation is `\cite[Item~4, L210--213]{lane2_six_item_verdict}`
which anchors the deferral to the LANE-2 reasoning at
`lane2_six_item_verdict.md` L210–213.

## Summary

| Gate                              | Result | Notes                          |
|-----------------------------------|--------|--------------------------------|
| HALT_067_FORBIDDEN_VERB           | PASS   | 0 hits (case-sensitive)         |
| HALT_067_RETRACTION_LANGUAGE      | PASS   | 0 hits (case-sensitive)         |
| HALT_067_W21_VOCAB_DRIFT          | PASS   | 1 occurrence + 1 footnote       |
| HALT_067_LATEX_BUILD_FAIL         | PASS   | 5pp PDF; zero Undefined/Error   |
| HALT_067_BT_BASELINE_DRIFT (P5)   | PASS   | v1.0 .tex SHA unchanged         |
| HALT_067_LANE2_DRIFT (P2)         | PASS   | LANE-2 SHAs match               |
| HALT_067_064_065_DRIFT (P3)       | PASS   | 064 + 065 SHAs match            |
| HALT_067_066_NOT_LANDED (P4)      | PASS   | 066 LANDED at HEAD `9261c79`    |
| HALT_067_GROUNDING_PARTIAL        | PASS   | rule5 grounding complete        |
| HALT_067_RE_DERIVATION            | PASS   | §3 / §4 verbatim quotes only    |
| HALT_067_PCF1_V14_SCOPE_CREEP     | PASS   | v1.4 forward-pointer only       |
| HALT_067_PB4_SCOPE_CREEP          | PASS   | P-B4 explicitly out of scope    |
