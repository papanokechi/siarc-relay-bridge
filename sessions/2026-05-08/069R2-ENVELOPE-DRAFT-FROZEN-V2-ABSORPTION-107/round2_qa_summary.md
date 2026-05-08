# Round-2 QA — operator parallel-manual rubber-duck pass

**Invoked**: 2026-05-08 ~09:10 JST (post-compaction, post-Round-1)
**Tool**: human operator (papanokechi) running parallel manual QA with full bridge git access
**Input**: 069r2 envelope DRAFT-FROZEN-V1 body + bridge git history + cited handoffs (601500b, 2eb9b28, c0619a5, others)
**Output**: 6 findings (1 BLOCKING + 3 high-impact non-blocking + 2 minor), all absorbed

## Findings absorbed (6 of 6)

### R-1 BLOCKING — Greek-letter route-namespace collision with 069r1

**Substrate**: 069r1 handoff (`601500b:sessions/2026-05-07/M6-CC-R1-CLOSURE-PREFLIGHT-069R1/handoff.md` L60-69) defines:
- Path α = KNY chart-shift Δ (RULED OUT by 069r1)
- Path β = Okamoto §3 alone (RULED OUT by 069r1)
- Path γ = T1-Synth analytic-guidance request (069r2 envelope IS the executing-instance of this path)
- Path δ = literature acquisition (JM/CM/FW)

069r2 DRAFT-FROZEN-V1 silently re-used Path γ for "FW arXiv + Okamoto 1987" and Path β for "JM 1981 / CM 2008 OA wait" — distinct from 069r1's Path β/γ meanings. §3 then explicitly stated "Path α (KNY-only) and Path β-Okamoto-only: Already RULED OUT by 069r1" using the OLD meaning while §4 asked the synth to weigh "Path γ vs Path β" with the NEW meaning, AND §4 Q4 introduced yet a third namespace `β1…β5`. The synth would have hit triple-meaning ambiguity for β in a single envelope.

**Resolution**: Full Route A/B/C/D/E rename across §1-§10 (rather than δ_FW/δ_JM-CM/ε_NUM/ε_AUTHOR per operator suggestion — see judgment call in handoff). HALT-S6 forbids re-use of α/β/γ/δ for new routes within 069r2 to preserve 069r1 namespace integrity. 069r1 namespace preserved verbatim in §9 cross-references.

| 069r2 (NEW) | Was (DRAFT-FROZEN-V1) | Description |
|---|---|---|
| Route A | (no V1 equivalent — operator R-1 surfaced) | In-hand Hamiltonian coefficient-matching from 058R+KNY+Okamoto; zero-acquisition |
| Route B | "Path γ" | FW arXiv math-ph/0201051 + Okamoto 1987 §3 (Tier 1 OA) |
| Route C | "Path β" | JM 1981 / CM 2008 ILL/OA acquisition (Tier 3 paywalled) |
| Route D | (R-3b NEW) | Direct numerical chart-map fitting (PSLQ / symbolic regression) |
| Route E | (R-3b NEW) | CT v1.3 §3.5 author-side (η,θ)→(α,β) rename — orthogonal precondition |

### R-2 high-impact — §4 Q2 missing (η,θ)→(α,β) rename probe

**Substrate**: 069r1 surfaced OQ-W21-CHART-MAP (the (η,θ)→(α,β) rename gap): Okamoto 1987 §3 uses parametrisation (η_∞, η_0, θ_∞, θ_0); the four-tuple (α,β) is a CT v1.3 §3.5 project-side rename. If the synth answers "Y, Okamoto §3 closes the second half" without acknowledging the rename derivation, the agent will hit a hidden substrate gap mid-Route-B-executor.

**Resolution**: QB.3 added to §4 with answer space `Y_RENAME_REQUIRED` / `N_OKAMOTO_USES_AB` / `UNCLEAR`. Cascade in §6 wired so `Y_RENAME_REQUIRED` triggers Route E precondition gate.

### R-3 high-impact — §5 Q3 missing PARTIAL_RENAME bin

**Substrate**: PARTIAL_PATH_GAMMA in V1 was scoped to "FW supplement required from JM 1981 / CM 2008" — a literature-mechanism PARTIAL. The most likely realistic outcome (FW + Okamoto §3 close the literature side, but the (η,θ)→(α,β) rename is still author-side) collapsed into PARTIAL_PATH_GAMMA via the wrong mechanism.

**Resolution**: QB.4 verdict bins split into:
- `PARTIAL_ROUTE_B_LIT` (FW fragment + JM/CM supplement needed)
- `PARTIAL_ROUTE_B_RENAME` (FW + Okamoto literature-complete, but CT v1.3 §3.5 author-rename derivation needed → escalates to Route E)

The Q4 cascade trigger condition was correspondingly updated.

### R-3b high-impact — Path δ/ε scan: two routes omitted

**Substrate**: §8 Q.3 of the envelope explicitly asked whether a Path δ/ε exists that the dichotomy is missing. Two existed:
- **Path ε_NUM** (direct numerical chart-map fitting from V_quad → P_III numerical solutions): executor-class alternative requiring no literature acquisition; 2-4 hr fitting relay if both Path γ and Path δ stall.
- **Path ε_AUTHOR** (CT v1.3 §3.5 author-side (η,θ)→(α,β) rename derivation): the original scope of 069r1's Path γ recommendation; 069r2 V1 dropped it without comment.

**Resolution**: Path ε_NUM became Route D (parallel, executor-class). Path ε_AUTHOR became Route E (orthogonal precondition gate; operator-side, not synth-weighable as a route alternative). §3 NOTE block flags Route E as gate-for-ALL-of-A-D.

### M-3 minor — Forbidden-verb pattern at 14 verbs

**Substrate**: 099 envelope uses an 8-verb scan superset that includes `discharges` and `ratifies`; 069r2 V1 omitted these.

**Resolution**: STEP 0.3 + §7 both extended to 16-verb pattern. Final pattern:
```
\b(shows|confirms|proves|demonstrates|establishes|verifies|verified|
   validates|validated|corroborates|corroborated|certifies|certified|
   settles|settled|discharges|ratifies)\b
```

### M-4 minor — STEP 0.2 SHA pre-flight had truncated hashes

**Substrate**: V1 STEP 0.2 listed 7 of 9 SHAs with truncated `...` rather than full hashes; only 2 were full 40-char.

**Resolution**: All 9 SHAs replaced with full 40-char hashes via `git rev-parse <short>` output:
```
e7bfe4969d7e68f510fb588b309d2e0314261db0  068
9596c21af645b1b70ad5ce98cccbd8171ac11d6a  074
05810a201b9fc8761d748d0ba4230e6340128e97  069 (Phase D numerical follow-up)
601500baf6deb469f3a82c1b8a5742779fbaf6f9  069r1
5de7d2bd99ec9ad01d4dae8ad3df3ef1ab414f60  102 initial
aa350404f77a5c07b74e4f8116492ab30d17be7f  102 follow-on
5137155d83b748bf9c0696fbf50bd91d83b8dacd  075
c0619a5b9478cbb0b7ab015eb4308378ccd5d58e  097
2eb9b28105ca9ebef7bf3288db9a28f090cfafcf  058R
```

## Additional path-inventory finding (not enumerated separately)

V1 §1 path-inventory was wrong on 6 of 9 entries:

| # | V1 said | Actual (`git show --stat=200`) |
|---|---------|-------------------------------|
| 3 | `sessions/2026-05-06/M6_CC_PHASE_D_NUMERICAL_FOLLOWUP-069/` | `sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/` (date+folder both wrong) |
| 5 | `sessions/2026-05-08/102/` | `sessions/2026-05-07/T1-069R1-SUBSTRATE-GAP-PRE-VERIFICATION-102/` |
| 6 | `sessions/2026-05-08/102/` | same as #5 |
| 7 | `sessions/2026-05-08/T2-M6-CC-CHART-MAP-CANDIDATE-B1-CHECK-075/` | `sessions/2026-05-07/...` |
| 8 | `sessions/2026-05-08/T2-ICA-VQUAD-PHI-PCF-097/` | `sessions/2026-05-07/...` |

**Resolution**: All 9 paths rewritten from canonical `git show --stat=200 <SHA> | grep handoff.md` output.

## §2 chart-map direction reciprocal-mismatch finding (non-blocking)

058R `phase_b_canonical_map.md` L132-140 states the chart-map direction as "(α,β) 4-tuple → KNY (a₀,a₁,a₂)"; 069r2 V1 §2 cited the gap as "(a₀,a₁,a₂) → (α_∞,α_0,β_∞,β_0)" (inverse direction).

**Resolution**: §3 NOTE block carries a one-sentence reciprocal-direction note. Map presumed bijective; direction is conventional. No structural rewrite required.

## Status

Round-2 absorption COMPLETE post-compaction. Envelope progressed from DRAFT-FROZEN-V1 → DRAFT-FROZEN-V2. Final state at SHA256 `CBA1FD6E42A47FD2C0BCACF4061173F5F92624596FFCCC0FF207C3408D58168F`.
