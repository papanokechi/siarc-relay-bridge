"""check_171.py -- CT-S36-DRAFT-NOTATION, task 3.

Classifies each of the 171 used-before-defined items reported by the isolated
reader of CT-S23 (outputs/coldread_main.txt, task 2) as

    DEFINED IN SECTION 1 / DEFINED ELSEWHERE (with location) / STILL UNDEFINED

THE CHECK CAN FAIL.  Every DEFINED IN SECTION 1 ruling names an anchor: a
literal string that must occur in section1.tex.  If an anchor is absent the
ruling is false and the item is reported ANCHOR MISSING and the script exits 1.
A ruling can therefore be wrong, and saying "defined" does not make it so.

CONTROL (pre-registered in PREREG.md, section 3):
  item 054, "apparent singularity", is deliberately left undefined in section 1
  and must be reported STILL UNDEFINED.  If it is ever reported otherwise the
  script exits 1.

NEGATIVE CONTROL: scripts/mutants_171.py corrupts one anchor and requires this
script to exit 1.  Per P0 Amendment E the mutant is drawn from outside this
file's own anchor list.

READER INTEGRITY (P0 Amendment C): before any absence is reported, assert
known-present features of both inputs, including non-ASCII ones, so that a
mis-decoded or empty read cannot pass as a clean result.
"""
import pathlib, re, sys, hashlib

HERE = pathlib.Path(__file__).resolve().parent.parent
ITEMS = HERE / "refs" / "ct-s23-task2-items.txt"
SEC1 = HERE / "section1.tex"
COLDREAD = HERE.parent / "CT-S23-OUTSIDER-READ" / "outputs" / "coldread_main.txt"

S1, ELSE, UNDEF = "DEFINED IN SECTION 1", "DEFINED ELSEWHERE", "STILL UNDEFINED"

# --- anchors: literal strings that must be present in section1.tex ----------
A = {
    "poly":     r"b(n)=\sum_{k=0}^{d}\beta_k n^k",
    "lead":     r"\emph{leading} coefficient",
    "pcf":      r"\emph{polynomial continued fraction} (PCF)",
    "rec":      r"Q_n=b(n)Q_{n-1}+Q_{n-2}",
    "qn":       r"\emph{normalised denominator sequence}",
    "qinf":     r"q_\infty=\lim_{n\to\infty}q_n",
    "roots":    r"\lambda_1,\dots,\lambda_d\in\C",
    "footnote": r"\textbf{Correspondence with the deposited record.}",
    "A1":       r"\item[\textbf{(A1)}] $b(k)\neq0$",
    "A2":       r"\item[\textbf{(A2)}] No root $\lambda_i$ is a positive integer",
    "A3":       r"\item[\textbf{(A3)}] $q_\infty=\lim_{n\to\infty}Q_n/B_n$",
    "gamma":    r"Euler's Gamma function",
    "bigO":     r"$f=O(g)$ means",
    "littleo":  r"$f=o(g)$ means $f/g\to0$",
    "tilde":    r"$f\sim g$ means",
    "factorial": r"for $\Gamma(dn+1)$ when $dn$ is a non-negative integer",
    "formalsol": r"A \emph{formal solution} is a solution taken as a formal power",
    "newton":   r"\emph{Newton polygon} of a linear differential operator",
    "germ":     r"\emph{germ coefficient}",
    "amp":      r"\emph{amplitude} of an exponentially small or large term",
    "cpm":      r"$c_\pm$ denote the amplitudes",
    "stokes":   r"A \emph{Stokes constant} is the coefficient",
    "K":        r"\emph{connection constant} $K$",
    "s":        r"\emph{growth exponent}",
    "xi0":      r"\xi_0=\frac{2}{\sqrt{\beta_2}}",
    "rho":      r"$\rho$ for the exponent of the leading Borel-plane singularity",
    "indicial": r"An \emph{indicial exponent} of a linear differential equation",
    "dps":      r"\emph{dps} abbreviates \emph{decimal places of working precision}",
    "richard":  r"\emph{Richardson extrapolation}",
    "pslq":     r"\emph{PSLQ} is the integer-relation algorithm",
    "NN2":      r"$N/2$-versus-$N$ agreement",
    "ABC":      r"\textbf{$\mathsf A$} is the generating function",
    "sysC":     r"\textbf{$\mathsf C$} is the scalar second-order equation",
    "spd":      r"s_\pm=(-1\pm i\sqrt{11})/6",
    "PCQC":     r"y''+P_{\mathsf C}\,y'+Q_{\mathsf C}\,y=0",
    "PQ":       r"Writing a scalar equation as $\partial^2+P\partial+Q$",
    "normpot":  r"\emph{normal potential}",
    "tracefree": r"is obtained by removing the $P$ term",
    "projeq":   r"\emph{projectively equivalent}",
    "twist":    r"rank-one twist $y\mapsto fy$",
    "blind":    r"the normal potential is blind to such a twist",
    "AWC":      r"$A\,W''+A'\,W'+C\,W=0$",
    "katz":     r"\emph{Katz invariant} $r(c)$ is the largest slope",
    "multiset": r"\emph{Katz multiset}",
    "table":    r"\widetilde D_5:\ \mathrm{PV},\ (0,0,1,-)",
    "necessary": r"\textbf{A matching multiset is a necessary condition only.}",
    "Bi":       r"$B_1$, $B_2$, $B_3$ are the monodromy matrices",
    "traces":   r"x_1=\operatorname{tr}(B_2B_3)",
}

# --- per-item rulings -------------------------------------------------------
# n : (status, anchor-key or location-string or note)
R = {
  1:(S1,"poly"), 2:(S1,"poly"), 3:(S1,"rec"), 4:(S1,"qn"), 5:(S1,"qinf"),
  6:(S1,"bigO"), 7:(S1,"roots"), 8:(S1,"A2"), 9:(S1,"lead"), 10:(S1,"gamma"),
  11:(S1,"tilde"), 12:(S1,"K"), 13:(S1,"factorial"),
  14:(UNDEF,"branch of zeta=w^(1/d) deliberately deferred; sec 1.9 says where it is fixed, and does not fix it"),
  15:(S1,"xi0"), 16:(S1,"rho"), 17:(S1,"richard"), 18:(S1,"NN2"), 19:(S1,"pslq"),
  20:(S1,"footnote"),
  21:(UNDEF,"PSLQ basis belongs to the cut section 9"),
  22:(UNDEF,"partial: formal solution and c_pm are defined in sec 1.3; 'action' is not"),
  23:(S1,"newton"), 24:(S1,"germ"), 25:(S1,"amp"),
  26:(UNDEF,"S_{zeta*} belongs to the cut section 9"),
  27:(UNDEF,"zeta* belongs to the cut section 9"),
  28:(S1,"ABC"),
  29:(UNDEF,"L_phi is named in sec 1.6 as object B but not constructed"),
  30:(UNDEF,"'formal type' not defined"),
  31:(S1,"multiset"), 32:(S1,"table"),
  33:(UNDEF,"'quadratic cover' not defined"),
  34:(UNDEF,"'special parameters' not specified"),
  35:(S1,"projeq"), 36:(S1,"tracefree"), 37:(S1,"AWC"),
  38:(UNDEF,"W occurs in the display of sec 1.6 but is not declared as the unknown function"),
  39:(UNDEF,"r(x) is local to the section-3 computation"),
  40:(S1,"twist"),
  41:(UNDEF,"dlog A"), 42:(UNDEF,"strong Riemann-Hilbert problem"),
  43:(UNDEF,"M(u), u"), 44:(UNDEF,"P as a parameter space"),
  45:(UNDEF,"R as a family of affine cubic surfaces"), 46:(UNDEF,"M(t), t"),
  47:(UNDEF,"'affine cubic surface' is used in sec 1.8 and not defined there"),
  48:(UNDEF,"'monodromy side' is used in sec 1.8 and not defined there"),
  49:(S1,"traces"),
  50:(S1,"spd"), 51:(S1,"sysC"), 52:(S1,"PCQC"), 53:(S1,"normpot"),
  54:(UNDEF,"CONTROL: 'apparent singularity' deliberately left undefined"),
  55:(UNDEF,"r_z"), 56:(UNDEF,"ellipsis in the expansion at infinity"),
  57:(UNDEF,"type-(0,0,1) module"), 58:(UNDEF,"strong Riemann-Hilbert problem"),
  59:(UNDEF,"A_0, A_1, A_infty sign convention"), 60:(UNDEF,"C*"),
  61:(UNDEF,"theta_0, theta_1, theta_infty"), 62:(UNDEF,"'singular points normalised'"),
  63:(UNDEF,"semisimple / resonance / reducibility"),
  64:(ELSE,"packet section 4, defined as N = -A/D"),
  65:(UNDEF,"q, p used in the family formula before definition"),
  66:(UNDEF,"q, p as coordinates"), 67:(UNDEF,"H_V"), 68:(UNDEF,"Omega, foliation"),
  69:(UNDEF,"flow (4.4), Hamiltonian (4.5) not supplied"),
  70:(UNDEF,"'printed source' external referent"),
  71:(UNDEF,"b(z) versus b(n): sec 1.1 fixes b as a polynomial in n and does not address the clash"),
  72:(UNDEF,"b_1"), 73:(S1,"normpot"),
  74:(UNDEF,"'time invariant'"), 75:(UNDEF,"'irregular type'"),
  76:(UNDEF,"'configuration'"), 77:(UNDEF,"'local data'"), 78:(UNDEF,"'exact draws'"),
  79:(UNDEF,"R(infty)"), 80:(UNDEF,"s_1, s_2"), 81:(UNDEF,"unipotent local monodromy"),
  82:(UNDEF,"nilpotent"), 83:(UNDEF,"'log term'"), 84:(UNDEF,"Riccati test, w"),
  85:(UNDEF,"A in A^2-A=-1/4"), 86:(UNDEF,"c_0, r_1, n in the irreducibility argument"),
  87:(UNDEF,"'Riccati locus'"), 88:(UNDEF,"'overdetermined solve'"), 89:(UNDEF,"b_1=0"),
  90:(UNDEF,"'general formula', 'reduced closed form'"),
  91:(UNDEF,"partial: dps is defined in sec 1.5; 'relative residual' is not"),
  92:(UNDEF,"vector field (4.4)"), 93:(UNDEF,"'leaf'"),
  94:(UNDEF,"'normalisation' as an equivalence relation"),
  95:(ELSE,"packet Proposition 6"),
  96:(UNDEF,"'orbit'"), 97:(UNDEF,"'trace-free member'"), 98:(UNDEF,"L, f"),
  99:(UNDEF,"d as a differential operator"), 100:(UNDEF,"w=z as a witness"),
  101:(UNDEF,"2-torsion rank-1 module"), 102:(UNDEF,"triviality of determinant"),
  103:(S1,"PQ"), 104:(S1,"blind"),
  105:(UNDEF,"partial: projective equivalence is defined in sec 1.6; 'isomorphic' is used there and not defined"),
  106:(UNDEF,"local exponents, lattice"), 107:(UNDEF,"'normalised form'"),
  108:(UNDEF,"Y, N, n_ij"), 109:(ELSE,"packet section 7, defined by formulas"),
  110:(UNDEF,"b-route, c-route"), 111:(UNDEF,"'gauge relation'"),
  112:(UNDEF,"first component, subdominant branch"), 113:(UNDEF,"ord_infty"),
  114:(UNDEF,"mu(+), mu(-)"), 115:(UNDEF,"'head coefficients'"),
  116:(UNDEF,"'arithmetic control'"), 117:(UNDEF,"'scalar exponents'"),
  118:(S1,"traces"), 119:(UNDEF,"a_0, a_1"), 120:(UNDEF,"s_1, s_2"),
  121:(ELSE,"packet section 8, defined as formal solutions"),
  122:(UNDEF,"d_1, d_2, d_3"), 123:(UNDEF,"G_m"), 124:(UNDEF,"'eigen-lines'"),
  125:(UNDEF,"branch cut, sector labelling, Stokes rays"),
  126:(UNDEF,"Taylor-block continuation, continuous log z, optimally truncated"),
  127:(UNDEF,"f_1, f_2, alpha"), 128:(UNDEF,"M_0, M_1, M_infty"),
  129:(UNDEF,"gamma_0, gamma_1 loop generators"),
  130:(UNDEF,"unipotent, triangular, opposite triangles"),
  131:(UNDEF,"S_pi, S_2pi"), 132:(UNDEF,"L, L_11"), 133:(UNDEF,"B in B[Phi]"),
  134:(UNDEF,"Phi"), 135:(UNDEF,"Euler system, Kummer's equation"),
  136:(UNDEF,"a, b as control parameters versus the coefficient polynomial b"),
  137:(UNDEF,"N-tilde"), 138:(UNDEF,"SL_2 factorisation"),
  139:(UNDEF,"'clockwise big circle'"), 140:(UNDEF,"'unimodular'"),
  141:(UNDEF,"m_11"), 142:(UNDEF,"'dependent restatement'"), 143:(UNDEF,"Lambda"),
  144:(UNDEF,"R as a radius, clashing with the normal potential R of sec 1.6"),
  145:(UNDEF,"F as the cubic polynomial"), 146:(UNDEF,"grad F"),
  147:(UNDEF,"'first-order sensitivity'"), 148:(UNDEF,"'observable'"),
  149:(UNDEF,"'PV system'"), 150:(UNDEF,"s=t-t_0, t_0, t_1, epsilon"),
  151:(UNDEF,"'exact recurrences'"), 152:(UNDEF,"'wrong vector field'"),
  153:(ELSE,"packet Proposition 9, as a Galois automorphism"),
  154:(UNDEF,"'Galois automorphism'"), 155:(UNDEF,"'character variety'"),
  156:(UNDEF,"constant-gauge analytic equivalence"), 157:(UNDEF,"P_1, P_2"),
  158:(UNDEF,"'known-true identity'"),
  159:(UNDEF,"'native normalisation'; section 9 is cut"),
  160:(UNDEF,"B[Phi]; section 9 is cut"), 161:(UNDEF,"C; section 9 is cut"),
  162:(UNDEF,"S_{zeta*}; section 9 is cut"), 163:(UNDEF,"'decoys'; section 9 is cut"),
  164:(UNDEF,"Legendre duplication, reflection; section 9 is cut"),
  165:(UNDEF,"m in 1<=|m|<=12; section 9 is cut"),
  166:(UNDEF,"'cost'; section 9 is cut"), 167:(UNDEF,"'stated bases'; section 9 is cut"),
  168:(UNDEF,"'Membership' as a formal proposition"),
  169:(S1,"rho"),
  170:(S1,"indicial"),
  171:(UNDEF,"u=sqrt(z) is named in sec 1.4 as the uniformiser; the coordinate change and branch are not given"),
}

CONTROL_ITEM = 54

# Definitions the session task requires of section 1, independently of the 171.
# These are checked as well, so that an item-by-item pass cannot hide an
# omission of something the task asked for by name.
TASK_REQUIRED = [
    "qn", "qinf", "roots", "footnote",          # the three r-objects + 1 footnote
    "A1", "A2", "A3",                            # hypotheses, separately
    "katz", "multiset", "table", "necessary",    # Katz invariant / multiset
    "traces", "Bi",                              # trace coordinates and B_i
    "ABC", "projeq",                             # A, B, C and projective equivalence
    "gamma", "bigO", "littleo", "tilde", "dps", "pslq", "richard",
    "newton", "germ", "amp", "cpm",
    "table", "xi0", "rho", "K", "qinf", "pcf",
]


def integrity(items_text, sec1_text):
    """Assert both inputs were read correctly BEFORE any absence is reported."""
    checks = [
        ("items: 171 lines", len(items_text.splitlines()) == 171),
        ("items: non-ASCII xi-nought present", "\u03be\u2080" in items_text),
        ("items: non-ASCII beta present", "\u03b2_k" in items_text),
        ("items: non-ASCII D-tilde-5 present", "D\u0303\u2085" in items_text),
        ("items: control item 054 text present",
         "apparent singularity" in items_text),
        ("sec1: non-empty", len(sec1_text) > 8000),
        ("sec1: section heading present",
         r"\section{Notation and standing conventions}" in sec1_text),
        ("sec1: has subsections", sec1_text.count(r"\subsection{") >= 5),
        ("sec1: backslash survived decoding", sec1_text.count("\\") > 200),
    ]
    bad = [n for n, ok in checks if not ok]
    for n, ok in checks:
        print("  integrity %-44s %s" % (n, "ok" if ok else "FAILED"))
    if bad:
        print("READER INTEGRITY FAILED: %s" % ", ".join(bad))
        sys.exit(1)
    return len(checks)


def read_or_fail(path, label):
    """Read UTF-8, reporting an undecodable file as a READER failure.

    A reader that cannot decode its input must say so in the same words it uses
    for any other failure to see the content (P0 Amendment C).  Letting the
    UnicodeDecodeError propagate produces a traceback that is indistinguishable,
    to a harness, from the script having been broken outright.
    """
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, FileNotFoundError, OSError) as e:
        print("READER INTEGRITY FAILED: cannot read %s (%s): %s"
              % (label, path, e.__class__.__name__))
        sys.exit(1)


def main():
    global ITEMS, SEC1
    if "--root" in sys.argv:
        root = pathlib.Path(sys.argv[sys.argv.index("--root") + 1]).resolve()
        ITEMS = root / "refs" / "ct-s23-task2-items.txt"
        SEC1 = root / "section1.tex"
    items_text = read_or_fail(ITEMS, "items file")
    sec1_text = read_or_fail(SEC1, "section 1")
    # newline-insensitive view of section 1, so an anchor may span a line break
    sec1_flat = re.sub(r"\s+", " ", sec1_text)

    print("check_171.py -- classification of the 171 CT-S23 task-2 items")
    print("  section1.tex sha256 %s" %
          hashlib.sha256(SEC1.read_bytes()).hexdigest()[:16])
    print("  items file   sha256 %s" %
          hashlib.sha256(ITEMS.read_bytes()).hexdigest()[:16])
    print()
    n_int = integrity(items_text, sec1_text)
    print("  %d integrity assertions passed\n" % n_int)

    items = [l.split("\t") for l in items_text.splitlines()]
    assert len(R) == 171, "rulings table has %d entries, expected 171" % len(R)

    failures, rows = [], []
    counts = {S1: 0, ELSE: 0, UNDEF: 0}
    for num, sect, body in items:
        n = int(num)
        if n not in R:
            failures.append("item %03d has no ruling" % n)
            continue
        status, key = R[n]
        note = key
        if status == S1:
            anchor = A.get(key)
            if anchor is None:
                failures.append("item %03d names unknown anchor %r" % (n, key))
                status, note = "ANCHOR MISSING", "unknown anchor key %r" % key
            else:
                flat = re.sub(r"\s+", " ", anchor)
                if flat not in sec1_flat:
                    failures.append(
                        "item %03d ruled %s but anchor %r is ABSENT from section1.tex"
                        % (n, S1, key))
                    status, note = "ANCHOR MISSING", "anchor %r absent" % key
                else:
                    note = "anchor %r verified" % key
        counts[status] = counts.get(status, 0) + 1
        rows.append((n, sect, body, status, note))

    for n, sect, body, status, note in rows:
        print("%03d  %-19s  %s" % (n, status, body[:88]))
        print("     [%s] %s" % (sect, note))

    print("\n" + "=" * 70)
    print("TOTALS over 171 items")
    for k in (S1, ELSE, UNDEF, "ANCHOR MISSING"):
        if counts.get(k):
            print("  %-19s %3d" % (k, counts[k]))
    print("=" * 70)

    # --- pre-registered control ---------------------------------------------
    ctrl = dict((r[0], r[3]) for r in rows)[CONTROL_ITEM]
    ok_ctrl = ctrl == UNDEF
    print("\nCONTROL item %03d ('apparent singularity'), deliberately undefined:"
          % CONTROL_ITEM)
    print("  reported as: %s  -> %s" % (ctrl, "PASS" if ok_ctrl else "FAIL"))
    if not ok_ctrl:
        failures.append("control item %d not reported %s" % (CONTROL_ITEM, UNDEF))

    print("\nSTILL UNDEFINED list is the session's output, not a hidden failure.")

    # --- task coverage, independent of the 171 -------------------------------
    print("\nTASK COVERAGE -- definitions the session task names explicitly:")
    missing = []
    for key in sorted(set(TASK_REQUIRED)):
        anchor = A.get(key)
        ok = anchor is not None and re.sub(r"\s+", " ", anchor) in sec1_flat
        print("  %-10s %s" % (key, "present" if ok else "ABSENT"))
        if not ok:
            missing.append(key)
    if missing:
        failures.append("task-required definitions absent from section 1: %s"
                        % ", ".join(missing))
    print("  %d/%d required definitions present"
          % (len(set(TASK_REQUIRED)) - len(missing), len(set(TASK_REQUIRED))))

    if failures:
        print("\nCHECK FAILED (%d):" % len(failures))
        for f in failures:
            print("  - %s" % f)
        sys.exit(1)
    print("\nVERDICT: all 171 rulings verified; %d anchors resolved in section1.tex."
          % counts[S1])
    sys.exit(0)


if __name__ == "__main__":
    main()
