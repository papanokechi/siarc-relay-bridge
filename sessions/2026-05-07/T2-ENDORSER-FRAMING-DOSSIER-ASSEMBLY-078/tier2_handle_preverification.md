# Tier-2 Handle Pre-Verification [HANDLE-PREVERIFICATION] — 078

**Session:** T2-ENDORSER-FRAMING-DOSSIER-ASSEMBLY-078
**Compiled:** 2026-05-07
**Spec reference:** §5 TIER-2 HANDLE PRE-VERIFICATION.
**Discipline:** Per memory `Bibliographic identifier pre-verification`
+ HALT_078_TIER2_HANDLE_FABRICATION (spec §5.E.2 + §8): no non-resolving
arXiv handle is populated into a gap-template header block. Standard
slug query results below are RECORD-ONLY; the load-bearing decision is
the placeholder `<arXiv handle to be confirmed by operator OOB>` used
in Phase D gap-templates.

---

## §E.1 — Standard slug query status

The 2026-05-04 ENDORSER-HANDLE-ACQUISITION dossier (SHA-256/16
`315410D80EDC92C5`) recorded the following standard-slug fetch result
on 2026-05-04 (verbatim per `candidate_dossier.md` §"Privacy + AEAL
notes" L168-176, ≤ 50 words):

> "arxiv.org/a/costin_o_1.html — HTTP 404"
> "arxiv.org/a/sauzin_d_1.html — HTTP 404"
> "arxiv.org/a/beukers_f_1.html — HTTP 404"

This 078 session does NOT re-fetch the URLs. Per spec RUNTIME PROFILE
"NO web-fetch except optional arXiv author-id slug pre-verification …
no auth", the operator may re-attempt at send-time. The 2026-05-04
result anchored above is treated as the load-bearing record.

| Endorser | Standard slug | Resolution status (anchor 2026-05-04) | Verdict |
|---|---|---|---|
| Costin | `costin_o_1` | HTTP 404 | HANDLE_404 |
| Sauzin | `sauzin_d_1` | HTTP 404 | HANDLE_404 |
| Beukers | `beukers_f_1` | HTTP 404 | HANDLE_404 |

Per spec §5.E.1 verdict ladder:
- **HANDLE_VERIFIED**: 0 of 3
- **HANDLE_404**: 3 of 3 (Costin, Sauzin, Beukers)
- **HANDLE_AMBIGUOUS**: 0 of 3

---

## §E.2 — HALT_078_TIER2_HANDLE_FABRICATION discipline

[NOTE-078-E2-1] All 3 Tier-2 gap-templates drafted in Phase D
(`endorsement_request_d2note_sauzin.md`,
`endorsement_request_d2note_costin.md`,
`endorsement_request_t2b_beukers.md`) MUST use the placeholder
`<arXiv handle to be confirmed by operator OOB>` in the header block
"arXiv author id" field. Verification protocol: each Phase D template
file has been pattern-scanned for this placeholder and for the absence
of the unverified slugs `costin_o_1`, `sauzin_d_1`, `beukers_f_1` in
any field that arXiv would consume as an author-id.

Pattern-scan result (cross-referenced in `forbidden_verb_scan.md`
§G.3 below if extended):

| Template | placeholder present? | unverified slug present? | PASS/FAIL |
|---|---|---|---|
| `endorsement_request_d2note_costin.md` | YES (header L) | NO | PASS |
| `endorsement_request_d2note_sauzin.md` | YES (header L) | NO | PASS |
| `endorsement_request_t2b_beukers.md` | YES (header L) | NO | PASS |

(SHAs cross-referenced in `endorser_substrate_anchor_shas.md` §A.7
when written.)

---

## §E.3 — Beukers emeritus eligibility gate

[NOTE-078-E3-1] arXiv requires the endorser to have submitted at least
one paper in the requested category in the past 5 years (per spec §5.E.3
verbatim recall, ≤ 50 words):

> "arXiv requires the endorser to have submitted at least one paper in
> the requested category in the past 5 years. Note the gate; agent does
> not assert eligibility, only surfaces the gate for operator pre-flight."

Beukers is per 2026-05-04 dossier "emeritus per public departmental
page" (verbatim, 5 words). The agent does not infer whether Beukers
has math.NT submission activity in 2021-2026; this is operator
pre-flight at `arxiv.org/auth/show-privileges` after the OOB handle
recovery succeeds.

Suggested operator pre-flight sequence for Beukers:
1. Resolve arXiv handle out-of-band (direct contact / alternate slug
   search).
2. Confirm math.NT submission activity 2021-2026 via the resolved
   handle's arXiv page.
3. Confirm `show-privileges` returns ACTIVE for math.NT category.
4. Only then send populated `endorsement_request_t2b_beukers.md`.

---

## §E.4 — Operator-side handle recovery protocols (verbatim from 2026-05-04 dossier)

For Costin / Sauzin / Beukers, per `candidate_dossier.md` L116-120 +
L136 + L153-155 verbatim quotes (each ≤ 50 words; quoted separately
to keep individual blockquote runs under the 50-word ceiling):

Costin recovery instruction (verbatim, 35 words):

> "Operator action: contact Prof. Costin at his publicly listed
> institutional email and request either (a) endorsement directly
> using a handle he has under a non-standard slug, or (b) referral
> to a colleague with an active math.CA handle."

Sauzin recovery instruction (verbatim, 7 words):

> "Operator action: contact directly; same protocol as Costin."

Beukers recovery instruction (verbatim, 15 words):

> "Operator action: optional secondary candidate; Tier-1 candidates
> Zudilin and Garoufalidis are likely sufficient for math.NT."

These verbatim phrasings are the operator's send-time pre-flight
checklist. 078 does not advance them.

---

## §E.5 — Verdict

[NOTE-078-E5-1] **DOSSIER_PARTIAL** branch active for the 3 Tier-2
endorsers per spec §10. Tier-2 gap-templates (D9 + D10 + D11 + D12) are
drafted with HANDLE_404 placeholder; synth decision packet must surface
this PARTIAL tag and the named OOB-confirmation gates per spec §6.F.1.

End of handle pre-verification file.
