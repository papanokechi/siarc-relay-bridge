# Extracted claims (raw)

## UMB -- `tex\submitted\umbrella_program_paper\main.tex` (sha12=75485e5bbd9b)
- **conjecture** `conj:t2b`  *[Trans-Stratum $-2/9$ Conjecture]*
  > \label{conj:t2b} Let $\{K(x)\}$ be a PCF family of generic degree $(2,1)$ uniformized by $\PSLZ$, satisfying the regularity conditions of companion paper~T2B. Then $K(x)$ lies in tier T2, and its trans-stratum exponent satisfies \begin{equation} c_{\PSLZ,(2,1)} \;=\; -\tfrac{2}{9}. \end{equation}
- **definition** `(no label)`  *[Tier T0: Algebraic]*
  > A PCF family $\{K(x)\}_{x \in S}$ lies in tier T0 over an arithmetic set $S \subseteq \Z_{\geq 1}$ if $K(x)$ is algebraic over $\Q$ for every $x \in S$, and the algebraic degree is uniformly bounded as $x$ varies in $S$.
- **definition** `(no label)`  *[Tier T1: Transcendental]*
  > A PCF family lies in tier T1 if $K(x)$ is transcendental for every $x \in S$, \emph{and} a Mahler-type or Nesterenko-type criterion certifies the transcendence uniformly in $x$.
- **definition** `(no label)`  *[Tier T2: Trans-stratum]*
  > A PCF family lies in tier T2 if its irrationality measure $\mu(K(x))$ satisfies an asymptotic \[ \mu(K(x)) \;=\; 2 + \frac{c}{\log x} + o\!\left(\frac{1}{\log x}\right), \qquad x \to \infty, \] for an explicit rational constant $c$ (the \emph{trans-stratum exponent}) that depends only on the polynomial degrees $(\deg a, \deg b)$ and the Fuchsian group $\Gamma$. The trans-stratum is therefore not a
- **definition** `(no label)`  *[Tier T3: Barrier]*
  > A PCF family lies in tier T3 if the Fuchsian uniformization itself degenerates: either $\Gamma$ fails to be of finite covolume, or the associated $L$-function fails to admit analytic continuation to the required half-plane. T3 families are inaccessible to the methods of T0--T2 and serve as the negative boundary of the program.
- **problem** `prob:31`  *[Degree-$(3,1)$ classification]*
  > \label{prob:31} Establish the four-tier classification for $\PSLZ$-uniformized PCF families of generic degree $(3,1)$. The asymmetry between numerator and denominator degrees breaks the symmetric treatment of \#14.
- **problem** `prob:t2-d2-nonpsl`  *[Trans-stratum at $d=2$ for non-$\PSLZ$]*
  > \label{prob:t2-d2-nonpsl} Determine the trans-stratum exponent $c_{\Gamma,(2,1)}$ for $\Gamma = \Gamma_0(2)$ and for the Hecke triangle groups $G_q$ with $q \geq 4$. Is the value $-2/9$ specific to $\PSLZ$, or does it recur with a $\Gamma$-dependent denominator?
- **problem** `prob:painleve`  *[Painlevé connection]*
  > \label{prob:painleve} Make precise the conjectural correspondence between trans-stratum PCF families and solutions of Painlevé~VI with monodromy in $\Gamma$. A pointer-level discussion is given in companion paper~P08; a full correspondence theorem is open.
- **problem** `prob:effective`  *[Effective T0/T1 boundary]*
  > \label{prob:effective} Provide an algorithm that, given the polynomials $a_n(x), b_n(x)$ in exact arithmetic, decides in finite time whether the family lies in T0 or T1. \#14 establishes the boundary as a set; effectivity is open.
- **problem** `prob:t3`  *[T3 nonemptiness]*
  > \label{prob:t3} Exhibit an explicit PCF family that provably lies in T3 (not merely fails to lie in T0--T2 by current methods). Equivalently, exhibit a PCF whose monodromy group has infinite covolume in a controlled way.
- **problem** `prob:mahler`  *[Mahler-Nesterenko gap]*
  > \label{prob:mahler} For T1 families, identify the precise hypothesis that fails when the Mahler criterion does not apply and the Nesterenko criterion does. The empirical gap is small; a structural explanation is missing.
- **problem** `prob:census`  *[Census completeness]*
  > \label{prob:census} Extend the empirical census underlying Conjecture~\ref{conj:t2b} beyond degree-$(2,1)$. A negative result --- a single counterexample in any degree --- would falsify the Trans-Stratum Conjecture as stated and force a refinement.

## P14 -- `tex\submitted\paper4_takeuchi_outline.tex` (sha12=9a7a04baaadb)
- **conjecture** `(no label)`  *[Tier 0 generic transcendence]*
  > For a Tier~0 family, the PCF evaluation point $z_0$ is generically transcendental and non-CM, while genuinely algebraic or CM values arise only at isolated modularly distinguished arguments.
- **conjecture** `(no label)`  *[Tier 1 cusp rigidity]*
  > Every arithmetic-but-degenerate PCF family is governed by a finite list of cusp signatures, and the analytic Frobenius obstruction is determined by that cuspidal degeneration data.
- **conjecture** `(no label)`  *[Tier 2 rigidity]*
  > No Tier~2 family can be rescued by a rational change of variable, M\"obius normalization, or classical Hauptmodul substitution while remaining inside the same Gauss \({}_2F_1\) framework.
- **conjecture** `(no label)`  *[Tier 3 uniformization principle]*
  > Tier~3 families should admit a different arithmetic or geometric description, if any exists, through a Heun, confluent-Heun, or isomonodromic framework rather than through classical Schwarz triangles.
- **conjecture** `(no label)`  *[Master hierarchy conjecture]*
  > Every polynomial continued fraction family in the present spectral program admits a well-defined tier within the framework of Section~\ref{sec:tiers}. Moreover, the tier determines the correct ambient geometry: modular, cuspidal, non-arithmetic Fuchsian, or irregular Heun.
- **theorem** `thm:psl2z`  *[Arithmetic PCF families uniformize \(X(1)\)]*
  > \label{thm:psl2z} Every arithmetic polynomial continued fraction family in the current verified $d=1$ taxonomy has hypergeometric Schwarz triangle group commensurable with the full modular group $\mathrm{PSL}_2(\mathbf{Z})$. Equivalently, every arithmetic family uniformizes the classical modular curve $X(1)$.
- **lemma** `lem:takeuchi`  *[Takeuchi obstruction for non-arithmetic PCF families]*
  > \label{lem:takeuchi} Let $K(a_n,b_n)$ be a $d=1$ polynomial continued fraction admitting a Gauss hypergeometric witness ${}_2F_1(a,b;c;z)$, and let $\tau(z)$ be its Schwarz period ratio. If the associated triangle-order triple $(\infty,q,r)$ with $q=|a-b|$ and $r=|a+b-c|$ does not occur on Takeuchi's arithmetic list, then the Schwarz group is non-arithmetic. Consequently the family has no Shimura-
- **proposition** `prop:spectral-class`  *[Spectral class is complete only up to modular sampling]*
  > \label{prop:spectral-class} Define the coefficient-level spectral class by \[ \mathrm{SC}(K):=(\Delta_\infty \bmod 24,\, \mathrm{tier},\, \mu), \] where $\mu=|a-b|$ is the middle Schwarz order in the project normalization. Then for the verified $d=1$ Gauss-sector rows, $\mathrm{SC}(K)$ cleanly separates the obstruction \emph{mode}, but it does not distinguish the seven arithmetic families individu
- **proposition** `prop:heun`  *[Heun obstruction for \texttt{V\_quad}]*
  > \label{prop:heun} The family \texttt{V\_quad} does not admit a Gauss-Schwarz triangle interpretation of the type governing the $d=1$ arithmetic PCF families. Instead it belongs to an irregular, confluent-Heun-type sector with an obstruction coming from the singularity at infinity.

## P14alt -- `tex\submitted\paper14-ratio-universality-SUBMISSION.tex` (sha12=30233ba219c5)
- **theorem** `thm:meinardus`  *[Meinardus]*
  > \label{thm:meinardus} Let~$F(q)$ be as in~\eqref{eq:generating} with associated Dirichlet series~$D(s) = \sum_{m=1}^\infty a_m\,m^{-s}$ convergent for $\Re(s) > \alpha$ and satisfying standard analytic conditions. Then \begin{equation}\label{eq:meinardus} f(n) \;\sim\; C_0\,n^{\kappa}\,e^{c\sqrt{n}} \qquad (n \to \infty), \end{equation} where~$c = \sqrt{2A \cdot \pi^2/3}$, $A = D(1)$, and~$\kappa 
- **theorem** `thm:ratio`  *[Ratio Universality]*
  > \label{thm:ratio} Let~$\{f(n)\}$ be a sequence with Meinardus-type asymptotics \[ f(n) = C_0\,n^{\kappa}\,e^{c\sqrt{n}}\!\left(1 + \sum_{j=1}^{M} A_j\,n^{-j/2} + E_M(n)\right), \qquad |E_M(n)| \leq B_M\,n^{-(M+1)/2}. \] Then the consecutive ratio admits the expansion \begin{equation}\label{eq:ratio_expansion} R_m = \frac{f(m)}{f(m-1)} = 1 + \frac{c}{2\sqrt{m}} + \frac{L}{m} + \frac{\alpha}{m^{3/2}
- **theorem** `thm:ratio_prime`  *[Ratio Expansion with Controlled Error]*
  > \label{thm:ratio_prime} Under the hypotheses of Theorem~\ref{thm:ratio} with expansion order~$M \geq 1$: \begin{equation}\label{eq:ratio_M} R_n = 1 + \sum_{j=1}^{M} C_j\,n^{-j/2} + O_{c,\kappa,B_M}\!\left(n^{-(M+1)/2}\right), \end{equation} where~$C_1 = c/2$, $C_2 = c^2/8 + \kappa$, and~$C_3 = c(c^2+6)/48 + c\kappa/2 - A_1/2$.
- **theorem** `thm:cuberoot`  *[Cube-Root Ratio]*
  > \label{thm:cuberoot} \begin{equation}\label{eq:cuberoot} R_m = 1 + \frac{2c}{3\,m^{1/3}} + \frac{2c^2}{9\,m^{2/3}} + \frac{L_{\mathrm{pp}}}{m} + O(m^{-4/3}), \qquad L_{\mathrm{pp}} = \frac{4c^3}{81} + \kappa. \end{equation}
- **theorem** `thm:A1k`  *[Proven for $k = 1, 2, 3, 4$]*
  > \label{thm:A1k} For~$k$-colored partitions with~$k \in \{1,2,3,4\}$: \begin{equation}\label{eq:A1k} A_1^{(k)} = -\frac{k\,c_k}{48} - \frac{(k+1)(k+3)}{8\,c_k}, \end{equation} where~$c_k = \pi\sqrt{2k/3}$. Equivalently:~$A_1^{(k)} = -[2k^2\pi^2 + 18(k+1)(k+3)]/(144\pi\sqrt{2k/3})$.
- **theorem** `conj:2star`  *[Theorem $2^*$ (formerly Conjecture $2^*$)]*
  > \label{conj:2star} The formula of Theorem~\ref{thm:A1k} extends to all~$k \geq 1$: \[ A_1^{(k)} = -\frac{k\,c_k}{48} - \frac{(k+1)(k+3)}{8\,c_k}, \qquad c_k = \pi\sqrt{2k/3}. \] Equivalently, \[ A_1^{(k)} = -\frac{2k^2\pi^2 + 18(k+1)(k+3)}{144\pi\sqrt{2k/3}}. \]
- **theorem** `thm:A2k`  *[$A_2^{(k)}$ and $\beta_k$ --- proved for $k=1$; Conjecture $3^*$ for $k \geq 2$]*
  > \label{thm:A2k} \begin{align} A_2^{(k)} &= \frac{(k+3)(\pi^2 k^2 - 9k - 9)}{96\,k\,\pi^2}, \label{eq:A2k}\\[4pt] \beta_k &= \frac{k^3\pi^6 - 3k^2(5k+6)\pi^4 + 45k^2(k+3)\pi^2 + 81(k+1)(k+3)}{864\,k\,\pi^2}. \label{eq:betak} \end{align} The fourth-order decomposition gives \begin{equation}\label{eq:beta_decomp} \beta_k = \frac{c^4}{384} + \frac{c^2(1+2\kappa)}{16} + \frac{\kappa(\kappa+1)}{2} - \fr
- **lemma** `lem:selection`  *[General Selection Rule]*
  > \label{lem:selection} For~$f(n) \sim C_0\,n^{\kappa}\,e^{c\,n^d}(1 + A_1\,n^{-d} + O(n^{-2d}))$ with~$d \in (0,1)$: \[ R_m = 1 + \frac{cd}{m^{1-d}} + \cdots + \frac{L_d}{m} + O(m^{-(1+d)}), \] where~$L_d$ depends only on~$c$, $\kappa$, $d$, and~$A_1$ is \textbf{forbidden} from contributing until order~$m^{-(1+d)}$.
- **lemma** `lem:pp`  *[Lemma PP: Plane Partition Sub-Leading Expansion]*
  > \label{lem:pp} \begin{equation}\label{eq:lemma_pp} \mathrm{PL}(n) = C_{\mathrm{pp}}\,n^{-25/36}\,e^{c_{\mathrm{pp}}\,n^{2/3}}\!\left(1 + \frac{A_1^{\mathrm{pp}}}{n^{1/3}} + E_1(n)\right), \qquad |E_1(n)| \leq \frac{B_1}{n^{2/3}}, \end{equation} where~$B_1 \leq 18.3$ (uniform) and~$B_1^{\mathrm{eff}} \leq 2.5$ (tightened via Olver bounds).
- **lemma** `lem:K`  *[Lemma~K: conductor-$24$ Kloosterman bound]*
  > \label{lem:K} For every fixed integer $k\ge1$ there is a constant $C_k>0$ such that \begin{equation}\label{eq:lemmaK-weil} |K_k(n,1;c)| \le C_k\,d(c)\,c^{1/2} \end{equation} for all $n\ge1$ and $c\ge1$. If $R_k(n)$ denotes the $c\ge2$ tail and $M_k(n)$ the $c=1$ term in the Rademacher expansion of $p_k(n)$, then \begin{equation}\label{eq:lemmaK-tail} \frac{R_k(n)}{M_k(n)}=O_k\!\left(n^{1/2+\vareps
- **definition** `def:K24`  *[Level-$24$ twisted Kloosterman sum]*
  > \label{def:K24} For $c\ge2$ and $d$ with $0\le d<c$ and $(d,c)=1$, let $a\equiv d^{-1}\pmod c$ and define \[ \theta_c(d)=\frac{a+d}{12c}-s(d,c), \qquad s(d,c)=\sum_{r=1}^{c-1}\Bigl(\!\Bigl(\frac{r}{c}\Bigr)\!\Bigr)\Bigl(\!\Bigl(\frac{dr}{c}\Bigr)\!\Bigr), \] where $((x))=x-\lfloor x\rfloor-\tfrac12$ for $x\notin\mathbb Z$ and $((x))=0$ for $x\in\mathbb Z$. Dedekind's transformation law gives \[ \n

## T2A -- `t2a_paper_draft.tex` (sha12=6d07e458ab12)
- **observation** `obs:cmax1`  *[CMAX$=1$ Trans-hard density]*
  > \label{obs:cmax1} Of the $1{,}458$ degree-$(4,2)$ families with coefficient bound $1$ (modulo the WLOG sign symmetry $a_4 > 0$), exactly $1{,}162$ are Trans-hard: they admit no integer relation against the extended bilinear-$\pi$ basis at precision $\dps=300$.
- **observation** `obs:cmax2`  *[CMAX$=2$ Trans-hard density at scale]*
  > \label{obs:cmax2} Of the $125{,}000$ degree-$(4,2)$ families at coefficient bound $2$, $108{,}762$ ($\approx 87.0\%$) survive the float and mpmath prescreens as Trans-candidates. A uniform random sample of size $1{,}000$ from the deduplicated-by-limit candidates is deep-validated at $\dps=150$, with all $1{,}000$ returning Trans-hard against a $9$-element bilinear-$\pi$ basis.
- **observation** `obs:ratio-refuted`  *[Refutation of the ratio sub-hypothesis]*
  > \label{obs:ratio-refuted} Among the $1{,}000$ deep-validated families, the leading-coefficient ratio $\rho := a_4/b_2^2$ takes only values in $\{1/4,\;1/2,\;1,\;2\}$, distributed approximately uniformly ($\sim25\%$ each). The Trans-hard pass rate, conditioned on $\rho$, is $\{85.8\%, 89.1\%, 86.0\%, 89.0\%\}$ respectively---a spread of $3.3$ percentage points. No single value of $\rho$ predicts Tr
- **observation** `obs:R1`  *[A novel transcendental candidate]*
  > \label{obs:R1} A specific Trans-hard family at $\mathrm{CMAX}=1$ produces the limit \[ R_1 \;=\; -0.10123520070804963\,\ldots \qquad (30\ \text{significant digits}), \] which fails PSLQ identification against an extended seven-family basis at $\dps=300$, returns no match in OEIS on its $17$-digit prefix, and is detected by the RIES inverse-symbolic search only at an $8$-digit coincidence (with abs
- **observation** `obs:cmax1cert`  *[CMAX$=1$ certificate]*
  > \label{obs:cmax1cert} Out of $1{,}162$ Trans-candidate families, $1{,}162/1{,}162$ are Trans-hard at $\dps=300$ against the seven-family extended basis, yielding $0$ identifications across $35$ PSLQ probes ($5$ representative limits times $7$ bases).
- **observation** `obs:cmax2dv`  *[CMAX$=2$ deep validation]*
  > \label{obs:cmax2dv} $1{,}000/1{,}000$ sampled families return Trans-hard at $\dps=150$.
- **observation** `obs:rho-flat`  *[Ratio is not predictive]*
  > \label{obs:rho-flat} The Trans-hard rate by $\rho$ has spread $89.1 - 85.8 = 3.3$ percentage points over a $108{,}762$-family base. No value of $\rho$ materially predicts Trans-hardness; in particular the F$(2,4)$ value $\rho_{\text{F$(2,4)$}} = -2/9$, which has no analogue at degree $(4,2)$ because $\rho$ here is a square-denominator ratio, does not extend. The natural ``ratio-as-structural-law''
- **observation** `obs:apery-refuted`  *[$\pi^2$--Ap\'ery refuted at $k=2$]*
  > \label{obs:apery-refuted} $0$ of $1{,}000$ deep-validated families admit an integer relation against the basis containing $L\cdot\pi^2$, with the L-coefficient non-zero, at $\dps=150$.
- **definition** `(no label)`  *[Sign-symmetry reduction]*
  > The map $(a,b) \mapsto (-a, b)$ negates the limit, so without loss of generality we restrict to $a_4 > 0$. This halves the effective search space.
- **problem** `prob:R1`  *[Identification of $R_1$]*
  > \label{prob:R1} Determine an arithmetic characterisation of $R_1$, or prove that $R_1$ is not in $\overline{\mathbb{Q}(\pi,\log 2,\zeta(3))}$.
- **problem** `(no label)`  *[Basis identification]*
  > Determine the smallest basis $B$ of constants such that some nontrivial $\mathbb{Z}$-linear relation exists between $R_1$ and elements of $B$, or prove no such finite $B$ exists.
- **problem** `(no label)`  *[Extension to $k=3$]*
  > Carry out the analogous enumeration at degree profile $(6,3)$. The F$(2,4)$ enumeration cost is $\sim 5\times 10^5$ families; the degree-$(4,2)$ enumeration at $\mathrm{CMAX}=2$ costs $1.25\times 10^5$ families. At $\mathrm{CMAX}=2$, degree-$(6,3)$ would cost $5^{10} \approx 10^7$ families before symmetry reductions, an order-of-magnitude jump that nevertheless remains feasible.
- **problem** `prob:density`  *[Theoretical explanation for the $\sim87\%$ density]*
  > \label{prob:density} At $\mathrm{CMAX}=2$, $87\%$ of degree-$(4,2)$ families are Trans-hard at deep precision. Provide a heuristic or theoretical prediction of this density. Compare against the corresponding density at $\mathrm{CMAX}=1$, $\mathrm{CMAX}=3$, and as $\mathrm{CMAX}\to\infty$.
- **problem** `(no label)`  *[Connection to known transcendence theory]*
  > Determine whether any of the candidate Trans-hard limits arise as periods (in the sense of Kontsevich--Zagier) or as values of the Riemann zeta function or Dirichlet $L$-functions at integer arguments. Negative results in this direction would strengthen the case for the existence of a new family of transcendental constants.

## T2B -- `tex\submitted\t2b_paper_draft_v5_withauthor.tex` (sha12=d7630e6b2548)
- **conjecture** `conj:completeness`  *[Completeness, T2B-revised]*
  > \label{conj:completeness} The degree-$(2,1)$ Trans-stratum is exactly $\mathcal{T}_A \sqcup \mathcal{T}_B$, with no third class. Equivalently: every convergent generic-irrational integer degree-$(2,1)$ PCF has $a_2/b_1^2 \in \{-2/9, +1/4\}$.
- **theorem** `thm:resonance-family`  *[Resonance family]*
  > \label{thm:resonance-family} The two roots $\lambda_\pm$ of \eqref{eq:characteristic} satisfy $\lambda_+ = k\,\lambda_-$ for some $k\in\mathbb{Z}_{\ge 1}$ if and only if \begin{equation}\label{eq:resonance-formula} \frac{a_2}{b_1^2} \;=\; -\frac{k}{(k+1)^2}. \end{equation}
- **theorem** `thm:k2-stokes`  *[Class A characterisation]*
  > \label{thm:k2-stokes} Conditional on $S_{12}\ne 0$ on $\mathcal{R}_2$ (Hypothesis~S), the Class A locus \[ \mathcal{T}_A \;=\; \mathcal{R}_2 \cap \mathcal{T} \;=\; \mathcal{R}_2 \cap \{S_{12}\ne 0\} \] contains $\Theta(N^4)$ primitive integer points of height $\le N$, in agreement with the empirical density of $\sim 1.5\times 10^5$ at $N=100$.
- **theorem** `thm:classB-stieltjes`  *[Class B Stieltjes equivalence]*
  > \label{thm:classB-stieltjes} Let $(a_2, 0, 0, b_1, b_1/2) \in \mathbb{Z}^5$ be a Pure-regime Class B family ($a_2 = b_1^2/4$, $a_1 = a_0 = 0$, $b_0 = b_1/2$, equivalently $b(n) = (b_1/2)(2n+1)$). Under the equivalence transformation \eqref{eq:mu}, recurrence \eqref{eq:recurrence} maps to the canonical Wallis kernel \begin{equation}\label{eq:wallis-kernel} a^*(n) = \frac{(2n)^2}{(2n-1)(2n+1)}, \qqu
- **lemma** `lem:bt-formal`  *[BT formal solutions]*
  > \label{lem:bt-formal} For $a_2 \ne 0$ and $b_1^2 + 4a_2 \ne 0$, recurrence \eqref{eq:recurrence} admits two linearly independent formal solutions \begin{equation}\label{eq:bt-ansatz} Q^\pm(n) \;=\; \lambda_\pm^{\,n}\,(n!)\,n^{\rho_\pm}\Bigl(1 + \sum_{j\ge 1} c_j^\pm\,n^{-j}\Bigr), \end{equation} with $\lambda_\pm$ the roots of \begin{equation}\label{eq:characteristic} \chi(\lambda) \;=\; \lambda^2
- **lemma** `lem:Delta2-trivial`
  > \label{lem:Delta2-trivial} On $\mathcal{R}_2$ the BT formal coefficients $\{c_j^-\}$ are determined uniquely and regularly through depth four; the would-be obstruction polynomial $\Delta_2$ vanishes identically: $\Delta_2 \equiv 0$.
- **proposition** `prop:pincherle`  *[Pincherle's theorem]*
  > \label{prop:pincherle} The PCF \eqref{eq:pcf-form} converges in $\widehat{\mathbb{C}}$ if and only if \eqref{eq:recurrence} admits a \emph{minimal} (subdominant) solution $Q^{\min}$. The limit is $-Q^{\min}(-1)/Q^{\min}(0)$ in the standard normalization \cite[Thm.~3.7]{lw1992}.
- **corollary** `cor:k=2`
  > \label{cor:k=2} The identity $a_2/b_1^2 = -2/9$ is exactly $k=2$ in \eqref{eq:resonance-formula}: $\lambda_- = b_1/3$, $\lambda_+ = 2b_1/3$.
- **corollary** `cor:classB-pi`  *[Pure-regime Class B is in $\mathbb{Q}(\pi)$]*
  > \label{cor:classB-pi} For every Pure-regime Class B family the limit lies in $\mathbb{Q}\cdot\pi^{-1}$. The five primitive Pure-regime families found by the SIARC search at height $\le 100$ are listed in Table~\ref{tab:classB-pure}.
- **definition** `def:trans-stratum`
  > \label{def:trans-stratum} The \emph{Trans-stratum} $\mathcal{T} \subset \mathbb{Z}^5$ is the set of primitive integer tuples $(a_2,a_1,a_0,b_1,b_0)$ with $a_2 b_1 \ne 0$ such that the limit $L$ exists in $\mathbb{R}$ and $L \notin \mathbb{Q}$ (the convergent, generic-irrational subclass implemented in \cite{siarc2024}).
- **definition** `def:Rk`
  > \label{def:Rk} For each $k\in\mathbb{Z}_{\ge 1}$, the $k$-th \emph{integer-resonance locus} is \[ \mathcal{R}_k \;=\; \bigl\{(a_2,a_1,a_0,b_1,b_0)\in\mathbb{R}^5\,:\,b_1\ne 0,\;a_2/b_1^2 = -k/(k+1)^2\bigr\}. \] We additionally distinguish the \emph{Wallis locus} $\mathcal{W} = \{a_2/b_1^2 = 1/4\}$.

## P06 -- `tex\submitted\p06_desert_ijnt_submission\pcf_desert_negative_result.tex` (sha12=1c5616e09589)
- **conjecture** `conj:desert`
  > \label{conj:desert} Let $a(n), b(n) \in \Z[n]$ with $\deg a = d_a \leq 5$, $\deg b = 3$, and suppose the generalized continued fraction $V = b(0) + K_{n=1}^{\infty}(a(n)/b(n))$ converges. Then $V$ admits no relation of the form \[ c_0 V + c_1 \beta_1 + \cdots + c_{12} \beta_{12} = 0, \qquad c_i \in \Z, \quad c_0 \neq 0, \quad \max|c_i| \leq 10{,}000, \] where $\{\beta_1, \ldots, \beta_{12}\} = \ca

## P08 -- `tex\submitted\vquad_resurgence_R2.tex` (sha12=2bda5a8e4732)
- **conjecture** `conj:S_id`  *[Identification of $S$]*
  > \label{conj:S_id} The Stokes constant $S\approx 0.43770528\ldots$ is given by the Jimbo (1982) \cite{Jimbo1982} formula \[ S = 2i\sin(\pi\sigma_{\mathrm{conn}}) \,\frac{\Gamma(1-\sigma_{\mathrm{conn}})^2} {\Gamma(1+\sigma_{\mathrm{conn}})^2}, \] where $\sigma_{\mathrm{conn}}$ satisfies $\mathrm{tr}(M_1 M_2) = 2\cos(2\pi\sigma_{\mathrm{conn}})$ for the monodromy matrices of the associated Riemann--
- **theorem** `thm:exclusion2`  *[Apparent singularity exclusion
for $\Vq$]*
  > \label{thm:exclusion2} Let $\Vq$ be the Stokes connection coefficient $M_{11}$ of the ODE~\eqref{eq:ode}. \begin{enumerate} \item[\textup{(i)}] At both finite singularities $s_{1,2}=(-1\pm i\sqrt{11})/6$, the indicial equation is $\rho^2=0$, giving a double root $\rho=0$. \item[\textup{(ii)}] The monodromy around each $s_k$ fixes $M_{11}=\Vq$; the effective monodromy on the connection coefficient 
- **theorem** `thm:painleve`  *[PIII($D_6$) classification]*
  > \label{thm:painleve} The isomonodromic deformation family containing the ODE~\eqref{eq:ode} is governed by degenerate Painlev\'e~V, equivalently PIII($D_6$) in the Sakai classification, with parameters \[ \alpha = \frac{1}{6},\quad \beta = 0,\quad \gamma = 0,\quad \delta = -\frac{1}{2}. \] The vanishing $\beta = \gamma = 0$ reflects the fact that both finite singularities are apparent.
- **theorem** `thm:borel`  *[Borel singularity]*
  > \label{thm:borel} The Borel transform $\hat{y}(\xi)$ of the formal series~\eqref{eq:formal} has a branch-point singularity at $\xi_0 = 2/\sqrt{3}$ on the negative real Borel axis. \begin{enumerate} \item[\textup{(i)}] The Domb--Sykes ratio $r_n = |a_n/a_{n-1}|$ satisfies $r_n \to 1/\xi_0 = \sqrt{3}/2$, confirmed by Richardson extrapolation to five significant figures. \item[\textup{(ii)}] The bran
- **proposition** `prop:stokes`  *[Stokes constant estimate]*
  > \label{prop:stokes} Using $501$ formal series terms with $\beta_{\mathrm{exp}} = -1/(3\sqrt{3})$ and $\xi_0 = 2/\sqrt{3}$: \begin{enumerate} \item[\textup{(i)}] Dingle--Richardson${}^2$ extraction in $1/(n+\beta)$ gives $S \approx 0.43770528$. \item[\textup{(ii)}] Split-half consistency (first 250 vs.\ last 251 terms) confirms $8$ significant digits. \item[\textup{(iii)}] PSLQ searches against $14

## P11 -- `f1_mathcomp_submission\main_R1.tex` (sha12=37a36a4a1684)
- **theorem** `thm:main`  *[Main theorem]*
  > \label{thm:main} Every convergent family in $\FF(2,4)$ falls into exactly one of the five strata. The partition is: \[ \Rat(113{,}270) \sqcup \Log(0) \sqcup \Alg(0) \sqcup \Trans(24) \sqcup \Des(400{,}093) = 513{,}387. \] The $24$ $\Trans$-stratum families have limits that are M\"obius transforms of~$\pi$, and are transcendental by Lindemann--Weierstrass.
- **theorem** `thm:rat`  *[Rat stratum, $\FF(2,4)$]*
  > \label{thm:rat} Among $531{,}441$ families in $\FF(2,4)$, exactly $113{,}270$ are $\Rat$. These decompose as: \begin{itemize}[leftmargin=2em] \item \emph{Trivial zero mechanism} ($a(1) = 0$): $729$ families. These satisfy $a(1) = a_2 + a_1 + a_0 = 0$, giving $K = b(0)$. \item \emph{Finite termination} ($a(k) = 0$ for some $k \ge 2$): $112{,}540$ families. \end{itemize} The two mechanisms account f
- **theorem** `thm:desert`  *[Desert dominance, $d=2$, $D=4$]*
  > \label{thm:desert} Among the $400{,}119$ non-$\Rat$ convergent families in $\FF(2,4)$, exactly $400{,}093$ are Desert ($\dps = 150$ classification, confirmed at $\dps = 300$ for $2000/2000$ random sample and $\dps = 500$ for $50/50$ sample). The Desert density among non-$\Rat$ convergent families is $400{,}093 / 400{,}119 \approx 99.99\%$.
- **theorem** `thm:trans`  *[Transcendence of $\Trans$-stratum limits]*
  > \label{thm:trans} All $24$ PCF limits are transcendental.
- **theorem** `thm:complete`  *[Completeness for $\FF(2,4)$]*
  > \label{thm:complete} The space $\FF(2,4)$ satisfies the Completeness Conjecture of~\cite{synthesis}, subject to the operational convergence criterion of Definition~\ref{def:conv}: \[ \FF(2,4)_{\mathrm{conv}} = \Rat \sqcup \Log \sqcup \Alg \sqcup \Trans \sqcup \Des, \] with the explicit partition \[ \Rat(113{,}270) \sqcup \Log(0) \sqcup \Alg(0) \sqcup \Trans(24) \sqcup \Des(400{,}093) = 513{,}387, 
- **proposition** `prop:mobius`  *[M\"obius identification]*
  > \label{prop:mobius} For all $24$ $\Trans$ families, the PCF limit~$K$ satisfies \eqref{eq:mobius} with the integer coefficients $(c_0, c_1, c_2, c_3)$ from the PSLQ output, to precision: \begin{equation}\label{eq:residual} \abs{K_{\mathrm{PCF}} - K_{\text{M\"obius}}} < 10^{-238} \end{equation} for all $24$ families (minimum residual $10^{-349}$, maximum $10^{-238}$, computed at $\dps = 300$).
- **proposition** `prop:deg21`  *[Degree-$(2,1)$ signature]*
  > \label{prop:deg21} All $24$ $\Trans$ families have $a(n)$ quadratic and $b(n)$ linear: $a_2 \ne 0$, $b_2 = 0$. This degree-$(2,1)$ profile occurs in $100\%$ of $\Trans$ families versus ${\sim}8\%$ of Desert and ${\sim}10\%$ of $\Rat$ families.
- **proposition** `prop:ratio`  *[Shared coefficient ratio]*
  > \label{prop:ratio} All three representative $\Trans$ families examined have $a_2/b_1^2 = -2/9$ (up to sign).
- **corollary** `cor:ratdens`  *[Rational density]*
  > \label{cor:ratdens} $P(K \in \Rat \mid K \in \FF(2,4)) = 113{,}270 / 531{,}441 \approx 21.3\%$.
- **definition** `def:strata`  *[Strata]*
  > \label{def:strata} For $K \in \FF(2,4)$ convergent with limit~$L$: \begin{itemize}[leftmargin=1.5em] \item $K \in \Rat$ if $L \in \mathbb{Q}$. Characterized by $a(1) = 0$ or $\exists\, k \ge 2$ with $a(k) = 0$ (Theorem~3.1 of~\cite{contamination}). \item $K \in \Log$ if $L \notin \mathbb{Q}$ but PSLQ finds an integer relation against $\{1, L, \ln p, L\ln p\}$ for some prime~$p$, or $\{1, L, G, LG\
- **definition** `def:conv`  *[Convergence criterion]*
  > \label{def:conv} $K$ is declared convergent if $\abs{K_N - K_{N-1}} < 10^{-10}$ at $N = 500$ partial quotients, computed at $\dps = 15$. This criterion is heuristic: it identifies convergence operationally for the purposes of classification, but does not rule out false positives (spurious convergence) or false negatives (slowly converging families below the threshold); see Remark~\ref{rem:prescree
- **problem** `prob:d3`
  > \label{prob:d3} \textbf{$\FF(1)$ for $d=3$, $D=4$.} The Completeness Conjecture remains open for $d \ge 3$. The complete enumeration of $\FF(3,4)$ involves $9^6 = 531{,}441$ families with degree-$3$ polynomials; the $\Trans$-stratum density and structure may differ substantially.
- **problem** `prob:deg21open`
  > \label{prob:deg21open} \textbf{Explanation of the degree-$(2,1)$ $\Trans$ signature.} Why are all $24$ $\Trans$ families degree-$(2,1)$ ($b_2 = 0$)? Is there a structural theorem characterizing which degree profiles admit $\Trans$-stratum families at $D = 4$? The coefficient ratio $a_2/b_1^2 = -2/9$ shared across multiple families suggests a deeper arithmetic constraint.
- **problem** `prob:hyp`
  > \label{prob:hyp} \textbf{Hypergeometric interpretation of $\Trans$ families.} The degree-$(2,1)$ profile and Ap\'ery-like recurrence structure suggest these PCFs may be expressible via ${}_3F_2$ or Appell hypergeometric functions. A positive result would place them in a known special function family and give a structural proof of the M\"obius-of-$\pi$ identification, independent of PSLQ.
- **problem** `prob:density`
  > \label{prob:density} \textbf{$\Trans$-stratum density as $D \to \infty$.} At $D = 4$ the $\Trans$ density is $24/513{,}387 \approx 4.7 \times 10^{-5}$. What is the asymptotic $\Trans$ density as $D \to \infty$ with $d = 2$ fixed? Does it grow (more transcendental identities found at larger coefficient bounds) or shrink (relative to the growing Desert)?
- **problem** `prob:logalg`
  > \label{prob:logalg} \textbf{$\Log$ and $\Alg$ at $d = 2$.} The $\Log$ and $\Alg$ strata are empirically empty at $D = 4$. The smallest~$D$ at which a $\Log$ family exists in $\FF(2,D)$ is unknown; the known degree-$2$ $\Log$ examples (classical Catalan CF) use non-polynomial structure outside $\FF(d,D)$. What is the smallest~$D$ such that $\FF(2,D)$ contains a $\Log$ or $\Alg$ family?
