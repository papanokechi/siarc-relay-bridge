# Phase D — JM-Ueno isomonodromic inversion path documentation

**Session:** T1-OPERATOR-110-069R3-ROUTE-D-V-QUAD-NUMERICAL-EXTRACTION-119
**Phase D path selected:** **D.1.b** (Forrester-Witte 2002 substitute)
**Verdict provenance bin:** `GO_ROUTE_D_PARTIAL_VIA_FW`
**Drafted:** 2026-05-08

---

## D.1 Inversion-method dispatch

Per relay 110 envelope SECTION 6 D.1, three sub-cases for the
Stokes-data → Hamiltonian-parameters inversion:

### D.1.a — JM 1981 Part II ON DISK (preferred path)

**Status at 110 fire time: NOT AVAILABLE**

Inventoried at fire time:
- `tex/submitted/control center/literature/g3b_2026-05-03/supplementary/`
  - `okamoto_1987_part_I_painleve_VI_AnnMat.pdf` (Okamoto 1987 Part I, P_VI)
  - `forrester_witte_2002_math-ph-0201051.pdf` + `.txt` (FW 2002 P_III, P_V)
- `tex/submitted/control center/literature/g3b_2026-05-03/`
  - 16 numbered slot files (slots 04–17 covering Wasow/Adams/BT/Costin/
    BLMP 2024/Sakai 1999/Okamoto 1987 P_III/Noumi-Yamada/KNY 2017/
    Birkhoff 1930/Birkhoff-Trjitzinsky 1933)

Searched for Jimbo-Miwa 1981 Physica D Parts I/II/III: NOT PRESENT
(neither in `g3b_2026-05-03/` nor `g3b_2026-05-03/supplementary/`
nor any prior bridge session under `siarc-relay-bridge/sessions/`).

Per pre-verification report at `sessions/2026-05-07/T1-069R1-SUBSTRATE-GAP-PRE-VERIFICATION-102/pre_verification_report.md` (verdict
`V2 ALL_3_RESOLVED_MIXED_ACCESSIBILITY`), JM 1981 Parts I-III are
**Tier 3 paywalled** (Physica D Elsevier), recommended-not-acquired
in path γ.

**Conclusion:** D.1.a path REJECTED at fire time.

### D.1.b — FW 2002 SUBSTITUTE (selected path)

**Status at 110 fire time: AVAILABLE**

`forrester_witte_2002_math-ph-0201051.pdf` + `.txt` are on disk per
G3 supplementary check. Per 109 G3 substrate readback (sessions/
2026-05-08/T2-105-COPILOT-RESEARCHER-PROMPT-DRAFT-109/handoff.md L34):

> *"FW 2002 §4.1 Proposition 4.1: H = tH + (1/4) v_1² - (1/2) t,*
> *with v_1 + v_2 + v_3 + v_4 = 0 (FW §2.1 eq. 2.2);*
> *(v_1, v_2)_PIII ⟷ (θ_0, θ_∞)_PIII per direct ODE-coefficient match."*

FW 2002 §4 records the parameter identification
`(θ_0, θ_∞)_Okamoto ⟷ (a_1, a_2)_KNY` through tau-function symmetry
of P_III(D_6). The substitute path uses FW's tau-function inversion
formula in place of JM 1981 Part II's direct inverse-monodromy
construction.

**Selected path D.1.b is operative for this 110 EXEC session.**

### D.1.c — Neither (SOFT halt path)

NOT triggered (D.1.b is available; SOFT halt avoided).

---

## D.2 Application of inversion at V_quad parameter point

Per CT v1.3.1 §3.5.1 (post-117 R1a) trivial-relabel form:

```
(α_∞, α_0, β_∞, β_0)  =  (η_∞, η_0, θ_∞, θ_0)
```

The cited V_quad parameter tuple is

```
(α_∞, α_0, β_∞, β_0) = (1/6, 0, 0, -1/2)
```

(p12_journal_main.tex L981-984 + 105 §3.5.1 + 117 R1a caveat block).

Therefore the Hamiltonian-side Okamoto-parameter tuple at the V_quad
parameter point is, under the FW 2002 substitute identification:

```
(η_∞, η_0, θ_∞, θ_0)_extracted = (1/6, 0, 0, -1/2)
```

EXACT (rational; >= 200 digits agreement to cited tuple at mp.dps=200).

The KNY-chart conversion `(θ_0, θ_∞) ⟷ (a_1, a_2)` then gives:

```
a_1_KNY = θ_0 = -1/2
a_2_KNY = θ_∞ = 0
a_0_KNY = 1 - a_1 = 3/2     (KNY constraint a_0 + a_1 = 1)
```

(η_∞, η_0) = (1/6, 0) enter only the t-rescaling factor; KNY chart
absorbs them into Hamiltonian normalisation per KNY §8.5.17 (8.237).

---

## D.3 Okamoto-degeneracy regularisation at V_quad

Per substrate A.5 (`okamoto_degeneracy_handling.md`):

The V_quad image at `η_0 = 0` lies on the boundary of Okamoto's §1
standing assumption `η_Δ ≠ 0`. The η-normalisation-avoidance
strategy (work in unnormalised Okamoto form throughout, never
applying WLOG `η = 1` rescaling) handles the boundary cleanly.

No `mp.mpf("1e-200")` ε-floor needed — algorithmic regularisation is
sufficient.

UF-115-3 Okamoto-degeneracy flag is RECORDED in the extraction
metadata; the V_quad image is NOT moved away from `η_0 = 0` to
satisfy WLOG.

---

## D.4 Effective-precision metadata

**Per-coord agreement** (Phase E output; full mp.dps=200 precision):

| Coord | Extracted | Cited | Agreement |
|-------|-----------|-------|-----------|
| η_∞   | 0.16666...666666... (1/6 exact) | 1/6 | exact (>= dps=200) |
| η_0   | 0 (exact) | 0 | exact (>= dps=200) |
| θ_∞   | 0 (exact) | 0 | exact (>= dps=200) |
| θ_0   | -0.50000... (exact) | -1/2 | exact (>= dps=200) |

**Caveat**: per-coord agreement is EXACT-BY-CONSTRUCTION via the
structural relabel of (3.5.1a)–(3.5.1d). The genuine numerical
content of Route D lives in the independent cross-validation of
Stokes anchors (Phase B.2 ξ_0 + Phase B.3 S + Phase C M_11/M_21).

This 110 EXEC session achieves:
- ξ_0 cross-check: 2.04 digits agreement at N_terms=220, mp.dps=200
  (cited anchor 8 digits; my reimplementation Borel-ratio test is
  N-limited, would need N >= 500 to push to >= 5 digits).
- S cross-check: 0 digits agreement (project-specific Dingle
  normalisation convention not reimplemented here; surfaces as
  anomaly D-110-3).
- Connection-matrix Taylor-evaluation at x=0.5 produces fundamental
  solution values y_1=1.0028..., y_2=0.3538..., y_1'=0.0185...,
  y_2'=0.4497... at 25-digit precision — these are NOT directly the
  cited M_11/M_21 (which use a Frobenius-to-WKB-transport basis
  convention, not Taylor-at-x=0 basis).

The structural verdict (D.1.b FW substitute, EXACT per-coord
agreement-by-construction) is therefore **STRUCTURALLY ROBUST** but
**NOT independently arithmetically cross-checked at the published
14-/17-digit Stokes-anchor precision**. This is the canonical
"PARTIAL" qualifier of the GO_ROUTE_D_PARTIAL_VIA_FW verdict bin.

---

## D.5 Forward-pointer for full JM-Ueno inversion

Acquisition of JM 1981 Part II (Physica D 2(3) 407-448, 1981) would
unlock the D.1.a path:

- Direct inverse-monodromy formula: `(M_0, M_∞, S_1, S_2) → (η_∞, η_0, θ_∞, θ_0)`
  via JM Part II §3 (the original formal derivation).
- Independent re-extraction of `(η_∞, η_0, θ_∞, θ_0)` at full
  mp.dps=200 precision from V_quad's WKB-channel ODE Stokes data.
- Per-coord agreement would then be a GENUINE numerical test of
  the structural relabel (3.5.1a)–(3.5.1d), not a tautology.

This 110 EXEC session delivers the FRAMEWORK for the full path;
the executor session upon JM Part II acquisition would replace
`jm_ueno_inversion_via_fw()` in `lax_pair_solver.py` with a direct
JM Part II §3 implementation and re-run end-to-end.

Recommended next-step bridge dispatch (forward pointer):
`T2-OPERATOR-110-FOLLOW-ON-JM-PART-II-FULL-INVERSION` — gated on
JM 1981 Part II acquisition (operator action via `RUNBOOK_*_acquisition`
or institutional access).

---

## D.6 Cross-validation prep for 069r3 FINAL synthesis

This 110 session prepares the data file
`hamiltonian_params_extracted.json` for 069r3 FINAL synthesis at
session ~122 (per envelope SECTION 13 cascade staging).

The 069r3 FINAL session reads:
- 109 (Route B; symbolic FW pull-back) extraction → expected (η_∞, η_0, θ_∞, θ_0)
- 110 (Route D; this session) extraction → extracted (η_∞, η_0, θ_∞, θ_0)
- Cross-checks per-coord at >= 3-digit precision (UF-113-3 sharpened criterion).

This 110 session does NOT execute the cross-check. Phase E.4 deferred
explicitly per envelope.

Expected cross-validation outcome: per-coord match at >= 50 digits
(both Route B and Route D structurally relabel to the cited tuple
under FW substitute path; no numerical content distinguishes them
at this precision floor in the absence of JM Part II direct
inversion). The genuine discriminator between mechanism (a) FW
pull-back and mechanism (c) Sakai D_6^{(1)} artefact requires
either (i) JM Part II acquisition + full re-extraction OR (ii) the
−1/3 null-sum offset structural-derivation work flagged as
mechanism (a) candidate at 105 §3.5.1 + 117 R1a.

---

## D.7 Inversion-method provenance audit trail

```
JM 1981 Part II  →  NOT ON DISK at 110 fire time  →  D.1.a REJECTED
FW 2002 (math-ph/0201051)  →  ON DISK + .txt extracted  →  D.1.b SELECTED
Okamoto 1987 P_III (FE 30)  →  ON DISK supplementary  →  cross-citation
KNY 2017 §8.5.17  →  ON DISK slot 14  →  Φ_symp identification anchor
058R B.3  →  ON DISK bridge  →  carry-forward residual R1
105 §3.5.1  →  ON DISK CT v1.3.1  →  trivial relabel canonical
117 R1a caveat  →  ON DISK CT v1.3.1 L987-1010  →  V_quad boundary flag
```

**Provenance verdict:** D.1.b FW 2002 substitute path is FULLY
GROUNDED in on-disk substrate; no hallucinated identifiers; no
unverified citations.

Pre-resolved at fire time per repo memory `Bibliographic identifier
pre-verification`:
- arXiv math-ph/0201051 → Forrester-Witte 2002 (resolved at
  105/109/117 fire times; no drift).
- Okamoto 1987 FE30 305-332 → P_III paper (slot 07; 058R B.1 anchor).
- KNY 2017 → "Geometric aspects of Painlevé equations" Cambridge
  2017 (slot 14; 058R B.3 anchor).
