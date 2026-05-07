# Bridge Attribution Audit — Phase D.P5

**Relay:** 084-AMEND (T1; OPTION B follow-up onto landed 084)
**Date (JST):** 2026-05-07
**Bridge HEAD at fire time:** `dbe7a71`

---

## D.P5.1 — Search for own-record arXiv: patterns in bridge handoffs

**Search.** Regex `arXiv:\s*\d{4}\.\d{4,5}` and
`arxiv\.org/abs/\d{4}\.\d{4,5}` against
`siarc-relay-bridge/sessions/**/handoff.md` (also-pulled: any `*.md`
in those session directories that cites an arXiv ID).

**Result.** 13 hits across 4 distinct session folders. ALL 13 hits
resolve to **external citations**:

| Session folder | arXiv ID(s) cited | Role |
|---|---|---|
| `2026-05-07/T2-R5-LIT-HUNT-TRIANGULATION-086/` | `2307.11217` (V1 Barhoumi-Lisovyy-Miller-Prokhorov 2024); `1604.03082` (V2 Its-Lisovyy-Prokhorov 2018) | substrate-anchor literature for T2 R5 lit-hunt; pre-verified at fire time per post-031 rule |
| `2026-05-04/WITTE-FORRESTER-2010-ACQUISITION/` | `0911.1762` (Desrosiers-Eynard 2009; substituted for hallucinated WF target) | lit-hunt anchor (031 verdict precedent) |
| `2026-05-04/ENDORSER-HANDLE-ACQUISITION/` | `2603.25506` (Zudilin); `2407.17366` + `2405.10541` (Mazzocco); `2412.04241` + `1712.04887` (Garoufalidis) | endorser-handle confirmation papers |
| `2026-05-04/NOUMI-YAMADA-2004-ACQUISITION/` | `1509.08186` (KNY 2017) | lit-hunt anchor |

**Verdict:** zero own-record arXiv: references in bridge handoffs.
Bridge attribution is CLEAN.

## D.P5.2 — Search for own-record arXiv: patterns in submission_log.txt

**Search.** Pattern `arXiv:\s*\d{4}\.\d{4,5}` against
`tex/submitted/submission_log.txt`.

**Result.** Zero matches.

The single `arXiv` substring in the file (line 212) is "Filename:
pcf_unified_arxiv.pdf", a local PDF filename, not a published-record
ID.

**Verdict:** submission_log.txt attribution is CLEAN.

## D.P5.3 — Future-state amendment-table framework

When the first own-record arXiv ID lands (e.g. PCF-1 v1.3 first
to math.NT per 084 J6 recommendation), the operator will need to
back-fill arXiv-attribution prose in already-landed handoffs.

The mechanical rule is:

- **SHA-anchored references survive.** Every existing bridge
  handoff `tex/submitted/submission_log.txt` reference to a
  Zenodo record is keyed by Zenodo DOI + MD5 + SHA-256 + size +
  page count. None of these depend on arXiv ID. **No SHA anchor
  breaks** when an arXiv ID is later assigned.
- **Human-readable attributions may need amendment.** When the
  manuscript later gets cited as both a Zenodo deposit AND an
  arXiv preprint, prose like "PCF-1 v1.3 (Zenodo
  10.5281/zenodo.19937196)" should be amended to "PCF-1 v1.3
  (arXiv:NNNN.NNNNN; Zenodo 10.5281/zenodo.19937196)".
- **Append-only convention.** Per SIARC instructions §STANDING B3
  ("never write handoff before the last run"), already-landed
  handoffs SHOULD NOT be modified retroactively. The arXiv-ID
  attribution is added as a new entry in the next forward
  handoff or the next CMB.txt amendment block, with a
  back-pointer to the original landed handoff by SHA.

This means the bridge attribution audit at re-fire time will be
**not** a back-edit task — it is a forward-pointer-collation
task: produce a single `bridge_attribution_supplement.md` listing
each pre-arXiv-ID-landing handoff that references a now-arXiv-
attached record, with a one-line "SHA-anchor invariant; arXiv ID
was issued at <date>" annotation.

## D.P5.4 — Records most likely to need supplements at first arXiv landing

Per the Zenodo `related_identifiers` field of the two spot-checked
records (R2 PCF-1 v1.3 + R3 PCF-2 v1.3), neither has an arXiv-side
related-identifier today (re-confirmed via live API at audit time).
Once an arXiv ID is added on the Zenodo side via the
"Add related identifier ... arXiv" Zenodo edit-flow described in
RUNBOOK §_post_submission, the chain that needs forward-pointer
attribution is:

| Record | High-fanout citing handoffs (count of references in bridge SHAs/DOIs) |
|---|---|
| R2 PCF-1 v1.3 (concept DOI `10.5281/zenodo.19931635`; version DOI `10.5281/zenodo.19937196`) | high — cited by `BT-BASELINE-NOTE-FOLLOWUP-V1-0-067/` substrate_anchor_shas.md, annotated_bibliography_followup.bib, multiple PCF-1 leg handoffs in 2026-05-01 / 2026-05-02 / 2026-05-03 / 2026-05-04 / 2026-05-06 / 2026-05-07 sessions, plus `T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077/` paper_profile_pcf1_v13.md L14 |
| R3 PCF-2 v1.3 (concept DOI `10.5281/zenodo.19936297`; version DOI `10.5281/zenodo.19963298`) | high — cited by `T2-M9-V0-SUBSTRATE-PRE-STAGE-096/` phi_assignment_statement.md L50, `BT-BASELINE-NOTE-FOLLOWUP-V1-0-067/` substrate_anchor_shas.md, multiple PCF-2 session handoffs in 2026-05-01 / 2026-05-02 / 2026-05-04 / 2026-05-06 / 2026-05-07 sessions, plus `T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077/` paper_profile_pcf2_v13.md L14 |
| R4 CT v1.3 (version DOI `10.5281/zenodo.19972394`) | medium — cited by paper_profile_ct_v13.md L16, multiple CT-leg handoffs |
| R1 SIARC umbrella v2.0 (version DOI `10.5281/zenodo.19965041`) | medium-low — cited by paper_profile_umbrella_v20.md L14, picture milestone cross-walks |
| R5 T2B v3.0 (version DOI `10.5281/zenodo.19915689`) | medium — cited by submission_log.txt Item 22 chain (Adamczewski rejection content-mute), paper_profile_t2b_v30.md L18; complicated by D-077-4 inherited DOI inconsistency (CMB.txt L31 anchors older v2.x DOI 19801038) |

**Recommendation.** The audit re-fire after the first arXiv ID lands
should produce a single `bridge_attribution_supplement.md`
back-pointing to each row above. The supplement is forward-only;
no retroactive handoff edits are needed because all existing SHA +
DOI anchors are content-keyed and **invariant** under arXiv ID
assignment.

## D.P5.5 — Conclusion

Bridge attribution audit verdict: **CLEAN_PRE_ARXIV_LANDING**.

No own-record arXiv: prose reference exists in the bridge today, so
nothing can be drift-broken by a later arXiv metadata change. The
audit framework's next-fire action item (`bridge_attribution_supplement.md`)
is enumerated above and ready to populate at first arXiv-ID landing.
