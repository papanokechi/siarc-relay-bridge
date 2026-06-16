# Related identifiers — FINAL (V_quad period-rep deposit, Scenario B)

**Slot:** VQUAD-ZENODO-READY-001 · **run-2 (re-run)** · 2026-06-16
**STATUS: STAGED FOR OPERATOR REVIEW — NOT MINTED.**
**Supersedes** the PREP-001 provisional `related-identifiers.md` (12 ids, bundle
placeholder). This is the deposit-ready array the runner loads as
`related_identifiers.md`.

## What changed vs PREP-001 (Stage 4 of the re-run)

1. **Scenario B → `isSupplementTo` row DROPPED.** The bundle ships as a *secondary
   file in this same Zenodo record* (paper PDF + `vquad-periodrep-bundle.zip` in one
   deposit), so there is **no separate bundle DOI** to point at. The placeholder
   `{{VQUAD-REPRO-BUNDLE-002-CONCEPT-DOI}}` row is removed entirely (not filled).
   Count: **12 → 11** (2 `continues` + 1 `isPartOf` + 8 `references` + **0**
   `isSupplementTo`).
2. **F-ANTICIPATORY → RESOLVED.** All 6 previously-anticipatory `references`
   (EBR-Ib, EBR-II, δ-Fredholm, and the three Marchal topological-recursion papers)
   are now **printed in the corrections-final bibliography** (added by
   CORRECTIONS-001 M-3 + L-1). Every `references` target is therefore grounded in
   the deposited PDF — the reference↔related-id consistency check passes naturally;
   no operator ratification of "pure provenance links" is required.

All DOIs are **concept** (cite-all parent) DOIs, sourced from
`VQUAD-ZENODO-PREP-001/related-identifiers.md` and `related-identifiers-resolved.json`
(themselves line-cited to the corpus `sakai-stratification/related_identifiers.md`,
`DEPOSIT_LOG_INDEX.md`, and the paper bibliography) — **never from memory**. The
retracted V_quad v1.0 **version** DOI `20455090` is NOT wired (concept `20455089`
is); see the no-leak check below.

## Relation graph (11 ids)

| Relation | Targets |
|---|---|
| `continues` (×2) | V_quad companion (concept `20455089`), Sakai-Stratification program (concept `20694840`) |
| `isPartOf` (×1) | SIARC umbrella program (concept `19885549`) |
| `references` (×8) | EBR-Ib `20569723`, EBR-II `20566465`, δ-Fredholm `20624813`, Sakai-2001 CMP `10.1007/s002200100446`, Kovacic-1986 JSC `10.1016/S0747-7171(86)80010-4`, Marchal-Alameddine-2024 `10.1007/s00220-024-05187-0`, Iwaki-Marchal-Saenz-2018 `10.1016/j.geomphys.2017.10.009`, Marchal-Orantin-2020 `10.1063/5.0002260` |

## Paste-ready array (11 ids — no placeholders)

`_`-prefixed keys are annotations stripped by `clean_meta` before send.

```json
{
  "related_identifiers": [
    { "identifier": "10.5281/zenodo.20455089", "relation": "continues",  "scheme": "doi", "resource_type": "publication-preprint", "_ref": "VQUAD-parent" },
    { "identifier": "10.5281/zenodo.20694840", "relation": "continues",  "scheme": "doi", "resource_type": "publication-preprint", "_ref": "SAKAI-STRAT-program" },
    { "identifier": "10.5281/zenodo.19885549", "relation": "isPartOf",   "scheme": "doi", "_ref": "SIARC-umbrella" },
    { "identifier": "10.5281/zenodo.20569723", "relation": "references", "scheme": "doi", "resource_type": "publication-preprint", "_ref": "EBR-Ib" },
    { "identifier": "10.5281/zenodo.20566465", "relation": "references", "scheme": "doi", "resource_type": "publication-preprint", "_ref": "EBR-II" },
    { "identifier": "10.5281/zenodo.20624813", "relation": "references", "scheme": "doi", "resource_type": "publication-preprint", "_ref": "FRED-delta" },
    { "identifier": "10.1007/s002200100446", "relation": "references", "scheme": "doi", "_ref": "Sakai-2001-CMP" },
    { "identifier": "10.1016/S0747-7171(86)80010-4", "relation": "references", "scheme": "doi", "_ref": "Kovacic-1986-JSC" },
    { "identifier": "10.1007/s00220-024-05187-0", "relation": "references", "scheme": "doi", "_ref": "Marchal-Alameddine-2024-CMP" },
    { "identifier": "10.1016/j.geomphys.2017.10.009", "relation": "references", "scheme": "doi", "_ref": "Iwaki-Marchal-Saenz-2018-JGP" },
    { "identifier": "10.1063/5.0002260", "relation": "references", "scheme": "doi", "_ref": "Marchal-Orantin-2020-JMP" }
  ]
}
```

## Gate-1 assertions (Scenario B)

The runner's Gate-1 count assertion becomes (per `deposit-pin-update-instructions.md`,
Scenario B branch):

```python
if not (len(arr)==11 and c==2 and ip==1 and rf==8):
    halt("wired array not hole-free 11 (2+1+8).")
```

- `len==11`, `continues==2`, `isPartOf==1`, `references==8`, `isSupplementTo==0`. ✓
- **No version/record-DOI leak:** none of the BLOCKLIST version DOIs
  (`20455090`, `20481592`, `20694841`, `19885550`, `20569724`, `20571232`,
  `20624814`) appears in the array. ✓
- Retracted V_quad v1.0 `20455090` **absent**; concept `20455089` **present**
  (the only V_quad-companion identifier). ✓
- No `{{…}}` placeholder remains. ✓

Validated programmatically: see `stage4-related-identifiers.md` and
`_validate_related_ids.py` in this slot.

## Operator may still enrich (optional)

The 8 `_available_to_add` in-paper publisher DOIs (vdPS, Hien, Berry–Howls,
Loday-Richaud, gfun, ore_algebra, Ramanujan Machine, Nesterenko — all printed in
the bibliography) may be wired for a richer graph (Sakai wired 15 `references`).
If added, bump `rf` and `len` in the Gate-1 assertion accordingly.

## NOT changed
Manuscript content untouched; staging only. No DOI minted, no API called.
