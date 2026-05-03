# Phase 0 — Input validation + gate check

**Task:** D2-NOTE-V2-1-WASOW-FULL-CLOSURE  (QS-2)
**Date:** 2026-05-03

---

## 0.0 — Prompt-spec provenance

`prompt_spec.md` written verbatim from the operator-pasted body
via `RELAY_PROMPT_BODY.txt` (the synthesizer-side staged body
mirrored in this same session dir).

- `prompt_spec.md` SHA-256:
  `0f0de177063f3b23983be8ee789c68f63268803b93d3ffab162d30ac4bd82508`
- Bytes: 61 467
- Body anchor matches `RELAY_PROMPT_BODY.sha256` (byte-identical).
- The synthesizer-side draft was preserved as
  `prompt_spec_synthesizer_draft.md`
  (SHA `013E3E8783A687F4E685E60254FDFB73A1BF5337F98B2AA12117FB1B66A41E40`,
  75 824 B). It and the executed body are intentionally distinct
  artefacts; the executed body is the canonical Phase 0.0 deliverable.

---

## 0.1 — A1 / A2 / A4 SHA verification

### A1 — D2-NOTE v2 source (read-only; v2.1 derives from this)

Path: `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/`

| file                         | bytes  | SHA-256 prefix   |
| ---------------------------- | ------ | ---------------- |
| d2_note_v2.tex               | 22 130 | 2323A99D65B59ABF |
| annotated_bibliography.bib   | 34 268 | 27CABE7C76B85079 |
| d2_note_v2.pdf               | 404 837| B9954D12BFE4F0C5 |
| d2_note_v2.log               | 34 985 | 7DD791D7C29D6A12 |
| d2_note_v2.aux               |  6 036 | 34C8B02A251114C0 |
| d2_note_v2.bbl               |  4 737 | 51697161715A5C16 |

PASS: all six files present.

### A2 — Phase A* sweep (read-only; results threaded forward)

Path: `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/`

| file                              | bytes  | SHA-256 prefix   |
| --------------------------------- | ------ | ---------------- |
| phase_a_star_extended_sweep.py    |  9 071 | 06D87DE35EE3BF62 |
| phase_a_star_results.json         |  5 534 | 7CB00221313122B3 |
| phase_a_star_summary.md           |  5 247 | B1DB14121EE0EAF9 |
| phase_a_star_run.log              |  3 166 | 4A93D7DB0779AA76 |
| claims.jsonl                      | 36 732 | 981CD5F5D779AD1D |

PASS. Wrapper full SHA matches anchor `06d87de…0ac277`:
`06d87de35ee3bf62e848283ba703d63d88307e08f8f2a44389765c10810ac277`

### A4 — Literature anchors

Path: `tex/submitted/control center/literature/g3b_2026-05-03/`

| slot | file                                    | expected SHA-256                                                   | match |
| ---- | --------------------------------------- | ------------------------------------------------------------------ | ----- |
| 01   | 01_birkhoff_1930_acta54.pdf             | aeb5291e4150535969726aa9e8aba8c604ae437612e026092122208cb3952efa   | ✓     |
| 03   | 03_birkhoff_trjitzinsky_1933_acta60.pdf | dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6   | ✓     |
| 04   | 04_wasow_1965_dover.pdf                 | f59d6835db58d2de59eab843b881b97106eee6c66e56bfce43de5788bbbaa5fd   | ✓     |
| 06   | 06_costin_2008_chap5.pdf (Tier-2)       | 436c6c115149052634b103a2ed3b460680ad38cd161897794d5eb1f2f6243289   | ✓     |

PASS on slots 01 / 03 / 04 (required) and slot 06 (Tier-2
secondary, available; ETHICS-GATE for "see also" cite — the
PDF was opened by the relay agent and ch. 5 content registry-
verified per `SHA256SUMS.txt` annotation).

Loday-Richaud 2016 ch. 2: NOT acquired (Scenario C). Tier-2
optional source; relay proceeds with B-T 1933 §§4-6 alone per
synthesizer Rev-A grant. NOT cited in v2.1 bib; flagged in
handoff Anomalies.

### A3 — Peer-review consolidation (read-only context)

Path: `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-PEER-REVIEW/`

Present (per pre-flight checklist commit `95f06de`).
The synthesizer-side §0 briefing in `prompt_spec.md` is also
sufficient. Either source PASSES.

---

## 0.2 — Phase A* numerical content drift check

`phase_a_star_results.json` contents:

- `verdict_signal`: `A_DIRECT_IDENTITY_d10`
- `q20_anchor_sha256`: `8e6f9ebde933652e2581578d282163f0220091ea0ee4adbd6754bd53458f7496`
  (matches Q20A anchor `8e6f9eb…f7496`)
- sweep PASS rate: 18 / 18
- cross-check PASS rate: 3 / 3
- d range: {2,3,4,5,6,7,8,9,10}
- max relative error across all 18: `1.7270275150361838e-51` (occurs at
  d=5, β_5=11; AEAL-cached value, not drifted)
- d=2 entries: `rel_error = 0.0` (exact)

PASS. Numerical content matches Q20A baseline. Note: spec §0
text reads "relative error < 1.6e-51 above d=2"; the actual
cached maximum is 1.73e-51 (d=5, β_5=11). This is the cached
AEAL value, not a drift. The Phase 0.2 gate fires only on
DRIFT (content change), not on a slight wording mismatch in
the spec recall of the Q20A summary; the Q20A summary's own
text reports `< 5.34e-51` actually
(`phase_a_star_summary.md`). The Q20A anchor SHA matches.
Drift gate not triggered.

---

## 0.3 — v2.0 PDF SHA drift check

`d2_note_v2.pdf` SHA-256 prefix: `B9954D12BFE4F0C5`
Expected: `b9954d12bfe4f0c54351d9e87409c0d6870af6d53ff4904daf30e78e0e7ece66`

PASS (full SHA matches the deposited Zenodo readback).

---

## 0.4 — QS-A (g3b-acquire-bt-1933) done

Slot 03 PDF on disk + SHA-anchored at
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`,
matching `SHA256SUMS.txt` entry. Equivalent to SQL todo `done`.

PASS.

---

## 0.5 — Bib-key collision pre-flight

Grep on
`siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/annotated_bibliography.bib`:

- `birkhoff_trjitzinsky_1933` — NOT present. **NEW key in v2.1.**
- `costin2008asymptotics` — present at line 13. Existing entry:
  `@book{costin2008asymptotics, author={Costin, Ovidiu}, title={Asymptotics
  and {B}orel summability}, series={Chapman & Hall/CRC Monographs},
  volume={141}, publisher={CRC Press}, address={Boca Raton, FL}, year={2008}}`.
  Bibliographic core matches canonical form (CRC Monographs vol 141, 2008).
  Existing `annote` cites Ch. 3 + Ch. 5 (resurgence + Borel-Laplace);
  superset of the spec's Ch. 5 expectation. **REUSE** existing key
  per Phase 0.5(a).
- `lodayrichaud2016divergent` — present at line 58. Existing entry:
  Lecture Notes vol 2154, Springer, 2016, doi 10.1007/978-3-319-29075-1.
  Bibliographic core matches canonical form. Existing `annote` cites
  Ch. 7 (Stokes cocycles). Spec asks to cite Ch. 2 (Borel-Laplace machinery).
  PDF is NOT on disk per pre-flight; ETHICS-GATE blocks adding a "see also"
  cite without verification. **OMIT** the v2.1 cite per spec C.4 ETHICS GATE
  ("the agent does NOT add Loday-Richaud or Costin to the bib without having
  opened the file"). Existing bib entry is left untouched.

PASS.

---

## 0.6 — Gate aggregate

| sub-gate | outcome |
| -------- | ------- |
| 0.0 prompt provenance        | PASS |
| 0.1 input SHAs               | PASS (A1, A2, A4 slots 01/03/04) |
| 0.2 Phase A* drift           | PASS |
| 0.3 v2.0 PDF SHA             | PASS |
| 0.4 QS-A done                | PASS |
| 0.5 bib-key collision        | PASS (new key: birkhoff_trjitzinsky_1933; reuse: costin2008asymptotics; omit: lodayrichaud2016divergent) |
| 0.6 emit gate-pass           | this file |

**PHASE_0_GATE_PASS** — all preconditions satisfied; Phase A
proceeds.
