# Stage 2 — PDF pin refresh (run-3)

**New PDF pin (supersedes run-2's `4ca12a35…`):**

| field | value |
|-------|-------|
| `PDF_NAME` | `vquad-periodrep-paper.pdf` |
| **SHA-256** | `33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea` |
| **MD5** | `99faea5b0f4095788e4ee932436beeda` |
| size | 773171 bytes |
| pages | 24 |

**Source:** the layout-fixed PDF from `VQUAD-PAPER-LAYOUTFIX-001` (`627d17e`), identical to
the copy embedded in `VQUAD-REPRO-BUNDLE-002` run-2 (`56a1402`). Both SHA-256 and MD5
computed with `Get-FileHash` against
`…/VQUAD-REPRO-BUNDLE-002/run-2/vquad-periodrep-bundle/paper/vquad-periodrep-paper.pdf`
(byte-identical to the LAYOUTFIX `latex/` source). Byte-reproducibility independently
re-confirmed (in-place + pristine-temp-dir builds) in BUNDLE-002 run-2.

**Why the hash moved (reflow-only):** the layout fix cleared 20→0 overfull `\hbox` (breakable
monospace + display/table reflow). The PDF text diff was −2 line-end hyphens and 0 content
characters — no digit, symbol, word, or equation changed. The hash moved only because the
glyph **positions** changed.

## Why both hashes

- **SHA-256** is the Gate-2 pin in `run_production_draft.py` (`PDF_SHA256_PIN`): the runner
  re-hashes the staged PDF and halts on mismatch.
- **MD5** is the integrity value **Zenodo returns** after a bucket file upload
  (`"checksum": "md5:<hex>"`). At deposit, compare Zenodo's returned MD5 to
  `99faea5b0f4095788e4ee932436beeda`. (Do **not** compare the SHA-256 pin to Zenodo's
  checksum — that is an MD5 field; a SHA-vs-MD5 compare false-halts every upload.)

## Trap-7 reminder — PENDING HAND-ACTION (operator, at deposit)

After staging the PDF in the deposit folder, re-run
`(Get-FileHash -Algorithm SHA256 .\vquad-periodrep-paper.pdf).Hash.ToLower()` and confirm it
still equals **`33f339ed…`** before `--execute` (file-copy / OneDrive can alter bytes). This
is a backstop the agent cannot resolve in advance; it is a hand-step performed against the
actual staged file at deposit time.
