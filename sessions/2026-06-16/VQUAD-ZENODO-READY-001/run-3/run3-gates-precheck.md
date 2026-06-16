# Stage 5 — Gate re-confirmation against the new PDF (run-3) → ALL PASS

Static re-confirmation mirroring what `run_production_draft.py` enforces at deposit time.
The wrong-venue gate (2.2) is re-run against the **layout-fixed** PDF `33f339ed…` (not the
run-2 `4ca12a35…`), because the reflow changed glyph positions and thus the extracted text
stream — so the check must be repeated on the actual new file. Harness:
`run-3/_validate_related_ids.py` (PDF path repointed to the BUNDLE-002 run-2 paper PDF).

## Gate 1 — related identifiers (Scenario B): PASS — UNCHANGED from run-2

```
=== GATE 1 (related identifiers, Scenario B) ===
len=11 continues=2 isPartOf=1 references=8 isSupplementTo=0
count assertion 11 (2+1+8+0): True
placeholders remaining: []
BLOCKLIST version-DOI leak: []
retracted 20455090 present: False
concept 20455089 present: True
all scheme=doi: True
GATE 1: PASS
```

`related_identifiers.md` is byte-identical to run-2 (the layout fix touched no reference);
this is a re-confirmation, not a re-derivation. BLOCKLIST (version DOIs that must never leak):
`20455090, 20481592, 20694841, 19885550, 20569724, 20571232, 20624814` — none present.

## Gate 2.1 — PDF SHA-256 == the new pin: PASS

The harness reads the deposit-target PDF and prints its SHA-256:
```
PDF sha256: 33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea
```
Equals the Stage-2 pin `33f339ed…` exactly.

## Gate 2.2 — wrong-venue absent in the 33f339ed PDF: PASS

```
=== GATE 2.2 (wrong-venue, vs 33f339ed PDF) ===
PDF chars: 63713
Compositio   present: False
AAECC        present: False
ETNA         present: False
'Symbolic Comput' (legit Kovacic cite) present: True
GATE 2.2: PASS
```

- `Compositio` (canonical wrong-venue halt token) — **absent**.
- `AAECC` (the venue that desk-rejected EBR-III) — **absent**.
- `ETNA` (legacy Sakai-kit placeholder) — **absent**.
- `Symbolic Comput` **present** = the legitimate Kovacic citation (*J. Symbolic Comput.* 2
  (1986) 3–43), correctly **not** a venue leak.

**Note on the char count:** 63713 chars vs run-2's 63635 (Δ +78). The text *content* is
unchanged (LAYOUTFIX proved reflow-only, −2 hyphens / 0 content); the small extracted-char
delta is a pypdf artifact of re-flowed line breaks / de-hyphenation across the layout-fixed
lines. No forbidden token appears either way — which is exactly why the brief mandates
re-running the gate on the actual new file rather than trusting the run-2 result.

## Gate 2.3 — metadata anchor: PASS (unchanged)

Anchor = `4a75234f…` (Stage 3, Case A: not PDF-hash-dependent; `zenodo_metadata.md`
byte-identical to run-2, re-hash confirms). The runner's `METADATA_ANCHOR` constant is
unchanged.

## Summary

| gate | result | vs run-2 |
|------|--------|----------|
| Gate 1 (related-ids, 11, hole-free, no leak) | **PASS** | unchanged |
| Gate 2.1 (PDF SHA == `33f339ed…`) | **PASS** | re-pinned |
| Gate 2.2 (wrong-venue absent in new PDF) | **PASS** | re-run on `33f339ed…` |
| Gate 2.3 (metadata anchor `4a75234f…`) | **PASS** | unchanged |

All gates PASS against the new PDF + bundle. Deposit-ready pin set established.
