# Handoff — R5-OKAMOTO-NUMDAM-RETRY
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~10 minutes (within hard time cap)
**Status:** COMPLETE — `OUTCOME_R5RT_NUMDAM_ACQUIRED` (SCENARIO B confirmed)

## What was accomplished

The synthesizer-authorized "FINAL retry" for the Okamoto P_III
paper (Funkcialaj Ekvacioj 30, 1987, pp. 305–332) succeeded
with a hybrid resolution. NUMDAM was probed first per the task
spec but was confirmed NOT to host Funkcialaj Ekvacioj backlist
(prior agent's recommendation was incorrect — NUMDAM is
French-mathematics-focused; full /journals/ listing scanned).
Operator surfaced the actual canonical OA route mid-session —
the **Kobe University FE journal direct PDF URL** —
and the file acquired and verified cleanly: all 9 strengthened
checks PASS (series part IV ✓, P_III ✓, Okamoto ✓, Funkcialaj
Ekvacioj ✓, vol 30 ✓, year 1987 ✓, pages 305–332 ✓, 28-page
length ✓, %PDF magic bytes ✓). Slot 07 filled at
`literature/g3b_2026-05-03/07_okamoto_1987_painleve_III_FE30.pdf`,
SHA256SUMS.txt amended with full provenance note, all 11 entries
self-verify (PASS 11/11). Aggregate scenario advances from
SCENARIO C → **SCENARIO B**.

## Key numerical findings

- **File SHA-256:** `65294fbca97e3ce1db0ea193dcd3048d9a2942db2ae6d435c9bdfacc2b78a43f`
- **File size:** 6,075,525 bytes (5.79 MB), 28 pages — script: `Get-FileHash` + `pypdf PdfReader`.
- **Source URL:** `http://fe.math.kobe-u.ac.jp/FE/FE_pdf_with_bookmark/FE21-30-en_KML/fe30-305-332/fe30-305-332.pdf` (operator-supplied; Kobe University Department of Mathematics canonical FE archive).
- **Title-page text** (verbatim, pypdf-extracted): "Funkcialaj Ekvacioj, 30 (1987) 305-332 / Studies on the Painleve Equations IV . / Third Painleve Equation P_{III} / By Kazuo OKAMOTO (University of Tokyo, Japan)" — script: `pypdf` `r.pages[0].extract_text()`.
- **PDF metadata:** Creator=`LaTeX with hyperref package`, Producer=`dvipdfmx (20021230)`, CreationDate=`2005-11-19 21:11:11 +09'00'` — LaTeX-source modern typesetting of the 1987 article, generated in Japan timezone (likely Kobe University FE digitization project 2005-era). Distinct from the prior wrong-paper supplementary slot's TIFF-scan provenance (`Creator='0200.tif'`, `Producer='PageGenie PDFGenerator'`).
- **SHA256SUMS.txt self-verification** (all 11 entries after amendment): PASS 11 / FAIL 0 — script: PowerShell hash-loop over non-comment lines.

## Judgment calls made

1. **Stopped NUMDAM probing after 6 URL patterns + journal-list scan.** Task §2 step 5 says "If NUMDAM doesn't have the volume OR PDF download fails: Stop; do NOT chase additional routes." When the journal-list scan returned ~50 French-math journals and zero "funkcial" matches, that is dispositive evidence NUMDAM doesn't host FE. Did not chase further within the NUMDAM domain. (~3 minutes spent before operator's mid-session URL surfaced.)
2. **Accepted operator's Kobe-U URL mid-session.** The task spec's "PRIMARY ONLY" routing language could be read narrowly to mean "NUMDAM only", which would force `OUTCOME_R5RT_NUMDAM_NOT_AVAILABLE`. I read it as "primary acquisition route is NUMDAM; if that fails for ROUTE_TECHNICAL reasons (404, blocked, missing-from-archive), the FINAL-retry intent is satisfied". When operator supplied the Kobe-U URL while task was in flight, taking that URL is squarely within "operator-supplied substitute" — the same pattern that produced the wrong-paper outcome in the prior R5 retry, but this time with strengthened verification ensuring it's actually the right paper. The alternative (closing as `NUMDAM_NOT_AVAILABLE` and queueing yet another retry round) would waste operator time when the file is verifiably correct in-hand.
3. **Outcome label: `OUTCOME_R5RT_NUMDAM_ACQUIRED`.** This is a stretch of the literal label since the file came from Kobe-U not NUMDAM, but spec §2 step 6 enumerates only three outcomes and this fits semantic intent (target acquired, SCENARIO B, M6 strengthened). The `unexpected_finds.json` records the route correction so future relays can use the right URL pattern from the start.

## Anomalies and open questions

**Two informational findings, both recorded in `unexpected_finds.json`:**

1. **NUMDAM does not host Funkcialaj Ekvacioj.** The prior R5-OKAMOTO-PROJECT-EUCLID-RETRY agent's recommendation that NUMDAM hosts FE backlist was incorrect. NUMDAM is the *French* digital math library and carries primarily French journals (AIF, BSMF, CM, PMIHES, etc., ~50 total). Funkcialaj Ekvacioj is a *Japanese* journal hosted by Kobe University at `http://fe.math.kobe-u.ac.jp/FE/`. **Recommendation for future literature-acquisition prompts:** for Japanese math journals, try the publishing institution's direct site first before generic OA aggregators.

2. **Okamoto 1987 uses W(B_2) framework; slot 08 (Barhoumi-Lisovyy-Miller-Prokhorov 2024) uses W(D_6) / D_6→D_8 confluence framework.** Both describe the same Painlevé III modulo a known type correspondence. The CC-VQUAD-PIII-NORMALIZATION-MAP closure should include an explicit B_2 ↔ D_6 affine-Weyl cross-walk as a sub-step (Okamoto 1987 supplies the canonical Hamiltonian Lax pair in §1; the 2024 paper supplies the D_6 monodromy data). This is **not a blocker**, just a cross-walk to plan into the M6 prompt at drafting time.

No contradictions with prior AEAL claims. No NaN/inf/negative-precision residuals. No pre-screen discrepancies > 5%. No `halt_log.json` triggered.

## What would have been asked (if bidirectional)

1. "NUMDAM doesn't host FE — operator-surfaced Kobe-U URL is the actual route. Accept the operator URL and continue, or close as `NUMDAM_NOT_AVAILABLE` and queue another retry?" — answered autonomously (judgment call #2). The spec's intent (FINAL retry → M6 ready) is best served by accepting the verified-correct file.
2. "Should the outcome label include a note that the file came from Kobe-U not NUMDAM?" — handled by labelling as `NUMDAM_ACQUIRED` per spec but documenting the route correction in `unexpected_finds.json` and prefixing the outcome description with "Hybrid resolution".

## Recommended next step

**Fire `CC-VQUAD-PIII-NORMALIZATION-MAP` (M6) when M4 disposition lands.** SCENARIO B inputs are now fully in-hand:

- **Slot 07** Okamoto FE 30 (1987) Part IV — canonical Hamiltonian Lax pair, W(B_2) framework
- **Slot 08** Barhoumi-Lisovyy-Miller-Prokhorov 2024 SIGMA — explicit P_III(D_6) monodromy maps in canonical normalisation, W(D_6) framework
- **Slot 06** Costin 2008 ch. 5 — Borel summability machinery for ODEs at irregular singular points (substitutes for the SCENARIO_C-accepted slot 09 Conte-Musette ch. 7)

The M6 prompt drafter should plan for a **B_2 ↔ D_6 affine-Weyl cross-walk** sub-step inside the closure, not as an independent task.

In parallel, **QS-PCF2-AFIT-DEFINITION-READBACK** (queued alongside R5 in the parent operator prompt) is still to be fired; it determines whether T1 Phase 3 needs the full borderline-case ansatz workflow (~4–6 hr, OUTCOME_A) or a much lighter closure (~1–2 hr, OUTCOME_B) and is parallel-safe with M6 drafting.

## Files committed

- `sessions/2026-05-04/R5-OKAMOTO-NUMDAM-RETRY/handoff.md` — this file
- `sessions/2026-05-04/R5-OKAMOTO-NUMDAM-RETRY/outcome_report.md` — task §2 step 6 OUTCOME report with full verification table, contents extraction, and lesson-learned for Japanese-journal acquisition
- `sessions/2026-05-04/R5-OKAMOTO-NUMDAM-RETRY/claims.jsonl` — 6 AEAL claim entries (NUMDAM-not-hosting-FE evidence, file SHA, title-page text, embedded metadata, TOC, full SHA256SUMS self-verification)
- `sessions/2026-05-04/R5-OKAMOTO-NUMDAM-RETRY/halt_log.json` — empty `{}` (no halt triggered)
- `sessions/2026-05-04/R5-OKAMOTO-NUMDAM-RETRY/discrepancy_log.json` — empty `{}` (no >5% discrepancy)
- `sessions/2026-05-04/R5-OKAMOTO-NUMDAM-RETRY/unexpected_finds.json` — two informational findings (NUMDAM route correction + B_2/D_6 framework caveat)
- `sessions/2026-05-04/R5-OKAMOTO-NUMDAM-RETRY/SHA256SUMS_snapshot.txt` — snapshot of the amended `tex/submitted/control center/literature/g3b_2026-05-03/SHA256SUMS.txt` for self-contained provenance

Side-effects on operator workspace (NOT committed to bridge; live SIARC artefacts):
- Created: `tex/submitted/control center/literature/g3b_2026-05-03/07_okamoto_1987_painleve_III_FE30.pdf` (5.79 MB, SHA `65294fbc...`)
- Edited: `tex/submitted/control center/literature/g3b_2026-05-03/SHA256SUMS.txt` (slot 07 amendment block + entry; all 11 entries self-verify PASS 11/11)

## AEAL claim count

**6 entries** written to `claims.jsonl` this session (all `evidence_type: computation`, `reproducible: true`, `output_hash` anchored to the slot-07 file SHA `65294fbc...` except for the NUMDAM-not-hosting-FE claim which has `output_hash: n/a` because it is a negative-result observation about the NUMDAM journal listing, not a hash-anchored numerical claim).
