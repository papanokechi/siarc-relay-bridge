# Zenodo Deposit Confirmation — bt_baseline_note v1.0

**Date:** 2026-05-06
**Operator:** papanokechi (Mauricio Echizen Kubo, ORCID 0009-0000-6192-8273)
**Status:** PUBLISHED (Version 1.0 current; first and only version)

---

## DOI assignments

| Type | DOI | Resolves to |
|---|---|---|
| **Concept (cite-all)** | `10.5281/zenodo.20048196` | latest version (currently v1.0) |
| **Version (v1.0)** | `10.5281/zenodo.20048197` | this specific deposit (frozen) |

**Record URL:** https://zenodo.org/records/20048197

Per Zenodo "cite all versions" convention: the concept DOI 20048196 is FRESH (no prior version of this artefact existed on Zenodo). The version DOI 20048197 is permanent and immutable. Future v1.1 / v2.0 etc. will mint new version DOIs under the same concept DOI 20048196.

---

## Local artefact provenance

| Artefact | SHA-256 | Bytes | Notes |
|---|---|---|---|
| `bt_baseline_note.pdf` | `23022f0de77ac8388ed584b2196c0ab995cd8cf18b2dd71efbc0488a0f6e5b7c` | 409 337 | 8 pp, primary upload artefact |
| `bt_baseline_note.tex` | `6746692c517dc25238473e819527c5682465cdc9e1def69d1f6df31c1014d51b` | 38 023 | LaTeX source (~720 lines) |
| `annotated_bibliography.bib` | `589f6e4a0b29de401229d60a6252de15436f355a2fa8b3ac04907779c2de923d` | 14 816 | 15 entries, scoped subset of `bibliography_pass1.bib` |
| `rubber_duck_critique.md` | `97765d9b5c303cf5b13c5a9e4e67323dc47c9e5256b2be4301d0d458fe11bfa3` | 14 603 | pre-commit self-review |
| `claims.jsonl` | (post-A11 SHA `24469D12…2AA926`) | 7 977 | AEAL provenance, 11 entries (A1..A11) |

---

## Form metadata recorded (Zenodo deposit form)

- **Resource type:** Publication / Working paper
- **Title:** A Newton-polygon formal-level baseline for the Birkhoff-Trjitzinsky exponent on the SIARC polynomial continued-fraction Wallis stratum
- **Author:** Mauricio Echizen Kubo (papanokechi) — ORCID `0009-0000-6192-8273`, Independent researcher, Yokohama, Japan
- **Description source:** `zenodo_description_bt_baseline_note.txt` (128 lines / 6154 B)
- **License:** CC-BY 4.0
- **Communities:** `siarc`
- **Keywords (8):** Newton polygon · Birkhoff-Trjitzinsky · formal asymptotic exponent · polynomial continued fractions · SIARC · Wallis stratum · Wimp-Zeilberger ansatz · difference equations
- **Version:** 1.0
- **Funding:** (blank — unfunded independent research)

### Related identifiers (8 entries)

| # | Relation | Identifier | Scheme | Resource type |
|---|---|---|---|---|
| 1 | isPartOf | `10.5281/zenodo.19937196` (PCF-1 v1.3) | DOI | Publication / Working paper |
| 2 | isPartOf | `10.5281/zenodo.19963298` (PCF-2 v1.3) | DOI | Publication / Working paper |
| 3 | isContinuationOf | `10.5281/zenodo.20015923` (D2-NOTE v2.1) | DOI | Publication / Working paper |
| 4 | isCitedBy | `10.5281/zenodo.19899996` (CT v1.3) | DOI | Publication / Working paper |
| 5 | isCitedBy | `10.5281/zenodo.19915689` (T2B v3) | DOI | Publication / Working paper |
| 6 | isPartOf | `10.5281/zenodo.19965041` (SIARC umbrella v2.0) | DOI | Publication / Working paper |
| 7 | references | `10.1007/BF02398269` (Birkhoff-Trjitzinsky 1933, Acta Math 60) | DOI | Publication / Journal article |
| 8 | isSupplementTo | `https://github.com/papanokechi/siarc-relay-bridge/tree/37c939f/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER` | URL | Software |

---

## Post-publish operator follow-ups (recommended, deferred)

### Tier 1 (immediate, T2-batch)

- [x] Append claim `T1P2B-A11` to `claims.jsonl` (deposit-confirmation entry; this session) → **DONE**
- [x] Splice Item 21 into `tex/submitted/submission_log.txt` (mirror Item 17/18/19/20 pattern; 6th May 2026 entry) → **DONE**
- [x] Add this `zenodo_deposit_confirmation.md` (additive deposit-confirmation file in same folder; preserves handoff.md as deposit-time snapshot per AEAL convention) → **DONE**

### Tier 2 (operator-side, deferred)

- [ ] **Byte-clean readback verification.** Download https://zenodo.org/records/20048197/files/bt_baseline_note.pdf?download=1 and verify SHA-256 matches `23022f0de77ac8388ed584b2196c0ab995cd8cf18b2dd71efbc0488a0f6e5b7c`. Mirrors D2-NOTE v2.0 claim 64 pattern; non-blocking if deferred but provides the canonical byte-identity audit.
- [ ] **Optional Zenodo metadata polish.** Edit PCF-1 v1.3 / PCF-2 v1.3 / CT v1.3 / SIARC umbrella v2.0 / D2-NOTE v2.1 records to add `IsCitedBy: 10.5281/zenodo.20048196` (mirrors prior cycle convention; deferred, consistent with the v2.1-cycle posture).

### Tier 3 (downstream)

- [ ] **Picture v1.20 deposit** absorbing the v1.0 publication event alongside open Q1/Q4 gap-closure trajectory + 058R verdict UPGRADE_V1_0_PARTIAL_NUMERICAL.
- [ ] **`@misc{papanokechi_bt_baseline_v1, ...}` bibtex stub** added to umbrella v2.x bibliography pool when umbrella v2.1 dispatch lands. Suggested entry:

```bibtex
@misc{papanokechi_bt_baseline_v1,
  author       = {Echizen Kubo, Mauricio},
  title        = {A {Newton}-polygon formal-level baseline for the
                  {Birkhoff}-{Trjitzinsky} exponent on the {SIARC}
                  polynomial continued-fraction {Wallis} stratum},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.20048196},
  url          = {https://doi.org/10.5281/zenodo.20048196},
  note         = {Concept DOI; resolves to latest version}
}
```

(Concept DOI `10.5281/zenodo.20048196` chosen for `cite-all` resolution; downstream consumers can swap to the version DOI `10.5281/zenodo.20048197` for permanent v1.0 citation if version-pinning is desired.)

### Tier 4 (gated, deferred under existing endorsement-chain status quo)

- [ ] **arXiv mirror for bt_baseline_note v1.0** (math.CA primary classification; gated on existing endorsement-chain status quo). Not part of W19/W20 scope.

---

## Open questions (carried forward, NOT closed by deposit)

The deposit publishes the **formal-level baseline** only. Two gaps remain explicitly open:

- **Q1 (the d ≥ 3 gap, A_naive < 2d).** Proposition 1.2 frames the gap with two non-mutually-exclusive structural mechanisms — (i') borderline-locus condition `deg a = 2 deg b` on a sub-stratum, (ii') alternative definition of `A_fit` in the [PCF-2 v1.3] fit-protocol — but does NOT close it. T1 Phase 3 territory.
- **Q4 (the formal-to-analytic sectorial upgrade gap).** Birkhoff-Trjitzinsky 1933 §§7–9 produces formal series; the connection to the analytic (true) asymptotic exponent on the SIARC stratum requires a sectorial summability theorem. Candidate: Wasow §X.3 Theorem 11.1 / Adams 1928 / Turrittin 1955 / Immink 1984 / Costin 2008. None has been verified to apply to the SIARC stratum. T1 Phase 3 / Phase 4 territory.

**Conjecture B4** ([PCF-2 v1.3] R1.1+R1.3+Q1; A = 2d for representatives in the SIARC stratum at each d ≥ 2) is explicitly NOT claimed to be proven, partially proven, or refuted by this deposit. Triple-framing PROVEN | VERIFIED | STRUCTURAL FRAMING | CONJECTURED is intact in every section of the deposited PDF.

---

## AEAL bridge anchor

- **Substrate session:** `sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/` (commit `37c939fe8990a814eefec0d227b493499608bd31`, 2026-05-04)
- **Note draft session:** `sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/` (this folder)
- **Claims chain:** A1..A6 carry-forward from substrate session + A7..A8 PCF-1/PCF-2 literature anchors + A9 build claim + A10 rubber-duck self-review + **A11 deposit confirmation (this entry)**
- **Total AEAL claims:** 11

This file is an additive deposit-time-snapshot per AEAL convention (handoff.md preserved bit-identical; new files added in same folder when post-deposit events occur).
