\section{The rapid-decay cycle \texorpdfstring{$\gamma$}{gamma}}\label{sec:cycle}

This section makes the cycle $\gamma$ of Theorem~\ref{thm:main} precise, verifies that it is a
rapid-decay cycle in the Fres\'an--Jossen sense, and records its relative-homology class. All
statements are sourced to the probe deliverables
\texttt{cycle-formal-definition.md} and \texttt{rapid-decay-verification.md} of the slot
\texttt{PERIOD-REP-VQUAD-003}.

\subsection{The Hankel thimble}
By Proposition~\ref{prop:exponents} the Borel transform $\Bhat$ has, at the regular-singular
point $\xi=-\xizero$, the local form
\begin{equation}\label{eq:branch-local}
  \Bhat(\xi)\;\sim\;A\,(\xi+\xizero)^{-(1+\beta)},\qquad
  -(1+\beta)=-1+\tfrac{\sqrt3}{9}=-0.80754991027\ldots,
\end{equation}
with $A=(S/2\pi i)\,\Gamma(1+\beta)$ the branch amplitude (so $\lvert A\rvert=K\,\Gamma(1+\beta)$;
Section~\ref{sec:verif}). The cut emanating from $-\xizero$ runs along the negative real axis to
$-\infty$, which---crucially---is the direction in which the action factor $e^{\xi}$ decays.

\begin{definition}[The cycle $\gamma$]\label{def:gamma}
Fix $\varepsilon\to0^+$. The cycle $\gamma=\gamma_{\mathrm{below}}+\gamma_{\mathrm{loop}}
+\gamma_{\mathrm{above}}$ is the Hankel thimble wrapping the cut $(-\infty,-\xizero]$:
\[
\begin{array}{lll}
  \gamma_{\mathrm{below}}: & \xi(s)=-s-i\varepsilon, & s:+\infty\to\xizero \quad(\text{lower lip}),\\[2pt]
  \gamma_{\mathrm{loop}}:  & \xi(\theta)=-\xizero+\varepsilon e^{i\theta}, & \theta:-\pi\to+\pi
        \quad(\text{clockwise around }-\xizero),\\[2pt]
  \gamma_{\mathrm{above}}: & \xi(s)=-s+i\varepsilon, & s:\xizero\to+\infty \quad(\text{upper lip}),
\end{array}
\]
oriented so that the branch point $-\xizero$ is encircled once clockwise (the orientation matching
Laplace inversion $\int_0^\infty\!\to\!\text{wrapped contour}$). The two lips carry the two
determinations $(\xi+\xizero)^{-(1+\beta)}_{\pm}$, differing by the monodromy factor
$e^{\mp2\pi i(1+\beta)}$.
\end{definition}

\begin{figure}[h]
\centering
\begin{tikzpicture}[scale=1.05,>=Latex]
  % axes
  \draw[->,gray!60] (-6.2,0) -- (1.6,0) node[below right,black]{$\operatorname{Re}\xi$};
  \draw[->,gray!60] (0,-1.4) -- (0,1.6) node[left,black]{$\operatorname{Im}\xi$};
  % branch cut
  \draw[decorate,decoration={zigzag,segment length=4pt,amplitude=1pt},red!70]
        (-5.9,0) -- (-2.6,0);
  % branch point
  \fill (-2.6,0) circle (1.6pt) node[below=5pt]{$-\xizero$};
  \node[red!70] at (-4.4,0.32) {cut};
  % origin (apparent) and label
  \fill (0,0) circle (1.4pt) node[above right=-1pt]{$0$};
  \node[font=\footnotesize] at (0.05,-0.32) {(apparent)};
  % upper lip (above), incoming arrow pointing toward branch point
  \draw[blue!75,thick,->] (-5.9,0.16) -- (-3.7,0.16);
  \draw[blue!75,thick] (-3.7,0.16) -- (-2.75,0.16);
  \node[blue!75,font=\footnotesize] at (-4.7,0.40) {$\gamma_{\mathrm{above}}$};
  % loop
  \draw[blue!75,thick] (-2.75,0.16) arc (130:-130:0.22);
  % lower lip outgoing
  \draw[blue!75,thick,<-] (-5.9,-0.16) -- (-3.7,-0.16);
  \draw[blue!75,thick] (-3.7,-0.16) -- (-2.75,-0.16);
  \node[blue!75,font=\footnotesize] at (-4.7,-0.42) {$\gamma_{\mathrm{below}}$};
  % rapid decay direction
  \draw[->,green!55!black,thick] (-1.2,1.0) -- (-2.4,1.0)
        node[midway,above,font=\footnotesize,black]{$e^{\xi}\!\to\!0$};
\end{tikzpicture}
\caption{The rapid-decay cycle $\gamma=\gamma_{\mathrm{below}}+\gamma_{\mathrm{loop}}
+\gamma_{\mathrm{above}}$ (Definition~\ref{def:gamma}): a Hankel thimble wrapping the cut
$(-\infty,-\xizero]$ of $\Bhat$, clockwise about the branch point $-\xizero$. The action factor
$e^{\xi}$ decays into $\operatorname{Re}\xi\to-\infty$, which is the cut direction; the point
$\xi=0$ is apparent and carries no cut.}
\label{fig:gamma}
\end{figure}

\subsection{Rapid decay}
\begin{proposition}[$\gamma$ is a rapid-decay cycle for $f=-\xi$]\label{prop:rapiddecay}
The integrand $e^{\xi}\Bhat(\xi)$ decays super-polynomially at both non-compact ends of $\gamma$
and is integrable at the finite branch point, so $\int_\gamma e^{\xi}\Bhat(\xi)\,d\xi$ converges
absolutely.
\end{proposition}

\begin{proof}
\emph{Ends.} On either lip $\xi=-s\pm i\varepsilon$ with $s\to+\infty$, so
$\lvert e^{\xi}\rvert=e^{\operatorname{Re}\xi}=e^{-s}$. Since $\Bhat$ is holonomic, it has
moderate (tempered) growth in the fixed non-Stokes direction $\arg\xi=\pi$: $\lvert\Bhat(\xi)\rvert
\le C_0\,s^{N}$ for some fixed $N$ (\cite{vdPS}, Ch.~3). Hence
$\lvert e^{\xi}\Bhat(\xi)\rvert\le C_0\,s^{N}e^{-s}\to0$ super-polynomially, and
$\int^{+\infty}C_0 s^N e^{-s}\,ds=C_0\,\Gamma(N+1)<\infty$. This is precisely the Fres\'an--Jossen
rapid-decay condition at the non-compact ends.

\emph{Branch point.} By~\eqref{eq:branch-local} the local exponent satisfies $-(1+\beta)>-1$
(equivalently $\beta<0$, true since $\beta=-1/(3\sqrt3)$). Thus
$\int_{\lvert\xi+\xizero\rvert<\delta}\lvert\xi+\xizero\rvert^{-(1+\beta)}\lvert d\xi\rvert
=\int_0^\delta r^{-(1+\beta)}\,dr=\delta^{-\beta}/(-\beta)<\infty$, and the radius-$\varepsilon$
loop contributes nothing in the limit. The thimble integral collapses to the discontinuity
integral
\begin{equation}\label{eq:disc}
  \int_\gamma e^{\xi}\Bhat\,d\xi
  =\bigl(1-e^{2\pi i(1+\beta)}\bigr)\int_{-\infty}^{-\xizero}e^{\xi}\,[\operatorname{disc}\Bhat](\xi)\,d\xi,
\end{equation}
which is finite. (If instead $\beta\le-1$ the $\Gamma$-factor of Section~\ref{sec:verif} would
diverge, contradicting the observed finite amplitude $\lvert A\rvert$.)
\end{proof}

\subsection{Fres\'an--Jossen relative homology}
We record $\gamma$ as a class in rapid-decay homology. Let $X=\mathbb{A}^1_\xi$ over $\Qsqrt$ with
the regular potential $f=-\xi\in\mathcal{O}(X)$ (so $df=-d\xi\ne0$: no finite critical points), and
let
\begin{equation}\label{eq:Mmotive}
  M=\bigl(\mathcal{O}_X\text{-module defined by }\LV\bigr)\otimes E^{-f},\qquad
  E^{-f}=(\mathcal{O}_X,\nabla=d-df),
\end{equation}
be the twisted connection. By Theorem~\ref{thm:LV}, $\omega=\Bhat(\xi)\,d\xi$ is a global algebraic
de Rham section of $M$ defined over $\Qsqrt$.

\begin{proposition}[Class of $\gamma$]\label{prop:fjclass}
$\gamma$ defines a class in the rapid-decay homology
$H_1^{\mathrm{rd}}(X,M)=H_1(X,Z;\mathrm{rd})$ (in the sense of Hien's rapid-decay
homology~\cite{Hien}, the Betti realisation underlying the Fres\'an--Jossen pairing), $Z=\{-\xizero\}$, with the rapid-decay condition
prescribing ends running into the half-plane $\operatorname{Re}\xi\to-\infty$. In Fres\'an--Jossen
thimble notation,
\begin{equation}\label{eq:fjthimble}
  [\gamma]=\bigl\langle\,-\xizero\,;\,(-\infty\cdot e^{i\pi})\,\bigr\rangle_{\mathrm{rd}}
  \in H_1^{\mathrm{rd}}(\mathbb{A}^1,M),
\end{equation}
the moderate (finite, integrable, exponent $-(1+\beta)>-1$) endpoint being the branch point
$-\xizero$ and the rapid-decay endpoint the ray $\arg\xi=\pi$. The exponential period is the
canonical pairing
\begin{equation}\label{eq:fjpairing}
  \int_\gamma e^{\xi}\Bhat(\xi)\,d\xi
  =\bigl\langle\,[\gamma]_{\mathrm{rd}},\,[e^{\xi}\Bhat\,d\xi]_{\mathrm{dR}}\,\bigr\rangle .
\end{equation}
\end{proposition}

\begin{remark}[Rank of the rapid-decay homology]\label{rmk:rank}
The local system underlying $M$ has rank $4$ (the order of $\LV$), but the rapid-decay class
$[\gamma]$ probes only the part with nontrivial monodromy at $-\xizero$. Of the four local
exponents $\{-(1+\beta),0,1,2\}$ there, the three integer exponents give single-valued
(holomorphic) solutions and the apparent point $\xi=0$ contributes nothing
(Proposition~\ref{prop:exponents}); the monodromy around $-\xizero$ is therefore the rank-one
factor $e^{2\pi i\,(-(1+\beta))}=e^{-2\pi i(1+\beta)}=e^{-2\pi i\beta}$ acting on the branch
solution. The discontinuity~\eqref{eq:disc} is exactly $(1-e^{2\pi i(1+\beta)})$ times the
one-sided integral, so $[\gamma]$ is the generator of the one-dimensional rapid-decay homology of
this branch, paired against the algebraic class $[\omega]$. This is why a single thimble captures
the entire connection datum: the finite resurgence of Corollary~\ref{cor:finite} has reduced the
period problem to a rank-one branch.
\end{remark}

The three structural conditions a Fres\'an--Jossen thimble must satisfy
(\cite{FJ}; \texttt{fj-cycle-compatibility.md}) hold: \emph{(C1)} the de Rham datum $\omega$ is
algebraic over a number field---here $\Qsqrt$ (Theorem~\ref{thm:LV}); \emph{(C2)} the potential $f$
is a regular function with the cut aligned to a rapid-decay direction
(Proposition~\ref{prop:rapiddecay}); \emph{(C3)} the chain has moderate endpoints on $Z$ and
rapid-decay non-compact ends~\eqref{eq:fjthimble}. We use this in Section~\ref{sec:fj}.

\begin{remark}[Sign convention]\label{rmk:fjsign}
Fres\'an--Jossen write the integrand as $e^{-f}\omega$. We use $f=-\xi$, so $e^{-f}=e^{+\xi}$,
matching the task convention $f_{\mathrm{task}}=-f_{\mathrm{FJ}}$. The rapid-decay direction is
therefore $\operatorname{Re}\xi\to-\infty$, exactly where the corrected (negative-axis) Borel
geometry of Section~\ref{sec:operators} places the cut: the geometry is the Fres\'an--Jossen
natural one, not an artefact.
\end{remark}
