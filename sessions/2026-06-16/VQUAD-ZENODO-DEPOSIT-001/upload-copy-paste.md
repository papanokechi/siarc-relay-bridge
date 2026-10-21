# Copy-paste sheet — V_quad period-rep Zenodo deposit (web UI)

Frictionless paste source for <https://zenodo.org/uploads/new>. Values are byte-identical
to `MANUAL-UPLOAD.md` §1–§3 (run-3 pins, anchor `4a75234f…`). This is a convenience
artifact — `MANUAL-UPLOAD.md` remains the authoritative sheet. One record, two files
(Scenario B). Publishing is the operator's irreversible step.

## Files (upload both into one record; set the PDF as default preview)

File 1 (PDF, preview):
C:\LocalWork\siarc-relay-bridge\sessions\2026-06-16\VQUAD-REPRO-BUNDLE-002\run-2\vquad-periodrep-bundle\paper\vquad-periodrep-paper.pdf
  size 773171 B · 24 pp
  SHA-256 33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea
  MD5     99faea5b0f4095788e4ee932436beeda   <- Zenodo shows MD5 after upload; match this

File 2 (bundle zip):
C:\LocalWork\siarc-relay-bridge\sessions\2026-06-16\VQUAD-REPRO-BUNDLE-002\run-2\vquad-periodrep-bundle.zip
  size 776968 B
  SHA-256 7bc5d00885bd823a758c4476f60e950a88f54e9f42b7a4bf254730ac894de013
  MD5     c1b5a39c0b56576e81b5c5723935669f   <- match this

Trap-7: re-hash the staged PDF == 33f339ed… IMMEDIATELY before upload (OneDrive-drift backstop).

## Core fields

Resource type: Publication -> Preprint
Title:         An explicit exponential-period representation of the V_quad connection coefficient
Creator:       Family = Papanokechi   (mononym — leave Given name blank)
               ORCID = 0009-0000-6192-8273
               Affiliation = Independent Researcher, Yokohama, Japan
Publication date: the actual publish date (do NOT backdate)
Version:       1.0.0
Language:      eng (English)
License:       Creative Commons Attribution 4.0 International (CC-BY-4.0)
Access:        Open Access
DOI:           leave "Zenodo will register a DOI" (do NOT enter an external DOI)

## Description / Abstract  (paste verbatim into Description)

We prove that the connection coefficient C of the V_quad polynomial continued fraction—the rank-one standalone closure on the Sakai surface D₅⁽¹⁾ (Painlevé V)—admits an explicit exponential-period representation C=(|Γ(β)|/2π)∫_γ e^ξ B̂(ξ) dξ=|Γ(β)| K, where B̂ is the Borel transform of the V_quad asymptotic series, holonomic of order 4 (the Borel–Laplace dual of the order-2 operator annihilating the series) with coefficients in the real quadratic field ℚ(√3); γ is an explicit Hankel rapid-decay cycle on (−∞,−2/√3]; and β=−1/(3√3). The identity is verified by three structurally independent methods—differential-equation/operator duality, Borel–Laplace contour deformation, and Stokes-data—agreeing to 46 digits. The order-2 operator annihilating the asymptotic series has differential Galois group SL₂(ℂ) by Kovacic's algorithm. As a by-product, holonomicity of the Borel transform forces a finite resurgent structure. Finally, conditional on the Fresán–Jossen period conjecture for exponential motives and on a stated motivic-comparison hypothesis, C is transcendental over ℚ̄. This record accompanies the VQUAD-PERIODREP reproducibility bundle (verification scripts, certificates, and a byte-reproducible build), which reproduces every numerical claim above, including the 46-digit agreement. The work was produced under the SIARC governance methodology; per-stage provenance and AEAL-level claim ledgers are linked from the bundle's SIARC_PROVENANCE.md. The identity continues the V_quad companion paper (concept DOI 10.5281/zenodo.20455089) within the Sakai Stratification of PCF Transcendence program.

(Optional: for a pure-Abstract description, trim from "This record accompanies…" onward.
 Zenodo renders HTML; Greek/sub-superscripts/dashes may entity-encode on the published
 record — expected, verify with the normalized compare, Trap 3.)

## Keywords  (add 8 — press Enter after EACH; no comma/bulk paste)

polynomial continued fractions
exponential periods
Painlevé V
Fresán-Jossen exponential motives
Borel-Laplace duality
conditional transcendence
Sakai stratification
motivic Galois group

## MSC 2020  (optional — "Keywords and subjects", or skip)

34M55 (primary)
11J81
34E20
14F40
33C20
37K10

## Related works  (add 11 — Relation + Identifier; scheme auto-detects DOI)

Per-work "Resource type" field describes the CITED work, not this deposit:
  rows 1–6 (Zenodo records) = Publication / Preprint   (verified: resource_type=publication/preprint)
  rows 7–11 (publisher DOIs) = Publication / Journal article  (verified: Crossref type=journal-article)

  Relation     Identifier                     Resource type                  what it is
  Continues    10.5281/zenodo.20455089        Publication / Preprint         V_quad companion paper (concept)
  Continues    10.5281/zenodo.20694840        Publication / Preprint         Sakai-Stratification program (concept)
  Is part of   10.5281/zenodo.19885549        Publication / Preprint         SIARC umbrella program (concept)
  References   10.5281/zenodo.20569723        Publication / Preprint         EBR-Ib (concept)
  References   10.5281/zenodo.20566465        Publication / Preprint         EBR-II (concept)
  References   10.5281/zenodo.20624813        Publication / Preprint         δ-Fredholm (concept)
  References   10.1007/s002200100446          Publication / Journal article  Sakai 2001, Comm. Math. Phys.
  References   10.1016/S0747-7171(86)80010-4  Publication / Journal article  Kovacic 1986, J. Symbolic Comput.
  References   10.1007/s00220-024-05187-0     Publication / Journal article  Marchal–Alameddine 2024, CMP
  References   10.1016/j.geomphys.2017.10.009 Publication / Journal article  Iwaki–Marchal 2018, J. Geom. Phys.
  References   10.1063/5.0002260              Publication / Journal article  Marchal–Orantin 2020, J. Math. Phys.

All concept DOIs. Do NOT enter the retracted V_quad v1.0 VERSION DOI 10.5281/zenodo.20455090
— use the concept …20455089 (#1).

## Before Publish (checklist)

[ ] both files present; PDF is default preview; file MD5s match §Files
[ ] author Papanokechi + ORCID + affiliation correct
[ ] 11 related works, correct relations; NO …20455090
[ ] License CC-BY-4.0; Open Access; Version 1.0.0; Language eng
[ ] no target-venue string (e.g. "Compositio") anywhere (PDF already clean)
[ ] Save draft -> review render -> Publish (irreversible; mints concept + version DOI)
[ ] then: §B ledger append, update DEPOSIT_LOG_INDEX.md, send O. Marchal the concept DOI,
    open VQUAD-COMPOSITIO-PRECLEAR-001 (see handoff.md)
