# CT-S7-COLDREAD Cold Mathematical Review

Repository HEAD at start: `08aa0e2381b3dc37ee54a3200b7272755ca11d59` [INSPECTED].
Repository HEAD at end-of-review capture: `08aa0e2381b3dc37ee54a3200b7272755ca11d59` [INSPECTED].
Scope obeyed: I read only `sessions\2026-09-17\CT-S1-THEOREM\theorem.tex` inside the repository, plus DLMF pages named below [INSPECTED]. I did not read the forbidden audit/report paths [INSPECTED].

## What I did

- Wrote `PREREG.md` before running computation [INSPECTED].
- Extracted the target theorem passages with line numbers into `theorem_excerpts.out` using `extract_theorem_excerpts.py` [INSPECTED].
- Ran exact symbolic expansion in SymPy with `check_symbolic.py`; output hash `469094587c5b3c951723325278f154ced28753799c6b3ccb8728e74f19156c46` [PROVEN].
- Ran exact-integer small-range multinomial checks with `check_multinomial.py`; output hash `2f62ea57731b0195e5d564558df662a00f9e77e19f49570ef040fbaaa56ad3fe` [PROVEN].
- Fetched DLMF TeX endpoints with `fetch_dlmf.py`; output hash `cb5237240aa7eea3f68608a9803ef2798db5585ed21eac905e0fe18d088d08f5` [INSPECTED].

## Passage 1: Theorem `thm:radius`, Step 3

### Quoted text judged

```tex
\textbf{Step 3 ($(n!)^d$ against $(dn)!$).}
We claim
\begin{equation}\label{eq:multinomial}
\lim_{n\to\infty}\left(\frac{(dn)!}{(n!)^{d}}\right)^{1/n}=d^{\,d}.
\end{equation}
Write $C(k_1,\dots,k_d):=\binom{dn}{k_1,\dots,k_d}=(dn)!/(k_1!\cdots k_d!)$ for
a composition $k_1+\cdots+k_d=dn$ into non-negative parts.

\emph{Sub-lemma (the balanced composition is maximal).} $C$ attains its maximum
over all such compositions at $k_1=\cdots=k_d=n$. Indeed, suppose
$k_i\ge k_j+2$ for some $i\neq j$. Replacing $(k_i,k_j)$ by $(k_i-1,k_j+1)$
leaves the total $dn$ unchanged and multiplies $C$ by
\[
\frac{k_i!\,k_j!}{(k_i-1)!\,(k_j+1)!}=\frac{k_i}{k_j+1}\ \ge\ \frac{k_j+2}{k_j+1}>1 ,
\]
so $C$ strictly increases. As the set of compositions is finite, any maximiser
must therefore satisfy $|k_i-k_j|\le1$ for all $i,j$; together with
$\sum_ik_i=dn$ this forces $k_1=\cdots=k_d=n$. Hence
$(dn)!/(n!)^d=\max C$. \hfill$\square$

Now $(dn)!/(n!)^d$ is one term of the multinomial expansion
$\sum_{k_1+\cdots+k_d=dn}C(k_1,\dots,k_d)=(\underbrace{1+\cdots+1}_{d})^{dn}=d^{\,dn}$,
which gives the upper bound; and being the \emph{maximum} it is at least the
average, i.e.\ $d^{\,dn}$ divided by the number $N_{d,n}$ of compositions. Each
composition is determined by $(k_1,\dots,k_{d-1})\in\{0,1,\dots,dn\}^{d-1}$
(the last part being forced), so $N_{d,n}\le(dn+1)^{d-1}$. Therefore
\[
\frac{d^{\,dn}}{(dn+1)^{d-1}}\ \le\ \frac{(dn)!}{(n!)^d}\ \le\ d^{\,dn}.
\]
Taking $n$-th roots and using $(dn+1)^{(d-1)/n}\to1$ gives
\eqref{eq:multinomial}. \textsc{complete.}
```

### Line-by-line judgement

- The exchange ratio is correct: changing `(k_i,k_j)` to `(k_i-1,k_j+1)` multiplies the coefficient by `k_i/(k_j+1)` [PROVEN].
- If a maximizer had `k_i >= k_j+2`, the exchange would strictly increase the coefficient, contradiction; hence every maximizer has pairwise differences at most 1 [PROVEN].
- Since the sum is exactly `dn`, pairwise differences at most 1 force all parts to be exactly `n`: if parts were `n` and `n+1`/`n-1`, the integer average would still be `n`, but pairwise spread at most 1 permits mixed `n`/`n+1` only with average above `n` or mixed `n-1`/`n` only with average below `n`; mixed `n-1`/`n+1` would violate spread [PROVEN].
- The maximality claim is load-bearing for the lower bound exactly as the prompt suspected: the proof uses balanced coefficient = maximum, then maximum >= average [PROVEN]. It is not merely asserted; it is proved [INSPECTED].
- Number-of-compositions bound `N_{d,n} <= (dn+1)^{d-1}` is correct because the first `d-1` parts lie in `{0,...,dn}` and determine the last part, with overcount allowed only in the bounding box [PROVEN].
- Upper bound direction is correct because the balanced term is one nonnegative term in the multinomial sum [PROVEN].
- Lower bound direction is correct because balanced term is the maximum and maximum is at least average [PROVEN].
- `d=1` is harmless: there is only one composition, `(n)`, and the displayed sandwich is `1 <= 1 <= 1` [PROVEN].

### Computation

`check_multinomial.out` reports:

```text
checked_sandwich_d=1..8_n=1..12_exact_integer
sandwich_failures= []
checked_maximality_by_enumeration_for_d<=5_total<=30
maximality_failures= []
edge_d1_examples= [(1, 1, 1), (2, 1, 1), (3, 1, 1), (4, 1, 1), (5, 1, 1)]
```

### Verdict: **SOUND**

I could reconstruct every step of Theorem `thm:radius`, Step 3 [STRUCTURAL]. The former load-bearing point is now proved in the text [INSPECTED].

## Passage 2: Theorem `thm:growth`, Step 3 / G1

### Quoted text judged

```tex
\textbf{Step 3 (Gamma-ratio asymptotics).}
For fixed $r\in\C$,
\begin{equation}\label{eq:gammaratio}
\frac{\Gamma(n+1-r)}{\Gamma(n+1)}=n^{-r}\bigl(1+O(1/n)\bigr).
\end{equation}

\emph{Proof of \eqref{eq:gammaratio}.} Put
$h(n):=\Gamma(n+1-r)\,n^{r}/\Gamma(n+1)$ for $n>\max(0,\Re r)$, so that
\eqref{eq:gammaratio} is the assertion $h(n)=1+O(1/n)$. Using
$\Gamma(x+1)=x\Gamma(x)$ twice,
\begin{equation}\label{eq:hratio}
\frac{h(n)}{h(n-1)}
=\frac{\Gamma(n+1-r)}{\Gamma(n-r)}\cdot\frac{\Gamma(n)}{\Gamma(n+1)}
\cdot\Bigl(\frac{n}{n-1}\Bigr)^{r}
=\Bigl(1-\frac{r}{n}\Bigr)\Bigl(1-\frac1n\Bigr)^{-r} .
\end{equation}
Expanding, $(1-1/n)^{-r}=1+r/n+O(1/n^{2})$, so the right-hand side of
\eqref{eq:hratio} equals $(1-r/n)(1+r/n+O(1/n^2))=1+O(1/n^{2})$. Since
$\sum_n O(1/n^2)<\infty$, the telescoping product
$h(n)=h(n_0)\prod_{m=n_0+1}^{n}h(m)/h(m-1)$ converges to a finite nonzero limit
$h_\infty$, and because the tail of a convergent $\sum O(1/m^{2})$ is $O(1/n)$,
\begin{equation}\label{eq:hlimit}
h(n)=h_\infty\bigl(1+O(1/n)\bigr).
\end{equation}
It remains to identify $h_\infty=1$. This is the classical Gamma-ratio
normalisation: DLMF~(5.11.12) states
$\Gamma(z+a)/\Gamma(z+b)\sim z^{a-b}\sum_{k\ge0}G_k(a,b)z^{-k}$ as
$|z|\to\infty$ with $|\operatorname{ph}z|\le\pi-\delta$, where $G_0(a,b)=1$
\cite[\S5.11(iii)]{DLMF}. Taking $a=1-r$, $b=1$, $z=n$ gives
$\Gamma(n+1-r)/\Gamma(n+1)\sim n^{-r}$, i.e.\ $h_\infty=1$. Substituting into
\eqref{eq:hlimit} yields \eqref{eq:gammaratio}. \hfill$\square$
```

### Algebraic expansion

SymPy output:

```text
coeff_x1= 0
coeff_x2= r*(1 - r)/2
coeff_x3= r*(1 - r**2)/3
log_coeff_x1= 0
log_coeff_x2= r*(1 - r)/2
conclusion=1/n coefficient cancels identically; ratio is 1 + r*(1-r)/(2*n^2) + O(n^-3) for fixed r
```

Thus the claimed cancellation of the `1/n` terms is correct [PROVEN].

### Product-tail error

The text's `1+O(1/n)` conclusion is justified [PROVEN], not merely `o(1)`: for fixed `r`, write `h(m)/h(m-1)=1+a_m` with `a_m=O(m^-2)`. For large `m`, `|a_m|<1/2`, so `log(1+a_m)=O(a_m)`. Therefore the tail logarithm is `O(sum_{m>n} m^-2)=O(1/n)`, and exponentiating gives the relative tail `1+O(1/n)` [PROVEN].

### DLMF verification

Fetched URLs and output:

```text
URL: https://dlmf.nist.gov/5.11.E12.tex
\[\frac{\Gamma\left(z+a\right)}{\Gamma\left(z+b\right)}\sim z^{a-b},\]

URL: https://dlmf.nist.gov/5.11.E13.tex
\[\frac{\Gamma\left(z+a\right)}{\Gamma\left(z+b\right)}\sim z^{a-b}\sum_{k=0}^{%
\infty}\frac{G_{k}(a,b)}{z^{k}},\]
```

This verifies that DLMF equation `5.11.12` itself supplies the needed normalization `h_inf=1` when `z=n`, `a=1-r`, `b=1` [INSPECTED]. However, the theorem text is not accurate when it says that DLMF `(5.11.12)` is the full `sum_{k>=0} G_k(a,b) z^{-k}` expansion with `G_0(a,b)=1`; the fetched full-sum formula is `5.11.13`, not `5.11.12` [INSPECTED].

### Uniformity, complex `r`, and circularity

- The theorem applies to the finitely many fixed roots `r_i`; no uniform statement over a moving `r`-family is required [STRUCTURAL].
- Complex `r` is not a problem for the ratio proof: `n^r` is evaluated on positive real `n`, and DLMF's sector condition holds for `z=n` [STRUCTURAL].
- Large `Re(r)` only changes the threshold `n_0`; for fixed `r`, it does not break the argument [STRUCTURAL].
- (A2) is sufficient for the theorem's exact product formula because it excludes positive-integer roots, equivalently poles of `Gamma(1-r_i)` [INSPECTED].
- There is no internal circularity in the ratio-product part; it proves existence of `h_inf` and the `O(1/n)` tail. The constant is imported from DLMF [STRUCTURAL]. If the author wants to avoid any external gamma-ratio asymptotic at all, then a separate proof of `h_inf=1` is still needed [STRUCTURAL].

### Verdict: **ERROR**

The mathematical asymptotic conclusion is repairable and the needed constant is in DLMF `5.11.12`, but the passage as written contains an external-reference error [INSPECTED]: it quotes `DLMF~(5.11.12)` as the full `G_k` expansion, while the fetched equation `5.11.12` is only `Gamma(z+a)/Gamma(z+b) ~ z^{a-b}` and the full expansion is at `5.11.13` [INSPECTED]. Correcting this citation/wording would make the Step 3 argument sound [STRUCTURAL].

## Claims

See `claims.jsonl`. Summary:

1. HEAD start verified [INSPECTED].
14. HEAD end-of-review capture verified [INSPECTED].
2. Radius Step 3 exchange proof is present [INSPECTED].
3. Exchange proof proves balanced maximality [PROVEN].
4. Balanced maximality is load-bearing for the lower bound [PROVEN].
5. Finite exact-integer sandwich/max checks had no failures [PROVEN].
6. `d=1` edge case is correct [PROVEN].
7. Gamma-ratio `1/n` cancellation is exact [PROVEN].
8. Product convergence gives `1+O(1/n)` [PROVEN].
9. DLMF `5.11.12` supplies `h_inf=1` [INSPECTED].
10. The text's full-expansion attribution to `5.11.12` is wrong; fetched full expansion is `5.11.13` [INSPECTED].
11. Fixed-complex-root hypotheses suffice; no uniformity in varying `r` is needed [STRUCTURAL].
12. Radius Step 3 verdict is SOUND [STRUCTURAL].
13. Growth Step 3 verdict is ERROR due citation/wording mismatch [INSPECTED].

## What I could NOT establish

- NOT FOUND in fetched `https://dlmf.nist.gov/5.11.E12.tex` by direct URL fetch: the displayed full `sum_{k>=0}G_k(a,b)z^{-k}` expansion or `G_0(a,b)=1` wording [INSPECTED].
- I did not inspect forbidden audit/report files, so I make no claim about derivation history or prior audit contents [INSPECTED].

## Open questions for the operator

- Should the theorem cite DLMF `5.11.12` in its simpler form, or cite DLMF `5.11.13` for the full expansion and separately document `G_0(a,b)=1`? [CONJECTURED]

## Overall recommendation

Not yet fit to carry a deposit `PROVEN` label as written [STRUCTURAL]. Required fix: in Theorem `thm:growth`, Step 3 and the bibliography, correct the DLMF equation attribution/wording. The proof may either cite DLMF `5.11.12` as the simple ratio asymptotic `Gamma(z+a)/Gamma(z+b) ~ z^{a-b}` or cite `5.11.13` for the full expansion with whatever DLMF page/equation explicitly defines `G_0(a,b)=1` [STRUCTURAL]. I found no mathematical defect in Theorem `thm:radius`, Step 3 [STRUCTURAL].

## Uncommitted files I created

- `sessions\2026-09-17\CT-S7-COLDREAD\head_start.out`
- `sessions\2026-09-17\CT-S7-COLDREAD\head_end.out`
- `sessions\2026-09-17\CT-S7-COLDREAD\PREREG.md`
- `sessions\2026-09-17\CT-S7-COLDREAD\check_symbolic.py`
- `sessions\2026-09-17\CT-S7-COLDREAD\check_symbolic.out`
- `sessions\2026-09-17\CT-S7-COLDREAD\check_multinomial.py`
- `sessions\2026-09-17\CT-S7-COLDREAD\check_multinomial.out`
- `sessions\2026-09-17\CT-S7-COLDREAD\fetch_dlmf.py`
- `sessions\2026-09-17\CT-S7-COLDREAD\fetch_dlmf.out`
- `sessions\2026-09-17\CT-S7-COLDREAD\extract_theorem_excerpts.py`
- `sessions\2026-09-17\CT-S7-COLDREAD\theorem_excerpts.out`
- `sessions\2026-09-17\CT-S7-COLDREAD\claims.jsonl`
- `sessions\2026-09-17\CT-S7-COLDREAD\REPORT.md`
