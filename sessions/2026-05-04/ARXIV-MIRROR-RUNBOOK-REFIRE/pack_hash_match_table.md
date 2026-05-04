# pack_hash_match_table — ARXIV-MIRROR-RUNBOOK-REFIRE

Compiled 2026-05-04. Deposited-PDF md5/sha256/size compared against
live Zenodo API for each of the 5 published records. Source rows for
the 4 non-PCF-1 records reuse 032 audit cache + each pack's cached
`zenodo.pdf` (the byte-equal Zenodo download); PCF-1 row reuses 030
manifest + live API GET against record 19937196 in 034 PHASE A.1.

**AEAL deposit gate** = md5+sha+size+pages of the deposited PDF
(`zenodo.pdf` for records 1, 3, 4, 5; `p12_pcf1_main.pdf` for record
2 — byte-equal to Zenodo per 030).  **Local-rebuild drift** =
expected pdfTeX `/CreationDate` timestamp drift in the locally
compiled `pack/<pdf>`; size + page count match exactly, md5+sha
differ; this is the same regime 032 documented and is NOT a FAIL
gate (Zenodo serves the deposit, not the local rebuild).

| Record | PDF size (B) | Pages | Deposit md5 (Zenodo-match) | Deposit SHA-256 match | Rebuild drift | Overall |
|---|---:|---:|---|---|---|---|
| `siarc_umbrella_v2.0` | 455,178 | 12 | `d633699fbfe698da…` (PASS) | PASS | expected (timestamp) | **PASS** |
| `pcf1_v1.3` | 392,886 | 16 | `fbf5449b2678834b…` (PASS) | PASS | none (byte-equal) | **PASS** |
| `pcf2_v1.3` | 558,153 | 22 | `cdd628911f3fd95c…` (PASS) | PASS | expected (timestamp) | **PASS** |
| `ct_v1.3` | 581,459 | 17 | `e58951de5cbf1be7…` (PASS) | PASS | expected (timestamp) | **PASS** |
| `t2b_v3.0` | 331,769 | 8 | `d245be3b2b60cf04…` (PASS) | PASS | expected (timestamp) | **PASS** |

Local source artefacts (tex + tar.gz) for each pack:

| Record | tex SHA-256 (short) | tex size | tar.gz SHA-256 (short) | tar.gz size |
|---|---|---:|---|---:|
| `siarc_umbrella_v2.0` | `612f732ebe2d…` | 44,935 | `19d709a952e6…` | 16,395 |
| `pcf1_v1.3` | `e83bb377f297…` | 46,349 | `93770e03c6ab…` | 17,560 |
| `pcf2_v1.3` | `507704dbf618…` | 74,911 | `96da73905c66…` | 33,197 |
| `ct_v1.3` | `59c5352795f8…` | 70,178 | `acccc8123f0b…` | 33,370 |
| `t2b_v3.0` | `9bdd6a5d799b…` | 28,635 | `7eec81322af1…` | 10,762 |

Verdict: all 5 deposited PDFs match Zenodo md5+size+SHA-256+pages.
No re-rebuild needed. PHASE A.2 → PASS.