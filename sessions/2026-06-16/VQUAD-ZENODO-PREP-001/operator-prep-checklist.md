# Operator prerequisites checklist — VQUAD-ZENODO-PREP-001 (Stage 5)

Hand-actions that must complete **before** the eventual `VQUAD-ZENODO-DEPOSIT-001`
slot runs. This slot prepares; the deposit slot executes once every box is checked.
**0 of 14 complete** at hand-off (this is a prep slot; nothing is executed here).

## A. Paper-final gate (must clear first)

- [ ] **Cold-read of paper complete; Verdict A** (or B-resolved). Currently
      UNRECORDED — the bundle slot flagged this open.
- [ ] **VQUAD-PAPER-CORRECTIONS-001 complete.** Slot does not yet exist; the paper
      is still "working draft; not yet submitted" (`paper.tex` L46).
- [ ] **Fresán response received and incorporated** (or confirmed-deferred). The
      FRESAN-JOSSEN-INQUIRY-001 letter is drafted-not-sent.
- [ ] **Marchal personal-communication citation finalized** in §2 of the paper
      (June 2026 personal comm.; the convention L₁,₂ = x² + (1/3)x + 1/3).

## B. Bundle gate

- [ ] **VQUAD-REPRO-BUNDLE-002 generated and verified.** Current artifact is
      BUNDLE-001 (held). The deposit supplements BUNDLE-002 (post-corrections
      regeneration). Its concept DOI fills the `isSupplementTo` placeholder, OR the
      paper+bundle deposit as one record and that row is dropped.

## C. Re-pin gate (hashes change when the paper changes)

- [ ] **PDF SHA-256 re-pinned** against the final corrected PDF. Provisional pin
      (current byte-reproducible draft `vquad-periodrep-paper.pdf`):
      `359d1172af3f867f4349cf4776a222813a855cd354bc78c0b68ccfb0026c702b`.
      See `deposit-pin-update-instructions.md`.
- [ ] **metadata-anchor SHA-256 re-pinned** against any title/abstract/MSC/
      affiliation/version change. Current anchor (`zenodo_metadata.md`):
      `dee9195c7957f25fc57f497d6875cdd2b63d97d24f55f36b5e54e388ec003eb8`.
- [ ] **Affiliation decision resolved (F-AFFIL):** blank (corpus convention) vs.
      brief's "Independent Researcher, Yokohama, Japan". Changes the anchor.
- [ ] **Anticipatory-references decision resolved (F-ANTICIPATORY):** either the
      corrections pass adds citations for EBR-Ib / EBR-II / δ-Fredholm / the 3
      Marchal papers, OR the operator ratifies them as pure provenance-graph
      `references` links. (Affects whether check (b) reference↔related-id passes.)

## D. Token gate (operator hand-steps — never the agent)

- [ ] **`set_prod_token.ps1` executed** — production `ZENODO_TOKEN` exported in the
      same PowerShell process that will run the deposit.
- [ ] **`check_prod_token.ps1` confirms** scope `deposit:write` (+ `deposit:actions`
      if publishing via API) and instance = production (zenodo.org).

## E. Staging integrity gate

- [ ] **Re-confirm PDF on-disk hash after staging (Trap 7).** OneDrive/file-copy can
      alter bytes; recompute `Get-FileHash -Algorithm SHA256` on the PDF *in the
      deposit folder* and confirm it equals the re-pinned value before `--execute`.
- [ ] **Gate constants updated** in `run_production_draft.py` (or a deposit copy):
      `PDF_NAME`, `PDF_SHA256_PIN`, `METADATA_ANCHOR`, `TITLE`, `BLOCKLIST`,
      Gate-1 count assertion, and the forbidden-venue token (`ETNA`→`Compositio`).
      See `deposit-pin-update-instructions.md`. **This is the largest single task.**

---

**Gate between this slot and the deposit slot:** all 14 boxes checked. Until then
`VQUAD-ZENODO-DEPOSIT-001` does not open. No box is checkable by the agent — every
item is an operator hand-action or depends on a not-yet-existing slot.
