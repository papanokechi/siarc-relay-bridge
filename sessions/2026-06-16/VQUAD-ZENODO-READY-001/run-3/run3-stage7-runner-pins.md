# Stage 6 — Runner constant pins, FINAL (run-3)

The operator updates these in the **deposit working copy** of `run_production_draft.py` (and
identically in `run_sandbox_draft.py`) before `--execute`. Do **not** fork the Sakai kit.
Every value is sourced from this run's Stage 2–5 deliverables. **Only the PDF and bundle pins
move vs run-2; the anchor, title, BLOCKLIST, and Gate-1 assertion are unchanged.**

## Constant block (FINAL — supersedes run-2's pins)

| Loc | Constant | **run-3 value** | supersedes (run-2) |
|-----|----------|-----------------|--------------------|
| L44 | `PDF_NAME` | `vquad-periodrep-paper.pdf` | — |
| L45 | `PDF_SHA256_PIN` | `33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea` | `4ca12a35…` |
| L46 | `METADATA_ANCHOR` | `4a75234faaef79d68caed6588d0fa0e2418ae17dfb2c18825a150b92f7970895` | **unchanged** |
| L47 | `TITLE` | `An explicit exponential-period representation of the V_quad connection coefficient` | — |
| L48–49 | `BLOCKLIST` | 7-DOI set below | — |
| L110 | Gate-1 assertion | **Scenario B** branch below | unchanged |
| L131–132 | forbidden-venue token | `Compositio` | — |

```python
BLOCKLIST = {"20455090", "20481592", "20694841", "19885550",
             "20569724", "20571232", "20624814"}

# Gate-1 count assertion (Scenario B — isSupplementTo dropped, 11 ids):
sp = sum(1 for r in arr if r["relation"] == "isSupplementTo")
if not (len(arr) == 11 and c == 2 and ip == 1 and rf == 8 and sp == 0):
    halt("wired array not hole-free 11 (2+1+8+0).")
```

## Files the runner loads (copy into the deposit folder)

- `vquad-periodrep-paper.pdf` — the **`33f339ed…`** PDF (from BUNDLE-002 **run-2** `paper/`).
- `zenodo_metadata.md` — this slot's **run-3** copy (anchor `4a75234f…`; byte-identical to run-2).
- `related_identifiers.md` — this slot's **run-3** copy (11 ids, Scenario B; byte-identical to run-2).
- `vquad-periodrep-bundle.zip` — BUNDLE-002 **run-2** archive (**`7bc5d008…`**), the secondary file.

## Zenodo upload MD5 (per uploaded file)

After each bucket upload, Zenodo returns `"checksum": "md5:<hex>"`. Confirm:
- paper PDF → MD5 `99faea5b0f4095788e4ee932436beeda`
- bundle zip → MD5 `c1b5a39c0b56576e81b5c5723935669f`

(Compare MD5↔MD5, never the SHA-256 pin to Zenodo's checksum — a SHA-vs-MD5 compare
false-halts every upload.)

## Procedure (operator)

1. Paste the constants above into the deposit copy of `run_production_draft.py` **and**
   `run_sandbox_draft.py`.
2. Dry-run (no `--execute`, no network): `python run_production_draft.py` — re-checks Gate 1
   (11 ids) and Gate 2 (PDF `33f339ed…` / anchor `4a75234f…` / venue) against the new pins.
3. Sandbox `--execute` first (`sandbox.zenodo.org`, sandbox token), then production
   `--execute` — **STOP at the publish gate** (agent runs none of this).
