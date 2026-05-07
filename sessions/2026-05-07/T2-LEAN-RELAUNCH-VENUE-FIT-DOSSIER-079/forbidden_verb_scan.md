# Forbidden-Verb Scan — T2-LEAN-RELAUNCH-VENUE-FIT-DOSSIER-079

**Scan fire time:** 2026-05-07 ~15:05 JST (post-mitigation final run)
**Scan tool:** PowerShell `Select-String -Pattern "\b<verb>\b"` over
all 12 production .md deliverables (case-insensitive, word-boundary).
**Scan-pattern-descriptor file:** this file is the canonical
descriptor. The verb-set literal below is structurally exempt from
its own scan per the relay-prompt Phase H.1 rule:

> "Set-literal echoes in scan-pattern-descriptor file structurally
> exempt."

---

## Verb set (FV-7)

The strict 7-verb scan pattern is:

- closes
- discharges
- proves
- establishes
- ratifies
- demonstrates
- shows

Inflected variants outside the strict present-tense-3rd-singular
form (e.g. "proved", "showing", "established") are NOT in the FV-7
pattern per the precedent established in 075 envelope sec 5.E.3 and
preceding 069r1 / 074 / 077 envelopes.

## Scanned files (12 production .md)

In alphabetical order:

1. cover_letter_framing_jfr.md
2. cover_letter_framing_lmcs.md
3. cover_letter_framing_mcs.md
4. cover_letter_framing_tcs.md
5. cross_venue_compatibility.md
6. submission_log_item26_splice_spec.md
7. venue_profile_jfr.md
8. venue_profile_lmcs.md
9. venue_profile_mcs.md
10. venue_profile_tcs.md
11. venue_scope_fit_matrix.md
12. w21_lane1_lean_relaunch_decision_packet.md

## Final scan output (post-mitigation)

```
Total raw hits: 0
```

ASSERTION hits in non-quoted prose: **0**.
Set-literal / scan-pattern echoes in production deliverables: **0**
(mitigated in-session per below).
Quoted-substrate echoes in > -prefixed blockquotes: **0** (the
verbatim abstract block contains "fully proved" with past-participle
form, not the present-tense "proves" in FV-7).

## In-session mitigations

Two ASSERTION hits surfaced on the first scan and were mitigated:

- `venue_profile_jfr.md` L86: "shows the latest issue ..." rewritten
  to "lists the latest issue as ...".
- `venue_profile_mcs.md` L92: "dblp shows MCS publishes regular
  special issues" rewritten to "dblp records that MCS publishes
  regular special issues".

Seven set-literal echoes surfaced in self-check footers across:

- cover_letter_framing_lmcs.md / _jfr.md / _mcs.md / _tcs.md
- cross_venue_compatibility.md
- submission_log_item26_splice_spec.md
- w21_lane1_lean_relaunch_decision_packet.md

All seven were mitigated by replacing the verbatim verb-set with
the neutral phrase "the FV-7 verb set (enumerated only in
forbidden_verb_scan.md to avoid set-literal echoes in production
deliverables)" — precedent: 075 J2 mitigation.

## Final verification

The post-mitigation final run returned **zero hits** of any FV-7
pattern across all 12 production deliverables. The
HALT_079_FORBIDDEN_VERB envelope discipline returns PASS.

This file (forbidden_verb_scan.md) is the only file in the dossier
that contains the verb-set literal. The set-literal echoes here are
structurally exempt as scan-pattern-descriptor content.
