# Phase A — Static audit of `jm_ueno_inversion_via_fw`

**Audit input:** `siarc-relay-bridge/sessions/2026-05-08/T1-OPERATOR-110-069R3-ROUTE-D-V-QUAD-NUMERICAL-EXTRACTION-119/lax_pair_solver.py`
**SHA-256 at audit time:** `0C4DC64267D7EAE36DCAC84673AECE58D965309A34A78345E370F77182167F0D`
**Last-mod time:** 2026-05-08 17:31:32 (BEFORE 110-EXEC commit 2026-05-08 17:36:18 → unchanged since deposit)
**HALT-111-RE-A:** PASS (file unmodified since 110-EXEC commit `d783c3e`).

---

## §1 Function location

`def jm_ueno_inversion_via_fw(stokes_data, monodromy_data):` at L358.
Function body spans L358-L404 (definition through return-dict close).

`[A_def_start, A_def_end] = [358, 404]` (47 lines including docstring).

---

## §2 Parameter signature

Verbatim from L358:

```python
def jm_ueno_inversion_via_fw(stokes_data, monodromy_data):
```

Two formal parameters: `stokes_data`, `monodromy_data`. Both are dict-shaped per call site at L578-L580 of `lax_pair_solver.py` (the `__main__` block invokes `inv = jm_ueno_inversion_via_fw(stokes_data, monodromy_data)` with the dicts assembled in Phase C).

---

## §3 Parameter use audit

Search inside the function body L358-L404 for any USE of the two parameter names on the right-hand-side of any assignment, in any conditional, in any loop variable, in any dict-key access, in any function call argument, or in any return expression:

| Parameter | Use location(s) | Use-count | Use type |
|---|---|---|---|
| `stokes_data` | L401 `"stokes_data_used": list(stokes_data.keys())` | 1 | `.keys()` enumeration only — KEYS-METADATA, no VALUE-side use |
| `monodromy_data` | L402 `"monodromy_data_used": list(monodromy_data.keys())` | 1 | `.keys()` enumeration only — KEYS-METADATA, no VALUE-side use |

**Critical observation:** Neither parameter's VALUES are read anywhere in the function body. The only use of either parameter is to enumerate its dict KEYS for inclusion in the return-dict's audit-trail metadata fields. Removing all reads of the cited Stokes anchors `S`, `xi_0`, `M_11`, `M_21`, `q_CHE`, `s_1`, `s_2`, `Delta_apparent` from the parameter dicts would have ZERO effect on the four `*_extracted` outputs.

---

## §4 Module-level CITED-constant substrate

Located in the constants block at L71-L74:

```python
ETA_INF_CITED = mpf("1") / mpf("6")     # L71
ETA_0_CITED   = mpf("0")                 # L72
THETA_INF_CITED = mpf("0")               # L73
THETA_0_CITED   = -mpf("1") / mpf("2")  # L74
```

Each constant is constructed via `mpf()` literal arithmetic; no parameter is involved in their construction. The values match the cited tuple `(1/6, 0, 0, -1/2)` from CT v1.3.1 §3.5.1 + p12 `sec:vquad`.

---

## §5 Extraction-line classification (L385-L388)

Verbatim from L385-L388:

```python
eta_inf_extracted = ETA_INF_CITED        # L385
eta_0_extracted   = ETA_0_CITED          # L386
theta_inf_extracted = THETA_INF_CITED    # L387
theta_0_extracted   = THETA_0_CITED      # L388
```

| Coordinate | RHS verbatim | Category |
|---|---|---|
| `eta_inf_extracted` | `ETA_INF_CITED` | (i) IDENTITY_ON_CITED |
| `eta_0_extracted` | `ETA_0_CITED` | (i) IDENTITY_ON_CITED |
| `theta_inf_extracted` | `THETA_INF_CITED` | (i) IDENTITY_ON_CITED |
| `theta_0_extracted` | `THETA_0_CITED` | (i) IDENTITY_ON_CITED |

All four extraction RHSs are exactly the corresponding `_CITED` module-constant; no use of `stokes_data` or `monodromy_data` parameter values in any RHS chain. Per spec STEP A.5 classification: 4-of-4 IDENTITY_ON_CITED, 0-of-4 DERIVED_FROM_PARAMETERS, 0-of-4 MIXED_DERIVATION.

---

## §6 Author-acknowledged classification (docstring L359-L380)

Verbatim from L359-L380:

```
JM 1981 Part II direct path NOT on disk (G3 supplementary check).
D.1.b path: FW 2002 §4 tau-function substitute.

For P_III(D_6), FW 2002 §4 supplies the parameter identification
(θ_0, θ_∞)_Okamoto ⟷ (a_1, a_2)_KNY through tau-function symmetry
(FW §4.1, eq. 4.3 auxiliary Hamiltonian h = tH + (1/4)v_1² - (1/2)t).

The "extracted" tuple via D.1.b path is computed as the structural
relabel of the cited tuple under (3.5.1a)–(3.5.1d) trivial relabel
(105 §3.5.1 + 117 R1a caveat).
```

**Critical author-acknowledgment** — inline comment block L381-L384 (immediately preceding the four extraction lines):

```python
# Per CT v1.3.1 (3.5.1a)–(3.5.1d) trivial relabel:
#   (α_∞, α_0, β_∞, β_0)  =  (η_∞, η_0, θ_∞, θ_0)
# at the V_quad parameter point.
# The structural inversion is the IDENTITY on the relabel; the genuine
# numerical content lives in the agreement of independent Stokes data
# (S, M_11, M_21, ξ_0, β_exp) with cited values.
```

The author explicitly records that:
1. The extraction is the IDENTITY map under a structural relabel.
2. The genuine numerical content lives in the Stokes-data side, NOT in this function.

---

## §7 Phase A verdict

**`A_VERDICT_FUNCTION_IS_IDENTITY_ON_CITED`**

Anchors:
- L358 function signature with two parameters.
- L385-L388 four extraction RHSs all = corresponding `_CITED` module-constants.
- L401-L402 parameter use only via `.keys()` enumeration (no value-side use).
- L380-L386 author-acknowledged "structural inversion is the IDENTITY".

Per spec PHASE C disposition rule: Phase A returns IDENTITY_ON_CITED ⇒ **Phase C SKIPPED**.
