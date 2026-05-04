# Handoff — ENDORSER-HANDLE-ACQUISITION
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code) — Claude Opus 4.7
**Session duration:** ~45 minutes
**Status:** COMPLETE

## What was accomplished

Closed the G14 information gap (endorsement-request templates
populated with real arXiv-handle-confirmed candidates).
Identified three Tier-1 endorser candidates with publicly
confirmed arXiv author identifiers, ORCIDs, recent math.NT or
math.CA activity, and research-area overlap with PCF-1 v1.3 +
CT v1.3 bibliographies.  Produced five populated email
templates (one per record × candidate pair).  Did **not**
auto-submit any endorsement request, in compliance with
Rule 2 and the relay prompt § 6 (out of scope).

## Key numerical findings

  - **3 Tier-1 candidates with confirmed handles** (live arXiv
    author-page fetch, 2026-05-04):
       * Wadim Zudilin — `zudilin_w_1` — ORCID
         0000-0001-9551-2903 — Radboud Univ., Nijmegen —
         primary math.NT, latest paper arXiv:2603.25506 (Mar
         2026)
       * Marta Mazzocco — `mazzocco_m_1` — ORCID
         0000-0001-9917-2547 — Univ. of Birmingham — primary
         math.CA / math-ph, latest paper arXiv:2407.17366
         (Jul 2024) → Indag. Math. 2025
       * Stavros Garoufalidis — `garoufalidis_s_1` — ORCID
         0000-0001-5381-1593 — SUSTech / MPIM Bonn — math.GT
         primary, strong math.NT cross-list (Habiro ring
         arXiv:2412.04241, Bloch groups arXiv:1712.04887)

  - **3 Tier-2 candidates** with research-area match but no
    public arXiv handle at the standard slug (HTTP 404):
    Costin (`costin_o_1` 404), Sauzin (`sauzin_d_1` 404),
    Beukers (`beukers_f_1` 404).

  - **5 populated templates** produced:
       * `endorsement_request_record2_PCF1_zudilin.md`
       * `endorsement_request_record2_PCF1_garoufalidis.md`
       * `endorsement_request_record4_CT_mazzocco.md`
       * `endorsement_request_record4_CT_zudilin.md`
       * `endorsement_request_record4_CT_garoufalidis.md`

  - **8 AEAL claims** in `claims.jsonl` (1 Phase A literature
    citation + 1 CT-bibliography literature citation + 3
    handle-confirmation web_query + 1 negative-result
    web_query + 1 deposit_confirmation for templates + 1
    deposit_confirmation for verdict).

## Judgment calls made

  1. **Spec-label drift on record #2.**  Prompt 022 § 0 + § 7
     refer to record #2 as "PCF-2 v1.3"; the actual existing
     endorsement template at
     `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/` is
     `ENDORSEMENT_REQUEST_pcf1_v1.3.md` — i.e. record #2 is
     **PCF-1 v1.3**, not PCF-2.  PCF-2 v1.3 is record #5 in
     the runbook and inherits the math.NT endorsement
     obtained for PCF-1 v1.3 under arXiv's
     single-endorsement-per-category rule.  I treated the
     existing PCF-1 template as canonical and labelled new
     templates `record2_PCF1_<candidate>.md` accordingly.
     Logged to `discrepancy_log.json`.  No operator action
     required.

  2. **Did not transcribe candidate emails.**  Per the relay
     prompt § 5 PII / privacy hygiene and per the
     `HALT_G14_PRIVACY_CONCERN` guard at § 4, I did not
     transcribe candidate institutional email addresses into
     templates or dossier — even though several are
     in-principle public.  Each populated template instead
     contains the candidate's institutional homepage URL and
     instructs the operator to confirm the email at the
     institutional page before sending.  This is a deliberate
     choice to (a) avoid stale-email errors, (b) avoid
     creating a checked-in artefact that bundles personal
     contact info for multiple researchers.  Verdict downgraded
     accordingly from
     `UPGRADE_G14_ENDORSERS_IDENTIFIED_3` to
     `UPGRADE_G14_ENDORSERS_IDENTIFIED_3_HANDLES_CONFIRMED_EMAILS_PENDING_OPERATOR`.

  3. **Tier-2 not populated as templates.**  Costin, Sauzin,
     Beukers are strong subject-matter candidates but have
     no publicly resolvable arXiv author identifier at the
     standard slug.  Rather than fabricate a handle or guess
     a non-standard slug, I left them as Tier-2 in the
     dossier with operator-side action notes.  Operator may
     attempt to locate handles by other means
     (arxiv.org/find author search; institutional homepages;
     direct email enquiry) before contacting.

  4. **Did not attempt institutional-email retrieval at scale.**
     The prompt suggested arXiv's "endorser_xxxx" code-style
     handle could be sometimes recovered via Google Scholar
     external-links.  I did not pursue this beyond the standard
     `arxiv.org/a/<handle>.html` slug fetch, because (a) the
     Google Scholar route is unreliable and frequently scraped
     incorrectly; (b) I already had 3 confirmed Tier-1
     candidates, which exceeds the 2-per-record minimum.

## Anomalies and open questions

  1. **Garoufalidis primary category is math.GT, not math.NT.**
     His Habiro-ring (arXiv:2412.04241) and Bloch-groups
     (arXiv:1712.04887) papers ARE math.NT primary, so per
     arXiv endorsement rules he is eligible to endorse
     math.NT submitters.  But the bulk of his recent work is
     math.GT.  Operator should confirm with Prof. Garoufalidis
     directly that he holds **active** math.NT endorsement
     privileges (which arXiv grants per-category based on
     primary-category submission count).  If math.NT
     privileges are inactive, fall back to Zudilin (primary
     math.NT — privileges are certain).

  2. **Mazzocco primary category is math-ph / math.CA mixed.**
     Her recent papers are split: arXiv:2407.17366 is
     math.CA primary, but arXiv:2405.10541 is math-ph primary.
     Per arXiv's endorsement-privilege rules, math.CA
     endorser status requires a sufficient count of math.CA
     primary papers; she likely qualifies (Koornwinder-
     Mazzocco 2024 math.CA + Horrobin-Mazzocco 2020 math.CV
     + Mazzocco-Vidunas 2013 nlin.SI/math.CV + several
     pre-2020 math.CA-primary papers).  Operator can verify at
     `arxiv.org/auth/show-privileges` once the endorsement
     request is initiated.

  3. **PCF-1 v1.3 page-count drift (carried from prior halt).**
     The 2026-05-02 ARXIV-MIRROR-RUNBOOK halted at
     `ARXIV_MIRROR_HALTED_PAGE_COUNT_DRIFT_2` (PCF-1 21 pp
     local vs 16 pp on Zenodo).  This task does not touch
     that drift; it must be resolved before Prompt 002 can
     re-fire after endorsement is in place.

  4. **No Costin/Sauzin handle is a mild surprise.**  Costin
     has a vast arXiv corpus going back 25 years; Sauzin has
     dozens of math.CA papers.  Both returning HTTP 404 at
     the standard slug suggests neither has claimed an arXiv
     author identifier (the system is opt-in per
     `arxiv.org/a/help/author_identifiers`).  Logged in the
     dossier but not flagged as a halt.

## What would have been asked (if bidirectional)

  1. Should Tier-2 candidates (Costin / Sauzin / Beukers)
     receive operator-drafted "could you share your arXiv
     handle, or recommend a colleague who can endorse?"
     emails as a parallel step?  This would substantially
     widen the candidate pool but extends the timeline.

  2. Is there a SIARC-internal preference between Tier-1
     candidates (e.g., Zudilin vs Garoufalidis for math.NT)?
     I lean Zudilin for math.NT (primary-category match,
     direct continued-fraction overlap), Mazzocco for
     math.CA (Painlevé monodromy direct citation), but the
     operator may have author-relationship constraints I
     don't see.

## Recommended next step

Operator-side: (a) Verify institutional emails for the three
Tier-1 candidates by visiting their institutional homepages
(URLs in `candidate_dossier.md`).  (b) Submit
`arxiv.org/auth/need-endorsement.html` requests for record #2
(math.NT, naming Zudilin as primary candidate) and record #4
(math.CA, naming Mazzocco as primary candidate).  (c) Receive
the arXiv-issued endorsement codes; paste into the populated
templates; send.

After endorsements are in place, queue **Prompt 002 (re-fire
arXiv mirror runbook)** for records #2, #4, and #5 (PCF-2 v1.3
inherits the record-#2 endorsement).  Resolve the PCF-1
page-count drift before re-firing record #2.

## Files committed

  - `prompt_spec_used.md` — provenance + spec-drift note
  - `candidate_dossier.md` — full candidate list (Tier 1 + 2)
    with handles / ORCIDs / affiliations / activity / citation
    overlap / operator action plan
  - `endorsement_request_record2_PCF1_zudilin.md` — PCF-1 v1.3
    math.NT request, Zudilin as endorser (primary)
  - `endorsement_request_record2_PCF1_garoufalidis.md` — PCF-1
    v1.3 math.NT request, Garoufalidis as endorser (fallback)
  - `endorsement_request_record4_CT_mazzocco.md` — CT v1.3
    math.CA request, Mazzocco as endorser (primary)
  - `endorsement_request_record4_CT_zudilin.md` — CT v1.3
    math.CA request, Zudilin as endorser (cross-NT)
  - `endorsement_request_record4_CT_garoufalidis.md` — CT v1.3
    math.CA request, Garoufalidis as endorser (fallback)
  - `claims.jsonl` — 8 AEAL entries
  - `halt_log.json` — empty {}
  - `discrepancy_log.json` — record-#2 label drift note
  - `unexpected_finds.json` — empty {}
  - `handoff.md` — this file

## AEAL claim count

8 entries written to `claims.jsonl` this session.

## Verdict

**UPGRADE_G14_ENDORSERS_IDENTIFIED_3_HANDLES_CONFIRMED_EMAILS_PENDING_OPERATOR**

3 Tier-1 candidates with publicly confirmed arXiv handles +
ORCIDs + recent math.NT or math.CA primary activity.  Emails
NOT transcribed per privacy hygiene; operator confirms at
institutional homepages before sending populated templates.
G14 closes pending operator-side outreach.

## Strategic implication

  - Picture v1.17 § 5 G14 row: status moves from
    *templates skeleton, no real handles* → *templates
    populated, 3 Tier-1 candidates with confirmed handles;
    awaiting operator email-confirmation + outreach*.
  - Prompt 002 (ARXIV-MIRROR-RUNBOOK) re-fire readiness for
    math.NT records #2 + #5 (PCF-1 + PCF-2 v1.3) is gated on
    (i) PCF-1 page-count drift resolution and (ii) operator
    completing math.NT endorsement outreach (Zudilin primary).
  - Prompt 002 re-fire readiness for math.CA record #4 (CT
    v1.3) is gated on operator completing math.CA endorsement
    outreach (Mazzocco primary).
  - No further researcher session needed for G14 unless all
    three Tier-1 candidates decline.  In that case, escalate
    to Tier-2 (Costin / Sauzin / Beukers via direct email
    contact) or to math.NT moderator route at
    `arxiv.org/help/endorsement-moderator`.
