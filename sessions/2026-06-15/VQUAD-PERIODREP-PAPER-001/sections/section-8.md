\appendix
\section{Explicit operators, Kovacic certificate, logs, conventions, reproducibility}\label{app:all}

\subsection{Full coefficient listings}\label{app:coeffs}
The operator $\Lphi=q_2D^2+q_1D+q_0$ is given in full in Theorem~\ref{thm:Lphi}. Here we record
the Borel-dual operator $\LV=\sum_{k=0}^4 p_k(\xi)D^k$, normalised by $p_0\equiv1$, with
coefficients in $\Qsqrt$ (denominators $431$ and $418501=431\times971$):
\begin{align*}
  p_0&=1,\\
  p_1&=\frac{659+150\sqrt3}{431}+\frac{432+12\sqrt3}{431}\,\xi,\\
  p_2&=\frac{2552175+199224\sqrt3}{418501}
       +\frac{496044+61620\sqrt3}{418501}\,\xi
       +\frac{70092+3240\sqrt3}{418501}\,\xi^2,\\
  p_3&=\frac{77760+560736\sqrt3}{418501}
       +\frac{1685448+101124\sqrt3}{418501}\,\xi
       +\frac{70092+3240\sqrt3}{418501}\,\xi^2,\\
  p_4&=\frac{19440+140184\sqrt3}{418501}\,\xi
       +\frac{210276+9720\sqrt3}{418501}\,\xi^2
       =\frac{210276+9720\sqrt3}{418501}\,\xi\Bigl(\xi+\tfrac{2}{\sqrt3}\Bigr).
\end{align*}
The residual $\LV\Bhat$ vanishes identically in $\Qsqrt$ through order $\xi^{129}$
(\texttt{stage0\_residual\_check.py}, method~A: \texttt{sympy} exact over $\Qsqrt$; method~B:
\texttt{mpmath} at $160$ digits, cross-checked). Source: \texttt{PERIOD-REP-VQUAD-002},
\texttt{operator-verification.md} \S4.0.

\subsection{Kovacic certificate for \texorpdfstring{$\Lphi$}{Lphi}}\label{app:kovacic}
Reducing $\Lphi$ to $u''=r\,u$ via $y=u\exp(-\tfrac12\int q_1/q_2)$ gives~\eqref{eq:r},
\[
  r(z)=\frac{11z^4+4z^2+4z+12}{4z^4(z^2+z+3)^2},
\]
with pole orders $\{0:4,\ \rho_\pm:2\}$, $\rho_\pm=\tfrac{-1\pm i\sqrt{11}}2$, $o(\infty)=4$, and
leading Laurent coefficient $\tfrac13 z^{-4}$ at $0$. Kovacic case elimination
(\texttt{stage2\_kovacic.py}, \texttt{stage2b\_symsquare.py}):
\begin{itemize}[leftmargin=1.4em,itemsep=1pt]
  \item \emph{Case 3} (finite groups): requires every pole order $\le2$; the order-$4$ pole at
        $z=0$ excludes it.
  \item \emph{Case 1} (reducible): requires a rational solution of $v'=r-v^2$; the rational
        Riccati solver returns the empty set.
  \item \emph{Case 2} (imprimitive): with Case~1 excluded, requires a rational solution of the
        symmetric square $\Lphi^{\odot2}=D^3-4rD-2r'$; the ansatz $f=N(z)/(z^8(z^2+z+3)^4)$,
        $\deg N\le18$, yields a homogeneous $38$-unknown $\mathbb{Q}$-linear system with only the
        trivial solution.
  \item \emph{Case 4}: by elimination, $G=\SL_2(\mathbb{C})$.
\end{itemize}
Independent structural confirmation: the reduced equation has no first-order term, so
$G\subseteq\SL_2$; the two distinct exponentials $\exp(\pm(1/\sqrt3)/z)$ at $z=0$ generate the
diagonal torus, and the nonzero Stokes constant $S=2\pi K$ supplies an off-torus unipotent;
torus-plus-unipotent generate $\SL_2$. Source: \texttt{PERIOD-REP-VQUAD-003},
\texttt{kovacic-verification.md}.

\subsection{Numerical logs}\label{app:numlogs}
All constants to the stated precision (\texttt{PERIOD-REP-VQUAD-001},
\texttt{numerical-check.md}; \texttt{mpmath}):
\[
\begin{array}{ll}
  K=0.0728781025518669641294423633296525128045556892\ldots & (58\ \text{digits}),\\
  S=2\pi K=0.457906623169017636119097842548225837962395135\ldots,\\
  \beta=-1/(3\sqrt3)=-0.19245008972987525\ldots, & \xizero=2/\sqrt3=1.1547005383792517\ldots,\\
  \C=\lvert\Gamma(\beta)\rvert K=0.437705286193537221230739749794369589981725597\ldots.
\end{array}
\]
Method agreement (\texttt{stage4\_methods.py}, \texttt{stage1\_hankel\_period.py} at dps
$160$--$260$): leading thimble period $=S\,e^{-\xizero}$ to relative error $8.84\times10^{-46}$
(Method~B); $\lvert S_{\mathrm{mult}}\rvert=2\pi K$ to $8.84\times10^{-46}$ and
$\C=\lvert\Gamma(\beta)\rvert K$ to $9.31\times10^{-46}$ (Method~C). Frobenius solution at
$-\xizero$: exponents $\{-(1+\beta),0,1,2\}$, no logarithmic terms, recurrence residual
$1.6\times10^{-46}$ (\texttt{stage3b\_frobenius\_v2.py}).

\subsection{The four sign conventions for Method A}\label{app:conventions}
Method~A (\S\ref{sub:methodA}) hinges on the Borel--Laplace intertwiner~\eqref{eq:duality}. Because
both the kernel exponent and the $\xi$-multiplication carry a sign, there are four a~priori
conventions; we tested all four (\texttt{stage4a\_methodA\_v2.py}) and only one produces a
proportional operator $M=h(z)\Lphi$:
\begin{center}
\begin{tabular}{@{}cccl@{}}
\hline
$D_\xi\mapsto$ & $\xi\mapsto$ & kernel & result \\
\hline
$+1/z$ & $+z^2D_z$ & $e^{-\xi/z}$ (Borel sum) & $M=h(z)\Lphi$, $h=\dfrac{27(649+30\sqrt3)}{418501\,z^2(2\sqrt3-3)}$ \\
$+1/z$ & $-z^2D_z$ & --- & three coefficient ratios disagree \\
$-1/z$ & $+z^2D_z$ & --- & three coefficient ratios disagree \\
$-1/z$ & $-z^2D_z$ & $e^{+\xi/z}$ & three coefficient ratios disagree \\
\hline
\end{tabular}
\end{center}
Only the kernel forced by the normalisation $b_m=a_{m+1}/m!$ (top row) works. This is the
anti-fluke test: a spurious operator proportionality would not have singled out the correct
analytic convention. We record it here because every reader reconstructing Method~A will face the
same sign choice. Source: \texttt{PERIOD-REP-VQUAD-003}, \texttt{method-A-verification.md}.

\subsection{Reproducibility statement and code availability}\label{app:repro}
Every computational claim of this paper is reproducible from the scripts in the probe slots
\texttt{PERIOD-REP-VQUAD-001/002/003} (SIARC relay bridge). The differential-algebra is exact over
$\Qsqrt$ (\texttt{sympy} $1.14.0$); the asymptotic/period numerics use \texttt{mpmath} $1.3.0$ at
$160$--$260$ decimal digits; Python $3.12.10$. The parent V\_quad deposit is Zenodo
\texttt{10.5281/zenodo.20455090} (concept \texttt{10.5281/zenodo.20455089})~\cite{Vquad}, with the
$S=2\pi K$ calibration in \texttt{10.5281/zenodo.20481592}~\cite{StokesNote}. Key scripts:
\texttt{stage0\_residual\_check.py} (operator residuals), \texttt{stage2\_kovacic.py} and
\texttt{stage2b\_symsquare.py} (Galois), \texttt{stage3b\_frobenius\_v2.py} (branch exponent),
\texttt{stage4a\_methodA\_v2.py} (Method~A and the four-convention test),
\texttt{stage4\_methods.py} (Methods~B, C), \texttt{stage1\_hankel\_period.py} (Hankel period).
The LaTeX source compiles with \texttt{pdflatex} (MiKTeX $25.12$) under a fixed
\texttt{SOURCE\_DATE\_EPOCH} for byte-reproducible output. No proprietary software is required;
the Kovacic verdict, optionally cross-checkable in Maple's
\texttt{DEtools[DifferentialGaloisGroup]}, is here obtained by open case-elimination plus the
structural argument of Appendix~\ref{app:kovacic}.
