\section{The differential operators \texorpdfstring{$\Lphi$}{Lphi} and \texorpdfstring{$\LV$}{LV}}\label{sec:operators}

Throughout, $D=d/dz$ on the $\varphi$-side and $D=d/d\xi$ on the Borel side; the base field is
the real quadratic number field $\Qsqrt$. Every coefficient below is exact in $\Qsqrt$, obtained
by linear algebra over $\Qsqrt$ (Fraction pairs $p+q\sqrt3$), \emph{not} by numerical
integer-relation search; the annihilation residuals are identically zero in $\Qsqrt$, not merely
small. Full coefficient listings and the verification protocol are in
Appendix~\ref{app:coeffs}.

The exactness is concrete already at the level of the coefficient stream. Seeding the V\_quad
Riccati recursion with $\sigma=-1/\sqrt3$ (so $\sigma^2=\tfrac13\in\mathbb{Q}$,
$1/\sigma=-\sqrt3$) produces every $a_n$ as an exact element $p+q\sqrt3$ of $\Qsqrt$; the first
few, and the corresponding Borel coefficients $b_m=a_{m+1}/m!$, are
(script \texttt{holonomic\_recognition\_q3.py}, \texttt{PERIOD-REP-VQUAD-002}):
\begin{equation}\label{eq:coeffstream}
\renewcommand{\arraystretch}{1.25}
\begin{array}{r|l|l}
 n & a_n\in\Qsqrt & \text{(decimal)}\\\hline
 0 & 1 & 1.0000000000\\
 1 & -\tfrac{1}{12}-\tfrac{1}{24}\sqrt3 & -0.1555021170\\
 2 & -\tfrac{73}{1152}-\tfrac{17}{648}\sqrt3 & -0.1088076601\\
 3 & \tfrac{6589}{41472}-\tfrac{13415}{746496}\sqrt3 & \phantom{-}0.1277522430\\
 4 & \tfrac{9247897}{71663616}-\tfrac{846407}{4478976}\sqrt3 & -0.1982654887
\end{array}
\end{equation}
with e.g.\ $b_0=a_1$, $b_1=a_2$, $b_2=\tfrac{6589}{82944}-\tfrac{13415}{1492992}\sqrt3=
0.0638761215\ldots$. The exactness of these rationals is what licenses the word ``provably'' in
all field claims below: no step uses a numerical approximation of $\sqrt3$.

\subsection{The operator \texorpdfstring{$\Lphi$}{Lphi}}
\begin{theorem}[$\varphi$ is $D$-finite over $\Qsqrt$]\label{thm:Lphi}
The series $\varphi(z)=\sum_{n\ge0}a_nz^n$ of~\eqref{eq:phi-series} is annihilated by a unique
minimal operator
\[
  \Lphi \;=\; q_2(z)\,D^2 + q_1(z)\,D + q_0(z),\qquad q_i\in\Qsqrt[z],
\]
of order $2$ and degree $4$, with
\begin{align*}
  q_0(z)&=1+\Bigl(\tfrac{23}{9}+\tfrac{14}{27}\sqrt3\Bigr)z
              +\Bigl(-\tfrac{253}{9}+\tfrac{488}{27}\sqrt3\Bigr)z^2,\\
  q_1(z)&=(48-24\sqrt3)+(-64+44\sqrt3)z+\Bigl(-\tfrac{68}{3}+\tfrac{52}{3}\sqrt3\Bigr)z^2
              +\Bigl(-\tfrac{152}{3}+\tfrac{100}{3}\sqrt3\Bigr)z^3,\\
  q_2(z)&=(-36+24\sqrt3)z^2+(-12+8\sqrt3)z^3+(-12+8\sqrt3)z^4
           \;=\;4(2\sqrt3-3)\,z^2\,(z^2+z+3).
\end{align*}
The annihilation $\Lphi\varphi=0$ holds exactly in $\Qsqrt$ for every power $z^0,\dots,z^{139}$
tested; the minimal $(\text{order},\text{degree})$ has nullity $1$, and the higher nullities
$\{1,3,5,7\}$ (order $2$) and $\{2,6,10,14\}$ (order $3$) match the left-multiple count
$d-4+1$ of a single minimal order-$2$ operator, so there are no spurious solutions.
\end{theorem}

The coefficient field is \emph{exactly} $\Qsqrt$: all computations close over $\Qsqrt$, and both
$q_1,q_0$ carry genuine $\sqrt3$ parts, so the field is neither smaller (not $\mathbb{Q}$) nor
larger. Operationally $\Lphi$ is the scalar (Schr\"odinger) reduction of the V\_quad Painlev\'e-V
linear problem, recovered from the Riccati linearisation $c=\psi'/\psi$; the parent corpus
records the existence of this linear problem only verbally~\cite{Vquad}, and Theorem~\ref{thm:Lphi}
makes it explicit.

\begin{remark}[Provenance of $\Lphi$]\label{rmk:provenance}
We stress that $\Lphi$ is obtained by holonomic recognition from the coefficient stream
$(a_n)$---guessing an annihilating operator and then certifying $\Lphi\varphi=0$ exactly over
$\Qsqrt$---and \emph{not} from an a~priori Lax pair. The literature provides no explicit classical
Lax pair for the $\Vquad$ transcendent (a dedicated search returned none;
\texttt{PERIOD-REP-VQUAD-002}, \texttt{lax-pair-found.md}), so the holonomic route is the available
one and is in fact stronger here: it yields the minimal operator with a verifiable exact
certificate rather than a gauge-dependent matrix. For context, although no classical Lax pair for
$\Vquad$ appears in the literature, isomonodromic Lax systems and their Stokes data for
Painlev\'e equations can be constructed from spectral curves by topological recursion and
isomonodromic Hamiltonian methods~\cite{MarchalOrantin,IwakiMarchalSaenz,MarchalAlameddine}; the
holonomic route taken here is independent of that construction (Section~\ref{sec:disc}). The two
exponential parts
$\exp(\pm(1/\sqrt3)/z)$ at $z=0$ found below are consistent with the V\_quad WKB/Riccati seed
$\sigma=-1/\sqrt3$ ($\sigma^2=1/3\in\mathbb{Q}$) and with the formal monodromy exponent
$\theta_\infty=2/\sqrt3$ of~\cite{Vquad}.
\end{remark}

\subsection{Singular structure of \texorpdfstring{$\Lphi$}{Lphi} and its Galois group}
Reducing $\Lphi$ to normal form $u''=r\,u$ via $y=u\exp(-\tfrac12\int q_1/q_2)$ gives, with
$a=q_1/q_2$, $b=q_0/q_2$ and $r=\tfrac14a^2+\tfrac12a'-b$,
\begin{equation}\label{eq:r}
  r(z)\;=\;\frac{11z^4+4z^2+4z+12}{\,4\,z^4\,(z^2+z+3)^2\,}.
\end{equation}
The poles of $r$ are $z=0$ (order $4$), the two roots $z=\tfrac{-1\pm i\sqrt{11}}2$ of $z^2+z+3$
(order $2$ each), and $o(\infty)=4$; the leading Laurent coefficient at $z=0$ is
$r\sim\tfrac13 z^{-4}$. Thus $z=0$ is an irregular singular point of Poincar\'e rank $1$ with two
distinct exponential parts $\exp(\pm(1/\sqrt3)/z)$; the two finite poles $\rho_\pm$ are
regular-singular for the reduced equation, and the point at infinity is regular-singular with
exponent difference fixed by $o(\infty)=4$. Only the irregular point $z=0$ carries the Stokes
phenomenon, and it is there that the connection coefficient lives. Table~\ref{tab:config}
summarises the singular configuration of $\Lphi$ alongside its Borel dual $\LV$.

\begin{table}[h]
\centering
\begin{tabular}{@{}lll@{}}
\toprule
 & $\Lphi$ (order $2$, on $z$) & $\LV$ (order $4$, on $\xi$) \\
\midrule
order / degree & $2$ / $4$ & $4$ / $2$ \\
base field & $\Qsqrt$ & $\Qsqrt$ \\
finite singularities & $\rho_\pm=\tfrac{-1\pm i\sqrt{11}}2$ (reg.) & $0$ (apparent), $-\xizero$ (branch) \\
irregular point & $z=0$, Poincar\'e rank $1$ & $\xi=\infty$, slope $1$ \\
Stokes datum & $S=2\pi K$ at $z=0$ & branch amplitude $A$ at $-\xizero$ \\
Galois group & $\SL_2(\mathbb{C})$ (Thm.~\ref{thm:galois}) & $G_V\supseteq\Gm\times(\SL_2\text{-dual})$ \\
\bottomrule
\end{tabular}
\caption{Singular configuration of the $\varphi$-side operator $\Lphi$ and its Borel dual $\LV$.
The irregular point of $\Lphi$ (at $z=0$) and the branch of $\LV$ (at $-\xizero$) are the two
faces of the same connection datum under Borel--Laplace duality. Source:
\texttt{PERIOD-REP-VQUAD-002}, \texttt{operator-verification.md} \S4.}
\label{tab:config}
\end{table}

\begin{proof}[Proof of Theorem~\ref{thm:galois}]
We give both arguments.

\emph{(1) Kovacic case-elimination.} In the Kovacic case/group
dictionary~\cite{Kovacic,vdPS} for $u''=ru$: Case~3 (finite groups $A_4,S_4,A_5$) requires every
pole order $\le2$; the pole of order $4$ at $z=0$ excludes it. Case~1 (reducible, $G\subseteq$
Borel) holds iff the Riccati equation $v'=r-v^2$ has a rational solution; a complete rational
Riccati solver returns none. Case~2 (imprimitive, $G\subseteq N(T)$) holds, given Case~1
excluded, iff the symmetric square $\Lphi^{\odot2}=D^3-4rD-2r'$ has a rational solution; the
ansatz $f=N(z)/\bigl(z^8(z^2+z+3)^4\bigr)$, $\deg N\le18$, yields a homogeneous linear system in
$38$ rational unknowns whose only solution is trivial. With Cases~1,2,3 excluded, the algorithm
returns Case~4: $G=\SL_2(\mathbb{C})$.

\emph{(2) Structural argument.} The reduced equation $u''=ru$ has no first-order term, so the
Wronskian is constant and $G\subseteq\SL_2$. At $z=0$ the two distinct exponentials
$\exp(\pm(1/\sqrt3)/z)$ generate the full diagonal torus $\mathbb{G}_m\subset\SL_2$ (the local
exponential torus). The nonvanishing Stokes constant $S=2\pi K\ne0$ at this irregular point is a
nonidentity unipotent off that torus. A maximal torus together with one off-torus unipotent
generate $\SL_2$, whence $G=\SL_2(\mathbb{C})$.
\end{proof}

The two routes are genuinely independent---an exhaustive negative search versus a positive
generation argument from the Stokes datum---and agree. (Only one symbolic engine was available;
the second route supplies the cross-check that a second computer-algebra system would otherwise
provide. See Appendix~\ref{app:kovacic}.)

\subsection{The Borel operator \texorpdfstring{$\LV$}{LV}}
We construct $\LV$ from $\Lphi$ by Borel--Laplace duality. The (formal) Borel transform of order
$1$ acts on the coefficient stream by $a_{m+1}\mapsto b_m=a_{m+1}/m!$; equivalently, on series, it
is the Hadamard-type rescaling that turns the Gevrey-$1$ divergent $\varphi$ into the convergent
germ $\Bhat$. On operators it intertwines the two differential structures by
\begin{equation}\label{eq:formalduality}
  z^2 D_z\ \longleftrightarrow\ \xi,\qquad \tfrac1z\ \longleftrightarrow\ D_\xi,
\end{equation}
the same intertwiner~\eqref{eq:duality} used analytically in Section~\ref{sec:verif}. Under it a
term $z^{a}D_z^{k}$ of $\Lphi$ maps to a term of $\xi$-degree bounded by the original
$z$-\emph{order} and of $\xi$-order bounded by the original $z$-\emph{degree}: order and degree are
exchanged. Hence the order-$2$, degree-$4$ operator $\Lphi$ produces an operator of order $4$ and
degree $2$ in $\xi$, and $D$-finiteness is preserved because~\eqref{eq:formalduality} is an
isomorphism of the Weyl algebra $\Qsqrt\langle\xi,D_\xi\rangle$. We verify the resulting operator
directly on the coefficient stream rather than relying on the formal map alone.

\begin{theorem}[$\Bhat$ is holonomic over $\Qsqrt$]\label{thm:LV}
The Borel transform $\Bhat(\xi)=\sum_{m\ge0}b_m\xi^m$, $b_m=a_{m+1}/m!$, is annihilated by a
unique minimal operator $\LV=\sum_{k=0}^4 p_k(\xi)D^k$ of order $4$ and degree $2$, normalised by
$p_0\equiv1$, with $p_1,\dots,p_4\in\Qsqrt[\xi]$ given explicitly in
Appendix~\ref{app:coeffs}. The residual $\LV\Bhat$ is identically zero in $\Qsqrt$ for every power
$\xi^0,\dots,\xi^{129}$ tested. The leading coefficient factors exactly as
\begin{equation}\label{eq:p4-factor}
  p_4(\xi)\;=\;\frac{210276+9720\sqrt3}{418501}\;\xi\,\Bigl(\xi+\frac{2}{\sqrt3}\Bigr),
  \qquad 418501=431\times971,
\end{equation}
so the singular locus of $\LV$ is $\{0,\,-\xizero=-2/\sqrt3,\,\infty\}$.
\end{theorem}

\begin{proposition}[Local exponents]\label{prop:exponents}
The local exponents of $\LV$ are
\[
  \{-1,0,1,2\}\ \text{at } \xi=0,\qquad
  \{\,-(1+\beta),\,0,1,2\,\}\ \text{at } \xi=-\xizero,\qquad
  \text{irregular of slope }1\ \text{at } \xi=\infty,
\]
with $-(1+\beta)=-1+\sqrt3/9=-0.80754991027\ldots$ the unique non-integer exponent. At $\xi=0$
the four exponents are consecutive integers, so the point is \emph{apparent} (single-valued, $\Bhat$
itself is the holomorphic exponent-$0$ solution). At $\xi=-\xizero$ the branch is carried by the
single irrational exponent $-(1+\beta)$, governing $\Bhat(\xi)\sim A\,(\xi+\xizero)^{-(1+\beta)}$
and hence the large-order law $a_n\sim \Gamma(n+\beta)/\xizero^{\,n+\beta}$ up to the amplitude
$A$. Both statements are obtained twice, by a falling-factorial indicial computation and by direct
solution of the Frobenius recurrence at $-\xizero$ (residuals $1.6\times10^{-46}$, no
logarithms); see Appendix~\ref{app:numlogs}.
\end{proposition}

\begin{remark}[From branch exponent to large-order law]\label{rmk:largeorder}
The single irrational exponent at $-\xizero$ controls the divergence of $\varphi$. Writing the
branch as $\Bhat(\xi)\sim A(\xi+\xizero)^{-(1+\beta)}$ and inverting the Borel transform
$b_m=a_{m+1}/m!$ term by term against $(\xi+\xizero)^{-(1+\beta)}=\xizero^{-(1+\beta)}\sum_m
\binom{-(1+\beta)}{m}(\xi/\xizero)^m$ gives, by Stirling,
\begin{equation}\label{eq:largeorder}
  a_n\;\sim\;\frac{S}{2\pi i}\,\frac{\Gamma(n+\beta)}{\xizero^{\,n+\beta}}\qquad(n\to\infty),
\end{equation}
the standard resurgence late-term law with action $\xizero=2/\sqrt3$ and characteristic exponent
$\beta=-1/(3\sqrt3)$. Thus the operator datum at $-\xizero$ (an algebraic exponent in $\Qsqrt$)
and the analytic datum $K$ governing $\lvert a_n\rvert$ are two readings of the same branch; the
amplitude $\lvert A\rvert=K\,\Gamma(1+\beta)$ relates them (Section~\ref{sec:verif}).
\end{remark}

\begin{remark}[Sign of the action]
The dominant Borel singularity lies on the \emph{negative} real axis at $-\xizero$. The modulus
$\xizero=2/\sqrt3$ was known to $95.6$ digits from $\lim_n\lvert a_n/a_{n+1}\rvert\,n$, but as a
modulus the sign was unpinned; the exact factorisation~\eqref{eq:p4-factor} fixes it, consistently
with $a_n\sim(-1)^{n+1}\lvert a_n\rvert$ for $n\ge3$, i.e. $b_m\sim(-1)^m(+)$. This places the cut
in the direction $\arg\xi=\pi$, which is exactly the rapid-decay direction for $f=-\xi$
(Section~\ref{sec:cycle}).
\end{remark}

\subsection{Finite resurgence}
\begin{proof}[Proof of Corollary~\ref{cor:finite}]
A holonomic function has finitely many singularities, located among the zeros of the leading
coefficient of its annihilator and the point at infinity. By Theorem~\ref{thm:LV} the leading
coefficient $p_4$ vanishes only at $0$ and $-\xizero$, so
$\operatorname{Sing}(\Bhat)\subseteq\{0,-\xizero,\infty\}$; the point $0$ is apparent
(Proposition~\ref{prop:exponents}), leaving the genuine singularities $-\xizero$ and the
irregular $\infty$. In particular $\Bhat$ has no singularity at $2\xizero,3\xizero,\dots$, so the
hypothetical infinite alien tower (in the sense of \'Ecalle's alien calculus~\cite{Ecalle})
suggested by the $(1/2)^n$ numerical floor reported in the parent probe
(\texttt{PERIOD-REP-VQUAD-001}, \texttt{numerical-check.md})
does not exist; the resurgence of $\Vquad$ is governed by the finite rank-$4$ connection $\LV$.
\end{proof}

This finiteness is what makes the period analysis of Section~\ref{sec:verif} possible at all: a
single branch at $-\xizero$ carries the entire connection datum, and the thimble of
Section~\ref{sec:cycle} sees exactly that branch.

\begin{lemma}[The apparent point carries no period]\label{lem:apparent}
The singularity of $\Bhat$ at $\xi=0$ contributes nothing to any rapid-decay period: its local
exponents $\{-1,0,1,2\}$ are consecutive integers, so the local monodromy is trivial and $\Bhat$
extends holomorphically across $0$ (it is the exponent-$0$ solution). Hence no cut emanates from
$0$, and the only branch a thimble can wrap is the one at $-\xizero$.
\end{lemma}

\begin{proof}
At a regular-singular point with integer exponents differing by integers and no logarithmic
solution, the local solution space contains a single-valued generator for each exponent, with the
top exponent solution holomorphic; the indicial data at $0$
(\eqref{eq:p4-factor} gives a simple zero of $p_4$ at $0$, and the falling-factorial indicial
polynomial $\propto s(s-2)(s-1)(s+1)$ has roots $\{-1,0,1,2\}$) shows $\Bhat$, the exponent-$0$
member, is holomorphic. Triviality of the monodromy is the definition of an apparent singularity.
Source: \texttt{PERIOD-REP-VQUAD-002}, \texttt{operator-verification.md}~\S4.2.
\end{proof}

\subsection{Algebraicity for Fres\'an--Jossen}
Theorems~\ref{thm:Lphi} and~\ref{thm:LV} discharge the load-bearing Fres\'an--Jossen axiom for
the eventual motive: $\omega=\Bhat(\xi)\,d\xi$ is an algebraic de Rham form for the twisted
connection $E^{-f}\otimes(\mathcal{O}^4,\nabla_{\LV})$ with $f=-\xi$, defined over the number
field $\Qsqrt$. The transcendental Painlev\'e-V accessory parameter of $\Vquad$ lives in the
\emph{nonlinear} moduli; the \emph{linear} scalar reduction governing the asymptotics is over
$\Qsqrt$, which is why no transcendental constant enters $\Lphi$ or $\LV$. We make the motivic
use of this precise in Section~\ref{sec:fj}.
