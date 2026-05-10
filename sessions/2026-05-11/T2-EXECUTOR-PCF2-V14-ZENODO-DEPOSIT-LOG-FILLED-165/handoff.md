# Handoff — T2-EXECUTOR-PCF2-V14-ZENODO-DEPOSIT-LOG-FILLED-165

**Date:** 2026-05-11
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes (cumulative across post-deposit review + logging)
**Status:** COMPLETE

## What was accomplished

Post-deposit landing of PCF-2 v1.4 on Zenodo (version-DOI `10.5281/zenodo.20114315`, May 11, 2026) was verified, logged, and propagated through the SIARC bookkeeping chain. The deposit-log template from slot 137 (LANDED `45e236c`; immutable) was copied into this slot and filled with all captured values from the live record. The submission_log Item 11 series 2 splice template was format-adapted (slot 137 `===` block format → existing compact `N. Filename:` field-line format) and applied to `tex/submitted/submission_log.txt` in the claude-chat repo. Live Zenodo record (via JSON API) was inspected for metadata fidelity vs paste-source.

## Key numerical findings

- PCF-2 v1.4 version-DOI assigned: `10.5281/zenodo.20114315` (Zenodo recid `20114315`; conceptrecid `19936297`).
- Version chain intact: v1.0..v1.4 = 5 versions; v1.4 = API index 4, `is_last: true`.
- File integrity: all 3 files (PDF 636,049 B / tex 80,244 B / diff 10,486 B) byte-for-byte verified via MD5 round-trip (local Get-FileHash ↔ Zenodo md5). SHA-256 16-char prefixes match slot 137 template exactly: `471DC7C7EBF8BD4F` / `0CF4E7DC90C1AC2A` / `30371C2EBD9885B1`.
- 5 Related-identifier rows in live record: all `publication-preprint` resource_type; both Umbrella supplement rows correctly cite `19885549` (concept), NOT `19885550` (v1.0). **D-162-1 substrate→deposit chain RESOLVED at deposited-record level.**

## Judgment calls made

1. **Slot ID choice**: used `T2-EXECUTOR-PCF2-V14-ZENODO-DEPOSIT-LOG-FILLED-165` (next sequential after slot 163-164 `b936eb0`). The session summary suggested `-167`; I chose `-165` because no slots 165 or 166 are landed in the bridge or in-flight elsewhere visible to this session. Operator may renumber post-hoc if conflicting with planned reservations.
2. **submission_log splice format adaptation**: the slot 137 template's `===` block delimiter format is inconsistent with the existing minimalist `N. Filename:` field-line style used by Items 1-10. I format-adapted to match existing style rather than introduce visual discontinuity. All field semantics preserved; substrate-trail (SHAs + cascade-132 ordering + DOI-correction lineage + Resource-type note) compressed into the Notes line. Documented in `submission_log_v14_splice_applied.md`.
3. **HTML description preparation**: I drafted an HTML-converted replacement description body at `session-state files/pcf2_v14_description_HTML.html` (~4.2 KB) ready for operator Edit → Description paste. NOT auto-applied to the live record — operator decision whether to apply.
4. **Resource type discontinuity (Working paper vs Preprint)**: documented as forward-only (Note 1 in deposit log; UF-165-1). No back-edit recommendation issued; chain-consistency loss accepted as operator-deliberate per slot 137 paste-source.
5. **Co-numbered metadata fixes (keywords, ORCID, dates anomaly)**: documented in UF-165-4 with cosmetic-only severity. NOT auto-applied; left for operator Edit.

## Anomalies and open questions

**Verified anomalies, all INFO-severity:**

1. **UF-165-1 — Resource type discontinuity** (v1.0..v1.3 = Preprint; v1.4 = Working paper). Operator-deliberate per slot 137 paste-source. Forward-document only.
2. **UF-165-2 — Third instance of v1.0-vs-concept single-digit anti-pattern** (PCF-2 19936297/19936298 in addition to umbrella 19885549/19885550 and T2B 19783311/19783312). Promote-to-memory candidate at end of this session.
3. **UF-165-3 — Markdown description body not auto-parsed**. Cosmetic-only; HTML replacement prepared.
4. **UF-165-4 — Three minor metadata gaps**: keywords stored as one comma-concatenated string, no ORCID attached, anomalous `dates` field entry. All Zenodo-Edit-fixable.

**Open questions for next operator-decision:**

- **Q1** Apply HTML description + keyword split + ORCID add to live record via Zenodo Edit? Single Edit transaction can cover all 4 cosmetic fixes (description + keywords + ORCID + dates field). No DOI bump on metadata-edit-without-file-change.
- **Q2** Branch Z (umbrella v2.2) — does the paste-source's `IsSupplementTo PCF-2 v1.4` row need to be at concept-DOI granularity (`19936297`) or version-DOI granularity (`20114315`)? Slot 162 amended block currently uses concept; cascade-132 Option α step 2 should clarify before firing. Possible slot 166 OVERLAY-COPY needed.
- **Q3** Picture-chain v1.20+ deposit (Branch Z step 3) — same question about granularity for the PCF-2 cross-link row.

## What would have been asked (if bidirectional)

- "Should I apply the HTML description + keyword split + ORCID add now via Zenodo Edit? (Recommended yes; ~5 min, no DOI bump, fixes 4 cosmetic issues in one transaction.)"
- "For Branch Z paste-source, do you want PCF-2 cross-link at concept granularity (19936297) or version granularity (20114315)?"
- "Slot 165 numbering OK, or do you have 165/166 reserved for other work?"

## Recommended next step

**Either** (a) operator applies the 4 Zenodo Edit cosmetic fixes (HTML description + keyword split + ORCID add + dates cleanup) — Q1; **or** (b) advance to Branch Z step 2 (umbrella v2.2 paste-source update + deposit). Both are independent; (a) is lower-risk (Zenodo Edit on metadata only); (b) is higher-leverage (advances cascade-132 Option α chain).

If (b): fire a new slot drafting the v1.4-DOI-spliced umbrella v2.2 paste-source (similar pattern to slot 163+164 OVERLAY-COPY; based on slot 135 substrate `887981b` or slot 162 amended block `9271d74`).

## Files committed

- `zenodo_v14_deposit_log_FILLED.md` (8,823 B; §1-§6 all filled with captured values)
- `submission_log_v14_splice_applied.md` (3,193 B; documents format-adaptation + applied diff)
- `claims.jsonl` (25 AEAL entries)
- `halt_log.json` (empty `{}`)
- `discrepancy_log.json` (1 entry: D-165-1 = D-162-1 deposited-record-level closure verification)
- `unexpected_finds.json` (4 entries: UF-165-1 Resource type, UF-165-2 single-digit pattern n=3, UF-165-3 Markdown rendering, UF-165-4 metadata gaps)
- `handoff.md` (this file)

Plus `tex/submitted/submission_log.txt` Item 11 series 2 inserted (intentionally local-only / not git-tracked in claude-chat; persistence via OneDrive sync per operator workflow convention — verified by `git check-ignore` returning not-ignored AND `git ls-files` returning empty, i.e. file exists physically but was never `git add`-ed; this is consistent for all 10 prior items in the same file, so no policy change here).

## AEAL claim count

25 entries written to `claims.jsonl` this session.
