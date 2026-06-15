# Deposit pin-update instructions — VQUAD-ZENODO-PREP-001 (Stage 5.2)

The Sakai kit's `run_production_draft.py` / `run_sandbox_draft.py` carry
**Sakai-specific hard-coded constants** at the top + two in-gate strings. The
V_quad deposit reuses the *same script* (do not fork the kit) but the operator
must update these values in the **deposit working copy** before `--execute`.
Source of every value below is this slot's Stage-2/Stage-3/Stage-4 deliverables.

> A `deposit-pins.json` does not exist yet (it is created at deposit time). When it
> does, mirror the same values into it. Until then, these are the authoritative
> pre-pins.

## Constants to update (current Sakai value → V_quad value)

| Loc (prod script) | Constant | Sakai value | **V_quad value** | Source |
|---|---|---|---|---|
| L44 | `PDF_NAME` | `sakai-stratification-pcf.pdf` | **`vquad-periodrep-paper.pdf`** | bundle `paper/` |
| L45 | `PDF_SHA256_PIN` | `7f7cb8e0…df8f` | **`359d1172af3f867f4349cf4776a222813a855cd354bc78c0b68ccfb0026c702b`** ⚠️ PROVISIONAL | current byte-reproducible draft; **re-pin to FINAL corrected PDF** |
| L46 | `METADATA_ANCHOR` | `929fef4e…21a3d` | **`dee9195c7957f25fc57f497d6875cdd2b63d97d24f55f36b5e54e388ec003eb8`** ⚠️ PROVISIONAL | `metadata-anchor-current.txt`; **re-pin after corrections** |
| L47 | `TITLE` | `The Sakai Stratification of PCF Transcendence` | **`An explicit exponential-period representation of the V_quad connection coefficient`** | `zenodo_metadata.md`; current draft |
| L48-49 | `BLOCKLIST` | Sakai's 11 version DOIs | **V_quad set below** | Stage-2 flags |
| L131-132 | forbidden-venue token | `ETNA` | **`Compositio`** | `wrong-venue-token-decision.md` |

### V_quad `BLOCKLIST` (version/record DOIs that must NOT appear in the wired array)

These are the **version/record** counterparts of the **concept** DOIs we wired —
the gate halts if any leaks in. (Our wired array uses only the concepts, so the
gate passes; the blocklist is the tripwire.)

```python
BLOCKLIST = {"20455090",  # Vquad v1.0 version (concept 20455089 wired)
             "20481592",  # StokesNote v1.2 record (same concept 20455089)
             "20694841",  # Sakai-strat version (concept 20694840 wired)
             "19885550",  # SIARC umbrella version (concept 19885549 wired)
             "20569724",  # EBR-Ib record (concept 20569723 wired)
             "20571232",  # EBR-II v1.2 record (concept 20566465 wired)
             "20624814"}  # FRED δ version (concept 20624813 wired)
```

### Gate-1 count assertion (L110) — MUST change

Sakai asserts `len(arr)==19 and c==3 and ip==1 and rf==15`. That logic counts only
`continues`/`isPartOf`/`references` and assumes no other relation. **V_quad adds an
`isSupplementTo` row**, so the assertion must count it. Two scenarios:

```python
# Scenario A — bundle DOI filled, isSupplementTo kept (12 ids):
sp = sum(1 for r in arr if r["relation"]=="isSupplementTo")
if not (len(arr)==12 and c==2 and ip==1 and rf==8 and sp==1):
    halt("wired array not hole-free 12 (2+1+8+1).")

# Scenario B — paper+bundle = one record, isSupplementTo dropped (11 ids):
if not (len(arr)==11 and c==2 and ip==1 and rf==8):
    halt("wired array not hole-free 11 (2+1+8).")
```

> If the operator adds any of the 8 `_available_to_add` publisher DOIs, bump `rf`
> and `len` accordingly. The placeholder `{{VQUAD-REPRO-BUNDLE-002-CONCEPT-DOI}}`
> is NOT a valid DOI — it must be filled (Scenario A) or the row removed (Scenario
> B) before `--execute`, or Zenodo will reject the metadata.

## Re-pin commands (PowerShell)

```powershell
# PDF (run AFTER staging the FINAL corrected PDF in the deposit folder; Trap 7):
(Get-FileHash -Algorithm SHA256 .\vquad-periodrep-paper.pdf).Hash.ToLower()

# Metadata anchor (run AFTER any title/abstract/MSC/affiliation/version edit):
(Get-FileHash -Algorithm SHA256 .\zenodo_metadata.md).Hash.ToLower()
```

Paste each result into the matching constant (and into `deposit-pins.json` when it
exists). The dry-run (`python run_production_draft.py`, no `--execute`) re-checks
Gate 2 against the new pins with no network call — use it to confirm before
exporting the token.

## Sandbox script note

`run_sandbox_draft.py` carries the **same** constant block + ETNA string. Apply the
identical edits there for the Step-4 sandbox dry-run (it targets
`sandbox.zenodo.org`; a separate sandbox token).
