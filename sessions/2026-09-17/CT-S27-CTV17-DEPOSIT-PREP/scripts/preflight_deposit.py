"""preflight_deposit.py -- CT-S27-CTV17-DEPOSIT-PREP

A GATE, not a measurement.  Every check compares a file on disk against either
the deposited v1.6 record or the staged artefact.  No check reads this script's
own prose, and none reads DEPOSIT-FORM.md's narrative -- only its machine
readable ```form blocks.

The two defect classes this exists to stop, both of which cost a round at the
previous deposit:

  1. FILENAME.  vquad_resurgence_v1.2_zenodo-20481592.pdf was uploaded to
     record 22831933.  The BYTES were correct; the label was not.  Filenames
     cannot be changed after publishing.
  2. HASH.  A hash taken before the final edit resolves to nothing.  It must be
     computed from the staged file on disk, after the last edit.

SECTION 2 mutates the STAGED ARTEFACT AND THE FORM -- not the prose -- and
requires every check to reject its mutant.  A check whose mutant is accepted is
reported BROKEN and the gate does not pass.

SECTION 3 mutates the INPUT PATH (proposed Amendment C): a check that reports
"the form does not carry the hash" must not be able to mean "I could not read
the form".
"""

import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
SESSIONS = os.path.dirname(SESSION)
SESSIONS_ROOT = os.path.dirname(SESSIONS)
REPO = os.path.dirname(os.path.dirname(SESSIONS))

FORM = os.path.join(SESSION, "DEPOSIT-FORM.md")
UPLOAD = os.path.join(SESSION, "upload")
DRAFT = os.path.join(SESSIONS, "CT-S26-CTV17-DRAFT")
NOTICE = os.path.join(DRAFT, "NOTICE-v1.7.md")
RECORD = os.path.join(DRAFT, "refs", "zenodo_22782807.json")
REV3_OUT = os.path.join(DRAFT, "outputs", "verify_notice_rev3.out.txt")

failures = []
broken = []


class ReadError(Exception):
    pass


# ----------------------------------------------------------------- readers
def read_text(path, sentinels):
    """Decode, normalise once, and assert known-present features before use."""
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    if "\r" in text:
        raise ReadError("CR survived normalisation")
    for s in sentinels:
        if s not in text:
            raise ReadError("known-present sentinel %r absent: the read is suspect" % s)
    return text


def parse_form(text):
    """Collect every ```form block into one dict.  Order-independent."""
    blocks = re.findall(r"```form\n(.*?)```", text, re.DOTALL)
    if not blocks:
        raise ReadError("no ```form block found: the form is unreadable")
    d = {}
    for b in blocks:
        for line in b.split("\n"):
            if not line.strip() or ":" not in line:
                continue
            k, v = line.split(":", 1)
            d[k.strip()] = v.strip()
    if len(d) < 10:
        raise ReadError("only %d form keys parsed: the read is suspect" % len(d))
    return d


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def record():
    with open(RECORD, encoding="utf-8") as fh:
        return json.load(fh)


def report(name, ok, detail):
    print("  [%s] %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
    if not ok:
        failures.append(name)


# ------------------------------------------------------- GROUP A: staging
BANNED_IN_NAME = ("draft", "copy", "final", "new", "tmp", "temp", "untitled")


def check_staged_name(form, _staged_sha):
    """The publishable filename, decided before upload and checked mechanically."""
    name = form.get("staged_filename", "")
    if not name:
        return False, "the form declares no staged_filename"
    low = name.lower()
    for bad in BANNED_IN_NAME:
        if bad in low:
            return False, "filename contains %r: %s" % (bad, name)
    ids = re.findall(r"\d{6,}", name)
    if ids:
        return False, ("filename embeds what looks like a record id %s -- this is "
                       "the v1.3 defect exactly: %s" % (ids, name))
    if name != low:
        return False, "filename is not lowercase: %s" % name
    if not name.endswith(".md"):
        return False, "staged file is not .md: %s" % name
    if re.search(r"\s|\(|\)", name):
        return False, "filename carries whitespace or parentheses: %s" % name
    return True, "publishable name decided and clean: %s" % name


def check_staged_present(form, _staged_sha):
    """Exactly one file staged, under exactly the declared name."""
    name = form.get("staged_filename", "")
    present = sorted(os.listdir(UPLOAD))
    if present != [name]:
        return False, ("upload/ holds %s but the form declares %r -- a staging "
                       "directory with anything else in it is how the wrong file "
                       "gets picked" % (present, name))
    return True, "upload/ holds exactly the declared file"


def check_staged_bytes(form, _staged_sha):
    """Staged bytes must equal the source notice byte for byte."""
    name = form.get("staged_filename", "")
    p = os.path.join(UPLOAD, name)
    if not os.path.exists(p):
        return False, "staged file does not exist: %s" % name
    src = sha256_file(NOTICE)
    got = sha256_file(p)
    if src != got:
        return False, "staged bytes differ from the source notice (%s vs %s)" % (
            got[:16], src[:16])
    if int(form.get("staged_bytes", "-1")) != os.path.getsize(p):
        return False, "declared byte count %s != actual %d" % (
            form.get("staged_bytes"), os.path.getsize(p))
    return True, "staged bytes identical to the source, %d bytes" % os.path.getsize(p)


# -------------------------------------------------- GROUP B: hash discipline
def check_hash_is_of_staged_file(form, staged_sha):
    """The declared hash must be the hash of the staged file AS IT NOW IS."""
    declared = form.get("staged_sha256", "")
    if not re.fullmatch(r"[0-9a-f]{64}", declared):
        return False, "staged_sha256 is not a 64-hex digest: %r" % declared
    if declared != staged_sha:
        return False, ("declared hash %s is NOT the hash of the staged file (%s) "
                       "-- a hash taken before the final edit points at nothing"
                       % (declared[:16], staged_sha[:16]))
    return True, "declared hash equals the staged file on disk: %s" % staged_sha[:16]


def check_notice_is_the_verified_one(form, staged_sha):
    """The staged file must be the revision the checker actually passed."""
    try:
        out = read_text(REV3_OUT, ["VERDICT (rev3): OK"])
    except ReadError as exc:
        return False, "cannot read the rev-3 checker output: %s" % exc
    m = re.search(r"sha256 : ([0-9a-f]{64})", out)
    if not m:
        return False, "the checker output records no notice hash"
    if m.group(1) != staged_sha:
        return False, ("the staged file (%s) is not the revision the checker "
                       "passed (%s)" % (staged_sha[:16], m.group(1)[:16]))
    if "checks failed       : 0" not in out or "broken checks       : 0" not in out:
        return False, "the checker output does not record 0 failed / 0 broken"
    return True, "staged file is the revision that passed rev 3, 0 failed, 0 broken"


# ------------------------------------------- GROUP C: metadata vs the record
def check_title_no_drift(form, _s):
    rec = record()["metadata"]
    policy = form.get("title_policy")
    if policy != "same-as-v1.6":
        return False, ("title_policy is %r; a title change needs its own ruling "
                       "and this gate will not infer one" % policy)
    if form.get("title") != rec.get("title"):
        return False, "title drifts from the v1.6 record"
    return True, "title matches the deposited v1.6 title exactly"


def check_version(form, _s):
    rec = record()["metadata"]
    if rec.get("version") != form.get("version_previous"):
        return False, ("the record is at version %r but the form says the previous "
                       "version is %r" % (rec.get("version"), form.get("version_previous")))
    if form.get("version") != "1.7":
        return False, "version is %r, not 1.7" % form.get("version")
    if form.get("version") == rec.get("version"):
        return False, "the form would re-publish the version already on the record"
    return True, "record at 1.6, form at 1.7, declared as a deliberate change"


def check_creator_no_drift(form, _s):
    """The v1 affiliation-drift class: 'Independent Researcher' vs a longer form."""
    rec = record()["metadata"]
    cr = (rec.get("creators") or [{}])[0]
    if form.get("creator_name") != cr.get("name"):
        return False, "creator name drifts: %r vs record %r" % (
            form.get("creator_name"), cr.get("name"))
    if form.get("creator_affiliation") != cr.get("affiliation"):
        return False, ("affiliation drifts: %r vs record %r -- this is the v1 "
                       "affiliation-drift defect" % (form.get("creator_affiliation"),
                                                     cr.get("affiliation")))
    return True, "creator name and affiliation match the record exactly"


def check_licence_and_keywords(form, _s):
    rec = record()["metadata"]
    lic = rec.get("license")
    lic_id = lic.get("id") if isinstance(lic, dict) else lic
    if form.get("license") != lic_id:
        return False, "licence drifts: %r vs record %r" % (form.get("license"), lic_id)
    kws = rec.get("keywords") or []
    if form.get("keywords_policy") != "same-as-v1.6":
        return False, "keywords_policy is %r; a keyword change needs a ruling" % \
            form.get("keywords_policy")
    if int(form.get("keywords_count", "-1")) != len(kws):
        return False, ("declared keyword count %s != the record's %d -- the "
                       "title/keyword drift class" % (form.get("keywords_count"), len(kws)))
    return True, "licence %s and %d keywords, both unchanged from the record" % (
        lic_id, len(kws))


def check_concept_doi(form, _s):
    """The concept DOI is a FIELD.  It is never derived from a record number."""
    rec = record()
    cdoi = rec.get("conceptdoi")
    if not cdoi:
        return False, "the held record carries no conceptdoi field"
    if form.get("concept_doi") != cdoi:
        return False, "concept DOI %r != the record's conceptdoi %r" % (
            form.get("concept_doi"), cdoi)
    vdoi = rec.get("doi")
    if form.get("concept_doi") == vdoi:
        return False, "the concept DOI has been given as the VERSION DOI %r" % vdoi
    if str(rec.get("id", "")) in form.get("concept_doi", ""):
        return False, "the concept DOI appears to be built from the record number"
    if form.get("version_doi") != "MINTED-ON-PUBLISH":
        return False, "a version DOI is written in advance; Zenodo mints it on publish"
    return True, "concept DOI read from the conceptdoi field, distinct from the version DOI"


# ------------------------------------------------ GROUP D: the deposit shape
def check_shape_not_a_promise(form, _s):
    """The form must not name a file it does not hold."""
    if form.get("deposit_shape") != "UNDECIDED":
        return False, ("deposit_shape is %r, but no shape can be executed: the "
                       "v1.6 PDF is not held and v1.4-v1.6 sources are absent"
                       % form.get("deposit_shape"))
    if form.get("pdf_held") != "false" or form.get("pdf_rebuild_possible") != "false":
        return False, "the form claims a PDF is held or rebuildable; neither is true"
    pdfs = [f for f in os.listdir(UPLOAD) if f.lower().endswith(".pdf")]
    if pdfs:
        return False, "a PDF is staged (%s) while the form says none is held" % pdfs
    return True, "shape left UNDECIDED and no unheld file is named or staged"


def check_no_v14_v16_source(form, _s):
    """The blocker, verified against the tree rather than asserted.

    This walks the WHOLE sessions/ tree, not this date's folder.  The first
    version walked only sessions/2026-09-17/ and reported "no Channel Theory
    source found at all" -- which, had the reader-integrity clause not been
    present, would have been read as confirming the blocker for the wrong
    reason.  The sources live under 2026-05-*.
    """
    hits = []
    for root, _dirs, files in os.walk(SESSIONS_ROOT):
        for f in files:
            if f.endswith(".tex") and "channel_theory_outline" in f:
                hits.append(os.path.join(root, f))
    if not hits:
        return False, "no Channel Theory source found at all: the read is suspect"
    names = sorted(os.path.basename(h) for h in hits)
    late = [n for n in names if re.search(r"v1[._]?[456]", n)]
    if late:
        return False, ("a v1.4-v1.6 source appears to exist after all: %s -- the "
                       "blocker must be re-examined" % late)
    if not any("v13" in n or "v1_3" in n for n in names):
        return False, ("no v1.3-era source among %s: the version reading is "
                       "suspect" % names)
    return True, ("%d Channel Theory sources in the tree, newest v1.3.1; no v1.4-v1.6 "
                  "source, so the outline cannot be rebuilt at v1.7" % len(hits))


CHECKS = [
    ("A1 publishable filename decided and clean", check_staged_name),
    ("A2 exactly the declared file is staged", check_staged_present),
    ("A3 staged bytes identical to the source", check_staged_bytes),
    ("B1 declared hash is the hash of the staged file", check_hash_is_of_staged_file),
    ("B2 staged file is the revision the checker passed", check_notice_is_the_verified_one),
    ("C1 title does not drift from the record", check_title_no_drift),
    ("C2 version is 1.7 over a record at 1.6", check_version),
    ("C3 creator and affiliation do not drift", check_creator_no_drift),
    ("C4 licence and keyword count do not drift", check_licence_and_keywords),
    ("C5 concept DOI read from the conceptdoi field", check_concept_doi),
    ("D1 deposit shape names no unheld file", check_shape_not_a_promise),
    ("D2 the PDF blocker holds against the tree", check_no_v14_v16_source),
]

# Mutants act on (form dict, staged sha).  They mutate the ARTEFACT VALUES,
# never this file's prose.
MUTANTS = {
    "A1 publishable filename decided and clean": [
        lambda f, s: (dict(f, staged_filename="DRAFT-channel_theory_v1.7_version_notice.md"), s),
        lambda f, s: (dict(f, staged_filename="channel_theory_v1.7_zenodo-22782807.md"), s),
        lambda f, s: (dict(f, staged_filename="Channel Theory v1.7 (1).md"), s),
    ],
    "A2 exactly the declared file is staged": [
        lambda f, s: (dict(f, staged_filename="something_else.md"), s),
    ],
    "A3 staged bytes identical to the source": [
        lambda f, s: (dict(f, staged_bytes="47700"), s),
    ],
    "B1 declared hash is the hash of the staged file": [
        # the hash of revision 2 -- a hash taken one edit too early
        lambda f, s: (dict(f, staged_sha256="9d93aeb1984d0039cdf711644df8725c"
                                            "db807029445a404d6967b91bb61dc11a"), s),
        lambda f, s: (dict(f, staged_sha256="not-a-hash"), s),
    ],
    "B2 staged file is the revision the checker passed": [
        lambda f, s: (f, "0" * 64),
    ],
    "C1 title does not drift from the record": [
        lambda f, s: (dict(f, title=f["title"].replace("Bridge Conjecture",
                                                       "Bridge Theorem")), s),
        lambda f, s: (dict(f, title_policy="updated"), s),
    ],
    "C2 version is 1.7 over a record at 1.6": [
        lambda f, s: (dict(f, version="1.6"), s),
        lambda f, s: (dict(f, version_previous="1.5"), s),
    ],
    "C3 creator and affiliation do not drift": [
        lambda f, s: (dict(f, creator_affiliation="Independent researcher, "
                                                  "Yokohama, Japan"), s),
    ],
    "C4 licence and keyword count do not drift": [
        lambda f, s: (dict(f, keywords_count="26"), s),
        lambda f, s: (dict(f, license="cc-by-sa-4.0"), s),
    ],
    "C5 concept DOI read from the conceptdoi field": [
        lambda f, s: (dict(f, concept_doi="10.5281/zenodo.22782807"), s),
        lambda f, s: (dict(f, version_doi="10.5281/zenodo.99999999"), s),
    ],
    "D1 deposit shape names no unheld file": [
        lambda f, s: (dict(f, deposit_shape="B"), s),
        lambda f, s: (dict(f, pdf_held="true"), s),
    ],
    "D2 the PDF blocker holds against the tree": None,  # tree-reading; see SECTION 2b
}


# ------------------------------------------------ SECTION 3 reader controls
def reader_binary_no_normalise():
    return open(FORM, "rb").read().decode("utf-8")


def reader_wrong_codec():
    return open(FORM, "rb").read().decode("latin-1").replace("\r\n", "\n")


def reader_truncating():
    return open(FORM, "rb").read()[:400].decode("utf-8", "ignore").replace("\r\n", "\n")


# At least one sentinel MUST be non-ASCII.  With ASCII-only sentinels a
# latin-1 misread passes every one of them -- the mojibake lands in the title
# and nowhere the check looks.  "\u03be\u2080" is the xi_0 in the title line.
FORM_SENTINELS = ["# DEPOSIT-FORM", "```form", "staged_filename:", "concept_doi:",
                  "\u03be\u2080 = 2/\u221a\u03b2\u2082"]


def assert_form(text):
    if "\r" in text:
        raise ReadError("CR present: line endings were not normalised")
    for s in FORM_SENTINELS:
        if s not in text:
            raise ReadError("sentinel %r absent: the read is suspect" % s)
    parse_form(text)


def main():
    print("=" * 76)
    print("preflight_deposit.py -- CT-S27-CTV17-DEPOSIT-PREP")
    print("  A GATE.  Any FAIL blocks the deposit.  No thresholds, no partial credit.")
    print("=" * 76)
    print()

    print("SECTION 0 -- READER INTEGRITY")
    print("-" * 76)
    try:
        form_text = read_text(FORM, FORM_SENTINELS)
        form = parse_form(form_text)
    except ReadError as exc:
        print("  [FAIL] cannot read DEPOSIT-FORM.md -- %s" % exc)
        print("VERDICT: BLOCKED")
        return 2
    print("  [PASS] form read: %d keys, sentinels present, no CR" % len(form))

    name = form.get("staged_filename", "")
    staged_path = os.path.join(UPLOAD, name)
    if not os.path.exists(staged_path):
        print("  [FAIL] the staged file does not exist: %s" % name)
        print("VERDICT: BLOCKED")
        return 2
    staged_sha = sha256_file(staged_path)
    print("  [PASS] staged file read: %s" % name)
    print("staged : upload/%s" % name)
    print("sha256 : %s   (from disk, after the last edit)" % staged_sha)
    print("bytes  : %d" % os.path.getsize(staged_path))
    print()

    print("SECTION 1 -- THE GATE")
    print("-" * 76)
    for cname, fn in CHECKS:
        try:
            ok, detail = fn(form, staged_sha)
        except Exception as exc:
            ok, detail = False, "check raised %s: %s" % (type(exc).__name__, exc)
        report(cname, ok, detail)
    print()

    print("SECTION 2 -- CAN-FAIL CONTROLS (mutate the ARTEFACT, not the prose)")
    print("-" * 76)
    for cname, fn in CHECKS:
        muts = MUTANTS.get(cname)
        if muts is None:
            print("  [n/a ] %s -- reads the tree; controlled in SECTION 2b" % cname)
            continue
        fired = True
        for i, mf in enumerate(muts):
            mform, msha = mf(dict(form), staged_sha)
            if mform == form and msha == staged_sha:
                print("  [BROKEN] %s -- mutant %d is identical to the original"
                      % (cname, i + 1))
                fired = False
                continue
            try:
                ok, _d = fn(mform, msha)
            except Exception:
                ok = False
            if ok:
                print("  [BROKEN] %s -- mutant %d ACCEPTED" % (cname, i + 1))
                fired = False
        if fired:
            print("  [PASS] %s -- %d mutant(s) rejected" % (cname, len(muts)))
        else:
            broken.append(cname)
    print()

    print("SECTION 2b -- TREE CONTROL for D2")
    print("-" * 76)
    print("  D2 reads the repository, so a form mutant cannot reach it.  Its")
    print("  control is a fake source file name matched by the same pattern.")
    probe = ["channel_theory_outline_v1.5_something.tex"]
    d2_fires = any(re.search(r"v1[._]?[456]", n) for n in probe)
    print("  [%s] D2's pattern recognises a v1.5 source when one is present"
          % ("PASS" if d2_fires else "BROKEN"))
    if not d2_fires:
        broken.append("D2 the PDF blocker holds against the tree")
    print()

    print("SECTION 3 -- READER CONTROLS (mutate the INPUT PATH)")
    print("-" * 76)
    reader_fail = 0
    for rname, rf in [("binary read, CRLF not normalised", reader_binary_no_normalise),
                      ("wrong codec (latin-1)", reader_wrong_codec),
                      ("silently truncated read", reader_truncating)]:
        try:
            assert_form(rf())
            print("  [BROKEN] %s -- NOT caught" % rname)
            reader_fail += 1
        except ReadError as exc:
            print("  [PASS] %s -- caught: %s" % (rname, exc))
        except Exception as exc:
            print("  [PASS] %s -- caught by decoding: %s" % (rname, type(exc).__name__))
    print()

    print("=" * 76)
    print("checks run     : %d" % len(CHECKS))
    print("checks failed  : %d%s" % (len(failures),
                                     ("  -> " + ", ".join(failures)) if failures else ""))
    print("broken checks  : %d%s" % (len(broken),
                                     ("  -> " + ", ".join(broken)) if broken else ""))
    print("reader controls: %d of 3 caught" % (3 - reader_fail))
    print()
    clean = not failures and not broken and not reader_fail
    print("GATE: %s" % ("PASSED" if clean else "BLOCKED"))
    print()
    print("DEPOSIT READY: NO.")
    print("  The gate passing means the PACKET is consistent -- filename, bytes,")
    print("  hash and every metadata value agree with the deposited record.  It")
    print("  does NOT mean a deposit can proceed: the deposit SHAPE is undecided")
    print("  and every available shape is blocked on material absent from this")
    print("  repository (the v1.6 PDF, or the v1.4-v1.6 LaTeX sources).")
    print("  That is an operator decision, not a check that can be made to pass.")
    print("=" * 76)
    return 0 if clean else 1


if __name__ == "__main__":
    sys.exit(main())
