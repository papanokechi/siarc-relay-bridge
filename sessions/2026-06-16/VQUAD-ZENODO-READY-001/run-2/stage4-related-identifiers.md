# Stage 4 — Related identifiers: Scenario B + Gate 1 → PASS (run-2)

**Decision:** Scenario B confirmed (operator). The bundle is a **secondary file in
the paper's single deposit**, so there is **no separate bundle DOI**. The
`isSupplementTo` placeholder from PREP-001 is **dropped entirely** (not filled).

## Count: 12 → 11

| relation | count | identifiers |
|----------|-------|-------------|
| `continues` | 2 | V_quad companion (concept) `10.5281/zenodo.20455089`; Sakai program (concept) `10.5281/zenodo.20694840` |
| `isPartOf` | 1 | SIARC umbrella (concept) `10.5281/zenodo.19885549` |
| `references` | 8 | EBR-Ib `10.5281/zenodo.20569723`; EBR-II `10.5281/zenodo.20566465`; δ-Fredholm `10.5281/zenodo.20624813`; Sakai-2001 CMP `10.1007/s002200100446`; Kovacic `10.1016/S0747-7171(86)80010-4`; Marchal–Alameddine CMP `10.1007/s00220-024-05187-0`; Iwaki–Marchal–Saenz `10.1016/j.geomphys.2017.10.009`; Marchal–Orantin `10.1063/5.0002260` |
| `isSupplementTo` | **0** | **placeholder dropped (Scenario B)** |
| **total** | **11** | was 12 |

The full array is in `related_identifiers.md`, the underscore-named file the runner
loads. Every DOI is sourced from PREP-001 `related-identifiers-resolved.json`, never
memory. **Zenodo concepts** are used throughout (3 in `references`, 2 in `continues`,
1 in `isPartOf`); the remaining 5 `references` entries are external publisher DOIs.

## Gate 1 — automated assertions (`_validate_related_ids.py`)

```
len=11 continues=2 isPartOf=1 references=8 isSupplementTo=0
count assertion 11 (2+1+8+0): True
placeholders remaining: []
BLOCKLIST version-DOI leak: []
retracted 20455090 present: False
concept 20455089 present: True
all scheme=doi: True
GATE 1: PASS
```

**BLOCKLIST** (version DOIs that must never leak):
`20455090, 20481592, 20694841, 19885550, 20569724, 20571232, 20624814` — none present.
The wired array uses **concept** DOIs only (`20455089, 20694840, 19885549, 20569723,
20566465, 20624813`) plus 5 external publisher DOIs.

**Hole-free:** no `{{…}}` placeholders remain; all entries `scheme=doi`; the retracted
v1.0 `20455090` is absent and the companion is cited at its concept DOI `20455089`.
