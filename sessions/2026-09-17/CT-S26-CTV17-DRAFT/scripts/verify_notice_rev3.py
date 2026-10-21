"""verify_notice_rev3.py -- CT-S26-CTV17-DRAFT

Revision 3 of the v1.7 notice checker.  It does NOT re-implement revision 2:
it imports it, so every revision-2 check, mutant and reader control still runs
exactly as written, and adds the checks that the operator's five rulings of
2026-09-19 require.  Output goes to a NEW path; revision 2's output file is
cited by claims S26C-16/S26C-17 and must not be overwritten.

One revision-2 check is REPLACED rather than added to:

    "every op:/rem: tag exists in the deposited record"

As written it rejects any tag absent from the held deposited descriptions.
That was correct while the notice only referred to existing problems.  Ruling 8
requires v1.7 to CREATE a tag -- exactly as v1.6 created op:xi0-singularity-type
-- so the check must admit a tag the notice declares new while still rejecting
one that is merely invented.  This is a LOOSENING, and per the standing rule it
is disclosed as such and arrives with extra can-fail controls in the same edit:
the replacement carries three mutants where the original carried one, including
a tag that is invented without being declared, and a removal of the declaration
that makes the new tag legitimate.

The rulings checked here:

  R4  no forward reference to an undeposited document
  R5  Wong & Li II left NOT OBTAINED, and the notice not gated on it
  R7  v1.6's falsifiers are POINTED AT by version DOI and section, not restated
  R8  the S_{zeta*} negative has its own tag, kept distinct from
      op:cc-stokes-closed-form, with the non-implication stated in both
      directions
  W   op:xi0-degree-d is not reported as closed: the analytic residual is
      stated as open and named, inside section 2 itself
  R9  claim S3A-06 has been narrowed to the artefact actually inspected
      (checked against the corpus record, not against the notice)
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import verify_notice_rev2 as r2  # noqa: E402

SESSION = r2.SESSION
SESSIONS = os.path.dirname(SESSION)


# --------------------------------------------------------------- helpers
def flat(text):
    """Collapse blockquote wrapping and whitespace, as revision 2 does.

    A requirement must not be defeated by where a line happens to wrap.
    """
    return re.sub(r"\s+", " ", text.replace("\n>", " "))


# ----------------------------------------------- REPLACED: tag reality check
NEW_AT_V17 = {"op:cc-szeta-closed-form"}


def check_obligation_tags_are_real_v3(text):
    """Every op:/rem: tag must be in the deposited record OR declared new here.

    A tag declared new must carry the declaration in the notice, so that a
    reader can tell a created problem from an invented one.  A tag that is
    neither present in the record nor declared new is an invention and fails.
    """
    held = r2._held_sources()
    blob = "\n".join(held.values())
    body = flat(text)
    tags = set(re.findall(r"`((?:op|rem):[A-Za-z0-9\-]+)`", text))
    if not tags:
        return False, "the notice names no obligation tag at all"

    invented, created = [], []
    for t in sorted(tags):
        if t in blob:
            continue
        if t in NEW_AT_V17 and re.search(
                re.escape("`%s`" % t) + r".{0,600}?new at v1\.7", body,
                re.IGNORECASE):
            created.append(t)
            continue
        invented.append(t)

    if invented:
        return False, ("tags neither in the deposited record nor declared new "
                       "at v1.7: " + ", ".join(invented))
    return True, ("%d obligation tags: %d present in the deposited record, "
                  "%d declared new at v1.7 (%s)"
                  % (len(tags), len(tags) - len(created), len(created),
                     ", ".join(created) or "none"))


# ------------------------------------------------------------ R4
def check_no_forward_reference(text):
    """Ruling 4: do not point at a document that does not yet exist.

    An absence check, so it asserts a known-present feature first: the notice
    must carry the explicit undertaking in section 8.  Without that sentinel a
    truncated or mis-read file would report a clean absence.
    """
    body = flat(text)
    if "No forward reference is made to any undeposited document" not in body:
        return False, "section 8 does not carry the no-forward-reference undertaking"
    if "has an identifier" not in body:
        return False, "the condition for adding a pointer later is not stated"

    bad = [
        "forthcoming paper", "in preparation", "the forthcoming",
        "will appear in", "to appear in", "a paper now in draft",
        "the paper now being drafted", "see the forthcoming",
    ]
    hits = [p for p in bad if p.lower() in body.lower()]
    if hits:
        return False, "forward reference to an unpublished document: " + ", ".join(hits)
    return True, ("no forward reference; the undertaking and its condition are "
                  "both stated in section 8")


# ------------------------------------------------------------ R5
def check_wongli_not_gating(text):
    """Ruling 5: leave it NOT OBTAINED, and say the notice is not gated on it."""
    body = flat(text)
    if "NOT OBTAINED" not in body:
        return False, "Wong & Li II is no longer marked NOT OBTAINED"
    if "not gated on obtaining it" not in body:
        return False, "the notice does not say it is not gated on obtaining it"
    for needed in ("Wong & Zhao", "priority position stated here must not be softened"):
        if needed not in body:
            return False, "missing from the non-gating paragraph: %r" % needed
    return True, ("NOT OBTAINED retained; non-gating stated; the held "
                  "Wong & Zhao route named; no softening permitted")


# ------------------------------------------------------------ R7
def check_falsifier_pointed_not_restated(text):
    """Ruling 7: point at the falsifier by version DOI and section; never paraphrase."""
    body = flat(text)
    if "does not restate the falsifier" not in body:
        return False, "the notice no longer declines to restate the falsifier"
    if not re.search(r"§9 of version `?10\.5281/zenodo\.22782807`?", body):
        return False, "the falsifier is not pointed at by version DOI and section"
    if "Pointing at unread text is accurate" not in body:
        return False, "the reason for pointing rather than paraphrasing is not stated"
    # The defect this check exists to catch is a PARAPHRASE of unread text, so
    # the check must be able to detect one, not merely confirm a disclaimer.
    leak = re.search(r"(v1\.6 falsifier[^.]{0,60}(is|was|of)\s+\d"
                     r"|§9 falsifier threshold[^.]{0,40}\d"
                     r"|falsifier threshold (is|was|of)\s+\d)", body, re.IGNORECASE)
    if leak:
        return False, ("a numeric value is asserted for the unread v1.6 falsifier: "
                       + leak.group(0))
    return True, ("falsifier pointed at by version DOI + section, explicitly not "
                  "restated, and no numeric value asserted for it")


# ------------------------------------------------------------ R8
def check_szeta_tag_separate(text):
    """Ruling 8: own tag, kept distinct, with the non-implication both ways."""
    body = flat(text)
    if "`op:cc-szeta-closed-form`" not in body:
        return False, "the new tag op:cc-szeta-closed-form is not present"
    if "new at v1.7" not in body.lower():
        return False, "the tag is not declared new at v1.7"
    if "not\nunder `op:cc-stokes-closed-form`" not in text and \
       "not under `op:cc-stokes-closed-form`" not in body:
        return False, "the notice does not say the negative is NOT filed under the v1.5 tag"

    # The non-implication must be stated in BOTH directions, or the separation
    # is an assertion rather than an argument.
    if "neither implies the other" not in body:
        return False, "the non-implication is not stated"
    if "could have a closed form with the identification false" not in body:
        return False, "the first direction of the non-implication is missing"
    if "identification could hold with `C` outside every Gamma basis" not in body:
        return False, "the second direction of the non-implication is missing"
    if "must not be cited as" not in body:
        return False, "the notice does not forbid citing the negative against the other tag"
    return True, ("own tag, declared new, kept distinct, non-implication stated "
                  "in both directions, mis-citation forbidden")


# ------------------------------------------------------------ W (watch item)
def check_degree_d_not_closed(text):
    """The operator's watch item: section 2 must not read as closing the problem."""
    body = flat(text)
    if "What §2 does not close" not in body:
        return False, "section 2 carries no statement of what it does not close"
    if "analytic residual is open" not in body:
        return False, "the analytic residual is not stated as open"
    if "its name is `op:xi0-singularity-type`" not in body:
        return False, "the open residual is not named"
    if "must not be reported as closed" not in body:
        return False, "the notice does not forbid reporting op:xi0-degree-d as closed"
    # and the section-7 row must agree with the section-2 statement
    if "is **not** closed by §2" not in body:
        return False, "the section 7 row no longer agrees with section 2"
    return True, ("section 2 states the residual open, names it, and forbids "
                  "reporting the problem closed; section 7 agrees")


# ------------------------------------------------------------ R9 (corpus, not notice)
def check_s3a06_narrowed(_text):
    """Ruling 9, checked where the change actually landed: the claims record."""
    path = os.path.join(SESSIONS, "CT-S3A-ZETA-AUDIT", "claims.jsonl")
    if not os.path.exists(path):
        return False, "CT-S3A-ZETA-AUDIT/claims.jsonl not found"
    raw = open(path, "rb").read().decode("utf-8").replace("\r\n", "\n")
    rows = [json.loads(l) for l in raw.split("\n") if l.strip()]

    # reader integrity: assert a known-present feature before judging absence
    if not rows or not all("claim_id" in r for r in rows):
        return False, "claims file did not parse as expected: read is suspect"

    hit = [r for r in rows if r.get("claim_id") == "S3A-06"]
    if len(hit) != 1:
        return False, "expected exactly one S3A-06, found %d" % len(hit)
    c = hit[0]
    if "claim_before_s26c" not in c:
        return False, "S3A-06 has not been narrowed (no claim_before_s26c)"
    if c.get("narrowed_not_retracted") is not True:
        return False, "the amendment is not flagged as a narrowing"
    if c.get("label") != "INSPECTED":
        return False, "label moved to %r; a narrowing must not move the label" % c.get("label")
    for needed in ("v1.3.1 LaTeX LABEL/SOURCE SET",
                   "PRESENT IN THE DEPOSITED PROSE",
                   "does not match the v1.3.1 label set"):
        if needed not in c["claim"]:
            return False, "narrowed text missing %r" % needed
    if "CT-S26-CTV17-DRAFT" not in c.get("amended_in", ""):
        return False, "the amending session is not named"
    if "CT-R1-AUDIT/R2" not in c.get("amended_in", ""):
        return False, "the earlier amendment trail was dropped"
    return True, ("S3A-06 narrowed to the artefact inspected, label unchanged, "
                  "superseded text retained, trail intact")


# ------------------------------------------------------------ wiring
def install():
    """Replace one revision-2 check and append the ruling checks."""
    name_tags = "every op:/rem: tag exists in the deposited record"
    for i, (name, _fn) in enumerate(r2.CHECKS):
        if name == name_tags:
            r2.CHECKS[i] = (name_tags, check_obligation_tags_are_real_v3)
            break
    else:
        raise SystemExit("FATAL: revision-2 tag check not found; refusing to run")

    # Three mutants where revision 2 had one, because the check was loosened.
    r2.MUTANTS[name_tags] = [
        # 1. an existing tag renamed -- the original control, unchanged
        lambda t: t.replace("`op:xi0-singularity-type`", "`op:xi0-type-of-singularity`"),
        # 2. a tag invented outright, never declared new
        lambda t: t.replace("`op:cc-formal-borel`", "`op:cc-formal-borel-II`"),
        # 3. the new tag stripped of the declaration that legitimises it
        lambda t: t.replace("**OPEN; new at v1.7.**", "**OPEN.**"),
    ]

    added = [
        ("R4 no forward reference to an undeposited document",
         check_no_forward_reference,
         [lambda t: t.replace(
             "No forward reference is made to any undeposited document",
             "A forward reference is made to the forthcoming paper"),
          lambda t: t.replace("until then this notice cites only records that exist",
                              "see the forthcoming paper")]),
        ("R5 Wong-Li II left NOT OBTAINED and not gating",
         check_wongli_not_gating,
         [lambda t: t.replace("not gated on obtaining it", "waiting on it"),
          lambda t: t.replace("priority position stated here must not be softened",
                              "priority position may be revisited")]),
        ("R7 falsifier pointed at, not restated",
         check_falsifier_pointed_not_restated,
         [lambda t: t.replace("§9 of version `10.5281/zenodo.22782807`",
                              "the relevant section of the PDF"),
          lambda t: t.replace("Pointing at unread text is\n> accurate;",
                              "That is the operative constraint;"),
          lambda t: t.replace("> that is the citation a reader should follow.",
                              "> the v1.6 falsifier threshold is 30 digits.")]),
        ("R8 S_zeta* negative carries its own tag, kept distinct",
         check_szeta_tag_separate,
         [lambda t: t.replace("`op:cc-szeta-closed-form`", "`op:cc-stokes-closed-form`"),
          lambda t: t.replace("neither implies the other", "each implies the other"),
          lambda t: t.replace(
              "could have a closed form with the identification false",
              "would follow from the identification")]),
        ("W op:xi0-degree-d is not reported as closed",
         check_degree_d_not_closed,
         [lambda t: t.replace("What §2 does not close", "What §2 settles"),
          lambda t: t.replace("must not be reported as closed",
                              "may now be reported as closed"),
          lambda t: t.replace("its name is `op:xi0-singularity-type`",
                              "it is a further question")]),
    ]
    for name, fn, muts in added:
        r2.CHECKS.append((name, fn))
        r2.MUTANTS[name] = muts

    # R9 is deliberately NOT appended to r2.CHECKS.  It reads the corpus claims
    # record, not the notice, so the SECTION 2 machinery -- which mutates the
    # notice text -- cannot supply a can-fail control for it.  A mutant that the
    # check cannot see is not a control.  R9 runs in SECTION 4 instead, against
    # a mutated copy of the record itself.


def corpus_control():
    """Can-fail control for R9: strip the narrowing from a copy and re-check."""
    real = os.path.join(SESSIONS, "CT-S3A-ZETA-AUDIT", "claims.jsonl")
    raw = open(real, "rb").read().decode("utf-8").replace("\r\n", "\n")
    rows = [json.loads(l) for l in raw.split("\n") if l.strip()]
    stripped = []
    for c in rows:
        if c.get("claim_id") == "S3A-06":
            c = dict(c)
            c["claim"] = c.pop("claim_before_s26c")
            c.pop("narrowed_not_retracted", None)
        stripped.append(c)
    tmp = os.path.join(SESSION, "outputs", "_r9_control.jsonl")
    with open(tmp, "w", encoding="utf-8") as fh:
        for c in stripped:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    backup = real + ".realtmp"
    os.rename(real, backup)
    os.rename(tmp, real)
    try:
        ok, detail = check_s3a06_narrowed(None)
    finally:
        os.rename(real, tmp)
        os.rename(backup, real)
        os.remove(tmp)
    return (not ok), detail


def main():
    install()
    print("=" * 74)
    print("verify_notice_rev3.py -- revision-2 checks PLUS the 2026-09-19 rulings")
    print("  revision-2 checks, mutants and reader controls run unchanged;")
    print("  one check (obligation tags) was LOOSENED to admit a tag the notice")
    print("  declares new, and carries 3 mutants where it carried 1.")
    print("=" * 74)
    print()
    rc = r2.main()

    print()
    print("SECTION 4 -- R9, checked against the corpus record, with its own control")
    print("-" * 74)
    print("  R9 reads sessions/2026-09-17/CT-S3A-ZETA-AUDIT/claims.jsonl, not the")
    print("  notice, so SECTION 2's notice mutants cannot reach it.  Its control")
    print("  mutates the record: the narrowing is stripped from a copy and the")
    print("  check must reject it.")
    ok9, detail9 = check_s3a06_narrowed(None)
    print("  [%s] R9 claim S3A-06 narrowed to the artefact inspected -- %s"
          % ("PASS" if ok9 else "FAIL", detail9))
    fired, detail = corpus_control()
    print("  [%s] control: R9 rejects the record with the narrowing removed -- %s"
          % ("PASS" if fired else "BROKEN", detail))
    print()
    print("=" * 74)
    good = (rc == 0) and ok9 and fired
    print("VERDICT (rev3): %s" % ("OK" if good else "FAIL"))
    print("=" * 74)
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
