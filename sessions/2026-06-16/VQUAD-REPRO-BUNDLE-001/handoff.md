# Handoff — VQUAD-REPRO-BUNDLE-001

**Status:** Reproducibility bundle **assembled and integrity-verified**; staged
and **HELD** (no commit, no push, no Zenodo deposit) per the standing meta-rule.

## What was produced

- **`vquad-periodrep-bundle/`** — the bundle tree (40 files): paper (PDF + self-
  contained `.tex` + `preamble.tex` + bundle `build.py`), 14 verification scripts
  in 4 narrative-ordered directories, 12 reference result JSONs, 4 reproducibility
  docs, top-level README, and a CC BY 4.0 LICENSE.
- **`vquad-periodrep-bundle.zip`** — the packaged archive.
  - SHA-256 `e7eff5c85de1a495165730742772ec0a0eac6aa58f46bb210ce4c37bf43d3432`
  - 708568 bytes, 40 entries, portable (forward-slash, single top dir, testzip OK).
- Slot records: `prerequisite-check.md`, `inventory.md`,
  `bundle-integrity-verification.md`, `bundle-archive-info.md`, `ledger.json`,
  `claims.jsonl`, this `handoff.md`.
- Auditable build tooling (kept in slot root, **not** shipped in the bundle):
  `relativize_and_copy.py` (parent→bundle transformer),
  `verify_bundle.py` (integrity harness), `_package_bundle.py` (packager).

## Integrity result

- **All 13 runnable essential scripts pass** (exit 0; 11 exact match to `data/`,
  1 match-modulo-volatile, 1 stdout-only). No hardcoded absolute paths.
- **Paper reproduces byte-for-byte**: `python paper/build.py` → 23 pp, 0 errors,
  PDF SHA-256 `359d1172…` (matches the deposited target), re-confirmed in a
  pristine temp dir.
- **HALT GATE 5: PASS.**

## Open gate (read before depositing)

This slot certifies **bundle integrity**, not paper editorial-finality. Two
prerequisites named in the brief are **not yet satisfied**:

1. `VQUAD-PAPER-CORRECTIONS-001` does not exist in the bridge.
2. The cold-read verdict is unrecorded.
3. `FRESAN-JOSSEN-INQUIRY-001` is drafted, not sent (G-MOTGALOIS gap is
   conditional-pending in the paper's §6 framing).

The bundle is built against the current byte-reproducible draft. If corrections
land later, re-run `relativize_and_copy.py` (if scripts change) and
`_package_bundle.py`, then refresh the two SHA-256 values.

## Recommended next operator actions

1. **Review the bundle** — open `vquad-periodrep-bundle/README.md`, skim
   `docs/`, spot-check a script per directory.
2. **Close the paper-final gate** — run/record the cold-read and any
   `VQUAD-PAPER-CORRECTIONS-001` work; if the PDF changes, rebuild + re-hash.
3. **Decide on the Fresán inquiry** — send it (and fold the reply into a
   corrections slot) or accept the conditional §6 framing for this deposit.
4. **Deposit** — run the next slot **VQUAD-ZENODO-DEPOSIT-001**: upload
   `paper/vquad-periodrep-paper.pdf` and `vquad-periodrep-bundle.zip` under
   CC BY 4.0, mirroring the creator/ORCID/license metadata of the prior V_quad
   records (concept-linked to 10.5281/zenodo.20455090). Verify the Zenodo
   server-side MD5 of the uploaded zip (Zenodo returns `md5:…`, not SHA-256).
5. **Release this slot** — when authorized, commit with the prepared message
   ("VQUAD-REPRO-BUNDLE-001 — reproducibility bundle assembled and verified;
   ready for Zenodo deposit") + Co-authored-by trailer, and push.

## Standing-rule disposition

Slot `git add`-staged, **HELD**. No commit, no push, no deposit performed by the
agent. HEAD unchanged at `f3dd3a4`. Also still held in the bridge:
`VQUAD-REVIEW-PREP-001`, `FRESAN-JOSSEN-INQUIRY-001`.
