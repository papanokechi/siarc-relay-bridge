# Stage 1 — Prerequisite verification (run-3)

**Date:** 2026-06-16 (Asia/Tokyo) · **HEAD:** `56a1402` · **Slot:** `VQUAD-ZENODO-READY-001/run-3`

run-3 is a **HASH-REFRESH** of run-2 (`2a7f969`): the only things that changed since run-2
are the paper PDF (`4ca12a35…` → `33f339ed…`) and the bundle archive (`8752d7c7…` →
`7bc5d008…`). The layout fix was proven **reflow-only** (no abstract, reference, or value
changed), so no metadata content is re-derived — only the PDF/bundle pins move, and the
gates are re-confirmed against the new PDF.

## Prerequisites (all met)

| prerequisite | commit | evidence |
|--------------|--------|----------|
| VQUAD-PAPER-LAYOUTFIX-001 | `627d17e` | layout-fixed PDF `33f339ed…`, 20→0 overfull, reflow-only |
| VQUAD-REPRO-BUNDLE-002 run-2 | `56a1402` | re-pinned bundle archive `7bc5d008…`, integrity PASS, embeds `33f339ed…` |
| VQUAD-ZENODO-READY-001 run-2 | `2a7f969` | the stale pin set (template); pins `4ca12a35…` / `8752d7c7…` |

## New artifacts confirmed on disk (Get-FileHash)

| artifact | path | SHA-256 | MD5 | size |
|----------|------|---------|-----|------|
| layout-fixed PDF | `…/VQUAD-REPRO-BUNDLE-002/run-2/vquad-periodrep-bundle/paper/vquad-periodrep-paper.pdf` | `33f339ed…` ✓ | `99faea5b…` ✓ | 773171 B ✓ |
| (same PDF, source) | `…/VQUAD-PAPER-LAYOUTFIX-001/latex/vquad-periodrep-paper.pdf` | `33f339ed…` ✓ (byte-identical) | `99faea5b…` | 773171 B |
| bundle archive | `…/VQUAD-REPRO-BUNDLE-002/run-2/vquad-periodrep-bundle.zip` | `7bc5d008…` ✓ | `c1b5a39c…` ✓ | 776968 B ✓ |

Full hashes:
- PDF SHA-256 `33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea`, MD5 `99faea5b0f4095788e4ee932436beeda`
- bundle SHA-256 `7bc5d00885bd823a758c4476f60e950a88f54e9f42b7a4bf254730ac894de013`, MD5 `c1b5a39c0b56576e81b5c5723935669f`

## Supersedes (run-2 stale pins)

| pin | run-2 (stale) | run-3 (new) |
|-----|---------------|-------------|
| PDF SHA-256 | `4ca12a35d655df…582fe` | `33f339edd17c54…3eea` |
| PDF MD5 | `028a1a5d…` | `99faea5b…` |
| PDF size | 714771 B | 773171 B |
| bundle SHA-256 | `8752d7c7…` | `7bc5d008…` |
| bundle MD5 | (run-2 did not pin) | `c1b5a39c…` |
| bundle size | 721715 B | 776968 B |
| metadata anchor | `4a75234f…` | **`4a75234f…` (unchanged — see Stage 3)** |
| related-ids count | 11 | 11 (unchanged) |

**Disposition:** all prerequisites met; new PDF and bundle exist and hash exactly as stated.
Proceed to the pin refresh (Stages 2–4) and gate re-confirmation (Stage 5).
