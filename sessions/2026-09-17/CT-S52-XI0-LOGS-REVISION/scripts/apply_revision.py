#!/usr/bin/env python3
"""CT-S52 Part B -- apply the revision to a COPY of the submitted source.

The submitted source is never opened for writing. This script reads it, applies
an explicit list of (old, new) replacements each of which must match EXACTLY
once, and writes revision/vquad-periodrep-paper.tex. It is idempotent: it always
starts from the pristine source, so re-running cannot compound an edit.

Each replacement is tagged with the email item it serves (1..4) or R for the
reference block, so the changes list is derived from the code, not retyped.

Exit: 0 all applied, 2 refusal (a pattern matched 0 or >1 times), 3 crash.
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
SRC = os.path.join(ROOT, "sessions", "2026-06-16", "VQUAD-PAPER-LAYOUTFIX-001",
                   "latex", "vquad-periodrep-paper.tex")
DST = os.path.join(HERE, "..", "revision", "vquad-periodrep-paper.tex")
OUT = os.path.join(HERE, "..", "outputs", "apply_revision.out.txt")
LINES = []


def say(s=""):
    print(s)
    LINES.append(s)


# (item, tag, old, new)
R = []


def rep(item, tag, old, new):
    R.append((item, tag, old, new))


# ---------------------------------------------------------------- item 1
rep("1", "abstract: D5 stated as fact",
    """rank-one standalone closure on the Sakai surface $D_5^{(1)}$ (Painlev\\'e~V)---admits an explicit""",
    """rank-one standalone closure whose Sakai surface type is conjectured to be $D_5^{(1)}$
(Painlev\\'e~V)---admits an explicit""")

rep("1", "1.1: identification + v1.3 notice on the Painleve parameters",
    """companion paper~\\cite{Vquad}, where it is identified as a non-classical Painlev\\'e~V
transcendent on the Sakai surface $D_5^{(1)}$ (symmetry $W(A_3^{(1)})$, $\\delta=-\\tfrac12\\ne0$,
in the surface/symmetry classification of~\\cite{SakaiClass}),
with formal monodromy exponent $\\theta_\\infty=2/\\sqrt3$ and $\\alpha=\\theta_\\infty^2/8=\\tfrac16$.""",
    """companion paper~\\cite{Vquad}, where it is \\emph{conjectured} to be a non-classical
Painlev\\'e~V transcendent on the Sakai surface $D_5^{(1)}$ (symmetry $W(A_3^{(1)})$,
$\\delta=-\\tfrac12\\ne0$, in the surface/symmetry classification of~\\cite{SakaiClass}).
That identification is Conjecture~4.1 of~\\cite{Vquad}, not a theorem, and nothing in the
present paper depends on it: every result below is a statement about the operators $\\Lphi$
and $\\LV$ and the cycle $\\gamma$. The formal monodromy exponent $\\theta_\\infty=2/\\sqrt3$ and
$\\alpha=\\theta_\\infty^2/8=\\tfrac16$ quoted there are the companion's; its version~1.3
correction notice~\\cite{VquadV13} revises the derivation by which those Painlev\\'e
parameters were obtained.""")

rep("1", "7.1: the representative described as a D5 representative",
    """(ii)(a)---that for the $D_5^{(1)}$ (Painlev\\'e~V) stratum this period is explicit. For $\\Vquad$,
the rank-one $D_5^{(1)}$ representative, that entry was previously graded \\emph{structural}: the""",
    """(ii)(a)---that for the $D_5^{(1)}$ (Painlev\\'e~V) stratum this period is explicit. For $\\Vquad$,
conjecturally the rank-one $D_5^{(1)}$ representative (\\cite{Vquad}, Conjecture~4.1), that
entry was previously graded \\emph{structural}: the""")

rep("1", "4.x algebraicity: accessory parameter asserted as fact (found by the sweep, not on the reported list)",
    """field $\\Qsqrt$. The transcendental Painlev\\'e-V accessory parameter of $\\Vquad$ lives in the
\\emph{nonlinear} moduli; the \\emph{linear} scalar reduction governing the asymptotics is over""",
    """field $\\Qsqrt$. Under the conjectured identification of~\\cite{Vquad}, Conjecture~4.1, the
transcendental Painlev\\'e-V accessory parameter of $\\Vquad$ would live in the
\\emph{nonlinear} moduli; the \\emph{linear} scalar reduction governing the asymptotics is over""")

# ---------------------------------------------------------------- item 2
rep("2", "7.1: 'completes part (ii)(a) for d=2'",
    """Theorem~\\ref{thm:main} exhibits the integral and verifies it three ways, so the present paper
\\emph{completes part (ii)(a) for $d=2$}: the $D_5^{(1)}$ connection constant is realised as an
explicit Fres\\'an--Jossen exponential period, and (conditionally) transcendental.""",
    """Theorem~\\ref{thm:main} exhibits the integral and verifies it three ways. What this
establishes is an \\emph{instance} of part~(ii)(a) for the single representative $\\Vquad$:
its connection constant is realised as an explicit Fres\\'an--Jossen exponential period, and
is transcendental under the two hypotheses of Corollary~\\ref{cor:transc}. The instance is
attached to the $D_5^{(1)}$ stratum only through the conjectured surface identification
of~\\cite{Vquad}, Conjecture~4.1. Part~(ii)(a) is \\emph{not} established for the stratum: no
statement is made here about any other member, and nothing here proves that $\\Vquad$ lies in
that stratum.""")

# ---------------------------------------------------------------- item 3
rep("3", "Theorem 1.2: 'proved twice'",
    """The differential Galois group of $\\Lphi$ over $\\Qsqrt(z)$ is $\\SL_2(\\mathbb{C})$. This is proved
twice: by Kovacic case-elimination and by a structural torus-plus-unipotent argument
(Section~\\ref{sec:operators}, certificate in Appendix~\\ref{app:kovacic}).""",
    """The differential Galois group of $\\Lphi$ over $\\Qsqrt(z)$ is $\\SL_2(\\mathbb{C})$. The proof is
Kovacic case-elimination (Section~\\ref{sec:operators}, certificate in
Appendix~\\ref{app:kovacic}). The structural torus-plus-unipotent argument recorded there is a
consistency check on the same computation, not a second proof: a maximal torus together with
one root unipotent generates a \\emph{Borel} subgroup, and the passage to $\\SL_2(\\mathbb{C})$
uses the exclusion of the reducible case, which is Kovacic's Case~1.""")

rep("3", "1.4: 'an independent structural argument'",
    """are the province of Kovacic's algorithm~\\cite{Kovacic} and of packages such as Maple's
\\texttt{DEtools[DifferentialGaloisGroup]} (we reproduced the Kovacic verdict by case-elimination
and by an independent structural argument, Appendix~\\ref{app:kovacic}); and the Borel--Pad\\'e""",
    """are the province of Kovacic's algorithm~\\cite{Kovacic} and of packages such as Maple's
\\texttt{DEtools[DifferentialGaloisGroup]} (we obtained the Kovacic verdict by case-elimination,
with the structural argument of Appendix~\\ref{app:kovacic} as a consistency check on it, not as
a second derivation); and the Borel--Pad\\'e""")

rep("3", "2.2 proof: the structural argument restated correctly",
    """\\emph{(2) Structural argument.} The reduced equation $u''=ru$ has no first-order term, so the
Wronskian is constant and $G\\subseteq\\SL_2$. At $z=0$ the two distinct exponentials
$\\exp(\\pm(1/\\sqrt3)/z)$ generate the full diagonal torus $\\mathbb{G}_m\\subset\\SL_2$ (the local
exponential torus). The nonvanishing Stokes constant $S=2\\pi K\\ne0$ at this irregular point is a
nonidentity unipotent off that torus. A maximal torus together with one off-torus unipotent
generate $\\SL_2$, whence $G=\\SL_2(\\mathbb{C})$.
\\end{proof}

The two routes are genuinely independent---an exhaustive negative search versus a positive
generation argument from the Stokes datum---and agree. (Only one symbolic engine was available;
the second route supplies the cross-check that a second computer-algebra system would otherwise
provide. See Appendix~\\ref{app:kovacic}.)""",
    """\\emph{(2) Structural argument (a consistency check on~(1), not a second proof).} The reduced
equation $u''=ru$ has no first-order term, so the Wronskian is constant and $G\\subseteq\\SL_2$.
At $z=0$ the two distinct exponentials $\\exp(\\pm(1/\\sqrt3)/z)$ generate the diagonal torus
$T=\\mathbb{G}_m\\subset\\SL_2$ (the local exponential torus), and the nonvanishing Stokes constant
$S=2\\pi K\\ne0$ at this irregular point supplies one root unipotent $u\\in U$. A maximal torus
together with a single root unipotent generates the Borel subgroup $B=T\\ltimes U$: the opposite
root group is not produced, so this datum alone gives only $G\\supseteq B$. Passing from $B$ to
$\\SL_2(\\mathbb{C})$ requires ruling out $G\\subseteq B$, i.e. ruling out the reducible case---which
is precisely Kovacic's Case~1, eliminated in~(1). With that exclusion in hand, $G\\supsetneq B$
and the only connected subgroup of $\\SL_2$ properly containing a Borel subgroup is
$\\SL_2(\\mathbb{C})$ itself, whence $G=\\SL_2(\\mathbb{C})$.
\\end{proof}

The two routes are therefore \\emph{not} independent: route~(2) is conditional on the Case~1
exclusion established in route~(1), and cross-checks that computation rather than replacing it.
(Only one symbolic engine was available; an independent verdict would require a second
computer-algebra system, for example Maple's \\texttt{DEtools[DifferentialGaloisGroup]}. See
Appendix~\\ref{app:kovacic}.)""")

rep("3", "Appendix A.2: 'Independent structural confirmation'",
    """Independent structural confirmation: the reduced equation has no first-order term, so
$G\\subseteq\\SL_2$; the two distinct exponentials $\\exp(\\pm(1/\\sqrt3)/z)$ at $z=0$ generate the
diagonal torus, and the nonzero Stokes constant $S=2\\pi K$ supplies an off-torus unipotent;
torus-plus-unipotent generate $\\SL_2$. Source: \\texttt{PERIOD-REP-VQUAD-003},""",
    """Structural consistency check (not independent of the above): the reduced equation has no
first-order term, so $G\\subseteq\\SL_2$; the two distinct exponentials $\\exp(\\pm(1/\\sqrt3)/z)$ at
$z=0$ generate the diagonal torus, and the nonzero Stokes constant $S=2\\pi K$ supplies one root
unipotent. Torus-plus-one-root-unipotent generates a \\emph{Borel} subgroup; $\\SL_2$ follows only
after the reducible case is excluded, which is Case~1 above. Source:
\\texttt{PERIOD-REP-VQUAD-003},""")

rep("3", "A.5: 'case-elimination plus the structural argument'",
    """the Kovacic verdict, optionally cross-checkable in Maple's
\\texttt{DEtools[DifferentialGaloisGroup]}, is here obtained by open case-elimination plus the
structural argument of Appendix~\\ref{app:kovacic}.""",
    """the Kovacic verdict, optionally cross-checkable in Maple's
\\texttt{DEtools[DifferentialGaloisGroup]}, is here obtained by open case-elimination, with the
structural argument of Appendix~\\ref{app:kovacic} as a consistency check that depends on the
same Case~1 exclusion.""")

# ---------------------------------------------------------------- item 4
rep("4", "Prop 2.4: apparency at xi=0",
    """with $-(1+\\beta)=-1+\\sqrt3/9=-0.80754991027\\ldots$ the unique non-integer exponent. At $\\xi=0$
the four exponents are consecutive integers, so the point is \\emph{apparent} (single-valued, $\\Bhat$
itself is the holomorphic exponent-$0$ solution). At $\\xi=-\\xizero$ the branch is carried by the""",
    """with $-(1+\\beta)=-1+\\sqrt3/9=-0.80754991027\\ldots$ the unique non-integer exponent. At $\\xi=0$
the four exponents are consecutive integers, so every step of the Frobenius recursion from the
lowest exponent $-1$ to the next is \\emph{resonant} and a logarithm is possible. It occurs: the
recursion started at $\\xi^{-1}$ is obstructed at the first resonant step, the obstruction being
the nonzero element
\\[
  \\frac{38286+24984\\sqrt3}{418501}\\;\\in\\;\\Qsqrt ,
\\]
so there is no formal solution with leading exponent $-1$, the log-free local solution space has
dimension $3$ (leading exponents $0,1,2$) and the fourth local solution carries $\\log\\xi$. Hence
$\\xi=0$ is a genuine regular singular point of $\\LV$ with unipotent local monodromy, \\emph{not}
an apparent one. $\\Bhat$ itself is the exponent-$0$ solution and is holomorphic at $0$, which is
all the main identity uses (Lemma~\\ref{lem:apparent}). The computation is exact in $\\Qsqrt$ and
is confirmed by three implementations that share no code: the resonant-step obstruction, the
rank of the truncated Laurent system, and the explicit construction of the logarithmic solution;
see Appendix~\\ref{app:numlogs}. At $\\xi=-\\xizero$ the branch is carried by the""")

rep("4", "Table 1: '0 (apparent)'",
    """finite singularities & $\\rho_\\pm=\\tfrac{-1\\pm i\\sqrt{11}}2$ (reg.) & $0$ (apparent), $-\\xizero$ (branch) \\\\""",
    """finite singularities & $\\rho_\\pm=\\tfrac{-1\\pm i\\sqrt{11}}2$ (reg.) & $0$ (reg. sing., logarithmic; $\\Bhat$ holomorphic there), $-\\xizero$ (branch) \\\\""")

rep("4", "Cor 1.4 proof: 'the point 0 is apparent'",
    """$\\operatorname{Sing}(\\Bhat)\\subseteq\\{0,-\\xizero,\\infty\\}$; the point $0$ is apparent
(Proposition~\\ref{prop:exponents}), leaving the genuine singularities $-\\xizero$ and the""",
    """$\\operatorname{Sing}(\\Bhat)\\subseteq\\{0,-\\xizero,\\infty\\}$; and although $0$ is a genuine regular
singular point of $\\LV$, carrying a logarithmic local solution
(Proposition~\\ref{prop:exponents}), $\\Bhat$ is not that solution: it is the holomorphic
exponent-$0$ one, so $0$ is not a singularity of $\\Bhat$, leaving the genuine singularities
$-\\xizero$ and the""")

rep("4", "Lemma 2.7 statement and proof",
    """\\begin{lemma}[The apparent point carries no period]\\label{lem:apparent}
The singularity of $\\Bhat$ at $\\xi=0$ contributes nothing to any rapid-decay period: its local
exponents $\\{-1,0,1,2\\}$ are consecutive integers, so the local monodromy is trivial and $\\Bhat$
extends holomorphically across $0$ (it is the exponent-$0$ solution). Hence no cut emanates from
$0$, and the only branch a thimble can wrap is the one at $-\\xizero$.
\\end{lemma}

\\begin{proof}
At a regular-singular point with integer exponents differing by integers and no logarithmic
solution, the local solution space contains a single-valued generator for each exponent, with the
top exponent solution holomorphic; the indicial data at $0$
(\\eqref{eq:p4-factor} gives a simple zero of $p_4$ at $0$, and the falling-factorial indicial
polynomial $\\propto s(s-2)(s-1)(s+1)$ has roots $\\{-1,0,1,2\\}$) shows $\\Bhat$, the exponent-$0$
member, is holomorphic. Triviality of the monodromy is the definition of an apparent singularity.
Source: \\texttt{PERIOD-REP-VQUAD-002}, \\texttt{operator-verification.md}~\\S4.2.
\\end{proof}""",
    """\\begin{lemma}[The point $\\xi=0$ carries no period]\\label{lem:apparent}
The point $\\xi=0$ contributes nothing to any rapid-decay period of $\\Bhat$. The local solution
space of $\\LV$ at $0$ does contain a logarithm (Proposition~\\ref{prop:exponents}), so $0$ is not
an apparent singularity of the operator; but $\\Bhat$ is the holomorphic exponent-$0$ solution, so
$\\Bhat$ extends across $0$, no cut of $\\Bhat$ emanates from $0$, and the only branch a thimble
can wrap is the one at $-\\xizero$.
\\end{lemma}

\\begin{proof}
The indicial data at $0$ (\\eqref{eq:p4-factor} gives a simple zero of $p_4$ at $0$, and the
falling-factorial indicial polynomial $\\propto(s+1)s(s-1)(s-2)$ has roots $\\{-1,0,1,2\\}$) make
$0$ regular singular with consecutive integer exponents. The exponent-$0$ solution is the
convergent power series $\\Bhat=\\sum_m b_m\\xi^m$ itself: the residual $\\LV\\Bhat$ vanishes
identically in $\\Qsqrt$ through order $\\xi^{129}$ (Theorem~\\ref{thm:LV},
Appendix~\\ref{app:coeffs}), and $\\Bhat$ is holomorphic at $0$ because $\\varphi$ is Gevrey-$1$.
A function holomorphic at a point has no cut there, whatever the monodromy of the other local
solutions of its annihilator; and the cycle $\\gamma$ of Section~\\ref{sec:cycle} lies in
$(-\\infty,-\\xizero]$ and does not approach $0$. Note that the older assertion that $0$ is
\\emph{apparent} is false---consecutive integer exponents make the point resonant, not
apparent---and is corrected in Proposition~\\ref{prop:exponents}; the present lemma, and with it
the main identity, does not use apparency. Source: \\texttt{PERIOD-REP-VQUAD-002},
\\texttt{operator-verification.md}~\\S4.2, and Appendix~\\ref{app:numlogs}.
\\end{proof}""")

rep("4", "figure: node label '(apparent)'",
    """  \\node[font=\\footnotesize] at (0.05,-0.32) {(apparent)};""",
    """  \\node[font=\\footnotesize] at (0.05,-0.32) {(no cut)};""")

rep("4", "figure caption: 'xi=0 is apparent and carries no cut'",
    """$e^{\\xi}$ decays into $\\operatorname{Re}\\xi\\to-\\infty$, which is the cut direction; the point
$\\xi=0$ is apparent and carries no cut.}""",
    """$e^{\\xi}$ decays into $\\operatorname{Re}\\xi\\to-\\infty$, which is the cut direction; $\\Bhat$ is
holomorphic at $\\xi=0$, so no cut of $\\Bhat$ emanates from that point.}""")

rep("4", "Remark 3.3: 'the apparent point'",
    """(holomorphic) solutions and the apparent point $\\xi=0$ contributes nothing
(Proposition~\\ref{prop:exponents});""",
    """(holomorphic) solutions, and $\\xi=0$ contributes nothing---$\\Bhat$ is holomorphic there and
$\\gamma$ does not approach it (Lemma~\\ref{lem:apparent})---""")

rep("4", "A.3: record the xi=0 log computation",
    """Method agreement (\\texttt{stage4\\_methods.py}, \\texttt{stage1\\_hankel\\_period.py} at dps""",
    """\\emph{Logarithms at $\\xi=0$ (exact, no floating point).} The local exponents of $\\LV$ at
$\\xi=0$ are the consecutive integers $\\{-1,0,1,2\\}$, the exact integer roots of the indicial
polynomial. Running the Frobenius recursion from the lowest exponent $-1$ in exact $\\Qsqrt$
arithmetic, the first resonant step is obstructed by
$(38286+24984\\sqrt3)/418501\\ne0$; the steps from exponents $0$, $1$ and $2$ are unobstructed.
The log-free local solution space therefore has dimension $3$, with leading exponents
$0,1,2$, and the fourth local solution carries $\\log\\xi$; a representative of it,
$\\xi^{-1}(1+\\cdots)+c\\,\\log\\xi\\,(v_0+v_1\\xi+\\cdots)$ with $v_0=-(2+\\sqrt3)/24$, is exhibited
explicitly. Three implementations sharing no code agree: the resonant-step obstruction, the
rank of the truncated Laurent system (dimension $3$ at truncation orders $16$ and $24$), and
the explicit logarithmic solution. Consequently $\\xi=0$ is \\emph{not} an apparent singularity
of $\\LV$; $\\Bhat$, the exponent-$0$ solution, is unaffected, and so is the main identity
(Lemma~\\ref{lem:apparent}).

Method agreement (\\texttt{stage4\\_methods.py}, \\texttt{stage1\\_hankel\\_period.py} at dps""")

# ---------------------------------------------------------------- references
rep("R", "new bibitem for the companion's v1.3 correction notice",
    """DOI \\texttt{10.1070/SM1996v187n09ABEH000158}.

\\end{thebibliography}""",
    """DOI \\texttt{10.1070/SM1996v187n09ABEH000158}.

\\bibitem{VquadV13}
Papanokechi,
\\emph{A non-classical Painlev\\'e~V transcendent from a quadratic polynomial continued fraction:
surface classification and resurgent Stokes data}.
Zenodo, 2026, version DOI \\texttt{10.5281/zenodo.22831933} (version~1.3; concept DOI
\\texttt{10.5281/zenodo.20455089}). See its correction notice, whose items~C1 and~C2 respectively
withdraw an apparency claim and revise the derivation of the quoted Painlev\\'e parameters.

\\end{thebibliography}""")


def main():
    say("=" * 74)
    say("CT-S52 PART B -- applying the revision to a copy")
    say("=" * 74)
    data = open(SRC, "rb").read()
    say("source      : %s" % os.path.relpath(SRC, ROOT))
    say("source sha256: %s" % hashlib.sha256(data).hexdigest())
    text = data.decode("utf-8")
    crlf = "\r\n" in text
    body = text.replace("\r\n", "\n")
    say("line endings : %s" % ("CRLF" if crlf else "LF"))
    say()
    bad = 0
    for item, tag, old, new in R:
        n = body.count(old)
        say("  item %-2s %-52s matches=%d" % (item, tag[:52], n))
        if n != 1:
            say("      REFUSED: pattern must match exactly once")
            bad += 1
            continue
        body = body.replace(old, new, 1)
    if bad:
        say()
        say("REFUSED: %d replacement(s) did not match exactly once; nothing written."
            % bad)
        return 2
    outtext = body.replace("\n", "\r\n") if crlf else body
    os.makedirs(os.path.dirname(os.path.abspath(DST)), exist_ok=True)
    with open(os.path.abspath(DST), "wb") as fh:
        fh.write(outtext.encode("utf-8"))
    after = open(SRC, "rb").read()
    say()
    say("  replacements applied : %d" % len(R))
    say("  revised copy         : %s" % os.path.relpath(os.path.abspath(DST), ROOT))
    say("  revised sha256       : %s"
        % hashlib.sha256(outtext.encode("utf-8")).hexdigest())
    say("  submitted source unchanged: %s"
        % ("YES" if after == data else "NO -- REFUSE"))
    say("=" * 74)
    return 0 if after == data else 2


if __name__ == "__main__":
    try:
        rc = main()
    except Exception as exc:  # noqa: BLE001
        say("CRASH: %r" % (exc,))
        rc = 3
    os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
    with open(os.path.abspath(OUT), "w", encoding="utf-8") as fh:
        fh.write("\n".join(LINES) + "\n")
    print("[wrote]", os.path.abspath(OUT))
    sys.exit(rc)
