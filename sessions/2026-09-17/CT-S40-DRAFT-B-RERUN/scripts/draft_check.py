"""draft_check.py -- Group B draft check (CT-S37-DRAFT-B).

Reads the drafted sections, extracts every (claim id, asserted label) pair, and
checks each against the corpus index built by claim_index.py.

The check FAILS (exit 1) if any cited id is UNRESOLVED, structurally
SUPERSEDED, or carries a label in the prose that differs from the label the
corpus record carries.

The 'CT-' prefix alias that CT-S37 used to resolve the short form has been
REMOVED (operator ruling; claim S39-08).  A bare short form is now UNRESOLVED
and fails.  Where the retired alias WOULD have resolved it, that is printed as
a diagnostic on the failing row -- so the removal is visible in the output
rather than silent -- but it does not resolve the citation.

Reader integrity is asserted FIRST, as bounds rather than fingerprints, so that
an empty or undecodable read cannot be reported as '0 problems' and so that a
legitimate edit to the prose cannot fire the guard before the pairs are
examined.
"""
import pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import claim_index

HERE = pathlib.Path(__file__).resolve().parent.parent
SECTIONS = ["section3.tex", "section4.tex"]
REFS = HERE / "refs"
OUTLINE = (HERE.parent / "CT-S24-PAPER-OUTLINE" / "OUTLINE.md")
# Set by the M12 arm to stage the stale CT-S37 copy of section1 in place of the
# repaired one.  Default: the repaired file.
SECTION1 = REFS / "section1.tex"
SECTION1_STALE = REFS / "section1.CT-S37.tex"

LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}
SENTINEL = "\u00e9 \u00f6 \u00b1"

CID = re.compile(r"(?:CT-)?S\d+[A-Z]*(?:-[A-Z0-9]+)+")
TOKEN = re.compile(r"\\textbf\{([A-Z]+)\}|\\texttt\{([^{}]+)\}")

MIN_BYTES = 4000
MIN_SUBSECTIONS = 4
# Pre-registered at 15 per file.  That value proved ILL-POSED: section4.tex
# genuinely carries 12 citations, so a bound of 15 fired on correct prose,
# which is the fingerprint failure the bound exists to avoid.  Narrowed
# post-hoc to 5 per file plus 30 across the group; both the original value and
# the reason are recorded in PREREG.md (amendment) and REPORT.md, and mutant
# arm 9 is the boundary mutant added in the same edit.
MIN_PAIRS = 5
MIN_PAIRS_TOTAL = 30


def read_or_fail(path):
    """Return text, or abort loudly.  An unreadable file is a reader failure,
    never an absence of findings."""
    try:
        raw = path.read_bytes()
    except OSError as e:
        print("READER INTEGRITY FAILED: cannot read %s: %s" % (path, e))
        sys.exit(2)
    try:
        return raw.decode("utf-8-sig").replace("\r\n", "\n")
    except UnicodeDecodeError as e:
        print("READER INTEGRITY FAILED: cannot decode %s: %s" % (path, e))
        sys.exit(2)


def extract(text):
    """(claim id, asserted label) pairs.  The asserted label is the nearest
    PRECEDING \\textbf{LABEL} whose content is in the label vocabulary; a
    \\textbf{} that is not a label (e.g. \\textbf{not}) is ignored."""
    pairs, current = [], None
    for m in TOKEN.finditer(text):
        bold, tt = m.group(1), m.group(2)
        if bold is not None:
            if bold in LABELS:
                current = bold
            continue
        tt = tt.strip()
        if CID.fullmatch(tt):
            pairs.append((tt, current, m.start()))
    return pairs


def structured_supersession(index):
    """Only structured fields.  A claim whose free text merely MENTIONS
    superseding something is not superseded by that mention."""
    hard = {}
    for cid, c in index.items():
        for key in ("superseded_by", "replaced_by"):
            if c.get(key):
                hard[cid] = "%s: %s" % (key, c[key])
        for key in ("supersedes", "replaces"):
            v = c.get(key)
            if v:
                for other in re.findall(r"[A-Z0-9]+-[A-Z0-9\-]*\d+", str(v)):
                    hard.setdefault(other, "superseded by %s (%s)" % (cid, key))
    return hard


def main():
    index, _dupes, nfiles, bad, _loose = claim_index.build()
    hard = structured_supersession(index)

    print("draft_check (CT-S37-DRAFT-B, Group B: sections 3 and 4)")
    print("corpus: %d claims.jsonl files, %d unique claim ids, %d unparseable "
          "lines (pre-existing, out of scope)" % (nfiles, len(index), len(bad)))

    # ---- reader integrity, asserted BEFORE any count is reported ----
    print("\n[reader integrity]")
    texts = {}
    for name in SECTIONS:
        p = HERE / name
        t = read_or_fail(p)
        texts[name] = t
        nb = len(t.encode("utf-8"))
        nsub = t.count("\\subsection{")
        pairs = extract(t)
        fails = []
        if SENTINEL not in t:
            fails.append("non-ASCII sentinel %r absent" % SENTINEL)
        if nb < MIN_BYTES:
            fails.append("only %d bytes (bound: >= %d)" % (nb, MIN_BYTES))
        if nsub < MIN_SUBSECTIONS:
            fails.append("only %d subsections (bound: >= %d)"
                         % (nsub, MIN_SUBSECTIONS))
        if len(pairs) < MIN_PAIRS:
            fails.append("only %d (id,label) pairs (bound: >= %d)"
                         % (len(pairs), MIN_PAIRS))
        if fails:
            print("  READER INTEGRITY FAILED for %s:" % name)
            for f in fails:
                print("    - " + f)
            sys.exit(2)
        print("  %-14s %6d bytes, %d subsections, %d (id,label) pairs  OK"
              % (name, nb, nsub, len(pairs)))

    grand = sum(len(extract(texts[n])) for n in SECTIONS)
    if grand < MIN_PAIRS_TOTAL:
        print("  READER INTEGRITY FAILED: %d (id,label) pairs across the group "
              "(bound: >= %d)" % (grand, MIN_PAIRS_TOTAL))
        sys.exit(2)
    print("  group total    %6d (id,label) pairs (bound: >= %d)  OK"
          % (grand, MIN_PAIRS_TOTAL))

    # ---- the check proper ----
    counts = {"OK": 0, "UNRESOLVED": 0, "SUPERSEDED": 0, "MISMATCH": 0,
              "NOLABEL": 0}
    would_alias, warn_text_superseded, rows = [], [], []

    for name in SECTIONS:
        for cid, asserted, _pos in extract(texts[name]):
            rec = index.get(cid)
            if rec is None:
                # Diagnostic only.  The retired CT- alias does NOT resolve it.
                note = "no such claim id in the corpus"
                if not cid.startswith("CT-") and index.get("CT-" + cid):
                    would_alias.append((name, cid, "CT-" + cid))
                    note += ("; the retired CT- alias would have resolved it "
                             "as CT-%s" % cid)
                counts["UNRESOLVED"] += 1
                rows.append((name, cid, asserted, "-", "UNRESOLVED", note))
                continue
            key = cid
            corpus = rec.get("label", "?")
            if key in hard:
                counts["SUPERSEDED"] += 1
                rows.append((name, cid, asserted, corpus, "SUPERSEDED",
                             hard[key]))
                continue
            txt = (str(rec.get("claim", "")) + " "
                   + str(rec.get("review_note", ""))).lower()
            if any(w in txt for w in ("superseded", "withdrawn", "retracted")):
                warn_text_superseded.append((name, cid))
            if asserted is None:
                counts["NOLABEL"] += 1
                rows.append((name, cid, "(none)", corpus, "MISMATCH",
                             "no label asserted in the prose"))
                counts["MISMATCH"] += 1
                continue
            if asserted != corpus:
                counts["MISMATCH"] += 1
                rows.append((name, cid, asserted, corpus, "MISMATCH",
                             "prose says %s, corpus says %s"
                             % (asserted, corpus)))
            else:
                counts["OK"] += 1
                rows.append((name, cid, asserted, corpus, "OK", ""))

    print("\n[citations]")
    print("  %-14s %-24s %-12s %-12s %-11s %s"
          % ("file", "claim id", "prose", "corpus", "verdict", "note"))
    for r in rows:
        print("  %-14s %-24s %-12s %-12s %-11s %s" % r)

    fired = []
    print("\n[alias removal]")
    print("  the CT- prefix alias is RETIRED; a bare short form is UNRESOLVED.")
    if would_alias:
        for name, cid, alias in would_alias:
            print("  %s cites %s, which the retired alias would have resolved "
                  "as %s -- now failed, not normalised." % (name, cid, alias))
    else:
        print("  no citation in the group needed it: every id is cited in the "
              "corpus form, so the removal is a no-op on this prose.")

    # F5: the NOTE that used to stand here asserted that OUTLINE.md cites this
    # family as S9-PVPARAMS-*.  CT-S38 fixed the outline, so that sentence is
    # now FALSE and has been removed.  Its replacement is a CHECK, positively
    # resolved against the outline itself rather than a remembered fact.
    print("\n[outline citation form]")
    if not OUTLINE.exists():
        print("  READER INTEGRITY FAILED: outline not found at %s" % OUTLINE)
        sys.exit(2)
    otext = read_or_fail(OUTLINE)
    pv_all = re.findall(r"(CT-)?S9-PVPARAMS-", otext)
    bare = [m for m in pv_all if not m]
    if not pv_all:
        print("  READER INTEGRITY FAILED: no S9-PVPARAMS citation of either "
              "form in the outline; the check cannot be non-vacuous")
        sys.exit(2)
    print("  OUTLINE.md: %d occurrences of the PVPARAMS family, %d bare "
          "(threshold: 0)" % (len(pv_all), len(bare)))
    if bare:
        fired.append("F5: the outline still cites the bare short form")
        print("  F5 FIRED: the outline still cites the bare short form; the "
              "alias removal would break it.")
    else:
        print("  all in the corpus form CT-S9-PVPARAMS-*  OK")

    # F4 / M12: section 1 is an INPUT that changed under CT-S37's feet.  Assert
    # the repaired file positively -- by CONTENT, not by path (S38-07) -- and
    # TWO-SIDED: the stale snapshot must still carry the pre-repair sentences,
    # or "differs from the stale copy" is a statement about a file that is no
    # longer the thing it is named for.  Matching is on whitespace-squashed
    # text because every one of these sentences spans a line break in the
    # source; a raw containment test reports a FALSE ABSENCE (CT-S39, F6c).
    print("\n[section 1 provenance: two-sided, on squashed text]")
    s1 = read_or_fail(SECTION1)
    if not SECTION1_STALE.exists():
        print("  READER INTEGRITY FAILED: the CT-S37 snapshot is absent, so "
              "the comparison has nothing to resolve against")
        sys.exit(2)
    stale = read_or_fail(SECTION1_STALE)
    sq = lambda t: re.sub(r"\s+", " ", t)
    s1q, stq = sq(s1), sq(stale)
    PRE = [("rho sentence", "The letter $\\rho$ is never used for anything else"),
           ("lambda roots", "\\lambda_1,\\dots,\\lambda_d\\in\\C"),
           ("q_infty", "q_\\infty=\\lim_{n\\to\\infty}q_n")]
    POST = [("rho two meanings", "the letter $\\rho$ carries two meanings"),
            ("nu roots", "\\nu_1,\\dots,\\nu_d\\in\\C"),
            ("psi_infty", "\\psi_\\infty=\\lim_{n\\to\\infty}\\psi_n"),
            ("s vs s_pm", "The unsubscripted letter $s$ always denotes"),
            ("P,Q vs Q_n", "are a different object from the denominators")]
    for desc, needle in PRE:
        a, b = needle in stq, needle in s1q
        ok = a and not b
        print("  pre-repair  %-18s stale:%-5s live:%-5s  %s"
              % (desc, a, b, "OK" if ok else "FIRED"))
        if not ok:
            fired.append("F4: pre-repair marker %r %s" % (
                desc, "absent from the snapshot" if not a
                else "still present in the live file"))
    for desc, needle in POST:
        a, b = needle in s1q, needle in stq
        ok = a and not b
        print("  repair      %-18s live:%-5s stale:%-5s  %s"
              % (desc, a, b, "OK" if ok else "FIRED"))
        if not ok:
            fired.append("F4: repair marker %r %s" % (
                desc, "absent from the live file" if not a
                else "already in the snapshot"))
    if s1 == stale:
        fired.append("F4: section 1 is the stale CT-S37 copy")
        print("  F4 FIRED: refs/section1.tex is byte-identical to the stale "
              "CT-S37 copy; the re-run is reading the file it exists to replace.")

    print("\n[labels borrowed by sections 3 and 4]")

    s1_labels = set(re.findall(r"\\label\{([^{}]+)\}", s1))
    s2_labels = set(re.findall(r"\\label\{([^{}]+)\}",
                               read_or_fail(REFS / "section2.tex")))
    own = set()
    for name in SECTIONS:
        own |= set(re.findall(r"\\label\{([^{}]+)\}", texts[name]))
    used = set()
    for name in SECTIONS:
        used |= set(re.findall(r"\\(?:ref|eqref|Cref|cref)\{([^{}]+)\}",
                               texts[name]))
    borrowed = sorted(used - own)
    missing = [t for t in borrowed if t not in s1_labels | s2_labels]
    for t in borrowed:
        where = ("section1" if t in s1_labels else
                 "section2" if t in s2_labels else "NOWHERE")
        print("  %-22s borrowed from %s" % (t, where))
    if not borrowed:
        print("  READER INTEGRITY FAILED: sections 3 and 4 borrow no label at "
              "all; the check cannot be non-vacuous")
        sys.exit(2)
    if missing:
        fired.append("F4: %d borrowed label(s) resolve nowhere" % len(missing))
        print("  F4 FIRED: %d borrowed label(s) resolve nowhere: %s"
              % (len(missing), ", ".join(missing)))
    else:
        print("  all %d borrowed labels resolve  OK" % len(borrowed))

    # O4 census, reported not failed.  The stated reason for this re-run was
    # that sections 3 and 4 "cite a section that isn't there".  That premise is
    # measured here rather than assumed: count what they actually take from
    # section 2, by cross-reference and by name.
    from_s2 = [t for t in borrowed if t in s2_labels]
    named = sum(len(re.findall(r"growth|\\S\\ref\{sec:growth\}", texts[n]))
                for n in SECTIONS)
    print("\n[dependency on section 2, measured]")
    print("  labels borrowed from section 2 : %d %s"
          % (len(from_s2), from_s2 or ""))
    print("  occurrences of 'growth' or a reference to sec:growth : %d" % named)
    if not from_s2 and not named:
        print("  FINDING: sections 3 and 4 depend on section 2 neither by "
              "cross-reference nor by name.  The blocker was real for the "
              "GROUP ORDER, but it does not bind this check: nothing in "
              "sections 3 or 4 was unresolvable for want of section 2.")
    else:
        print("  sections 3/4 do depend on section 2; the dependency now "
              "resolves.")

    print("\n[warnings, not failures]")
    if warn_text_superseded:
        for name, cid in warn_text_superseded:
            print("  %s cites %s, whose free text mentions supersession; "
                  "no structured superseded_by field.  For adjudication."
                  % (name, cid))
    else:
        print("  none.")

    total = sum(len(extract(texts[n])) for n in SECTIONS)
    bad_n = counts["UNRESOLVED"] + counts["SUPERSEDED"] + counts["MISMATCH"]

    # C6 -- the S34 ordering trap, closed by construction rather than by
    # remembering to run the gate first.  Asserted NON-VACUOUSLY: it is not
    # enough that this session's claims.jsonl is absent from the walk; it must
    # EXIST and be absent, or the assertion passes on a file that was simply
    # never written.
    print("\n[self-exclusion]")
    walked = {p.resolve() for p in claim_index.corpus_files()}
    if not claim_index.SELF.exists():
        print("  this session's claims.jsonl does not exist yet; the exclusion "
              "is VACUOUS so far (re-asserted after emission)")
    elif claim_index.SELF.resolve() in walked:
        fired.append("C6: this session's own claims.jsonl is inside the walk")
        print("  C6 FIRED: %s is inside the corpus walk; any claim citing this "
              "gate's digest would go stale on re-run" % claim_index.SELF)
    else:
        print("  %s exists and is EXCLUDED from the %d-file walk  OK"
              % (claim_index.SELF.name, len(walked)))

    print("\n[summary]")
    print("  citations checked : %d" % total)
    print("  OK                : %d" % counts["OK"])
    print("  UNRESOLVED        : %d" % counts["UNRESOLVED"])
    print("  SUPERSEDED        : %d" % counts["SUPERSEDED"])
    print("  MISMATCH          : %d" % counts["MISMATCH"])
    print("  other falsifiers  : %s" % ("; ".join(fired) if fired else "none"))
    print("  falsifier         : (UNRESOLVED + SUPERSEDED + MISMATCH) > 0, or "
          "any of F4, F5, C6 fired")
    print("VERDICT: %s" % ("PASS" if (bad_n == 0 and not fired) else "FAIL"))
    sys.exit(0 if (bad_n == 0 and not fired) else 1)


if __name__ == "__main__":
    main()
