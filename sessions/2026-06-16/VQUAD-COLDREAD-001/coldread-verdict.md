# VQUAD-COLDREAD-001 — Cold read of the V_quad period-representation paper

**Object read:** `sessions/2026-06-16/VQUAD-REPRO-BUNDLE-001/vquad-periodrep-bundle/paper/vquad-periodrep-paper.tex`
(amsart, 1352 lines, ~23 pp; title "An explicit exponential-period representation of the V_quad
connection coefficient"; author Papanokechi + ORCID, no affiliation; date 15 June 2026).
PDF sibling SHA-256 `359d1172af3f…c702b` (pre-corrections, unchanged).

**Read scope:** full text — abstract, §1 Intro, §2 operators (L_φ/L_V, Galois, finite resurgence),
§3 cycle γ, §4 main identity, §5 three verifications (A/B/C), §6 Fresán–Jossen + conditional
transcendence, §7 Discussion, Appendices (coeffs, Kovacic cert, numerical logs, four-sign
convention, reproducibility), §References. Every page read; numerics independently re-checked
with mpmath (this slot, `constants-recheck` below).

---

## VERDICT: **A — publication-ready pending a small, well-defined set of correction items.**

Mapping to the `VQUAD-REVIEW-PREP-001/cold-read-checklist.md` three tiers:

- **A = publication-ready pending the open items** ✅ (this verdict)
- B = needs substantive revision — **NO** (no restructuring or re-derivation required)
- C = showstopper — **NO** (no mathematical error; transcendence properly doubly-conditional;
  every central object defined in-paper; CAS/SOTA section present)

The paper is genuinely strong. It is careful, exactly sourced (every claim → a probe slot, a
deposit DOI, or a named conjecture), honestly conditional, and it **pre-empts the AAECC/Lecerf
desk-reject lesson directly** with two explicit CAS sections (§1.4 and §7.5) plus a reproducibility
appendix. No correction item touches a graded mathematical result; all are presentation,
provenance, citation-completeness, or operator-fill items. Full list in `corrections-list.md`.

---

## Why not C (no showstoppers)

- **No mathematical error in the core identity.** The bridge is internally exact and
  cross-confirmed two independent ways inside the paper:
  - eq:C-from-A (L686): `C = |A|/|β| = K·Γ(1+β)/|β| = K·|Γ(β)|`, using `Γ(1+β)=βΓ(β)`, `β<0`,
    `Γ(β)<0` on (−1,0).
  - eq:main-recentred (L660): `C = (|Γ(β)|/2π)·S = (|Γ(β)|/2π)(2πK) = |Γ(β)|K`.
  Both give `C = |Γ(β)|K`; consistent. Re-verified numerically this slot (50 dps):
  `S = 2πK = 0.4579066231690176361190978…`, `C = |Γ(β)|K = 0.4377052861935372212307397…`,
  `|Γ(β)| = 6.0059917981814175262`, `C/S = |Γ(β)|/2π = 0.95588328284995364297` (exact bridge).
- **Transcendence is correctly DOUBLY conditional** (Cor 1.4 / Cor:transc, L174–181, proof
  L1006–1014): on (i) the Fresán–Jossen period conjecture (cite FJ, Conj 1.3.2) AND (ii) the
  named hypothesis **G-MOTGALOIS** (L993–999). Never collapsed to unconditional; Rmk:uncond
  (L1027–1037) explicitly separates what is unconditional (`C=|Γ(β)|K`, β irrational) from what
  is not. This is exactly the guardrail `open-items-decisions.md` mandates.
- **All central objects are defined in-paper** (the Lecerf-2 criterion): L_φ (Thm 2.4, full
  coefficients), L_V (Thm 2.7 + Appendix coefficients), γ (Def 3.2 + figure), β/ξ₀/K/S (§1.6 +
  eq:constants), C (eq:C-skeleton), the motive M (eq:Mmotive). The only citation-only framework
  is Fresán–Jossen itself — and even there the paper extracts and states the specific axioms it
  uses (C1/C2/C3, L624–629).

## The order-4-vs-order-2 question (flagged in prior context) — RESOLVED, not an issue

The abstract's "holonomic of order 4" (B̂) and "the order-2 operator annihilating the asymptotic
series" (L_φ) are **two different operators**, correctly: L_φ is order 2 / degree 4 on the z-side;
L_V is its Borel–Laplace dual, order 4 / degree 2 on the ξ-side (order↔degree exchanged). Table 2.6
(tab:config, L317–336) makes this explicit and the §2.4 duality (L364–378) derives it. No
inconsistency. (Optional LOW polish: one clause in the abstract could pre-empt the first-read
double-take — see corrections L-3.)

---

## Lecerf 4-criteria assessment (the AAECC/Item-40 desk-screen)

1. **Readability** — **STRONG.** Abstract is split; §1.5 gives a section-by-section roadmap; §1.6
   fixes notation/conventions before use; signposting throughout ("Method A fixes the ODE, B and C
   fix the value"). Directly answers Lecerf-1.
2. **Central objects defined (not citation-only)** — **STRONG.** See above. Answers Lecerf-2.
3. **Significance framed vs external SOTA** — **GOOD, one gap.** §7.3 (Ramanujan Machine /
   conservative matrix field) and §7.4 (placement among π, log2, ζ(3) vs Stokes/exponential
   periods) are well done. **Gap:** the single most directly competing SOTA for Painlevé Stokes
   constants — Eynard–Orantin **topological recursion** and the Iwaki–Marchal line — is absent.
   See corrections **M-3** (add Marchal et al. citations + one §7 sentence). This is the only
   place the paper under-delivers on Lecerf-3.
4. **CAS / state-of-the-art-algorithms comparison** — **STRONG (a headline strength).** §1.4
   ("What is and is not computer-algebra-automatable here") and §7.5 ("What computer algebra
   settles, and what it does not") explicitly delimit what gfun/ore_algebra/Kovacic/Borel–Padé
   settle vs the period-theoretic content that no CAS supplies, with the reproducibility appendix
   listing exact tools/versions. This is precisely the section whose absence sank the EBR-III
   AAECC submission (Item 40). **Lesson learned and applied.**

Net: 3 of 4 criteria strongly met; the 4th (significance/SOTA) is good with one fillable gap (M-3).

---

## Resolution of the six pre-identified open items (cold-read-checklist.md)

| # | Item | Status after read |
|---|------|-------------------|
| MED-1 | Sakai concept-DOI placeholder | **CONFIRMED present** — bibitem{Sakai} L1254: "[Concept DOI to be inserted by the operator at submission time.]". Operator hand-fill at deposit (→ corrections **M-4**). |
| MED-2 | 23 pp page count (don't pre-expand) | **HONORED.** No expansion proposed; corrections add ≤1 page total. Stays ≤30 pp. |
| MED-3 | G-MOTGALOIS strength for a flagship venue | **ADEQUATE as a *named conjectural* hypothesis** (the mandated stance). §6.2 period matrix (eq:periodmatrix) + Rmk:specialised make the surrounding argument as strong as possible without overclaiming. Kept conjectural per `open-items-decisions.md`. Minor optional tightening only (→ L-6). |
| LOW-1 | pseudonym / affiliation | **HANDLED:** `\author{Papanokechi}` + ORCID, no affiliation (matches the deposit-metadata "affiliation blank, byline carries ORCID only" convention). `\thanks` still says "working draft; not yet submitted" — update at submission (→ L-7). Operator decision; not blocking. |
| LOW-2 | b_m coefficient table | **SUFFICIENT.** eq:coeffstream (L247–255) tabulates a_n exactly in ℚ(√3) + decimals; b₀,b₁,b₂ given in text (L256); b_m = a_{m+1}/m! stated. No separate table needed. |
| LOW-3 | §5.3 numerical A spot-check | **PRESENT.** Method C extracts |A| = K·Γ(1+β) from large-order data (L854–862); numerical logs L1186–1191 give the 46-digit agreement and the Frobenius residual 1.6×10⁻⁴⁶. Adequate. |

All six are either confirmed handled, honored, or reduced to an operator hand-fill (M-4) — none is a
blocker, none reopens the mathematics.

---

## The one finding the checklist did NOT anticipate (top-priority)

**H-1 — provenance of `C = 0.4377052861935…`.** This headline value is *numerically identical* to
the value that was **publicly retracted** as the V_quad **Stokes constant** in the companion
Painlevé-V note (v1.0 → v1.1 correction: the v1.0 scripts used prefactor `Γ(βexp) = −6.00599`
instead of `2π`, giving `0.43770528`; corrected to `S = 2πK = 0.45790662`). The number
`6.00599 = |Γ(β)|` (verified this slot). The present paper is **mathematically correct** — C
(connection coefficient) and S (Stokes constant) are genuinely distinct, the |Γ(β)| prefactor is
*right* for C and *wrong* for S, and the whole paper is the bridge between them — but it **never
says so**, and cites the companion only at its corrected v1.2 (StokesNote, 20481592). A referee or
program reader who recalls `0.43770528` as "the retracted number" will stumble.

This is the single most important correction. It is also an **opportunity**: a one-paragraph remark
disambiguating C from the retracted Stokes value turns a credibility landmine into a demonstration
of the paper's core explanatory contribution (it *explains where the v1.0 error came from* — the
erroneous prefactor was computing the connection coefficient, not the Stokes constant). See
corrections **H-1**.

---

## Bottom line

**Verdict A.** Ship after working the `corrections-list.md` items — one HIGH (H-1 provenance
remark), four MED (terminology fix L804; topological-recursion/Marchal SOTA citations; Sakai DOI
fill; sibling-deposit cross-refs optional), and a few LOW polish items. No substantive revision, no
re-derivation, no showstopper. The corrections list is the input to **VQUAD-PAPER-CORRECTIONS-001**;
only after that does the PDF/metadata re-pin (**VQUAD-ZENODO-READY-001** re-run) and deposit proceed.
