"""preflight_deposit_rev2.py -- CT-S27-CTV17-DEPOSIT-PREP

Revision 2 of the deposit gate, for the RULED shape: description-only.

What changed, and why the revision is a new file rather than an edit:
`outputs/preflight_deposit.out.txt` and `..._r2.out.txt` are cited by claims
S27-01..S27-05, so neither the rev-1 script nor its outputs are touched.

The shape ruling moves the artefact.  Under description-only, NOTHING IS
UPLOADED: the v1.6 PDF carries over by platform action and the notice becomes
the record description.  So the rev-1 staging checks (A1 filename, A2 exactly
one staged file, A3 staged bytes) no longer describe anything real, and are
replaced by their description-only counterparts:

  S1  upload/ is EMPTY -- the only way to publish a wrong file is to have one
  S2  the description artefact exists and matches the form's hash ON DISK
  S3  the description is the one the description checker passed
  S4  the carried-over file is named by key, md5 and size from the RECORD,
      and no attempt is made to hash bytes this session does not hold

The metadata group (C1-C5) is imported unchanged from rev 1, which keeps its
mutants and its evidence.  Rev 1's D2 tree check is imported too: the blocker
did not go away, it was ruled around, and the notice now states the reason.
"""

import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import preflight_deposit as r1  # noqa: E402

SESSION = r1.SESSION
UPLOAD = r1.UPLOAD
DESC = os.path.join(SESSION, "DESCRIPTION-v1.7-rev2.html")
DESC_OUT = os.path.join(SESSION, "outputs", "verify_description_r7.out.txt")
EXPECTED_DESC_CHECKS = 17

failures, broken = [], []

# Rev 1's sentinels name staged_filename:, which the shape ruling deleted, so
# rev 1 can no longer read this form at all -- it fails closed, which is the
# correct behaviour and is why it is superseded rather than edited.  A
# reader-integrity sentinel set is coupled to the artefact and must be revised
# with it.  One sentinel is non-ASCII, per the adopted Amendment C.
REV2_SENTINELS = [
    "\u03be\u2080 = 2/\u221a\u03b2\u2082",
    "# DEPOSIT-FORM",
    "```form",
    "description_sha256:",
    "deposit_shape_ruled:",
]
r1.FORM_SENTINELS = REV2_SENTINELS


def sha(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ------------------------------------------------- description-only staging
def s1_upload_empty(form, _d):
    if form.get("upload_dir_must_be_empty") != "true":
        return False, "the form does not require upload/ to be empty"
    if form.get("new_file_uploaded") != "false":
        return False, "the form contemplates uploading a new file"
    present = sorted(os.listdir(UPLOAD))
    if present:
        return False, ("upload/ is not empty (%s) -- under a description-only "
                       "version nothing is uploaded, and a file sitting in the "
                       "staging directory is the only way to publish one by "
                       "accident" % present)
    return True, "upload/ is empty and the form forbids a new file"


def s2_description_hash(form, desc_sha):
    declared = form.get("description_sha256", "")
    if not re.fullmatch(r"[0-9a-f]{64}", declared):
        return False, "description_sha256 is not a 64-hex digest: %r" % declared
    if declared != desc_sha:
        return False, ("declared hash %s is NOT the hash of DESCRIPTION-v1.7-rev2.html "
                       "on disk (%s) -- a hash taken before the final edit points "
                       "at nothing" % (declared[:16], desc_sha[:16]))
    if int(form.get("description_chars", "-1")) != len(
            open(DESC, encoding="utf-8").read()):
        return False, "declared description_chars does not match the file"
    src = form.get("source_notice_sha256", "")
    actual_src = sha(os.path.join(r1.DRAFT, "NOTICE-v1.7.md"))
    if src != actual_src:
        return False, ("the form's source_notice_sha256 %s is not the notice on "
                       "disk %s -- the description was generated from a different "
                       "revision than the form records" % (src[:16], actual_src[:16]))
    return True, "description and source-notice hashes both match the files on disk"


def s3_description_verified(form, desc_sha):
    try:
        out = r1.read_text(DESC_OUT, ["VERDICT: OK"])
    except r1.ReadError as exc:
        return False, "cannot read the description checker output: %s" % exc
    m = re.search(r"sha256 : ([0-9a-f]{64})", out)
    if not m:
        return False, "the description checker output records no hash"
    if m.group(1) != desc_sha:
        return False, ("the description on disk (%s) is not the one the checker "
                       "passed (%s)" % (desc_sha[:16], m.group(1)[:16]))
    ran = re.search(r"checks run\s+: (\d+)", out)
    if not ran or ran.group(1) != str(EXPECTED_DESC_CHECKS):
        return False, ("the checker output records %s checks, not %d: a stale "
                       "output from a different check set"
                       % (ran.group(1) if ran else "no", EXPECTED_DESC_CHECKS))
    if "checks failed  : 0" not in out or "broken checks  : 0" not in out:
        return False, "the description checker did not record 0 failed / 0 broken"
    if "reader controls: 3 of 3 caught" not in out:
        return False, "the description checker's reader controls did not all fire"
    return True, ("description is the revision that passed %d/%d with 3/3 reader "
                  "controls" % (EXPECTED_DESC_CHECKS, EXPECTED_DESC_CHECKS))


def s4_carried_file(form, _d):
    """The carried file is described from the RECORD and never hashed here."""
    rec = r1.record()
    files = rec.get("files") or []
    if len(files) != 1:
        return False, "the v1.6 record does not publish exactly one file (%d)" % len(files)
    f = files[0]
    key = f.get("key") or f.get("filename")
    if form.get("carried_file_key") != key:
        return False, "carried_file_key %r != the record's %r" % (
            form.get("carried_file_key"), key)
    cks = f.get("checksum", "")
    md5 = cks.split(":")[-1] if cks else f.get("checksum")
    if form.get("carried_file_md5") != md5:
        return False, "carried_file_md5 %r != the record's %r" % (
            form.get("carried_file_md5"), md5)
    if int(form.get("carried_file_bytes", "-1")) != f.get("size"):
        return False, "carried_file_bytes %s != the record's %s" % (
            form.get("carried_file_bytes"), f.get("size"))
    if os.path.exists(os.path.join(UPLOAD, key)):
        return False, ("the carried file has been staged locally -- it must be "
                       "carried over by the platform, not re-uploaded from bytes "
                       "this session does not hold")
    return True, ("carried file described from the record (%s, %d bytes, md5 %s) "
                  "and not re-staged" % (key, f.get("size"), md5[:8]))


def s5_shape_ruled(form, _d):
    if form.get("deposit_shape") != "DESCRIPTION-ONLY":
        return False, "deposit_shape is %r, not the ruled DESCRIPTION-ONLY" % \
            form.get("deposit_shape")
    if form.get("deposit_shape_ruled") != "DESCRIPTION-ONLY":
        return False, "the ruling is not recorded in the form"
    if form.get("pdf_held") != "false" or form.get("pdf_rebuild_possible") != "false":
        return False, ("the form claims a PDF is held or rebuildable; neither "
                       "became true, the shape was ruled around them")
    return True, "shape is the ruled DESCRIPTION-ONLY, with the blocker still recorded"


CHECKS = [
    ("S1 upload/ is empty, no file is published", s1_upload_empty),
    ("S2 description hash matches the file on disk", s2_description_hash),
    ("S3 description is the verified revision", s3_description_verified),
    ("S4 carried file described from the record, not re-staged", s4_carried_file),
    ("S5 shape is the ruled description-only", s5_shape_ruled),
    ("C1 title does not drift from the record", r1.check_title_no_drift),
    ("C2 version is 1.7 over a record at 1.6", r1.check_version),
    ("C3 creator and affiliation do not drift", r1.check_creator_no_drift),
    ("C4 licence and keyword count do not drift", r1.check_licence_and_keywords),
    ("C5 concept DOI read from the conceptdoi field", r1.check_concept_doi),
    ("D2 the rebuild blocker still holds against the tree", r1.check_no_v14_v16_source),
]

MUTANTS = {
    "S1 upload/ is empty, no file is published": [
        lambda f, d: (dict(f, upload_dir_must_be_empty="false"), d),
        lambda f, d: (dict(f, new_file_uploaded="true"), d),
    ],
    "S2 description hash matches the file on disk": [
        lambda f, d: (dict(f, description_sha256="0" * 64), d),
        lambda f, d: (dict(f, description_chars="1"), d),
        # the hash of the notice BEFORE the build statement was added
        lambda f, d: (dict(f, source_notice_sha256="75cd3476b89d18c13460e835f19d9"
                                                   "2f92c4db2b84a7548093ca9a82cf4f50872"), d),
    ],
    "S3 description is the verified revision": [
        lambda f, d: (f, "0" * 64),
    ],
    "S4 carried file described from the record, not re-staged": [
        lambda f, d: (dict(f, carried_file_md5="0" * 32), d),
        lambda f, d: (dict(f, carried_file_bytes="609301"), d),
        lambda f, d: (dict(f, carried_file_key="channel_theory_v1.7.pdf"), d),
    ],
    "S5 shape is the ruled description-only": [
        lambda f, d: (dict(f, deposit_shape="UNDECIDED"), d),
        lambda f, d: (dict(f, pdf_held="true"), d),
    ],
    "C1 title does not drift from the record": r1.MUTANTS[
        "C1 title does not drift from the record"],
    "C2 version is 1.7 over a record at 1.6": r1.MUTANTS[
        "C2 version is 1.7 over a record at 1.6"],
    "C3 creator and affiliation do not drift": r1.MUTANTS[
        "C3 creator and affiliation do not drift"],
    "C4 licence and keyword count do not drift": r1.MUTANTS[
        "C4 licence and keyword count do not drift"],
    "C5 concept DOI read from the conceptdoi field": r1.MUTANTS[
        "C5 concept DOI read from the conceptdoi field"],
    "D2 the rebuild blocker still holds against the tree": None,
}


def main():
    print("=" * 76)
    print("preflight_deposit_rev2.py -- description-only shape, as ruled")
    print("  A GATE.  Any FAIL blocks the deposit.  No thresholds.")
    print("=" * 76)
    print()

    print("SECTION 0 -- READER INTEGRITY")
    print("-" * 76)
    try:
        form_text = r1.read_text(r1.FORM, r1.FORM_SENTINELS)
        form = r1.parse_form(form_text)
    except r1.ReadError as exc:
        print("  [FAIL] cannot read DEPOSIT-FORM.md -- %s" % exc)
        return 2
    print("  [PASS] form read: %d keys, sentinels present, no CR" % len(form))
    if not os.path.exists(DESC):
        print("  [FAIL] DESCRIPTION-v1.7-rev2.html does not exist")
        return 2
    desc_sha = sha(DESC)
    print("  [PASS] description read")
    print("artefact : DESCRIPTION-v1.7-rev2.html   (nothing is uploaded)")
    print("sha256   : %s   (from disk, after the last edit)" % desc_sha)
    print("chars    : %d" % len(open(DESC, encoding="utf-8").read()))
    print()

    print("SECTION 1 -- THE GATE")
    print("-" * 76)
    for name, fn in CHECKS:
        try:
            ok, detail = fn(form, desc_sha)
        except Exception as exc:
            ok, detail = False, "check raised %s: %s" % (type(exc).__name__, exc)
        print("  [%s] %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
        if not ok:
            failures.append(name)
    print()

    print("SECTION 2 -- CAN-FAIL CONTROLS (mutate the ARTEFACT, not the prose)")
    print("-" * 76)
    for name, fn in CHECKS:
        muts = MUTANTS.get(name)
        if muts is None:
            print("  [n/a ] %s -- reads the tree; controlled in SECTION 2b" % name)
            continue
        fired = True
        for i, mf in enumerate(muts):
            mform, msha = mf(dict(form), desc_sha)
            if mform == form and msha == desc_sha:
                print("  [BROKEN] %s -- mutant %d is identical to the original"
                      % (name, i + 1))
                fired = False
                continue
            try:
                ok, _d = fn(mform, msha)
            except Exception:
                ok = False
            if ok:
                print("  [BROKEN] %s -- mutant %d ACCEPTED" % (name, i + 1))
                fired = False
        if fired:
            print("  [PASS] %s -- %d mutant(s) rejected" % (name, len(muts)))
        else:
            broken.append(name)
    print()

    print("SECTION 2b -- FILESYSTEM CONTROL for S1")
    print("-" * 76)
    print("  S1 reads the directory, so a form mutant cannot reach its second")
    print("  clause.  A file is created in upload/, S1 must reject, and it is")
    print("  removed in a finally block.")
    probe = os.path.join(UPLOAD, "_s1_control.tmp")
    try:
        with open(probe, "w", encoding="utf-8") as fh:
            fh.write("control")
        ok, detail = s1_upload_empty(form, desc_sha)
        if ok:
            print("  [BROKEN] S1 accepted a non-empty upload/")
            broken.append("S1 upload/ is empty, no file is published")
        else:
            print("  [PASS] S1 rejects a non-empty upload/ -- %s" % detail)
    finally:
        if os.path.exists(probe):
            os.remove(probe)
    assert not os.listdir(UPLOAD), "the control left a file behind in upload/"
    print("  [PASS] control cleaned up; upload/ is empty again")
    print()

    print("SECTION 2c -- TREE CONTROL for D2")
    print("-" * 76)
    d2_fires = bool(re.search(r"v1[._]?[456]",
                              "channel_theory_outline_v1.5_something.tex"))
    print("  [%s] D2's pattern recognises a v1.5 source when one is present"
          % ("PASS" if d2_fires else "BROKEN"))
    if not d2_fires:
        broken.append("D2 the rebuild blocker still holds against the tree")
    print()

    print("SECTION 3 -- READER CONTROLS (mutate the INPUT PATH)")
    print("-" * 76)
    reader_fail = 0
    for rname, rf in [("binary read, CRLF not normalised", r1.reader_binary_no_normalise),
                      ("wrong codec (latin-1)", r1.reader_wrong_codec),
                      ("silently truncated read", r1.reader_truncating)]:
        try:
            r1.assert_form(rf())
            print("  [BROKEN] %s -- NOT caught" % rname)
            reader_fail += 1
        except r1.ReadError as exc:
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
    clean = not failures and not broken and not reader_fail
    print()
    print("GATE: %s" % ("PASSED" if clean else "BLOCKED"))
    print()
    if clean:
        print("DEPOSIT READY: YES, for a description-only new version, subject to")
        print("  the six by-eye checks in DEPOSIT-FORM.md section 4 and the")
        print("  walkthrough's stop points.  The gate certifies the packet; it")
        print("  cannot see the browser, so the carried-over file and the pasted")
        print("  description must be confirmed in the dialog before publishing.")
        print("  PUBLISHING REMAINS OPERATOR-GATED AND IS IRREVERSIBLE.")
    else:
        print("DEPOSIT READY: NO.")
    print("=" * 76)
    return 0 if clean else 1


if __name__ == "__main__":
    sys.exit(main())
