# Handoff — ADAMS-1928-FINAL-ACQUISITION-PROBE

**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE
**Verdict:** **UPGRADE_ADAMS_NIA_ILL_RECOMMENDED_AMS**

## What was accomplished

Executed the final OA acquisition probe for C. R. Adams, "On the irregular
cases of the linear ordinary difference equation", Trans. Amer. Math. Soc. 30
(1928), 507–541 (G3b residual (ii) of T1-A01 verdict
`A01_WASOW_READING_CONFIRMED`, 2026-05-03 bridge `bbc905d`). Phase A confirmed
the bibliographic record and corrected a PII typo in the relay-prompt
(canonical PII is `S0002-9947-1928-1501443-6`, not `-1501457-9`). Phase B
probed three OA routes (AMS direct, JSTOR, Internet Archive); none of them
yielded a downloadable PDF with text layer under plain HTTP fetch. Phase C
recommends operator-side AMS Free Digital Archive retrieval (one browser click
on the article landing page; AMS policy explicitly grants free access to all
volumes older than 5 years). G3b residual (ii) stays closed-via-transitive-
evidence per T1-A01.

## Key numerical findings

None — this is a literature-acquisition task with no numerical claims. (See
`claims.jsonl` for the 8 literature/deposit AEAL entries.)

## Judgment calls made

- **Cut clean per operator instruction "no further route probes".** Phase B
  was halted after routes B.1, B.1.a, B.1.b, B.2, B.3 (AMS direct, JSTOR,
  Internet Archive). Routes B.4–B.7 (zbMATH-Open, EuDML, Project Euclid, Brown
  archive, AMS oral-history) not probed.
- **Bibliographic correction.** Relay-prompt §2 Phase A.1 cites DOI
  `10.1090/S0002-9947-1928-1501457-9`; that PII is a different article in the
  same Trans. AMS 30, no. 3 issue. The correct Adams 1928 PII is
  `S0002-9947-1928-1501443-6`, confirmed against the issue TOC at
  <https://pubs.ams.org/journals/tran/1928-030-03>. All probes used the
  corrected PII.
- **Verdict label `UPGRADE_ADAMS_NIA_ILL_RECOMMENDED_AMS`** rather than a
  generic `..._<library>` label. The recommended operator action is not a
  library ILL — it's a one-click browser fetch of the AMS Free Digital
  Archive PDF. AMS is named as the "library" in the spec ladder slot.

## Anomalies and open questions

1. **AMS HTTP-vs-browser asymmetry.** AMS policy says these PDFs are free for
   volumes >5 years old, but the `pubs.ams.org/journals/tran/1928-030-03/.../...pdf`
   URL returns `Content-Type: text/html` (the AMS viewer wrapper, 8.04 MB)
   under `Invoke-WebRequest -UseBasicParsing`. The article landing page
   surfaces only a `/Account/Login?returnUrl=...` link to the actual PDF. This
   appears to be a JS-rendered viewer / session-cookie handshake that
   `Invoke-WebRequest` does not establish; a real browser will succeed without
   any login (per the AMS Free Digital Archive policy). This pattern is
   identical to the WASOW-X3 / SAKAI-2001 lessons-learned: AMS-hosted free
   archive PDFs require browser-side fetch.
2. **No direct primary-source reading was performed.** Therefore neither
   `HALT_ADAMS_DIRECT_DISAGREES_WITH_TRANSITIVE` nor `HALT_ADAMS_TEXT_LAYER_BAD`
   is reachable, and the T1-A01 transitive-evidence verdict is unaffected.
3. **JSTOR Early Journal Content boundary** (Adams 1928 is at the borderline
   of the 95-year U.S. EJC threshold of 1931). Not investigated in depth in
   this session because the operator-side AMS path is strictly cleaner and
   already free.

## What would have been asked (if bidirectional)

- "Operator: would you prefer the agent perform an OS-level browser-driven
  fetch (Playwright / Selenium with Rule-2 review) of the AMS Free Digital
  Archive PDF, or is one-click manual operator retrieval acceptable?"
  (Default: manual, per Rule 2.)

## Recommended next step

**Operator-side AMS retrieval (one-step path).** Per Rule 2:

1. Browser-visit
   <https://pubs.ams.org/journals/tran/1928-030-03/S0002-9947-1928-1501443-6/>.
2. Click "Article PDF" / "View in volume". (No AMS login is required for
   volumes older than 5 years, per AMS Free Digital Archive policy.)
3. Save as
   `tex/submitted/control center/literature/g3b_2026-05-03/12_adams_1928_TransAMS30.pdf`.
4. Append SHA-256 to `SHA256SUMS.txt` with provenance line referencing AMS
   Free Digital Archive + PII `S0002-9947-1928-1501443-6` + page range
   507–541.
5. Once the PDF is on disk, fire a follow-up Phase D task (cross-validation of
   Adams 1928 §§1–3 σ-normalisation against T1-A01 transitive-evidence
   baseline). On agreement, this upgrades to
   `UPGRADE_ADAMS_ACQUIRED_AGREES_WITH_TRANSITIVE` (or
   `UPGRADE_ADAMS_AMS_ROUTE_ACQUIRED` as the AMS-direct sub-tier). On
   disagreement, escalate to `HALT_ADAMS_DIRECT_DISAGREES_WITH_TRANSITIVE`
   (full T1-A01 re-audit gate).

If AMS-direct surprisingly fails for the operator: Tier-2 ILL routes are
Yokohama City Library (operator local), AMS Member Services (only if operator
has membership; should not be needed), Brown University Library ILL.

## Files committed

- `prompt_spec_used.md` — relay-prompt body verbatim (Phase 0 provenance).
- `route_probe_log.md` — per-route URL + HTTP status + content-type +
  acquisition possibility, plus AMS Free Digital Archive policy quotation.
- `claims.jsonl` — 8 AEAL entries (1 Phase A bibliographic + 4 Phase B
  per-route + 2 policy/correction + 1 verdict).
- `halt_log.json`, `discrepancy_log.json`, `unexpected_finds.json` — empty
  (no halt, no discrepancy, no unexpected find).
- `handoff.md` — this file.

## AEAL claim count

**8** entries written to `claims.jsonl` this session.
