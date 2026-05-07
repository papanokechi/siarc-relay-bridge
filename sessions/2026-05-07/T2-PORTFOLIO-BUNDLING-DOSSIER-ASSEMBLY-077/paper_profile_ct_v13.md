# Paper Profile [PROFILE-P3] — Channel Theory v1.3 (with v1.4 in-flight note)

**Session:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Compiled:** 2026-05-07
**Source SHA-256 (16) v1.3:** `59C5352795F8D63D` (TeX) / `DF3B90E808E49E84` (PDF)
**Path v1.3:** `siarc-relay-bridge/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/channel_theory_outline.tex` (70178 B, 1594 lines)
**Source SHA-256 (16) v1.4 in-flight:** `0600A4456803A43D` (TeX) / `4435BC0C2DDE4D78` (PDF)
**Path v1.4 in-flight:** `siarc-relay-bridge/sessions/2026-05-03/CT-V14-NARRATIVE-DRAFT/ct_v1.4_main.tex` (91605 B, 2050 lines)

---

## B.1 Record metadata (canonical: v1.3)

- **Title:** "Channel theory for polynomial continued fractions: asymptotic channels, the ξ_0 = 2/√β₂ identity, and a bridge conjecture" (verbatim L43-46; 17 words)
- **Concept DOI:** `10.5281/zenodo.19941678` (per `portfolio_inventory.md` L42)
- **Version DOI (v1.3):** `10.5281/zenodo.19972394`
- **Page count (PDF estimate):** ~17 pp typeset for v1.3 (1594 source lines AMS article); v1.4 in-flight ~21 pp (2050 source lines)
- **Primary arXiv category:** `math-ph` (per portfolio inventory L42: "math-ph (math.DS, math.NT)")
- **Cross-list categories:** `math.DS`, `math.NT`
- **Submission status:** v1.3 PUBLISHED on Zenodo; v1.4 in-flight NARRATIVE-DRAFT bridge session 2026-05-03; G17 layer-separation literature anchor referenced in 2026-05-04 G17-LAYER-SEPARATION-LIT-ANCHOR session
- **AEAL claim count (paper-internal):** v1.3 contains Proposition 4.x (`prop:xi0`) + Theorem `thm:vquad-cc` + Conjecture `conj:xi0-univ` + bridge conjecture revised + L_t no-go conjecture; ≥ 5 named claims; v1.4 adds in-flight CC channel functor narrative

## B.2 Mathematical-result spine (v1.3 canonical)

**80-word summary [verbatim from abstract L57-99, 49 words]:**
> "We propose, define, and catalogue asymptotic channels for sequences arising from polynomial continued fractions (PCFs). Each channel is a triple (D, T, S) specifying a formal-series space D, an asymptotic gauge T, and an analytic-continuation section S; three concrete channels appear in the SIARC stack."

**Key theorem labels (≤ 5 most-cited, verbatim labels only):**

- `prop:xi0` (Newton-polygon ξ_0 = 2/√β₂ at d=2; cited in V_quad recovery)
- `conj:xi0-univ` — "Cross-degree universality of ξ_0, c(d) = d" (L575)
- `thm:vquad-cc` — "V_quad CC-channel recovery" (L693)
- L_t no-go conjecture (L1072) — "L_t no-go for degree 2, Δ < 0"
- Bridge conjecture revised (L1107)

**Open conjectures or empirical claims (with AEAL-status):**

- ξ_0 = 2/√β₂ at d=2: TIER-1-CONFIRMED (Newton-polygon proof per CC-PIPELINE-G; verified at 200 dps)
- ξ_0 = d/β_d^{1/d} (Conjecture xi0-univ; v1.2 correction): TIER-2-EMPIRICAL (proven at d=2; verified d=4 spread 0; d=3 deferred to `op:xi0-d3-direct`)
- V_quad CC-channel recovery: TIER-2-EMPIRICAL ((i)+(ii) exact algebraic; (iii) "modulo Borel-Laplace summation of formal coefficient series"; Domb-Sykes residual diagnosed)
- L_t no-go for d=2 Δ<0: TIER-3-OPEN
- Bridge conjecture (B1/B2/B3 tier stratification; QL01 vs QL02 ξ_0 + ρ collision): TIER-2-EMPIRICAL

## B.3 Substrate dependency graph

**Cites (within the 6-record portfolio):**

- PCF-1 v1.3 — `siarc_pcf1_v13` (Stokes signal S(t)<1 on six Δ<0 families, V_quad → P_III(D_6) reduction)
- PCF-2 v1.3 — `siarc_pcf2_v13` (modular-discriminant axis at d=3)
- SIARC umbrella v2.0 — `siarc_umbrella_v2` (three-axis cross-degree invariant; channel functor χ : Σ → Channel)
- D2-NOTE v2.1 — implicit via `op:xi0-d3-direct` open problem and the Borel-singularity radius framing

**Cited by (within the 6-record portfolio):**

- D2-NOTE v2.1 §Setup L223 [Remark 5.E] cites `siarc_pcf1_v13` (out-of-scope marker) and §1 cites CT v1.3 as the source of the d=2 Newton-polygon argument that D2-NOTE makes self-contained
- SIARC umbrella v2.0 abstract L63: "Channel Theory v1.2 (a Borel-resurgence functor on the V_quad...)" (note: cite is to v1.2, not v1.3 — minor stale-cite drift surfaced in `discrepancy_log.json` D-077-3)
- PCF-1 v1.3 §6 V_quad section cross-references the CC channel
- PCF-2 v1.3 cubic-modular framing cross-references CT's ξ_0 axis

## B.4 Endorsement-fit summary

**[verbatim from `portfolio_inventory.md` row 4, 36 words]:**
> "Channel Theory v1.3 — Asymptotic Channels, the ξ₀ = 2/√β₂ Identity, and a Bridge Conjecture. math-ph (math.DS, math.NT). Zudilin H (math.NT cross). Mazzocco H (math-ph primary). Garoufalidis H (math.NT cross + Garoufalidis-Costin resurgence cite). Anomalies: none."

3 of 3 Tier-1 endorsers rated H (HIGH); Tier-2 candidates Costin
+ Sauzin both have CT v1.3 bibliography entries but arXiv handle
not publicly resolvable (per candidate dossier L73-95).

---

End of P3 profile.
