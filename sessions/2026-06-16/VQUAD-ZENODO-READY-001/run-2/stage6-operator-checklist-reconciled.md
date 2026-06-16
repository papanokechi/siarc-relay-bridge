# Stage 6 — Operator prerequisites checklist, reconciled (run-2)

Reconciles the PREP-001 `operator-prep-checklist.md` against current reality. That
checklist enumerated **13 boxes** (its header's "14" miscounts the bullets by one),
"0 of 14 complete" at PREP-001 hand-off. **9 of 13 are now resolved** by the
corrections chain + this re-run; the remaining **4 are operator hand-steps** (token
×2, post-staging re-hash, apply gate constants — values fully prepared here).

## A. Paper-final gate
- [x] **Cold-read complete; Verdict A** — `VQUAD-COLDREAD-001` (`e207b33`).
- [x] **VQUAD-PAPER-CORRECTIONS-001 complete** — `d4fc87a`; PDF `4ca12a35…`, 24 pp.
- [x] **Fresán response — CONFIRMED-DEFERRED** — operator: deposit now with §6 as
      drafted (doubly-conditional G-MOTGALOIS heuristic; cold-read certified it
      honest/never-overclaimed). A substantive reply, if it arrives, is a **Zenodo v2
      enhancement**, not a held gate.
- [x] **Marchal personal-communication citation finalized** — corrections M-3 added
      O. Marchal (3 papers) + B-4 acknowledgement (personal communication, June 2026).

## B. Bundle gate
- [x] **VQUAD-REPRO-BUNDLE-002 generated and verified** — `a33ff59`; archive
      `8752d7c7…`, integrity PASS. **Scenario B** → `isSupplementTo` placeholder
      **dropped** (the bundle is a secondary file in the paper's single deposit; no
      separate bundle DOI to fill).

## C. Re-pin gate
- [x] **PDF SHA-256 re-pinned** — `4ca12a35…` (Stage 2; supersedes provisional `359d1172…`).
- [x] **metadata-anchor SHA-256 re-pinned** — `4a75234f…` (Stage 3; supersedes provisional `dee9195c…`).
- [x] **F-AFFIL resolved** — Option C: "Independent Researcher, Yokohama, Japan".
- [x] **F-ANTICIPATORY resolved** — the corrections pass (M-3 + L-1) added the
      EBR-Ib / EBR-II / δ-Fredholm / 3 Marchal citations to the bibliography, so the
      reference↔related-id check (b) passes **naturally** — no "pure provenance"
      ratification needed.

## D. Token gate — OPERATOR hand-steps (never the agent)
- [ ] **`set_prod_token.ps1` executed** — production `ZENODO_TOKEN` in the deposit shell.
- [ ] **`check_prod_token.ps1` confirms** scope `deposit:write` (+ `deposit:actions`
      if API-publishing) and instance = production (zenodo.org).

## E. Staging integrity gate
- [ ] **Re-confirm PDF on-disk hash after staging (Trap 7)** — recompute SHA-256 on
      the PDF *in the deposit folder*; must equal `4ca12a35…`. (Source-PDF hash
      already confirmed by the agent; this box is the post-copy re-check.)
- [x→operator] **Gate constants updated in `run_production_draft.py`** — the exact
      final values are prepared in `stage7-runner-pins.md`; the operator pastes them
      into the deposit working copy (and the sandbox script). Largest single task,
      now reduced to copy-paste.

**Summary: 9/13 resolved; 4 operator hand-steps remain (D1, D2, E1, and applying the
prepared E2 constants).** The deposit gate (`VQUAD-ZENODO-DEPOSIT-001`) opens once the
4 operator boxes are checked.
