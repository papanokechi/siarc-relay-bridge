#!/usr/bin/env python3
"""CT-S57: re-verify every claim in claims.jsonl against the files on disk.

Why this exists. On 2026-09-21 the follow-up email was pasted into
email/email_as_sent.txt, the file the five existing claims hash. The record's
sha256 went stale the moment that write landed, and NOTHING in this session
noticed: the recorder had already exited 0, and a recorder cannot detect a
write that happens after it. Only a check that re-reads both sides from disk,
later, can.

This script therefore takes NOTHING from the recorders. It re-reads
claims.jsonl from disk, re-hashes each cited email file from disk, and
compares. Run it LAST, and run it again any time the email files are touched.

Exit codes: 0 all consistent / 1 a claim is stale / 2 refusal.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REC = SESS / "claims.jsonl"
OUT = SESS / "outputs" / "verify_claims_s57.out.txt"

L: list[str] = []


def say(s: str = "") -> None:
    L.append(s)
    print(s)


def flush() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")


def main() -> int:
    say("=" * 74)
    say("CT-S57 -- post-hoc verification of the email record")
    say("=" * 74)
    say("Re-reads claims.jsonl and every cited email file from disk. Takes no")
    say("value from any recorder.")
    say()

    if not REC.exists():
        say("REFUSED: no claims.jsonl")
        flush()
        return 2
    rows = [json.loads(x) for x in
            REC.read_text(encoding="utf-8").splitlines() if x.strip()]
    if not rows:
        say("REFUSED: claims.jsonl is empty; 'nothing stale' would be "
            "indistinguishable from 'nothing checked'")
        flush()
        return 2
    say(f"claims on disk: {len(rows)}")
    say()

    bad = 0
    checked_hash = 0
    files_seen: dict[str, str] = {}

    # Every email file on disk, indexed by its digest. The five CT-S53 claims
    # cite a hash but no filename; requiring both keys made this check SKIP
    # exactly the rows that went stale, which is the defect it exists to
    # catch wearing a different hat. A hash with no filename is still
    # decidable: it either matches some email file on disk or it matches
    # none, and "none" is precisely staleness.
    EMAILDIR = SESS / "email"
    on_disk: dict[str, str] = {}
    for p in sorted(EMAILDIR.glob("*.txt")):
        on_disk[hashlib.sha256(p.read_bytes()).hexdigest()] = \
            p.relative_to(SESS).as_posix()
    say(f"email files on disk: {len(on_disk)}")
    for d, rel in sorted(on_disk.items(), key=lambda kv: kv[1]):
        say(f"    {rel}  {(SESS / rel).stat().st_size} B  {d[:16]}")
    if not on_disk:
        say("REFUSED: no email files on disk to check against")
        flush()
        return 2
    say()

    say("--- per-claim: cited hash vs the file on disk ---")
    for c in rows:
        cid = c["claim_id"]
        rel = c.get("email_file")
        cited = c.get("email_sha256")
        if not cited:
            say(f"  {cid}  cites no hash -- nothing to check")
            continue
        checked_hash += 1
        if rel:
            p = SESS / rel
            if not p.exists():
                say(f"  {cid}  MISSING FILE {rel}")
                bad += 1
                continue
            actual = hashlib.sha256(p.read_bytes()).hexdigest()
            files_seen[rel] = actual
            if actual == cited:
                say(f"  {cid}  ok    {rel}  {p.stat().st_size} B")
            else:
                say(f"  {cid}  STALE {rel}  {p.stat().st_size} B")
                say(f"        cited   {cited}")
                say(f"        on disk {actual}")
                bad += 1
        else:
            # no filename: resolve the digest against every email file
            match = on_disk.get(cited)
            if match:
                files_seen[match] = cited
                say(f"  {cid}  ok    (no filename cited; the digest is "
                    f"{match} on disk)")
            else:
                say(f"  {cid}  STALE (no filename cited, and NO email file "
                    "on disk has this digest)")
                say(f"        cited {cited}")
                bad += 1
    say(f"  {checked_hash} of {len(rows)} claim(s) carried a hash to check")
    if checked_hash == 0:
        say("REFUSED: no claim cited a hash, so this check could not fail")
        flush()
        return 2
    say()

    # ---- label discipline
    say("--- labels ---")
    labels: dict[str, int] = {}
    for c in rows:
        labels[c.get("label", "<none>")] = labels.get(c.get("label", "<none>"),
                                                      0) + 1
    for k, v in sorted(labels.items()):
        say(f"  {k}: {v}")
    for c in rows:
        if c.get("label") != "INSPECTED":
            say(f"  PROBLEM: {c['claim_id']} is not INSPECTED")
            bad += 1
    say()

    # ---- the substance each claim asserts must still be in the file it cites
    say("--- substance: assertions re-read from the cited text ---")
    probes = [
        ("S53-03", "email/email_as_sent.txt",
         r"\[If the log check finds no logarithms:\]", True,
         "the first email's item 4 carries its bracketed alternatives"),
        ("S57-F03", "email/followup_as_sent.txt",
         r"^\s*5\.\s", True, "the follow-up carries an item 5"),
        ("S57-F04", "email/followup_as_sent.txt",
         r"\[If ", False, "the follow-up carries NO bracketed alternative"),
        ("S57-F04", "email/followup_as_sent.txt",
         r"is not an apparent singularity", True,
         "the follow-up asserts non-apparency"),
        ("S57-F05", "email/followup_as_sent.txt",
         r"3\.7 x 10\^-46", True,
         "the follow-up quotes the stream-extracted reconstruction"),
    ]
    have = {c["claim_id"] for c in rows}
    for cid, rel, pat, want, what in probes:
        if cid not in have:
            say(f"  {cid}  not in the record -- probe skipped")
            continue
        p = SESS / rel
        if not p.exists():
            say(f"  {cid}  MISSING FILE {rel}")
            bad += 1
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        n = len(re.findall(pat, txt, re.M))
        got = n > 0
        if got == want:
            say(f"  {cid}  ok    {what} (hits={n})")
        else:
            say(f"  {cid}  FAIL  {what} (hits={n}, expected "
                f"{'>0' if want else '0'})")
            bad += 1
    say()

    # ---- control: the hash check must be able to fail
    say("--- control: a one-byte perturbation must be detected ---")
    fired = 0
    for rel, actual in sorted(files_seen.items()):
        mutated = hashlib.sha256((SESS / rel).read_bytes() + b"x").hexdigest()
        if mutated != actual:
            fired += 1
            say(f"  {rel}: appending one byte changes the digest -- the "
                "comparison discriminates")
        else:
            say(f"  {rel}: CONTROL DID NOT FIRE")
    if fired != len(files_seen):
        say("REFUSED: the control did not fire for every cited file")
        flush()
        return 2
    if fired == 0:
        if bad:
            say("  no file resolved, because every cited digest is stale; "
                "the finding below is the reason, not a starved control")
        else:
            say("REFUSED: no file was checked and nothing was found wrong; "
                "that combination cannot be told from a check that did "
                "nothing")
            flush()
            return 2
    say()

    # The unkeyed path is the one that silently skipped the five CT-S53
    # claims in this script's first version. Prove it discriminates.
    say("--- control: the no-filename path must reject an absent digest ---")
    absent = hashlib.sha256(b"a digest no email file on disk has").hexdigest()
    if absent in on_disk:
        say("REFUSED: the synthetic absent digest is present on disk")
        flush()
        return 2
    say(f"  synthetic digest {absent[:16]} resolves to None -> would be "
        "reported STALE")
    present = next(iter(on_disk))
    if on_disk.get(present) is None:
        say("REFUSED: a digest that IS on disk failed to resolve")
        flush()
        return 2
    say(f"  real digest      {present[:16]} resolves to "
        f"{on_disk[present]} -> ok")
    say("  the path separates present from absent; it cannot pass everything")
    say()

    say("=" * 74)
    if bad:
        say(f"FINDING: {bad} problem(s). The record does not describe the "
            "files on disk.")
        flush()
        return 1
    say(f"All {len(rows)} claims consistent with the files on disk.")
    say(f"Files verified: {', '.join(sorted(files_seen))}")
    flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
