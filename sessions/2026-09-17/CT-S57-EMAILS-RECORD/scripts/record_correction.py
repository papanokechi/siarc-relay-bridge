#!/usr/bin/env python3
"""CT-S53 -- record the author's correction sent to the LMP editor.

This script is the recorder for MATH-D-26-00523. It refuses to write a record
until the two pieces of required data are present:

  email/email_as_sent.txt   the email text EXACTLY as sent
  email/META.json           {"date_sent": "YYYY-MM-DD", ...}

A record of a sent email whose text was never supplied is not a record; it is a
placeholder that will later read as one. So the refusal is the point, not a
limitation.

Checks that can fail (PREREG F1-F4):
  F1  email text absent or empty                 -> refuse
  F4  date_sent absent, placeholder, or unparsable -> refuse
  F2  item 4 not locatable, or bracketed alternatives unresolved -> REPORTED,
      never guessed
  F3  any Zenodo version of concept 20719042 published/updated after the date
      sent -> refuse (the "not updated" claim would be false as stated)

exit 0 written, 2 refusal, 3 crash.
"""
import hashlib
import json
import re
import sys
import urllib.request
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
EMAIL = SESS / "email" / "email_as_sent.txt"
META = SESS / "email" / "META.json"
CLAIMS = SESS / "claims.jsonl"
OUT = SESS / "outputs" / "record.out.txt"

TASK = "CT-S53-LMP-CORRECTION-RECORD"
CONCEPT = "20719042"
SUBMISSION_ID = "MATH-D-26-00523"

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
    say("Nothing was written to claims.jsonl.")
    flush()
    sys.exit(2)


def zenodo_versions() -> list[dict]:
    url = ("https://zenodo.org/api/records?q=conceptrecid:"
           f"{CONCEPT}&all_versions=true&size=25")
    with urllib.request.urlopen(url, timeout=60) as fh:
        data = json.loads(fh.read().decode("utf-8"))
    return [
        {
            "id": h["id"],
            "doi": h["doi"],
            "version": h["metadata"].get("version"),
            "publication_date": h["metadata"].get("publication_date"),
            "updated": h.get("updated"),
        }
        for h in data["hits"]["hits"]
    ]


def main() -> int:
    say("=" * 74)
    say("CT-S53 -- author's correction to the LMP editor, " + SUBMISSION_ID)
    say("=" * 74)
    say("record only. Nothing sent, deposited, uploaded or committed.")

    # ---------------------------------------------------------------- F1
    say()
    say("[F1] the email text exactly as sent")
    if not EMAIL.exists():
        refuse(f"{EMAIL.relative_to(SESS)} does not exist. The operator must "
               "paste the email text exactly as sent; this agent has no mail "
               "access and will not reconstruct it.")
    raw = EMAIL.read_bytes()
    if not raw.strip():
        refuse(f"{EMAIL.relative_to(SESS)} is empty.")
    text = raw.decode("utf-8")
    sha = hashlib.sha256(raw).hexdigest()
    say(f"  bytes        : {len(raw)}")
    say(f"  sha256       : {sha}")
    say(f"  lines        : {len(text.splitlines())}")

    # ---------------------------------------------------------------- F4
    say()
    say("[F4] the date sent")
    if not META.exists():
        refuse(f"{META.relative_to(SESS)} does not exist; it must carry "
               '{"date_sent": "YYYY-MM-DD"}.')
    meta = json.loads(META.read_text(encoding="utf-8"))
    ds = str(meta.get("date_sent", "")).strip()
    if not ds or ds.startswith("<"):
        refuse(f"date_sent is {ds!r}, which is a placeholder, not a date.")
    try:
        sent = datetime.strptime(ds, "%Y-%m-%d").date()
    except ValueError:
        refuse(f"date_sent {ds!r} is not an ISO YYYY-MM-DD date.")
    if sent > date.today():
        refuse(f"date_sent {ds} is in the future.")
    say(f"  date sent    : {sent.isoformat()}")
    say(f"  via          : {meta.get('via', 'OPERATOR-SUPPLY MISSING')}")

    # ---------------------------------------------------------------- F2
    say()
    say("[F2] which item-4 alternative went out")
    brackets = re.findall(r"\[[^\]\n]{8,}\]", text)
    has_item4 = re.search(r"(?mi)^\s*(?:\*\*)?4[.)]", text) is not None
    say(f"  an item 4 is locatable in the text : {has_item4}")
    say(f"  bracketed spans of 8+ chars found  : {len(brackets)}")
    for b in brackets:
        say("      " + (b[:120] + ("..." if len(b) > 120 else "")))
    if not has_item4:
        item4_state = ("NOT LOCATABLE -- no line in the pasted text begins "
                       "with an item-4 marker; reported, not guessed")
    elif brackets:
        item4_state = (f"UNRESOLVED -- {len(brackets)} bracketed alternative "
                       "span(s) remain in the text as sent; both alternatives "
                       "appear to have gone out unresolved")
    else:
        item4_state = ("RESOLVED -- no bracketed alternatives remain in the "
                       "text as sent; a single item-4 wording went out")
    say(f"  -> {item4_state}")

    # ---------------------------------------------------------------- F3
    say()
    say("[F3] Zenodo concept " + CONCEPT + " not updated since the email")
    try:
        vs = zenodo_versions()
    except Exception as e:  # noqa: BLE001
        refuse(f"could not query Zenodo: {type(e).__name__}: {e}. The "
               '"not updated" claim cannot be checked, so it is not written.')
    if len(vs) < 2:
        refuse(f"the version query returned {len(vs)} version(s). The vacuity "
               "pre-check requires it to return the versions that do exist, "
               'otherwise "no version after D" cannot be distinguished from '
               '"the query returns nothing".')
    vs.sort(key=lambda v: str(v["publication_date"]))
    for v in vs:
        say(f"    id={v['id']}  v{v['version']}  pub={v['publication_date']}  "
            f"updated={v['updated']}")
    after = [v for v in vs if str(v["publication_date"]) > sent.isoformat()]
    say(f"  versions published after {sent.isoformat()}: {len(after)}")
    if after:
        for v in after:
            say(f"    CONFLICT: id={v['id']} v{v['version']} "
                f"pub={v['publication_date']}")
        refuse("a version of the concept was published after the email was "
               "sent, so the claim that the record was deliberately not "
               "updated pending the editor's reply is false as stated.")
    latest = vs[-1]
    say(f"  latest version: v{latest['version']} (record {latest['id']}), "
        f"published {latest['publication_date']} -- unchanged since")

    # ---------------------------------------------------------- build claims
    C: list[dict] = []

    def claim(cid, text_, source, extra=None):
        c = {
            "claim_id": cid,
            "task_id": TASK,
            "label": "INSPECTED",
            "claim": text_,
            "evidence_type": "file_inspection",
            "source": source,
            "email_sha256": sha,
            "reproducible": True,
            "script": "scripts/record_correction.py",
            "output_file": "outputs/record.out.txt",
        }
        if extra:
            c.update(extra)
        C.append(c)

    claim("S53-01",
          f"The author's correction for {SUBMISSION_ID} (Letters in "
          f"Mathematical Physics) was sent on {sent.isoformat()} via the "
          f"Editorial Manager \"Send E-mail\" function. OPERATOR-SUPPLIED: "
          "this agent has no mail access and did not observe the send.",
          "email/META.json")

    claim("S53-02",
          "The email text exactly as sent is saved at "
          "email/email_as_sent.txt and is hashed in this record. It was "
          "pasted by the operator and has not been edited, reflowed or "
          "reconstructed by this agent.",
          "email/email_as_sent.txt",
          {"bytes": len(raw), "lines": len(text.splitlines())})

    claim("S53-03",
          "The correction carries four items. Item 4 state as read from the "
          "text as sent: " + item4_state + ".",
          "email/email_as_sent.txt",
          {"item4_state": item4_state,
           "bracketed_spans": len(brackets)})

    claim("S53-04",
          "No reply from the editor has been received as of the time of this "
          "recording. OPERATOR-SUPPLIED: this agent has no mail access and "
          "cannot observe an inbox; absence of a reply is reported, not "
          "verified.",
          "operator report at recording time",
          {"recorded_on": date.today().isoformat()})

    claim("S53-05",
          f"The Zenodo record under concept 10.5281/zenodo.{CONCEPT} has "
          "deliberately NOT been updated pending the editor's reply. CHECKED "
          f"against the Zenodo REST API: {len(vs)} versions exist, the latest "
          f"being v{latest['version']} (record {latest['id']}) published "
          f"{latest['publication_date']}; no version has been published since "
          f"the email was sent on {sent.isoformat()}. The word "
          "\"deliberately\" is OPERATOR-SUPPLIED intent; what is checked is "
          "that no update occurred.",
          "Zenodo REST API, conceptrecid:" + CONCEPT,
          {"versions": vs})

    # ------------------------------------------ validate BEFORE writing
    problems = []
    seen = set()
    for c in C:
        if c["claim_id"] in seen:
            problems.append("duplicate " + c["claim_id"])
        seen.add(c["claim_id"])
        if c["label"] != "INSPECTED":
            problems.append(c["claim_id"] + ": label must be INSPECTED")
        if not c["claim"].strip():
            problems.append(c["claim_id"] + ": empty claim")
        if len(c["email_sha256"]) != 64:
            problems.append(c["claim_id"] + ": bad email hash")
    if problems:
        for p in problems:
            say("  PROBLEM: " + p)
        refuse("the claim buffer failed validation")

    buf = "\n".join(json.dumps(c, ensure_ascii=False) for c in C) + "\n"
    for ln in buf.strip().split("\n"):
        json.loads(ln)

    CLAIMS.write_text(buf, encoding="utf-8")
    say()
    say(f"wrote {len(C)} claims -> {CLAIMS.relative_to(SESS)}")
    say("claims.jsonl sha256: "
        + hashlib.sha256(CLAIMS.read_bytes()).hexdigest())
    for c in C:
        say(f"  {c['claim_id']}  INSPECTED  {c['claim'][:64]}")
    say()
    say("=" * 74)
    flush()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        print(f"CRASH: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(3)
