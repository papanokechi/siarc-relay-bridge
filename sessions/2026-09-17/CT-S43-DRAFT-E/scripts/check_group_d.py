"""check_group_d.py -- drafting gate for CT-S42-DRAFT-D (Group D, sections 7 and 8).

Rules, per PREREG.md sections 2-4:
  D0  reader integrity -- non-vacuity BOUNDS, never a fingerprint of the text
      under test (a fingerprint fires first and masks the check it precedes)
  D1  every cited id resolves in the corpus
  D2  no cited id is structurally superseded
  D3  every label asserted in the prose matches the corpus label
  D4  every significant numeric literal traces to a claim cited in the SAME
      subsection
  D5  non-vacuity floor on D4's NUMERATOR -- see below
  D6  the pre-declared transcription hazards are positively present
  D7  the build stub declares labels ONLY for sections that do not exist

D5 exists because of the defect the operator named in the CT-S41 review:
"a count printed as a fraction with zero numerator and a nonzero denominator
is the signature, and the fix is a non-vacuity assertion on the numerator
before printing."  CT-S41's own confirmation script printed 0/11 -- a count of
zero tests performed, rendered as a result.  Every counting reader here
asserts its numerator BEFORE printing it.

CENSUS AND FINGERPRINT (operator ruling, CT-S41 review question 1).
The corpus walk is a measurement over a LIVE tree.  This gate prints the
census AND a fingerprint -- a sha256 over the sorted list of walked paths --
and makes NO claim of byte-reproducibility across sessions.  A differing count
with a differing fingerprint is a different input, not a disagreement.

Normalisation for D4, declared here and not revised after any run:
  - significant literal := integer run of >= 3 digits, or a decimal, or a
    LaTeX scientific form  m\\times10^{-k}  /  10^{-k}
  - "m\\times10^{-k}" matches the claim-text form "me-k"
  - bare "10^{-k}"     matches the claim-text form "1e-k"
  - the pool for one subsection is the claim AND review_note fields of every
    claim cited in it.  Inherited from CT-S41's repair: reading claim alone
    produced a FALSE hit on a value that lived in a review_note.
D4 is a TRANSCRIPTION test.  It cannot see a value that is wrong in the
corpus, and it cannot see a transposition inside a numeral of fewer than three
digits.  No displayed formula is re-derived anywhere in this gate; see
PREREG.md section 6.
"""
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE / "scripts"))
import claim_index  # noqa: E402

LABELS = ("PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED", "CONJECTURED")
SECTIONS = ("section7.tex", "section8.tex")
STUB = "forwardrefs_E.tex"
ASSEMBLED = ["refs/section%d.tex" % i for i in range(7)] + list(SECTIONS)

LIT_FLOOR = 20
BYTE_FLOOR = 4000

failures = []
fired = []


def fail(rule, msg):
    failures.append("%s: %s" % (rule, msg))


def squash(s):
    return re.sub(r"\s+", " ", s)


def read_or_fail(p):
    try:
        return p.read_text(encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        print("READER INTEGRITY FAILED: cannot read %s: %s" % (p, e))
        raise SystemExit(2)


def subsections(text):
    marks = [(m.start(), m.group(1)) for m in
             re.finditer(r"\\label\{(ssec:[^}]+)\}", text)]
    out = []
    if marks:
        out.append(("<lead-in>", text[: marks[0][0]]))
    for i, (pos, name) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out.append((name, text[pos:end]))
    if not marks:
        out.append(("<whole>", text))
    return out


GAP = re.compile(r"^[\s,;()}{]*(and)?[\s,;()}{]*$")
ID_RE = re.compile(r"\\texttt\{((?:CT-)?S[0-9][^}]*)\}")
LAB_RE = re.compile(r"\\textbf\{(" + "|".join(LABELS) + r")\}")


def citations(body):
    s = squash(body)
    ids = [(m.start(), m.end(), m.group(1)) for m in ID_RE.finditer(s)]
    labs = [(m.start(), m.end(), m.group(1)) for m in LAB_RE.finditer(s)]
    out = []
    for a, b, cid in ids:
        asserted = None
        for la, lb, lab in labs:
            if lb <= a and GAP.match(s[lb:a]):
                asserted = lab
                break
            if la >= b and GAP.match(s[b:la]):
                asserted = lab
                break
        out.append((cid, asserted, a))
    return out


SCI = re.compile(r"(\d+(?:\.\d+)?)\s*\\times\s*10\^\{(-?\d+)\}")
BARE_SCI = re.compile(r"(?<!\\times)10\^\{(-?\d+(?:\.\d+)?)\}")
DEC = re.compile(r"\d+\.\d+")
BIGINT = re.compile(r"\d{3,}")


def literals(body):
    out, consumed = [], []
    for m in SCI.finditer(body):
        mant, exp = m.group(1), m.group(2)
        out.append((m.group(0), [mant + "e" + exp,
                                 mant + "e+" + exp.lstrip("+")]))
        consumed.append((m.start(), m.end()))
    for m in BARE_SCI.finditer(body):
        if any(a <= m.start() < b for a, b in consumed):
            continue
        out.append((m.group(0), ["1e" + m.group(1)]))
        consumed.append((m.start(), m.end()))
    for rx in (DEC, BIGINT):
        for m in rx.finditer(body):
            if any(a <= m.start() < b for a, b in consumed):
                continue
            out.append((m.group(0), [m.group(0)]))
    return out


# The hazards of PREREG.md section 5, as positive markers.  Each is a
# statement the prose MUST make; D6 fails if any is absent.
HAZARDS = {
    "S22-15 disclaimer": ("section8.tex",
                          "is not a proof of leaf membership"),
    "S22-20 not upgraded": ("section8.tex",
                            r"remains \textbf{VERIFIED}, on two independent runs"),
    "upgrade is about parameters": ("section8.tex",
                                    "not a statement about the Stokes data"),
    "not proved on the character variety": (
        "section8.tex",
        "thereby proved at the level of the character variety"),
    "S22-24 consequence": ("section8.tex", "not as structural"),
    "branch 2 was run": ("section8.tex", r"was \emph{run}, not inferred"),
    "sigma carries no monodromy": ("section8.tex",
                                   r"carries \emph{no} monodromy information"),
    "conventions selected not assumed": (
        "section7.tex", "not an input to it"),
    "S22-07 relied on nowhere": ("section7.tex",
                                 "Nothing\nin this paper rests on it"),
}


def run(texts, corpus, assembled):
    """texts: {filename: source} for the drafted files AND the stub."""
    global failures, fired
    failures, fired = [], []
    idx, _dupes, _nfiles, _bad, _sup = corpus

    # ---- D0 reader integrity: BOUNDS, never fingerprints
    for fn in SECTIONS:
        t = texts[fn]
        if len(t) < BYTE_FLOOR:
            fail("D0", "%s: %d bytes, below the %d-byte floor"
                 % (fn, len(t), BYTE_FLOOR))
        if t.count("\\subsection{") < 4:
            fail("D0", "%s: fewer than 4 subsections" % fn)
        if len(ID_RE.findall(t)) < 8:
            fail("D0", "%s: fewer than 8 claim citations" % fn)
    if len(idx) < 1000:
        fail("D0", "corpus index has only %d ids" % len(idx))

    # ---- D0b self-exclusion, asserted non-vacuously
    walked = [p.resolve() for p in claim_index.corpus_files()]
    if claim_index.SELF.resolve() in walked:
        fail("D0", "self-exclusion failed: this session's claims.jsonl is in "
                   "the corpus walk")
    fired.append("[self-exclusion] SELF present on disk: %s; absent from the "
                 "walk of %d files: True"
                 % (claim_index.SELF.exists(), len(walked)))

    seen = {}
    nlit = 0
    for fn in SECTIONS:
        for ssec, body in subsections(texts[fn]):
            cits = citations(body)
            claim_texts = []
            for cid, asserted, _ in cits:
                c = idx.get(cid)
                if c is None:                                   # D1
                    fail("D1", "%s %s: %s does not resolve" % (fn, ssec, cid))
                    continue
                claim_texts.append(str(c.get("claim", "")) + " " +
                                   str(c.get("review_note") or ""))
                seen.setdefault(cid, (asserted, c.get("label")))
                sup = [o for o in idx.values() if o.get("supersedes") == cid]
                if sup:                                         # D2
                    fail("D2", "%s %s: %s is superseded by %s"
                         % (fn, ssec, cid, sup[0].get("claim_id")))
                if asserted is not None and asserted != c.get("label"):
                    fail("D3", "%s %s: %s asserted %s, corpus says %s"
                         % (fn, ssec, cid, asserted, c.get("label")))
            pool = " ".join(claim_texts)
            if cits:                                            # D4
                for disp, forms in literals(body):
                    nlit += 1
                    if not any(f in pool for f in forms):
                        fail("D4", "%s %s: literal %r not found in the text "
                                   "of any claim cited here" % (fn, ssec, disp))

    # ---- D5 non-vacuity assertion on D4's NUMERATOR, before it is printed
    if nlit < LIT_FLOOR:
        fail("D5", "D4 inspected only %d literals, below the floor of %d -- "
                   "a count of zero tests is not a result" % (nlit, LIT_FLOOR))

    # ---- D6 hazards
    for name, (fn, needle) in HAZARDS.items():
        if squash(needle) not in squash(texts[fn]):
            fail("D6", "pre-declared hazard marker absent: %s" % name)

    # ---- D7 the stub may declare ONLY labels for sections that do not exist
    declared = re.findall(r"r@((?:sec|app):[A-Za-z0-9:_-]+)", texts[STUB])
    if not declared:
        fail("D5", "D7 found 0 declared stub labels -- nothing was tested")
    body_all = "\n".join(assembled.values())
    for lab in declared:
        if ("\\label{%s}" % lab) in body_all:
            fail("D7", "stub declares %s, but a section defines it: a stub "
                       "may declare only labels for sections that DO NOT "
                       "exist" % lab)

    return failures, seen, nlit, len(declared)


def corpus_fingerprint():
    """sha256 over the sorted list of walked paths.  Ruling 1: a census over a
    live tree is a measurement with a timestamp, so it is printed WITH a
    fingerprint and WITHOUT any claim of byte-reproducibility."""
    rel = sorted(str(p.relative_to(claim_index.ROOT)).replace("\\", "/")
                 for p in claim_index.corpus_files())
    return hashlib.sha256("\n".join(rel).encode("utf-8")).hexdigest(), len(rel)


def main():
    corpus = claim_index.build()
    texts = {fn: read_or_fail(HERE / fn) for fn in list(SECTIONS) + [STUB]}
    assembled = {fn: read_or_fail(HERE / fn) for fn in ASSEMBLED}

    fp, nfp = corpus_fingerprint()
    print("CT-S42-DRAFT-D :: Group D drafting gate")
    print("corpus census  : %d claims.jsonl files, %d unique ids"
          % (corpus[2], len(corpus[0])))
    print("corpus f/print : %s  (over %d sorted paths)" % (fp[:32], nfp))
    print("               : the census is a measurement over a LIVE tree.  A")
    print("               : differing count with a differing fingerprint is a")
    print("               : different input, not a disagreement.  NO claim of")
    print("               : byte-reproducibility across sessions is made.")
    for fn in SECTIONS:
        print("  %s: %d bytes" % (fn, len(texts[fn])))

    print("\n[treatment]")
    f, seen, nlit, ndecl = run(texts, corpus, assembled)
    nl = sum(1 for a, _ in seen.values() if a)
    print("  citations audited : %d distinct ids" % len(seen))
    print("  literals audited  : %d  (floor %d)" % (nlit, LIT_FLOOR))
    print("  stub labels tested: %d" % ndecl)
    print("  labelled in prose : %d" % nl)
    print("  bare citations    : %d" % (len(seen) - nl))
    print("  failures          : %d" % len(f))
    for line in fired:
        print("  " + line)
    for x in f:
        print("    " + x)
    treat_ok = not f

    # ------------------------------------------------ control arms
    print("\n[arms] each mutates a COPY; the rule must fire for the right "
          "reason, and each arm asserts its mutation site EXISTS first")
    arms = []

    def arm(name, rule, mutate):
        t2 = dict(texts)
        a2 = dict(assembled)
        got = mutate(t2, a2)
        if got is None:
            arms.append((name, rule, "SKIPPED (mutation site absent)", False))
            return
        try:
            f2, _, _, _ = run(t2, corpus, a2)
        except SystemExit:
            arms.append((name, rule, "reader refused", rule == "D0"))
            return
        hit = [x for x in f2 if x.startswith(rule + ":")]
        arms.append((name, rule, "%d failures, %d on %s"
                     % (len(f2), len(hit), rule), bool(hit)))

    def sub(fn, old, new):
        def m(t, a):
            if old not in t[fn]:
                return None
            t[fn] = t[fn].replace(old, new, 1)
            if fn in a:
                a[fn] = t[fn]
            return True
        return m

    arm("D1 unresolvable id", "D1",
        sub("section7.tex", r"\texttt{S22-09}", r"\texttt{S22-99}"))
    arm("D2 superseded id", "D2",
        sub("section7.tex", r"\texttt{S22-13}", r"\texttt{S1-04}"))
    arm("D3 THE wrong label (S22-15 -> PROVEN)", "D3",
        sub("section8.tex",
            r"\texttt{S22-15}, \textbf{VERIFIED}]",
            r"\texttt{S22-15}, \textbf{PROVEN}]"))
    arm("D3b STRUCTURAL asserted PROVEN", "D3",
        sub("section7.tex",
            r"\texttt{S22-01}, \textbf{VERIFIED}]",
            r"\texttt{S22-01}, \textbf{PROVEN}]"))
    arm("D4 transposed digit", "D4",
        sub("section7.tex", "0.60459978807807261686",
            "0.60459978807807261868"))
    arm("D4b wrong exponent", "D4",
        sub("section8.tex", r"3.83\times10^{-2}", r"3.83\times10^{-5}"))

    def strip_cits(t, a):
        n = 0
        for fn in SECTIONS:
            t[fn], k = ID_RE.subn("XX", t[fn])
            a[fn] = t[fn]
            n += k
        return True if n else None
    arm("D5 literal pool emptied", "D5", strip_cits)

    arm("D6 hazard deleted", "D6",
        sub("section8.tex", "is not a proof of leaf membership",
            "is a proof of leaf membership"))
    # NOTE: arms mutate RAW text while the rules compare SQUASHED text, so an
    # arm needle that straddles a line break cannot reach its site.  The first
    # run of this gate reported exactly that, as SKIPPED rather than MISSED.
    arm("D6b scope sentence deleted", "D6",
        sub("section8.tex", "the Stokes data, which is transcendental",
            "the Stokes matrices, which are transcendental"))

    def stub_overreach(t, a):
        if r"r@sec:limits" not in t[STUB]:
            return None
        t[STUB] = t[STUB].replace(
            r"\expandafter\gdef\csname r@sec:limits\endcsname",
            "\\expandafter\\gdef\\csname r@sec:monodromy\\endcsname{{7}{1}{}"
            "{section.7}{}}\n\\expandafter\\gdef\\csname r@sec:limits"
            "\\endcsname", 1)
        return True
    arm("D7 stub re-declares a live label", "D7", stub_overreach)

    def truncate(t, a):
        if len(t["section7.tex"]) < BYTE_FLOOR:
            return None
        t["section7.tex"] = t["section7.tex"][:100]
        a["section7.tex"] = t["section7.tex"]
        return True
    arm("D0 section truncated below floor", "D0", truncate)

    caught = 0
    for name, rule, detail, ok in arms:
        print("  %s %-42s [%s] %s"
              % ("CAUGHT " if ok else "MISSED ", name, rule, detail))
        caught += bool(ok)
    print("\n  arms: %d/%d CAUGHT" % (caught, len(arms)))

    print("\n" + "=" * 62)
    ok = treat_ok and caught == len(arms)
    print("GATE: %s" % ("PASSED" if ok else "FAILED"))
    print("checks run    : %d citations, %d literals, %d stub labels"
          % (len(seen), nlit, ndecl))
    print("checks failed : %d" % len(f))
    print("arms caught   : %d/%d" % (caught, len(arms)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
