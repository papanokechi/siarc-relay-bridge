# Handoff — Q20A-PHASE-C-RESUME (Dispatch 3)

**Date:** 2026-05-03
**Dispatch 3 timestamp:** 2026-05-03 (re-fire 3)
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** PARTIAL (Phase A* cached PASS; C.0 PASS; C.1 HALT; C.2 PARTIAL; C.3 BLOCKED; D verdict landed; E skipped)
**Verdict:** `HALT_Q20A_WASOW_PDF_IMAGE_ONLY`
**Prior dispatch handoffs:** archived at `handoff_pre_refire.md` (dispatch 1) and `handoff_pre_dispatch3.md` (dispatch 2; itself referenced as "pre_refire2" in dispatch 2's own naming).

## What was accomplished

Re-fired Q20A-PHASE-C-RESUME (dispatch 3) with the operator's
G3b PDFs now landed under the runbook-canonical path
`tex/submitted/control center/literature/g3b_2026-05-03/`.
All four PDF SHA-256 hashes match SHA256SUMS.txt byte-exactly,
so Phase C.0 gate **PASSES** for the first time across the
three Q20A dispatches. Phase A* re-validated from cache via
SHA-256 (8e6f9eb…f7496 anchor + 06d87de…0ac277 wrapper), no
re-execution. Phase C.1 (Wasow §X.3) **HALTS** because the
Wasow PDF is image-only (zero text bytes via either pypdf or
pdfminer.six; tesseract not available). Phase C.2 (Birkhoff
1930 §§2-3) **PARTIAL**: §2 formal-series existence theorem is
extracted with three verbatim ≤30-word quotes and is uniform
in n and p, hence uniform-in-d theorem-grade citable for the
formal-direction half of PCF-2 v1.3 §3.3.A* (`xi_0(d) = d / β_d^{1/d}`).
Phase C.2 (ii) — the Borel-singularity-radius identification
named in Prompt 018 §2 step 5 — is **NOT in Birkhoff 1930
§§2-3** (recorded as a spec error in `unexpected_finds.json`).
Aggregate Phase C.3 = `C_LITERATURE_BLOCKED_AT_C1`. Phase D
verdict = new halt code `HALT_Q20A_WASOW_PDF_IMAGE_ONLY`
(no Prompt 018 ladder entry fits cleanly).

Net dispatch 3 outcome strictly **strengthens** dispatches 1/2:
the formal half of the Q20a upgrade now has theorem-grade
citation (Birkhoff 1930 §2, uniform in d ≥ 1).

## Key numerical findings

- Phase A* anchor SHA-256:
  `8e6f9ebde933652e2581578d282163f0220091ea0ee4adbd6754bd53458f7496`
  (matches dispatch 1/2 entries exactly).
- Phase A* wrapper SHA-256:
  `06d87de35ee3bf62e848283ba703d63d88307e08f8f2a44389765c10810ac277`
  (matches dispatch 1/2 entries exactly).
- Birkhoff 1930 PDF SHA-256:
  `aeb5291e4150535969726aa9e8aba8c604ae437612e026092122208cb3952efa`
  (4/4 path-aliases match SHA256SUMS.txt; 42 pages, text layer
  extractable).
- Wasow 1965 chap X PDF SHA-256:
  `e84b3e4823f60c049e8dfc9c2fae2c6c5271ec229d1f80d623a4778d5de46410`
  (4/4 path-aliases match SHA256SUMS.txt; 7 pages, **no text
  layer**; pdfminer.six returns 7 bytes total, all 0x0c).
- Phase A* cached d ∈ {2..10} sweep result (still valid):
  18/18 tests pass; rel_err = 0 in 16/18, ≤ 1.8e-51 in 2/18 at
  dps=50 (entries #1-9 of `claims.jsonl`).

## Judgment calls made

1. **Phase C.0 path-mismatch accepted as PASS.** Prompt 018
   spec gates on workspace-root path
   `literature/g3b_2026-05-03/`; operator placed PDFs under
   the runbook-canonical
   `tex/submitted/control center/literature/g3b_2026-05-03/`.
   Hashes match SHA256SUMS.txt byte-exactly. I treated this
   as gate PASS rather than halting on the literal path
   string (which would have been the dispatch-1/2 behaviour).
   Documented in `phase_c0_gate_pass.md` and
   `unexpected_finds.json` finding #3.

2. **Wasow §X.3 not OCR'd.** I did not attempt to install
   tesseract (system-level admin operation) nor invoke a
   cloud OCR API (Rule 1: no API-key actions). Halted at
   Phase C.1 honestly. Future operator action required.

3. **Borel-half of Phase C.2 reported as spec error rather
   than fabricated.** AEAL discipline forbids extracting
   theorems that are not in the cited text. The Borel-
   singularity-radius theorem named in Prompt 018 §2 step 5
   is provably absent from Birkhoff 1930 §§2-3 (word "Borel"
   absent from the entire §§2-3 text dump; §3 treats the
   formal converse problem only). I recorded this as a
   prompt-spec inaccuracy and pointed at B–T 1933 / Wasow
   §X.3 as the likely actual source. Synthesizer should
   amend Prompt 018 spec for dispatch 4.

4. **New halt code `HALT_Q20A_WASOW_PDF_IMAGE_ONLY` adopted.**
   Prompt 018 §3 verdict ladder does not list this exact
   condition. The closest entry,
   `HALT_Q20A_LITERATURE_NOT_LANDED`, is technically wrong:
   PDFs ARE landed (hashes verified). Coining a precise new
   code is more useful for downstream than forcing a poor
   ladder fit. Dispatches 1/2 also coined non-ladder verdicts
   (`UPGRADE_DEFERRED_PENDING_LITERATURE_LANDING`).

## Anomalies and open questions

THIS IS THE MOST IMPORTANT SECTION.

1. **Prompt 018 §2 step 5 mis-attributes the Borel-singularity
   radius theorem to Birkhoff 1930 §§2-3.** It is not there.
   Birkhoff 1930 is the *formal-series* theory paper (cf.
   abstract: "the formal questions are also treated"). The
   *analytic* theory companion is Birkhoff–Trjitzinsky 1933
   (Acta Math 60), which is in the broader G3b queue but not
   yet acquired (per `_OPERATOR_INSTRUCTIONS.md`). Wasow §X.3
   may also contain it. Synthesizer: please amend Prompt 018
   §2 step 5 (ii) to point at B–T 1933 (or Wasow §X.3 with
   readable PDF) before dispatch 4.

2. **Wasow Dover reprint via IA borrow viewer produces
   image-only PDFs.** This is a structural fact about the IA
   workflow described in `_OPERATOR_INSTRUCTIONS.md` § "Source
   2". Operator should be advised that future IA-sourced
   PDFs need OCR or an alternative source (e.g. an
   institutional library scan with text layer, or manual
   transcription of just the relevant theorems X.3.x). For
   dispatch 4 specifically: a 1-page text file containing
   verbatim transcriptions of Wasow §X.3 theorems X.3.1–X.3.3
   would be sufficient and minimal-effort (≤ 30 minutes
   operator time, comparable to one IA borrow cycle).

3. **Path-mismatch between spec and runbook.** Prompt 018
   uses workspace-root `literature/...`; runbook uses
   `tex/submitted/control center/literature/...`. Both work
   for dispatch 3 (operator chose the runbook path; I
   accepted it as gate PASS). But the literal path-string
   gate of dispatches 1/2 wasted two cycles. Recommend
   pinning one canonical path in the spec for dispatch 4.

4. **Two consecutive dispatches now coined non-ladder verdict
   codes** (dispatch 2:
   `UPGRADE_DEFERRED_PENDING_LITERATURE_LANDING`; dispatch 3:
   `HALT_Q20A_WASOW_PDF_IMAGE_ONLY`). This is a sign that the
   Q20a verdict ladder under-specifies the partial-extraction
   regime. Synthesizer may want to expand the ladder for
   dispatch 4 to include
   `UPGRADE_PARTIAL_FORMAL_HALF_THEOREM` and
   `HALT_Q20A_WASOW_OCR_REQUIRED` (or equivalent names).

5. **Anomaly #2 from dispatches 1/2 (`A_DIRECT_IDENTITY_d10`
   sitting unused) is finally addressed in dispatch 3.** The
   d-extension result combines with Birkhoff §2 formal
   existence to give a reasonably strong conjecture-with-
   formal-half-theorem landmark. Synthesizer should consider
   whether to land this in CT v1.5 / D2-NOTE v1.5 *now*
   independently of Wasow §X.3, rather than waiting for
   dispatch 4 (cf. Recommended next step alternative).

## What would have been asked (if bidirectional)

- "Should I attempt a manual OCR pass on the 7 image pages of
  Wasow §X.3 (browser-driven cloud OCR via the IA viewer's
  text-extract feature, if accessible)?" — I judged this
  equivalent to a Rule 1 / Rule 2 violation and did not.
- "Is the Borel-singularity-radius theorem you want me to
  extract actually in B–T 1933 §§2 (or §§3-4), and should
  Phase C.2 (ii) be re-targeted accordingly?"
- "Do you want me to land the dispatch-3 strengthening
  (Birkhoff §2 uniform-in-d formal half) into a draft
  D2-NOTE v1.5 *now*, even though Phase E is gated on
  UPGRADE_*?"

## Recommended next step

**Primary:** before dispatch 4, operator either
(a) transcribes Wasow §X.3 theorems (X.3.1, X.3.2, X.3.3 — or
whatever Wasow's actual numbering is) into a text file under
`tex/submitted/control center/literature/g3b_2026-05-03/wasow_X3_transcription.txt`,
SHA-adds it to SHA256SUMS.txt, and re-fires Q20A; OR
(b) acquires Birkhoff–Trjitzinsky 1933 (Acta Math 60) per the
G3b runbook and synthesizer re-targets Phase C.2 (ii) at B–T
1933 §§2-3 in a Prompt 018 v2.

**Alternative:** synthesizer drafts a separate
`Q20A-LIT-INDEPENDENT-PARTIAL-LANDING` prompt that lands the
two dispatch-3 strengthenings (`A_DIRECT_IDENTITY_d10` +
Birkhoff §2 formal existence uniform in d) into CT v1.5 §3.3
or D2-NOTE v1.5 as a "extended-conjecture-with-formal-half-
theorem" landmark, *independent of* Wasow §X.3 and the
Borel half. This unlocks downstream value now without waiting
on the Wasow OCR cycle.

## Files committed (this dispatch)

New / replaced this dispatch:
- `phase_c0_gate_pass.md` (new; gate PASS doc + hash table + path judgment)
- `phase_c1_wasow_verification.md` (new; halt doc for Wasow image-only PDF)
- `phase_c2_birkhoff_verification.md` (new; §2 (i) extracted; §3 converse; §2 (ii) NIA reported)
- `phase_c_summary.md` (new; aggregate Phase C.3)
- `phase_d_verdict.md` (replaced; dispatch 3 verdict; prior archived)
- `phase_d_verdict_pre_refire2.md` (new; archive of dispatch 2 verdict)
- `handoff.md` (this file; replaces dispatch 2 handoff)
- `handoff_pre_dispatch3.md` (new; archive of dispatch 2 handoff)
- `claims.jsonl` (appended; 39 entries total = 21 prior + 18 new)
- `halt_log.json` (replaced; now carries 3-dispatch history)
- `halt_log_pre_dispatch3.json` (new; archive of dispatch 2 halt log)
- `unexpected_finds.json` (replaced; 3 new findings)
- `unexpected_finds_pre_dispatch3.json` (new; archive of prior empty file)
- `extract_pdfs.py` (new; pypdf-based extraction script for §C.1/C.2)
- `wasow.txt` (new; pypdf extraction output; 7 empty-page markers)
- `birkhoff.txt` (new; pypdf extraction output; 42 pages of text)

Files unchanged from prior dispatches (carried forward):
- `phase_a_star_extended_sweep.py` (SHA-256 verified, no drift)
- `phase_a_star_results.json`, `phase_a_star_run.log`,
  `phase_a_star_summary.md`
- `phase_c_gate_halt.md` (dispatch 1), `phase_c_gate_halt_refire.md` (dispatch 2)
- `discrepancy_log.json` (still `{}`)
- `handoff_pre_refire.md`, `handoff_pre_refire2.md`,
  `phase_d_verdict_pre_refire.md`

## AEAL claim count

18 entries appended to `claims.jsonl` this dispatch
(Phase A* cache verify ×2; Phase C.0 hash matches ×4;
Phase C.1 halt evidence ×3; Phase C.2 (i) extraction ×5;
Phase C.2 (ii) NIA ×1; Phase C.2 §3 ×1; Phase C.3 ×1;
Phase D ×1).

Total across 3 dispatches: **39** AEAL entries (>= 31
target per dispatch 2 §4 success criterion).
