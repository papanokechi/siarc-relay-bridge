# Phase F.1 — Forbidden-Verb Self-Check (envelope §5.E.3 strict 7-verb scan)

**Session:** 075 T2-M6-CC-CHART-MAP-CANDIDATE-B1-CHECK
**Phase:** F.1
**Discipline anchor:** envelope §5.E.3 (HALT_075_R1_CLOSURE_OVERREACH).

---

## Pattern

Per envelope §5.E.3, the strict pattern is the third-person-singular
forms of the seven over-claiming verbs:

| index | verb form     |
|-------|---------------|
| 1     | `closes`      |
| 2     | `discharges`  |
| 3     | `proves`      |
| 4     | `establishes` |
| 5     | `ratifies`    |
| 6     | `demonstrates`|
| 7     | `shows`       |

Regex (case-insensitive, word-boundary-safe):
`\b(closes|discharges|proves|establishes|ratifies|demonstrates|shows)\b`.

Per envelope §5.E.3, the scan applies to "agent-authored
synthesizer-decision-packet body". 075 extends the scan to **all
markdown deliverables** in this session as a defensive policy
(precedent: 069r1 `forbidden_verb_scan.md` STEP E.1 cross-deliverable
extension).

## Permitted exceptions

Per envelope §6:
- ONE permitted verbatim quote of an over-claiming verb is the
  069r1 handoff §A.1.5 quote. The 075 instance of this permitted
  quote is `synthesizer_decision_packet.md` §E.3 verbatim
  blockquote (28 words; past-participle "closed" appears once
  inside the quote). The strict §5.E.3 pattern targets the
  third-person-singular form `closes` (not the past-participle
  `closed`), so this exception is technically narrower than the
  075 envelope rule; the 075 scan recorded both pattern
  observations for hygiene.

## Initial scan (pre-mitigation, fire-time pass 1)

Run via PowerShell `Select-String -Pattern …` over all `*.md`
deliverables in the session directory.

| file                                          | hits | matched tokens                                                                |
|-----------------------------------------------|-----:|-------------------------------------------------------------------------------|
| `chart_map_required_form.md`                  | 0    | —                                                                             |
| `bt_5_13a_structural_form.md`                 | 0    | —                                                                             |
| `structural_match_matrix.md`                  | 0    | —                                                                             |
| `synthesizer_decision_packet.md` (pre-fix)    | 14   | scan-pattern set-literal echoes (×2 occurrences of the 7-verb set)            |
| `substrate_anchor_shas.md`                    | 0    | —                                                                             |
| `quote_length_scan.md`                        | (run after F.2 completes; expected 0)                                          |
| `handoff.md`                                  | (run after handoff.md drafted; expected 0)                                     |

The 14 hits in pre-fix `synthesizer_decision_packet.md` were two
explicit set-literal listings of the seven verbs (`{closes,
discharges, proves, establishes, ratifies, demonstrates, shows}`)
appearing in the §E body and §E.4 surfacing-block disclaimer. These
are scan-pattern descriptors (precedent: 069r1 `forbidden_verb_scan.md`
allowed-exception "lines containing the words 'forbidden' or
'HALT_071_FORBIDDEN' (these are scan-pattern descriptors, not
predictions)"), but the 075 envelope §5.E.3 does **not** explicitly
grant this exception. To eliminate any ambiguity, the two set-literal
echoes were rewritten in `synthesizer_decision_packet.md` to indirect
references: "the seven over-claiming verbs enumerated in the §5.E.3
forbidden-verb set" and "the seven third-person-singular forms
enumerated in the §5.E.3 forbidden-verb set", with the explicit
set-literal recorded only here in `forbidden_verb_scan.md` §F.1
(this file).

## Re-scan (post-mitigation, fire-time pass 2)

| file                                          | hits | matched tokens |
|-----------------------------------------------|-----:|----------------|
| `chart_map_required_form.md`                  | 0    | —              |
| `bt_5_13a_structural_form.md`                 | 0    | —              |
| `structural_match_matrix.md`                  | 0    | —              |
| `synthesizer_decision_packet.md`              | 0    | —              |
| `substrate_anchor_shas.md`                    | 0    | —              |
| `quote_length_scan.md`                        | 0    | —              |
| `handoff.md`                                  | 0    | —              |

**Total post-mitigation hits across all `.md` deliverables: 0.**

`HALT_075_R1_CLOSURE_OVERREACH` not triggered.

## Cross-deliverable extension scan (069r1 precedent; not envelope-required)

A more aggressive inflection scan
(`\b(close[ds]?|closing|discharg(e[ds]?|ing)|prov(e[ds]?|ing)|establish(es|ed|ing)?|ratif(y|ies|ied|ying)|demonstrat(e[ds]?|ing)|show(s|ed|ing|n)?)\b`,
matching past tenses + gerunds + root forms) was run for hygiene.
Hits:

| file                                  | match (token/line)                                                   | classification                                                                                  |
|---------------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `chart_map_required_form.md` L32      | `closed` inside verbatim 069r1 phase_a_path_alpha.md §1.5 quote      | verbatim-quote permitted; substrate-cited                                                       |
| `chart_map_required_form.md` L44      | `closed` inside verbatim 058R `phase_b_canonical_map.md` L136-140 quote | verbatim-quote permitted; substrate-cited                                                       |
| `chart_map_required_form.md` L48      | `closed` in disclosure note ("permitted occurrence of 'closed'")     | scan-pattern descriptor                                                                         |
| `chart_map_required_form.md` L88      | `closed-form` adjective compound                                     | mathematical adjective; not a verb form                                                         |
| `chart_map_required_form.md` L145     | `closed-form` adjective compound (table row)                         | mathematical adjective; not a verb form                                                         |
| `chart_map_required_form.md` L155-157 | `closed` (×2) inside Phase B.4 discipline reassertion ("does not assert R1 is closed") | disclaimer / non-prediction; past-participle predicate adjective                                |
| `bt_5_13a_structural_form.md` L117    | `closed-form` adjective compound                                     | mathematical adjective                                                                          |
| `bt_5_13a_structural_form.md` L189    | `closed` in Phase C.5 discipline reassertion ("not assert that R1 is closed") | disclaimer / non-prediction                                                                     |
| `structural_match_matrix.md` L19      | `closed-form` adjective compound (table row)                         | mathematical adjective                                                                          |
| `structural_match_matrix.md` L42      | `closed-form` adjective compound (justification text)                | mathematical adjective                                                                          |
| `structural_match_matrix.md` L103     | verbatim envelope §4.D.3 quote ("closure discharge requires T1 synthesis") | envelope verbatim; "discharge" is root form, not third-person-singular `discharges`             |
| `structural_match_matrix.md` L109     | `closed` in §D.4 discipline reassertion ("not an assertion that R1 cannot be closed by any path") | disclaimer / non-prediction                                                                     |
| `synthesizer_decision_packet.md` §E.3 | `closed` inside permitted verbatim quote from 069r1 handoff §A.1.5   | THE one permitted verbatim quote per envelope §6                                                |

**Total third-person-singular hits (envelope §5.E.3 strict scan):
0 in all deliverables. PASS.**

The aggressive inflection scan hits are all classified as either
(a) verbatim substrate quotes, (b) mathematical-adjective compounds
(`closed-form`), (c) past-participle predicate-adjective usage
inside disciplinary disclaimers ("does not assert R1 is closed"),
or (d) the ONE permitted verbatim quote from 069r1 handoff §A.1.5
in the synthesizer-decision-packet body (per envelope §6 rule).

None of the aggressive-inflection hits trigger
HALT_075_R1_CLOSURE_OVERREACH at the envelope §5.E.3 strict scope.

## §F.1 verdict

`HALT_075_R1_CLOSURE_OVERREACH` not triggered. Strict scan clean
(0 hits) across all 7 markdown deliverables in the 075 session
directory.

End of `forbidden_verb_scan.md`.
