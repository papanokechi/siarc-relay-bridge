\section{Introduction}\label{sec:intro}

\subsection{The V\_quad continued fraction and its connection coefficient}
Let $\Vquad$ denote the polynomial continued fraction
\begin{equation}\label{eq:vquad-pcf}
  \Vquad \;=\; 1 \;+\; \K_{n\ge 1}\,\frac{1}{\,3n^{2}+n+1\,}
  \;=\; 1+\cfrac{1}{\,5+\cfrac{1}{\,15+\cfrac{1}{\,31+\cdots}}}\,,
\end{equation}
the partial denominators being the quadratic $b_n=3n^2+n+1$ and all partial numerators $1$.
This is the rank-one ($n=1$) standalone member of the V\_quad family studied in the V\_quad
companion paper~\cite{Vquad}, where it is identified as a non-classical Painlev\'e~V
transcendent on the Sakai surface $D_5^{(1)}$ (symmetry $W(A_3^{(1)})$, $\delta=-\tfrac12\ne0$,
in the surface/symmetry classification of~\cite{SakaiClass}),
with formal monodromy exponent $\theta_\infty=2/\sqrt3$ and $\alpha=\theta_\infty^2/8=\tfrac16$.
The asymptotic (WKB/Riccati) solution of the associated problem is a Gevrey-1 formal power
series
\begin{equation}\label{eq:phi-series}
  \varphi(z)\;=\;\sum_{n\ge 0} a_n z^n ,\qquad a_0=1,
\end{equation}
whose Borel transform has an isolated singularity at the \emph{action}
$\xizero=2/\sqrt3=1.15470053837925\ldots$ of branch type governed by the exponent
\begin{equation}\label{eq:beta}
  \beta=-\frac{1}{3\sqrt3}=-0.19245008972987525\ldots
\end{equation}
The \emph{connection coefficient} $\C$ of $\Vquad$ is the Borel branch amplitude attached to
that singularity; in the standard resurgence normalisation~\cite{Dingle,BerryHowls,StokesNote}
it equals
\begin{equation}\label{eq:C-skeleton}
  \C \;=\; \lvert\Gamma(\beta)\rvert\cdot K,\qquad
  K=0.0728781025518669641294\ldots,
\end{equation}
where $K$ is the prefactor-stripped Dingle late-term amplitude of~\eqref{eq:phi-series}. The
companion Stokes constant is $S=2\pi K=0.4579066231690176361190\ldots$, and the two normalisations
are tied by the exact bridge identity
\begin{equation}\label{eq:bridge}
  \frac{S}{\C}\;=\;\frac{2\pi}{\lvert\Gamma(\beta)\rvert}\qquad(\text{residual }0).
\end{equation}
The constant $\C$ governs the inter-sectorial (Stokes) jump of the Borel sum of $\varphi$ and is,
in the language of the parent program, the arithmetic fingerprint of the $\Vquad$ transcendent.

\subsection{The Sakai-stratification context}
The present paper is a self-contained contribution to one entry of a larger program, the
\emph{Sakai stratification of polynomial-continued-fraction transcendence}~\cite{Sakai}, which
classifies PCF limits by the Sakai surface type of the Painlev\'e isomonodromy governing their
tails and asks, for each stratum, whether the associated connection constant admits a period
interpretation. For the $D_5^{(1)}$ (Painlev\'e~V) stratum the master conjecture predicts that
$\C$ is an \emph{exponential period} in the sense of Fres\'an--Jossen~\cite{FJ}; the entry was
previously graded \emph{structural} (the skeleton $\Gamma(\beta)\cdot K$ matches, but no explicit
period integral was exhibited). All objects used below are defined in-paper, so no familiarity
with~\cite{Sakai} is required.

The significance is not confined to the program. Exhibiting a specific, independently interesting
constant as an explicit exponential period---rather than merely asserting it should be one---is the
kind of evidence the Kontsevich--Zagier and Grothendieck period philosophies call for: the
arithmetic of a number is conjecturally governed by the geometry of a motive realising it as a
period, and concrete realisations are scarce, especially for \emph{divergent}-series (Stokes)
constants rather than convergent integrals. The constant $\C$ here arises from a continued fraction
of the type produced en masse by the Ramanujan Machine~\cite{RamanujanMachine}, so the method also
indicates how the transcendence of machine-discovered constants might be approached structurally
rather than case by case.

\subsection{Main results}
We exhibit $\C$ as an explicit exponential-period integral and verify the identity three
independent ways. Write $\Bhat(\xi)=\sum_{m\ge0}b_m\xi^m$, $b_m=a_{m+1}/m!$, for the Borel
transform of~\eqref{eq:phi-series}, and let $\gamma$ be the Hankel thimble wrapping the cut
$(-\infty,-\xizero]$ (Definition~\ref{def:gamma}).

\begin{theorem}[Explicit exponential-period representation]\label{thm:main}
The Borel transform $\Bhat$ is holonomic with coefficients in the real quadratic field
$\Qsqrt$, annihilated by an explicit order-$4$ operator $\LV$ (Theorem~\ref{thm:LV}); the
cycle $\gamma$ is a rapid-decay cycle for the potential $f=-\xi$
(Proposition~\ref{prop:rapiddecay}); and
\begin{equation}\label{eq:main-identity}
  \boxed{\;\C\;=\;\frac{\lvert\Gamma(\beta)\rvert}{2\pi}\int_{\gamma} e^{\xi}\,\Bhat(\xi)\,d\xi
  \;=\;\lvert\Gamma(\beta)\rvert\cdot K\;}
\end{equation}
where the raw thimble integral equals $S\,e^{-\xizero}$ at leading order and $\C$ is recovered
by the explicit algebraic-$\Gamma$ factor $\lvert\Gamma(\beta)\rvert/2\pi$. The identity is
verified by three structurally independent methods---differential-equation/operator duality,
Borel--Laplace/Hankel, and Stokes-data---which agree to $46$ significant digits
(Section~\ref{sec:verif}).
\end{theorem}

The differential input is sharp. The series $\varphi$ is $D$-finite over \emph{exactly} $\Qsqrt$
(minimal operator $\Lphi$ of order $2$, degree $4$), and its differential Galois group is as
large as possible.

\begin{theorem}[Galois group of $\Lphi$]\label{thm:galois}
The differential Galois group of $\Lphi$ over $\Qsqrt(z)$ is $\SL_2(\mathbb{C})$. This is proved
twice: by Kovacic case-elimination and by a structural torus-plus-unipotent argument
(Section~\ref{sec:operators}, certificate in Appendix~\ref{app:kovacic}).
\end{theorem}

Holonomicity of $\Bhat$ has an immediate qualitative consequence for the resurgence of $\Vquad$.

\begin{corollary}[Finite resurgence]\label{cor:finite}
Because $\Bhat$ is holonomic of order $4$, it has only finitely many singularities, namely
$\{0,-\xizero,\infty\}$. In particular there is \emph{no} infinite alien tower at
$2\xizero,3\xizero,\dots$: the resurgent structure of $\Vquad$ is a finite rank-$4$ connection,
not a wild lattice (Section~\ref{sec:operators}).
\end{corollary}

Finally, interpreting~\eqref{eq:main-identity} in the Fres\'an--Jossen framework yields a
conditional transcendence statement. We are careful to flag \emph{both} layers of
conditionality.

\begin{corollary}[Conditional transcendence]\label{cor:transc}
Assume \emph{(i)} the Fres\'an--Jossen period conjecture for exponential motives
\textup{(\cite{FJ}, Conjecture~1.3.2)}, and \emph{(ii)} that the de Rham realisation computed
here represents the motivic Galois group of the exponential motive
$M=(\mathbb{A}^1\smallsetminus\{0,-\xizero\},\,f=-\xi,\,\Bhat\,d\xi)$ \textup{(the comparison
gap G-MOTGALOIS, Section~\ref{sec:fj})}. Then the V\_quad connection coefficient $\C$ is
transcendental over $\Qbar$.
\end{corollary}

\subsection{What is and is not computer-algebra-automatable here}
The differential backbone of this paper is squarely within reach of present-day symbolic
software, and we have used it: the recognition of $\Lphi$ and $\LV$ from the coefficient stream
is exactly holonomic guessing as implemented in \texttt{gfun}~\cite{gfun} and
\texttt{ore\_algebra}~\cite{oreAlgebra}; the Kovacic decision and the differential-Galois data
are the province of Kovacic's algorithm~\cite{Kovacic} and of packages such as Maple's
\texttt{DEtools[DifferentialGaloisGroup]} (we reproduced the Kovacic verdict by case-elimination
and by an independent structural argument, Appendix~\ref{app:kovacic}); and the Borel--Pad\'e
and large-order extractions are standard exponential-asymptotics computations. What is
\emph{not} automatable, and what constitutes the mathematical content of the paper, is
(a)~the identification of the precise rapid-decay cycle $\gamma$ and the proof that the three
period-extraction routes agree, and (b)~the motivic interpretation
(Corollary~\ref{cor:transc}), which lies beyond any current CAS. We return to this comparison
in Section~\ref{sec:disc} and Appendix~\ref{app:repro}.

\subsection{Organisation}
Section~\ref{sec:operators} constructs and verifies $\Lphi$ and $\LV$, proves
Theorem~\ref{thm:galois} and Corollary~\ref{cor:finite}. Section~\ref{sec:cycle} defines the
cycle $\gamma$ and establishes its rapid-decay property and Fres\'an--Jossen compatibility.
Section~\ref{sec:main} states and normalises the main identity. Section~\ref{sec:verif} gives
the three verifications and their cross-check. Section~\ref{sec:fj} applies the
Fres\'an--Jossen framework and proves Corollary~\ref{cor:transc}.
Section~\ref{sec:disc} discusses the place of the result in the stratification program, the
$d\ge3$ obstruction, and the relation to the Ramanujan-Machine/conservative-matrix-field
circle of ideas. Appendices collect the explicit coefficients, the Kovacic certificate, the
numerical logs, the four sign-convention enumeration for the differential-equation method, and
the reproducibility statement.

\subsection{Notation and conventions}
Throughout, $\Qsqrt=\mathbb{Q}(\sqrt3)$ is the real quadratic field generated by the V\_quad
Riccati seed $\sigma=-1/\sqrt3$, and $\Qbar$ the algebraic closure of $\mathbb{Q}$. We write
$D_z=d/dz$ and $D_\xi=d/d\xi$ (abbreviated $D$ when the variable is clear), and treat differential
operators as elements of the Weyl algebra $\Qsqrt\langle z,D_z\rangle$ (resp.\ in $\xi$). The
\emph{order} of an operator is its degree in $D$ and its \emph{degree} is the maximal polynomial
degree of its coefficients. The Borel transform is taken at Gevrey order $1$, $b_m=a_{m+1}/m!$,
mapping the divergent series $\varphi(z)=\sum a_nz^n$ to the convergent germ
$\Bhat(\xi)=\sum b_m\xi^m$; the dual variables satisfy $z\leftrightarrow1/\xi$ at the level of
exponential scales, with the operator intertwiner~\eqref{eq:duality}. The action is
$\xizero=2/\sqrt3$, the branch exponent $\beta=-1/(3\sqrt3)$, and we use the resurgence
normalisation in which the Stokes constant is $S=2\pi K$ with $K$ the prefactor-stripped Dingle
amplitude. The potential is written $f=-\xi$ in the task convention, equal to $-f_{\mathrm{FJ}}$ in
the Fres\'an--Jossen sign convention (Remark~\ref{rmk:fjsign}); the period pairing is
$\langle e^{-f}\omega,\gamma\rangle=\int_\gamma e^{\xi}\Bhat(\xi)\,d\xi$. All numerical constants
are reported to the precision at which they were certified (typically $46$--$58$ digits);
``residual $0$'' means an exact identity in $\Qsqrt$, while a residual such as
$8.84\times10^{-46}$ is a high-precision floating check.