# Related identifiers — DOI cross-reference graph (V_quad period-rep deposit)

**STATUS: STAGED FOR OPERATOR REVIEW — NOT MINTED.** Resolution drawn from
*authoritative local sources only* — the line-cited corpus table
`sakai-stratification/related_identifiers.md` (itself sourced from the SIARC
ledger `submission_log.txt`), `DEPOSIT_LOG_INDEX.md`, and the V_quad paper's own
printed bibliography — plus three external Marchal journal DOIs verified against
the arXiv API. **Never from memory.** Conflicts/gaps are flagged, not guessed.

> **Trap-6 note.** The originating task brief supplied **version/record** DOIs for
> five works (VQUAD 20455090, EBR-Ib 20569724, EBR-II 20571232, FRED 20624814,
> UMB 19885550). All five are corrected to the **concept** (cite-all parent) DOI
> below. See the flag summary.

---

## ⚠️ Relation-verb gotcha (read before mint)

Zenodo's metadata API rejects the DataCite term `isContinuationOf` with HTTP 400.
The corpus convention is **`continues`**. All continuation rows below use
`continues`. The operator may additionally mirror each `continues` target as a
`cites` row (corpus belt-and-suspenders precedent; EBR-IV did this).

---

## Relation graph

| Relation (use at mint) | Targets |
|---|---|
| `continues` (NOT `isContinuationOf`) | VQUAD-parent, SAKAI-STRAT-program — the immediate predecessors |
| `isPartOf` | SIARC umbrella program concept `10.5281/zenodo.19885549` |
| `isSupplementTo` | VQUAD-REPRO-BUNDLE-002 — **PLACEHOLDER** (bundle not yet regenerated) |
| `references` | corpus deposits (EBR-Ib, EBR-II, δ-Fredholm), the two load-bearing external method refs (Sakai 2001, Kovacic 1986), and the three Marchal topological-recursion papers |

---

## Resolution table

`VERIFIED` = concept DOI confirmed against an authoritative local source, no
conflict. `VERIFIED-EXTERNAL` = journal DOI confirmed via arXiv API / publisher
page. `PLACEHOLDER` = to be filled at deposit time.

### Continuation predecessors (`continues`)

| Ref | brief DOI | Resolved concept DOI | Relation | Status | Source / note |
|---|---|---|---|---|---|
| VQUAD-parent | `…20455090` (v1.0) | **10.5281/zenodo.20455089** | continues | VERIFIED | V_quad paper bibitem `Vquad` L1242-1243 prints "(concept 20455089)"; sakai table L84. v1.2 record (`StokesNote`) 20481592 = **same concept** — do not double-wire. **In bibliography ✓** |
| SAKAI-STRAT-program | `…20694840` | **10.5281/zenodo.20694840** | continues | VERIFIED | `DEPOSIT_LOG_INDEX.md` §B#35 L14 (version 20694841 / concept 20694840). The program paper (bibitem `Sakai`), distinct from Sakai 2001 CMP below. **In bibliography ✓** |

### Umbrella (`isPartOf`)

| Ref | brief DOI | Resolved concept DOI | Relation | Status | Source / note |
|---|---|---|---|---|---|
| SIARC-umbrella | `…19885550` (version) | **10.5281/zenodo.19885549** | isPartOf | VERIFIED | `related_identifiers.template.md` L65; sakai table L71; `_zenodo_uploader.py` `SIARC_UMBRELLA_CONCEPT`. Provenance link, not a bibitem. |

### Supplement (`isSupplementTo`)

| Ref | DOI | Relation | Status | Source / note |
|---|---|---|---|---|
| VQUAD-REPRO-BUNDLE-002 | `{{BUNDLE-002-CONCEPT-DOI}}` | isSupplementTo | **PLACEHOLDER** | Bundle not regenerated (current = BUNDLE-001, held). **Fill at deposit**, or **drop** if paper + bundle deposit as one record (Sakai model). |

### Corpus deposits (`references`)

| Ref | brief DOI | Resolved concept DOI | Relation | Status | Source / note |
|---|---|---|---|---|---|
| EBR-Ib | `…20569724` (record) | **10.5281/zenodo.20569723** | references | VERIFIED | sakai table L78 / array L130; ledger §B Item 29 L1152-1156. ⚠️ **Anticipatory — not in current bib.** |
| EBR-II | `…20571232` (v1.2 record) | **10.5281/zenodo.20566465** | references | VERIFIED | sakai table L65 / array L117; ledger §B Item 31 L1175-1176. ⚠️ **Anticipatory — not in current bib.** |
| FRED-δ | `…20624814` (version) | **10.5281/zenodo.20624813** | references | VERIFIED | sakai table L80 / array L121; ledger L803 region. ⚠️ **Anticipatory — not in current bib.** |

### External works (`references`) — publisher / journal DOI

| Ref | DOI | Relation | Status | Source / note |
|---|---|---|---|---|
| Sakai-2001-CMP | **10.1007/s002200100446** | references | VERIFIED | V_quad paper bibitem `SakaiClass` L1284. Comm. Math. Phys. 220 (2001) 165-229. **In bibliography ✓** Distinct from SAKAI-STRAT-program (continues). |
| Kovacic-1986-JSC | **10.1016/S0747-7171(86)80010-4** | references | VERIFIED | V_quad paper bibitem `Kovacic` L1265. J. Symbolic Comput. 2 (1986) 3-43. **In bibliography ✓** Central method ref (Galois of L_φ). |
| Marchal-Alameddine-2024 | **10.1007/s00220-024-05187-0** | references | VERIFIED-EXTERNAL | arXiv 2302.13905 ("Published version in Comm. Math. Phys."); HAL hal-04019889. ⚠️ **Anticipatory — not in current bib.** |
| Iwaki-Marchal-Saenz-2018 | **10.1016/j.geomphys.2017.10.009** | references | VERIFIED-EXTERNAL | J. Geom. Phys. 124 (2018) 16-54. prefix+vol+pages self-consistent; give a live confirm at mint. ⚠️ **Anticipatory.** |
| Marchal-Orantin-2020 | **10.1063/5.0002260** | references | VERIFIED-EXTERNAL | arXiv API 1901.04344 `<arxiv:doi>`. J. Math. Phys. ⚠️ Rejected hallucinated `10.1063/1.5135288`. **Anticipatory.** |

### Available to add (resolved, in-paper publisher DOIs — operator may wire)

vdPS `10.1007/978-3-642-55750-7`, Hien `10.1007/s00222-009-0196-4`, Berry-Howls
`10.1098/rspa.1990.0111`, Loday-Richaud `10.1007/978-3-319-29075-1`, gfun
`10.1145/178365.178368`, ore_algebra `10.1007/978-3-319-15081-9_6`,
Ramanujan Machine `10.1038/s41586-021-03229-4`, Nesterenko
`10.1070/SM1996v187n09ABEH000158`. All printed in the paper bibliography
(L1271–L1348); add for a richer graph (Sakai wired 15 references).

---

## Paste-ready array (12 ids; the bundle row is the only placeholder)

`_`-prefixed keys (`_ref`, `_flag`, `_note`) are annotations stripped by
`clean_meta` before send. **Re-verify every `_flag` row against the live Zenodo
record before mint.** The `isSupplementTo` row holds the only `{{…}}` slot.

```json
{
  "related_identifiers": [
    { "identifier": "10.5281/zenodo.20455089", "relation": "continues",  "scheme": "doi", "resource_type": "publication-preprint", "_ref": "VQUAD-parent", "_flag": "brief 20455090 = v1.0 version; concept 20455089 (StokesNote 20481592 = same concept)" },
    { "identifier": "10.5281/zenodo.20694840", "relation": "continues",  "scheme": "doi", "resource_type": "publication-preprint", "_ref": "SAKAI-STRAT-program" },
    { "identifier": "10.5281/zenodo.19885549", "relation": "isPartOf",   "scheme": "doi", "_ref": "SIARC-umbrella", "_flag": "brief 19885550 = version; concept 19885549" },
    { "identifier": "{{VQUAD-REPRO-BUNDLE-002-CONCEPT-DOI}}", "relation": "isSupplementTo", "scheme": "doi", "_ref": "REPRO-BUNDLE", "_flag": "PLACEHOLDER — fill at deposit, or drop if paper+bundle = one record" },
    { "identifier": "10.5281/zenodo.20569723", "relation": "references", "scheme": "doi", "resource_type": "publication-preprint", "_ref": "EBR-Ib", "_flag": "brief 20569724 = record; concept 20569723. ANTICIPATORY — not in current bib" },
    { "identifier": "10.5281/zenodo.20566465", "relation": "references", "scheme": "doi", "resource_type": "publication-preprint", "_ref": "EBR-II", "_flag": "brief 20571232 = v1.2 record; concept 20566465. ANTICIPATORY — not in current bib" },
    { "identifier": "10.5281/zenodo.20624813", "relation": "references", "scheme": "doi", "resource_type": "publication-preprint", "_ref": "FRED-delta", "_flag": "brief 20624814 = version; concept 20624813. ANTICIPATORY — not in current bib" },
    { "identifier": "10.1007/s002200100446", "relation": "references", "scheme": "doi", "_ref": "Sakai-2001-CMP", "_flag": "paper L1284; distinct from SAKAI-STRAT-program" },
    { "identifier": "10.1016/S0747-7171(86)80010-4", "relation": "references", "scheme": "doi", "_ref": "Kovacic-1986-JSC", "_flag": "paper L1265" },
    { "identifier": "10.1007/s00220-024-05187-0", "relation": "references", "scheme": "doi", "_ref": "Marchal-Alameddine-2024-CMP", "_flag": "ANTICIPATORY — not in current bib" },
    { "identifier": "10.1016/j.geomphys.2017.10.009", "relation": "references", "scheme": "doi", "_ref": "Iwaki-Marchal-Saenz-2018-JGP", "_flag": "ANTICIPATORY — not in current bib; live-confirm DOI at mint" },
    { "identifier": "10.1063/5.0002260", "relation": "references", "scheme": "doi", "_ref": "Marchal-Orantin-2020-JMP", "_flag": "ANTICIPATORY — not in current bib; rejected hallucinated 10.1063/1.5135288" }
  ],
  "_operator_verify_unresolved": [
    "FJ-monograph (Fresán–Jossen 'Exponential Motives', book in prep, expmot.pdf; NO DOI — bibliography-only)",
    "P7-P11-governance-stack (NOT cited in V_quad bib; no clean concept DOIs in submission_log — UNRESOLVED, do not guess)",
    "CMF (arXiv:2303.09318 preprint — bibliography-only, or wire scheme=arxiv)",
    "Dingle-1973 / Ecalle-1981-85 / DLMF / Whittaker-Watson-1927 (books/online, no DOI — bibliography-only)"
  ]
}
```

---

## Flag summary (for the pre-mint checklist)

- **F-DOI-1** [VQUAD] brief `20455090` = v1.0 version → concept `20455089` (`StokesNote` `20481592` = same concept; do not double-wire).
- **F-DOI-2** [EBR-Ib] brief `20569724` = record → concept `20569723`.
- **F-DOI-3** [EBR-II] brief `20571232` = v1.2 record → concept `20566465`.
- **F-DOI-4** [FRED] brief `20624814` = version → concept `20624813`.
- **F-DOI-5** [UMB] brief `19885550` = version → concept `19885549`.
- **F-VERB-1** Use `continues` / `isPartOf` / `references` / `isSupplementTo`; never `isContinuationOf` (HTTP 400).
- **F-ANTICIPATORY** EBR-Ib, EBR-II, FRED, and the 3 Marchal papers are **not** in the current V_quad bibliography. They require either the VQUAD-PAPER-CORRECTIONS-001 pass to add the citations **or** operator ratification as pure provenance links. The `continues`/`isPartOf` rows and Sakai-2001/Kovacic are grounded in the paper/index.
- **F-SUPPLEMENT** `isSupplementTo` → VQUAD-REPRO-BUNDLE-002 is a placeholder pending bundle regeneration; fill or drop at deposit.
- **F-ORANTIN** Rejected web-search hallucination `10.1063/1.5135288` (unrelated chemistry paper); correct DOI `10.1063/5.0002260` from arXiv API.

---

## NOT changed
Manuscript content untouched; staging only. No DOI minted, no API called.
