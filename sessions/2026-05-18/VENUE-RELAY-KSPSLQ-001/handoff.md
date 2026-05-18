# Handoff — VENUE-RELAY-KSPSLQ-001
**Date:** 2026-05-18
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Executed a 5-stage SIARC venue-determination relay (Synthesis → Investigation → Audit → Relay → Closure) for the manuscript "A Precision-Controlled Null Result for a Khinchin-Signature PSLQ Family" (submission 264514392, currently at Experimental Mathematics). Built a fingerprint from the manuscript source, enumerated 12 candidate venues with hard/soft/portfolio exclusions explicitly applied, web-verified the top-5 candidates' AI disclosure stance + decision time + pseudonymity-policy posture, and produced a primary/backup/reserve venue recommendation with pre-submission checklist and AEAL claim entries. Discovered and resolved one material discrepancy (INTEGERS hard-AI-ban) during the audit stage.

## Key numerical findings
- **Manuscript fingerprint**: primary contribution type = computational null result; primary MSC = 11Y65; secondary MSC = 11K50, 11J70, 68W30; length 6–8 pp; 2 tables; 4-panel figure; 7-entry bibliography. Four of five most-cited works appeared in Mathematics of Computation (source: stage1_fingerprint.json).
- **Audited 5 candidates** via direct web fetch on 2026-05-18; recorded 12 verified factual claims in claims.jsonl with source URLs (10 fully verified, 2 verification-blocked at Springer login wall).
- **AMS Math of Computation**: AI-permissive with disclosure (COPE Feb 2023 adoption); double-anonymous peer review since AMS Council Jan 2021; verified currently publishing MSC 11Y16/11Y35/11Y65 papers in early-view list.
- **Bulletin of the Australian Mathematical Society**: editorial decisions normally within a month; 12-page cap; explicit CUP-level pseudonymous-authorship policy clause; AI-permissive with disclosure.
- **INTEGERS** (originally Stage-2 rank #2): hard AI ban verbatim — "Integers will not consider any article that makes use of artificial intelligence in producing mathematics, computer code, bibliographic information, or other content."

## Judgment calls made
- **Selected MComp over BAustMS as primary** on literature-centroid grounds (4/5 most-cited works appeared at MComp). Alternative defensible reading: BAustMS has the fastest verified decision time and explicit pseudonymity-policy clause and could be promoted to primary on speed-and-friction grounds. Chose MComp because the manuscript was originally cast for Experimental Mathematics and would benefit from a venue whose remit centroid is more centrally aligned with the bibliography; the double-anonymous review structurally removes the rejection-history bias that motivated the friction-minimisation reading.
- **Dropped INTEGERS at Stage 3 rather than re-running Stage 2** with the hard-AI-ban filter pre-applied. Recorded the discrepancy and lesson in discrepancy_log.json with the recommendation that AI-policy pre-filtering should move into Stage-2 input filter for future portfolio-wide relays.
- **Demoted Ramanujan Journal and Research in Number Theory to reserve / drop** partly because Springer login wall blocked policy verification, not solely on scope grounds. Flagged this asymmetry as an open issue: if both MComp and BAustMS fail, a fresh Springer-policy audit is mandatory before activating Ramanujan Journal as reserve.

## Anomalies and open questions
**THIS IS THE MOST IMPORTANT SECTION.**

1. **INTEGERS hard AI ban (discovered Stage 3)**. This was not anticipated by the Stage-2 enumeration. Beyond this manuscript, INTEGERS should be added to the persistent hard-exclusion list alongside NNTDM for any portfolio manuscript carrying an AI assistance disclosure. The lesson generalises: a single Stage-2 pre-filter for "AI ban" (analogous to the existing hard-exclusion check for Experimental Mathematics rejection count) would have caught this without spending Stage-3 audit budget. Recommend Claude review whether this filter should become a standing input to the venue-relay prompt template.

2. **Springer-policy verification gap (Ramanujan Journal, Research in Number Theory)**. Both Springer-side journal pages redirected to the idp.springer.com login flow when fetched; no anonymous policy-page retrieval succeeded. The reserve target (Ramanujan Journal) is therefore proposed on inferred-from-Springer-Nature-standard-policy grounds, not directly verified. Two AEAL entries (C11, C12) are recorded with evidence_type "web_verification_failed". If primary and backup both fail, a fresh Springer audit (possibly via a browser-based screenshot path or via a Springer journal's policy-disclosure-via-author-portal route) is required before activating Ramanujan Journal.

3. **Mathematics of Computation editorial board not directly enumerated**. The MComp editorial board page returned no meaningful content via the fetch path used. The "any editor with PSLQ/Khinchin/experimental-NT history?" question in Stage-3 was therefore not directly answered. Cover-letter editor-targeting would benefit from a manual lookup pass at https://www.ams.org/mcomedit.

4. **Operator-side withdrawal action required**. The manuscript is currently submitted to Experimental Mathematics (ID 264514392). Resubmission to MComp requires prior withdrawal from Experimental Mathematics. This is an operator action, not an agent action, and is the binding sequencing constraint on the recommendation.

5. **Double-anonymous review preparation**. The submitted-to-MComp pdf must be free of author-identifying content including the GitHub URL in the AI Disclosure section. Recommend a review-version pdf with the URL replaced by "[available on acceptance]", with the actual URL added on revision. The current source.tex has \author{} blank, which is good, but the disclosure section URL and the PDF metadata still need to be sanitised.

6. **Three-constant replication may be requested**. Stage-3 noted that referee may request a third constant (e.g. log 2, Apéry, Catalan) before publication. The precision-controlled pipeline supports this directly. No action needed pre-submission, but worth flagging in the cover letter that the pipeline is ready for extension.

## What would have been asked (if bidirectional)
- **Q1**: Was a withdrawal from Experimental Mathematics already executed by the operator, or is the manuscript still actively under review there? If still active, the MComp resubmission cannot be staged until withdrawal completes. (This is the binding sequencing question.)
- **Q2**: Is the GitHub repo https://github.com/papanokechi/khinchin-signature-pslq currently public, and does its README contain script-level pointers reproducing the n=91 (pi) and n=192 (e) certified prefixes and the 1698 conservative-cap unsupported attempts? The MComp reproducibility statement (Stage-4 checklist item #4) hinges on this.
- **Q3**: Does the operator have a preference for "fast verdict cheap to bounce" (BAustMS first) versus "literature-centroid maximum-fit" (MComp first)? My recommendation is MComp first, but BAustMS-first is defensible.
- **Q4**: Should the persistent hard-exclusion list (Experimental Mathematics, NNTDM, INTEGERS post-this-chain, JTNB post-rejection) be lifted from this handoff into a workspace-level rule that the venue-relay prompt template pulls from automatically? This would prevent the Stage-2/Stage-3 round-trip for the next relay.

## Recommended next step
**Operator action first, then synthesizer drafts the resubmission relay prompt.**

1. **Operator (manual)**: Withdraw 264514392 from Experimental Mathematics. Confirm withdrawal completion before agent work resumes.
2. **Next relay (suggested chain ID)**: `MCOM-RESUB-KSPSLQ-001` — "Prepare Khinchin-PSLQ-Family manuscript for Mathematics of Computation resubmission". Deliverables: (a) AMSLaTeX-converted source.tex; (b) double-anonymous-sanitised review-version pdf; (c) cover letter with methodology-as-contribution framing; (d) updated reproducibility statement with frozen commit hash; (e) confirmed-public repository check. Pre-submission checklist already specified in stage4_recommendation.json item 1–6.
3. **Parallel housekeeping**: add INTEGERS to the workspace's persistent hard-exclusion list (consider lifting that list into `.github/copilot-instructions.md` or a dedicated `venue_exclusions.json` for portfolio-wide automation).

## Files committed
- `stage1_fingerprint.json` — manuscript fingerprint (Stage 1)
- `stage2_candidates.json` — 12 candidate venues with exclusions and concurrent-submission cross-check (Stage 2)
- `stage3_audit.json` — Stage-3 web-verified audit of top-5 with INTEGERS drop and revised ranking
- `stage4_recommendation.json` — primary/backup/reserve with pre-submission checklist and risk-weighted outcomes
- `stage5_ledger_and_aeal.json` — SIARC ledger entry, AEAL claim entries, redirect-queue update, hard-exclusion update
- `claims.jsonl` — 12 AEAL claim entries (one per line)
- `halt_log.json` — no halt triggered (per protocol; empty-with-explanation log)
- `discrepancy_log.json` — INTEGERS hard-AI-ban discovery + lesson
- `unexpected_finds.json` — AMS double-anonymous review + CUP pseudonymity clause
- `handoff.md` — this file

## AEAL claim count
12 entries written to claims.jsonl this session (10 verified via direct web fetch; 2 flagged as web_verification_failed pending re-audit).
