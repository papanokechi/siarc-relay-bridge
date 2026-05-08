# Phase D — Verdict synthesis and demotion decision

## §1 Inputs (verbatim Phase A + Phase B verdicts)

- **Phase A:** `A_VERDICT_FUNCTION_IS_IDENTITY_ON_CITED`
  - Audit anchors: `lax_pair_solver.py` L358-L404 function body; L385-L388 four extraction lines all RHS = corresponding `_CITED` module-constants; L401-L402 parameter use only via `.keys()` enumeration (no value-side use); L381-L386 author-acknowledged inline comment "The structural inversion is the IDENTITY on the relabel".
- **Phase B:** `B_VERDICT_S_HARDCODED_STRING_LITERAL_DIAGNOSTIC_SCRIPT`
  - Audit anchors: `jimbo_final.py` L26 `S_num = mpf("0.43770528073458")` string-literal `mpf()` constructor; no upstream computation in the file; no project-internal `from X import S_num`; L329 `"S_precision_digits": 8` companion metadata; L172-L211 `Dingle` references discuss normalisations only, NOT digit provenance; top-level `__main__` is PSLQ + closed-form-search DIAGNOSTIC, emits `"match": false`.
- **Phase C:** `C_PHASE_SKIPPED_PER_PHASE_A_VERDICT` (spec STEP A.7 + STEP C disposition: skip when Phase A is IDENTITY_ON_CITED).

---

## §2 Truth-table mapping (per VERDICT BINS table in prompt 111)

| Phase A | Phase B | Final verdict |
|---|---|---|
| **IDENTITY_ON_CITED** | **HARDCODED_LITERAL + DIAGNOSTIC** | **TAUTOLOGY_CONFIRMED_VERDICT_DEMOTED** |
| IDENTITY_ON_CITED | COMPUTED_FROM_PIPELINE | TAUTOLOGY_CONFIRMED_BUT_S_HAS_INDEPENDENT_PROVENANCE |
| IDENTITY_ON_CITED | IMPORTED_FROM_OTHER_FILE | TAUTOLOGY_CONFIRMED_S_PROVENANCE_OPAQUE |
| DERIVES_FROM_PARAMETERS | (any) | TAUTOLOGY_REFUTED_VERDICT_RETAINED |
| MIXED_DERIVATION | (any) | AUDIT_INCONCLUSIVE_PHASE_C_SHOULD_HAVE_RUN |

Inputs match **row 1** (top row, bolded). Final verdict bin lands at the strongest demotion outcome.

---

## §3 Verdict ladder placement

**`TAUTOLOGY_CONFIRMED_VERDICT_DEMOTED`**

Both arms of the audit return the strongest classification supporting demotion:
- The `jm_ueno_inversion_via_fw` function returns its inputs ignored, on the `_CITED` constants directly.
- The `jimbo_final.py` source for the cited 14-digit `S = 0.43770528073458` is itself a hardcoded string literal in a DIAGNOSTIC script that does not produce these digits — the script consumes them as INPUT for PSLQ attribution attempts (which return `"match": false`).

The 110-EXEC `GO_ROUTE_D_PARTIAL_VIA_FW` verdict, in light of this audit, carries:
- ZERO independent numerical content from the `jm_ueno_inversion_via_fw` side (the four extracted coordinates are tautologically equal to the cited tuple, by construction at the source level).
- ZERO independent numerical content recoverable via cross-check against `jimbo_final.py:S_num`, because that anchor is itself a hardcoded literal whose upstream provenance is not documented in the file.

The 110-EXEC handoff §J6 + UF-110-4 already self-disclose the structural-relabel tautology at the inversion-function level. This Phase D verdict adds:
1. Independent confirmation by static-code audit.
2. Extension of the tautology classification one level upstream — to the `S_num` anchor itself.

---

## §4 069r3 FINAL synthesis implication

In any future 069r3 FINAL synthesis turn (anticipated at session ~125-127 per the 109-EXEC handoff §"Cascade implication"), the 110-EXEC `GO_ROUTE_D_PARTIAL_VIA_FW` verdict is treated as carrying **ZERO probative weight in cross-checking Route B's `NO_GO_OFF_DEGENERATION`**.

Specifically:
- **Route B (109-EXEC)** is symbolic and reaches `NO_GO_OFF_DEGENERATION` via three independent obstructions ((i) FW (2.2) PV null-sum residual `-1/3 != 0`; (ii) Okamoto S1 standing-assumption boundary `eta_0 = 0`; (iii) FW (4.1) PIII' Hamiltonian hardcodes WLOG `eta_inf = eta_0 = 1`). These obstructions are derivation-grounded and remain probative.
- **Route D (110-EXEC)** under the D.1.b FW substitute path returns the cited tuple by relabel construction. Per this Phase D verdict, the per-coord EXACT agreement at all 4 coords is a TAUTOLOGY of the implementation, NOT an independent measurement.
- **Cross-check synthesis:** comparing 109-EXEC NO_GO against 110-EXEC GO is VACUOUS at the inversion-function level because the GO is structural-relabel-by-construction. The two verdicts are NOT in genuine tension; the apparent disagreement dissolves once the tautology is recognised.

Recommended 069r3 FINAL synthesis treatment:
- Cite Route B (109-EXEC) `NO_GO_OFF_DEGENERATION` as the operative cascade signal.
- Note Route D (110-EXEC) tautology with reference to this audit (sessions/2026-05-08/T2-OPERATOR-110-EXTRACTION-TAUTOLOGY-STATIC-AUDIT-122).
- Forward-point any independent Stokes-data cross-check to the cascade-stub outlined in Phase E.

---

## §5 Independent-Stokes-data residual

Per the `lax_pair_solver.py:380-386` author-acknowledged inline comment:

> The structural inversion is the IDENTITY on the relabel; the genuine
> numerical content lives in the agreement of independent Stokes data
> (S, M_11, M_21, ξ_0, β_exp) with cited values.

This audit does **NOT** address that residual. The genuine numerical content of any Route D path lives in:
- (a) Independent computation of the WKB-channel Stokes anchor `S` from the V_quad ODE at higher than 0-digit agreement (110-EXEC Phase B.3 generic Dingle reimplementation gave `S ≈ 2.89e-5` vs cited `0.43770528073458`, recorded as 110 anomaly D-110-3 normalisation-convention difference).
- (b) Independent computation of the Borel singularity `ξ_0 = 2/sqrt(3)` at higher than 2.04 digits agreement (110 D-110-4).
- (c) Independent computation of the Frobenius-to-WKB connection-matrix anchors `M_11 = 1.9420321374711220465`, `M_21 = -2.9999268666050110215` (110 D-110-5 basis-convention deferment).

This Phase D verdict bin DEMOTED applies strictly to the inversion-function-output side. The independent-Stokes-data side remains OPEN and is the scope of the cascade-stub forward-prompt outlined in [Phase E](phase_e_cascade_stub_outline.md).

---

## §6 Audit limitations

This audit is purely STATIC. It does not:
- Re-run `lax_pair_solver.py` (Phase C SKIPPED per Phase A verdict).
- Acquire JM 1981 Part II (out of scope per prompt 111 §header).
- Re-litigate the 109-EXEC `NO_GO_OFF_DEGENERATION` verdict (out of scope).
- Reverse-engineer the upstream pipeline (if any) that produced the 14 digits at `jimbo_final.py:26` (this is the scope of the cascade-stub Phase E).
- Modify any source file (out of scope per prompt 111 §header).
