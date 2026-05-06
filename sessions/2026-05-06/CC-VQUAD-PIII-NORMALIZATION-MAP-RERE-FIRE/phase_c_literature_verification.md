# Phase C — Literature anchoring (5 verbatim anchors)

**Session:** 058R CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE
**Phase C signal:** **C_LITERATURE_UNIFORM** (5/5 anchors uniform; 1
substantive structural reconciliation in B.5).
**Method:** SHA-verified literature anchors + verbatim ≤30-word quotes.

---

## C.0 — SHA verification of 6 anchor PDFs (Phase C.0 gate)

Per 057 `slot_sha_verification.md` (bridge `9d6e801`) and 058R STEP 1
re-verification:

| slot | filename | spec prefix | live (058R re-hash) | result |
|------|----------|-------------|---------------------|--------|
| 01   | 01_birkhoff_1930_acta54.pdf                            | aeb5291e | aeb5291e | PASS |
| 03   | 03_birkhoff_trjitzinsky_1933_acta60.pdf                | dcd7e3c6 | dcd7e3c6 | PASS |
| 04   | 04_wasow_1965_dover.pdf                                | f59d6835 | f59d6835 | PASS |
| 06   | 06_costin_2008_chap5.pdf                               | 436c6c11 | 436c6c11 | PASS |
| 07   | 07_okamoto_1987_painleve_III_FE30.pdf                  | 65294fbc | 65294fbc | PASS |
| 08   | 08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf  | 96c49cdd | 96c49cdd | PASS |

**6/6 PASS.** No `HALT_M6_LITERATURE_NOT_LANDED` triggered. (Also
4/4 auxiliary slots Sakai 1999 / KNY 2017 / NY 1998 / NY 2000 PASS,
re-verified via SHA256SUMS.txt; confirmed PASS 16/16 total — see 057
slot_sha_verification.md §A-§E.)

---

## C.1 — Okamoto 1987 §1.1 (PRIMARY Lax / Hamiltonian anchor)

**Reference.** Okamoto, K. "Studies on the Painlevé equations IV. Third
Painlevé equation $P_{III}$." Funkcialaj Ekvacioj **30** (1987), 305–332.

**Page anchor.** §1.1 Introduction p. 306 (PDF text-extract
07_okamoto_1987_painleve_III_FE30.txt L185–189 of 2386).

**Theorem/equation reference.** Eq. (0.1) defining $H_{III}$.

**Verbatim quote (≤30 words):**

> *"The Hamiltonian associated with $P_{III}$ is
> $H_{III} = \tfrac{1}{t}\bigl[2 q^{2} p^{2} - \{2 \eta_{\infty} t q^{2} + (2\theta_{0} + 1) q - 2\eta_{0} t\} p + \eta_{\infty}(\theta_{0}+\theta_{\infty}) t q\bigr]$,
> where the constants $\eta_{\Delta}$, $\theta_{\Delta}$ ($\Delta = 0, \infty$) are connected to $\alpha, \beta, \gamma, \delta$ of the equation."*

**Use:** Phase B.1 H_III canonical Hamiltonian + Phase B.3 Φ_symp
identification. The verbatim formula matches Phase B's expression
modulo the substitution $\eta_{0} = \eta_{\infty} = 1$ (Okamoto p. 306
"By the assumption ... we set $\eta_{\Delta} = 1$ without loss of
generality").

**Related:** Okamoto §2.1 (W(B_2) generators) extracted verbatim in
Phase B.5.1 (page 318 anchor; the Lax pair itself is NOT in Okamoto
1987, surfaced as anomaly D4 — see B.5/Phase D).

---

## C.2 — Barhoumi-Lisovyy-Miller-Prokhorov 2024 §4 / Definition 1.3 (PRIMARY monodromy data anchor)

**Reference.** Barhoumi, A., Lisovyy, O., Miller, P.D., Prokhorov, A.
"Painlevé-III Monodromy Maps Under the $D_{6} \to D_{8}$ Confluence
and Applications to the Large-Parameter Asymptotics of Rational
Solutions." SIGMA **20** (2024), 019 (77 pp). arXiv:2307.11217;
DOI 10.3842/SIGMA.2024.019.

**Page anchor.** §1.3 Cubic surface and monodromy parametrization
(p. 5–6 of preprint; text-extract 08_blmp_2024.txt L411–425).

**Theorem/equation reference.** Eq. (1.16) + Definition 1.3.

**Verbatim quote (≤30 words):**

> *"$e_{1}^{2}, e_{1}^{-2}$ are eigenvalues of a certain monodromy
> matrix for a circuit about the origin ... The parameter $e_{2}$
> appears in the connection matrix for the same system. We call
> $(e_{1}, e_{2})$ monodromy parameters."*

**Numerical Stokes-data note.** BLMP 2024 provides the **structural**
parametrisation of the canonical $P_{III}(D_{6})$ monodromy manifold
(cubic surface eq. 1.13) via $(e_{1}, e_{2}) \in (\mathbb{C}^{*})^{2}$
with parametrisation $e_{1} = e^{i\pi\mu},\ e_{2} = e^{i\pi\eta}$
(eq. 1.16). It does **not** provide a numerical Stokes constant
table for the V_quad parameter point (which corresponds to a
specific non-rational $(\mu, \eta)$ value); see Phase D.2 for the
deferred numerical cross-check.

**Use:** Phase D.2 deferred numerical cross-check identification
target. The Stokes constant $S_{\zeta_{*}}^{\mathrm{can}}$ in
canonical normalisation is expressible in terms of $(e_{1}, e_{2})$
via the standard isomonodromy connection-matrix formula (BLMP
2024 §4 eq. 4.28 + §1.4 (monodromy manifold)).

---

## C.3 — Costin 2008 ch. 5 §5.4 Theorem 5.26 (Stokes-phenomenon framing)

**Reference.** Costin, O. "Asymptotics and Borel summability." CRC
Press Monographs **141** (2008). Ch. 5 "Borel summability in PDEs and
ODEs."

**Page anchor.** Theorem 5.26 (p. 156 of book, text-extract
06_costin_2008_chap5.txt L7996–8005).

**Theorem/equation reference.** Theorem 5.26.

**Verbatim quote (≤30 words):**

> *"Theorem 5.26: Let $\gamma_{\pm}$ be two paths in the right half
> plane, near the positive/negative imaginary axis ... Then
> $y = (C \pm \tfrac{1}{2} S_{1}) e_{1} x^{-\beta_{1}+1} e^{-x \lambda_{1}}(1 + o(1))$ for large $x$ along $\gamma_{\pm}$."*

**Use:** Phase A's resurgent ansatz framework + Phase D.1 signal
aggregation. Costin 2008 Theorem 5.26 expresses the Stokes
phenomenon as the **C-jump across a Stokes line** with $S_{1}$ the
leading Stokes constant (the same role $S_{\zeta_{*}}$ plays in
H4's measurement). This is the SCENARIO_C substitute for
Conte–Musette ch. 7 §7.4 (per A-01 verdict + 057 STEP 4
substitution chain).

---

## C.4 — Birkhoff-Trjitzinsky 1933 §§4–6 (Borel summability — carry-forward)

**Reference.** Birkhoff, G.D. and Trjitzinsky, W.J. "Analytic theory
of singular difference equations." Acta Math. **60** (1933), 1–89.

**Page anchor + use.** §§4–6 (Borel-summability machinery, pp.
21–48). Already extracted verbatim in **D2-NOTE v2.1** §3 reference
list (Zenodo 10.5281/zenodo.20015923, PDF SHA prefix `a8b6026a`); 058R
**carry-forward citation** per spec C.4.

**Carry-forward sentence (≤30 words):**

> *"The Borel-plane existence machinery of B-T 1933 §§4–6 underpins
> Phase A's β = 0 logarithmic Borel branch at $\zeta_{*} = 4/\sqrt{3}$,
> as recorded in D2-NOTE v2.1 universality result."*

**Use:** Phase A's resurgent ansatz Borel-plane existence; Phase D.1
signal aggregation.

---

## C.5 — Wasow 1965 §19 Theorem 19.1 (sectorial asymptotic existence — carry-forward)

**Reference.** Wasow, W. "Asymptotic Expansions for Ordinary
Differential Equations." Dover (1965/1987 reprint).

**Page anchor + use.** §19 Theorem 19.1, eq. (19.3) (sectorial
existence of asymptotic solutions at irregular singular points).
Already extracted verbatim in **D2-NOTE v2.1** §3 reference list +
T1 Phase 1/2 dossier (CLAUDE.md anchor); 058R **carry-forward
citation** per spec C.5.

**Carry-forward sentence (≤30 words):**

> *"Wasow 1965 §19 Theorem 19.1's sector-by-sector asymptotic
> existence supports Phase B's normalisation map M acting compatibly
> with V_quad's two formal sectors $f_{\pm}(u)$ at $u = 0$."*

**Use:** Phase B's sectorial structure (M respects the two formal
sectors, by construction of Φ_resc + Φ_shift); Phase D.1 signal
aggregation.

---

## Phase C cross-reading uniformity check

| anchor | Phase A use | Phase B use | Phase B.5 use | Phase D use |
|--------|-------------|-------------|---------------|-------------|
| C.1 Okamoto 1987 §1.1   | (—)              | H_III source     | s_i generators | (—) |
| C.2 BLMP 2024 §4        | (—)              | (—)              | monodromy framing | D.2 target |
| C.3 Costin 2008 §5.4    | resurgent ansatz | (—)              | (—)              | D.1 framing |
| C.4 B-T 1933 §§4–6      | β = 0 Borel      | (—)              | (—)              | D.1 framing |
| C.5 Wasow 1965 §19      | sectorial        | sectorial        | (—)              | D.1 framing |

No anchor contradicts another. No anchor contradicts H4's measurement
(β = 0; |C| = 8.127336795...). Phase B.5's substantive
**framing reconciliation** (spec's "W(D_6)" → literature's
"surface-type $D_{6}^{(1)}$ + symmetry-type $(2 A_{1})^{(1)}$") is a
notational, not numerical, correction; surfaced as anomaly D3.

**No HALT_M6_LITERATURE_DISAGREES_WITH_H4 triggered.**

---

## Phase C verdict

- **C.0 PASS:** all 6 spec §1 anchor PDFs SHA-verified (16/16 with
  auxiliary slots).
- **C.1 PASS:** Okamoto 1987 §1.1 H_III formula extracted verbatim.
- **C.2 PASS:** BLMP 2024 §4 / Definition 1.3 monodromy parametrisation
  extracted verbatim; numerical Stokes constants for V_quad parameter
  point not provided (deferred D.2).
- **C.3 PASS:** Costin 2008 ch. 5 Theorem 5.26 Stokes-phenomenon
  framing extracted verbatim.
- **C.4 PASS:** Birkhoff-Trjitzinsky 1933 §§4–6 carry-forward citation
  via D2-NOTE v2.1.
- **C.5 PASS:** Wasow 1965 §19 carry-forward citation via D2-NOTE v2.1.

**Signal: C_LITERATURE_UNIFORM** — no
HALT_M6_LITERATURE_DISAGREES_WITH_H4. The 5 anchors uniform with
Phases A + B + B.5; M is well-anchored modulo the **deferred Φ_symp
Jacobian numerical computation** (Phase D.2).
