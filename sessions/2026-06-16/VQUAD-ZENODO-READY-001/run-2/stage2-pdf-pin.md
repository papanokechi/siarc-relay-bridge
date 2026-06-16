# Stage 2 — PDF pin refresh (re-run / run-2)

**New PDF pin (supersedes the provisional `359d1172…`):**

| field | value |
|-------|-------|
| `PDF_NAME` | `vquad-periodrep-paper.pdf` |
| **SHA-256** | `4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe` |
| **MD5** | `028a1a5d9e10a3a9487596f6db3e6a38` |
| size | 714771 bytes |
| pages | 24 |

**Source:** the corrections-final PDF from `VQUAD-PAPER-CORRECTIONS-001` (`d4fc87a`),
identical to the copy embedded in `VQUAD-REPRO-BUNDLE-002` (`a33ff59`). Both SHA-256
and MD5 computed with `Get-FileHash` against
`…/VQUAD-REPRO-BUNDLE-002/vquad-periodrep-bundle/paper/vquad-periodrep-paper.pdf`.

## Why both hashes

- **SHA-256** is the Gate-2 pin in `run_production_draft.py` (`PDF_SHA256_PIN`): the
  runner re-hashes the staged PDF and halts on mismatch.
- **MD5** is the integrity value **Zenodo returns** after a bucket file upload
  (`"checksum": "md5:<hex>"`). At deposit, compare Zenodo's returned MD5 to
  `028a1a5d9e10a3a9487596f6db3e6a38` to confirm the upload was not corrupted.
  (Do **not** compare the SHA-256 pin to Zenodo's checksum — that is an MD5 field;
  a SHA-vs-MD5 compare would false-halt every upload.)

## Trap-7 reminder (operator, at deposit)

After staging the PDF in the deposit folder, re-run
`(Get-FileHash -Algorithm SHA256 .\vquad-periodrep-paper.pdf).Hash.ToLower()` and
confirm it still equals `4ca12a35…` before `--execute` (file-copy / OneDrive can
alter bytes). The byte-reproducibility of this PDF is independently confirmed
(in-place + pristine-temp-dir builds) in `VQUAD-REPRO-BUNDLE-002`.
