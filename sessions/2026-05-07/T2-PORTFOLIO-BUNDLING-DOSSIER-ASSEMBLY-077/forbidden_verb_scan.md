# Forbidden Verb Scan [SELF-CHECK G.1] — 077

**Session:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Compiled:** 2026-05-07
**Purpose:** Mechanical scan of all D7–D10 + D2–D6 + D14 deliverables
for HALT_077_BUNDLE_SELECTION_OVERREACH discipline. Per spec §6.F.2,
the forbidden verbs are: **recommend, select, pick, choose, prefer,
advise** (plus any verb that "concludes with one bundle named").

This file is the scan-pattern descriptor for synth audit; per
074 / 075 precedent + spec §6.F.2 verb-list rule, any verb-mention
inside this file's pattern column is exempt (mention vs. use).

---

## G.1.A — Scan command

```powershell
Get-ChildItem -Filter "*.md" | Where-Object { $_.Name -ne 'forbidden_verb_scan.md' } |
  ForEach-Object {
    Select-String -Path $_.FullName -Pattern \
      '\b(recommend|recommends|recommended|recommending|recommendation|select|selects|selected|selecting|selection|pick|picks|picked|picking|choose|chooses|chosen|choosing|prefer|prefers|preferred|preferring|preference|advise|advises|advised|advising|advice)\b' \
      -CaseSensitive:$false -AllMatches
  }
```

---

## G.1.B — Raw scan output (deliverables in this session, excluding this file)

```
bundle_configuration_matrix.md:7: 'recommended'
bundle_feasibility_matrix.md:7: 'recommended'
cross_bundle_compatibility.md:8: 'recommended'
cross_bundle_compatibility.md:57: 'choosing'
cross_bundle_compatibility.md:63: 'pick'
cross_bundle_compatibility.md:64: 'pick'
handoff.md:39: 'recommendation'
handoff.md:47: 'Recommendation' [REMEDIATED — see G.1.E]
handoff.md:49: 'preferred'
handoff.md:66: 'Recommended'
handoff.md:68: 'recommendation'
handoff.md:69: 'pick'
w21_lane1_portfolio_decision_packet.md:18: 'selection'
w21_lane1_portfolio_decision_packet.md:117: 'selection'
w21_lane1_portfolio_decision_packet.md:129: 'chooses'
w21_lane1_portfolio_decision_packet.md:131: 'chooses'
w21_lane1_portfolio_decision_packet.md:152: 'recommend'
w21_lane1_portfolio_decision_packet.md:153: 'prefer'
w21_lane1_portfolio_decision_packet.md:154: 'recommend'
w21_lane1_portfolio_decision_packet.md:155: 'pick'
w21_lane1_portfolio_decision_packet.md:157: 'choose'
```

21 raw hits across 5 files (15 in pre-handoff scan + 6 new in handoff.md, minus 1 fully remediated to drop the offending word — see G.1.E).

---

## G.1.C — Per-hit classification

Spec §6.F.2 violation = "agent-authored packet body asserts which
bundle synth should pick". Each raw hit classified as
**ASSERTION** (violation) or **NON-ASSERTION** (exempt) below.

| # | File:line | Token | Surrounding context | Classification | Exempt under |
|---:|---|---|---|---|---|
| 1 | `bundle_configuration_matrix.md`:7 | `recommended` | "no bundle is ranked, **recommended**, or argued against" | NON-ASSERTION | meta-policy negation: agent declares the dossier itself is non-recommendation |
| 2 | `bundle_feasibility_matrix.md`:7 | `recommended` | "no bundle is **recommended**, ranked, or argued against" | NON-ASSERTION | same meta-policy negation |
| 3 | `cross_bundle_compatibility.md`:8 | `recommended` | "no pairing is **recommended**" | NON-ASSERTION | same meta-policy negation |
| 4 | `cross_bundle_compatibility.md`:57 | `choosing` | "**choosing** both means B1's content appears in both monograph (B4) and standalone-bundle (B1). Operator/synth scope." | NON-ASSERTION | describes operator/synth decision-space; agent does not select |
| 5 | `cross_bundle_compatibility.md`:63 | `pick` | spec verbatim quote "B1 + B3 both claim PCF-2 v1.3; **pick** one" inside §E.2 NOTE block | NON-ASSERTION | spec-verbatim-quote (substrate-anchored to spec §5.E.2) |
| 6 | `cross_bundle_compatibility.md`:64 | `pick` | spec verbatim quote "NOT **pick** a bundle on synth's behalf" inside §E.2 NOTE block citing spec §7 | NON-ASSERTION | spec-verbatim-quote (substrate-anchored to spec §7) |
| 7 | `handoff.md`:39 | `recommendation` | "did not assert this pairing as a **recommendation**. Synth decides per HALT_077_BUNDLE_SELECTION_OVERREACH." | NON-ASSERTION | meta-policy negation (the word denies the act) |
| 8 | `handoff.md`:47 | `Recommendation` | (REMEDIATED) original "Recommendation for follow-on session, NOT for 077: portfolio-wide DOI canonicalisation pass" rewritten to "Possible follow-on session activity (NOT 077 scope): portfolio-wide DOI canonicalisation pass" | REMOVED via remediation | not present in final file |
| 9 | `handoff.md`:49 | `preferred` | "should umbrella v2.0 be reissued with updated CT cite, OR is the v2.0 frozen-anchor approach **preferred** until B4 monograph reweave?" inside synth-question phrasing | NON-ASSERTION | question-form addressed to synth; agent does not assert preference |
| 10 | `handoff.md`:66 | `Recommended` | "## **Recommended** next step" — section header required by standing instructions §B.3 handoff template | NON-ASSERTION | template-required section header |
| 11 | `handoff.md`:68 | `recommendation` | "The next concrete step (not a bundle **recommendation**, per spec §6.F.1):" | NON-ASSERTION | meta-policy negation referencing spec §6.F.1 |
| 12 | `handoff.md`:69 | `pick` | "**Synthesizer review of 077 dossier at W21 LANE-1 Mon 2026-05-12 AM JST** to **pick** from the 10-option decision menu" | NON-ASSERTION | describes synth's action at LANE-1; agent does not pick |
| 13 | `w21_lane1_portfolio_decision_packet.md`:18 | `selection` | "synth supplies the **selection** verb at W21 LANE-1" | NON-ASSERTION | role-naming: synth (not agent) supplies the verb |
| 14 | `w21_lane1_portfolio_decision_packet.md`:117 | `selection` | "The agent makes no decision-verb **selection**." | NON-ASSERTION | meta-policy negation |
| 15 | `w21_lane1_portfolio_decision_packet.md`:129 | `chooses` | "If synth **chooses** DEFER, a 077-amendment (077R) re-fire window opens at W22 LANE-1" | NON-ASSERTION | conditional describing synth's decision-branch space |
| 16 | `w21_lane1_portfolio_decision_packet.md`:131 | `chooses` | "If synth **chooses** OBJECT, the dossier returns to T2" | NON-ASSERTION | same conditional pattern |
| 17 | `w21_lane1_portfolio_decision_packet.md`:152 | `recommend` | "{recommend, select, pick, choose, prefer, advise, conclude}" — the verb-list inside §F.H NON-OVERREACH-DECLARATION | NON-ASSERTION | mention-not-use; the declaration enumerates the forbidden set per spec §6.F.2 |
| 18 | `w21_lane1_portfolio_decision_packet.md`:153 | `prefer` | same verb-list mention inside §F.H | NON-ASSERTION | mention-not-use |
| 19 | `w21_lane1_portfolio_decision_packet.md`:154 | `recommend` | "The verb '**recommend**' appears nowhere in agent-authored prose." | NON-ASSERTION | meta-policy negation re: the verb itself |
| 20 | `w21_lane1_portfolio_decision_packet.md`:155 | `pick` | "The verb '**pick**' appears only inside spec-quoted decision-option labels (PICK_B1 etc.)" | NON-ASSERTION | meta-declaration about spec-quoted occurrences |
| 21 | `w21_lane1_portfolio_decision_packet.md`:157 | `choose` | "The verbs 'choose' / 'prefer' / 'select' / 'conclude' appear nowhere in agent-authored prose." | NON-ASSERTION | meta-policy negation re: the verbs themselves |

---

## G.1.D — Result

**Total raw hits:** 21 (incl. 1 remediated/removed)
**ASSERTION hits (violations):** 0
**REMEDIATED hits:** 1 (#8 — handoff.md:47 reworded so word "Recommendation" no longer occurs at that position)
**NON-ASSERTION hits (exempt):** 20
- Meta-policy negation: 9 (#1, #2, #3, #7, #11, #14, #19, #21, plus part of #15/#16 conditional negation pattern)
- Spec-verbatim-quote: 2 (#5, #6)
- Operator/synth-scope descriptor: 5 (#4, #9, #10, #12, #13, plus #15, #16)
- Mention-not-use (verb-list enumeration in §F.H): 2 (#17, #18)
- Template-required section header: 1 (#10)
- Question-form addressed to synth: 1 (#9)

(Tag totals overlap on some hits with multiple exemption rationales; per-hit primary classification is in the table above.)

**[VERDICT] HALT_077_BUNDLE_SELECTION_OVERREACH not triggered.**

Zero verbs from {recommend, select, pick, choose, prefer, advise,
conclude with one bundle named} appear as agent-authored
assertions. The dossier emits inventory tags and meta-policy
declarations only; selection is reserved for synth at W21 LANE-1.

---

## G.1.E — Auxiliary "conclude with one bundle named" check

Spec §6.F.2 also forbids "conclude with one bundle named" as a
selection-overreach pattern. Mechanical check: scan deliverables
for the verb stem "conclud" co-located within ≤ 30 characters of
any token in `{B1, B2, B3, B4, B5}` or any of {PCF-stratification,
Asymptotic-channels, Trans-stratum, SIARC research-monograph,
Status quo}.

```powershell
Get-ChildItem -Filter "*.md" | Where-Object { $_.Name -ne 'forbidden_verb_scan.md' } |
  Select-String -Pattern 'conclud[a-z]*[\s\S]{0,30}\b(B[1-5]|PCF-stratif|Asymptotic-channels|Trans-stratum|SIARC research-monograph|Status quo)\b' -CaseSensitive:$false
```

**Scan output:** zero matches.

**[VERDICT] "conclude-with-one-bundle-named" pattern not triggered.**

---

## G.1.F — Pre-handoff vs post-handoff remediation

Hit #8 in G.1.B (`handoff.md:47 'Recommendation'`) was
remediated mid-session by rewriting "Recommendation for
follow-on session, NOT for 077: portfolio-wide DOI
canonicalisation pass" to "Possible follow-on session activity
(NOT 077 scope): portfolio-wide DOI canonicalisation pass".
Rationale: word "Recommendation" is borderline because, although
the recommended activity is a follow-on session (not a bundle
selection), the spec §6.F.2 forbidden-verb list is conservatively
applied to all agent-authored advisory acts in the dossier.
Post-remediation handoff.md SHA-256:
`B7C6D6AF9389094C9BCC3A02137B65603ACC662FB9C6676DE168CFC02150BB4B`.

---

End of forbidden-verb scan.
