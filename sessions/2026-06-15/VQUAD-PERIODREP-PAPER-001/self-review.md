# Stage 4 — Self-review (Compositio-referee pass + Lecerf four criteria)

Paper: `An explicit exponential-period representation of the V_quad connection coefficient`
Build: 23 pages, 0 LaTeX errors, 0 undefined references, 0 uncited bibitems (19/19 cited).
Reviewer stance: simulated Compositio/AAECC referee. Scope: bugs, missing
justification, conditionality leaks, undefined-before-use, readability.

---

## A. Lecerf's four criteria (from the AAECC desk-reject lesson, Item 40)

**Obj. 1 — Is the paper readable?**  PASS (with note).
- Roadmap present (§1 "Organisation"); a dedicated "Notation and conventions"
  subsection (§1) fixes vocabulary before use; every verification has an
  intro sentence stating what it proves and what input it uses (§5 opener +
  §5.1 "Strategy: why three methods, and why they are independent").
- Longest rendered paragraphs are ≤ ~14 lines (source files are hard-wrapped,
  so raw line counts overstate). No paragraph exceeds the 15-line guide in the
  PDF; no sentence exceeds 4 rendered lines.
- NOTE (LOW): §5.1 (Method A) and §2 (Borel construction) are dense by nature
  (worked operator-duality derivations). Judged acceptable for a "three
  verifications" section; not split further to avoid fragmenting the argument.

**Obj. 2 — Are central objects defined before use?**  PASS.
- C, β, ξ₀, K, S defined in §1.1 (eq:C-skeleton, eq:beta, eq:bridge) before any use.
- B̂ defined in §1.3; γ used in §1.3 with an explicit forward pointer to
  Definition~\ref{def:gamma} (§3); L_φ, L_V stated in §1.3 with forward pointer
  to Thm~\ref{thm:LV} and fully defined in §2.
- The exponential motive M = (X, f, ω) is written explicitly in §1 (cor:transc),
  §3 (eq:Mmotive) and §6 (prop:expperiod). G-MOTGALOIS is a displayed, named
  hypothesis (§6). No object is used before a definition or an explicit pointer.

**Obj. 3 — Is the significance framed beyond the program itself?**  PASS.
- §1 has a standalone "significance is not confined to the program" paragraph
  (Kontsevich–Zagier / Grothendieck period philosophy; scarcity of explicit
  realisations of *divergent*-series constants; Ramanujan-Machine pipeline).
- §7 "Comparison with established period constants" positions C against
  π, log2, ζ(3) (ordinary periods) vs Γ(s), Airy/Bessel connection constants
  (exponential periods). The paper does not assume the reader cares about the
  Sakai program: "All objects used below are defined in-paper" (§1).

**Obj. 4 — Is the CAS / SOTA context addressed?**  PASS.
- §1 "What is and is not computer-algebra-automatable here": names gfun,
  ore_algebra (holonomic guessing), Kovacic's algorithm, Maple
  DEtools[DifferentialGaloisGroup], Borel–Padé; states explicitly what is *not*
  automatable (cycle identification, three-route agreement, motivic
  interpretation).
- §7 "What computer algebra settles, and what it does not" and §A.5
  reproducibility statement reinforce the boundary. Even though this is not a
  CAS paper, the comparison the AAECC EiC asked for is present.

---

## B. Referee findings by section (severity: HIGH applied; MED/LOW deferred)

| # | Sev | Location | Finding | Disposition |
|---|-----|----------|---------|-------------|
| 1 | HIGH | §4 (eq:constants area) | Text called Γ(β) "the only **transcendental** constant", asserting unconditional transcendence of a Γ-value at an algebraic-irrational argument — contradicts §6 rmk:uncond which (correctly) says this is only conditionally known. | **FIXED**: reworded to "the only **non-algebraic** factor". |
| 2 | HIGH | §9 references | 4 relevant bibitems uncited (Hien, SakaiClass, Écalle, Loday-Richaud) — a referee flags unused references and the corresponding claims were under-sourced. | **FIXED**: cited SakaiClass (§1 surface classification), Hien (§3 rapid-decay homology), Écalle (§2 alien tower), Loday-Richaud (§5 lateral/median Borel sums). 19/19 now cited. |
| 3 | MED | §9, bibitem `Sakai` | Parent Sakai-stratification deposit **concept DOI is unknown in the corpus** ("[Concept DOI to be inserted by the operator at submission time.]"). | **DEFER to operator**: must insert the real Zenodo concept DOI before any deposit/submission. Flagged here and in ledger.json open-items. |
| 4 | MED | global | Page count **23** sits just above the 22 floor, at the **lower end** of the 25–30 target band. All content is genuine/sourced; the remaining gap is amsart typesetting density, not missing content. Further word-count expansion was declined as padding (would harm Obj. 1). | **DEFER to operator**: accept 23pp, or request specific additional content (e.g., explicit L_φ/L_V coefficient walk-through moved into body, full Frobenius indicial display). Not auto-expanded per AEAL/no-pad discipline. |
| 5 | MED | §6 (G-MOTGALOIS) | The motivic-comparison hypothesis is explicit and boxed, but the *evidence* for G_V ≅ relevant quotient of G_mot(M) is heuristic (de Rham realisation + Tannakian formalism). A motives referee may want Nori/Ayoub specifics. | **DEFER**: acknowledged in §6 as a "conjectural bridge"; this is the honest state (the probe did not close it). Do **not** overclaim. |
| 6 | LOW | §1 thanks / author block | Pseudonymous author "Papanokechi", no affiliation. Some venues (Springer) require legal names. | **DEFER to VENUE-RELAY** (out of scope for this draft per task; do not anonymize or alter here). |
| 7 | LOW | §2 eq:coeffstream | First a_n / b_m table is exact in ℚ(√3) and reproducible (holonomic_recognition_q3.py); b_2 given inline. Could tabulate b_m fully, but the point (exactness) is made. | Keep as is. |
| 8 | LOW | §5.3 Method C | "amplitude A extracted from large-order data" leans on Borel–Padé acceleration (borel_pade_census.py) — numerically robust but not exact. Clearly labelled as a 46-digit numerical extraction, not an exact identity. | Keep; correctly hedged. |

---

## C. Conditionality audit (must never leak to unconditional)

Every transcendence statement checked (grep `transcend*`):
- Abstract: "**conditional on** the Fresán–Jossen period conjecture … **and on** a
  stated motivic-comparison hypothesis, C is transcendental over Q̄." ✓ both layers.
- §1 cor:transc: "Assume (i) … (ii) … Then C is transcendental over Q̄." ✓
- §6 proof of cor:transc + rmk:specialised + rmk:uncond: both layers named;
  rmk:uncond explicitly refuses to collapse to unconditional. ✓
- §7: "(conditionally) transcendental". ✓
- §4 (after fix #1): no unconditional transcendence assertion remains. ✓

G-MOTGALOIS acknowledgment in §6: PRESENT (displayed hypothesis box) — task
DO-NOT satisfied.

---

## D. Forward-reference / dangling-object audit

- 72 distinct labels; **0 undefined references** in the build log.
- All forward references (γ→def:gamma, L_V→thm:LV, motive M→eq:Mmotive,
  G-MOTGALOIS→§6) carry an explicit pointer at first mention.

---

## E. Net result

- HIGH-severity issues: 2 found, **2 fixed** (rebuilt clean: 23pp / 0 err / 0 undef / 19-19 cited).
- MED/LOW issues: 6 deferred to operator review (items 3–8 above).
- The paper satisfies all four Lecerf criteria and keeps the transcendence
  corollary doubly-conditional throughout.

**Open items for operator review: 6** (items 3–8; the two HIGH items are already fixed).
