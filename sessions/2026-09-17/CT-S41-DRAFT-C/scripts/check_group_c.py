"""check_group_c.py -- drafting gate for CT-S41-DRAFT-C (Group C, section 5 and 6).

Rules, per PREREG.md:
  C1 reader integrity (non-vacuity BOUNDS, not fingerprints of the text)
  C2 every cited id resolves in the corpus
  C3 no cited id is structurally superseded
  C4 every label asserted in the prose matches the corpus label
  C5 every significant numeric literal traces to a claim cited in the SAME
     subsection
  C6 the two pre-declared transcription hazards are positively present

Every rule is exercised by an in-memory ARM that mutates the drafted text and
requires the rule to fire FOR THE RIGHT REASON.  The arms are run on copies;
the files on disk are never modified.

Normalisation rules for C5, declared here and not revised after any run:
  - significant literal := integer run of >= 3 digits, or a decimal, or a
    LaTeX scientific form  m\\times10^{-k}  / 10^{-k}
  - "m\\times10^{-k}"  matches the claim-text form  "me-k"
  - bare "10^{-k}"      matches the claim-text form "1e-k"
  - the pool for one subsection is the claim AND eview_note fields of
    every claim cited in it; the first run of this gate used claim only and
    reported a FALSE C5 hit on 1e-3, which lives in S17-04's note
  - comparison is on literal digit strings; no rounding, no tolerance
C5 is a TRANSCRIPTION test.  It cannot see a value that is wrong in the corpus,
and it cannot see a transposition inside a numeral of fewer than three digits.
"""
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE / "scripts"))
import claim_index  # noqa: E402

LABELS = ("PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED", "CONJECTURED")
SECTIONS = ("section5.tex", "section6.tex")

failures = []
fired = []


def fail(rule, msg):
    failures.append(f"{rule}: {msg}")
    print(f"  FAIL {rule}: {msg}")


def squash(s):
    return re.sub(r"\s+", " ", s)


# ---------------------------------------------------------------- readers
def read_or_fail(p):
    try:
        return p.read_text(encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        print(f"READER INTEGRITY FAILED: cannot read {p}: {e}")
        raise SystemExit(2)


def subsections(text):
    """[(name, body)] -- body of each \\subsection, plus a lead-in block."""
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


# ------------------------------------------------------- citation parsing
GAP = re.compile(r"^[\s,;()}{]*(and)?[\s,;()}{]*$")
ID_RE = re.compile(r"\\texttt\{((?:CT-)?S[0-9][^}]*)\}")
LAB_RE = re.compile(r"\\textbf\{(" + "|".join(LABELS) + r")\}")


def citations(body):
    """[(id, asserted_label_or_None, pos)] for one subsection body."""
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


# ------------------------------------------------------- numeric literals
SCI = re.compile(r"(\d+(?:\.\d+)?)\s*\\times\s*10\^\{(-?\d+)\}")
BARE_SCI = re.compile(r"(?<!\\times)10\^\{(-?\d+)\}")
DEC = re.compile(r"\d+\.\d+")
BIGINT = re.compile(r"\d{3,}")


def literals(body):
    """[(display, [acceptable claim-text forms])]"""
    out = []
    consumed = []
    for m in SCI.finditer(body):
        mant, exp = m.group(1), m.group(2)
        out.append((m.group(0), [mant + "e" + exp, mant + "e+" + exp.lstrip("+")]))
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


# ============================================================ the gate
def run(texts, corpus, quiet=False):
    """texts: {filename: source}.  Returns (failures, report_lines)."""
    global failures, fired
    failures, fired = [], []
    idx, dupes, nfiles, _, _ = corpus

    # ---- C1 reader integrity: BOUNDS, never fingerprints
    for fn, t in texts.items():
        if len(t) < 4000:
            fail("C1", f"{fn}: {len(t)} bytes, below the 4000-byte floor")
        if t.count("\\subsection{") < 4:
            fail("C1", f"{fn}: fewer than 4 subsections")
        if len(ID_RE.findall(t)) < 8:
            fail("C1", f"{fn}: fewer than 8 claim citations")
    if len(idx) < 1000:
        fail("C1", f"corpus index has only {len(idx)} ids")

    # ---- C1b self-exclusion, asserted non-vacuously.  This gate's output is
    # cited by this session's claims, and this session writes a claims.jsonl
    # into the corpus the index walks.  If SELF were walked, every cited
    # digest would go stale the moment the gate ran again (the CT-S34
    # ordering defect).  Excluded by construction; asserted here.
    walked = [p.resolve() for p in claim_index.corpus_files()]
    self_exists = claim_index.SELF.exists()
    if claim_index.SELF.resolve() in walked:
        fail("C1", "self-exclusion failed: this session's claims.jsonl is in "
                   "the corpus walk")
    fired.append(f"[self-exclusion] SELF present on disk: {self_exists}; "
                 f"absent from the walk of {len(walked)} files: True")

    seen = {}
    nlit = [0]
    for fn, t in texts.items():
        for ssec, body in subsections(t):
            cits = citations(body)
            claim_texts = []
            for cid, asserted, _ in cits:
                c = idx.get(cid)

                # ---- C2 resolution
                if c is None:
                    fail("C2", f"{fn} {ssec}: {cid} does not resolve")
                    continue
                claim_texts.append(c.get("claim", "") + " " +
                                   str(c.get("review_note") or ""))
                seen.setdefault(cid, (asserted, c.get("label")))

                # ---- C3 supersession
                sup = [o for o in idx.values()
                       if o.get("supersedes") == cid]
                if sup:
                    fail("C3", f"{fn} {ssec}: {cid} is superseded by "
                               f"{sup[0].get('claim_id')}")

                # ---- C4 label
                if asserted is not None and asserted != c.get("label"):
                    fail("C4", f"{fn} {ssec}: {cid} asserted {asserted}, "
                               f"corpus says {c.get('label')}")

            # ---- C5 numeric traceability
            pool = " ".join(claim_texts)
            if cits:
                for disp, forms in literals(body):
                    nlit[0] += 1
                    if not any(f in pool for f in forms):
                        fail("C5", f"{fn} {ssec}: literal {disp!r} not found "
                                   f"in the text of any claim cited here")

    # ---- C6 the two pre-declared hazards, positively present
    s5 = squash(texts.get("section5.tex", ""))
    haz = {
        "theta_inf sign": r"-2\mp\sqrt3/9",
        "the +1 shift": "the $+1$ being the shift",
        "naive entry named": r"t\,\theta_\infty/2",
        "field named": r"K=\mathbb Q\bigl(i\sqrt{11}\bigr)",
        "sqrt3 not adjoined": "generated} by the answer",
        "gauge not closed": "does \\emph{not} close the $z$-dependent gauge",
    }
    for name, needle in haz.items():
        if squash(needle) not in s5:
            fail("C6", f"pre-declared hazard marker absent: {name}")

    # ---- C5 non-vacuity: the literal test must have inspected something
    if nlit[0] < 20:
        fail("C1", f"C5 inspected only {nlit[0]} literals, below the floor of 20")

    return failures, seen, nlit[0]


def main():
    corpus = claim_index.build()
    texts = {fn: read_or_fail(HERE / fn) for fn in SECTIONS}

    print("CT-S41-DRAFT-C :: Group C drafting gate")
    print(f"corpus: {corpus[2]} files, {len(corpus[0])} ids")
    for fn, t in texts.items():
        print(f"  {fn}: {len(t)} bytes, sha256 "
              f"{hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]}")
    print("\n[treatment]")
    f, seen, nlit = run(texts, corpus)
    print(f"  citations audited : {len(seen)} distinct ids")
    print(f"  literals audited  : {nlit}")
    nl = sum(1 for a, _ in seen.values() if a)
    print(f"  labelled in prose : {nl}")
    print(f"  bare citations    : {len(seen) - nl}")
    print(f"  failures          : {len(f)}")
    for line in fired:
        print("  " + line)
    for x in f:
        print("   ", x)
    treat_ok = not f

    # ------------------------------------------------ control arms
    print("\n[arms] each mutates a COPY; the rule must fire for the right reason")
    arms = []

    def arm(name, rule, mutate):
        t2 = {k: v for k, v in texts.items()}
        t2 = mutate(t2)
        if t2 is None:
            arms.append((name, rule, "SKIPPED (mutation site absent)", False))
            return
        try:
            f2, _, _ = run(t2, corpus)
        except SystemExit:
            arms.append((name, rule, "reader refused", rule == "C1"))
            return
        hit = [x for x in f2 if x.startswith(rule + ":")]
        arms.append((name, rule, f"{len(f2)} failures, {len(hit)} on {rule}",
                     bool(hit)))

    def sub(fn, old, new):
        def m(t):
            if old not in t[fn]:
                return None
            t[fn] = t[fn].replace(old, new, 1)
            return t
        return m

    arm("A-control  wrong label", "C4",
        sub("section5.tex", r"(\texttt{S16-07}, \textbf{PROVEN})",
            r"(\texttt{S16-07}, \textbf{VERIFIED})"))
    arm("A-control2 PROVEN for STRUCTURAL", "C4",
        sub("section5.tex", r"\textbf{STRUCTURAL} (\texttt{S16-14})",
            r"\textbf{PROVEN} (\texttt{S16-14})"))
    arm("A-numeric  transposed digit", "C5",
        sub("section5.tex", "5.79877", "5.97877"))
    arm("A-numeric2 wrong exponent", "C5",
        sub("section6.tex", r"4.8\times10^{-61}", r"4.8\times10^{-16}"))
    arm("A-unres    bad id", "C2",
        sub("section6.tex", r"\texttt{S17-04}", r"\texttt{S17-99}"))
    arm("A-super    superseded id", "C3",
        sub("section5.tex", r"\texttt{S16-13}", r"\texttt{S1-04}"))
    arm("A-hazard   field un-named", "C6",
        sub("section5.tex", r"K=\mathbb Q\bigl(i\sqrt{11}\bigr)",
            r"K=\mathbb Q\bigl(\sqrt3,\sqrt{11}\bigr)"))
    arm("A-hazard2  gauge claim dropped", "C6",
        sub("section5.tex", "does \\emph{not} close the $z$-dependent gauge",
            "closes the $z$-dependent gauge"))
    def truncate(fn):
        def m(t):
            t[fn] = t[fn][:100]
            return t
        return m

    arm("A-bounds   section emptied", "C1", truncate("section6.tex"))

    caught = 0
    for name, rule, detail, ok in arms:
        print(f"  {'CAUGHT ' if ok else 'MISSED '} {name:32s} [{rule}] {detail}")
        caught += bool(ok)
    print(f"\n  arms: {caught}/{len(arms)} CAUGHT")

    print("\n" + "=" * 62)
    ok = treat_ok and caught == len(arms)
    print(f"GATE: {'PASSED' if ok else 'FAILED'}")
    print(f"checks run    : {len(seen)} citations across {len(SECTIONS)} files")
    print(f"checks failed : {len(f)}")
    print(f"arms caught   : {caught}/{len(arms)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
