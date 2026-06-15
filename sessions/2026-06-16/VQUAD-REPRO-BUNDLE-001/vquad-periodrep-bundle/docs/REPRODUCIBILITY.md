# REPRODUCIBILITY

Every computational claim in the paper is reproducible from the open scripts in
[`../scripts/`](../scripts/) against the reference outputs in
[`../data/`](../data/). No proprietary software is required (an optional Maple
cross-check is noted where relevant but never load-bearing).

**Setup.** Install the dependencies in [`DEPENDENCIES.md`](DEPENDENCIES.md)
(Python 3.12.x, `mpmath`, `sympy`, `numpy`). Run each script **from its own
directory** so sibling imports resolve; each writes its `*_results.json` next to
itself, which you compare against the matching file in [`../data/`](../data/).

Constants referenced below (certified, §A.3):

```
K       = 0.0728781025518669641294423633296525128045556892…   (58 digits)
S = 2πK = 0.457906623169017636119097842548225837962395135…
β       = −1/(3√3) = −0.19245008972987525…
ξ₀      = 2/√3     =  1.1547005383792517…
C       = |Γ(β)|·K = 0.437705286193537221230739749794369589981725597…
−(1+β)  = −1 + √3/9 = −0.80754991027…   (branch exponent at −ξ₀)
bridge:   S/C = 2π/|Γ(β)|   (residual 0, exact)
```

---

## Claim-by-claim

### 1. $L_\varphi$ algebraicity / exact recognition over $\mathbb{Q}(\sqrt3)$ — §2

- **Claim.** The $V_{\mathrm{quad}}$ coefficient stream is exact in
  $\mathbb{Q}(\sqrt3)$ and is annihilated by an order-2 operator $L_\varphi$
  (deg 4) with residual identically $0$.
- **Script.** `scripts/01-algebraicity/holonomic_recognition_q3.py`
- **Expected output.** `holonomic_recognition_q3_results.json`
  (`holonomic_found = true`); console reports `HOLONOMIC ODE FOUND`.
- **Run.** `cd scripts/01-algebraicity && python holonomic_recognition_q3.py`
  (~3–4 min).

### 2. $L_V$ holonomic structure over $\mathbb{Q}(\sqrt3)$ — §2

- **Claim.** The Borel transform $\widehat B$ is holonomic of order 4 (deg 2),
  $L_V$; both operators have coefficient field exactly $\mathbb{Q}(\sqrt3)$;
  operator residual $0$.
- **Script.** `scripts/01-algebraicity/extract_verify_operators.py`
  (after script 1).
- **Expected output.** `operator_verification_results.json`; console
  `coefficient field of both operators: Q(sqrt3)`.
- **Run.** `cd scripts/01-algebraicity && python extract_verify_operators.py`.

### 3. Singular locus and local exponents; branch $-(1+\beta)$ — §2 (prop. exponents)

- **Claim.** Singular locus $\{0,-\xi_0,\infty\}$; exponents at $0$ are
  $\{-1,0,1,2\}$; the local Borel exponent at $-\xi_0$ is $-(1+\beta)=-0.80755…$.
- **Script.** `scripts/01-algebraicity/indicial_analysis.py`.
- **Expected output.** `indicial_results.json`; console prints exponents
  `[-1, 0, 1, 2]` at $0$ and the $-(1+\beta)$ prediction at $-\xi_0$.
- **Run.** `cd scripts/01-algebraicity && python indicial_analysis.py`.

### 4. $L_\varphi$ differential Galois group $=\mathrm{SL}_2(\mathbb{C})$ (Kovacic) — §2 (thm. galois), §A.2

- **Claim.** Kovacic case-elimination (Cases 1–3 excluded) ⇒
  $\mathrm{Gal}(L_\varphi)=\mathrm{SL}_2(\mathbb{C})$.
- **Scripts.** `scripts/02-galois/stage2_kovacic.py` (console),
  `scripts/02-galois/stage2b_symsquare.py` (symmetric-square test).
- **Expected output.** `stage2_kovacic_results.json`; console reports the case
  eliminations and the $\mathrm{SL}_2$ verdict.
- **Run.** `cd scripts/02-galois && python stage2_kovacic.py && python stage2b_symsquare.py`.

### 5. $L_V$ Galois structure ($\mathbb{G}_m$ × Stokes structure) — §6

- **Claim.** A **structural** identification of the $L_V$ differential Galois
  group used to frame the Fresán–Jossen application (structural, not a full
  Picard–Vessiot computation — the paper states this scope explicitly).
- **Script.** `scripts/02-galois/stage3_galois_LV.py`.
- **Expected output.** `stage3_galois_LV_results.json`.
- **Run.** `cd scripts/02-galois && python stage3_galois_LV.py`.
- **Cross-check.** `stage3b_frobenius_v2.py` → `stage3b_frobenius_results.json`:
  Frobenius solution at $-\xi_0$ has **no logarithms**, residual
  $1.6\times10^{-46}$ (§A.3).

### 6. Method A — differential-equation / operator duality — §5.1, §A.4

- **Claim.** $M=h(z)\,L_\varphi$ **exactly**, with
  $h(z)=27(649+30\sqrt3)/\bigl(418501\,z^2(2\sqrt3-3)\bigr)$; survives a
  4-convention anti-fluke test (only the $e^{-\xi/z}$ kernel reproduces the
  exact factorisation).
- **Script.** `scripts/03-verification/stage4a_methodA_v2.py`.
- **Expected output.** `stage4_methodA_results.json` (exact factorisation
  confirmed; 4-convention test passes).
- **Run.** `cd scripts/03-verification && python stage4a_methodA_v2.py`.

### 7. Method B — Borel–Laplace contour deformation — §5.2

- **Claim.** The Hankel period equals $S\,e^{-\xi_0}$, relative error
  $8.84\times10^{-46}$.
- **Scripts.** `scripts/03-verification/stage4_methods.py` and
  `scripts/04-cycle/stage1_hankel_period.py`.
- **Expected output.** `stage4_methods_results.json`, `stage1_hankel_results.json`.
- **Run.** `cd scripts/04-cycle && python stage1_hankel_period.py`;
  `cd scripts/03-verification && python stage4_methods.py`.

### 8. Method C — Stokes-data / large-order — §5.3

- **Claim.** $|S_{\mathrm{mult}}|=2\pi K$ and $C=|A|/|\beta|$, relative error
  $9.31\times10^{-46}$.
- **Scripts.** `scripts/03-verification/stage4_methods.py`;
  large-order amplitude $A$ extracted in
  `scripts/01-algebraicity/borel_pade_census.py`.
- **Expected output.** `stage4_methods_results.json`, `borel_pade_results.json`.
- **Run.** `cd scripts/03-verification && python stage4_methods.py`.

### 9. 46-digit agreement of the three methods — §5

- **Claim.** Methods A, B, C agree on $C$ to **46 digits**.
- **Scripts.** the Method-A/B/C scripts above plus
  `scripts/03-verification/numcheck_period_rep.py` (the headline numerics).
- **Expected output.** `numcheck_period_rep_results.json`,
  `stage4_methods_results.json`.
- **Run.** `cd scripts/03-verification && python numcheck_period_rep.py`.

### 10. Finite resurgence (order-4 ⇒ finite connection) — §5.3

- **Claim.** Holonomicity of $\widehat B$ (order 4, finite singular locus
  $\{0,-\xi_0,\infty\}$) forces a **finite** resurgent structure — no infinite
  tower of singularities.
- **Script.** `scripts/01-algebraicity/borel_pade_census.py`.
- **Expected output.** `borel_pade_results.json`; console
  `… => NO infinite resurgent tower.`
- **Run.** `cd scripts/01-algebraicity && python borel_pade_census.py`.

### 11. The main identity $C=|\Gamma(\beta)|\,K=|A|/|\beta|$ — §4

- **Claim.** $C=|\Gamma(\beta)|K=0.437705286…$, and the bridge $S/C=2\pi/|\Gamma(\beta)|$
  holds with residual $0$.
- **Script.** `scripts/03-verification/numcheck_period_rep.py`.
- **Expected output.** `numcheck_period_rep_results.json` (contains $K,S,C,\beta,\xi_0$
  and the bridge residual).
- **Run.** `cd scripts/03-verification && python numcheck_period_rep.py`.

### 12. Operator residual sanity — §2

- **Claim.** The recognised operators annihilate the series to working
  precision (independent residual check).
- **Script.** `scripts/03-verification/stage0_residual_check.py` (imports the
  co-located support module `q3_foundation.py`).
- **Expected output.** `stage0_residual_results.json`.
- **Run.** `cd scripts/03-verification && python stage0_residual_check.py`.

---

## Conditional statement (not a computational claim)

The transcendence of $C$ over $\overline{\mathbb{Q}}$ (§6) is **conditional** on
(i) the Fresán–Jossen period conjecture for exponential motives and (ii) a
stated motivic-comparison hypothesis relating the differential and motivic
Galois groups of $L_V$. Neither is verified by any script in this bundle; both
are flagged as hypotheses in the paper. The open comparison question is the
subject of an inquiry to J. Fresán (see [`SIARC_PROVENANCE.md`](SIARC_PROVENANCE.md)).

## Byte-reproducibility of the PDF

See [`DEPENDENCIES.md`](DEPENDENCIES.md). `python paper/build.py` runs
`pdflatex` twice with `SOURCE_DATE_EPOCH` fixed and the reproducibility guards
in `preamble.tex`, producing a byte-identical PDF (target SHA-256 recorded in
the bundle's integrity-verification record).
