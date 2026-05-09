# Q4 Round-2 Direct-Derivation Packet (069r3 cascade)

**Bridge session:** `T1-OPERATOR-Q4-ROUND2-DIRECT-DERIVATION-PACKET-130`
**Parent HEAD:** `ad33058` (T1-SYNTH-Q4-ROUTE-F-VERDICT-ABSORPTION-129; Round-1 verdict UNDECIDABLE_NEEDS_MORE_SUBSTRATE)
**Deposited:** 2026-05-08
**Tier:** T1-Synth dispatch (fresh Claude.ai web conversation)
**Scope:** single-round paste-and-derive packet absorbing OKS-O 2006 + Okamoto 1987 + KNY §8.5.17 + CT v1.3 §3.5.1 substrate to enable a direct derivation of the Q4 fixed-point-vs-generic-orbit classification of `V_quad → (α_∞, α_0, β_∞, β_0) = (1/6, 0, 0, −1/2)` under `W((2A_1)^{(1)})`.

---

## §1. Cascade context

- **Q1–Q3 settled** at session 124 (`ae5b7f7`): Routes A + B closed; mechanisms (a) + (b) eliminated; Route F (Sakai D₆⁽¹⁾ surface-type machinery) is the unique surviving candidate.
- **Q4 framing:** does the V_quad image sit at an affine-Weyl fixed point of `W((2A_1)^{(1)})` (signalling structural distinguishedness inside the surface-type framework) or at a generic orbit point?
- **Round-1 verdict (session 129):** UNDECIDABLE_NEEDS_MORE_SUBSTRATE (high confidence). Three BLOCKING residuals identified:
  - **UF-126-PARAM-COUNT** — Sakai `(a_0, a_1, b_0, b_1)` ↔ KNY `(a_0, a_1, a_2)` cross-walk required at symbol level.
  - **UF-126-DELTA-DECOMP-FORM** — V_quad's null-sum violation `Δ = −1/3` admits ≥3 decomposition forms (additive / coefficient-rescaled / composite).
  - **UF-129-1** — Sakai EOM constraint `a_0 + a_1 = b_0 + b_1 = 1` is a hard prerequisite, not just a normalisation choice.

## §2. What is NEW since Round 1

Two acquisitions landed between session 129 and this dispatch:

1. **OKS-O 2006** (Ohyama–Kawamuko–Sakai–Okamoto, *Studies on the Painlevé equations V: third Painlevé equations of types `D_7^{(1)}` and `D_8^{(1)}`*, J. Math. Sci. Univ. Tokyo Vol. 13 (2006) pp. 145–204) — acquired this session at `tex/submitted/control center/literature/g3b_2026-05-03/10_ohyama_kawamuko_sakai_okamoto_2006_painleve_V_D7_D8.pdf` (SHA `ABC5A43B80BB1E6992606CCC2597995420AF2975BAB6FAB9697F8A0833091F6B`; 353 756 B; 60 pp). Full pypdf extraction at companion `.txt` (78 466 B). Provides the **explicit Hamiltonian → classical-ODE α/β/γ/δ map** (§3 eq. (26) + L556-558) and the **PIII'(D₇) Cremona-action table** (§2.3 Theorem 6 + table at L460-481) that close the cross-walk gap.
2. **CT v1.3 §3.5.1 Okamoto-rename derivation** — landed at session 105 (`0427c0a`) as `siarc-relay-bridge/sessions/2026-05-08/T1-OPERATOR-CT-V13-3.5.1-OKAMOTO-RENAME-DERIVATION-105/section_3_5_1_okamoto_rename.tex` (216 lines, 10 069 B). Pins the four-tuple labelling at the Hamiltonian convention (resolving A-115-1 reconciliation); reconciliation amendment landed at session 128 (`111de50`).

Together with Okamoto 1987 §0+§1 (already on disk at `literature/g3b_2026-05-03/07_okamoto_1987_painleve_III_FE30.txt`) and KNY 2017 §8.5.17 (carry-forward from session 126 packet `route_f_substrate_paste_packet.md`, SHA `FAA5F083E2156A34`), the substrate is now **sufficient** for a direct derivation under reasonable structural assumptions.

## §3. CT v1.3 §3.5.1 (Hamiltonian-rename derivation; substrate-on-disk)

**Path pointer:** `siarc-relay-bridge/sessions/2026-05-08/T1-OPERATOR-CT-V13-3.5.1-OKAMOTO-RENAME-DERIVATION-105/section_3_5_1_okamoto_rename.tex` (216 lines, SHA-anchored at landing commit `0427c0a`).

**Salient content (synth reads file directly; key spans flagged):**

- **L42–47:** Okamoto's H_III display verbatim:
  ```
  t·H_III(η_∞, η_0, θ_∞, θ_0; t; q, p)
    = q² p² − (η_∞ q² + θ_0 q − η_0 t) p + (1/2) η_∞ (θ_0 + θ_∞) q
  ```
- **L92–108:** four-tuple definitional formulae (3.5.1a–d):
  ```
  α_∞ := η_∞ ,   α_0 := η_0 ,   β_∞ := θ_∞ ,   β_0 := θ_0
  ```
  i.e. the renaming is the trivial identity in Hamiltonian-parameter symbol assignments. Under (3.5.1a–d) the V_quad image `(1/6, 0, 0, −1/2)` reads as `η_∞ = 1/6`, `η_0 = 0`, `θ_∞ = 0`, `θ_0 = −1/2`.
- **L137–174:** three structural-mechanism candidates listed for the `Δ = −1/3` null-sum violation (mechanism (a) FW pull-back / (b) per-coordinate symmetric −1/12 / (c) Sakai D₆⁽¹⁾ surface-type). Mechanisms (a) + (b) are eliminated by the 069r3 cascade (see §1). Mechanism (c) is the Q4 target.
- **L185–216:** three-tuple disambiguation Remark `[rem:alpha-beta-tuples]` resolving namespace collisions across PCF coefficients vs Hamiltonian parameters vs Sakai root variables.

## §4. Okamoto 1987 — H_III + standing assumption + WLOG normalisation

**Path pointer:** `tex/submitted/control center/literature/g3b_2026-05-03/07_okamoto_1987_painleve_III_FE30.txt` (191 162 B; pypdf extraction with ¥-encoded LaTeX; minor whitespace normalisation on transcription).

- **§0 H_III display + (0.1) α/β/γ/δ map** (.txt L185–220, transcribed):
  ```
  t·H_III = q² p² − {η_∞ q² + θ_0 q − η_0 t} p + (1/2) η_∞ (θ_0 + θ_∞) q
  ```
  with classical-ODE coefficients
  ```
  α = −4 η_∞ θ_∞ ,   β = 4 η_0 (θ_0 + 1) ,   γ = 4 η_∞² ,   δ = −4 η_0² .
  ```
  **Standing assumption:** `η_Δ ≠ 0` for `Δ ∈ {0, ∞}`. WLOG normalisation `η_Δ = 1`.
- **§1 normalised form** (.txt L875–905, transcribed): under `η_0 = η_∞ = 1`,
  ```
  t·H_III = q² p² − {q² + θ_0 q − t} p + (1/2)(θ_0 + θ_∞) q
  ```
  with reduction map
  ```
  α = −4 θ_∞ ,   β = 4 (θ_0 + 1) ,   γ = 4 ,   δ = −4 .
  ```
  Standing assumption `η_0 η_∞ ≠ 0` (equivalently `γδ ≠ 0`) is reaffirmed as the prerequisite for the §1 normalisation.

## §5. KNY 2017 §§8.5.1–8.5.16 (convention-fixing material)

**Status:** known gap; not on disk. Round-1 named this as TERTIARY acquisition target. Synth treats §§8.5.1–8.5.16 as **structural placeholder** in the chain `Sakai → KNY §8.5.17`; if the derivation requires a specific convention from §§8.5.1–8.5.16, the synth should flag as a residual rather than fabricate. KNY §8.5.17 is on disk and substantive (next §).

## §6. KNY 2017 §8.5.17 — discrete shift `T_α` (carry-forward from 126)

**Path pointer:** `siarc-relay-bridge/sessions/2026-05-08/T2-OPERATOR-069R3-PRIORITY-1-S10-ROUTE-F-SUBSTRATE-CONSOLIDATION-126/route_f_substrate_paste_packet.md` (601 lines, SHA `FAA5F083E2156A34`). §6 of that packet contains §8.5.17 verbatim including:

- KNY-side Hamiltonian (eq. 8.237) in `(a_0, a_1, a_2)` parameters
- discrete shift `T_α: (a_1, a_2) ↦ (a_1 + 1, a_2 + 1)` (eq. 8.240)
- level constraint `a_0 + a_1 + a_2 = 1` (per §D4.6 of the 126 packet)

## §7. Forrester–Witte 2002 §4.1 / eq. (4.3)

**SHA-cite (length control):** see 126 packet §7 for the Route B closure context. Forrester–Witte 2002 has been ratified as Q1_PROVISIONAL_RATIFY_B_CLOSED at session 124. No re-extraction needed in this packet.

## §8. NEW — OKS-O 2006 verbatim spans

Substrate framing: spans below are **as appearing in OKS-O 2006 §N (pypdf extraction; minor whitespace normalisation applied)**. Synth can verify against `literature/g3b_2026-05-03/10_ohyama_kawamuko_sakai_okamoto_2006_painleve_V_D7_D8.txt` at the cited line ranges.

### §8.A — OKS-O 2006 §3 (.txt L540–558): L(D₆) Lax pair eq. (26) + α/β/γ/δ map (CENTRAL)

> **eq. (26):**
> `H = (1/t) { q² p² − (η_∞ q² + θ_0 q − η_0 t) p + (1/2) η_∞ (θ_0 + θ_∞) q }`
>
> Under the substitution leading to the classical-ODE form,
> `α = −4 η_∞ θ_∞ ,   β = 4 η_0 (1 + θ_0) ,   γ = 4 η_∞² ,   δ = −4 η_0² .`
>
> Here we assume `η_0 η_∞ ≠ 0`; the deformation given above concerns `P_III'(D_6)`.

This block matches Okamoto 1987 §0 verbatim and pins the Hamiltonian → classical-ODE map across both substrate sources.

### §8.B — OKS-O 2006 §2.3 (.txt L460–481): PIII'(D₇) Cremona table

Per OKS-O 2006 Theorem 6, `Cr(D_7^{(1)}) = W̃_a(A_1) = ⟨s_1, σ⟩` with `α_0 = 1 − α_1`, acting on `(α_0, α_1; q, p; t, tH)` via the table (transcribed; column header: `x | α_0 | α_1 | p | q | t | tH`):

```
s_0 :  −α_0          α_1 + 2 α_0    p − α_0/q + t/q²    q          −t      tH + t/q − α_0
s_1 :  α_0 + 2 α_1   −α_1           −p                  −q − α_1/p − 1/p²   −t   tH
σ   :  α_1           α_0            −q/t                t·p        −t      tH − q·p
```

**Significance:** PIII'(D₇) carries a **single A_1^{(1)} factor** (vs **two A_1^{(1)} factors** for P_III(D_6) per KNY 2017 §8.5.17). The D_6 → D_7 degeneration **collapses one A_1^{(1)} factor**; this is the structural feature that the V_quad image is candidate-located at.

### §8.C — OKS-O 2006 §3.1 (.txt L575–720): L(D_7) + L(D_8) Riemann schemes + Hamiltonians

- **L(D_7):** singularities at `x = 0, ∞, q`; `x = 0` irregular Poincaré rank 1; `x = ∞` irregular Poincaré rank 1/2; `x = q` apparent (exponents 0, 2).
- **L(D_8):** both `x = 0` and `x = ∞` irregular Poincaré rank 1/2; `x = q` apparent.
- **PIII'(D_7) Hamiltonian:** `t·H = q² p² + α_1 q p + t p + q` (single parameter `α_1`).
- **PIII'(D_8) Hamiltonian:** `t·H = q² p² + q p − (1/2)(q + t/q)` (no parameters; Theorem 7: Cremona group is `Z_2`).

## §9. UF-129-1 + UF-126-PARAM-COUNT cross-walk substrate (synth-side derivation request)

The Round-1 verdict identified the Sakai `(a_0, a_1, b_0, b_1)` ↔ KNY `(a_0, a_1, a_2)` cross-walk + the Sakai-EOM constraint `a_0 + a_1 = b_0 + b_1 = 1` as the load-bearing missing pieces.

**Substrate now in hand to drive the cross-walk:**

1. The §8.A α/β/γ/δ map **fixes the classical-ODE → Hamiltonian-parameter direction** unambiguously across OKS-O 2006 + Okamoto 1987.
2. CT v1.3 §3.5.1 **fixes the four-tuple labelling at the Hamiltonian convention** (resolves A-115-1).
3. KNY §8.5.17 **fixes the KNY-side discrete-shift action** in `(a_0, a_1, a_2)`.
4. OKS-O 2006 §2.3 + §3.1 **provide the structural identification of the D_6 → D_7 degeneration boundary** as a single-A_1^{(1)}-factor collapse.

**Critical implication for V_quad image** `(α_∞, α_0, β_∞, β_0) = (1/6, 0, 0, −1/2)` under CT §3.5.1 trivial relabel:

- `η_∞ = 1/6 ≠ 0` ✓ but `η_0 = 0` → **violates `η_0 η_∞ ≠ 0` standing assumption** of OKS-O 2006 §3 + Okamoto 1987 §0/§1.
- `γ = 4·(1/6)² = 1/9 ≠ 0`; `δ = −4·0² = 0` → **`γ δ = 0` violates classical-ODE form prerequisite**.
- Therefore V_quad's image **lands exactly on the D_6 → D_7 degeneration boundary**, where one A_1^{(1)} factor of `W((2A_1)^{(1)})` collapses (OKS-O 2006 §2.3 Theorem 6: PIII'(D_7) has only `W̃_a(A_1) = ⟨s_1, σ⟩` Cremona action).

This is the **substantive structural finding** that the substrate now supports. The Q4 fixed-point-vs-generic question can be re-cast on the boundary side: in the surviving A_1^{(1)} factor (acting on `α_1`), is `V_quad` a fixed point of `s_1` (which sends `α_1 ↦ −α_1`) or `σ` (which interchanges `α_0 ↔ α_1`)?

## §10. Q4 v2.0 DIRECT DERIVATION REQUEST (synth scope)

**Synth asked to perform the following derivation** under the substrate above; output as Q4 v2.0 verdict packet.

### §10.1 Required derivations

(D1) **Confirm the D_6 → D_7 degeneration diagnosis** for V_quad: pull through the reduction map (Okamoto §0 / OKS-O 2006 §3) to verify that `η_0 = 0` → V_quad sits in the PIII'(D_7) sector (where `δ = 0` collapses the D_6 deformation) rather than on the open PIII'(D_6) generic stratum.

(D2) **Evaluate the W̃_a(A_1) action of OKS-O 2006 §2.3 Theorem 6** at the V_quad image. Specifically: what are the values of the Sakai-side `α_0` and `α_1` symbols at V_quad (after pullback through the cross-walk that the substrate now permits)? Is V_quad a fixed point of `s_1` (i.e. `α_1 = 0`)? Of `σ` (i.e. `α_0 = α_1`)? Of both? Of neither?

(D3) **Cross-walk note.** Acknowledge that the PIII'(D_6) → PIII'(D_7) sector identification eliminates the original `W((2A_1)^{(1)})` framing in favour of the smaller `W̃_a(A_1) ⋊ Z_2 = Aut(D_7^{(1)}) ⋉ W((A_1)^{(1)})` (from OKS-O 2006 Theorem 6). This is a **strict refinement** of the Round-1 framing, not a contradiction — it absorbs UF-126-PARAM-COUNT (parameter count drops from 4 to 2) and UF-129-1 (the Sakai EOM constraint `a_0 + a_1 = 1` survives in the surviving A_1^{(1)} factor).

(D4) **Resolve UF-126-DELTA-DECOMP-FORM** under the D_7 sector: the `Δ = −1/3` violation now reads as **the structural feature that places V_quad at the D_6 → D_7 boundary**, not as a free-decomposition ambiguity. In the D_7 single-parameter Hamiltonian `t·H = q² p² + α_1 q p + t p + q` (OKS-O 2006 §3.1), is V_quad's image a distinguished value of `α_1`?

### §10.2 Verdict packet (synth produces)

Synth returns Q4 v2.0 verdict in the form:

- **Q4_v2_VERDICT:** GO_ROUTE_F_FIXED_POINT_DISTINGUISHED | GO_ROUTE_F_GENERIC_ORBIT | NO_GO_ROUTE_F_DEGENERATION_BLOCKS_CLOSURE | UNDECIDABLE_NEEDS_KNY_§§8.5.1-16 | PATH_DELTA_ESCALATION (Jimbo–Miwa 1981 Part II)
- **Confidence band:** LOW / MEDIUM / MEDIUM-HIGH / HIGH
- **Per-derivation status:** D1 / D2 / D3 / D4 each marked CLOSED / PARTIAL / DEFERRED with substrate cite
- **Residual-question list** (if any): synth flags any remaining UFs at substrate level

## §11. Verdict ladder (cascade routing)

| Verdict bin | Cascade routing |
|---|---|
| GO_ROUTE_F_FIXED_POINT_DISTINGUISHED | fire prompt 117 (Route F executor envelope; novel surface-type framework derivation; ~8–20 hr) |
| GO_ROUTE_F_GENERIC_ORBIT | downgrade Route F priority; re-open Q5 conjectural ranking (JM 1981 II + Sakai 2001 hybrid) |
| NO_GO_ROUTE_F_DEGENERATION_BLOCKS_CLOSURE | escalate to PATH_DELTA fallback per session 124 §6 TIER 2 |
| UNDECIDABLE_NEEDS_KNY_§§8.5.1-16 | fire 069r4 substrate-acquisition envelope for KNY §§8.5.1-16 (~2–4 hr lit-hunt) |
| PATH_DELTA_ESCALATION | fire JM 1981 Part II acquisition (Tier 3 paywalled; ~7–30 days) |

## §12. SHA inventory + path inventory (verifiable substrate)

| Substrate | Path | SHA (or cited bridge SHA) | Status |
|---|---|---|---|
| OKS-O 2006 PDF | `tex/submitted/control center/literature/g3b_2026-05-03/10_ohyama_kawamuko_sakai_okamoto_2006_painleve_V_D7_D8.pdf` | `ABC5A43B80BB1E6992606CCC2597995420AF2975BAB6FAB9697F8A0833091F6B` | acquired this session |
| OKS-O 2006 .txt | `tex/submitted/control center/literature/g3b_2026-05-03/10_ohyama_kawamuko_sakai_okamoto_2006_painleve_V_D7_D8.txt` | (companion; pypdf extraction; 78 466 B) | acquired this session |
| Okamoto 1987 .txt | `tex/submitted/control center/literature/g3b_2026-05-03/07_okamoto_1987_painleve_III_FE30.txt` | (slot 07; ¥-encoded) | on disk pre-session |
| CT v1.3 §3.5.1 .tex | `siarc-relay-bridge/sessions/2026-05-08/T1-OPERATOR-CT-V13-3.5.1-OKAMOTO-RENAME-DERIVATION-105/section_3_5_1_okamoto_rename.tex` | bridge `0427c0a` | landed session 105 |
| KNY §8.5.17 substrate | `siarc-relay-bridge/sessions/2026-05-08/T2-OPERATOR-069R3-PRIORITY-1-S10-ROUTE-F-SUBSTRATE-CONSOLIDATION-126/route_f_substrate_paste_packet.md` | bridge `e18537e`; packet SHA16 `FAA5F083E2156A34` | landed session 126 |
| 069r3 final synthesis | `siarc-relay-bridge/sessions/2026-05-08/T1-SYNTH-069R3-FINAL-VERDICT-ABSORPTION-124/cascade_routing.md` | bridge `ae5b7f7` | landed session 124 |
| Q4 Round-1 verdict | `siarc-relay-bridge/sessions/2026-05-08/T1-SYNTH-Q4-ROUTE-F-VERDICT-ABSORPTION-129/verdict_packet.md` | bridge `ad33058` | landed session 129 |

---

**End packet.**

**Dispatch instructions for operator:** open a fresh Claude.ai T1-Synth web conversation (NOT the prior 069r2 thread or any 069r3 thread). Paste the body of this packet (§§1–12) as the conversation opener. Synth returns Q4 v2.0 verdict packet per §10.2. Agent absorbs at follow-on bridge session ≥131.
