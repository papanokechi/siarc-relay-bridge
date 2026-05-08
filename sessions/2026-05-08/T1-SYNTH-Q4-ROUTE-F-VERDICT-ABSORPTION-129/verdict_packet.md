# Q4 Verdict Packet — Route F (Sakai/KNY surface-type machinery for V_quad)

## Dispatch metadata

- **Cascade:** 069r3 FINAL synthesis (prompt 112) — Q4 re-fire
- **Substrate:** bridge session 126 (T2-OPERATOR-069R3-PRIORITY-1-S10-ROUTE-F-SUBSTRATE-CONSOLIDATION-126), commit `e18537e`
- **Packet (input):** `route_f_substrate_paste_packet.md` (601 lines, SHA `FAA5F083E2156A34...`)
- **Synth thread:** FRESH Claude.ai T1-Synth conversation (NOT 069r2 thread; per `q4-packet-126-dispatch-clarification` carry-forward)
- **Synth model:** Claude Sonnet (4.5/4.6 class)
- **Dispatch composed by:** Copilot CLI (this session); 28.8 KB total payload (2.6 KB wrapper + 26.8 KB packet + closing tag)
- **Synth response received:** 2026-05-08 ~21:18 JST
- **Round-trip duration:** ~4 min from clipboard load to verdict receipt

## Machine-readable verdict

```
VERDICT_LABEL:           UNDECIDABLE_NEEDS_MORE_SUBSTRATE
CONFIDENCE_BAND:         high
ROUND_2_PASTE_SUFFICES:  no
NEW_ACQUISITION_REQUIRED: yes
PRIMARY_TARGET:          Okamoto 1987 (Studies on the Painleve equations, P_III) section 1
SECONDARY_TARGET:        Ohyama-Kawamuko-Sakai-Okamoto 2006 (Studies on the Painleve equations V; D_7^(1) and D_8^(1) types)
TERTIARY_TARGET:         KNY 2017 sections 8.5.1 through 8.5.16 (preceding the section 8.5.17 already on disk)
IN_HOUSE_LOOKUP:         CT v1.3 section 3.5 explicit definition of (alpha_inf, alpha_0, beta_inf, beta_0)
FALLBACK_PATH:           Jimbo-Miwa 1981 II (monodromy-data side; triangulation source if Okamoto 1987 unavailable in-cycle)
GOVERNANCE_PARALLEL:     M9 V0 amendment recommended in parallel (independent of Q4 outcome)
DERIVATION_ESTIMATE:     30-60 min synth work once acquisition complete
```

## Verbatim synth response

[BEGIN VERBATIM SYNTH RESPONSE]

````markdown
# Q4 Verdict — Route F (Sakai/KNY surface-type machinery for V_quad)

**Verdict: `UNDECIDABLE_NEEDS_MORE_SUBSTRATE`**

---

## Brief verdict statement

The substrate in packet §§D2–D5 is sufficient to *frame* the Q4 structural question — whether the V_quad image `(α_∞, α_0, β_∞, β_0) = (1/6, 0, 0, -1/2)` lands at an affine-Weyl fixed point of `W((2A_1)^{(1)})` or at a generic orbit point — but it is **not** sufficient to *answer* it. The two flagged unfaceted residuals (UF-126-PARAM-COUNT and UF-126-DELTA-DECOMP-FORM) are both load-bearing for the fixed-point classification, and resolving them requires substrate that is intentionally deferred per packet §D5 + prompt 113 §2 D5/§8 N1.

## Key reasoning chain

1. **Surface-type/Cremona triple is locked in.** §D2.2 (S1 §A.2.2) gives the table-row `(D_6^{(1)}, P_III^{D_6^{(1)}}, Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)}))`, and §D2.1 supplies the `(2A_1)^{(1)}` simple-root data with `δ = α_1+α_0 = α'_1+α'_0`. The Cremona-action vehicle for Route F mechanism (c) is therefore identified at the surface-type level — this part is *not* the obstruction.

2. **Reflection action on Sakai parameters is fully explicit.** §D3.3 (S1 §A.2.4) gives `r_0, r_1, r'_0, r'_1` acting on `(a_0, a_1, b_0, b_1)`, each preserving the **two** null-sum constraints `a_0+a_1=1` and `b_0+b_1=1`. §D3.4 gives `Aut(D_6^{(1)}) ≅ D_4` with explicit `(π, π', σ)` action. The full Cremona action on Sakai-side parameters is on the table.

3. **KNY-side Hamiltonian + discrete shift are also explicit.** §D4.2 (eq. 8.237) and §D4.5 (eq. 8.240, `T_α: (a_1, a_2) ↦ (a_1+1, a_2+1)`) give the discrete-flow vehicle in KNY's `(a_0, a_1, a_2)` convention with the level constraint `a_0+a_1+a_2=1` (§D4.6).

4. **The pull-back to Okamoto/CT coordinates is *explicitly deferred*.** §D5.1 cross-references but does not re-paste; §D5 header states: *"the explicit pull-back of the W((2A_1)^{(1)}) action onto Okamoto / CT coordinates `(η_∞, η_0, θ_∞, θ_0)` is **not derived here**; it is the structural derivation synth performs."* §D5.3 reiterates this is the structural question Q4 asks.

5. **UF-126-PARAM-COUNT is load-bearing.** §D4.6's "Convention reminder" surfaces a one-symbol mismatch: Sakai uses 4 symbols / 2 null-sum constraints (≡ 2 free parameters); KNY uses 3 symbols / 1 level constraint (≡ 2 free parameters). Free-parameter counts agree, *but* the symbol-level cross-walk between `(a_0, a_1, b_0, b_1)` and `(a_0, a_1, a_2)` is what determines which of the four reflections `r_0, r_1, r'_0, r'_1` even *act* on the Okamoto/CT 4-tuple `(α_∞, α_0, β_∞, β_0)` — and that map is the missing piece. The packet flags resolution as "the extra KNY symbol is the discrete-shift orbit index" but explicitly labels this as "navigation aid, not derivation" (§D4.6 final paragraph).

6. **UF-126-DELTA-DECOMP-FORM is the second load-bearing gap.** V_quad's null-sum violation `Δ = -1/3` (§D5.2, second quote) must be expressed in a form that the Sakai surface-type analysis can ingest. Three candidate decompositions are admissible *a priori*:
   - **Additive form:** `(α_∞ + α_0) + (β_∞ + β_0) = 1/6 + (-1/2) = -1/3`, distributing `Δ` into the two `A_1^{(1)}`-block null-sum violations as e.g. `(a_0+a_1-1) + (b_0+b_1-1) = -1/3` with a free split.
   - **Coefficient-rescaled form:** rescaling `(α_∞, α_0, β_∞, β_0)` by a uniform factor to land on the Okamoto null-sum locus, with a compensating `s`-rescaling on the Sakai EOM time variable (§D3.1, `ds/dt = 4 = 4(a_1+a_0) = 4(b_1+b_0)` ties the time variable to the level).
   - **Composite form:** a `T_α`-orbit shift (§D4.5) followed by a residual additive correction.

   Each form sends V_quad to a *different* point of the parameter space, hence to a *different* W-orbit. Without selecting the form, the fixed-point-vs-generic question is ill-posed.

7. **Why the watch-list resolves the verdict either way.** Per the packet's own watch-list discipline ("if either ambiguity is decisive for Q4, prefer UNDECIDABLE over forced GO/NO_GO"), and given that *both* UFs are decisive (UF-126-PARAM-COUNT controls which reflections touch which CT-coordinate; UF-126-DELTA-DECOMP-FORM controls which point of parameter space V_quad maps to), the disciplined verdict is UNDECIDABLE.

8. **Note on the Sakai EOM constraint and V_quad's `Δ = -1/3`.** §D3.1 states `ds/dt = 4(a_1+a_0) = 4(b_1+b_0)`, i.e. the Sakai EOM *requires* `a_0+a_1 = b_0+b_1 = 1` for the equations as written to hold; this is not just a normalisation choice. If the V_quad 4-tuple is mapped under additive-form decomposition with a non-trivial split (e.g. `a_0+a_1 = 1+ε`, `b_0+b_1 = 1+ε'` with `ε+ε' = -1/3`), the Sakai EOM coefficient `(a_1+b_1)` in `df/dt` is shifted off its canonical value — meaning V_quad's image may not even live on the canonical Sakai chart without prior rescaling. This is a structural concern (not just a book-keeping one) and reinforces that UF-126-DELTA-DECOMP-FORM is decisive.

## Branch recommendation (UNDECIDABLE follow-up)

**A Round 2 paste from packet §§3+5+6+7 (already on disk) would NOT suffice.** The substrate already pasted in this packet IS the §3+§5+§6+§7 priority material. The genuine gap is derivational, not substrate-acquisitional, but it has a hard prerequisite that is acquisitional:

**New material acquisition required — minimal additional substrate:**

1. **Primary need: explicit Okamoto ↔ KNY parameter-symbol formula** (not just the matching `(θ_0, θ_∞)_Okamoto ↔ (a_1, a_2)_KNY` "modulo convention shift" quoted at §D5.2, but the *closed-form expression for the shift itself*). Candidate sources, in priority order:
   - **Okamoto 1987** §1 (the original Hamiltonian definition; needed to pin down which `(η, θ)` symbol pairs with which `(q, p)` chart variable). This is the single most decisive missing item.
   - **Ohyama–Kawamuko–Sakai–Okamoto 2006** ("Studies on the Painlevé equations V: third Painlevé equations of types `D_7^{(1)}` and `D_8^{(1)}`") which contains the explicit Okamoto ↔ Sakai cross-walk for `D_6^{(1)}` as a baseline.
   - **KNY 2017 §8.5** preceding subsections (8.5.1–8.5.16) for the convention-fixing display that §8.5.17 inherits.

2. **Secondary need: CT v1.3 §3.5 explicit definition of `(α_∞, α_0, β_∞, β_0)`** — specifically, whether CT's 4-tuple is defined directly against Okamoto's `(η_∞, η_0, θ_∞, θ_0)` (in which case the null-sum violation `Δ = -1/3` is on Okamoto's side and UF-126-DELTA-DECOMP-FORM resolves additively) or against a Sakai-side parametrisation (in which case the violation is two-component and the decomposition form is genuinely free). The 058R §B.3 quote at §D5.2 implies the former but does not nail it down.

3. **If both above are acquired, the derivation is then structural-only** (~30–60 min of synth work): pull `r_0, r_1, r'_0, r'_1` and `T_α` through the cross-walk, evaluate at `(1/6, 0, 0, -1/2)`, check fixed-point conditions for each reflection.

**Path-delta-escalation as fallback:** if Okamoto 1987 cannot be acquired in-cycle, escalate to **Jimbo–Miwa 1981 II** (the monodromy-data side of the same correspondence) as a triangulation source — but this is strictly a fallback; the Okamoto/Sakai cross-walk via Okamoto 1987 is the cleaner path.

**Governance-parallel branch (M9 V0 amendment, ~45–90 min):** worth running *in parallel* with the literature acquisition, since the V_quad `Δ = -1/3` anomaly (058R §B.3 / discrepancy_log.json D2) is an unclosed residual from the 2026-05-02 partial session and benefits from independent governance-side documentation regardless of the Q4 outcome.

---

**Verdict label:**

```
UNDECIDABLE_NEEDS_MORE_SUBSTRATE
```

Confidence band: **high** (the watch-list flags + §D5 deferral + S4 §B.3 anomaly D2 status all point the same direction; the packet is internally consistent in stopping short of the structural derivation).
````

[END VERBATIM SYNTH RESPONSE]

## Branch action plan

### Tier 1 (NEW critical-path) — substrate acquisition for derivation prerequisite

1. **Primary acquisition prompt (115R)**: literature-acquisition + cross-check prompt covering:
   - Okamoto 1987 §1 (original Hamiltonian definition for P_III; pins `(η, θ)` ↔ `(q, p)` chart pairing) — PRIMARY TARGET
   - Ohyama–Kawamuko–Sakai–Okamoto 2006 (Painlevé V; explicit Okamoto ↔ Sakai cross-walk for `D_6^{(1)}` baseline) — SECONDARY
   - KNY 2017 §§8.5.1–8.5.16 (convention-fixing material preceding the §8.5.17 already on disk) — TERTIARY
   - In-house: CT v1.3 §3.5 explicit definition of `(α_∞, α_0, β_∞, β_0)` — IN-HOUSE LOOKUP (no external acquisition required)
   - Per Bibliographic identifier pre-verification rule (custom_instruction): each DOI / arXiv ID for Okamoto 1987 + Ohyama et al. 2006 must be pre-resolved before prompt fires
   - Estimated effort: ~2–4 hr Copilot Researcher session

### Tier 2 (parallel, anytime — INDEPENDENT of Q4 outcome)

2. **Prompt 118 (governance-parallel M9 V0 amendment)** — synth explicitly recommends running in parallel with literature acquisition; documents `Δ = -1/3` anomaly governance-side regardless of Q4 outcome. ~45–90 min.

3. **Prompt 117 (M4 V0 cascade closure batch)** — closes 5 SQL todos; ~1–2 hr.

### Tier 3 (deferred until 115R lands)

4. **Round 2 substrate packet composition** from acquired material + structural derivation prompt — fresh Claude.ai T1-Synth thread → Q4 verdict 2.0 → ~30–60 min synth work per synth's estimate.

### Tier 4 (gated on Q4 verdict 2.0)

5. **If Q4 v2.0 = GO_ROUTE_F** → fire Route F executor envelope (~8–20 hr novel framework)
6. **If Q4 v2.0 = NO_GO_ROUTE_F** → escalate per branch recommendation
7. **If Q4 v2.0 = PATH_DELTA_ESCALATION** → fire Jimbo–Miwa 1981 II acquisition (synth's named fallback)

## Carry-forward unfacedteds

- **UF-129-1**: Sakai EOM constraint (`a_0+a_1 = b_0+b_1 = 1`, ds/dt = 4) flagged by synth as structural prerequisite, not just normalisation. If V_quad's `Δ = -1/3` decomposes additively with non-trivial split, the Sakai EOM coefficient `(a_1+b_1)` in `df/dt` shifts off canonical value — V_quad's image may not live on canonical Sakai chart without prior rescaling. This is a NEW structural concern beyond UF-126 watch-list.
- **UF-129-2**: Ohyama–Kawamuko–Sakai–Okamoto 2006 named by synth as secondary acquisition target; not on existing literature_dossier (per session 126 §D6 references). Acquisition prompt should add to dossier.
- **UF-129-3**: CT v1.3 §3.5 explicit `(α, β)` definition status uncertain per synth: 058R §B.3 quote "implies the former [Okamoto-side] but does not nail it down." In-house lookup of CT v1.3 §3.5 source can resolve this without external acquisition.
- **Carry-forward from session 126**: UF-126-PARAM-COUNT and UF-126-DELTA-DECOMP-FORM both `LOAD_BEARING_CONFIRMED` per synth's reasoning chain items 5 and 6; status upgraded from `LOW_INFO_WATCH_LIST` to `BLOCKING_PREREQUISITE`.
