# Stage 7 — Runner constant pins, FINAL (run-2)

The operator updates these in the **deposit working copy** of
`run_production_draft.py` (and identically in `run_sandbox_draft.py`) before
`--execute`. Do **not** fork the Sakai kit. Every value is sourced from this run's
Stage 2–4 deliverables.

## Constant block (FINAL — supersedes the PREP-001 provisionals)

| Loc | Constant | **FINAL V_quad value** | supersedes |
|-----|----------|------------------------|------------|
| L44 | `PDF_NAME` | `vquad-periodrep-paper.pdf` | — |
| L45 | `PDF_SHA256_PIN` | `4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe` | provisional `359d1172…` |
| L46 | `METADATA_ANCHOR` | `4a75234faaef79d68caed6588d0fa0e2418ae17dfb2c18825a150b92f7970895` | provisional `dee9195c…` |
| L47 | `TITLE` | `An explicit exponential-period representation of the V_quad connection coefficient` | — |
| L48–49 | `BLOCKLIST` | 7-DOI set below | — |
| L110 | Gate-1 assertion | **Scenario B** branch below | Sakai `==19` |
| L131–132 | forbidden-venue token | `Compositio` | `ETNA` |

```python
BLOCKLIST = {"20455090", "20481592", "20694841", "19885550",
             "20569724", "20571232", "20624814"}

# Gate-1 count assertion (Scenario B — isSupplementTo dropped, 11 ids):
sp = sum(1 for r in arr if r["relation"] == "isSupplementTo")
if not (len(arr) == 11 and c == 2 and ip == 1 and rf == 8 and sp == 0):
    halt("wired array not hole-free 11 (2+1+8+0).")
```

## Files the runner loads (copy into the deposit folder)

- `vquad-periodrep-paper.pdf` — the `4ca12a35…` PDF (from BUNDLE-002 `paper/`).
- `zenodo_metadata.md` — this slot's run-2 copy (anchor `4a75234f…`).
- `related_identifiers.md` — this slot's run-2 copy (11 ids, Scenario B).
- `vquad-periodrep-bundle.zip` — BUNDLE-002 archive (`8752d7c7…`), the secondary file.

## Zenodo upload MD5 (Stage 2)

After the bucket upload, Zenodo returns `"checksum": "md5:<hex>"`. Confirm it equals
the **MD5** `028a1a5d9e10a3a9487596f6db3e6a38` (not the SHA-256 pin — that is an MD5
field; a SHA-vs-MD5 compare false-halts every upload).

## Procedure (operator)

1. Paste the constants above into the deposit copy of `run_production_draft.py`
   **and** `run_sandbox_draft.py`.
2. Dry-run (no `--execute`, no network): `python run_production_draft.py` — re-checks
   Gate 1 (11 ids) and Gate 2 (PDF/anchor/venue) against the new pins.
3. Sandbox `--execute` first (`sandbox.zenodo.org`, sandbox token), then production
   `--execute` — **STOP at the publish gate** (agent runs none of this).
