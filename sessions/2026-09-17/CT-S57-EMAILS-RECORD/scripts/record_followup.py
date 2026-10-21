#!/usr/bin/env python3
"""CT-S57: record the follow-up email (items 4 and 5) sent to the LMP editor.

Record only. Nothing sent, deposited, uploaded or committed.

This APPENDS to claims.jsonl. It never rewrites the five claims already there:
those record the first email and are not this script's business. It refuses if
appending would disturb them.

Exit codes: 0 written / 2 refusal / 3 crash.
"""
import datetime as dt
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
EMAIL = SESS / "email" / "followup_as_sent.txt"
FIRST = SESS / "email" / "email_as_sent.txt"
META = SESS / "email" / "META.json"
REC = SESS / "claims.jsonl"
OUT = SESS / "outputs" / "record_followup.out.txt"

CONCEPT = "20719042"
SUBMISSION_ID = "MATH-D-26-00523"
FIRST_SHA = "9bdcd347505999fdfb269ca0b632b23d83c25245e55fac066f565cd29a0572a0"

L: list[str] = []


def say(s: str = "") -> None:
    L.append(s)
    print(s)


def flush() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")


def refuse(why: str) -> None:
    say()
    say("REFUSED: " + why)
    say("No claim was written.")
    # A refusal must not overwrite the log of the successful run it is
    # declining to repeat. Re-running this script for idempotency did exactly
    # that once, destroying the only record of the write that produced the
    # claims. Refusals get their own file.
    global OUT
    OUT = OUT.with_name(OUT.stem + ".refused.txt")
    flush()
    sys.exit(2)


def zenodo_versions() -> list[dict]:
    url = ("https://zenodo.org/api/records?q=conceptrecid:"
           f"{CONCEPT}&all_versions=true&size=25")
    with urllib.request.urlopen(url, timeout=60) as fh:
        data = json.loads(fh.read().decode("utf-8"))
    return [{"id": h["id"], "doi": h["doi"],
             "version": h["metadata"].get("version"),
             "publication_date": h["metadata"].get("publication_date"),
             "updated": h.get("updated")}
            for h in data["hits"]["hits"]]


def main() -> int:
    say("=" * 74)
    say(f"CT-S57 -- follow-up to the LMP editor, {SUBMISSION_ID}")
    say("=" * 74)
    say("record only. Nothing sent, deposited, uploaded or committed.")
    say()

    if not EMAIL.exists():
        refuse(f"no follow-up text at {EMAIL}. It must be pasted verbatim; "
               "this agent has no mail access and will not reconstruct it.")
    raw = EMAIL.read_bytes()
    if not raw.strip():
        refuse("the follow-up file is empty")
    txt = raw.decode("utf-8", errors="replace")
    h = hashlib.sha256(raw).hexdigest()
    say(f"follow-up text: {len(raw)} bytes, sha256 {h}")

    # ---- the first email must be untouched by the split that produced this
    if not FIRST.exists():
        refuse(f"the first email is missing at {FIRST}")
    fh = hashlib.sha256(FIRST.read_bytes()).hexdigest()
    say(f"first email    : {FIRST.stat().st_size} bytes, sha256 {fh}")
    if fh != FIRST_SHA:
        refuse("the first email no longer hashes to the value its five "
               "existing claims cite; splitting the two emails apart "
               "disturbed it. Fix that before recording the follow-up.")
    say("[ok] the first email is byte-identical to what the existing claims "
        "cite")
    say()

    meta = json.loads(META.read_text(encoding="utf-8"))
    sent = dt.date.fromisoformat(meta["date_sent"])
    say(f"date sent (operator-supplied): {sent.isoformat()}")
    say(f"via: {meta['via']}")
    say()

    # ---- F1: it is the follow-up, not a second copy of the first email
    say("[F1] the text is the follow-up, not the first email again")
    SUBJ = "Subject: MATH-D-26-00523: item 4 resolved, and one further correction"
    if not txt.lstrip().startswith(SUBJ):
        refuse("the text does not begin with the follow-up's subject line")
    if h == FIRST_SHA:
        refuse("the follow-up file is byte-identical to the first email")
    say("  subject line matches; content differs from the first email")
    say()

    # ---- F2: it carries items 4 and 5, and no others
    say("[F2] item numbering")
    nums = sorted({int(m.group(1)) for m in
                   re.finditer(r"^\s*(\d)\.\s", txt, re.M)})
    say(f"  numbered items found: {nums}")
    if nums != [4, 5]:
        refuse(f"expected items [4, 5], found {nums}. The follow-up's "
               "numbering is not what the record would assert.")
    say("  continues the first email's numbering, as intended")
    say()

    # ---- F3: item 4 is RESOLVED here (the first email sent it UNRESOLVED)
    say("[F3] item 4 resolution state")
    brackets = re.findall(r"\[If [^\]]{0,120}\]", txt)
    say(f"  bracketed conditional alternatives present: {len(brackets)}")
    for b in brackets:
        say(f"    {b}")
    says_log = bool(re.search(r"carries a logarithm|one local solution carries",
                              txt, re.I))
    says_not_apparent = bool(re.search(r"is not an apparent singularity", txt,
                                       re.I))
    say(f"  asserts a logarithm is present : {says_log}")
    say(f"  asserts xi=0 is not apparent   : {says_not_apparent}")
    if brackets:
        state = "UNRESOLVED"
    elif says_log and says_not_apparent:
        state = "RESOLVED-LOGARITHM-FOUND"
    else:
        refuse("item 4's state cannot be read from the text: no bracketed "
               "alternatives remain, but the text does not assert the "
               "logarithm case either. Refusing to guess.")
    say(f"  => item 4 state: {state}")
    if state != "RESOLVED-LOGARITHM-FOUND":
        refuse(f"item 4 is {state} in the follow-up. The follow-up exists to "
               "resolve it; recording it as unresolved would contradict the "
               "reason it was sent. Report this instead.")
    say()

    # ---- F4: item 5's substance
    say("[F4] item 5 substance")
    figs = {"8.84": "8.84" in txt, "9.31": "9.31" in txt, "3.7": "3.7" in txt}
    for k, v in figs.items():
        say(f"  figure {k} present: {v}")
    if not all(figs.values()):
        refuse("item 5 does not carry all three figures the record would "
               f"assert: {figs}")
    say()

    # ---- F5: Zenodo, still not updated
    say(f"[F5] Zenodo concept {CONCEPT} not updated since the emails")
    try:
        vs = zenodo_versions()
    except Exception as e:  # noqa: BLE001
        refuse(f"could not query Zenodo: {type(e).__name__}: {e}. The "
               '"not updated" claim cannot be checked, so it is not written.')
    if len(vs) < 2:
        refuse(f"the version query returned {len(vs)} version(s); "
               '"no version after D" cannot be distinguished from "the query '
               'returns nothing".')
    vs.sort(key=lambda v: str(v["publication_date"]))
    for v in vs:
        say(f"    id={v['id']}  v{v['version']}  "
            f"pub={v['publication_date']}  updated={v['updated']}")
    after = [v for v in vs if str(v["publication_date"]) > sent.isoformat()]
    say(f"  versions published after {sent.isoformat()}: {len(after)}")
    if after:
        refuse("a version was published after the emails were sent; the "
               '"deliberately not updated" claim is false as stated.')
    latest = vs[-1]
    say()

    # ---- build claims
    def C(cid, claim, evidence, extra=None):
        d = {"claim_id": cid, "task_id": "CT-S57-EMAILS-RECORD",
             "claim": claim, "label": "INSPECTED",
             "evidence_type": "file_inspection", "dps": None,
             "reproducible": True,
             "script": "scripts/record_followup.py",
             "email_file": "email/followup_as_sent.txt",
             "email_sha256": h, "evidence": evidence}
        if extra:
            d.update(extra)
        return d

    C_ = [
        C("S57-F01",
          f"A follow-up to the author's correction for {SUBMISSION_ID} "
          f"(Letters in Mathematical Physics) was sent on {sent.isoformat()} "
          f"via the Editorial Manager Send E-mail function. The date is "
          f"OPERATOR-SUPPLIED ('both went out today', {sent.isoformat()}); "
          "this agent has no mail access and derived it from no header.",
          "email/META.json; operator statement"),
        C("S57-F02",
          "The follow-up text exactly as sent is saved at "
          f"email/followup_as_sent.txt ({len(raw)} bytes) and is hashed in "
          "this record. It was separated from email_as_sent.txt, into which "
          "it had been pasted, by scripts/split_emails.py, which refused "
          "until the remaining first email reproduced the sha256 the five "
          "existing claims cite.",
          "scripts/split_emails.py output; byte-level split verified "
          "against the recorded hash"),
        C("S57-F03",
          "The follow-up carries exactly two numbered items, 4 and 5, "
          "continuing the numbering of the first email.",
          f"numbered items read from the text as sent: {nums}"),
        C("S57-F04",
          "Item 4 is RESOLVED in the follow-up: no bracketed conditional "
          "alternatives remain, and the text asserts that xi = 0 is not an "
          "apparent singularity and that one local solution carries a "
          "logarithm. The first email sent item 4 UNRESOLVED with both "
          "alternatives (claim S53-03); this follow-up settles it on the "
          "editor's side, and settles it to the alternative that the "
          "CT-S52 computation supports.",
          "0 bracketed alternatives; logarithm and non-apparency both "
          "asserted in the text as sent"),
        C("S57-F05",
          "Item 5 is new in the follow-up and states that Methods B and C "
          "were not independent as implemented, quoting 8.84e-46 for the "
          "collapsed comparison, 9.31e-46 for Method C's separate "
          "comparison, and 3.7e-46 for the stream-extracted-amplitude "
          "reconstruction of S.",
          "all three figures read from the text as sent"),
        C("S57-F06",
          "No reply from the editor has been received as of this recording. "
          "OPERATOR-SUPPLIED: this agent has no mail access and cannot check "
          "an inbox.",
          "operator statement; not independently checkable by this agent"),
        C("S57-F07",
          f"The Zenodo record under concept 10.5281/zenodo.{CONCEPT} has "
          "deliberately NOT been updated pending the editor's reply. CHECKED "
          f"against the Zenodo REST API: {len(vs)} versions exist, the latest "
          f"being v{latest['version']} (record {latest['id']}) published "
          f"{latest['publication_date']}; no version has been published since "
          f"the emails were sent on {sent.isoformat()}. The word "
          '"deliberately" is OPERATOR-SUPPLIED intent; what is checked is '
          "that no update occurred.",
          "Zenodo REST API, conceptrecid:" + CONCEPT,
          {"zenodo_versions": vs}),
    ]

    # ---- validate BEFORE writing
    say("validating before the write")
    existing = []
    if REC.exists():
        existing = [json.loads(x) for x in
                    REC.read_text(encoding="utf-8").splitlines() if x.strip()]
    have = {c["claim_id"] for c in existing}
    problems = []
    seen = set()
    for c in C_:
        cid = c["claim_id"]
        if cid in have:
            problems.append(f"{cid} already present in claims.jsonl")
        if cid in seen:
            problems.append(f"duplicate {cid}")
        seen.add(cid)
        if c["label"] != "INSPECTED":
            problems.append(f"{cid}: label must be INSPECTED")
        if not c["claim"].strip():
            problems.append(f"{cid}: empty claim")
        if len(c["email_sha256"]) != 64:
            problems.append(f"{cid}: bad email hash")
        if not c.get("evidence", "").strip():
            problems.append(f"{cid}: empty evidence")
    if len(existing) != 5:
        problems.append(f"expected 5 existing claims, found {len(existing)}; "
                        "refusing to append to a record I do not recognise")
    if problems:
        for p in problems:
            say("  PROBLEM: " + p)
        refuse("validation failed before the write")
    say(f"  {len(C_)} new claims validated; {len(existing)} existing claims "
        "will be preserved unchanged")
    say()

    before = REC.read_bytes() if REC.exists() else b""
    with REC.open("a", encoding="utf-8", newline="\n") as fhandle:
        for c in C_:
            fhandle.write(json.dumps(c) + "\n")

    after_b = REC.read_bytes()
    if not after_b.startswith(before):
        refuse("the append disturbed the existing claims; this should be "
               "impossible and must be investigated")
    say(f"appended {len(C_)} claims; the {len(existing)} existing claims are "
        "byte-unchanged at the head of the file")
    for c in C_:
        say(f"  {c['claim_id']}  INSPECTED")
    say()
    say("Nothing sent, deposited, uploaded or committed.")
    flush()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        say(f"CRASH: {type(e).__name__}: {e}")
        flush()
        sys.exit(3)
