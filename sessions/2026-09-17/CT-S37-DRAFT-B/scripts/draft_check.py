"""draft_check.py -- Group B draft check (CT-S37-DRAFT-B).

Reads the drafted sections, extracts every (claim id, asserted label) pair, and
checks each against the corpus index built by claim_index.py.

The check FAILS (exit 1) if any cited id is UNRESOLVED, structurally
SUPERSEDED, or carries a label in the prose that differs from the label the
corpus record carries.  Resolution via the 'CT-' prefix alias is REPORTED, not
failed.

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
    aliases, warn_text_superseded, rows = [], [], []

    for name in SECTIONS:
        for cid, asserted, _pos in extract(texts[name]):
            alias = None
            rec = index.get(cid)
            if rec is None and not cid.startswith("CT-"):
                rec = index.get("CT-" + cid)
                if rec is not None:
                    alias = "CT-" + cid
            if rec is None:
                counts["UNRESOLVED"] += 1
                rows.append((name, cid, asserted, "-", "UNRESOLVED",
                             "no such claim id in the corpus"))
                continue
            key = alias or cid
            if alias:
                aliases.append((name, cid, alias))
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

    print("\n[alias report]")
    if aliases:
        for name, cid, alias in aliases:
            print("  %s cites %s, resolved only as %s (CT- prefix alias)"
                  % (name, cid, alias))
    else:
        print("  no citation required the CT- prefix alias; the drafts use the "
              "corpus form throughout.")
    print("  NOTE: OUTLINE.md cites this family as S9-PVPARAMS-*; the corpus "
          "ids are CT-S9-PVPARAMS-*.  Reported as a finding, not normalised "
          "silently.")

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
    print("\n[summary]")
    print("  citations checked : %d" % total)
    print("  OK                : %d" % counts["OK"])
    print("  UNRESOLVED        : %d" % counts["UNRESOLVED"])
    print("  SUPERSEDED        : %d" % counts["SUPERSEDED"])
    print("  MISMATCH          : %d" % counts["MISMATCH"])
    print("  falsifier         : (UNRESOLVED + SUPERSEDED + MISMATCH) > 0")
    print("VERDICT: %s" % ("PASS" if bad_n == 0 else "FAIL"))
    sys.exit(0 if bad_n == 0 else 1)


if __name__ == "__main__":
    main()
