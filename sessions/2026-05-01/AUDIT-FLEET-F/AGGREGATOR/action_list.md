# Fleet-F Aggregator Action List

## Block-on-next-session list

- **NONE.** Fleet-F found no CRITICAL findings and no `INACCESSIBLE_PARTIAL` scopes. No global block applies before the next session writes new work.

## PCF2-V13-RELEASE preconditions

- **F1-01 — AEAL schema drift:** **RECOMMENDED** to address by formally re-spec'ing AEAL in PCF-2 v1.3 paper text or by running a migration to canonical claim records. This is not strictly blocking, but the v1.3 paper should not silently re-use the auditability claim without addressing the schema drift.
- **F4-H1 — `mpmath` bibliography:** Relevant only if PCF-2 v1.3 `main.tex` cites `mpmath`. Verify before fire; if cited, add a scoped, verified `mpmath` BibTeX entry first.

## Channel-Theory-V13 preconditions

- **F2-M1 and F2-M3:** Fix prose-level citation of PCF-2 v1.1 → current PCF-2 version in any new Channel Theory release description. The next Channel-Theory-V13 description should not continue saying it supplements PCF-2 v1.1 if the intended target is PCF-2 v1.2/v1.3.
- **F2-M2:** Historical v1.1 staleness can remain as record history; keep it visible in the reflexivity table rather than treating it as a blocking edit.

## Standalone-note-fire preconditions

- **NONE blocking.** Standalone note (CASE B with C-caveat) does not depend on any Fleet-F audit finding.

## Other affected-paper preconditions

- **F4-H1:** Add/verify `mpmath` before any affected p12, rigidity-entropy, or vquad submission.
- **F4-H2:** Add/verify `olver1974` and `odlyzko1995` before paper14 resubmission.
- **F4-H3:** Add/verify `Okamoto1987` before p12 resubmission.

## Defer list

- **F4-L1:** Add DOI for `costin2008asymptotics` only when the SpectralClasses bibliography is next touched.
- **F4-I1:** Leave unused library-bib entries unless the SpectralClasses bibliography is actively pruned or re-scoped.
- **F2-I1:** arXiv mirroring is a separate todo, not a Fleet-F blocker.
