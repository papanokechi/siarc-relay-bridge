# slot_sha_verification.md — STEP 2

**Generated:** 2026-05-06 (Wed, W19)
**Source of truth:**
- Expected SHAs:
  `tex/submitted/control center/literature/g3b_2026-05-03/SHA256SUMS.txt`
  (SHA-256 = `0518E111CFD408A3A04015FCE3D8278AF06226D0B7BD527361701FE5C8A0A190`,
  16 SHA-line entries; ≥11 required by P2)
- Spec citations:
  `siarc-relay-bridge/sessions/2026-05-04/CC-VQUAD-PIII-NORMALIZATION-MAP-PROMPT-SPEC/prompt_spec.md`
  §1 (SHA-256 = `BE3F8FE9D0857E2916452A8E5E6102B73F195B0E177457A077372CB6EF6E3319`)
- Verification method: PowerShell `Get-FileHash -Algorithm SHA256` on
  every entry in SHA256SUMS.txt; raw JSON in `sha_verification_raw.json`.

---

## §A — CC-VQUAD-PIII spec §1 PRIMARY anchors

| slot | filename | spec prefix | SHA256SUMS prefix | live prefix | result |
|------|----------|-------------|-------------------|-------------|--------|
| 01 | 01_birkhoff_1930_acta54.pdf | aeb5291e | aeb5291e | aeb5291e | PASS |
| 03 | 03_birkhoff_trjitzinsky_1933_acta60.pdf | dcd7e3c6 | dcd7e3c6 | dcd7e3c6 | PASS |
| 04 | 04_wasow_1965_dover.pdf | f59d6835 | f59d6835 | f59d6835 | PASS |
| 06 | 06_costin_2008_chap5.pdf | 436c6c11 | 436c6c11 | 436c6c11 | PASS |
| 07 | 07_okamoto_1987_painleve_III_FE30.pdf | 65294fbc | 65294fbc | 65294fbc | PASS |
| 08 | 08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf | 96c49cdd | 96c49cdd | 96c49cdd | PASS |

§A aggregate: **6/6 PASS** (all CC-VQUAD spec §1 PRIMARY anchors verified;
spec citation prefixes ↔ SHA256SUMS expected ↔ live disk content all
agree).

---

## §B — Auxiliary slots (cited by name in spec body, not in §1)

These slots are not listed in spec §1 ANCHOR FILES but are present in
the literature folder + SHA256SUMS.txt; the spec body cites Sakai by
name multiple times (L324, L345, L353-355, L611, L629, L945, L986,
L1026 of prompt_spec.md). Verified for completeness so 058 may cite
them if Phase B/C builds out the W cross-walk reading.

| slot | filename | SHA256SUMS prefix | live prefix | result |
|------|----------|-------------------|-------------|--------|
| 13 | 13_sakai_1999_preprint_kyoto99_10.pdf | ec1bbda3 | ec1bbda3 | PASS |
| 14 | 14_kajiwara_noumi_yamada_2017_geometric_aspects.pdf | 7cd88461 | 7cd88461 | PASS |
| 15 | 15_noumi_yamada_1998_affine_weyl_dynamical.pdf | 32424fe6 | 32424fe6 | PASS |
| 16 | 16_noumi_yamada_2000_birational_weyl_nilpotent.pdf | 75698afb | 75698afb | PASS |

§B aggregate: **4/4 PASS**.

---

## §C — Aliased filenames (byte-exact copies; SHA256SUMS lists both)

These entries are documented in SHA256SUMS.txt as Copy-Item byte-exact
aliases of the runbook-named originals; their hashes match by construction.

| filename | aliased to | SHA256SUMS prefix | live prefix | result |
|----------|-----------|-------------------|-------------|--------|
| birkhoff_1930.pdf | 01_birkhoff_1930_acta54.pdf | aeb5291e | aeb5291e | PASS |
| birkhoff_trjitzinsky_1933.pdf | 03_birkhoff_trjitzinsky_1933_acta60.pdf | dcd7e3c6 | dcd7e3c6 | PASS |
| wasow_1965_chap_X.pdf | 04_wasow_1965_dover.pdf | f59d6835 | f59d6835 | PASS |
| costin_2008_chap5.pdf | 06_costin_2008_chap5.pdf | 436c6c11 | 436c6c11 | PASS |

§C aggregate: **4/4 PASS**.

---

## §D — Supplementary / non-anchor (informational, not used by 058)

| filename | SHA256SUMS prefix | live prefix | result |
|----------|-------------------|-------------|--------|
| supplementary/okamoto_1987_part_I_painleve_VI_AnnMat.pdf | 0982c60e | 0982c60e | PASS |

This file is the *wrong* Okamoto paper (Part I / P_VI, not Part IV / P_III)
surfaced during the R5-OKAMOTO-PROJECT-EUCLID-RETRY anomaly and relocated
to `supplementary/`; its SHA is in SHA256SUMS.txt for provenance only and
it is **NOT** an anchor for CC-VQUAD-PIII. Slot 07 (P_III FE 30) was later
acquired separately by R5-OKAMOTO-NUMDAM-RETRY (Kobe-U direct PDF).

---

## §E — Bridge-path entry (not in workspace literature folder)

| filename | SHA256SUMS prefix | live prefix | result |
|----------|-------------------|-------------|--------|
| siarc-relay-bridge/.../substitute_FW_2005_PIIIp_boundary.pdf | 80e05009 | 80e05009 | PASS |

Bridge-resident substitute artefact from 031 WITTE-FORRESTER-2010-
ACQUISITION SCENARIO_C analogue; preserved for provenance only;
**NOT** a CC-VQUAD-PIII anchor.

---

## Aggregate

| group | PASS | FAIL | notes |
|-------|------|------|-------|
| §A spec §1 PRIMARY anchors | 6 | 0 | all CC-VQUAD anchors verified |
| §B auxiliary slots | 4 | 0 | Sakai 1999, KNY 2017, NY 1998/2000 |
| §C aliased filenames | 4 | 0 | byte-exact copies |
| §D supplementary | 1 | 0 | Part-I/P_VI wrong-target file |
| §E bridge-path | 1 | 0 | 031 substitute |
| **TOTAL** | **16** | **0** | **PASS 16/16** |

**Result:** No SHA drift detected. All 16 SHA256SUMS.txt entries hash-
match the live disk content as of 2026-05-06. Spec §1 SHA-prefix
citations agree with both SHA256SUMS expected and live disk content
for every PRIMARY anchor (6/6).

**No HALT_057_SHA_DRIFT condition.**
