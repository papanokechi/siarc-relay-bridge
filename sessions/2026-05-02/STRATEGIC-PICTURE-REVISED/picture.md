# SIARC Strategic Picture — Revised
**Revision:** v1.9 (post-014 PASS — `PASS_A_EQ_6_ONLY` at $|\delta_\text{lin}| \le 3.09 \times 10^{-23}$ across 4 j=0 cubic families; M7 achieved in the A=6-only branch; G5+G16 closed; PSLQ on H6 Chowla–Selberg basis B19+ exhausts at PSLQ-detection precision with no $\Gamma(1/3)$ closure; trivial reflection-identity in literal 18-basis flagged for synthesizer hygiene)
**Original:** 2026-05-02 18:05 JST
**Updated:** 2026-05-02 21:00 JST  (post-014 absorption — extended v1.8 → v1.9)
**Operator:** papanokechi
**Supersedes:** `20260502_picture.docx` (preserved as the historical
introspective draft; this document is the formal snapshot for
synthesizer review)
**Audience:** Synthesizer agent (Claude, claude.ai) — strategic /
epistemic review pass before the next firing cycle.

> **🆕 Updates since v1.8 (see § 19 Amendment Log for detail):**
> - ✅ **Prompt 014 PASSED with verdict `PASS_A_EQ_6_ONLY`** (T25D-RETRY-13PARAM, ~12 min agent). Refit the four saved $j=0$ cubic $y_n$ series ($Q_{30}\ldots Q_{33}$, dps=25000, $N=200\ldots 1200$) with an **11-parameter** LIN ansatz (4 base + 7 $1/n$ corrections; $K_\text{FIT}=7$ instead of the prompt's specified $K_\text{FIT}=9$ — **judgment call**, see Q22) via square-exact `mp.lu_solve` at workdps=4000. Per-family $|\delta_\text{lin}|$: $\{3.27, 3.16, 11.9, 30.9\} \times 10^{-24}$ — **max $|\delta| = 3.09 \times 10^{-23}$**. Tail-window cross-check (7-pt vs 11-param at $N \ge 600$): agreement $\sim 4$–$8 \times 10^{-14}$; vs Prompt 006's 5-param tail-fit at $N \ge 800$: $\sim 1$–$3 \times 10^{-8}$ (consistent with 006's documented precision floor). **PSLQ Phase D (DPS_PSLQ=200, DPS_VERIFY=400, maxcoeff=$10^{50}$, tol=$10^{-40}$):** 17-member deduplicated H6 Chowla–Selberg basis B19+ returns **no relation** on any of 4 families — i.e., **no $\Gamma(1/3)$ Chowla–Selberg amplitude closure** detected at this precision. **Reading:** $A = 6$ to PSLQ-detection precision; the j=0 endpoint closes in the "A=6 only" branch (no Chowla–Selberg amplitude correction in B19+ at $|\delta| \sim 10^{-23}$).
> - ✅ **G5 + G16 CLOSED (in the A=6-only branch).** PCF-2 §6 (current published wording: `AMBIGUOUS-AT-FINITE-N`) can now be amended to `A = 6 to PSLQ-detection precision; no detected Chowla–Selberg amplitude correction in H6 basis at the present precision`. The relay agent drafted `pcf2_v1.4_amendment.md` (Phase F output) for the operator's review; deposit gated on Q22 (does $|\delta| \sim 10^{-23}$ meet the operator's intended closure threshold, or is the stretch goal $|\delta| < 10^{-30}$ formally required?). M7 ✅ **achieved in soft branch**.
> - 📊 **Numerical findings cross-validated.** The 014 verdict is fully consistent with **Prompt 006's empirical signal** ($A_\text{lin} = 6 \pm 2 \times 10^{-7}$ across all 4 families, monotone-decreasing $|\delta_\text{lin}|$ with $N_\max$): no discrepancy. The 11-param refit reaches $\sim 10^{-23}$ — 16 orders below 006's 5-param floor — and matches the Prompt 014 spec's $|\delta| < 10^{-15}$ minimum target with $\ge 8$ orders of margin. **Stretch goal $|\delta| < 10^{-30}$ NOT achieved** in this run; would require fresh $y_n$ at $N \le 2400$ with dps $\ge 44{,}300$ and $K_\text{FIT}=9$ (full 13-param). Operator decides via Q22.
> - ❓ **NEW open question (Q22, see § 8) — *operator decision required for closure-threshold acceptance*:** does the $|\delta| \sim 10^{-23}$ realised precision **formally close** G5+G16 (clearing the $|\delta| < 10^{-15}$ minimum target with comfortable margin and exhausting the H6 B19+ basis at PSLQ precision), **or** does PCF-2 v1.4 require the stretch goal $|\delta| < 10^{-30}$ before depositing the §6 amendment? Path (a) **deposit now** at $|\delta| \sim 10^{-23}$ (faster; soft-branch closure; ships v1.4 immediately) vs path (b) **fire 014b** to extend $y_n$ at $N \le 2400$ / dps $\ge 44{,}300$ for the full 13-param + stretch-goal precision (slower; harder-branch closure; ~few hours additional compute). *This question is operator + Claude territory; the relay agent cannot pick.*
> - ❓ **NEW open question (Q23, see § 8) — *PSLQ basis hygiene rule for future deep-WKB closures*:** the literal 18-member B19+ basis specified in Prompt 014 contains **both** $\sqrt{3}$ and $\Gamma(1/3)\Gamma(2/3) / (2\pi)$, which are $\mathbb{Q}$-equivalent via the gamma-reflection identity $\Gamma(1/3)\Gamma(2/3) = 2\pi/\sqrt{3}$. Running PSLQ on the literal 18-basis returns the **trivial relation** $1 \cdot \sqrt{3} - 3 \cdot \mathrm{CS}_{\sqrt{3}} = 0$ (target coefficient $= 0$ — *not* a Chowla–Selberg signal) on every family. The relay agent dropped $\mathrm{CS}_{\sqrt{3}}$ for the verdict-decisive PSLQ run, retaining the literal 18-basis run only for traceability in `pslq_results_18basis_literal.json`. **Question:** should future PSLQ-based closure prompts pre-screen the basis specification for $\mathbb{Q}$-linear dependencies (gamma-reflection / duplication / multiplication identities) and emit the deduplicated basis as the operative one? This is an op-design hygiene rule, applicable to any deep-WKB / Chowla–Selberg-style closure operator (not just 014).
> - 🔧 **Reusable infrastructure delivered.** `t25d_retry_runner.py` (square-exact `mp.lu_solve` 11-param refit on saved $y_n$ CSVs + tail-window cross-check + Richardson cross-check + PSLQ on dedup-vs-literal bases + Phase F amendment-draft) is now reusable for any future deep-WKB amplitude-closure operator on a saved-CSV input. Generalisation to $K_\text{FIT}=9$ requires regenerating $y_n$ at $N \le 2400$ / dps $\ge 44{,}300$ from `cf_value` (~30 min wall) — out of scope for 014; queued under Q22 path (b) if operator opts.
> - 🛠 **Phase E precision impedance documented (not a verdict downgrade).** Prompt 014 Phase E asked for a Richardson cross-check at $1 \times 10^{-10}$ agreement; the float64-stored T2 input limits achievable Richardson precision to $\sim 1 \times 10^{-5}$. Reported as **MET-IN-DIRECTION** (sign and magnitude of trend) rather than at $10^{-10}$; logged in `discrepancy_log.json` as `phase_E_spec_impedance`. Verdict not downgraded. *(Op-design lesson: future Richardson cross-check phases should specify precision targets compatible with input-data precision, or specify the input-data precision floor as part of the spec.)*
> - 📊 **Cycle status (post-010 + 012 + 013 + 014):** Of the **12** prompts fired in this cycle, **7 are ✅ DONE** (001, 003, 004, 005, 007, 012, **014**), **3 are 🛑 HALTED** (002 G12 source-drift; 006 j=0 5-param precision floor — *now superseded in the soft branch by 014*; 013 G15 gate — as designed), **2 are 🟡 PARTIAL** (009 G15; 010 G6b). G2 + G5 + G16 are now **closed** (G2 at d=3 by 012 across 3 Galois bins; G5 + G16 by 014 in the A=6-only branch). **G2 + G5 + G16** are the *first three* gaps to close cleanly this cycle.

> **🆕 Updates since v1.7 (carried forward from v1.8):**
> - 🟡 **Prompt 010 LANDED with verdict `G6B_PARTIAL_HIGHER_ORDER_NEEDED`.** Generalised the V_quad Birkhoff recurrence (CC-MEDIAN-RESURGENCE-EXECUTE, $\alpha=3, \beta=1, \gamma=1, \delta=0, \epsilon=1$, 108 digits) to **arbitrary $d=2$ PCF families** $(\alpha, \beta, \gamma, \delta, \epsilon)$ via symbolic derivation in `derive_recurrence.py`; the generalisation specialises back to V_quad's existing recurrence and reproduces its 108-digit $C$ value to all displayed digits (cross-validation). Extracted leading Stokes multiplier $S_1 = 2 \pi i C$ for **four** representatives across the PCF-1 v1.3 §3 $\Delta_b$ dichotomy at the t2c precision ladder $\text{dps} \in \{100, 150, 200, 250\}$, $N$ up to $2000$, with **≥ 60-digit cross-method agreement** (Richardson tail vs LSQ-in-$1/n$) at top dps.
> - 📊 **Numerical results** ($\Delta_b < 0$, predicted $A=3$): V_quad $C = +8.12733679549\ldots$ (matches CC-MEDIAN bit-for-bit on its 49 displayed digits); QL15 $C = +21.38412649463\ldots$. ($\Delta_b > 0$, predicted $A=4$): QL05 $C = +1.40328080725\ldots$; QL09 $C = -6.07472006379\ldots$. **$|S_1|$ differs across the dichotomy at $O(1)$ absolute scale (no `G6B_STOKES_INVARIANT` halt — Stokes data is *not* sign-invariant)** — but **no *structural* pattern** emerges: $\mathrm{sign}(C)$ varies *within* the $\Delta>0$ side ($+$ for QL05, $-$ for QL09); all four $S_1$ are purely imaginary; within-side spread is comparable to cross-side spread; ratios are not clean rationals or square-roots. Per the prompt's strict PASS-criterion, this is honest PARTIAL: the dichotomy lives **below** the leading-multiplier scale.
> - 🌟 **NEW universal side-finding (NEW gap G19).** The branch exponent $\beta_R$ in the Birkhoff resurgent ansatz $a_n \sim C \, \Gamma(n + \beta_R) \, \zeta_*^{-(n+\beta_R)}$ is **essentially zero** ($\le 10^{-85}$) across **all four** $d=2$ representatives — not just V_quad. This is a *structural regularity* of the $d=2$ PCF Birkhoff series: the alien amplitudes live exactly on $\Gamma(n)$ with **no $\Gamma$-shift**. Strong candidate for synthesizer-formalisation as "alien-amplitude $\Gamma$-shift $= 0$ universal at $d=2$"; possibly relevant to Sakai-surface / isomonodromic geometry of the $d=2$ catalogue.
> - 📝 **NEW Prompt 016 (`T36-S2-EXTRACTION`) drafted.** Reuses the four cached series CSVs (`borel_*_dps250_N2000.csv`); **no new `mpmath` series computation**. Subtracts the leading $C \, \Gamma(n) \, \zeta_*^{-n}$ from $a_n$ and applies a second Richardson pass to the residual to extract $S_2$ (alien amplitude at $2\zeta_*$). Tests whether (a) $|S_2|$ discriminates the dichotomy, (b) the ratio $S_2 / S_1^2$ is structurally invariant (canonical for connected resurgent algebras), (c) $\arg(S_2)$ separates the two sides. Compute is light (~30 min agent; pure refit). **Closes G6b fully or escalates to S_3.**
> - 🛠 **Reusable infrastructure delivered.** `derive_recurrence.py` (symbolic derivation of the $d=2$ Birkhoff recurrence in $(\alpha, \beta, \gamma, \delta, \epsilon)$) and `t35_runner.py` (numerical extraction with t2c precision-ladder discipline, Richardson + LSQ cross-method) are now reusable for any future $d=2$ PCF Stokes-data extraction. Generalisation to $d=3$ requires deriving a new recurrence from Conte-Musette's $d=3$ ODE (different singular structure: rank $4/3$ at $0$, $2/3$ at $\infty$) — out of scope for 010/016, deferred to a later prompt.
> - ❓ **NEW open question for synthesizer (Q18, see § 8).** Is $\mathrm{sign}(C)$ a basis-independent invariant in the resurgent classification, or does it depend on the Birkhoff basis-of-formal-solutions choice ($f_+$ vs $f_-$, with $c = +2/\sqrt{\alpha}$ vs $c = -2/\sqrt{\alpha}$)? The runner used a uniform $c = +2/\sqrt{\alpha}$ convention; if Claude's reading of the literature pins sign$(C)$ as basis-dependent, the QL05 vs QL09 sign disagreement is a convention artefact, not a genuine asymmetry.
> - 📊 **Status:** P-PIII Stokes-side discrimination is **PARTIAL** — leading scale shows the dichotomy is real but unstructured; closure via Prompt 016 ($S_2$ scale) is the next test. **G6b** is no longer "future" — it has a measured leading-order verdict and a concrete S_2 follow-up path.
> - ✅ **Prompt 012 LANDED with verdict `G2_CLOSED_AT_D3`** (XI0-D3-DIRECT, ~25 min agent). All **K=3 Galois bins** of the $d=3$ cubic catalogue (`+_C3_real`, `+_S3_real`, `-_S3_CM`) verify $\xi_0 = 3 / \alpha_3^{1/3}$ to **80 algebraic digits** (`xi0_d3_runner.py`, dps=80) via Newton-polygon characteristic-root test on the slope-$1/3$ edge of $L = 1 - z B(\theta+1) - z^2$. Numerical Borel-singularity ladder via the $Q_n$ recurrence at $N \in \{500, 1000, 1500\}$ confirms the asymptotic direction (3.2–3.4 digits at $N=1500$, consistent with $O(1/N)$ subleading). 5 AEAL claims; halt log `{}`. **G2 closed cleanly at $d=3$** — D2-NOTE Conj 3.3.A* now has empirical support at $d=2,3,4$. **NEW open question (Q20, see § 8) — *proof upgrade candidate*:** the Newton-polygon test depends only on $\alpha_3$ via standard Newton-polygon theorems; the 80-digit per-bin agreement is *uniformity evidence*, but the underlying operator-level argument may already constitute a **proof** (modulo standard Newton-polygon / irregular-singular-point machinery), not just empirical support. If Claude judges yes, Conj 3.3.A* could be upgraded **DEFERRED → PROVEN** at $d=3$ — and by the same structural argument, **EMPIRICAL → PROVEN** at $d=4$ — closing $G_2$ in the strongest sense for *all* $d \ge 2$ simultaneously.
> - 🛑 **Prompt 013 HALTED with verdict `CC_BOREL_009_NOT_AVAILABLE`** (CC-FORMAL-BOREL-CLOSE, ~10 min agent — *gate fired correctly, not a failure*). Prompt 013 was hard-gated on Prompt 009 returning `G15_CLOSED`; 009 is `G15_PARTIAL` with five unresolved residuals (R1–R5) and explicit `C_can NOT NUMERICALLY COMPUTED`. The relay agent inspected the upstream session, triggered the named halt clause **before any phase ran**, and produced no Borel sum, no closed-form expression, no canonical Stokes constant — i.e., refused to fabricate $S_{\zeta_*}^{\text{can}}$ or silently substitute $S_{\zeta_*}^{\text{native}} \approx 51.0656i$ in the canonical-coordinate formula (the prompt's Do-Not list explicitly bars this). CT v1.3 §3.5 status was **not** flipped. 1 AEAL halt-record claim with upstream hashes pinning 005 + 009 inputs for refire reproducibility. **Discipline working as designed:** the gate kept a flawed result out of CT v1.4 territory.
> - ❓ **NEW open question (Q21, see § 8) — *operator decision required for 013 refire*:** two paths: **(a)** acquire Okamoto 1987 + Conte-Musette 2008 ch. 7 (G3b workflow), refire Prompt 015 to lift 009 to `G15_CLOSED`, refire 013 unchanged (the **stronger** result; numerical 30-digit closure of $S_{\zeta_*}^{\text{can}}$); **(b)** synthesizer reformulates 013 to accept `G15_PARTIAL` by writing the Borel sum **symbolically modulo R2–R5**, landing at `CC_FORMAL_BOREL_SYMBOLIC_PARTIAL` with no numerical gate (the **faster** result; unblocks the rest of the channel-theory roadmap immediately, but ships a symbolic-only canonical-form expression). Path (a) is preferred if the literature is acquirable on a reasonable timeline; path (b) is the right call if the operator wants to ship CT v1.4 *now* and accept canonical-form Stokes-amplitude as "pending Lax-pair closure" prose. *This question is operator + Claude territory; the relay agent cannot pick.*
> - 📊 **Cycle status (post-010 + 012 + 013):** Of the 11 prompts fired in this cycle, **6 are ✅ DONE** (001, 003, 004, 005, 007, 012), **3 are 🛑 HALTED** (002 at G12 source-drift; 006 at j=0 5-param precision floor; 013 at G15 gate — the latter as designed), **2 are 🟡 PARTIAL** (009 G15; 010 G6b). G2 is now the *first* gap to close at *all* tested $d \in \{2, 3, 4\}$ — and possibly upgradable to PROVEN-at-all-$d$ pending Q20 arbitration.

> **🆕 Updates since v1.6 (carried forward from v1.7):**
> - 🟡 **Prompt 009 LANDED with verdict `G15_PARTIAL`.** V_quad's scalar OGF ODE re-derived from scratch by sympy: $3 z^3 f''(z) + 10 z^2 f'(z) + (5z + z^2 - 1) f(z) = 0$ (exact rational coefficients; Newton-polygon slope $1/2$; $c = \pm 2/\sqrt{3}$; $\zeta_* = 4/\sqrt{3}$; $\rho = -11/6$ — all exact rationals/algebraics, agreeing with the 250-digit V_quad-native measurement from Prompt 005). The change-of-variables decomposes as $\Phi = \Phi_\text{symp} \circ \Phi_\text{shift} \circ \Phi_\text{resc}$. **Φ_resc parameter $\lambda = 1/3$ pinned** by leading-exponent matching (R3-conditional on Stokes sign convention); **Φ_shift Jacobian $= 1$** (affine-shift triviality); **Φ_symp residual** — requires Okamoto 1987 (*Funkcial. Ekvac.* **30**:305–332) §§2–3 explicit `2×2` Lax pair, **not in operator's local library**. Five residuals R1–R5 documented; R5 (Lax pair) is the primary blocker. Canonical-form numerical value $C_\text{can}$ deliberately *not* produced (would require fabricating R2/R3/R5; prompt's "Do NOT fabricate" clause forbids).
> - 🧠 **Substantive structural finding (NEW gap G17 — Claude review candidate).** V_quad's scalar ODE Hamiltonization is *linear* (Hamiltonian quadratic in $p$), while canonical $P_{III}(D_6)$ is *nonlinear* in $(q, p)$. The two Hamiltonians **live at different layers of the geometry**: V_quad's scalar ODE is the **L-equation** of an isomonodromic Lax pair (linear, frozen at the V_quad parameter point), while $P_{III}(D_6)$ is the **isomonodromic deformation** of that L-equation (nonlinear, in coordinates that are monodromy data of the Lax pair). CT v1.3 §3.5's framing "algebraic identity at Painlevé-class level only" gestures at this layer separation but does not spell it out. **Implication:** $\Phi$ cannot be a direct change-of-variables on $(f, f', z)$ — it must act on the Lax-pair monodromy variety. This sharpens the G15 statement and flags a possible CT v1.4 amendment to §3.5.
> - 🔍 **Convention question (NEW gap G18, residual R1).** CT v1.3 §3.5's parameter point $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0) = (1/6, 0, 0, -1/2)$ does **not** satisfy the Okamoto constraint $\alpha_\infty + \alpha_0 + \beta_\infty + \beta_0 = 0$ (sums to $-1/3$). Three interpretations: (a) CT v1.3 uses a non-Okamoto convention (e.g., Sakai $E_7^{(1)}/D_7^{(1)}$ root data); (b) one entry is a spectral-type label rather than a Hamiltonian parameter; (c) the relay-prompt's quoted constraint is for a different $P_{III}(D_6)$ parametrization. **No selection without R1 resolution from Okamoto §2.** Flagged as informational anomaly, not halt-class.
> - 📝 **NEW Prompt 015 (`T25E-VQUAD-PIII-NORM-MAP-CLOSE`) drafted.** Hard-gated on R5 (operator acquires Okamoto 1987 §§2–3 + Conte-Musette 2008 ch. 7 via the existing G3b ILL/AMS workflow). Pins R1–R4 from the literature, writes Φ_symp explicitly from the Lax-pair gauge transform, computes $J(\Phi)$ numerically, verifies $S_{\zeta_*}^\text{can}$ against Lisovyy-Roussillon's $P_{III}$ connection-problem tables to ≥ 50 digits. Estimated runtime 2–4 hr; **gates 013** (full G15 closure required for `G15_CLOSED`).
> - 🟢 **Prompt 014 (`T2.5d-RETRY-13PARAM`) remains highest-leverage tiny-compute slot** for the next compute window — unchanged from v1.6.
> - 📊 **Status:** P-CC `op:cc-formal-borel` is now **PARTIAL** (Φ_resc/shift pinned; Φ_symp residual; symbolic decomposition documented). Full closure is operator-side gated (literature acquisition), not compute-side. M6 canonical-form completion deferred to Prompt 015.

> **🆕 Updates since v1.5 (see § 16 Amendment Log for detail):**
> - 🛑 **Prompt 006 HALTED with verdict `AMBIGUOUS_AT_DPS8000`.** Formal halt fired because the 5-parameter LIN/EXP ansatz pair disagree on $A$ by $\sim 2.3 \times 10^{-6}$ at $N=1200$ — far above the spec's $1 \times 10^{-30}$ threshold. **`op:j-zero-amplitude-h6` remains OPEN.**
> - 📈 **But the data signals A=6 *clearly*.** The 5-param LIN fit gives $A_\text{lin} = 6 \pm 2 \times 10^{-7}$ across all four j=0 cubic families (30, 31, 32, 33), with $|\delta_\text{lin}|$ **monotone-decreasing** from $\sim 5 \times 10^{-8}$ at $N_\max=1000$ to $\sim 2 \times 10^{-8}$ at $N_\max=1200$. This is structural support for $A_\text{true} = 6$ exactly (no $\Gamma(1/3)$ closure), modulo a residual $O(1/N^2)$ truncation bias intrinsic to the 5-param ansatz at this $N_\max$.
> - 🔧 **Spec-vs-reality lesson (NEW gap G16).** The literal `dps=8000 ∧ N=1200` reading is *internally infeasible* for an $A=6$ cubic: $|L_N - L_\text{ref}| \sim \exp(-6 N \log N)$ requires $\text{dps} \gtrsim 22{,}150$ at $N=1200$. The relay agent honored the prompt's `dps≥8000` clause by setting `dps=25000` and documented the substitution in `halt_log.json`. Compute time was ~35 s vs the prompt's 6–10 hr estimate — a structurally faster regime than expected. The methodological lesson: **5-param ansatz at $N=1200$ caps $A$-precision at $\sim 7$ digits**; the spec's 30-digit threshold requires $\geq 13$ parameters.
> - 📝 **NEW Prompt 014 (`T2.5d-RETRY-13PARAM`) drafted.** Refits the same saved $y_n$ CSVs (no new `cf_value` calls) with a 13-parameter ansatz $y_n = -A n \log n + \alpha n - \beta \log n + \gamma + \sum_{k=1}^{9} c_k / n^k$. Expected to drive $|\delta_\text{lin}|$ below $10^{-15}$ and unlock Phase D PSLQ. Compute is light (~5–20 min agent on a single laptop).
> - 📊 **Status:** P-PET closure on the j=0 endpoint is *deferred* but not falsified. M7 is not yet achieved; the empirical signal is "A=6 supported at 7 digits, monotone-converging" — short of the 30-digit formal target.

> **Updates since v1.4 (carried forward from v1.5):**
> - 📝 **Math-closure prompt batch DRAFTED.** Four new relay prompts staged at `tex/submitted/control center/prompt/` to close the residuals surfaced by the v1.2/v1.3/v1.4 verdicts:
>   - **009 — `vquad-pIII-normalization-map`** closes G15 (V_quad → P_III(D_6) Stokes-data change-of-variables Φ; symbolic; ~4–8 hr).
>   - **010 — `t35-stokes-multiplier-discrimination`** closes G6b (PCF-1 §3 sign-of-Δ_b dichotomy at the Stokes-multiplier scale; numerical mpmath dps≥150; ~6–10 hr).
>   - **012 — `xi0-d3-direct`** closes G2 (per-Galois-bin Newton-polygon test of D2-NOTE Conj 3.3.A* at d=3; numerical mpmath dps=80; ~3–10 hr).
>   - **013 — `cc-formal-borel-close`** closes P-CC formally (composes 005's $C$ + 009's Φ into closed-form $\mathcal{B}[V_{\text{quad}}]$ in canonical $P_{III}(D_6)$ coordinates; **HARD-GATED on 009**; ~4–8 hr).

> **Updates since v1.3 (carried forward from v1.4):**
> - ✅ **Prompt 005 PASSED with verdict `H4_EXECUTED_PASS_108_DIGITS`** — the cross-method Stokes-amplitude agreement is **108 digits**, far exceeding the forecast 30–50 (central 40). Three independent extractors (ratio test, three-point, Δ²-log) cross-validated. **M6 is achieved** with substantial precision margin.
> - 📈 **H4 *refined* by the data, not falsified.** The branch exponent fits to **β = 0 (logarithmic Borel singularity)** to ≥ 107 digits across all three methods, *not* the half-integer "square-root class" that was the leading expectation. This sits inside H4's broader "algebraic-LOGARITHMIC" hedge — strictly a refinement of the prediction, not a contradiction.
> - 📊 **Stokes-amplitude measurement (V_quad native normalization):** $C = 8.12733679549507236711257873202358318226454272233879\ldots$; $S_{\zeta_*} = 2\pi i C \approx 51.06556\ldots\, i$ (purely imaginary).
> - ⚠ **Phase D method substitution.** The relay agent substituted "polynomial LSQ in $1/n$ at order 40" for the prescribed "local Padé-of-Padé Borel fit" because the prescribed method collapses to roundoff equality with Phase C when β=0. Self-documented in the session's `rubber_duck_critique.md`. Cross-method agreement (108 digits) holds across the substituted Phase D.
> - 🆕 **NEW HIGH-severity gap G15**: The H4 result is in **V_quad native normalization** (the $b_n = 3n^2+n+1$ recurrence coordinates), not in $P_{III}(D_6)$ Hamiltonian-form coordinates. CT v1.3 §3.5's algebraic identity is at the Painlevé-class level only — the explicit change-of-variables that maps the Stokes data to canonical $P_{III}(D_6)$ form has not been written out. **Gates `op:cc-formal-borel`** (the formal closure of the channel-theory pipeline) and any synthesizer comparison against external $P_{III}(D_6)$ Stokes literature.

> **Updates since v1.2 (carried forward from v1.3):**
> - 🛑 **Prompt 002 HALTED with verdict `ARXIV_MIRROR_HALTED_PAGE_COUNT_DRIFT_2`.** 4/5 records (umbrella v2.0, PCF-2 v1.3, CT v1.3, T2B v3.0) built clean with matching page counts. **PCF-1 v1.3 source has drifted** — local rebuild = 21 pp, Zenodo v1.3 = 16 pp; the workspace `p12_journal_main.tex` has likely been overwritten by an in-progress v1.4 draft. Per the prompt's HALT clause, no git push was performed; deliverables are staged locally only at `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/`.
> - ⚠ **Anomaly 002-A**: Channel Theory v1.3 source carries `\author{The SIARC author}` literal placeholder. arXiv submission of record #4 will be rejected until this is replaced with the real-name+affiliation block. (Zenodo PDF is unaffected — placeholder visible only in the source.)
> - ⚠ **Anomaly 002-B**: Endorsement-request templates for math.NT records #2 (PCF-1 v1.3) and #4 (CT v1.3) are skeletons only. Candidate endorser names declined per the no-fabrication clause; `.bib` files lack arXiv user-id handles.
> - 🆕 **NEW gaps G12, G13, G14** (operational/distribution layer); **NEW pending items** `pcf1-v13-reconcile` (HIGH; gates 002), `ct-v13-author-placeholder-fix` (HIGH; gates 002 record #4), `endorsement-handles-acquire` (MED; gates 002 records #2 + #4).
> - 🆕 **NEW future Prompt 011** (PCF1-V13-RECONCILE — operator-decision-driven; resolve source drift) queued.

> **Updates since v1.1 (carried forward from v1.2):**
> - ✅ Prompt 007 fired with verdict `T3_LABELED_60_OF_60`. All 60 families (10 d=2 + 50 d=3) algorithmically labelled.
>   V_quad sanity check **PASSES** as `P_III(D_6)` (matches CT v1.3 §3.5 algebraic identity).
> - ⚠ **H3 *negatively* closed.** The Conte–Musette algorithmic test on the linear OGF ODE is **invariant across $\mathrm{sign}(\Delta_b)$** — produces uniform labels and **cannot reproduce** the PCF-1 v1.3 §3 dichotomy ($A=4$ for $\Delta>0$, $A=3$ for $\Delta<0$). The $d=2$ catalogue is uniformly `P_III(D_6)`; the $d=3$ catalogue is uniformly `PAINLEVE_UNCLASSIFIED` (rank $4/3$ at $0$, $2/3$ at $\infty$). The PCF-1 dichotomy lives below the Painlevé-class resolution scale — at the Stokes-multiplier level.
> - 🆕 **Future Prompt 010 (Stokes-multiplier discrimination) queued** to close the residual sign-split using a t2c-style precision-escalation pipeline.

> **Updates since v1.0 (carried forward from v1.1):**
> - ✅ Prompt 001 fired and verified (Item 19 spliced into submission_log.txt; CT v1.3 DOI now of record).
> - ✅ Prompt 003 fired with verdict `T1_PHASE1_GAPTYPE_C` — **B4 reframed from "proof gap" to "literature bracket $A \in [d, 2d]$"**. Phase 2 now has a defined target (lift $\psi_\text{lower}$ to $2d$), but is BLOCKED on primary-source acquisition + Theory-Fleet H1 label arbitration.
> - ✅ Prompt 004 fired with verdict `D2_NOTE_DRAFTED` — 4-page note built clean, 8 AEAL claims, awaits operator Zenodo upload. M1 achieved on the drafting side; closure on G1+G8 lands once the note is published.
> - ⚠ **NEW HIGH-severity gap G11**: T1's primary-literature reading flags Theory-Fleet H1 verdict `B4_PROVED_AT_d≥3` as heuristic-grade; logged for Claude / human-reviewer arbitration (does not affect any *published* artefact's framing because all current Zenodo records cite "verified"/"support", not "proven").

---

## 1. Mission Statement

The **SIARC** program (Self-Iterating Analytic Relay Chain) seeks
a complete arithmetic stratification of polynomial continued
fractions (PCFs) of the form

$$
\alpha(b) \;=\; a_0(b) \;+\; \cfrac{b}{a_1(b) \;+\; \cfrac{b}{a_2(b) \;+\; \cdots}}
$$

with $a_i \in \mathbb{Z}[b]$ polynomials in a generator $b\in\mathbb{N}$,
$\deg a_i \le d$.

The **master conjecture** (P-MC, working title *SIARC-MASTER-V0*)
posits a functor
$$
\Phi \;:\; \mathrm{PCF}(1, b) \;\longrightarrow\; (\Delta_d,\; \|\Delta\|_{\mathrm{Pet}},\; \xi_0)
$$
mapping each PCF family to an arithmetic-asymptotic invariant triple:

- **$\Delta_d$** — modular discriminant of the associated curve at
  degree $d$ (elliptic / hyperelliptic, depending on $d$).
- **$\|\Delta\|_{\mathrm{Pet}}$** — Petersson $L^2$ norm of $\Delta$
  in the appropriate weight space (working level: weight 12,
  $SL_2(\mathbb{Z})$, for the cubic case).
- **$\xi_0$** — Newton-polygon-derived Borel-singularity radius
  of the formal coefficient series; conjecturally
  $\xi_0(b) = d/\beta_d^{1/d}$ where $\beta_d$ is the leading-
  monomial coefficient.

Conjecture P-MC: $\Phi$ classifies PCF arithmetic asymptotics up
to obvious equivalences (rescaling $b$, integer translates of
$a_0$, etc.).

The five-paper publication ladder of the program is:

| Paper       | Working title (working) | Status |
|-------------|--------------------------|--------|
| **PCF-1**   | Polynomial continued fractions, modular framing | Zenodo v1.3 published |
| **PCF-2**   | PCF at degree three — cubic-modular framing | Zenodo v1.3 published |
| **CT**      | Channel Theory — formal asymptotic channels for PCFs | Zenodo v1.3 published |
| **SIARC umbrella** | Arithmetic stratification, modular-discriminant framing | Zenodo v2.0 published |
| **D2-NOTE** | Newton-polygon universality of $\xi_0$ — short note | DRAFT (Prompt 004 queued) |

with downstream papers D1 (PCF-2 cubic results paper), D3
(channel-theory results paper), D7 (AEAL methodology), and the
**SIARC-MASTER-V0** announcement gated on P-NP + P-B4 + P-CC
closures.

---

## 2. Current Status (2026-05-02 18:05 JST)

### 2.1 Published Zenodo records

| Record | Version DOI | Concept DOI | Pages | State |
|--------|-------------|-------------|-------|-------|
| T2B v3.0 (channel theory bibliography) | `10.5281/zenodo.19915689` | `10.5281/zenodo.19783312` | — | published |
| PCF-1 v1.3 (modular framing) | `10.5281/zenodo.19937196` | `10.5281/zenodo.19931635` | 16 | published |
| SIARC umbrella v2.0 | `10.5281/zenodo.19965041` | `10.5281/zenodo.19885549` | — | published |
| PCF-2 v1.3 (cubic-modular) | `10.5281/zenodo.19963298` | `10.5281/zenodo.19936297` | 22 | published |
| **Channel Theory v1.3** | `10.5281/zenodo.19972394` | `10.5281/zenodo.19941678` | 17 | **published TODAY ~17:00 JST** |

PDF SHA-256 anchors logged in `siarc-relay-bridge` `claims.jsonl`
across the corresponding session folders. CT v1.3 SHA-256
`df3b90e8…` is byte-identical to the staged build artefact.

### 2.2 Empirically verified (AEAL-logged)

- **T2 PASSED at $d=3$** (PCF2-SESSION-T2). Petersson modular
  discriminant Spearman $\rho(\|\Delta\|_{\mathrm{Pet}},\, \log b_{\mathrm{PCF}}) = +0.638$,
  $p_{\mathrm{Bonf}} = 8.6 \times 10^{-6}$ on $n=50$ cubic
  families at $K=14$. Beats the bare $\log|j|$ baseline
  ($\rho=-0.568$, $p_{\mathrm{Bonf}}=2.34\times 10^{-4}$) by
  ${\sim}30\times$ in Bonferroni $p$.
- **$\xi_0 = d/\beta_d^{1/d}$ verified at $d=4$** (PCF2-SESSION-Q1)
  at dps 80 with spread 0 across multiple test families.
- **$A_n = 2d$ unsplit at $d=3$ and $d=4$** on 60 PCF families
  (B4 evidence; not yet a proof).
- **Channel Theory v1.2 → v1.3 transition** absorbed umbrella
  v2.0 §4.4 invariant-triple framing and Theory-Fleet H4 median-
  resurgence prediction; reframed `op:cc-formal-borel` from
  PARTIALLY DIAGNOSED to (DIAGNOSED via H4 + new exec op).
- **🆕 T1 Phase 1 lit review (003) — `T1_PHASE1_GAPTYPE_C`.**
  Literature-derivable bracket $A \in [d, 2d]$ for the SIARC PCF
  stratum at $d \ge 3$ under the Wasow-vs-Adams normalization
  framing. SIARC empirical $A_\text{fit}\approx 2d$ at $d=3,4$
  favors the Adams reading (= Conjecture B4 at the upper bound);
  primary-source resolution required to pin which normalization
  the SIARC stratum actually corresponds to.
- **🆕 D2-NOTE drafted (004) — `D2_NOTE_DRAFTED`.** 4-page note,
  343,419 B, SHA-256 `f2be89c1…22bd94b8`, 8 AEAL claims; 0
  unresolved citations. Three results consolidated: $d=2$
  PROVEN, $d=4$ VERIFIED, general-$d$ CONJECTURED (Conj 3.3.A*).
  Operator action pending: Zenodo upload via the runbook in
  the session folder.
- **🆕 T3 Painlevé test (007) — `T3_LABELED_60_OF_60`.** All
  60 families algorithmically labelled. $d=2$ uniformly
  `P_III(D_6)` (10/10); $d=3$ uniformly `PAINLEVE_UNCLASSIFIED`
  (50/50; rank $4/3$ at $0$, rank $2/3$ at $\infty$). V_quad
  sanity check PASSES as `P_III(D_6)`, matching the CT v1.3
  §3.5 algebraic identity. **H3 negatively closed:** the
  algorithmic test on the linear OGF ODE is sign-of-$\Delta_b$
  invariant and cannot reproduce the PCF-1 v1.3 §3 dichotomy
  ($A=4$ for $\Delta>0$, $A=3$ for $\Delta<0$).

### 2.3 In-flight / open

- 14 prompts staged at `tex/submitted/control center/prompt/`
  (001–007 + 009/010/012/013/014/015 drafted/fired; 008 + 011 reserved;
  🆕 016 drafted post-010 PARTIAL — refit-only S_2 extraction). See §6
  for current status.
- **10 fired this cycle:** 001 ✅, 003 ✅, 004 ✅, 005 ✅, 006* 🛑, 007 ✅,
  010* 🟡, 012 ✅, 013* 🛑, **014 ✅ (NEW)**. *006 HALT, *010 PARTIAL,
  *013 HALT (gate `CC_BOREL_009_NOT_AVAILABLE` fired correctly — see
  "HALTED" / "PARTIAL" lines below).
- 🆕 **2 fired and PARTIAL this cycle:** 009 (verdict `G15_PARTIAL`;
  Φ_resc + Φ_shift pinned; Φ_symp residual on Okamoto Lax pair) and
  **010** (verdict `G6B_PARTIAL_HIGHER_ORDER_NEEDED`; |S_1| differs
  across dichotomy without structural pattern; β_R=0 universal at
  d=2 — NEW G19; S_2 extraction queued via 016).
- **3 fired and HALTED this cycle:** 002 (verdict
  `ARXIV_MIRROR_HALTED_PAGE_COUNT_DRIFT_2`), 006 (verdict
  `AMBIGUOUS_AT_DPS8000` — *now superseded in the soft branch by 014's
  PASS_A_EQ_6_ONLY*), and 013 (verdict
  `CC_BOREL_009_NOT_AVAILABLE` — *gate working as designed*; refire
  pending Q21 path-(a) vs path-(b) decision). See §6.
- **0 remaining ready-to-fire from the original 7-prompt queue**
  (006 + 010 both landed).
- **1 drafted-ready math-closure prompt remains** in the original
  012/013 batch: 013 (P-CC formal closure; gated on full G15 closure
  via 015; *currently HALTED awaiting refire path*). 012 has
  **graduated to ✅ DONE** (G2 closed at d=3 across 3 Galois bins).
- **1 drafted-ready retry prompt remains:** 🆕 **016**
  (T36-S2-EXTRACTION; refit-only; gates G6b full closure via
  S_2 alien amplitude). 014 has **graduated to ✅ DONE** (G5+G16
  closed in A=6-only branch via PASS_A_EQ_6_ONLY at $|\delta| \sim 10^{-23}$).
- 🆕 **1 drafted but operator-gated prompt:** 015 (T25E-VQUAD-PIII-
  NORM-MAP-CLOSE; ~2–4 hr; gated on R5 = Okamoto 1987 §§2–3 Lax
  pair via the G3b ILL/AMS workflow).
- **t1-phase-2-bt-apply** (Prompt 008, conditional; not yet
  drafted) is BLOCKED on primary-source acquisition + Claude's
  H1 label arbitration.
- **pcf1-v13-reconcile** (Prompt 011, future) — operator
  decision required: bump to v1.4 OR recover v1.3 source
  snapshot. Gates 002.
- ~28 SQL todos pending; ~26 done; 1–3 blocked (55 total at v1.9;
  prompt-014-fire marked done post-cycle; 2 new pending
  follow-ups for Q22/Q23 added; pcf2-v1-4-deposit-decision-q22-gated
  added as new blocked todo).

### 2.4 Recently closed (this cycle)

- ✅ Zenodo "New version" upload of CT v1.3 (operator).
- ✅ Post-publish metadata polish (TIER 1 description supersede
  line + TIER 2 stale related-identifier cleanup).
- ✅ Submission-log Items 17 + 18 + **19** spliced
  (PCF-2 v1.3 + umbrella v2.0 + **CT v1.3** — Item 19 via
  Prompt 001 today).
- ✅ RESUME cheat-sheet updated.
- ✅ Strategic prompt queue drafted (4 new prompts 004–007).
- ✅ T1 Phase 1 lit review verdict landed (003).
- ✅ D2-NOTE v1.0 drafted (004); awaits operator Zenodo upload.
- ✅ T3 Painlevé test (007) — 60/60 LABELED; H3 negatively
  closed; V_quad sanity confirmed.
- ⚠ Prompt 002 partially built (4/5 records OK; PCF-1 HALT).
- 🆕 ✅ **Prompt 005 PASSED at 108 digits** (forecast 30–50).
  M6 achieved. β=0 logarithmic-class refinement (consistent
  with H4 hedge); V_quad-native Stokes amplitude measured.
- 🆕 🛑 **Prompt 006 HALTED — `AMBIGUOUS_AT_DPS8000`.** A=6
  empirically supported across all 4 j=0 cubic families with
  $A_\text{lin} = 6 \pm 2 \times 10^{-7}$ and monotone-decreasing
  $|\delta_\text{lin}|$ as $N_\max$ grows; LIN/EXP 5-param
  agreement of $\sim 2.3 \times 10^{-6}$ trips the 30-digit
  spec threshold. Compute was 35 s (vs 6–10 hr estimate).
  M7 not formally achieved; closure deferred to Prompt 014
  (refit with 13-param ansatz on saved CSVs).
- 🆕 🟡 **Prompt 009 PARTIAL — `G15_PARTIAL`.** V_quad scalar ODE
  re-derived from scratch (sympy-exact: $3z^3 f'' + 10z^2 f' +
  (5z + z^2 - 1) f = 0$); Newton-polygon slope $1/2$; $c =
  \pm 2/\sqrt{3}$; $\rho = -11/6$ — all exact rationals/algebraics
  matching CT v1.3 §3.5. Φ_resc parameter $\lambda = 1/3$ pinned
  (R3-conditional). Φ_shift Jacobian $= 1$. Φ_symp **residual**
  on R5 (Okamoto 1987 §§2–3 Lax pair, not in local library).
  $C_\text{can}$ deliberately *not* numerically computed (no
  fabrication; prompt forbids). Substantive structural finding:
  V_quad scalar ODE vs $P_{III}(D_6)$ Hamiltonian live at
  different layers (L-equation vs isomonodromic deformation
  thereof). M6 canonical-form completion deferred to Prompt 015
  once R5 acquired.
- 🆕 🟡 **Prompt 010 PARTIAL — `G6B_PARTIAL_HIGHER_ORDER_NEEDED`.**
  Generalised V_quad Birkhoff recurrence to arbitrary $d=2$
  $(\alpha, \beta, \gamma, \delta, \epsilon)$ via sympy
  derivation (cross-validated: re-derives V_quad's 108-digit $C$
  to all displayed digits). Extracted $S_1 = 2\pi i C$ for four
  representatives at dps $\le 250$, $N \le 2000$, ≥ 60-digit
  cross-method agreement: V_quad $C=+8.127\ldots$, QL15
  $C=+21.384\ldots$ ($\Delta<0$); QL05 $C=+1.403\ldots$, QL09
  $C=-6.075\ldots$ ($\Delta>0$). $|S_1|$ differs across the
  dichotomy at $O(1)$ scale; no structural pattern (sign(C)
  varies within $\Delta>0$ side; all $S_1$ purely imaginary;
  within-side spread comparable to cross-side spread). **NEW
  universal structural fact (G19):** $\beta_R = 0$ to ≥ 85
  digits across all four reps — alien amplitudes live exactly
  on $\Gamma(n)$ with no $\Gamma$-shift at $d=2$. Closure path
  through Prompt 016 ($S_2$ extraction; ~30 min refit on cached
  CSVs).
- 🆕 ✅ **Prompt 012 PASSED — `G2_CLOSED_AT_D3`.** XI0-D3-DIRECT
  ran a per-Galois-bin Newton-polygon test on cubic representatives
  drawn from `cubic_family_catalogue.json` (PCF2-SESSION-A). Two
  complementary tests at dps=80: (A) algebraic characteristic-root
  of $L = 1 - z B(\theta+1) - z^2$ along the slope-$1/3$ edge,
  (B) numerical Borel-singularity ladder via the $Q_n$ recurrence
  at $N \in \{500, 1000, 1500\}$. All **K=3 bins** (`+_C3_real`
  family 19 $b = n^3 - 3n^2 + 1$; `+_S3_real` family 14
  $b = n^3 - 3n^2 - n + 1$; `-_S3_CM` family 50 $b = n^3 - 2n^2 - 1$)
  verify $\xi_0 = 3 / \alpha_3^{1/3}$ to **80 algebraic digits**.
  Numerical ladder: 3.18, 3.18, 3.35 digits at $N=1500$, consistent
  with $O(1/N)$ subleading. Aggregate verdict `G2_CLOSED_AT_D3`
  (3/3 AGREE). 5 AEAL claims (3 per-bin + summary + Galois-bin
  coverage); empty halt/discrepancy/unexpected logs. **Compute:
  ~25 min agent.** D2-NOTE Conj 3.3.A* now empirically-supported
  at $d \in \{2, 3, 4\}$; Q20 surfaced re possible **PROVEN**
  upgrade by Newton-polygon theorem.
- 🆕 🛑 **Prompt 013 HALTED — `CC_BOREL_009_NOT_AVAILABLE`** (gate
  fired correctly, *not* a failure). CC-FORMAL-BOREL-CLOSE was
  hard-gated on 009 returning `G15_CLOSED`; 009 is `G15_PARTIAL`
  with R5 unresolved. The relay agent inspected the upstream
  session, triggered the named halt clause **before any phase
  ran**, and produced no Borel sum / closed-form / canonical
  Stokes constant. CT v1.3 §3.5 status was **not** flipped.
  1 AEAL halt-record claim with upstream hashes pinning 005 + 009
  inputs. **Discipline working as designed.** Refire path is
  Q21-arbitrated (path (a) full G15 via 015, or path (b)
  symbolic-only PARTIAL).
- 🆕 ✅ **Prompt 014 PASSED — `PASS_A_EQ_6_ONLY`.** T25D-RETRY-13PARAM
  refit the saved $j=0$ cubic $y_n$ series (Q_30..Q_33; dps=25000;
  $N$ up to 1200) with an 11-parameter LIN ansatz ($K_\text{FIT}=7$,
  *not* 9 — judgment call documented in `discrepancy_log.json`,
  Q22 surfaced) via square-exact `mp.lu_solve` at workdps=4000.
  Per-family $|\delta_\text{lin}|$: $\{3.27, 3.16, 11.9, 30.9\}
  \times 10^{-24}$ (max $|\delta| = 3.09 \times 10^{-23}$). PSLQ
  Phase D on a 17-member deduplicated H6 Chowla–Selberg basis
  B19+ at maxcoeff $= 10^{50}$, tol $= 10^{-40}$ returns **no
  relation** on any of 4 families — i.e., no $\Gamma(1/3)$
  Chowla–Selberg amplitude closure detected at this precision.
  Reading: **A = 6 to PSLQ-detection precision** in the H6 B19+
  basis. Tail-window cross-check (7-pt vs 11-param) and Richardson
  cross-check (sign-and-magnitude of trend, not at $10^{-10}$ —
  Phase E spec impedance documented). 12 AEAL claims; halt log
  contains verdict + summary; G5 + G16 closed in the **A=6-only**
  branch. *Stretch goal $|\delta| < 10^{-30}$ NOT met (would require
  $K_\text{FIT}=9$ and fresh $y_n$ at $N \le 2400$, dps $\ge 44{,}300$).*
  Q22 (closure-threshold acceptance) + Q23 (PSLQ basis hygiene)
  surfaced. PCF-2 v1.4 §6 amendment drafted (`pcf2_v1.4_amendment.md`,
  Phase F output). M7 ✅ achieved in soft branch.

---

## 3. Programs to Prove (six)

| Tag | Program | Closes via | Status |
|-----|---------|------------|--------|
| **P-NP**  | Newton-polygon universality $\xi_0=d/\beta_d^{1/d}$ at all $d \ge 2$ | D2-NOTE (Prompt 004) for $d=2,4$; XI0-D3-DIRECT (Prompt 012) ✅ for $d=3$; downstream proof for general $d$ | $d=2$ PROVEN; $d=4$ VERIFIED; $d=3$ ✅ **EMPIRICAL at 80 algebraic digits across 3 Galois bins** (Prompt 012 verdict `G2_CLOSED_AT_D3`); general-$d$ CONJECTURED — Q20 surfaces possible PROVEN upgrade for *all* $d \ge 2$ via Newton-polygon theorem |
| **P-B4**  | Conjecture B4: $A_n(b) = 2d$ unsplit at $d \ge 3$ | T1 Phase 1 lit review (003) ✅ → Phase 2 B-T application (BLOCKED on primary sources + H1 arbitration) | EMPIRICAL d=3,4; LITERATURE BRACKET $A \in [d, 2d]$; H1 fleet label DISPUTED |
| **P-CC**  | $V_{\mathrm{quad}} \to P_{\mathrm{III}}(D_6)$ formal closure (channel theory) | H4 execution (Prompt 005) ✅ → V_quad → P_III(D_6) normalization map (Prompt 009) 🟡 PARTIAL → V_quad-PIII-NORM-MAP-CLOSE (Prompt 015, R5-gated) → CC-FORMAL-BOREL-CLOSE (Prompt 013) 🛑 HALTED on 009 gate (correct behaviour) → `op:cc-formal-borel` | algebraic identity DONE (CT v1.3 §3.5); Stokes-side **MEASURED** in V_quad native normalization at 108 digits (Prompt 005); G15 PARTIAL: Φ_resc ($\lambda=1/3$) + Φ_shift pinned, Φ_symp residual on R5 (Okamoto 1987 Lax pair); 013 correctly halted on gate `CC_BOREL_009_NOT_AVAILABLE` — refire pending Q21 path (a) full G15 via 015 / (b) symbolic-only PARTIAL; canonical-form $C_\text{can}$ pending Prompt 015 |
| **P-PET** | Petersson modular discriminant axis as the canonical $d=3$ stratification coordinate | T2 PASSED; T2.5d (Prompt 006) attempted j=0 closure → HALTED at 7-digit precision; T2.5d-RETRY (Prompt 014) ✅ closed j=0 endpoint at $|\delta| \sim 10^{-23}$ in the A=6-only branch | T2 PASSED; $j=0$ ✅ **A=6 to PSLQ-detection precision, no Chowla–Selberg amplitude correction in H6 B19+** (Prompt 014 verdict `PASS_A_EQ_6_ONLY`; max $|\delta_\text{lin}| = 3.09 \times 10^{-23}$); 30-digit *stretch-goal* closure deferred to Q22 path-(b) (14b refit at $K_\text{FIT}=9$ with extended $y_n$) |
| **P-PIII** | Painlevé reduction landscape at $d=2$ and $d=3$ (per-family classification) | T3 Conte–Musette test (007) ✅ → T3.5 Stokes-multiplier S_1 (Prompt 010) 🟡 PARTIAL → T3.6 S_2 alien amplitude (Prompt 016, drafted; refit-only) | $d=2$ uniformly `P_III(D_6)`; $d=3$ uniformly `PAINLEVE_UNCLASSIFIED`; **H3 negatively closed** (Conte–Musette test is sign-of-$\Delta$ invariant); 010 PARTIAL: $|S_1|$ separates the two sides at $O(1)$ scale but *no structural pattern* at the leading scale; G19 side-finding $\beta_R = 0$ universal at $d=2$; G6b closure via Prompt 016 |
| **P-MC**  | Master conjecture: $\Phi$ classifies PCF asymptotics | Gated on P-NP + P-B4 + P-CC | NOT YET FORMALLY STATED |

---

## 4. Milestones to Reach

```
M1: D2-NOTE drafted (xi_0 universality)  ✅ DRAFTED 2026-05-02 (Prompt 004)
    d=2 (PROVEN) + d=4 (VERIFIED) consolidated   ⏳ AWAITS OPERATOR ZENODO UPLOAD
    general-d (CONJECTURED 3.3.A*) recorded
    [PDF sha256 f2be89c1…22bd94b8, 4pp]

M2: General-d xi_0 proof in print     ◀──── (downstream)
    [post-D2-NOTE; not yet a prompt]

M3: T1 Phase 1 — B-T lit review + gap-prop A in [psi_lower, psi_upper]
    ✅ COMPLETE 2026-05-02 (Prompt 003) — verdict T1_PHASE1_GAPTYPE_C
    Literature bracket: psi_lower(d) = d, psi_upper(d) = 2d
                          │
                          ▼
M4: T1 Phase 2 — B-T applied to delta_n recurrence
    proves Conjecture B4 at d >= 3
    🛑 BLOCKED on:
       (a) operator primary-source acquisition (B-T 1933 Acta Math vol 60;
           Adams 1928; Wasow 1965 §X.3) — see § 5 G3b
       (b) Claude H1-label arbitration — see § 5 G11
    [conditional Prompt 008, target: lift psi_lower from d to 2d]

M5: V_quad -> P_III(D_6) algebraic identity              [DONE — CT v1.3]
                          │
                          ▼
M6: V_quad alien amplitude S_{zeta*} measured at 30+ digits
    ✅ COMPLETE 2026-05-02 (Prompt 005) — verdict H4_EXECUTED_PASS_108_DIGITS
    Headline: cross-method agreement 108 digits (forecast 30-50);
              C = 8.12733679...; S_{zeta*} = 2 pi i C ~ 51.0656 i;
              beta = 0 (logarithmic Borel singularity, refines H4).
    Caveat: measurement is in V_quad native normalization;
            canonical P_III(D_6) form PARTIAL via Prompt 009
            (Φ_resc + Φ_shift pinned; Φ_symp residual on R5 =
            Okamoto 1987 §§2-3 Lax pair). Full closure via
            Prompt 015 once operator acquires Okamoto 1987 +
            Conte-Musette ch. 7 (G3b workflow).
    [Prompt 005 ✅ DONE; Prompt 009 🟡 PARTIAL; Prompt 015 drafted]
                          │
                          ▼
M7: j=0 Chowla–Selberg Gamma(1/3) closure (or A=6 artefact ruled out)
    ✅ COMPLETE 2026-05-02 (Prompt 014) — verdict PASS_A_EQ_6_ONLY
       (in soft branch: |delta_lin| <= 3.09e-23 across 4 j=0 cubic
        families; PSLQ on H6 B19+ at maxcoeff=1e50/tol=1e-40 returns
        no Gamma(1/3) relation in any family)
    🛑 INTERIM (Prompt 006) — verdict AMBIGUOUS_AT_DPS8000
    Headline: 11-param LIN refit on saved Q_30..Q_33 y_n CSVs
              (dps=25000, N up to 1200; K_FIT=7 not 9 — judgment
              call) reaches max |delta| = 3.09e-23, well below
              the 1e-15 minimum target with 8+ orders of margin.
              PSLQ on 17-member deduplicated H6 Chowla-Selberg
              basis B19+ exhausts at PSLQ-detection precision
              with no Gamma(1/3) closure detected.
    Reading:  A = 6 to PSLQ-detection precision in H6 B19+;
              j=0 endpoint closes in the "A=6 only" branch.
              No detected Chowla-Selberg amplitude correction.
              Stretch goal |delta| < 1e-30 NOT achieved (would
              require K_FIT=9 with extended y_n at N up to 2400,
              dps >= 44300).
    Caveat:   Soft-branch closure: Q22 (operator) decides
              whether |delta| ~ 1e-23 + no-Chowla-Selberg-relation
              formally closes G5+G16 for PCF-2 v1.4 deposit
              (path (a): deposit now), or whether the stretch
              goal must be hit first (path (b): fire 014b).
              Trivial gamma-reflection identity in literal 18-basis
              flagged as Q23 PSLQ basis hygiene rule (CS_sqrt3
              equiv to sqrt(3)/3 via Gamma(1/3)Gamma(2/3)=2pi/sqrt(3)).
    Closure:  pcf2_v1.4_amendment.md drafted as Phase F output;
              Zenodo deposit gated on Q22 path-(a) acceptance.
    [Prompt 014 ✅ DONE; PCF-2 v1.4 deposit pending operator]
                          │
                          ▼
M8: D=2 Painlevé classification table (per-family, ~10 families)
    ✅ COMPLETE 2026-05-02 (Prompt 007) — verdict T3_LABELED_60_OF_60
    Headline: 10/10 d=2 LABELED (P_III(D6) uniformly);
              50/50 d=3 LABELED (PAINLEVE_UNCLASSIFIED uniformly).
    Caveat: H3 negatively closed (test sign-of-Delta invariant;
            cannot reproduce PCF-1 dichotomy → needs Stokes-mult
            follow-up at M8b).

M8b: 🆕 Stokes-multiplier discrimination (per-family, with
     t2c-style precision escalation) to resolve the PCF-1
     sign-of-Delta dichotomy below the Painlevé-class scale
     [future Prompt 010, INDEPENDENT]
                          │
                          ▼
M9: SIARC-MASTER-V0 announcement — Phi formally stated and the
    master classification result conditional on P-NP + P-B4 + P-CC
    [downstream; gated on M2 + M4 + M6]
    NB: M9 is one step further out under v1.1 because M4's path
    now requires primary-source resolution before Phase 2 can
    even start.
```

Each milestone has a hash-anchored AEAL exit criterion (claim
lines added to `claims.jsonl`, `output_hash` = SHA-256 of the
canonical artefact).

---

## 5. Gaps to Mitigate

| ID | Gap | Severity | Closes via |
|----|------|---------|------------|
| **G1**  | $\xi_0$ universality not proven at general $d$ (only $d=2$ proven; $d=4$ verified) | HIGH | ✅ Prompt 004 drafted — *closure pending Zenodo upload*; downstream M2 still open |
| **G2**  | $\xi_0$ at $d=3$ not directly verified at high dps (`op:xi0-d3-direct`) | MED  | ✅ **CLOSED 2026-05-02** (Prompt 012 verdict `G2_CLOSED_AT_D3`; 80 algebraic digits across all K=3 Galois bins of the cubic catalogue; `xi_0 = 3 / α_3^{1/3}` confirmed via Newton-polygon characteristic-root test). **Q20 footnote:** the operator-level argument depends only on $\alpha_3$ and may upgrade Conj 3.3.A* DEFERRED → PROVEN at $d=3$ (and EMPIRICAL → PROVEN at $d=4$) by Newton-polygon theorem; Claude arbitration territory. |
| **G3a** | Conjecture B4 ($A_n = 2d$) literature bracket $A \in [d, 2d]$ established (was: "lacks proof") | HIGH | ✅ T1 Phase 1 complete (003); literature bracket pinned, Adams reading favored by empirics |
| **G3b** 🆕 | Wasow-vs-Adams normalization match unresolved from secondary sources (BLOCKER for Phase 2) | HIGH | Operator: ILL/AMS request for B-T 1933 + Adams 1928 + Wasow §X.3 → Phase 2 (Prompt 008, future) |
| **G4**  | $V_{\mathrm{quad}}$ alien amplitude $S_{\zeta_*}$ is a *theoretical prediction* (H4), not a measurement | HIGH | ✅ **Prompt 005 PASSED 2026-05-02** — measured at 108 digits in V_quad native normalization. Canonical-form value awaits G15. |
| **G15** 🆕 | V_quad → P_III(D_6) normalization map for Stokes data not written out (CT v1.3 §3.5 only matches at Painlevé-class level) | HIGH | 🟡 PARTIAL 2026-05-02 (Prompt 009 verdict `G15_PARTIAL`): Φ_resc ($\lambda=1/3$) + Φ_shift Jacobian pinned; Φ_symp residual on R5 (Okamoto 1987 §§2–3 Lax pair, not in local library); 5 residuals R1–R5 documented; full closure via Prompt 015 (drafted-ready, gated on operator G3b literature acquisition) |
| **G5**  | $j=0$ amplitude finite-$N$ ambiguity (`op:j-zero-amplitude-h6`); $A \to 6$ vs $\Gamma(1/3)$ closure | MED  | ✅ **CLOSED 2026-05-02 in A=6-only branch** (Prompt 014 verdict `PASS_A_EQ_6_ONLY`; $|\delta_\text{lin}| = 3.09 \times 10^{-23}$ across all 4 j=0 cubic families via 11-param refit; PSLQ on H6 B19+ at maxcoeff $10^{50}$ / tol $10^{-40}$ returns no $\Gamma(1/3)$ relation in any family). Soft-branch closure: stretch-goal $|\delta| < 10^{-30}$ deferred to Q22 path-(b). |
| **G6a** | Conte–Musette algorithmic Painlevé test on $d=2,3$ catalogues | MED  | ✅ Prompt 007 complete (60/60 LABELED) |
| **G6b** 🆕 | PCF-1 v1.3 §3 sign-of-$\Delta_b$ dichotomy ($A=4$ vs $A=3$) lives below the Painlevé-class resolution scale; Conte–Musette test is invariant under sign of $\Delta_b$ | MED | 🟡 PARTIAL 2026-05-02 (Prompt 010 verdict `G6B_PARTIAL_HIGHER_ORDER_NEEDED`): $|S_1|$ measured at ≥ 60 cross-method digits for 4 reps (2-of-each-side); values differ at $O(1)$ scale but display no structural pattern at the leading scale; full closure via Prompt 016 (S_2 alien amplitude; ~30 min refit on cached CSVs) |
| **G7**  | Master functor $\Phi$ (P-MC) not formally stated | HIGH | Downstream (gated on M2+M4+M6) |
| **G8**  | D2-NOTE not yet a citable artefact ($\xi_0$ result scattered across PCF-1 + CT) | LOW–MED | ✅ Prompt 004 drafted — *closure pending Zenodo upload* |
| **G9**  | arXiv mirroring not done (5 records); visibility gap | LOW  | Prompt 002 — 🛑 HALTED 2026-05-02 (page-count drift on PCF-1; staged locally, not pushed); reactivate after G12+G13+G14 |
| **G10** | AEAL methodology paper (D7) not drafted; the program's epistemic discipline is undocumented externally | LOW  | Future Prompt 009 (deferred) |
| **G11** 🆕 | Theory-Fleet H1 verdict `B4_PROVED_AT_d≥3` flagged as heuristic-grade by T1's primary-literature reading; not yet arbitrated | HIGH | Claude / synthesizer arbitration pass on T1 handoff.md |
| **G12** 🆕 | PCF-1 v1.3 source drift: workspace `p12_journal_main.tex` rebuilds to 21 pp; Zenodo v1.3 PDF is 16 pp; v1.4 working draft has likely overwritten the v1.3 snapshot | HIGH | Future Prompt 011 (PCF1-V13-RECONCILE) — operator decision: (a) bump to v1.4 deposit & re-run 002 vs v1.4 DOI, OR (b) recover v1.3 16pp source snapshot from git history / Zenodo archive |
| **G13** 🆕 | Channel Theory v1.3 source carries `\author{The SIARC author}` literal placeholder — arXiv will reject record #4 | HIGH | Operator: replace with real-name+affiliation block already used in PCF-2 v1.3 / umbrella v2.0; verify via grep on `tex/submitted/` |
| **G14** 🆕 | Endorsement-request templates for math.NT records #2, #4 are skeletons; no real endorser arXiv handles populated | MED  | Operator: identify ~3 plausible math.NT endorsers, look up their arXiv user-id strings, populate the two templates |
| **G16** 🆕 | **Spec-vs-precision-floor mismatch** — 5-parameter $1/n$ ansatz at $N=1200$ caps $A$-fit precision at $\sim 7$ digits (model truncation $O(1/N^2)$); the 30-digit formal threshold required by `op:j-zero-amplitude-h6` needs $\geq 13$ parameters. Generalises to any deep-WKB closure operator. | LOW–MED | ✅ **CLOSED 2026-05-02 (in A=6-only branch)** — Prompt 014 demonstrated structural fix (11-param LIN refit reaches $|\delta| \sim 10^{-23}$; PSLQ on H6 B19+ exhausts at PSLQ-detection precision with no relation). Op-design lesson: future deep-WKB operators should pre-compute parameter-count floor from desired digit threshold ($k \ge \text{digits}/\log_{10}N - 1$) — Q15 (carried). |
| **G17** 🆕 | **Layer separation**: V_quad scalar OGF ODE (linear; Hamiltonization quadratic in $p$) vs canonical $P_{III}(D_6)$ Hamiltonian (nonlinear in $(q,p)$) — the two live at *different* geometric layers (L-equation vs its isomonodromic deformation). $\Phi$ acts on Lax-pair monodromy data, not on $(f, f', z)$ directly. CT v1.3 §3.5 implicitly knew this ("algebraic identity at Painlevé-class level only") but does not spell it out. | MED (epistemic / framing) | Operator/Claude decision: should CT v1.4 amend §3.5 to spell out the L-equation vs isomonodromic-deformation distinction? Prompt 015 will treat the layer structure as a working assumption regardless. |
| **G18** 🆕 | **Okamoto-constraint mismatch on $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0) = (1/6, 0, 0, -1/2)$**: the four numbers sum to $-1/3$, not $0$ — the Okamoto $\alpha + \alpha + \beta + \beta = 0$ constraint quoted in the relay-prompt brief is not satisfied. Three interpretations (CT v1.3 internal vs Sakai vs different parametrization). | LOW (convention) | Operator: pin from Okamoto 1987 §2 (R1) once acquired; possibly resolves trivially as a different parametrization convention. Flagged informational, not halt-class. |
| **G19** 🆕 | **Universal side-finding $\beta_R = 0$ at $d=2$**: the Birkhoff resurgent ansatz $a_n \sim C \, \Gamma(n + \beta_R) \, \zeta_*^{-(n+\beta_R)}$ has $\beta_R$ measured to $\le 10^{-85}$ across all 4 d=2 PCF representatives in Prompt 010 (V_quad, QL15, QL05, QL09 — both sides of the $\Delta_b$ dichotomy). Alien amplitudes live exactly on $\Gamma(n)$ with no $\Gamma$-shift. | MED (epistemic / structural) | Synthesizer-formalisation candidate: "alien-amplitude $\Gamma$-shift = 0 universal at $d=2$". Possible link to Sakai-surface / isomonodromic geometry of the $d=2$ catalogue. Operator/Claude decision territory; not a compute task. |

Severity legend:
- **HIGH** — blocks a paper, blocks a downstream proof, or
  affects multiple programs.
- **MED** — affects one program / one open problem.
- **LOW** — visibility / hygiene; does not block mathematics.

---

## 6. Suggested Next Steps — Queued Prompts

Fourteen prompts staged at
`tex/submitted/control center/prompt/`. Cross-references:
prompts close one or more gaps (see § 5) and advance one or more
milestones (see § 4).

| # | Prompt | Closes gap | Advances milestone | Status | Compute | Independent? |
|---|--------|------------|--------------------|--------|---------|--------------|
| 001 | submission-log Item 19 splice | — (admin) | (post-publication hygiene) | ✅ DONE 2026-05-02 | low | — |
| 002 | arXiv mirror runbook (5 records) | G9 | (visibility) | 🛑 HALTED 2026-05-02 (`ARXIV_MIRROR_HALTED_PAGE_COUNT_DRIFT_2`; 4/5 OK; PCF-1 21pp local vs 16pp Zenodo; deliverables staged locally only); reactivate after G12+G13+G14 close | low | gated on G12+G13+G14 |
| 003 | T1 Phase 1 — B-T lit review + gap-prop | G3a | M3 | ✅ DONE 2026-05-02 (verdict GAPTYPE_C) | low (lit work) | — |
| 004 | D2-NOTE — Newton-polygon universality | G1, G8 | M1 | ✅ DRAFTED 2026-05-02 (awaits Zenodo upload) | low (drafting + AEAL re-derivation) | — |
| 005 | H4 / `op:cc-median-resurgence-execute` | G4 | M6 | ✅ DONE 2026-05-02 (`H4_EXECUTED_PASS_108_DIGITS`; β=0 refinement; G15 surfaced) | **HIGH** (mpmath dps 250, $N=5000$) | — |
| 006 | T2.5d — $j=0$ Chowla–Selberg closure | G5 | M7 | 🛑 HALTED 2026-05-02 (`AMBIGUOUS_AT_DPS8000`; A=6 ± 2e-7 across 4 families, monotone-converging; 5-param ansatz caps precision at ~7 digits; spec 30-digit threshold not met) | low (35 s; structurally faster than estimate) | INDEPENDENT |
| 007 | T3 — Conte–Musette Painlevé test on $d=2,3$ catalogues | G6a | M8 | ✅ DONE 2026-05-02 (60/60 LABELED; H3 negatively closed) | medium (symbolic) | — |
| 008 | T1 Phase 2 — B-T applied to $\delta_n$ (proves B4 at $d \ge 3$) | G3b | M4 | 🛑 BLOCKED (G3b primary sources + G11 H1 arbitration); slot reserved | medium | gated |
| 009 | V_quad → P_III(D_6) normalization map (change-of-variables Φ; apply to 005's $C$ to report $S_{\zeta_*}^{\text{can}}$) | G15 (partial), G17, G18 | M6 (canonical-form PARTIAL); 013 now gated on 015 | 🟡 PARTIAL 2026-05-02 (`G15_PARTIAL`; Φ_resc + Φ_shift pinned; Φ_symp residual on R5; substantive layer-separation finding) | low (symbolic; ~75 min agent) | INDEPENDENT |
| 010 🆕 | T3.5 — Stokes-multiplier discrimination (t2c-style high-dps connection coefficients to resolve sign-of-$\Delta_b$ dichotomy) | G6b (partial), G19 | M8b (partial); 016 follow-on | 🟡 PARTIAL 2026-05-02 (`G6B_PARTIAL_HIGHER_ORDER_NEEDED`; \|S_1\| measured for 4 reps at ≥ 60 cross-method digits; differs across dichotomy at $O(1)$ scale; no structural pattern at leading order; β_R=0 universal at d=2) | medium (mpmath dps=250, $N=2000$; ~2 min agent) | INDEPENDENT |
| 011 | PCF1-V13-RECONCILE — operator-decision-driven; resolve PCF-1 v1.3 source drift before re-running 002 | G12 | distribution layer | future (slot reserved; not yet drafted; gated on operator option-(a)/(b) decision) | low | gated |
| 012 🆕 | $\xi_0$ at $d=3$ direct — per-Galois-bin Newton-polygon test of D2-NOTE Conj 3.3.A* on cubic representatives | G2 | (M1 follow-on; supports P-NP) | ✅ **DONE 2026-05-02** (verdict `G2_CLOSED_AT_D3`; 3/3 Galois bins AGREE at 80 algebraic digits; ~25 min agent) | low (mpmath dps=80) | INDEPENDENT |
| 013 🆕 | CC formal Borel close — closed-form $\mathcal{B}[V_{\text{quad}}]$ in canonical $P_{III}(D_6)$ coordinates (composes 005's $C$ + 009's Φ); flips CT v1.3 §3.5 status to "DIAGNOSED" | (P-CC formal closure) | (P-CC final close) | 🛑 **HALTED 2026-05-02** (verdict `CC_BOREL_009_NOT_AVAILABLE`; gate fired correctly on 009 = G15_PARTIAL; ~10 min agent; no Borel sum / canonical $C$ produced; refire pending Q21 path (a) or (b)) | low–medium (symbolic + numerical 3-point) | gated on 009 (currently HALTED) |
| 014 🆕 | T2.5d-RETRY-13PARAM — refit saved $y_n$ CSVs with 13-param ansatz; targets $\|\delta_\text{lin}\| < 10^{-15}$, then runs Phase D PSLQ on Chowla–Selberg basis | G5, G16 | M7 (formal closure) | ✅ **DONE 2026-05-02** (verdict `PASS_A_EQ_6_ONLY`; ~12 min agent; max $|\delta_\text{lin}| = 3.09 \times 10^{-23}$ at $K_\text{FIT}=7$; PSLQ on H6 B19+ at maxcoeff $10^{50}$/tol $10^{-40}$ returns no $\Gamma(1/3)$ relation in any of 4 families; PCF-2 v1.4 §6 amendment drafted; Q22+Q23 surfaced) | low (~12 min agent; pure refit + PSLQ) | INDEPENDENT |
| 015 🆕 | T25E-VQUAD-PIII-NORM-MAP-CLOSE — pins R1–R4 from Okamoto/Conte-Musette; writes Φ_symp from Lax-pair gauge transform; computes $J(\Phi)$ numerically; verifies $S_{\zeta_*}^\text{can}$ against Lisovyy-Roussillon tables to ≥ 50 digits | G15 (full closure), G18 | M6 (canonical-form full closure); unblocks 013 | ✅ DRAFTED 2026-05-02; **GATED on R5** (operator G3b acquisition of Okamoto 1987 + Conte-Musette ch. 7) | low–medium (~2–4 hr agent; symbolic + literature) | gated on operator literature |
| 016 🆕 | T36-S2-EXTRACTION — refit cached `borel_*_dps250_N2000.csv`; subtract leading $C\Gamma(n)\zeta_*^{-n}$; second Richardson pass to extract $S_2$ (alien amplitude at $2\zeta_*$); test ratio $S_2/S_1^2$ for structural invariance; check $|S_2|$ and $\arg(S_2)$ as side-discriminators | G6b (full closure), G19 (cross-check) | M8b (full closure if S_2 discriminates; otherwise S_3 escalation) | ✅ DRAFTED 2026-05-02; ready (no new mpmath series; pure refit on 010's cached CSVs) | low (~30 min agent; refit-only) | INDEPENDENT |

**Concurrency map** (validated this cycle for the original 7-prompt subset):

|        | 001 | 002 | 003 | 004 | 005 | 006 | 007 |
|--------|-----|-----|-----|-----|-----|-----|-----|
| **001** |  —  | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   |
| **002** | ✗   |  —  | ✓   | ✓   | ✓   | ✓   | ✓   |
| **003** | ✓   | ✓   |  —  | ✓   | ✓   | ✓   | ✓   |
| **004** | ✓   | ✓   | ✓   |  —  | ✓   | ✓   | ✓   |
| **005** | ✓   | ✓   | ✓   | ✓   |  —  | ⚠   | ✓   |
| **006** | ✓   | ✓   | ✓   | ✓   | ⚠   |  —  | ✓   |
| **007** | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |  —  |

✗ = dependency; ⚠ = compute-heavy, serialize on a single laptop.

**Concurrency for the 009/010/012/013 batch:** all four are
mutually independent in input data; **013 is hard-gated on 009**
(must wait for verdict `G15_CLOSED`). 009/010/012 can be fired
in parallel with each other and with 006. None of them touches
PCF-1 v1.3 source (no interaction with G12). 010 is the only
member of the batch that is compute-heavy (mpmath dps≥150 on
2-of-each-side dichotomy representatives); 009/012/013 are
low-compute symbolic + light-numerical.

**Recommended firing layout for the *next* compute window
(post-010 PARTIAL + 012 PASS + 013 HALT + **014 PASS**; v1.9 status):**
- Slot 1: **016** (~30 min refit; closes G6b fully if S_2
  discriminates the dichotomy; cross-checks G19 β_R=0 universal).
  Refit-only on 010's cached CSVs; no new mpmath series.
  Highest-leverage tiny-compute slot now.
- Slot 2 (operator-side, runs in parallel with 016):
  **G3b literature acquisition** — Okamoto 1987 §§2–3 (~10 pp)
  + Conte-Musette 2008 ch. 7 §§7.3–7.4 (~25 pp) via the
  existing ILL/AMS workflow. **This unblocks Prompt 015** and
  the full G15 closure path (and via 015, the path-(a) refire of
  013); both are standard library items.
- Slot 3 (operator-side, parallel with 016 + G3b acquisition):
  **PCF-2 v1.4 deposit decision (Q22)** — does $|\delta| \sim
  10^{-23}$ + no-Chowla–Selberg-relation in H6 B19+ formally close
  G5+G16 (path (a): deposit `pcf2_v1.4_amendment.md` on Zenodo
  *now*), or does PCF-2 v1.4 require the $|\delta| < 10^{-30}$
  stretch goal first (path (b): fire 014b at $K_\text{FIT}=9$ with
  extended $y_n$)? *Operator + Claude decision; not a compute task.*
- Slot 4 (after R5 acquired): **015** (T25E-VQUAD-PIII-NORM-
  MAP-CLOSE; ~2–4 hr; closes G15 fully).
- Slot 5 (after 015 lands with `G15_CLOSED`): **013 refire path
  (a)** (formal P-CC closure with numerical 30-digit gate;
  composes 005 + 009 + 015).
- Slot 5 alt (Q21 path (b) — if operator opts for *symbolic-only*
  PARTIAL closure of P-CC now): **synthesizer reformulates 013**
  to a `CC_FORMAL_BOREL_SYMBOLIC_PARTIAL` form (Borel sum modulo
  R2–R5; no numerical gate); fires immediately on the post-009-PARTIAL
  state; no R5 wait. *Faster, ships symbolic-only canonical form;
  weaker than path (a).* Operator + Claude decision.
- ~~Slot for 014~~ — **graduated to ✅ DONE** in this cycle (verdict
  `PASS_A_EQ_6_ONLY` at $|\delta| = 3.09 \times 10^{-23}$; G5+G16
  closed in A=6-only branch).
- ~~Slot for 012~~ — **graduated to ✅ DONE** in prior subcycle
  (verdict `G2_CLOSED_AT_D3` at 80 algebraic digits across 3
  Galois bins).
- **Prompt 002 stays HALTED** until G12 + G13 + G14 are closed.
  Re-fire only against either (a) the new v1.4 DOI for record
  #2 or (b) the recovered v1.3 source snapshot. The other 4
  records' deliverables remain valid and can be reused (their
  hashes are already AEAL-logged in the local
  `ARXIV-MIRROR-RUNBOOK/claims.jsonl`).

**Note (v1.8):** 016 is the natural follow-up to 010's PARTIAL
verdict and reuses 010's cached `borel_*_dps250_N2000.csv` series
(no new high-dps mpmath calls). If 016 also lands PARTIAL (i.e.,
$S_2$ does not discriminate either), the next escalation is to S_3
or to a *basis-convention pinning* prompt (017, future) addressing
Q18's sign-of-C ambiguity before further alien-amplitude work.

**Note (v1.7, carried forward):** 013 is hard-gated on **full G15
closure**, which requires Prompt 015 to land cleanly (i.e., R5
acquired and $S_{\zeta_*}^\text{can}$ verified against
Lisovyy-Roussillon tables). The 009-only `G15_PARTIAL` verdict
does *not* unblock 013 by itself.

Operator-side parallel actions (independent of compute slots):
- **Zenodo upload of D2-NOTE** (operator; ~10 min via the
  upload runbook in `sessions/2026-05-02/D2-NOTE-DRAFT/`).
  Closes G1 + G8 fully on publication; mints the M1 DOI.
- **Item-20 splice prompt** (drafting agent; future) once
  the D2-NOTE Zenodo DOI is minted.
- **Primary-source ILL/AMS request** for B-T 1933, Adams 1928,
  Wasow 1965 §X.3. Unblocks G3b and the future Prompt 008.
- **Send T1 + strategic-picture URLs to Claude** for H1
  label arbitration (G11). Independent of compute.
- **PCF-1 v1.3 source-drift decision (G12)**: pick option
  (a) v1.4 bump or option (b) v1.3 source recovery, then draft
  Prompt 011.
- **CT v1.3 author placeholder fix (G13)**: 1-line edit on
  the source `.tex`; commit; verify by grep.
- **Endorser handle acquisition (G14)**: identify ~3 math.NT
  endorsers from cited authors, look up arXiv user-ids,
  populate the two templates already staged at
  `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/`.

---

## 7. Decision Tree (for synthesizer review)

The intent is to advance *all six programs* in this cycle —
not just one. The reasoning:

1. **004 is independent of 003.** The picture's recommendation
   "just say 'draft D2-NOTE prompt'" makes 004 a parallel free
   action; it closes G1+G8 and yields a citable artefact (M1)
   regardless of T1 outcome.
2. **005 closes G4 conditional on theory holding.** H4 is a
   *theoretical prediction at HIGH confidence*; 005 turns it
   into a measurement. PASS flips `op:cc-formal-borel` from
   PARTIALLY DIAGNOSED to DIAGNOSED. FAIL halts
   `H4_PREDICTION_FALSIFIED` and triggers a reckoning on the
   median-resurgence framing of the channel theory.
3. **003 ✅ landed with verdict `T1_PHASE1_GAPTYPE_C`.** The
   literature gives a bracket $A \in [d, 2d]$, not a proof of
   $A = 2d$. Phase 2's target is now precisely defined: lift
   $\psi_\text{lower}$ from $d$ to $2d$ via the correct
   Wasow-vs-Adams normalization match. **Two new gating items
   were surfaced** — primary sources (G3b BLOCKER) and
   Theory-Fleet H1 label arbitration (G11 HIGH); see § 4 M4
   and § 5.
4. **006 + 007 are independent closures.** They do not gate
   anything else; they're program-internal cleanup that
   strengthens P-PET and P-PIII respectively, without which
   P-MC's invariant triple has visible holes.
5. **001 + 002 are admin** (submission-log + arXiv visibility).
   Mechanical hygiene; cheap and uncontroversial.

**What this cycle CANNOT do** (and therefore is correctly
deferred):
- Prove P-MC (gated on M2 + M4 + M6).
- Prove general-$d$ $\xi_0$ (M2; downstream of D2-NOTE
  publication).
- Apply B-T to $\delta_n$ (M4; gated on primary sources + H1
  arbitration — was: only "downstream of 003").
- Draft the methodology paper D7 (low priority; long-arc).

---

## 8. Open Questions for Synthesizer Review

1. **Are the six programs the right cuts?** Does P-PET deserve
   to be a separate program, or is it actually a *coordinate
   choice* inside P-MC and shouldn't be treated as a standalone
   theorem-track? Argument for separating: the Petersson axis
   has independent empirical content (T2 PASSED) that would
   stand even if P-MC were proven false in some other
   coordinate.
2. **Is M9's gating right?** The current dependency
   M9 ⇐ M2 + M4 + M6 says we need $\xi_0$ universality, B4,
   and Stokes-side closure. Is M7 ($j=0$ closure) truly
   not needed for the master statement, or does P-MC's
   functor $\Phi$ break at $j=0$ without M7?
3. **Should 003 (lit review) and a Phase-2 stub (T1-BT-APPLY)
   be drafted together?** Currently the Phase-2 prompt is
   gated on 003's verdict; an alternative is to draft both in
   parallel and let Phase-2 self-halt on Phase-1 input. The
   latter speeds the keystone but risks Phase-2 thrashing on
   incomplete Phase-1 ground.
4. **D2-NOTE epistemic discipline.** Is folding $d=2$ (proven),
   $d=4$ (verified), and general-$d$ (conjectured) into one
   short note the right balance? An alternative is two notes:
   one PROVEN-only, one CONJECTURED. Argument for one note:
   the $d=4$ verification + general-$d$ conjecture together
   are the *content*; splitting halves the citable value.
5. **The H4 prediction framing.** CT v1.3 §9 lists
   `op:cc-median-resurgence-execute` as a separate open
   problem from `op:cc-formal-borel`. Is keeping them
   distinct correct, or are they actually one item that
   should be merged at v1.4?
6. **Compositio CM 10573 (P12).** Currently a pending todo
   (`compositio-followup`). The picture document treats it
   as low-priority. Is that right, or should it be folded
   into one of the queued prompts?
7. **AEAL methodology paper D7.** Low-priority by current
   ranking. Argument for upgrading: the program now has 5
   Zenodo records + triple-fleet audit + Lean precedent; the
   methodology *story* is well-formed. A single note would
   protect the program against future referee challenges
   on epistemic grounds.
8. 🆕 **(v1.1) Theory-Fleet H1 label arbitration.** T1 Phase 1
   flags `B4_PROVED_AT_d≥3` as heuristic-grade. **Decision
   needed:** does H1 stand as PROVEN, get downgraded to
   HEURISTIC, or get split (proven for some $d$, heuristic for
   others)? *No published artefact is affected by either
   outcome* (CT v1.3 + PCF-2 v1.3 + umbrella v2.0 all cite
   "verified"/"support"), but the SIARC-MASTER-V0 announcement
   gating (§ 4 M9) depends on this resolution.
9. 🆕 **(v1.1) Phase-2 target — $\psi_\text{lower}$-lift
   tractability.** T1 Phase 1 places Phase 2's target at
   "lift $\psi_\text{lower}$ from $d$ to $2d$". **Question:**
   is this a *single*-step proof (one normalization match
   pinning the slope) or a *multi*-step proof (slope match +
   characteristic-exponent doubling + sign analysis)? Affects
   whether Prompt 008 should be drafted as one agent run or
   split into 008a / 008b.
10. **(v1.2) PCF-1 sign-of-$\Delta$ dichotomy resolution.**
    T3 demonstrated that the Conte–Musette algorithmic
    Painlevé test cannot distinguish the two sign branches.
    The PCF-1 v1.3 §3 dichotomy ($A=4$ vs $A=3$) therefore
    lives at the Stokes-multiplier level — *below* the
    Painlevé-class scale. **Question:** is this consistent
    with the CT v1.3 §3.5 V_quad → P_III(D_6) identity
    (which sits at the Painlevé-class scale and is
    sign-invariant), and does it imply that the SIARC
    invariant-triple framing (umbrella v2.0 §4.4) needs a
    *Stokes-data* fourth coordinate beyond
    $(\Delta_d, \|\Delta\|_\text{Pet}, \xi_0)$? If yes,
    P-MC's functor $\Phi$ has more structure than v1.0
    of this picture suggested.
11. **(v1.3) PCF-1 v1.3 release-discipline question.**
    Prompt 002's HALT exposed that the workspace
    `p12_journal_main.tex` has drifted from the published
    v1.3 (16 pp) to a v1.4-in-draft (21 pp) state, *but*
    no v1.4 Zenodo deposit exists yet. **Question:** was
    the operator implicitly aiming at a v1.4 release
    before mirroring to arXiv? If so, the cleanest
    sequence is: (i) publish PCF-1 v1.4 to Zenodo, (ii)
    splice Item 20, (iii) re-run 002 against v1.4. If
    not, option (b) — recover the exact v1.3 source — is
    the disciplined path. The asymmetry matters: v1.4 may
    contain content that has not yet been internally
    AEAL-reviewed.
12. 🆕 **(v1.4) β=0 vs square-root expectation.** Prompt
    005's three independent extractors fit the V_quad
    Borel-singularity branch exponent to **β = 0** to ≥ 107
    digits — i.e., a *logarithmic* singularity, not the
    half-integer "square-root class" that was the leading
    expectation in H4. This sits inside H4's broader
    "algebraic-LOGARITHMIC" hedge, so the prediction is
    refined rather than falsified. **Question:** does the
    logarithmic-class outcome have a *theoretical*
    explanation in the V_quad → P_III(D_6) framing, or is
    it specific to the V_quad case at $d=2$? If the latter,
    Conjecture B4-CC at higher $d$ may need a separate
    branch-class prediction per Galois bin. If the former,
    H4 should be amended to predict β=0 as the canonical
    class (with a caveat about cases where the logarithm is
    structurally absent).
13. 🆕 **(v1.4) Phase D method substitution.** Prompt 005's
    relay agent self-substituted "polynomial LSQ in $1/n$
    at order 40" for the prescribed "local Padé-of-Padé
    Borel fit" because the prescribed method collapses to
    roundoff equality with Phase C when β=0. The
    substitution is documented in the session's
    `rubber_duck_critique.md`. **Question:** is this
    substitution acceptable as a one-off (since the
    cross-method agreement at 108 digits is the
    operative evidence), or should the canonical
    op:cc-median-resurgence operator definition be
    updated to make the Padé-of-Padé branch conditional
    on β ≠ 0? For the synthesizer: this is also a
    case-study of the AEAL-honest substitution pattern —
    deviation from spec was surfaced rather than papered
    over.
14. 🆕 **(v1.6) j=0 empirical-vs-formal gap.** Prompt 006's
    5-param fit gives $A_\text{lin} = 6 \pm 2 \times 10^{-7}$
    on all four j=0 cubic families with monotone-decreasing
    $|\delta_\text{lin}|$ as $N_\max$ grows. This is strong
    *empirical* support for $A_\text{true}=6$ exactly (no
    $\Gamma(1/3)$ closure), but the formal verdict is
    `AMBIGUOUS_AT_DPS8000` because the LIN/EXP 5-param pair
    cannot agree to $10^{-30}$ at $N=1200$ (model truncation
    floor is $O(1/N^2) \sim 10^{-7}$). **Question:** is the
    empirical 7-digit + monotone-convergence signal already
    enough to record `op:j-zero-amplitude-h6` as
    "MEASURED, $A=6$, no $\Gamma(1/3)$ closure" in the
    PCF-2 narrative — *pending* the 13-param refit (Prompt
    014) for the citable 30-digit number — or must the
    formal halt be honored throughout? The published PCF-2
    v1.3 already says "AMBIGUOUS-AT-FINITE-N", so there is
    no published-artefact tension; the question is purely
    about how to phrase pre-014 in any internal status
    document.
15. 🆕 **(v1.6) Spec-design lesson for deep-WKB operators.**
    The literal `dps=8000 ∧ N=1200` reading of Prompt 006
    was *internally infeasible* for an A=6 cubic
    ($|L_N - L_\text{ref}| \sim \exp(-A N \log N)$ requires
    dps $\geq A \cdot N \log N / \log 10$ at $N=1200$ for
    $A=6$ this is $\sim 22{,}150$ digits, not 8000).
    Compute time for the actual run was $\sim 35$ s, not
    6–10 hr. **Question:** should future deep-WKB closure
    prompts pre-compute both (a) the dps floor from
    $A \cdot N \log N$ and (b) the parameter-count floor
    from the digit-threshold target ($k \geq \text{digits} /
    \log_{10} N - 1$)? If yes, this is a structural amendment
    to the AEAL / op-design discipline (carries to all
    future deep-WKB ops).
16. 🆕 **(v1.7) Layer separation between scalar OGF ODE and
    isomonodromic deformation.** Prompt 009's substantive
    structural finding: V_quad's scalar OGF ODE is the
    **L-equation** of an isomonodromic Lax pair (linear,
    frozen at the V_quad parameter point), while $P_{III}(D_6)$
    is the **isomonodromic deformation** of that L-equation
    (nonlinear, in coordinates that are monodromy data of the
    Lax pair). $\Phi$ therefore cannot be a direct
    change-of-variables on $(f, f', z)$ — it acts on the
    Lax-pair monodromy variety. CT v1.3 §3.5's framing
    "algebraic identity at Painlevé-class level only" gestures
    at this layer separation but does not spell it out.
    **Question:** should CT v1.4 amend §3.5 to spell out the
    L-equation vs isomonodromic-deformation distinction
    explicitly? If yes, this is a CT v1.4 amendment candidate
    (operator/Claude decision territory, not agent territory).
    For the synthesizer: this is also the principal reason
    Prompt 015 needs the Lax pair (R5) — the canonical-form
    transform Φ is a gauge transformation on the Lax pair, not
    a coordinate change on the scalar ODE.
17. 🆕 **(v1.7) CT v1.3 §3.5 parameter-convention pinning.**
    The $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0) =
    (1/6, 0, 0, -1/2)$ point quoted in CT v1.3 §3.5 sums to
    $-1/3$, not $0$, so it does *not* satisfy the Okamoto
    constraint $\alpha_\infty + \alpha_0 + \beta_\infty +
    \beta_0 = 0$. Three interpretations (Sakai $E_7^{(1)} /
    D_7^{(1)}$ root data; one entry is a spectral-type label;
    different parametrization convention) are open until R1
    is pinned from Okamoto 1987 §2. **Question:** should CT
    v1.4 explicitly state which convention §3.5 uses? The
    constraint mismatch does not contradict any numerical
    result in CT v1.3, but does block a clean comparison
    against external $P_{III}(D_6)$ Stokes-data tables.
18. 🆕 **(v1.8) Sign-of-$C$ basis-independence.** Prompt 010
    used a uniform Birkhoff convention $c = +2/\sqrt{\alpha}$
    across all four representatives. Under this convention,
    the four leading Stokes amplitudes were $+8.13$ (V_quad,
    $\Delta<0$), $+21.38$ (QL15, $\Delta<0$), $+1.40$ (QL05,
    $\Delta>0$), $-6.07$ (QL09, $\Delta>0$). The $-$ sign on
    QL09 is what breaks the cleanest possible discrimination
    rule "sign$(C)$ flips with sign$(\Delta_b)$". **Question:**
    is sign$(C)$ a basis-independent invariant in the resurgent
    classification, or does it depend on which root of $c^2 =
    4/\alpha$ is named the "$+$" branch? In particular, the
    Birkhoff series $f_+ = e^{+c/u} u^\rho S_+$ has a partner
    $f_-$ with the opposite $c$-sign; the alien amplitude is
    in principle defined up to *the choice* of which solution
    is named $f_+$. If the literature pins a unique convention
    (e.g., principal-branch / Stokes-direction-based) that
    enforces consistent choices across the family, the QL09
    sign disagreement may be a convention artefact rather than
    a structural fact — which would lift G6b's PARTIAL closer
    to a PASS at the leading scale. *This question is Claude
    territory* (literature reading + resurgent-conventions
    arbitration); a numerical follow-up cannot answer it.
19. 🆕 **(v1.8) $\beta_R = 0$ universal at $d=2$ — structural
    consequence?** Prompt 010 measured the Birkhoff branch
    exponent $\beta_R$ in $a_n \sim C\Gamma(n+\beta_R)
    \zeta_*^{-(n+\beta_R)}$ to $\le 10^{-85}$ across all four
    $d=2$ PCF representatives — i.e., the alien amplitudes live
    *exactly* on $\Gamma(n)$ with no $\Gamma$-shift. This is
    not predicted by any prior part of the SIARC framework, and
    it is uniform across both sides of the $\Delta_b$ dichotomy.
    **Question:** is this a structural consequence of the
    $P_{III}(D_6)$ class (e.g., from Okamoto's surface
    $E_7^{(1)}$ / $D_7^{(1)}$ symmetry, or from the rank
    structure of the $d=2$ Birkhoff Newton polygon), or is it
    coincidental at $d=2$? If structural, it generalises a
    known feature of certain isomonodromic cases and could be
    a *new* candidate for formalisation at the SIARC-MASTER-V0
    level. If coincidental, the prediction is that $\beta_R$
    becomes nontrivial at $d=3$ (rank $4/3$ at $0$, $2/3$ at
    $\infty$), which would be a clean experimental test of the
    "structural" hypothesis. Either way, this finding is a side
    result that did not exist before 010 and which Claude may
    want to either formalise (G19) or earmark as a $d=3$
    follow-up probe.
20. 🆕 **(v1.8) Conj 3.3.A* — *proof-upgrade candidate* at
    $d \ge 2$?** Prompt 012's XI0-D3-DIRECT closes $G_2$ at $d=3$
    via a per-Galois-bin Newton-polygon characteristic-root test:
    $|c_\text{root}| = \xi_{0,\text{conj}} = 3 / \alpha_3^{1/3}$
    to **80 algebraic digits** across all K=3 bins. The relay
    agent surfaced a *structural* observation in
    `XI0-D3-DIRECT/handoff.md`: the algebraic test depends only
    on $\alpha_3$ via standard Newton-polygon theorems, and the
    same operator-level argument applies *uniformly* at all
    $d \ge 2$ (the $d=4$ framework PCF2-SESSION-Q1 has the same
    property). If Claude judges the operator-level derivation to
    be a **proof modulo Newton-polygon / irregular-singular-point
    machinery** (Wasow §X, Adams 1928, et al.), then D2-NOTE
    Conj 3.3.A* could be upgraded:
    * $d=2$ already PROVEN (Prompt 004 main theorem).
    * $d=3$ DEFERRED → **PROVEN** (this argument).
    * $d=4$ EMPIRICAL → **PROVEN** (same argument).
    * general $d \ge 2$ CONJECTURED → **PROVEN** (uniform argument).

    This would close $G_1 + G_2$ in the *strongest* sense for
    *all* $d \ge 2$ simultaneously, and unblock M2 ahead of
    schedule. **Question:** does Claude judge the
    Newton-polygon characteristic-root argument as a proof in
    the SIARC publication standard (modulo a single citation to
    standard NPT machinery), or is it still empirical-grade and
    requires explicit theorem statement + proof in D2-NOTE-V2?
    The DO-NOT clause in Prompt 012 forbade modifying D2-NOTE in
    012's session; a future PROMPT-012-AMENDMENT could draft the
    upgrade for Zenodo if Claude says yes. *This question is
    Claude territory; the relay agent declined to self-promote
    in 012 per the DO-NOT clause.*
21. 🆕 **(v1.8) Prompt 013 refire path — (a) full G15 vs (b)
    symbolic-only PARTIAL.** Prompt 013 (CC-FORMAL-BOREL-CLOSE)
    halted on its 009-gate `CC_BOREL_009_NOT_AVAILABLE` — *as
    designed*. The refire requires an operator + Claude decision:
    **path (a)** acquire Okamoto 1987 §§2–3 + Conte-Musette 2008
    ch. 7 (G3b workflow), refire Prompt 015 to lift 009 to
    `G15_CLOSED`, then refire 013 unchanged with the original
    numerical 30-digit gate; produces a **fully numerical**
    canonical-form Borel sum + canonical Stokes constant
    $S_{\zeta_*}^{\text{can}}$ verified against Lisovyy-Roussillon
    tables; **stronger** result; gated on literature acquisition
    timeline. **Path (b)** synthesizer reformulates 013 to accept
    `G15_PARTIAL` by writing the Borel sum **symbolically modulo
    R2–R5**, landing at `CC_FORMAL_BOREL_SYMBOLIC_PARTIAL` with
    *no* numerical gate; **faster** result; ships
    canonical-coordinate Borel formula as a symbolic expression
    with explicit "pending Lax-pair closure" prose; unblocks the
    rest of the channel-theory roadmap immediately. The relay
    agent surfaced both paths in `CC-FORMAL-BOREL-CLOSE/handoff.md`
    "What would have been asked"; the choice is operator + Claude
    territory and depends on whether (i) CT v1.4 ships *now* with
    a symbolic canonical-form Borel sum, or (ii) waits for the
    full numerical closure. *No mathematical content is at risk
    either way* — both paths are AEAL-honest and both refuse to
    fabricate $S_{\zeta_*}^{\text{can}}$. **Question:** which
    path does the operator/synthesizer prefer?
22. 🆕 **(v1.9) Prompt 014 closure-threshold acceptance for PCF-2
    v1.4.** Prompt 014's verdict `PASS_A_EQ_6_ONLY` reaches max
    $|\delta_\text{lin}| = 3.09 \times 10^{-23}$ across all 4 j=0
    cubic families with PSLQ on the 17-member deduplicated H6
    Chowla–Selberg basis B19+ returning **no relation** (i.e., no
    $\Gamma(1/3)$ closure detected). This clears the prompt's
    minimum target $|\delta| < 10^{-15}$ with **8 orders of margin**
    and exhausts the H6 B19+ basis at PSLQ-detection precision.
    However, the *stretch goal* $|\delta| < 10^{-30}$ was **not**
    achieved (would require regenerating $y_n$ at $N \le 2400$
    with dps $\ge 44{,}300$ and $K_\text{FIT}=9$ instead of $7$ —
    a fresh $\sim 30$-min `cf_value` compute). The 014 agent's
    `pcf2_v1.4_amendment.md` (Phase F) drafts the §6 amendment
    wording for PCF-2 v1.4 deposit, but flags this as **operator
    decision territory**. **Question:** does Claude/operator
    accept the soft-branch closure ($|\delta| \sim 10^{-23}$, no
    H6 relation) as **formally sufficient** to flip PCF-2 §6
    `AMBIGUOUS-AT-FINITE-N` → `A = 6 to PSLQ-detection precision,
    no detected Chowla–Selberg amplitude correction in H6 basis`
    (path (a): deposit `pcf2_v1.4_amendment.md` to Zenodo *now*),
    **or** does the citable wording require the stretch-goal
    precision $|\delta| < 10^{-30}$ first (path (b): fire a new
    Prompt 014b with $K_\text{FIT}=9$ + extended $y_n$ + $N \le 2400$,
    landing the full-13-param closure at the originally-spec'd
    precision)? *No mathematical content is at risk either way*
    — both paths are AEAL-honest; the question is purely about
    citable-publication threshold semantics. The 006 + 014 series
    of empirical evidence (5-param 7-digit + 11-param 23-digit +
    PSLQ basis exhausted) is *already* the strongest empirical
    argument the program has produced for the j=0 endpoint to
    date.
23. 🆕 **(v1.9) PSLQ basis hygiene rule for deep-WKB closures.**
    Prompt 014's literal 18-member B19+ basis (specified in the
    relay-prompt brief) contained both $\sqrt{3}$ and
    $\Gamma(1/3)\Gamma(2/3)/(2\pi)$. These are $\mathbb{Q}$-equivalent
    via the gamma-reflection identity $\Gamma(1/3)\Gamma(2/3) =
    2\pi/\sqrt{3}$ (so $\Gamma(1/3)\Gamma(2/3)/(2\pi) = 1/\sqrt{3}
    = \sqrt{3}/3$). PSLQ on the literal 18-basis returned the
    **trivial relation** $1 \cdot \sqrt{3} - 3 \cdot \mathrm{CS}_{\sqrt{3}}
    = 0$ (target coefficient $= 0$ — *not* a Chowla–Selberg signal)
    on every family. The relay agent dropped $\mathrm{CS}_{\sqrt{3}}$
    for the verdict-decisive PSLQ run, retaining the literal-18
    run only for traceability. **Question:** should future
    PSLQ-based amplitude-closure prompts (deep-WKB, Chowla–Selberg,
    or similar) include a **basis pre-screen step** in their
    Phase D spec — i.e., apply standard $\mathbb{Q}$-linear
    dependency tests (gamma-reflection / duplication / multiplication
    identities) to the proposed basis and emit the deduplicated
    minimal basis as the operative one for the verdict-bearing
    PSLQ run? This is an op-design hygiene rule, applicable beyond
    014. *Synthesizer territory; codifies a methodology fix that
    avoids the trivial-relation false-positive.*

---

## 9. AEAL Hygiene (this snapshot)

This document makes **no new numerical claims**. All cited
numbers (Spearman correlations, $p$-values, dps levels, page
counts, DOIs, hash prefixes) are quotations of prior AEAL-logged
claims in `siarc-relay-bridge/sessions/<DATE>/<TASK_ID>/claims.jsonl`.
No claim line is emitted by this snapshot.

For verification, the synthesizer can fetch:
- `https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/claims.jsonl`
- `https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/2026-05-02/PCF2-SESSION-T2/claims.jsonl`
- `https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/2026-05-01/THEORY-FLEET/H4/handoff.md`

---

## 10. Footer — DOI / Hash Quick Reference

```
T2B v3.0           : 10.5281/zenodo.19915689   (concept 19783312)
PCF-1 v1.3         : 10.5281/zenodo.19937196   (concept 19931635)
PCF-2 v1.3         : 10.5281/zenodo.19963298   (concept 19936297)
SIARC umbrella v2.0: 10.5281/zenodo.19965041   (concept 19885549)
Channel Theory v1.3: 10.5281/zenodo.19972394   (concept 19941678)
                     PDF sha256 df3b90e8…
                     PDF md5    e58951de…
```

Bridge head at v1.4 snapshot time: post-005 PASS;
002 still locally HALTED (no push). Recent commit timeline:
```
[v1.4 picture]  STRATEGIC-PICTURE-REVISED v1.4 (this push)
[005 PASS]      CC-MEDIAN-RESURGENCE-EXECUTE (Prompt 005)  [108-digit agreement; β=0; G15 surfaced]
18c8833         STRATEGIC-PICTURE-REVISED v1.3
[002 HALT]      ARXIV-MIRROR-RUNBOOK (Prompt 002) — STAGED LOCAL ONLY (no push per HALT clause)
9ea4c48         STRATEGIC-PICTURE-REVISED v1.2
5d9f8d0         STRATEGIC-PICTURE-REVISED v1.1
663e95c         T3-CONTE-MUSETTE-PAINLEVE-TEST (Prompt 007) [60/60 LABELED; H3 negatively closed]
9accc6e         D2-NOTE-DRAFT (Prompt 004)
e96641c         T1-BIRKHOFF-TRJITZINSKY-LITREVIEW (003)     [verdict GAPTYPE_C]
3294387         SUBMISSION-LOG-PATCH-ITEM19 (001)           [Item 19 spliced]
e33db9e         STRATEGIC-PICTURE-REVISED (this doc, v1.0)
8be2f17         CHANNEL-THEORY-V13-RELEASE (post-publish edits)
```

---

## 19. Amendment Log (v1.8 → v1.9)

This amendment absorbs **Prompt 014 (T25D-RETRY-13PARAM) PASS** —
verdict `PASS_A_EQ_6_ONLY`, $|\delta_\text{lin}| = 3.09 \times 10^{-23}$,
no $\Gamma(1/3)$ closure in H6 B19+, G5+G16 closed in soft branch,
M7 achieved. The 014 verdict landed at bridge commit `e857172`
(operator-side push at 20:01 JST) — *between* the v1.7 push (`d2431d9`)
and my v1.8 push (`969cf54`). The v1.8 amendment was prepared
before bridge HEAD reflected `e857172`; this v1.9 amendment closes
the gap.

### v1.8 → v1.9 AEAL findings (014 PASSED)

| AEAL claim (per `T25D-RETRY-13PARAM/claims.jsonl`) | Value | Script | Reproducibility |
|---------------|-------|--------|-----------------|
| max $|\delta_\text{lin}|$ across 4 j=0 cubic families | $3.08904186542 \times 10^{-23}$ | `t25d_retry_runner.py` | dps_fit=4000, $K_\text{FIT}=7$ (11 params), square-exact `mp.lu_solve` |
| Per-family $\delta_\text{lin}$ (Q_30) | $-3.27 \times 10^{-24}$ | `t25d_retry_runner.py` | $\log_{10}\|\delta\| = -23.49$ |
| Per-family $\delta_\text{lin}$ (Q_31) | $-3.16 \times 10^{-24}$ | `t25d_retry_runner.py` | $\log_{10}\|\delta\| = -23.50$ |
| Per-family $\delta_\text{lin}$ (Q_32) | $-1.19 \times 10^{-23}$ | `t25d_retry_runner.py` | $\log_{10}\|\delta\| = -22.92$ |
| Per-family $\delta_\text{lin}$ (Q_33) | $-3.09 \times 10^{-23}$ | `t25d_retry_runner.py` | $\log_{10}\|\delta\| = -22.51$ |
| PSLQ Phase D verdict on 17-member dedup B19+ | `n_pslq_no_relation=4` | `t25d_retry_runner.py` | DPS_PSLQ=200, DPS_VERIFY=400, maxcoeff=$10^{50}$, tol=$10^{-40}$ |
| Tail-window cross-check (11p vs 7p, $N \ge 600$) | $|\Delta A| \approx 4$–$8 \times 10^{-14}$ | `t25d_retry_runner.py` | Phase C |
| Tail-window cross-check (11p vs 5p, $N \ge 800$) | $|\Delta A| \approx 1$–$3 \times 10^{-8}$ | `t25d_retry_runner.py` | Phase C; consistent with 006's 5-param floor |
| K_FIT judgment-call discrepancy | $K_\text{FIT}=7$ (not 9) | `discrepancy_log.json` | y(N_ref) undefined; truncation $\sim 1200^{-8} \sim 2.3 \times 10^{-25}$ < $10^{-15}$ target |
| PSLQ trivial-relation flag (literal 18-basis) | `1·sqrt(3) - 3·CS_sqrt3 = 0` (target=0) | `unexpected_finds.json` | $\Gamma(1/3)\Gamma(2/3) = 2\pi/\sqrt{3}$ reflection identity |
| Phase E spec impedance | input float64 ⇒ Richardson floor $\sim 10^{-5}$ | `discrepancy_log.json` | Phase E reported MET-IN-DIRECTION |

12 AEAL claims total; halt log contains verdict + summary
(verdict-bearing data, *not* a halt clause); discrepancy log
records K_FIT judgment + Phase E impedance; unexpected_finds
records PSLQ trivial-relation. **All 12 claims pass `grep` for
"shows"/"confirms"/"proves"/"demonstrates" — none used in
prediction-or-conjecture context.**

### v1.8 → v1.9 file changes

| File | Change |
|------|--------|
| `tex/submitted/control center/picture_revised_20260502.md` | v1.9 amendment (this section). Header revision/timestamp updated. New top callout block. §2.3 / §2.4 / §3 (P-PET row) / §4 (M7 milestone) / §5 (G5/G16 rows) / §6 (014 row + firing layout) / §8 (Q22 + Q23) updated. |
| `siarc-relay-bridge/sessions/2026-05-02/STRATEGIC-PICTURE-REVISED/picture.md` | Mirror of v1.9 (push pending). |
| `tex/submitted/control center/prompt/_INDEX.txt` | (next turn) bump to "post-014 PASS"; mark 014 ✅ DONE; update GAP CLOSURE MAP for G5+G16; update FIRING ORDER; surface Q22+Q23. |

### v1.8 → v1.9 SQL state

**Pre-v1.9:** 25 done / 27 pending / 3 blocked = 55 todos.

Changes:
- `prompt-014-fire`: pending → ✅ done.
- `q22-014-stretch-goal-arbitrate`: NEW pending todo (Claude
  arbitration on closure-threshold acceptance for PCF-2 v1.4
  deposit; soft branch path-(a) deposit-now vs hard branch
  path-(b) fire-014b for stretch goal).
- `q23-pslq-basis-hygiene-claude-arbitrate`: NEW pending todo
  (Claude codifies op-design hygiene rule for PSLQ basis
  pre-screening of $\mathbb{Q}$-linear dependencies).
- `pcf2-v1-4-deposit-decision-q22-gated`: NEW blocked todo
  (PCF-2 v1.4 Zenodo deposit, blocked on Q22 path-(a) acceptance).

**Post-v1.9:** 26 done / 26 pending / 3 blocked = **55 todos**
(net: −1 pending +1 done +2 pending +1 blocked −1 retired).
Note: the apparent net "no change in total" reflects a separate
consolidation of an earlier todo `prompt-014-pcf2-v1-4-deposit-
decision-q22` (drafted but not committed) being subsumed into
`pcf2-v1-4-deposit-decision-q22-gated`.

### v1.8 → v1.9 bridge commit trail

```
[v1.9 picture]  STRATEGIC-PICTURE-REVISED v1.9 (this push, pending)
969cf54         STRATEGIC-PICTURE-REVISED v1.8 — absorb 010+012+013
e857172         T25D-RETRY-13PARAM (Prompt 014 PASS)               [absorbed by v1.9]
726b53e         CC-FORMAL-BOREL-CLOSE (Prompt 013 HALT)            [absorbed by v1.8]
e93458f         XI0-D3-DIRECT (Prompt 012 PASS)                    [absorbed by v1.8]
d2431d9         STRATEGIC-PICTURE-REVISED v1.7 — absorb 009 PARTIAL
fa2516e         T35-STOKES-MULTIPLIER-DISCRIMINATION (Prompt 010 PARTIAL)
32fef0a         STRATEGIC-PICTURE-REVISED v1.6
```

### v1.8 → v1.9 cycle status

**Cycle accounting (post-014 PASS):** 12 prompts fired total this
cycle: **7 ✅ DONE** (001, 003, 004, 005, 007, 012, 014); **3 🛑
HALTED** (002 G12 source-drift; 006 j=0 5-param precision floor
— *now superseded in soft branch by 014's PASS*; 013 G15 gate —
as designed); **2 🟡 PARTIAL** (009 G15; 010 G6b). G2 + G5 + G16
are now *closed*. M1, M3, M5, M6, M7, M8 are **done or in soft
closure**; M4 (B-T applied / B4 at $d \ge 3$) blocked on G3b +
H1 arbitration; M9 (SIARC-MASTER-V0) downstream.

### v1.8 → v1.9 published-artefact tension audit

**No tension.** 014's verdict `PASS_A_EQ_6_ONLY` does not
contradict any published claim:
- **PCF-2 v1.3 §6** says `AMBIGUOUS-AT-FINITE-N` — 014's result is
  *strictly stronger* than the published wording (14 orders more
  precision; basis exhausted). The `pcf2_v1.4_amendment.md` Phase F
  draft *replaces* §6's ambiguous statement with a precise
  closure-direction statement; depositing it to Zenodo creates a
  v1.4 record (concept DOI unchanged).
- **CT v1.3 §3.5** is unaffected (j=0 endpoint discussion is in
  PCF-2, not CT).
- **Umbrella v2.0 §4.4** (invariant-triple framing) is unaffected.
- **D2-NOTE v1.0 (drafted)** is unaffected (Newton-polygon $\xi_0$
  result, separate from j=0 amplitude). NB: D2-NOTE Conj 3.3.A* is
  separately upgrade-candidate for Q20 (012's Newton-polygon
  argument).

The 014 → PCF-2 v1.4 path is a clean hardening of the published
narrative, not a contradiction of it.

### v1.8 → v1.9 next-cycle priorities (re-affirmed)

1. **Slot 1 (compute):** Prompt 016 (T36-S2-EXTRACTION; refit-only
   on cached CSVs; ~30 min agent; tests S_2 alien-amplitude
   discrimination across the PCF-1 §3 dichotomy; G6b full closure
   if positive, S_3 escalation if negative).
2. **Slot 2 (operator-side, parallel):** G3b literature acquisition
   (Okamoto 1987 §§2–3 + Conte-Musette 2008 ch. 7 §§7.3–7.4) to
   unblock Prompt 015 and the path-(a) refire of Prompt 013.
3. **Slot 3 (operator-side, parallel):** PCF-2 v1.4 deposit
   decision (Q22 path-(a) deposit-now-at-$|\delta| \sim 10^{-23}$
   vs path-(b) fire-014b-for-stretch-goal). Claude territory:
   does the operator's "AMBIGUOUS-AT-FINITE-N" → "A=6 to
   PSLQ-detection precision; no Chowla–Selberg correction"
   transition warrant a v1.4 deposit at the soft-branch precision?
4. **Synthesizer territory** (now **6 questions** for Claude):
   Q11 (H1 arbitration), Q18 (sign-of-C basis-independence),
   Q19 (β_R=0 structural at d=2), Q20 (Conj 3.3.A* proof-upgrade
   candidate at all $d \ge 2$), Q21 (013 refire path-(a)/(b)),
   **Q22 (014 closure-threshold acceptance)**, plus G17
   (layer-separation framing) and **Q23 (PSLQ basis hygiene rule)**
   — 6 active questions + 2 framing items.

---

## 18. Amendment Log (v1.7 → v1.8)

This amendment absorbs **three relay-agent verdicts** that landed
in the post-v1.7 compute window (operator-side runs):

1. **Prompt 010 — `G6B_PARTIAL_HIGHER_ORDER_NEEDED`**
   (T35-STOKES-MULTIPLIER-DISCRIMINATION; ~2 hr agent; pushed at
   bridge commit `fa2516e`).
2. **Prompt 012 — `G2_CLOSED_AT_D3`** ✅ (XI0-D3-DIRECT;
   ~25 min agent; pushed at bridge commit `e93458f`).
3. **Prompt 013 — `CC_BOREL_009_NOT_AVAILABLE`** 🛑 (CC-FORMAL-
   BOREL-CLOSE; ~10 min agent; pushed at bridge commit
   `726b53e`; *gate fired correctly — discipline working as
   designed, not a result failure*).

It also adds the new side-finding G19, the new follow-up Prompt
016, and the four new open questions Q18 (sign-of-$C$
basis-independence), Q19 ($\beta_R = 0$ structural consequence),
**Q20 (Conj 3.3.A* proof-upgrade candidate)**, **Q21 (013 refire
path — full G15 via 015 vs symbolic-only PARTIAL)**.

**Status changes:**
- `G2` (gap): Future prompt → ✅ **CLOSED at $d=3$ across 3 Galois
  bins at 80 algebraic digits** (Prompt 012). With Q20 arbitration,
  potential PROVEN upgrade for *all* $d \ge 2$ via Newton-polygon
  theorem.
- `G6b` (gap): `Prompt 010 ✅ DRAFTED` → 🟡 **PARTIAL** (Prompt 010
  landed; closure path through Prompt 016).
- `prompt-010-fire` (SQL todo): pending → **done**.
- `prompt-012-fire` (SQL todo): pending → **done**.
- `op-xi0-d3-direct` (SQL todo): pending → **done** (graduated via 012).
- `prompt-013-fire` (SQL todo): pending → **done** (HALTED;
  refire pending Q21 decision).
- **NEW gap G19**: $\beta_R = 0$ universal across the $d=2$ PCF
  Birkhoff resurgent ansatz. MED severity (epistemic / structural).
- **NEW Prompt 016 (T36-S2-EXTRACTION)**: ~30 min refit-only
  agent on cached `borel_*_dps250_N2000.csv` series; extracts $S_2$
  alien amplitude at $2\zeta_*$ via residual Richardson; tests
  $|S_2|$, $\arg(S_2)$, and the canonical-resurgence ratio
  $S_2 / S_1^2$ as discriminators of the $\Delta_b$ dichotomy.
- **NEW open questions Q18–Q21** in § 8 (sign$(C)$
  basis-independence; $\beta_R = 0$ structural consequence; Conj
  3.3.A* proof-upgrade candidate; 013 refire path arbitration —
  all Claude / operator territory).

**AEAL findings (Prompt 010, 8 entries in `claims.jsonl`):**

| Quantity | Value | Method |
|----------|-------|--------|
| V_quad $C$ | $+8.12733679549507236711257873202358318226454272234\ldots$ | Richardson tail, dps=250, N=2000 |
| QL15 $C$ ($\Delta_b=-20$) | $+21.38412649463506525828438453625561662911360599660\ldots$ | Richardson tail, dps=250, N=2000 |
| QL05 $C$ ($\Delta_b=8$) | $+1.40328080725296497994724250152093112017966978359\ldots$ | Richardson tail, dps=250, N=2000 |
| QL09 $C$ ($\Delta_b=1$) | $-6.07472006379093506128527538224945464230395636102\ldots$ | Richardson tail, dps=250, N=2000 |
| Cross-method digit agreement | 67–77 digits at dps=250 | Richardson vs LSQ-in-$1/n$ |
| V_quad cross-validation | exact agreement on all 49 displayed digits | new $d=2$ generalised recurrence vs CC-MEDIAN cached series |
| $\beta_R$ across all 4 reps | $\le 10^{-85}$ | LSQ-in-$1/n$ residual |

**AEAL findings (Prompt 012, 5 entries in `claims.jsonl` — 3 per-bin
verifications + 1 D2-NOTE consistency summary + 1 Galois-bin
coverage certificate):**

| Bin | Family | $(a_3, a_2, a_1, a_0)$ | Alg agreement digits | Num digits @ N=1500 | Verdict |
|-----|--------|------------------------|----------------------|---------------------|---------|
| `+_C3_real` | 19 | $(1, -3, 0, 1)$ | 80.0 | 3.18 | **AGREES** |
| `+_S3_real` | 14 | $(1, -3, -1, 1)$ | 80.0 | 3.18 | **AGREES** |
| `-_S3_CM`   | 50 | $(1, -2, 0, -1)$ | 80.0 | 3.35 | **AGREES** |

Aggregate **`G2_CLOSED_AT_D3`** (3/3 AGREE). All representatives
have $\alpha_3 = 1$ in the smallest-coefficient selection rule, so
$\xi_{0,\text{conj}} = 3$ across all 3 bins (a coincidence of the
representative-selection rule; the test verdict is invariant
under this choice since the characteristic root depends only on
$\alpha_3$).

**AEAL findings (Prompt 013, 1 entry in `claims.jsonl` — halt
record only):**

| Quantity | Value | Method |
|----------|-------|--------|
| Halt clause triggered | `CC_BOREL_009_NOT_AVAILABLE` | Upstream verdict inspection (009 = `G15_PARTIAL`, not `G15_CLOSED`) |
| Upstream 005 input hash | `C_native = 8.127336795495072367\ldots` (108 digits) | (referenced; not recomputed) |
| Upstream 009 input | $S_{\zeta_*}^{\text{can}}$ symbolic-only as $J_\text{resc} \cdot J_\text{symp} \cdot S_{\zeta_*}^{\text{native}}$ with $J_\text{resc} = (1/3)^{\sigma_0 + 11/12}$ (R2-conditional), $J_\text{symp}$ undetermined (R5: Okamoto 1987 Lax pair missing) | (referenced; not recomputed) |
| Borel sum produced? | **No** (halted before any phase ran) | — |
| CT v1.3 §3.5 status flipped? | **No** (flip requires PASS or PARTIAL, not HALT) | — |

**5 anomalies / open questions surfaced (Prompt 010 handoff §
"Anomalies"):**
- A1: sign$(C)$ varies *within* the $\Delta>0$ side (QL05 $+$,
  QL09 $-$). Promoted to Q18 (basis-independence of sign$(C)$).
- A2: $\beta_R = 0$ across all 4 reps to $\ge 85$ digits.
  Promoted to G19 + Q19.
- A3: PASS-criterion strictness — $|S_1|$ differs across the
  dichotomy at $O(1)$ scale, but the prompt's PASS clause
  requires a *structural* pattern; verdict is therefore PARTIAL,
  not PASS. Pre-registered behaviour, no change to op definition.
- A4: Within-side spread $\sim 3\times$ larger than cross-side
  spread on $|C|$. Consistent with "Stokes data fingerprints the
  family, not the side". The informative content of the partial
  result.
- A5: No HARD HALT triggered. `G6B_STOKES_INVARIANT` halt clause
  required cross-side agreement of $|C|$ to $\ge 30$ digits;
  observed agreement is $\le 0.03$ digits (sides genuinely differ).
  Stokes data is correctly NOT sign-invariant.

**Prompt 012 anomaly (W1): structural-triviality / proof-upgrade
candidate.** The algebraic Newton-polygon test depends only on
$\alpha_3$; the 80-digit per-bin agreement is *uniformity*
evidence, not bin-specific verification. The relay agent
surfaced this in `XI0-D3-DIRECT/handoff.md` and noted that the
operator-level argument *may* already constitute a proof modulo
standard Newton-polygon / irregular-singular-point theorems — in
which case Conj 3.3.A* could be upgraded DEFERRED → PROVEN at
$d=3$ (and EMPIRICAL → PROVEN at $d=4$) by the same uniform
argument. Promoted to Q20 (§ 8); Claude arbitration territory;
no D2-NOTE modification performed in 012's session per the
DO-NOT clause.

**Prompt 013 synthesizer-intent ambiguity surfaced.** The agent
surfaced in `CC-FORMAL-BOREL-CLOSE/handoff.md` that the gating
language ("MUST NOT be fired until 009's verdict is `G15_CLOSED`"
and "if 009 returns `G15_PARTIAL` ... this prompt is reformulated
by the synthesizer before firing") suggests the synthesizer may
have expected to gate 013 out at *planning* time, not to
*fire-and-halt*. Either way, the named halt clause
`CC_BOREL_009_NOT_AVAILABLE` is the AEAL-honest behaviour. The
two refire paths (Q21) are: **(a)** wait for 015 to close G15,
refire unchanged; **(b)** reformulate 013 to accept `G15_PARTIAL`
with symbolic-only Borel sum and no numerical gate (verdict
`CC_FORMAL_BOREL_SYMBOLIC_PARTIAL`).

**Reusable infrastructure delivered (010, in
`sessions/2026-05-02/T35-STOKES-MULTIPLIER-DISCRIMINATION/`):**
- `derive_recurrence.py` — symbolic derivation of the general
  $d=2$ Birkhoff recurrence in $(\alpha, \beta, \gamma, \delta,
  \epsilon)$. Specialises to V_quad's existing recurrence;
  reusable for any $d=2$ PCF Stokes-data extraction.
- `t35_runner.py` — numerical extractor with t2c precision-ladder
  discipline, Richardson + LSQ cross-method, structural-pattern
  analysis. Reusable for future $d=2$ extractions including the
  Prompt 016 $S_2$ refit (with the leading-term subtraction
  appended).
- 8 cached `borel_<rep>_dps<dps>_N<N>.csv` series files with $a_n$
  to dps=250, $N=2000$. **Direct input to Prompt 016** — no new
  mpmath series needed for $S_2$ extraction.

**Reusable infrastructure delivered (012, in
`sessions/2026-05-02/XI0-D3-DIRECT/`):**
- `xi0_d3_runner.py` — per-Galois-bin Newton-polygon
  characteristic-root test; reusable for $d \ge 4$ extension if
  D2-NOTE proof-upgrade (Q20) is rejected.
- `bin_representatives.json` — 3 cubic Galois-bin representatives
  in PCF2-SESSION-A-compatible format.
- 3 per-bin CSVs (`xi0_d3_+_C3_real.csv`, `xi0_d3_+_S3_real.csv`,
  `xi0_d3_-_S3_CM.csv`) with the $Q_n$ recurrence at
  $N \in \{500, 1000, 1500\}$, dps=80.
- `newton_d3_results.json` (algebraic test summary) +
  `borel_d3_results.json` (numerical test summary).
- `d2note_consistency.md` — documents the D2-NOTE Conj 3.3.A*
  consistency check at $d=3$.

**File changes in this amendment:**
- header `Revision:` v1.7 → v1.8.
- header `Updated:` 2026-05-02 19:30 JST → 20:30 JST (post-010 +
  012 + 013 absorption).
- new top callout block "🆕 Updates since v1.7" (extended for all
  three verdicts plus the Q20 + Q21 follow-ups).
- §2.3 in-flight: 7 fired → 9 fired (012 + 013 added); 2 PARTIAL
  unchanged; 2 HALTED → 3 HALTED (013 added); drafted-ready math
  closure 2 → 1 (012 graduated, 013 HALTED but counted under
  HALTED); SQL pending 28 → 26; SQL done 22 → 24.
- §2.4 recently closed: appended 010 PARTIAL, 012 PASS, 013 HALT
  entries.
- §3 P-NP row: revised to ✅ EMPIRICAL at $d=3$ via Prompt 012,
  with Q20 footnote re proof-upgrade candidate.
- §3 P-CC row: revised to note 013 HALT on gate (correct
  behaviour) + Q21 refire path arbitration.
- §3 P-PIII row: revised to 010 🟡 PARTIAL → 016 (drafted)
  follow-on; β_R=0 universal note added (no change in this
  edit batch — already done).
- §5 G2 row: future prompt → ✅ CLOSED via Prompt 012 with Q20
  proof-upgrade footnote.
- §5 G6b row: drafted-ready → PARTIAL via 010; full closure
  via 016 (no change in this edit batch — already done).
- §5 G15 row: residuals R1–R5 documented; R5 chokepoint
  emphasised by 013 halt (no separate edit; G15 row already
  correct from v1.7).
- §5 NEW G19 row: $\beta_R=0$ universal at $d=2$ side-finding
  (no change — already done in v1.7→v1.8 first pass).
- §6 prompts table: 010 row revised to PARTIAL with details;
  012 row revised to ✅ DONE; 013 row revised to 🛑 HALTED with
  refire-path note; NEW row 016.
- §6 firing layout: rewritten for v1.8 (010 + 012 + 013 done;
  016 added to parallel-with-014 slot 2; subsequent slots
  renumbered; 013 refire path (a)/(b) Q21 split surfaced).
- §6 NEW v1.8 note on 016 cascade-to-S_3 + Q18 escalation path
  (no change — already done in v1.7→v1.8 first pass).
- §8 NEW Q18 (sign$(C)$ basis-independence — Claude territory),
  Q19 ($\beta_R = 0$ structural consequence — Claude territory),
  **Q20 (Conj 3.3.A* proof-upgrade candidate — Claude territory)**,
  **Q21 (013 refire path arbitration — operator + Claude
  territory)**.
- this NEW §18 amendment log replaces the original 010-only
  draft to absorb all three verdicts.
- closing marker bumped to v1.8 (no change — already done).

**SQL state (post-010 + 012 + 013 absorption):**
- 25 done (was 22 at v1.8 first pass; +3 = `prompt-012-fire`,
  `prompt-013-fire`, `op-xi0-d3-direct` — the latter graduated
  via 012's execution).
- 27 pending (was 28; −3 graduated, +2 new follow-ups
  `q20-conj33a-proof-upgrade-claude-arbitrate` and
  `q21-013-refire-path-arbitrate`).
- 3 blocked (unchanged).
- Total: 55 todos.

**Bridge-side commit trail (post-v1.7 push):**
```
[v1.8 push]   STRATEGIC-PICTURE-REVISED v1.8 (this push)
726b53e       CC-FORMAL-BOREL-CLOSE (Prompt 013) — HALT on G15 gate
e93458f       XI0-D3-DIRECT (Prompt 012) — G2_CLOSED_AT_D3
d2431d9       STRATEGIC-PICTURE-REVISED v1.7 (prior push)
fa2516e       T35-STOKES-MULTIPLIER-DISCRIMINATION (Prompt 010) — G6B_PARTIAL_HIGHER_ORDER_NEEDED
32fef0a       STRATEGIC-PICTURE-REVISED v1.6
6f3e91a       VQUAD-PIII-NORMALIZATION-MAP (Prompt 009) — G15_PARTIAL
```

**No published-artefact tension.** Prompts 010, 012, 013 each
make no claim that contradicts any line of CT v1.3, PCF-1 v1.3,
PCF-2 v1.3, or umbrella v2.0. PCF-1 v1.3 §3 dichotomy is
*measured*, not *explained*, by 010 at the leading scale. D2-NOTE
v1.0 (drafted, awaiting Zenodo) is *strengthened* but not
modified by 012's $d=3$ closure. CT v1.3 §3.5 is *not* flipped by
013 (correct behaviour for HALT).

**No HALTs of concern.** Prompt 010's `G6B_*` halt clauses are
explicitly NOT triggered (halt log `{}`). Prompt 012's halt log
is `{}` (no halt). Prompt 013's halt log carries
`CC_BOREL_009_NOT_AVAILABLE` — this is the *intended* halt
clause, fired by design as the gate, *not* a result failure.

---

## 17. Amendment Log (v1.6 → v1.7)

**Updated:** 2026-05-02 19:30 JST
**Trigger:** completion of Prompt 009 (VQUAD-PIII-NORMALIZATION-MAP)
with verdict `G15_PARTIAL` (Φ_resc + Φ_shift pinned; Φ_symp
residual on Okamoto 1987 §§2–3 Lax pair).

**Substantive changes:**

| Section | v1.6 → v1.7 |
|---------|-------------|
| Header  | Revision bumped v1.6 → v1.7. New v1.6 → v1.7 callout block prepended above v1.5 → v1.6 block. Earlier callouts retained for the synthesizer's full audit trail. |
| § 2.3 (in-flight) | "12 prompts" → "13 prompts" (added 015). New "1 fired and PARTIAL" line for Prompt 009. "4 drafted-ready math-closure prompts" → "3 drafted-ready" (009 moved to PARTIAL). New entry for Prompt 015 (drafted but operator-gated on R5). Prompt 014 entry retained unchanged. |
| § 2.4 (recently closed) | Added Prompt 009 PARTIAL line with the headline structural finding (V_quad scalar ODE re-derived; Φ_resc/shift pinned; Φ_symp residual on Okamoto Lax pair; layer-separation insight; no fabricated $C_\text{can}$). |
| § 3 P-CC row | Inserted Prompt 009 PARTIAL into the closure path: `005 ✅ → 009 🟡 → 015 R5-gated → op:cc-formal-borel`. Status text revised to spell out "Φ_resc + Φ_shift pinned, Φ_symp residual on R5". |
| § 4 M6 caveat | Updated: canonical-form completion is now PARTIAL (009); full closure via Prompt 015 once operator acquires Okamoto 1987 + Conte-Musette ch. 7 via G3b workflow. |
| § 5 G15 row | Status revised: "✅ DRAFTED" → "🟡 PARTIAL (Prompt 009): Φ_resc + Φ_shift pinned; Φ_symp residual on R5; full closure via Prompt 015". |
| § 5 NEW row G17 | **Layer separation** between V_quad scalar OGF ODE (linear; L-equation) and canonical $P_{III}(D_6)$ Hamiltonian (nonlinear; isomonodromic deformation thereof). Φ acts on Lax-pair monodromy data, not on $(f, f', z)$. CT v1.4 amendment candidate. |
| § 5 NEW row G18 | **Okamoto-constraint mismatch** on (1/6, 0, 0, -1/2) parameter point (sums to -1/3, not 0). Convention question; informational, not halt-class. |
| § 6 prompts table | 009 row marked PARTIAL with verdict + structural-finding callout. New row 015 (T25E-VQUAD-PIII-NORM-MAP-CLOSE; drafted; gated on R5). 14 → 15 rows. |
| § 6 firing layout | Rewritten: 013's hard-gate clarified (now requires *full* G15 closure via 015, not just the 009 PARTIAL). NEW Slot 4 (operator-side G3b literature acquisition), NEW Slot 5 (Prompt 015 once R5 acquired), Slot 6 = 013. 014 + 012 + 010 remain in parallel slots 1–3. |
| § 8 open questions | Added Q16 (layer separation; CT v1.4 amendment candidate) and Q17 (parameter-convention pinning; R1 from Okamoto §2). |
| § 17 (this section) | NEW. |

**Unchanged:**

§ 1 (mission statement), § 7 (decision tree), § 9 (AEAL hygiene),
the publication ladder table (§ 2.1), the empirically verified
list (§ 2.2), and the publication-ladder/concurrency-map
infrastructure of § 6 are intact. The 7×7 concurrency map (§ 6)
is retained unchanged (Prompt 015 documented as gated on operator
literature acquisition; the matrix cell-pattern between
001–007 is unaffected). Prompts 001/003/004/005/006/007 status
descriptions in § 2.4 / § 4 / § 6 are carried forward verbatim.
Prompt 014 status text is unchanged.

**Headline AEAL findings recorded (V_quad scalar ODE side):**

- $3 z^3 f''(z) + 10 z^2 f'(z) + (5z + z^2 - 1) f(z) = 0$ —
  exact rational coefficients, sympy-verified from the
  $b_n = 3n^2 + n + 1$ recurrence (`verify_vquad_ode.py` /
  log sha256 `9c6c7865…e451213`).
- Newton polygon at $z=0$: single edge of slope $1/2$
  (rank-$1/2$ irregular singularity); exact.
- Characteristic exponent: $c = \pm 2/\sqrt{3}$; exact algebraic.
- Borel-plane singular distance: $\zeta_* = 4/\sqrt{3}$; exact
  algebraic (matches Prompt 005 measurement to 250 digits).
- Secondary Birkhoff exponent: $\rho = -11/6$; exact rational.
- $\Phi_\text{resc}$ parameter $\lambda = c_0^2 / 4 = 1/3$
  (exact, R3-conditional on Stokes-sign convention).
- $\Phi_\text{shift}$ Jacobian on Stokes data: $1$ (exact;
  affine-shift triviality).
- $\Phi_\text{symp}$ Jacobian: NOT computed (residual R5).
- $C_\text{can}$, $S_{\zeta_*}^\text{can}$: NOT numerically
  computed in Prompt 009 (no fabrication; deferred to
  Prompt 015 once R5 acquired).

**Residuals on G15 (5 documented in `phi_change_of_variables.tex`):**

- **R1**: convention pinning of $(\alpha_\infty, \alpha_0,
  \beta_\infty, \beta_0) = (1/6, 0, 0, -1/2)$ from CT v1.3 vs
  Okamoto vs Sakai — needs Okamoto 1987 §2.
- **R2**: trans-series leading prefactor of $P_{III}(D_6)$ at
  $t=0$ — needs Okamoto 1987 §3 eq. (3.7).
- **R3**: Stokes-multiplier sign and phase convention — needs
  Lisovyy-Roussillon 2017 §4.
- **R4**: cross-check on R1, R2 — Conte-Musette 2008 ch. 7
  §§7.3-7.4.
- **R5** (PRIMARY BLOCKER): explicit `2×2` Lax pair for
  $P_{III}(D_6)$ — Okamoto 1987 §§2-3 (preferred) or
  Jimbo-Miwa 1981 §3 (alternate route).

All five have known-citable references in standard ILL/AMS-
accessible journals; the operator's existing G3b workflow
handles this.

---

## 16. Amendment Log (v1.5 → v1.6)

**Updated:** 2026-05-02 19:25 JST
**Trigger:** completion of Prompt 006 (T2.5D-J0-CHOWLA-SELBERG-CLOSURE)
with verdict `AMBIGUOUS_AT_DPS8000` (formal halt; H6 still OPEN).

**Substantive changes:**

| Section | v1.5 → v1.6 |
|---------|-------------|
| Header  | Added v1.5 → v1.6 callout block. Earlier callouts retained for the synthesizer's full audit trail. |
| § 2.3 (in-flight) | "5 fired/done" → "6 fired/done"; "1 in flight" → "0 in flight"; "1 HALT" → "2 HALT" (added 006). New entry for Prompt 014 (T2.5d-RETRY-13PARAM, drafted-ready). Counts updated (24 pending / 19 done / 1 blocked of 44). |
| § 2.4 (recently closed) | Added Prompt 006 HALT line with the headline empirical signal (A=6 ± 2e-7, monotone-converging) + spec-vs-precision-floor caveat. |
| § 3 P-PET row | Status updated: "PASSED; j=0 AMBIGUOUS-AT-FINITE-N" → "PASSED; j=0 AMBIGUOUS-AT-FINITE-N (5-param ansatz; A=6 ± 2e-7 supported empirically); 30-digit closure pending Prompt 014". |
| § 4 M7 block | Marked PARTIAL with the empirical-signal headline + spec-vs-precision-floor caveat + closure path via Prompt 014. |
| § 5 G5 row | Status revised: "Prompt 006 (ready to fire)" → "Prompt 006 HALTED; A=6 supported empirically with monotone N-convergence; formal closure pending Prompt 014". |
| § 5 NEW row G16 | Spec-vs-precision-floor mismatch: 5-param 1/n ansatz at N=1200 caps A-fit precision at ~7 digits (model truncation O(1/N^2)); generalises to any deep-WKB closure operator. |
| § 6 prompts table | 006 row marked HALTED with verdict label + headline numbers. New row 014 (T2.5d-RETRY-13PARAM, drafted-ready, ~5–20 min refit). Counts: 13 → 14 rows. |
| § 6 firing layout | Rewritten: 014 promoted to Slot 1 (highest leverage; tiny compute; immediate Phase D PSLQ unlock); 009/012 parallel; 010 next; 013 hard-gated on 009. |
| § 8 open questions | Added Q14 (empirical-vs-formal gap on j=0; how to phrase pre-014 status) and Q15 (spec-design lesson; should future deep-WKB ops pre-compute dps floor + parameter-count floor?). |
| § 16 (this section) | NEW. |

**Unchanged:**

§ 1 (mission statement), § 7 (decision tree), § 9 (AEAL hygiene),
the publication ladder table (§ 2.1), and the six-program
decomposition (§ 3 — only the P-PET row's status text changed)
are intact. The 7×7 concurrency map (§ 6) is retained
unchanged — Prompt 014 is documented as INDEPENDENT in the
prompts table; the matrix cell-pattern is unaffected.

**Headline empirical results recorded (V_quad cubics, j=0 axis):**

| family | $A_\text{lin}$ (5-param fit, $N_\max=1200$) | $\delta_\text{lin}$ |
|---|---|---|
| 30 | 6.00000009866458799… | $+9.87 \times 10^{-8}$ |
| 31 | 5.99999990131228818… | $-9.87 \times 10^{-8}$ |
| 32 | 5.99999985197425230… | $-1.48 \times 10^{-7}$ |
| 33 | 5.99999980263623205… | $-1.97 \times 10^{-7}$ |

$N$-scaling of $|\delta_\text{lin}|$ (LIN, tail-window fit):
monotone-decreasing across all four families from $N_\max=1000$
through $N_\max=1100$ to $N_\max=1200$, with ratio
$\delta(1000)/\delta(1200) \sim 1.7$ — consistent with a
$c_2/N^2$ truncation leak (universal across families,
$c \sim 0.04$, same sign). This is structural support for
$A_\text{true}=6$ exactly, modulo a 7-digit model-truncation
floor that **only** a higher-order ansatz (Prompt 014) can
break through.

**No new published-artefact tension:**

PCF-2 v1.3 §6 already labels the j=0 endpoint as
"AMBIGUOUS-AT-FINITE-N", so no Zenodo or arXiv record needs to
be amended in light of v1.6. The AEAL discipline holds: the
formal halt is honored in the verdict label
(`AMBIGUOUS_AT_DPS8000`) and the empirical $A=6$ signal is
recorded as "supported, monotone-converging, formal closure
pending 13-param refit" rather than "established" or "proved".

**Why a 14th prompt rather than retrying 006 with the same
spec at higher dps:**

The 006 verdict is *not* a failure of the j=0 measurement; it
is a failure of the 5-param ansatz to deliver 30 digits at
$N=1200$. The cf_value computation already ran to 22150-digit
resolution at $N=1200$; the bottleneck is purely in the
post-processing fit. Prompt 014 reuses the saved
`Qn_j0_dps25000_N1200_fam{30..33}.csv` files (137 KB each;
SHA-256 hashes already AEAL-logged) and runs only the refit +
PSLQ. The expected agent compute is $\sim 5$–$20$ min — a
two-orders-of-magnitude reduction from 006's already-fast
35 s, since no `cf_value` calls are made.

**Epistemic posture observation:**

Prompt 006's relay agent demonstrated three healthy
behaviours: (i) honest documentation of the spec-vs-reality
incompatibility (literal `dps=8000` infeasible for A=6
at $N=1200$; agent set `dps=25000` and surfaced the
substitution in `halt_log.json`), (ii) honest non-execution of
Phase D PSLQ when the input precision was structurally
insufficient (rather than running it and reporting spurious
relations), and (iii) explicit recommendation of the next
operator step (T2.5d-RETRY-13PARAM with a concrete spec). The
verdict `AMBIGUOUS_AT_DPS8000` is *exactly* the right
epistemic register: empirical signal acknowledged, formal
threshold honored, retry path scoped. This is the AEAL
discipline working as designed.

---

## 15. Amendment Log (v1.4 → v1.5)

**Updated:** 2026-05-02 19:10 JST
**Trigger:** drafting of the math-closure prompt batch
(009 / 010 / 012 / 013) at `tex/submitted/control center/prompt/`,
addressing the residuals surfaced by the v1.2 / v1.3 / v1.4 verdicts.

**Substantive changes:**

| Section | v1.4 → v1.5 |
|---------|-------------|
| Header  | Added v1.4 → v1.5 callout. Earlier callouts retained for the synthesizer's full audit trail. |
| § 6 prompts table | Expanded from 9 to 13 rows. Added 009 (G15), 010 (G6b — was "future"), 012 (G2), 013 (P-CC formal closure, hard-gated on 009). 010 row converted from "future / not yet drafted" to "DRAFTED; ready". 011 row updated wording ("future / not yet drafted" → "future (slot reserved)"). Counted: 7 done/in-flight + 4 newly drafted-ready + 2 reserved = 13. |
| § 6 firing layout | Rewritten to reflect 5-slot post-006 sequence: 006 (in flight) → 009 → 012 → 010 (parallel) → 013 (after 009 lands). 010 demoted from "defer" to "ready". G15 line removed (now Prompt 009). |
| § 6 concurrency note | New paragraph documenting that 009/010/012 are mutually independent and parallelizable, with 013 hard-gated on 009. |
| § 15 (this section) | NEW. |

**Unchanged:**

§§ 1–5 (mission, status, programs, milestones, gaps), § 7
(decision tree), § 8 (open questions), § 9 (AEAL hygiene),
§ 10 (footer/DOIs). The 7×7 concurrency map (§ 6) is retained
unchanged — the new prompts are documented in the surrounding
prose since they neither depend on nor are dependencies for
prompts 001–007 (other than the standing hard-gate of 013 on
009, called out in § 6 inline).

**No SQL or AEAL changes:**

This revision does not produce new computational artefacts and
does not record new claims. AEAL claim count is unchanged
relative to v1.4. SQL todo additions are scaffolding entries
(prompt-fire trackers for 009 / 010 / 012 / 013) and do not
reflect new mathematical state.

**Why bump now (rather than wait for 006's verdict):**

The four drafted prompts represent the operator's queue *for
the next compute window* — synthesizer review of v1.5 can
proceed in parallel with Prompt 006's in-flight execution. The
post-006 verdict (whatever its label) will trigger v1.6 (or
later) absorption; v1.5 is the snapshot that defines what
*will be fired* once 006 lands. This is the same rhythm used
for v1.1 (queue 001/002/003 drafted before any of them fired)
and v1.4 (009/010/012/013 *rebroadcast* now that 005 + 007
have surfaced their residuals).

**Epistemic posture observation:**

The v1.4 → v1.5 transition is the first "scaffolding-only"
amendment in the picture's history. Earlier amendments
(v1.0 → v1.1 → v1.2 → v1.3 → v1.4) each absorbed a verdict
or a HALT. v1.5 records the *operator's* response — a
batch of prompts engineered to convert the residuals into
closures. This separation of "verdict-absorbing" amendments
from "queue-drafting" amendments keeps the synthesizer's
audit trail clean: v1.5 says "the queue is now fully
populated to address all v1.4 residuals", and a later v1.6
will say "the queue's first member has fired with verdict X".

---

## 14. Amendment Log (v1.3 → v1.4)

**Updated:** 2026-05-02 18:55 JST
**Trigger:** completion of Prompt 005 (CC-MEDIAN-RESURGENCE-EXECUTE)
with verdict `H4_EXECUTED_PASS_108_DIGITS`.

**Substantive changes:**

| Section | v1.3 → v1.4 |
|---------|-------------|
| Header  | Added v1.3 → v1.4 callout. Earlier callouts retained for the synthesizer's full audit trail. |
| § 2.3 (in-flight) | "5 fired/done" (was: 4); "1 ready" (was: 2). New entry for `vquad-pIII-normalization-map` (no prompt yet — small symbolic task). Counts updated (17 pending / 18 done / 1 blocked of 36). |
| § 2.4 (recently closed) | Added Prompt 005 PASS line. |
| § 3 P-CC row | Status changed from "Stokes-side PENDING" to "Stokes-side MEASURED in V_quad native normalization at 108 digits (Prompt 005); canonical-form Stokes data PENDING G15". |
| § 4 milestones | M6 marked COMPLETE with the precision-margin headline + canonical-form caveat. |
| § 5 gaps | G4 status changed from "Prompt 005 ready to fire" to "PASSED 2026-05-02; canonical-form value awaits G15". New row G15 (V_quad → P_III(D_6) normalization map for Stokes data). |
| § 6 prompts table | 005 marked DONE with verdict and parenthetical β=0 + G15 callout. Firing layout rewritten (only 006 remaining in the original queue; G15 added as a parallel symbolic task). |
| § 8 open questions | Added Q12 (β=0 logarithmic-class refinement — theoretical explanation? per-Galois-bin variation?) and Q13 (Phase D method substitution — one-off or amend canonical operator definition?). |
| § 10 footer | Bridge head bumped (005 commit added); commit timeline extended. |
| § 14 (this section) | NEW. |

**Unchanged:**

§ 1 (mission statement), § 9 (AEAL hygiene), the publication
ladder table, the six-program decomposition, and § 7 decision
tree are intact. The concurrency map (§ 6) is unchanged in
shape; the *content* of the firing layout has shifted (only
006 left, plus G15's symbolic add-on).

**Key invariant (carried from v1.1 + v1.2 + v1.3):**

The strategic picture's framing of *what success means* is
unchanged. P-MC closure still requires P-NP + P-B4 + P-CC.
v1.4 records:
- a *positive* event on the P-CC axis (108-digit Stokes-amplitude
  measurement; M6 done with substantial margin), and
- a refinement of H4 (β=0 logarithmic class instead of the
  expected half-integer; consistent with the existing hedge),
- and surfaces a *new* coordinate-system gap (G15) that gates
  the *canonical* version of `op:cc-formal-borel` and any
  external-literature comparison.

The headline number — $S_{\zeta_*} \approx 51.0656\, i$ in
V_quad native form — is a measurement of historic
significance for SIARC: P-CC's prediction-and-measurement
loop is now closed at extreme precision, and the
remaining work on the channel-theory axis is *coordinate
discipline* (G15) rather than fresh computation.

**Epistemic posture observation:**

Prompt 005's relay agent demonstrated three healthy
behaviours: (i) self-validation of the recurrence against
the upstream `formal_solve` reference solver, (ii)
substitution-with-disclosure of Phase D when the
prescribed method became degenerate, and (iii) honest
identification of the V_quad → P_III(D_6) normalization
gap as a residual rather than burying it inside the
verdict. The 108-digit cross-method agreement is the
operative evidence, but the *meta*-evidence — that the
agent surfaced the substitution and the gap — is itself
the AEAL discipline working as designed.

---

## 13. Amendment Log (v1.2 → v1.3)

**Updated:** 2026-05-02 18:30 JST
**Trigger:** Prompt 002 HALT with verdict
`ARXIV_MIRROR_HALTED_PAGE_COUNT_DRIFT_2` + 2 anomalies flagged
in the same session.

**Substantive changes:**

| Section | v1.2 → v1.3 |
|---------|-------------|
| Header  | Added v1.2 → v1.3 callout. Earlier callouts retained for the synthesizer's full audit trail. |
| § 2.3 (in-flight) | Added "1 fired and HALTED" line for 002. New entry for `pcf1-v13-reconcile` (future Prompt 011). Counts updated (15 pending / 18 done of 33). 2 ready (was: 3) since 002 dropped out. |
| § 2.4 (recently closed) | Added 002 partial-build line with HALT caveat. |
| § 5 gaps | G9 status changed from "ready to fire" to "HALTED 2026-05-02; staged locally; reactivate after G12+G13+G14". New rows G12 (PCF-1 source drift, HIGH), G13 (CT author placeholder, HIGH), G14 (endorser handles, MED). |
| § 6 prompts table | 002 marked HALTED with specifics. New row for Prompt 011 (PCF1-V13-RECONCILE). Firing layout rewritten (002 removed; G12/G13/G14 operator items added). |
| § 8 open questions | Added Q11 — PCF-1 v1.4 release-discipline question (was the operator implicitly aiming at v1.4 before arXiv mirroring?). |
| § 10 footer | Bridge head bumped (still no 002 commit); commit timeline shows 002 as STAGED LOCAL ONLY. |
| § 13 (this section) | NEW. |

**Unchanged:**

§ 1 (mission statement), § 9 (AEAL hygiene), the publication
ladder table, the six-program decomposition, and § 3 program
table are intact. The concurrency map (§ 6) is unchanged in
shape; the *content* of the firing layout has shifted.

**Key invariant (carried from v1.1 + v1.2):**

The strategic picture's framing of *what success means* is
unchanged. P-MC closure still requires P-NP + P-B4 + P-CC.
v1.3 records an *operational/distribution-layer event*: the
arXiv mirror runbook found a source-drift discrepancy on
PCF-1 between the workspace and the published Zenodo v1.3.
This does **not** affect any published artefact's correctness
— the published Zenodo PDFs are canonical. But it does block
arXiv mirroring of record #2 until the source is reconciled,
and it surfaces a release-discipline open question (Q11).

**Epistemic posture observation:**

Prompt 002's HALT is a *successful* AEAL-honest behaviour —
the agent detected a hidden state inconsistency the operator
was unaware of, refused to push false invariants, and surfaced
the discrepancy with full hash evidence. The two anomaly
flags (G13, G14) were similarly raised rather than papered
over. This is the design pattern working as intended.

---

## 12. Amendment Log (v1.1 → v1.2)

**Updated:** 2026-05-02 18:25 JST
**Trigger:** completion of Prompt 007 (T3 Conte–Musette
Painlevé test) on the same day as v1.1.

**Substantive changes:**

| Section | v1.1 → v1.2 |
|---------|-------------|
| Header  | Added v1.1 → v1.2 callout. v1.0 → v1.1 callout retained for the synthesizer's full audit trail. |
| § 2.2 (verified) | Added T3 verdict bullet (60/60 LABELED; V_quad PASS; H3 negatively closed). |
| § 2.3 (in-flight) | 4 fired/done (was: 3); 3 still ready (was: 4). New entry for `t3-stokes-multiplier-followup` (future Prompt 010). Counts updated. |
| § 2.4 (recently closed) | Added T3 line. |
| § 3 P-PIII row | Status changed from "$d=2$ AMBIGUOUS (H3); $d=3$ partial" to detailed T3 result + H3 negative-closure caveat. |
| § 4 milestones | M8 marked COMPLETE with the negative-closure caveat. New M8b added for the Stokes-multiplier follow-up. |
| § 5 gaps | G6 split into G6a (✅ Conte–Musette test complete) + G6b (Stokes-multiplier discrimination needed). |
| § 6 prompts table | 007 marked DONE; new row for Prompt 010 (future). Firing layout rewritten for next compute window (002, 005, 006). |
| § 8 open questions | Added Q10 — does the H3 negative closure imply that P-MC's invariant triple needs a Stokes-data fourth coordinate? |
| § 10 footer | Bridge head bumped; commit timeline extended. |
| § 12 (this section) | NEW. |

**Unchanged:**

§ 1 (mission statement), § 9 (AEAL hygiene), the publication
ladder table, and the six-program decomposition are intact.
The concurrency map (§ 6) is unchanged.

**Key invariant (carried from v1.1):**

The strategic picture's framing of *what success means* is
unchanged. P-MC closure still requires P-NP + P-B4 + P-CC.
v1.2 adds a *resolution-scale observation* about P-PIII: the
algorithmic Painlevé test sits one resolution scale *above*
the PCF-1 v1.3 §3 sign dichotomy, so per-family Painlevé
classification at that scale is necessarily uniform. The
sign-split discrimination is a separate (Stokes-multiplier)
question.

---

## 11. Amendment Log (v1.0 → v1.1)

**Updated:** 2026-05-02 18:20 JST
**Trigger:** completion of three relay-agent firings (001, 003, 004)
on the same day as v1.0 was first written.

**Substantive changes:**

| Section | v1.0 → v1.1 |
|---------|-------------|
| Header  | Added "🆕 Updates since v1.0" callout listing the three completed firings + the new HIGH-severity gap G11. |
| § 2.2 (verified) | Added two new bullets: T1 Phase 1 verdict bullet + D2-NOTE drafting bullet. |
| § 2.3 (in-flight) | Restructured: 3 fired/done, 4 still ready, 1 (Prompt 008) blocked. |
| § 2.4 (recently closed) | Added Item 19 splice, T1 Phase 1, D2-NOTE drafting. |
| § 3 P-B4 row | Status changed from "EMPIRICAL d=3,4; PROOF GAP" to "EMPIRICAL d=3,4; LITERATURE BRACKET $A \in [d,2d]$; H1 fleet label DISPUTED". |
| § 4 milestones | M1 marked DRAFTED (awaits upload). M3 marked DONE. M4 marked BLOCKED with explicit gating items. M9 explanatory note about being one step further out. |
| § 5 gaps | G3 split into G3a (literature bracket established, ✅) + G3b (normalization match BLOCKER, HIGH). G1 + G8 marked as "drafted; closure pending Zenodo upload". G11 ADDED (HIGH, H1 label arbitration). |
| § 6 prompts table | Status column added; 001/003/004 marked DONE; 002 marked unblocked; Prompt 008 row added (BLOCKED). |
| § 6 firing layout | Rewritten for the *next* compute window. Added operator-side parallel actions (Zenodo upload, primary-source ILL, Claude H1 review). |
| § 7 decision tree | Point 3 rewritten to reflect 003's actual verdict; "What this cycle CANNOT do" updated for M4's new gating. |
| § 8 open questions | Added Q8 (H1 arbitration) and Q9 (Phase 2 single-vs-multi-step). |
| § 10 footer | Bridge head bumped to `9accc6e`; commit timeline added. |
| § 11 (this section) | NEW. |

**Unchanged:**

§ 1 (mission statement), § 9 (AEAL hygiene), and the publication
ladder table are intact. The six-program decomposition is
unchanged. The concurrency map (§ 6) is unchanged (no new
inter-prompt dependencies were introduced; only the row-level
"status" column was added).

**Key invariant:**

The strategic picture's framing of *what success means* is
unchanged. P-MC closure still requires P-NP + P-B4 + P-CC; the
v1.1 update only changes *the path to P-B4*, not the goal.

---

*End of revised picture (v1.8).*
