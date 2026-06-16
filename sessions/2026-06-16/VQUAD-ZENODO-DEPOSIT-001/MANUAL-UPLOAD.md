# Manual Zenodo upload sheet — V_quad period-representation paper

Copy-paste source for a **manual web-UI deposit** at <https://zenodo.org/uploads/new>.
All values are the authoritative run-2 deposit pins (from
`VQUAD-ZENODO-READY-001/run-2/zenodo_metadata.md` + `related_identifiers.md`), **not
memory**. One record, two files (Scenario B). Publishing is your irreversible step.

---

## 1. Files to upload (2 — same record)

| order | file | path | size | SHA-256 | MD5 (Zenodo shows this after upload) |
|---|---|---|---|---|---|
| 1 (default preview) | **vquad-periodrep-paper.pdf** | `C:\LocalWork\siarc-relay-bridge\sessions\2026-06-16\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle\paper\vquad-periodrep-paper.pdf` | 714,771 B (24 pp) | `4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe` | `028a1a5d9e10a3a9487596f6db3e6a38` |
| 2 | **vquad-periodrep-bundle.zip** | `C:\LocalWork\siarc-relay-bridge\sessions\2026-06-16\VQUAD-REPRO-BUNDLE-002\vquad-periodrep-bundle.zip` | 721,715 B | `8752d7c71d074564f112d769932ed83e2ffb8518c49c6683dfa210fd952892eb` | `9d811494d77f4ffa84127ef4d105584a` |

After each upload Zenodo lists the file's MD5 — confirm it matches the MD5 column
above (MD5↔MD5). Set the **PDF** as the default preview.

---

## 2. Core metadata (web-UI fields)

| Zenodo field | Value |
|---|---|
| **Resource type** | Publication → **Preprint** |
| **Title** | `An explicit exponential-period representation of the V_quad connection coefficient` |
| **Creators** | Family name `Papanokechi` (single mononym — leave Given blank); **ORCID** `0009-0000-6192-8273`; **Affiliation** `Independent Researcher, Yokohama, Japan` |
| **Publication date** | the actual publish date (do **not** backdate) |
| **Version** | `1.0.0` |
| **Language** | English (`eng`) |
| **License** | Creative Commons Attribution 4.0 International (**CC-BY-4.0**) |
| **Access** | Open Access |
| **DOI** | leave "Zenodo will register a DOI" — do **not** enter an external DOI |
| **Publisher** | Zenodo (default) |

### Description / Abstract (paste verbatim)

```text
We prove that the connection coefficient C of the V_quad polynomial continued fraction—the rank-one standalone closure on the Sakai surface D₅⁽¹⁾ (Painlevé V)—admits an explicit exponential-period representation C=(|Γ(β)|/2π)∫_γ e^ξ B̂(ξ) dξ=|Γ(β)| K, where B̂ is the Borel transform of the V_quad asymptotic series, holonomic of order 4 (the Borel–Laplace dual of the order-2 operator annihilating the series) with coefficients in the real quadratic field ℚ(√3); γ is an explicit Hankel rapid-decay cycle on (−∞,−2/√3]; and β=−1/(3√3). The identity is verified by three structurally independent methods—differential-equation/operator duality, Borel–Laplace contour deformation, and Stokes-data—agreeing to 46 digits. The order-2 operator annihilating the asymptotic series has differential Galois group SL₂(ℂ) by Kovacic's algorithm. As a by-product, holonomicity of the Borel transform forces a finite resurgent structure. Finally, conditional on the Fresán–Jossen period conjecture for exponential motives and on a stated motivic-comparison hypothesis, C is transcendental over ℚ̄. This record accompanies the VQUAD-PERIODREP reproducibility bundle (verification scripts, certificates, and a byte-reproducible build), which reproduces every numerical claim above, including the 46-digit agreement. The work was produced under the SIARC governance methodology; per-stage provenance and AEAL-level claim ledgers are linked from the bundle's SIARC_PROVENANCE.md. The identity continues the V_quad companion paper (concept DOI 10.5281/zenodo.20455089) within the Sakai Stratification of PCF Transcendence program.
```

> The first sentence onward (through "…forces a finite resurgent structure" and the
> transcendence sentence) is the **manuscript Abstract verbatim**; the last three
> sentences are a bundle/SIARC addendum. If you prefer a pure-Abstract description,
> trim from "This record accompanies…" onward — optional, your call.
> Zenodo renders this as HTML; on the published record Greek/sub-superscripts/dashes
> may entity-encode — that is expected (verify with the normalized compare, Trap 3).

### Keywords (add 8 — press **Enter after each**; no comma/bulk paste)

```
polynomial continued fractions
exponential periods
Painlevé V
Fresán-Jossen exponential motives
Borel-Laplace duality
conditional transcendence
Sakai stratification
motivic Galois group
```

### MSC 2020 (optional — add in "Keywords and subjects", or skip)

`34M55` (primary) · `11J81` · `34E20` · `14F40` · `33C20` · `37K10`

---

## 3. Related works (add 11 — Relation + Identifier; scheme auto-detects DOI)

| # | Relation (dropdown) | Identifier (DOI) | what it is |
|---|---|---|---|
| 1 | **Continues** | `10.5281/zenodo.20455089` | V_quad companion paper (concept) |
| 2 | **Continues** | `10.5281/zenodo.20694840` | Sakai-Stratification program (concept) |
| 3 | **Is part of** | `10.5281/zenodo.19885549` | SIARC umbrella program (concept) |
| 4 | **References** | `10.5281/zenodo.20569723` | EBR-Ib (concept) |
| 5 | **References** | `10.5281/zenodo.20566465` | EBR-II (concept) |
| 6 | **References** | `10.5281/zenodo.20624813` | δ-Fredholm (concept) |
| 7 | **References** | `10.1007/s002200100446` | Sakai 2001, Comm. Math. Phys. |
| 8 | **References** | `10.1016/S0747-7171(86)80010-4` | Kovacic 1986, J. Symbolic Comput. |
| 9 | **References** | `10.1007/s00220-024-05187-0` | Marchal–Alameddine 2024, CMP |
| 10 | **References** | `10.1016/j.geomphys.2017.10.009` | Iwaki–Marchal–Sałek/Saenz 2018, J. Geom. Phys. |
| 11 | **References** | `10.1063/5.0002260` | Marchal–Orantin 2020, J. Math. Phys. |

**All concept DOIs** (cite-all parents). Do **not** enter the retracted V_quad v1.0
**version** DOI `10.5281/zenodo.20455090` — use the concept `…20455089` (#1).

---

## 4. Repository URL — optional

The corpus convention links **Zenodo concept DOIs**, and the reproducibility **code
ships in this record as `vquad-periodrep-bundle.zip`** — so a separate repo URL is
**not required**.

If you nonetheless want to link the source repo, add it as a related work:
- **Relation** `Is supplemented by` · **Identifier** `https://github.com/papanokechi/project-fingerprint` · **Resource type** `Software`.
- ⚠️ Only add this if that repo is **public**. If it is private, leave it off (a
  403/404 link degrades the record). The git remote is
  `https://github.com/papanokechi/project-fingerprint.git` — confirm its visibility
  before linking.

---

## 5. Before you click Publish

- Both files present; PDF is default preview; file MD5s match §1.
- Author `Papanokechi` + ORCID + affiliation correct.
- 11 related works, correct relations; **no** `…20455090`.
- License CC-BY-4.0; Open Access; Version 1.0.0; Language English.
- No target-venue string (e.g. "Compositio") anywhere — the PDF is already clean.
- **Save draft → review render → Publish.** Publish is irreversible (mints concept +
  version DOI). Then: append the §B ledger entry, update `DEPOSIT_LOG_INDEX.md`, send
  O. Marchal the concept DOI, and open `VQUAD-COMPOSITIO-PRECLEAR-001` (see
  `handoff.md`).
