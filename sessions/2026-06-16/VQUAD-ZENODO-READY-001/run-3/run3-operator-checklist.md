# Stage 6 — Operator prerequisites checklist (run-3)

Carries the run-2 reconciliation forward, with the two re-pin boxes updated to the
layout-fixed values. **9 of 13 resolved; the same 4 operator hand-steps remain** — only the
hash values in the re-pin / Trap-7 boxes changed.

## A. Paper-final gate
- [x] **Cold-read complete; Verdict A** — `VQUAD-COLDREAD-001` (`e207b33`).
- [x] **VQUAD-PAPER-CORRECTIONS-001 complete** — `d4fc87a`; corrections-final paper, 24 pp.
- [x] **VQUAD-PAPER-LAYOUTFIX-001 complete** — `627d17e`; 20→0 overfull, reflow-only; PDF
      re-pinned `4ca12a35…` → **`33f339ed…`** (the deposit-target PDF).
- [x] **Fresán response — CONFIRMED-DEFERRED** — deposit now with §6 as drafted; any reply is
      a Zenodo v2 enhancement, not a held gate.
- [x] **Marchal personal-communication citation finalized** — O. Marchal (3 papers) + B-4
      acknowledgement.

## B. Bundle gate
- [x] **VQUAD-REPRO-BUNDLE-002 run-2 generated and verified** — `56a1402`; archive
      **`7bc5d008…`** (re-pinned to `33f339ed…`), integrity PASS. **Scenario B** →
      `isSupplementTo` placeholder **dropped** (no separate bundle DOI).

## C. Re-pin gate
- [x] **PDF SHA-256 re-pinned** — **`33f339ed…`** (Stage 2; supersedes run-2 `4ca12a35…`).
- [x] **bundle archive re-pinned** — **`7bc5d008…`** (Stage 4; supersedes run-2 `8752d7c7…`).
- [x] **metadata-anchor SHA-256** — `4a75234f…` (Stage 3; **unchanged** — not PDF-dependent).
- [x] **F-AFFIL resolved** — Option C: "Independent Researcher, Yokohama, Japan".
- [x] **F-ANTICIPATORY resolved** — bibliography already carries EBR-Ib / EBR-II / δ-Fredholm /
      3 Marchal citations; reference↔related-id check passes naturally.

## D. Token gate — OPERATOR hand-steps (never the agent)
- [ ] **`set_prod_token.ps1` executed** — production `ZENODO_TOKEN` in the deposit shell.
- [ ] **`check_prod_token.ps1` confirms** scope `deposit:write` (+ `deposit:actions` if
      API-publishing) and instance = production (zenodo.org).

## E. Staging integrity gate
- [ ] **Re-confirm PDF on-disk hash after staging (Trap 7)** — recompute SHA-256 on the PDF
      *in the deposit folder*; must equal **`33f339ed…`** (updated from run-2's `4ca12a35…`).
- [x→operator] **Gate constants updated in `run_production_draft.py`** — the exact final
      values are prepared in `run3-stage7-runner-pins.md`; the operator pastes them into the
      deposit working copy (and the sandbox script).

**Summary: 9/13 resolved; 4 operator hand-steps remain (D1, D2, E1 re-hash vs `33f339ed…`, and
applying the prepared E2 constants).** The deposit gate (`VQUAD-ZENODO-DEPOSIT-001`) opens once
the 4 operator boxes are checked — **and** after DEPOSIT-001/MANUAL-UPLOAD.md is reconciled from
the stale `4ca12a35…`/`8752d7c7…` to `33f339ed…`/`7bc5d008…` (the next task).
