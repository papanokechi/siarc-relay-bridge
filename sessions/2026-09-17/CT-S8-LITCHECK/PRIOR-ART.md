# PRIOR-ART.md — literature check for the polynomial-`b(n)` Wallis-denominator growth law

Session: `CT-S8-LITCHECK` · Repo HEAD at start: `08aa0e2381b3dc37ee54a3200b7272755ca11d59`
Retrieval date for all sources below: **2026-09-17**.

## 0. The object under test

For a polynomial `b(n) = sum_{k=0}^d beta_k n^k`, `d >= 1`, `beta_d != 0`, `b(n) != 0` for `n >= 1`:

```
Q_n = b(n) Q_{n-1} + Q_{n-2},   Q_{-1} = 0, Q_0 = 1.
```

(H): `r_inf = lim_n Q_n / prod_{k<=n} b(k)` exists and is nonzero.

- **R1** (radius/root): `lim |Q_n/(dn)!|^{1/n} = |beta_d|/d^d`; Borel-type transform `sum Q_n w^n/(dn)!` has radius `d^d/|beta_d|`.
- **R2** (growth law): `Q_n/Gamma(dn+1) = K (beta_d/d^d)^n n^s (1+O(1/n))`, `s = beta_{d-1}/beta_d + (d-1)/2`.
- **R3** (amplitude): explicit closed-form `K` in terms of `r_inf` and Gamma values at the roots `r_i` of `b`.
- **B** (Borel framing).

**Independent numerical confirmation of R1/R2/R3 (VERIFIED, computation).**
Script `scripts/verify_growth_law.py` (mpmath, 60 dps, N = 4000), output
`scripts/verify_growth_law.out` (sha256 `c910f7a6262529bb8c2307336d37e5549b0e0f195da3665691c0ef6c5d39f067`).
It reproduces R1 and R2 and confirms the specific closed form

```
K = r_inf * (2*pi)^((d-1)/2) / ( sqrt(d) * prod_i Gamma(1 - r_i) )
```

for `b(n) = 2n+3` (d=1), `n^2+1` (d=2, complex roots), `2n^2+n` (d=2), `n^3+n^2+n+2` (d=3);
`K_numeric/K_closed_form` = 1.00047, 0.99978, 1.00013, 1.000056 respectively, i.e. agreeing to
`O(1/N)` as the stated `1+O(1/n)` predicts. This `K` specialises to `r_inf/Gamma(1-r)` at `d=1`
and has prefactor `(2*pi)^{1/2}/sqrt(2) = sqrt(pi)` at `d=2`, matching the note's sanity checks.

---

## 1. Verdict table

| Result | Status | Precise citation, with quote |
|---|---|---|
| **R1** — `lim (Q_{n+1}/Q_n)/n^d = beta_d`, hence `lim|Q_n/(dn)!|^{1/n} = |beta_d|/d^d` | **PRIOR ART (immediate corollary of a classical theorem)** | **Perron–Kreuser theorem**, as stated in Gautschi (1967), Theorem 2.3(a), *SIAM Review* 9(1), p. 35. Verbatim (read off the page scan `refs/g1967_p35_mid.png`): "THEOREM 2.3 (Perron [42], Kreuser [29]). (a) *If the point* `P_1` *is above the line segment* `P_0 P_2` *(i.e.,* `sigma > tau`*), the difference equation* (2.1) *has two linearly independent solutions,* `y_{n,1}` *and* `y_{n,2}`*, for which* (2.9) `y_{n+1,1}/y_{n,1} ~ -a n^sigma`, `y_{n+1,2}/y_{n,2} ~ -(b/a) n^tau`, `n -> inf`." Hypotheses (p. 34, eq. (2.8)): "`a_n ~ a n^alpha`, `b_n ~ b n^beta`, `ab != 0`; `alpha, beta` real; `n -> inf`", with `y_{n+1} + a_n y_n + b_n y_{n-1} = 0` (eq. (2.1), p. 34) and the Newton–Puiseux diagram on `P_0(0,0), P_1(1,alpha), P_2(2,beta)`. **Application to our case:** write the recurrence as `Q_{n+1} - b(n+1) Q_n - Q_{n-1} = 0`, so `a_n = -b(n+1) ~ -beta_d n^d`, `b_n = -1`; thus `alpha = d`, `beta = 0`, `a = -beta_d`, `b = -1`; `P_1 = (1,d)` lies above `P_0P_2` (the x-axis) because `d >= 1`; `sigma = d`, `tau = -d`. Case (a) then gives `Q_{n+1}/Q_n ~ beta_d n^d` for the dominant solution and `~ -(1/beta_d) n^{-d}` for the minimal one. R1 follows by Stirling + Cesàro. **INSPECTED.** |
| **R2** — full growth law **with the explicit exponent** `s = beta_{d-1}/beta_d + (d-1)/2` | **PARTIAL (shape is classical; the explicit coefficient formula for `s` was NOT FOUND in any source I obtained)** | (i) *Shape:* Birkhoff–Trjitzinsky (1933), *Acta Math.* **60**, 1–89 ("Fundamental Theorem", §9, p. 69: "Every equation `L_n(y) = 0` (or system), with coefficients of the kind specified in §1 and known in the complete neighborhood of infinity, is completely proper in each of the several quadrants associated with the equation (or system).") establishes existence of actual solutions asymptotic to formal "normal" solutions built from `e^{Q(x)} x^{rx} rho^x x^s Σ`. This gives *existence and shape*, not a closed formula for `s` in terms of `beta_k`. **INSPECTED** (`refs/bt1933.pdf`, p. 69). (ii) *Explicit second-order machinery:* DLMF §2.9(i)–(ii) gives `w_j(n) ~ rho_j^n n^{alpha_j} Σ a_{s,j} n^{-s}` with the exponent **explicitly** `alpha_j = (f_1 rho_j + g_1)/(f_0 rho_j + 2 g_0)` (DLMF 2.9.6) — **but only for the bounded-coefficient case** `f(n) ~ Σ f_s/n^s`, `g(n) ~ Σ g_s/n^s`, `g_0 != 0`, which our equation violates (our `f(n) = -b(n+2)` grows like `n^d`). DLMF explicitly defers the growing case: "For analogous results for difference equations of the form (2.9.14) `w(n+2) + n^P f(n) w(n+1) + n^Q g(n) w(n) = 0` in which `P` and `Q` are any integers see Wong and Li (1992a)." (DLMF §2.9(ii), retrieved 2026-09-17). **INSPECTED.** (iii) The pointer target, **Wong & Li (1992a), "Asymptotic expansions for second-order linear difference equations. II", *Stud. Appl. Math.* 87(4), 289–324**, is the exact classical reference for our equation class — **PAYWALLED, not obtained** (Wiley returned HTTP 403). I therefore **cannot** say whether it prints `s` in closed form in terms of `beta_k`; see §4. |
| **R3** — explicit closed-form amplitude `K` | **NOT FOUND (in the sources I obtained), and there is positive evidence that classical methods do not supply it** | Classical difference-equation asymptotics fixes solutions only up to a multiplicative constant; the constant relating a *given* solution (here `Q_n`, fixed by `Q_{-1}=0, Q_0=1`) to the normalised formal solutions is a *connection coefficient*. Nemes (2026), arXiv:2508.15246v2, states this plainly — Abstract: "It also allows for the computation of problem-specific invariants, such as Stokes multipliers, whose values are often assumed or remain unknown in other approaches." and §1, p. 3: "hyperasymptotics enabled the numerical computation of Stokes multipliers (or connection coefficients)—often treated as unknowns in other methods—with arbitrary precision." **INSPECTED** (`refs/nemes2025.pdf`, abstract p. 1 and introduction p. 3). Note that even Nemes only offers *numerical* computation of connection coefficients, not a closed form. No source I obtained gives a closed-form amplitude for this recurrence. **NOT FOUND** in: Gautschi (1967) full text; DLMF §2.9 and §3.6 full text; Birkhoff–Trjitzinsky (1933) full text; Nemes (2026) full text; Wang (2014) full text — by ligature-normalised full-text search. |
| **B** — Borel-transform framing | **PARTIAL: Borel machinery for difference equations is well established; the particular `sum Q_n w^n/(dn)!` radius statement was NOT FOUND** | Borel/Mellin–Borel transforms are a standard modern tool for exactly this class of problem. Nemes (2026), arXiv:2508.15246v2, Abstract: "Our main tool is the Mellin–Borel transform."; §1, p. 2: "Immink [16] showed that each formal series in (1.3) is Borel summable, and that its Borel transform (inverse Laplace transform) possesses infinitely many singularities in the complex Borel plane." Keywords of that paper include "Borel transform". **INSPECTED** (`refs/nemes2025.pdf`, pp. 1–2). **However**, Nemes's standing hypothesis is an *irregular singularity of rank one* — "`f_k(z)` are polynomials of degree at most `n-k`, and `f_0(z)` has degree exactly `n`" (p. 1, eq. (1.1)–(1.2)) — which our equation does **not** satisfy for `d >= 2` (we have order `n = 2`, `deg f_1 = d`, `deg f_0 = 0`). So that framework does not contain our statement. I did **not find**, in any obtained source, the specific statement that `sum Q_n w^n/Gamma(dn+1)` has radius `d^d/|beta_d|`. **NOT FOUND** in: Gautschi (1967), DLMF §2.9/§3.6, Birkhoff–Trjitzinsky (1933), Nemes (2026), Wang (2014), by full-text search for `Borel`, `radius of convergence`, `Gevrey`. |
| **(H)** — nonvanishing of `r_inf` as a Pincherle/minimality condition | **PRIOR ART (framework), classical** | Gautschi (1967), Theorem 1.1, p. 31: "THEOREM 1.1 (Pincherle [45]). *The continued fraction* (1.14) *converges if and only if the recurrence relation* (1.11) *possesses a minimal solution* `f_n` *with* `f_0 != 0`." And p. 35, immediately after Theorem 2.3: "An argument similar to the one following Theorem 2.2 will show that in both case (a) and the first part of case (b) the solution `f_n = y_{n,2}` is a minimal solution of (2.1)." So under Perron–Kreuser case (a), `Q_n` is *dominant*; (H) is exactly the statement that `Q_n` is not (a multiple of) the minimal solution. **INSPECTED** (`refs/gautschi1967.txt`, extracted from p. 31 and p. 35). DLMF §3.6(ii) gives the same dichotomy: "Then `w_n` is said to be a recessive (equivalently, minimal or distinguished) solution as `n -> infinity`, and it is unique except for a constant factor." **INSPECTED.** |

### Body-by-body summary requested by the operator

| Body of work | R1? | R2 (explicit `s`)? | R3 (`K`)? | Borel? | Evidence status |
|---|---|---|---|---|---|
| **Poincaré (1885) / Perron (1909)** — constant-limit coefficients | No (hypotheses fail: our `a_n` is unbounded) | No | No | No | INSPECTED *via* Gautschi Thms 2.1–2.2, p. 34: hypothesis is `a_n -> a`, `b_n -> b` (eq. (2.3)). Originals not obtained. |
| **Perron (1911, *Acta Math.* 34, 109–137) + Kreuser** — Newton–Puiseux / growing coefficients | **Yes** (ratio asymptotic) | No — statement is only `y_{n+1}/y_n ~ -a n^sigma`, i.e. leading order; no `n^s` correction at all | No | No | INSPECTED *via* Gautschi (1967) Thm 2.3, p. 35. **Perron (1911) original NOT OBTAINED** (Project Euclid bot-blocked; see §4). |
| **Perron, *Die Lehre von den Kettenbrüchen*** | unknown | unknown | unknown | unknown | 1913 Teubner scan **obtained** (`refs/perron1913.pdf`, 541 pp.) but it has **no OCR text layer**, so I did **not** search it. **No claim is attributed to it.** |
| **Birkhoff (1930) / Birkhoff–Trjitzinsky (1933)** | Yes, implicitly (subsumed in normal-solution shape) | **Shape only.** Provides existence of solutions asymptotic to formal normal solutions; exponents are to be obtained by formal substitution case by case, not by a printed formula in `beta_k` | **No** — solutions are characterised up to constants; the Fundamental Theorem (p. 69) asserts properness, not normalisation | No | INSPECTED (`refs/bt1933.pdf`). Birkhoff (1930), *Acta Math.* 54, 205–246 — **NOT OBTAINED** (blocked). |
| **Wong & Li (1992a, *Stud. Appl. Math.* 87, 289–324)** — the `n^P`, `n^Q` case | Presumably yes | **Unknown — this is the key gap.** DLMF points here for exactly our equation class | Presumably no (see Nemes quote on connection coefficients) | No | **PAYWALLED — not obtained** (HTTP 403 from Wiley). CONJECTURED, unverified. |
| **Wong & Li (1992b, *J. Comput. Appl. Math.* 41, 65–94)** — bounded-coefficient case | No (hypotheses fail) | No | No | No | Not obtained; its content is however *summarised* by DLMF §2.9(i)–(ii) ("For proofs see Wong and Li (1992b)"), which I did inspect, and those hypotheses exclude our equation. |
| **Pincherle (1892) / Gautschi (1967) survey** | — | — | **No** | No | INSPECTED for Gautschi; Pincherle original **NOT OBTAINED**. Gives the minimal/dominant framework for (H) but no amplitude. |
| **Nemes (2026), arXiv:2508.15246** | — | Gives `Gamma(z) lambda_j^{-z} z^{mu_j}`-type expansions with `lambda_j, mu_j` from an indicial equation — **but only for rank-one irregular singularities**, which excludes our `d >= 2` | No closed form; numerical connection coefficients only | **Yes (general machinery)** | INSPECTED (`refs/nemes2025.pdf`). |
| **Elaydi, *An Introduction to Difference Equations*; Kooman; Van der Cruyssen; Wimp (1984) App. B** | unknown | unknown | unknown | unknown | **NOT OBTAINED** — no open-access copy located. See §4. |

---

## 2. Contribution relative to prior art (draft paragraph the note can adapt)

> The leading-order behaviour of `Q_n` is classical. Writing the Wallis recurrence as
> `Q_{n+1} + a_n Q_n + b_n Q_{n-1} = 0` with `a_n = -b(n+1) ~ -beta_d n^d` and `b_n = -1`, the
> Newton–Puiseux vertex `P_1 = (1,d)` lies strictly above the segment `P_0P_2`, so the
> Perron–Kreuser theorem (Perron 1911; Kreuser 1914; see Gautschi, *SIAM Rev.* **9** (1967),
> Thm. 2.3(a), p. 35) applies and yields at once `Q_{n+1}/Q_n ~ beta_d n^d` for the dominant
> solution and `~ -beta_d^{-1} n^{-d}` for the minimal one. Result 1 — equivalently, that the
> Borel-type transform `sum Q_n w^n/Gamma(dn+1)` has radius `d^d/|beta_d|` — is an immediate
> consequence and should be presented as such. Likewise the *shape* `rho^n n^s (1 + O(1/n))`
> after division by `Gamma(dn+1)` is exactly the Birkhoff–Trjitzinsky normal-solution shape
> (Birkhoff & Trjitzinsky, *Acta Math.* **60** (1933), Fundamental Theorem, §9, p. 69), and the
> dominant/minimal dichotomy that hypothesis (H) encodes is Pincherle's (Gautschi, op. cit.,
> Thm. 1.1, p. 31; DLMF §3.6(ii)). What we claim as new is *not* the existence of such an
> expansion but its **explicit, coefficient-level closed form**: the exponent
> `s = beta_{d-1}/beta_d + (d-1)/2` written directly in terms of the coefficients of `b`, and —
> more importantly — the **amplitude**
> `K = r_inf (2*pi)^{(d-1)/2} / ( sqrt(d) prod_i Gamma(1 - r_i) )`,
> obtained by factoring `b`, using `Gamma(n+1-r)/Gamma(n+1) ~ n^{-r}` and the Gauss
> multiplication formula. Classical difference-equation asymptotics determines solutions only up
> to a multiplicative connection coefficient, which in that framework "remain[s] unknown in other
> approaches" and is at best computed numerically (Nemes, arXiv:2508.15246, abstract and §1);
> here the connection problem is solved in closed form, with the single transcendental input
> `r_inf` isolated into hypothesis (H). The Borel framing of result 1 is a repackaging of the
> classical radius statement rather than a new asymptotic fact, and should be presented as an
> expository device. **Caveat:** the closest classical reference for our exact equation class,
> Wong & Li, *Stud. Appl. Math.* **87** (1992), 289–324 (to which DLMF §2.9 explicitly defers for
> equations `w(n+2) + n^P f(n) w(n+1) + n^Q g(n) w(n) = 0`), could not be consulted; a novelty
> claim for the explicit `s` should not be made until it has been.

---

## 3. Bibliography of sources actually obtained

All in `sessions/2026-09-17/CT-S8-LITCHECK/refs/`, retrieved **2026-09-17**.

| File | sha256 | Bibliographic data | URL fetched |
|---|---|---|---|
| `gautschi1967.pdf` | `47ed9dffc00a52b7cfb7f3943d7ba3f2a3d398284ec6a00926ced315ec1c5173` | W. Gautschi, "Computational aspects of three-term recurrence relations", *SIAM Review* **9**(1) (Jan. 1967), 24–82. DOI 10.1137/1009002. (Author's own scan, 59 pp.) | `https://www.cs.purdue.edu/homes/wxg/selected_works/section_09/029.pdf` |
| `gautschi1967.txt` | `24233f36fd1b5ed9b2ec3bdd897062afe183e548b2441a1bcf8f6fe7f55191d7` | pypdf text extraction of the above, ligature-normalised. **OCR is lossy for Greek letters** — all quotes above were checked against the page images. | derived |
| `g1967_p35_mid.png` | `e8389dab5af6abbcdee993b8d899d3bf7d266c563d2dd2b9a9a5642ecc74e049` | Page image, printed p. 35 (Theorem 2.3), source of the verbatim Perron–Kreuser quote | derived |
| `g_p58_top.png`, `g_p58_bot.png` | `fb88dfba029409ca4a220bcf350e04a7d5b468ecdb6cecaa53fff014fbf7f5e1`, `eac04bac6a13e77bb4572978fa6ba82a8a9a6ee411fd8f14feb98d11278c8255` | Page images, printed p. 81. The **bottom** crop (`g_p58_bot.png`) was read directly and shows references [41]–[48]; it is the source of the identifications Perron [41] = *Crelle* 136 (1909) 17–37, Perron [42] = *Acta Math.* 34 (1911) 109–137, Pincherle [45] = *Giorn. Mat. Battaglini* 32 (1894). The **top** crop was produced but not read. | derived |
| `bt1933.pdf` | `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6` | G. D. Birkhoff & W. J. Trjitzinsky, "Analytic theory of singular difference equations", *Acta Mathematica* **60** (1933), 1–89. DOI 10.1007/BF02398269. Open archive. | `https://projecteuclid.org/journals/acta-mathematica/volume-60/issue-none/Analytic-theory-of-singular-difference-equations/10.1007/BF02398269.pdf` |
| `bt1933.txt` | `63595af76698ff2389945f29ebadb1bd0bc8bb273a200042aa5c28c549a54368` | text extraction of the above | derived |
| `nemes2025.pdf` | `7f848c5bc15a792559442176477d609a861d9cf78b2f37d158a265c0d5511145` | G. Nemes, "Hyperasymptotics for linear difference equations with an irregular singularity of rank one: polynomial coefficients", arXiv:2508.15246v2 [math.CA], 16 Feb 2026. DOI 10.48550/arXiv.2508.15246 | `https://arxiv.org/pdf/2508.15246` |
| `nemes2025.txt` | `62a650030c3d2791b3de83ab888240e5af67e804ef62b5c12bde691b854d0a36` | text extraction | derived |
| `dlmf_2_9.html` / `.txt` | `ee9d443f560c33e209cd46cd93c2005c3083f50f91f62c1abbf70c879a05a8ea` / `72d6a344c2d04dc3564d95212091c40f1258f2369ec5062cc29daa6dc2c44f42` | NIST DLMF §2.9 "Difference Equations", Version 1.2.8, release 2026-09-15 | `https://dlmf.nist.gov/2.9` |
| `dlmf_3_6.html` / `.txt` | `354c39b7e7d7b943df83169a7f225a012fa8518fb6094b866525c4ed4495c14b` / `f6e2559307f5ac5fe7f9c909c5c71a95cdd986bd0b843e74843fc1c773a3dc86` | NIST DLMF §3.6 "Linear Difference Equations", same version | `https://dlmf.nist.gov/3.6` |
| `perron1913.pdf` | `dd8dbb5a15b83c9794976cf882dcbecb527111f61880b50796562f0cf4d9b809` | O. Perron, *Die Lehre von den Kettenbrüchen*, B. G. Teubner, Leipzig (1913), Google/IA scan, 541 pp. **No OCR text layer; NOT searched; no claim attributed.** Teubner imprint confirmed from the publisher advertisement page (`p1913_title.png`). | `https://archive.org/download/dielehrevondenk00perrgoog/dielehrevondenk00perrgoog.pdf` |
| `p1913_4.png` / `p1913_title.png` | `cdefa1e3ba37e2e551cd7efab939a5b32054d33d71aaf1052de0f06c3d9ab19f` / `83db3922a0315103653663d9a622ccb45a7e3578365591bfa4edcea30dbc747b` | front-matter page image from the above | derived |
| `wang_jat2014.pdf` / `.txt` | `1dca5c9a7d1f880c19f9854926ff78fdc85e3a30bc61ceb8c48f40b189517626` / `f6433d59a4da99edc6ee47c2d57c55d1df19a8c2d7bdfffa2870e56e0f0ea2be` | X.-S. Wang, "Plancherel–Rotach asymptotics of second-order difference equations with linear coefficients", *J. Approx. Theory* (2014) — author's copy. Searched; **no** amplitude/Borel statement for our problem. | `https://userweb.ucs.louisiana.edu/~xxw6637/papers/JAT2014.pdf` |
| `polycf.pdf` / `.txt` | `6a05e08c64c2f3d0b86d9e3e5c2e08a1ea0032ae47337bbd23dd135bee9a8f80` / `5ba9185392a926a125e04457aea528fd42b71aa55263feb90de31f5b380cc9e3` | "Real numbers with polynomial continued fraction expansions", arXiv:math/0402462v2 (authors NOT verified — I did not read the title page). Searched; contains **no** `Gamma`/asymptotic material (0 hits for "Gamma", "asymptot"). | `https://arxiv.org/pdf/math/0402462v2` |

**Cited only via Gautschi's reference list (bibliographic data INSPECTED from the page image, contents NOT obtained):**
- O. Perron, "Über einen Satz des Herrn Poincaré", *J. reine angew. Math.* **136** (1909), 17–37. [Gautschi ref. 41]
- O. Perron, "Über lineare Differenzengleichungen", *Acta Math.* **34** (1911), 109–137. [Gautschi ref. 42]
- S. Pincherle, *Giorn. Mat. Battaglini* **32** (1894), 209–291, esp. Ch. III §15 (also *Opere Scelte* vol. 1, 273–357). [Gautschi ref. 45]
- H. Poincaré, "Sur les équations linéaires aux différentielles ordinaires et aux différences finies", *Amer. J. Math.* **7** (1885), 203–258. [Gautschi ref. 46]
- F. W. Schäfke, "Lösungstypen von Differenzengleichungen und Summengleichungen in normierten abelschen Gruppen", *Math. Z.* **88** (1965), 61–104. [Gautschi ref. 51]
- E. Kreuser (Gautschi ref. 29) — the reference number is cited in Thm. 2.3 but the entry itself fell in an OCR/scan gap I did not resolve; the standard attribution is P. Kreuser, dissertation, Tübingen 1914.

---

## 4. Sources I could NOT obtain, and what I would have checked

1. **Wong & Li, "Asymptotic expansions for second-order linear difference equations. II", *Stud. Appl. Math.* **87**(4) (1992), 289–324** (ISSN 0022-2526). Wiley returned **HTTP 403**; no open-access or institutional-repository copy located. **This is the single most important gap.** DLMF §2.9(ii) names precisely this paper for `w(n+2) + n^P f(n) w(n+1) + n^Q g(n) w(n) = 0`, which is our equation with `P = d`, `Q = 0`. I would have checked: (a) whether the theorem prints the exponent of the algebraic factor **explicitly in terms of the coefficient expansions** (which, specialised, would be `s = beta_{d-1}/beta_d + (d-1)/2` modulo the `Gamma(dn+1)` vs `(n!)^d` normalisation); (b) whether the `Gamma`-type factor is written as `Gamma(n)^d`, `Gamma(dn)` or `(n!)^d` — i.e. whether the Gauss-multiplication step of result 3 already appears there; (c) whether any statement fixes the multiplicative constant for a designated solution.
2. **Wong & Li, *J. Comput. Appl. Math.* **41** (1992), 65–94**, DOI 10.1016/0377-0427(92)90239-T. ScienceDirect served a JS shell only. Lower priority: DLMF §2.9(i) summarises it and its hypotheses (`f, g` with `1/n` expansions, `g_0 != 0`) exclude our equation.
3. **Perron, *Acta Math.* 34 (1911)** and **Pincherle, *Acta Math.* 16 (1892)**, and **Birkhoff, "Formal theory of irregular linear difference equations", *Acta Math.* 54 (1930), 205–246** (DOI 10.1007/BF02547522). All three are open-archive on Project Euclid, but after the successful Birkhoff–Trjitzinsky download the host applied bot protection ("Pardon Our Interruption", 6,183-byte interstitial) to every subsequent request, across three attempts with cool-downs of 25 s, 100 s and 180 s. I would have checked Perron 1911 for the original statement and proof of the Newton-polygon theorem and, crucially, for whether Perron went beyond the ratio asymptotic to a full `n^s` refinement.
4. **Perron, *Die Lehre von den Kettenbrüchen*.** The 1913 Teubner scan was downloaded but has no text layer; the 1950 and 1957 editions on archive.org are lending-restricted (`dielehrevondenke0000dros`, `dielehrevondenke0000drdr`). I would have checked the chapter on convergence of continued fractions with unbounded partial quotients for any statement of `Q_n / prod b(k) -> r_inf != 0` and for asymptotics of `Q_n`.
5. **Elaydi, *An Introduction to Difference Equations* (Springer)** — Poincaré–Perron chapter; **Kooman**, papers on asymptotics of linear recurrences; **Van der Cruyssen**, "Linear difference equations and generalized continued fractions", *Computing* **22** (1979); **Wimp, *Computation with Recurrence Relations* (1984), Appendix B** (named by DLMF §2.9(iii) as the introduction to the general theory). No open copies located; **NOT OBTAINED**. I would have checked each for (a) a Perron–Kreuser statement refined to `n^s`, (b) any explicit amplitude.
6. **Cao, "Asymptotics for second-order linear difference equations", PhD thesis, City University of Hong Kong (2012)** — the repository page was indexed but I did not retrieve a full-text PDF. Would have checked for a self-contained restatement of Wong–Li 1992a, which theses often include.

**Search scope and method, for the absence claims.** Full-text search (ligature-normalised: `U+FB01 -> fi`, `U+FB02 -> fl`) over `gautschi1967.txt`, `bt1933.txt`, `nemes2025.txt`, `wang_jat2014.txt`, `polycf.txt`, `dlmf_2_9.txt`, `dlmf_3_6.txt` for the terms: `Borel`, `radius`, `Gauss multiplication`, `connection`, `undetermined`, `Pincherle`, `Perron`, `minimal`, `dominant`. Discovery searches: arXiv API (`all:"Perron-Kreuser"` — **0 results**; `all:"three-term recurrence" AND all:"minimal solution"` — 3 results, none relevant; `all:"Pincherle" AND all:"continued fraction"` — 4 results, none relevant; `abs:"difference equation" AND abs:"connection constant"` — 0 results), plus DLMF bibliography for `Wong`. **Not claimed: that these results do not exist anywhere.**

**Sources deliberately not used.** Search engines surfaced sci-hub mirrors for both Wong–Li papers and for Birkhoff–Trjitzinsky. These were **not** fetched, per the governance rule against paywall bypass.
