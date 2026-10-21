"""symbol_index.py -- symbol-collision index for the Channel Theory paper.

Ruling 1: "Report the index, not just the proposal -- the collisions are the
useful output."

SOURCES
  theorem.tex, section1.tex           (CT-S36-DRAFT-NOTATION)
  section3.tex, section4.tex          (CT-S37-DRAFT-B; an ADDITION to the
                                       instructed list, marked as such)
  OUTLINE.md                          (CT-S24-PAPER-OUTLINE, revision 6)
  the claim text of every claim id OUTLINE.md cites

EXTRACTION RULE, stated so a reader can judge it
  .tex sources: only MATH MODE is scanned ($..$, \\[..\\], \\(..\\), and the
    equation/align/gather families).  A token is a TeX control word
    (\\lambda, \\rho, ...) or a single Latin letter, optionally carrying a
    subscript.
  .md and claim texts: prose, so a single bare letter is NOT taken as a
    symbol.  A token must either carry a subscript (theta_0, q_n), or be a
    spelled greek name, or be a single letter immediately flanked by
    mathematical punctuation.  This is conservative by design: it under-reports
    rather than manufacturing meanings out of English.

Symbols are grouped by BASE letter, because a collision is a collision of
letters: q and q_n collide with the chart coordinate q alike.
"""
import collections, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
SESSIONS = HERE.parents[1]
assert SESSIONS.name == "sessions", SESSIONS

S36 = SESSIONS / "2026-09-17" / "CT-S36-DRAFT-NOTATION"
S37 = SESSIONS / "2026-09-17" / "CT-S37-DRAFT-B"
S24 = SESSIONS / "2026-09-17" / "CT-S24-PAPER-OUTLINE"

SOURCES = [
    ("theorem.tex",  S36 / "theorem.tex",  "tex", "instructed"),
    ("section1.tex", S36 / "section1.tex", "tex", "instructed"),
    ("OUTLINE.md",   S24 / "OUTLINE.md",   "prose", "instructed"),
    ("section3.tex", S37 / "section3.tex", "tex", "ADDED"),
    ("section4.tex", S37 / "section4.tex", "tex", "ADDED"),
]

MIN_BYTES = 1000
MIN_OCCURRENCES = 20

MATH = re.compile(
    r"\$\$(.+?)\$\$"
    r"|\$(.+?)\$"
    r"|\\\[(.+?)\\\]"
    r"|\\\((.+?)\\\)"
    r"|\\begin\{(?:equation|align|gather|multline)\*?\}(.+?)"
    r"\\end\{(?:equation|align|gather|multline)\*?\}",
    re.S)

SUB = r"(?:_\{[^{}]{0,24}\}|_[A-Za-z0-9\\]+)?"
TEX_TOKEN = re.compile(r"(\\[A-Za-z]+|(?<![A-Za-z\\])[A-Za-z](?![A-Za-z]))"
                       + SUB)

GREEK = ("alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu "
         "nu xi omicron pi rho sigma tau upsilon phi chi psi omega Gamma "
         "Delta Theta Lambda Sigma Phi Psi Omega varphi varrho varepsilon"
         ).split()
PROSE_TOKEN = re.compile(
    r"\b([A-Za-z]+)_(\{[^{}]{0,24}\}|[A-Za-z0-9+\-]+)"          # x_0, theta_inf
    r"|\b(" + "|".join(GREEK) + r")\b"                           # spelled greek
    r"|(?<=[=(^/~])\s*([A-Za-z])(?![A-Za-z])"                    # = q , (n
    r"|(?<![A-Za-z])([A-Za-z])(?=\s*[=^]\s*)"                    # q =
)

# TeX spacing / structural control words that are not symbols
NOT_SYMBOLS = set("""\\left \\right \\frac \\sqrt \\big \\Big \\bigl \\bigr
\\Bigl \\Bigr \\quad \\qquad \\text \\mathrm \\mathsf \\mathbb \\mathcal
\\operatorname \\emph \\textbf \\texttt \\label \\ref \\eqref \\cdot \\cdots
\\dots \\ldots \\pm \\mp \\to \\infty \\in \\neq \\le \\ge \\prod \\sum \\lim
\\int \\partial \\begin \\end \\displaystyle \\tfrac \\dfrac \\notag \\\\
\\ \\, \\; \\! \\colon \\mid \\times \\approx \\sim \\equiv \\subset \\cup
\\cap \\wedge \\vee \\mapsto \\longmapsto \\Rightarrow \\Longrightarrow
\\forall \\exists \\setminus \\bigl. \\phantom \\hspace \\medskip \\noindent
\\item \\paragraph \\section \\subsection \\begin{equation} \\nonumber
\\texorpdfstring \\qquad \\ne \\lvert \\rvert \\lVert \\rVert \\overline
\\widetilde \\tilde \\hat \\bar \\vec \\dot \\prime \\circ \\deg \\det \\dim
\\tr \\Re \\Im \\exp \\log \\sin \\cos \\max \\min \\sup \\inf \\arg
\\begin{align} \\end{align} \\end{equation} \\ensuremath \\newcommand""".split())

PROSE_STOPWORDS = set("""a i o e d s t n m k c b r p q u v w x y z f g h j l
A I O E""".split())


def read_or_fail(path, label):
    try:
        raw = path.read_bytes()
    except OSError as e:
        print("READER INTEGRITY FAILED: cannot read %s (%s): %s"
              % (label, path, e))
        sys.exit(2)
    try:
        return raw.decode("utf-8-sig").replace("\r\n", "\n")
    except UnicodeDecodeError as e:
        print("READER INTEGRITY FAILED: cannot decode %s: %s" % (label, e))
        sys.exit(2)


def ctx(text, a, b, width=62):
    lo, hi = max(0, a - width), min(len(text), b + width)
    return re.sub(r"\s+", " ", text[lo:hi]).strip()


def canon(tok, sub):
    """Canonical key and base letter."""
    sub = (sub or "").strip()
    sub = sub.strip("{}")
    base = tok
    key = base + ("_" + sub if sub else "")
    return key, base


def scan_tex(text):
    out = []
    for m in MATH.finditer(text):
        seg = next(g for g in m.groups() if g is not None)
        segoff = next(m.start(i + 1) for i, g in enumerate(m.groups())
                      if g is not None)
        for t in TEX_TOKEN.finditer(seg):
            tok = t.group(1)
            if tok in NOT_SYMBOLS or tok.startswith("\\begin") \
                    or tok.startswith("\\end"):
                continue
            whole = t.group(0)
            sub = whole[len(tok):].lstrip("_")
            key, base = canon(tok, sub)
            a = segoff + t.start()
            out.append((key, base, ctx(text, a, a + len(whole))))
    return out


def scan_prose(text):
    out = []
    for m in PROSE_TOKEN.finditer(text):
        if m.group(1):
            base, sub = m.group(1), m.group(2)
            if len(base) > 1 and base not in GREEK:
                continue
        elif m.group(3):
            base, sub = m.group(3), ""
        else:
            base = m.group(4) or m.group(5)
            sub = ""
            if base in PROSE_STOPWORDS and not re.search(
                    r"[=^]", text[m.end():m.end() + 3]):
                continue
        if base in GREEK:
            base = "\\" + base
        if base in NOT_SYMBOLS:
            # scan_tex consults NOT_SYMBOLS and scan_prose did not, so a token
            # excluded from the TeX reading was still admitted from prose.
            # The two readers must apply the same exclusion or the index
            # depends on which kind of source a symbol happens to occur in.
            continue
        key, base = canon(base, sub)
        out.append((key, base, ctx(text, m.start(), m.end())))
    return out


def outline_claim_texts():
    sys.path.insert(0, str(HERE.parent / "CT-S37-DRAFT-B" / "scripts"))
    import claim_index
    index, _d, _f, _b, _s = claim_index.build()
    outline = read_or_fail(S24 / "OUTLINE.md", "OUTLINE.md")
    cited = set()
    for m in re.finditer(r"(?:CT-)?S\d+[A-Z]*(?:-[A-Z0-9]+)+", outline):
        cid = m.group(0)
        if cid in index:
            cited.add(cid)
        elif "CT-" + cid in index:
            cited.add("CT-" + cid)
    blob = "\n".join(
        "%s: %s %s" % (c, index[c].get("claim", ""),
                       index[c].get("review_note", ""))
        for c in sorted(cited))
    return cited, blob


def build_index(verbose=True):
    """Scan every source and return (by_base, occ, per_source, sources).

    Exposed so that check_proposal.py screens candidate letters against the
    SAME index that is reported, rather than against a second, possibly
    divergent, reading of the corpus.
    """
    occ = collections.defaultdict(list)          # (base, key) -> [(src, ctx)]
    per_source = {}

    cited, blob = outline_claim_texts()
    sources = list(SOURCES) + [
        ("outline-cited claims (%d)" % len(cited), None, "prose", "instructed")]

    def say(*a):
        if verbose:
            print(*a)

    say("symbol_index -- Channel Theory symbol-collision index")
    say("\n[sources]")
    for label, path, kind, origin in sources:
        text = blob if path is None else read_or_fail(path, label)
        nb = len(text.encode("utf-8"))
        found = scan_tex(text) if kind == "tex" else scan_prose(text)
        if nb < MIN_BYTES:
            print("  READER INTEGRITY FAILED: %s is %d bytes (bound >= %d)"
                  % (label, nb, MIN_BYTES))
            sys.exit(2)
        if len(found) < MIN_OCCURRENCES:
            print("  READER INTEGRITY FAILED: %s yielded %d symbol "
                  "occurrences (bound >= %d)" % (label, len(found),
                                                 MIN_OCCURRENCES))
            sys.exit(2)
        per_source[label] = len(found)
        for key, base, c in found:
            occ[(base, key)].append((label, c))
        say("  %-28s %-6s %7d B  %5d occurrences   [%s]"
            % (label, kind, nb, len(found), origin))
        if not found:
            print("READER INTEGRITY FAILED: source %s contributed 0 symbol "
                  "occurrences. An empty or unreadable source is not the same "
                  "finding as a source with no collisions, and the index must "
                  "not report the second when it has the first." % label)
            sys.exit(4)

    by_base = collections.defaultdict(list)
    for (base, key), lst in occ.items():
        by_base[base].append((key, lst))

    # ---- vacuity pre-check, before any collision is reported ----
    say("\n[vacuity pre-check]")
    gsrc = {s for (k, l) in by_base.get("\\Gamma", []) for (s, _c) in l}
    bsrc = {s for (k, l) in by_base.get("B", []) for (s, _c) in l}
    bkeys = {k for (k, _l) in by_base.get("B", [])}
    ok_g = len(gsrc) >= 1
    ok_b = len(bkeys) >= 2 and len(bsrc) >= 2
    say("  control (one meaning) \\Gamma : %d keys in %d sources  %s"
        % (len(by_base.get("\\Gamma", [])), len(gsrc),
           "ok" if ok_g else "FAILED"))
    say("  control (two meanings) B     : %d keys in %d sources  %s"
        % (len(bkeys), len(bsrc), "ok" if ok_b else "FAILED"))
    if not (ok_g and ok_b):
        print("  VACUITY PRE-CHECK FAILED: the instrument cannot separate a "
              "one-meaning symbol from a two-meaning one; halting.")
        sys.exit(3)
    return by_base, occ, per_source, sources


def main():
    by_base, occ, per_source, sources = build_index(verbose=True)
    print("\n[index: every base letter, its keys, sources and contexts]")
    for base in sorted(by_base, key=lambda s: (s.startswith("\\"), s.lower())):
        entries = by_base[base]
        total = sum(len(l) for _k, l in entries)
        srcs = sorted({s for _k, l in entries for (s, _c) in l})
        print("\n  BASE %-12s %4d occurrences, %d keys, sources: %s"
              % (base, total, len(entries), ", ".join(srcs)))
        for key, lst in sorted(entries, key=lambda e: -len(e[1])):
            seen, shown = set(), 0
            print("    %-16s %3d" % (key, len(lst)))
            for s, c in lst:
                if s in seen or shown >= 3:
                    continue
                seen.add(s)
                shown += 1
                print("        [%s] %s" % (s, c[:150]))

    # ---- the free pool, which is what the proposal is drawn from ----
    used = set(by_base)
    latin = [chr(c) for c in range(ord("a"), ord("z") + 1)] + \
            [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    free_latin = [c for c in latin if c not in used]
    free_greek = ["\\" + g for g in GREEK if "\\" + g not in used]
    print("\n[free pool: base letters carrying NO meaning in any source]")
    print("  latin: %s" % " ".join(free_latin))
    print("  greek: %s" % " ".join(free_greek))

    print("\n[summary]")
    print("  sources scanned   : %d" % len(sources))
    print("  distinct bases    : %d" % len(by_base))
    print("  distinct keys     : %d" % len(occ))
    print("  occurrences       : %d" % sum(per_source.values()))
    multi = [b for b in by_base
             if len({s for _k, l in by_base[b] for (s, _c) in l}) >= 2
             and len(by_base[b]) >= 2]
    print("  bases with >=2 keys in >=2 sources (collision candidates): %d"
          % len(multi))
    print("  %s" % " ".join(sorted(multi, key=str.lower)))


if __name__ == "__main__":
    main()
