# Zenodo description block — PCF-2 v1.4 (operator-side; amendment-overlay)

**Status**: OPERATOR-PENDING. Phase C + D are TABLED under RULE 1. This file is a runbook template prepared at slot 137 (T2-EXECUTOR-PCF2-V14-M7-V0-AMENDMENT-PREP-137) and amended at slot 161 (T2-EXECUTOR-AMENDMENT-OVERLAY-PCF2-V14-DESCRIPTION-BLOCK-161) to bring the metadata into compliance with the SIARC v1 Zenodo schema locked by slot 160 (`T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160`, bridge `012736f`). When RULE 1 lifts, the operator pastes the description block below into the Zenodo new-version form for the PCF-2 record (concept DOI `10.5281/zenodo.19936297`).

**Per cascade-132 §3.1 unanimous Option α**: PCF-2 v1.4 is deposited FIRST in the M-axis V0 closure series, before umbrella v2.2 and picture-chain v1.20+, so that the PCF-2 v1.4 version DOI is available when the umbrella v2.2 / picture-chain v1.20+ records are deposited (those records cite PCF-2 v1.4 via `IsSupplementTo` related-identifier).

---

## §1 Concept-DOI / version-DOI taxonomy

| Field                            | Value                                                                                                |
|----------------------------------|------------------------------------------------------------------------------------------------------|
| **PCF-2 concept DOI (cite-all)** | **`10.5281/zenodo.19936297`**                                                                         |
| PCF-2 v1.0 version DOI            | (operator records via Zenodo sidebar at deposit time)                                                |
| PCF-2 v1.1 version DOI            | (operator records via Zenodo sidebar at deposit time)                                                |
| PCF-2 v1.2 version DOI            | (operator records via Zenodo sidebar at deposit time)                                                |
| PCF-2 v1.3 version DOI            | `19963298` (per `pcf-research/pcf2/release_v12_2026-05-01/zenodo_notes_v1.2.txt` substrate cross-check; operator paste-verify the bare numeric component against the Zenodo sidebar at deposit time) |
| **PCF-2 v1.4 version DOI**       | **TO_BE_ASSIGNED** (Zenodo issues at form-submit time; record in `zenodo_v14_deposit_log.md`)         |

### Substrate cross-check trail for the concept DOI `19936297`

Verified at slot 137 draft time across 4 substrate sources (per §4.2 of the relay prompt):

1. `pcf-research/pcf2/release_v12_2026-05-01/zenodo_notes_v1.2.txt` — concept DOI cite
2. `claims.jsonl L5` (workspace root) — concept DOI cite
3. `submission_log_patch_item15.txt L36` — concept DOI cite
4. `pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex L1522` — concept DOI cite

All four substrates cite `19936297` as the PCF-2 cite-all/concept DOI. **Recommendation**: operator should still paste-verify the PCF-2 Zenodo sidebar at deposit time per slot 116 J2 three-way mismatch precedent, but the substrate cross-check has resolved the concept-DOI question pre-fire (D-137-5 declassified to INFO).

### PCF-1 vs PCF-2 DOI taxonomy distinction (UF-137-6)

The DOI `10.5281/zenodo.19937196` (cited in slot 116/135 deliverables) is **PCF-1 v1.3 version DOI**, NOT PCF-2's anything.

| Paper | Concept DOI                       | v1.3 version DOI                  |
|-------|-----------------------------------|-----------------------------------|
| PCF-1 | `10.5281/zenodo.19931635`         | `10.5281/zenodo.19937196`         |
| PCF-2 | `10.5281/zenodo.19936297`         | `10.5281/zenodo.19963298`         |

**Forward-pointed governance**: any future cross-link splice that uses `IsSupplementTo` for PCF-1 should use the PCF-1 **concept DOI** `19931635` (Zenodo best practice — concept DOI tracks all versions), not the v1.3 version DOI `19937196`. Slot 135 `zenodo_v22_description_block.md` `IsSupplementTo` row may need a forward-pointed correction to switch from v1.3 version DOI to PCF-1 concept DOI; this is deferred to operator-side cross-link sweep.

---

## §2 Zenodo new-version form fields

### Title
```
PCF-2: A Program Statement for the Cubic Extension of the Δ-Discriminant
Transcendence Predicate (Version 1.4 — j=0 Chowla–Selberg PSLQ-Exhaustion
Amendment)
```

### Authors
- Papanokechi (ORCID: 0009-0000-6192-8273)

### Description (paste into Zenodo description field, MARKDOWN preserved)

```markdown
**PCF-2 v1.4** — minor amendment to v1.3, recording the resolution of one
forward-pointed Open Problem (`op:j-zero-amplitude-h6`, the *j=0* amplitude /
Chowla–Selberg closure) in the soft branch.

**Version changelog (v1.4)**:

> v1.4 (May 2026): Records the resolution of Open Problem `op:j-zero-amplitude-h6`
> (j=0 amplitude / Chowla–Selberg closure) in the soft branch via Prompt 014
> `PASS_A_EQ_6_ONLY` (T25D-RETRY-13PARAM, SIARC bridge SHA `e857172`, 2026-05-02);
> ratified at M7 V0 cascade `T1-SYNTH-M7-V0-CLOSURE-CASCADE-123` (bridge SHA
> `7f93b9e`, 2026-05-09; aggregated MEDIUM-HIGH; annotation
> *(SOFT-BRANCH; HARD-BRANCH-PENDING)*). Hard-branch stretch goal
> |δ| < 10^{-30} forward-pointed under Q22 path-(b). All other v1.3 content
> unchanged.

**Numerical content of the closure (inherited from M7 V0 cascade `7f93b9e`)**:
max |δ_lin| = 3.09 × 10^{-23} across the four j=0 cubic families (Q_30..Q_33,
dps = 25,000, N ≤ 1200, 11-parameter LIN refit at K_FIT = 7); PSLQ on the
17-member deduplicated H6 Chowla–Selberg basis B19+ at maxcoeff = 10^{50},
tolerance = 10^{-40} returns no Γ(1/3) relation in any of the 4 families.

**Q23 PSLQ basis hygiene**: the closure runs in the deduplicated 17-member basis,
NOT the literal 18-basis (which contains the ℚ-redundant pair
{√3, Γ(1/3)Γ(2/3)/(2π)} via Γ-reflection identity).

**Cascade-132 deposit-ordering note**: deposited FIRST in the M-axis V0
closure-series Zenodo session, before umbrella v2.2 and picture-chain v1.20+,
per cascade-132 unanimous Option α (path: PCF-2 v1.4 → umbrella v2.2 →
picture-chain v1.20+).

**Companion documents**:
- PCF-1 v1.3 (concept DOI `10.5281/zenodo.19931635`) — degree-2 progenitor.
- Umbrella v2.2 (forthcoming, deposited second per cascade-132 Option α).
- Picture-chain v1.20+ (forthcoming, deposited third per cascade-132 Option α).

---

**M1–M12 program-axis coverage (snapshot at PCF-2 v1.4 deposit time):**

| Axis | Status | Primary substrate |
|---|---|---|
| M1 | external | D2-NOTE concept `10.5281/zenodo.19996689` |
| M2 | tabled (RULE 1) | — |
| M3 | tabled (RULE 1) | — |
| M4 | closed (V0; folded) | bridge cascade `5f9db69` (cascade 106) |
| M5 | tabled (RULE 1) | — |
| M6.CC | closed (retired into Channel Theory) | Channel Theory concept `10.5281/zenodo.19941678` |
| M7 | closed (V0; folded) | bridge cascade `7f93b9e` (cascade 123) |
| M8a | closed (V0; folded) | bridge cascade `cb429e1` (cascade 127R) |
| M8b | closed (V0; folded) | bridge cascade `74c5630` (cascade 130R; d≥3 caveat in Umbrella v2.3 Appendix C iii) |
| M9 | partial | bridge cascade `b9aa881` (slot 136 picture v1.20+) |
| M10 | partial | Lean sorry discharge work-stream; SAFE phrasing in Umbrella v2.3 Appendix C ii |
| M11 | tabled (RULE 1) | — |
| M12 | tabled (RULE 1) | — |

The axis-coverage table follows the SIARC v1 schema locked by slot 160 verdict (siarc-relay-bridge cascade `012736f`); status vocabulary and atomic listing are normative. Bridge cascade SHAs are content-addressed persistent identifiers; URLs may decay if the `siarc-relay-bridge` repository is renamed but SHAs remain recoverable from any clone.
```

### Keywords (suggested; operator may amend)
- continued fractions
- cubic discriminant
- WKB amplitude
- Chowla–Selberg formula
- Γ(1/3)
- PSLQ
- transcendence predicate
- Galois group cubic
- equianharmonic CM

### Resource type
Publication → Working paper (program statement)

### Related identifiers (paste each row into the Zenodo `Related identifiers` table)

| Relation         | Identifier (DOI)                             | Resource type | Description                                                       |
|------------------|----------------------------------------------|---------------|-------------------------------------------------------------------|
| `IsNewVersionOf` | `10.5281/zenodo.19963298` (PCF-2 v1.3)       | Publication   | This v1.4 amendment supersedes v1.3                               |
| `IsSupplementTo` | `10.5281/zenodo.19931635` (PCF-1 concept)    | Publication   | Cubic extension of the PCF-1 framework (degree-2 progenitor)      |
| `Cites`          | `10.5281/zenodo.19931635` (PCF-1 concept)    | Publication   | PCF-1 v1.3 §5 d=2 split (sole known anomaly to Conjecture B4)     |
| `IsSupplementTo` | `10.5281/zenodo.19885550` (Umbrella concept) | Publication   | PCF-2 v1.4 supplements the SIARC umbrella program (Option α' deposit cascade per slot 157 §Q4b) |
| `Cites`          | `10.5281/zenodo.19885550` (Umbrella concept) | Publication   | Umbrella program-statement carrier (axis-coverage cross-references) |

(Operator: when umbrella v2.2 and picture-chain v1.20+ are deposited, their PCF-2-v1.4 cross-link rows go onto **their** records, not this one. PCF-2 v1.4's record only points back to the PCF-1 concept DOI and to the PCF-2 v1.3 prior version.)

**Schema authority**: the related-identifiers row pattern (5 rows; paired `IsSupplementTo` + `Cites` for each cross-link target) and the M1–M12 axis-coverage table format follow the SIARC v1 Zenodo metadata schema locked by slot 160 verdict (`T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160`, bridge SHA `012736f`, 2026-05-10). Concept-DOI vs version-DOI discipline: cross-links target concept-DOIs; `IsNewVersionOf` is the documented exception (version-to-version relation; targets v1.3 version-DOI `19963298`).

### Communities
(Operator selects the same community/communities used for v1.3.)

### License
(Operator selects the same license used for v1.3 — typically CC-BY-4.0 or equivalent.)

### Files to upload

1. `pcf2_program_statement_v14.pdf` (636,049 B; 23 pages; SHA-256 prefix `471DC7C7EBF8BD4F`)
2. `pcf2_program_statement_v14.tex` (80,244 B; SHA-256 prefix `0CF4E7DC90C1AC2A`) — source bundle (with the 4 `\input{}` dependencies flattened into the upload bundle, OR with the deposit-time arxiv-pack flatten procedure applied as in v1.3 deposit; see `b5_pdflatex_compile_log.md` § "Operator-side runbook prerequisites").
3. `b_amendment_v14.diff` (10,486 B; SHA-256 prefix `30371C2EBD9885B1`) — diff vs v1.3 baseline.

---

## §3 Post-deposit operator actions

1. Capture the assigned v1.4 version DOI from the Zenodo confirmation page.
2. Fill `zenodo_v14_deposit_log.md` (sibling file in this session folder; OPERATOR-PENDING template).
3. Splice the v1.4 entry into `tex/submitted/submission_log.txt` per `submission_log_v14_splice.diff` (sibling template; chronological order: v1.4 splice goes BEFORE umbrella v2.2 splice, per Option α).
4. Update cross-link metadata per `cross_link_update_log.md` (sibling template).
5. Proceed to umbrella v2.2 deposit (slot 135 substrate at `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135/`); splice the freshly assigned PCF-2 v1.4 version DOI into umbrella v2.2's `IsSupplementTo` row at deposit time.
