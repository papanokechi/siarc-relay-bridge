"""Narrow claim S3A-06 per operator ruling 9 (2026-09-19).

S3A-06 as written reports a text search of ONE artefact -- the v1.3.1 LaTeX
source -- and states the conclusion without naming which artefact the absence
is an absence from.  The deposited descriptions, fetched this session, contain
"Proposition 3.3.A" repeatedly.  v1.6 defect (4) establishes that the deposited
prose and the LaTeX label set disagree BY CONSTRUCTION, because the
cross-referencing package derived a reference's name from a shared counter.

So the accurate form is: "Proposition 3.3.A" occurs in the deposited prose but
not in the v1.3.1 label set.  That is a NARROWING, not a retraction: the
original inspection result is unchanged and is retained verbatim.

This follows the amendment mechanism already used by CT-R1-AUDIT/R2 on this
same claim: the superseded text is preserved in a claim_before_* field, the
amending session is named in amended_in, and an audit_* field states why.

Nothing is deleted.  The file is rewritten only if exactly one line changes.
"""

import hashlib
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
SESSIONS = SESSION.parent

TARGET = SESSIONS / "CT-S3A-ZETA-AUDIT" / "claims.jsonl"
CLAIM_ID = "S3A-06"
OUT = SESSION / "outputs" / "amend_s3a06.out.txt"

# The four deposited descriptions held in refs/, with the version each carries.
DEPOSITED = [
    ("datacite_19972394.description.txt", "v1.3", "10.5281/zenodo.19972394"),
    ("datacite_20585624.description.txt", "v1.4", "10.5281/zenodo.20585624"),
    ("zenodo_22717792.description.txt", "v1.5", "10.5281/zenodo.22717792"),
    ("zenodo_22782807.description.txt", "v1.6", "10.5281/zenodo.22782807"),
]

NEEDLE = "Proposition 3.3.A"

NEW_CLAIM = (
    "SCOPE OF THE ABSENCE, NARROWED (operator ruling 9, CT-S26-CTV17-DRAFT): the "
    "string 'Proposition 3.3.A' is ABSENT FROM THE v1.3.1 LaTeX LABEL/SOURCE SET and "
    "PRESENT IN THE DEPOSITED PROSE. Absent: zero matches by text search in "
    "sessions/2026-05-08/T1-OPERATOR-CT-V131-.../channel_theory_outline_v131_with_r1a_caveat.tex "
    "(the newest in-repo Channel Theory source, v1.3.1, at commit "
    "08aa0e2381b3dc37ee54a3200b7272755ca11d59); the object there carrying "
    "xi_0 = 2/sqrt(beta_2) is Conjecture 3.3.A-star, 'Cross-degree universality of xi_0', "
    "label prop:xi0 at L502, proven at d=2. Present: the deposited descriptions of v1.3, "
    "v1.4, v1.5 and v1.6 all name 'Proposition 3.3.A' explicitly as the source of "
    "xi_0 = 2/sqrt(beta_2) and rho = -3/2 - beta_1/beta_2. The two artefacts disagree BY "
    "CONSTRUCTION, per v1.6 erratum (4): the theorem-like environments share one counter "
    "and the cross-referencing package derived reference names from the counter, so every "
    "cross-reference in v1.0-v1.5 rendered as 'Theorem N' regardless of the environment's "
    "class, while the numbered blocks themselves were always correct. P1's citation "
    "'Proposition 3.3.A' is therefore CORRECT AGAINST THE DEPOSITED PROSE and does not "
    "match the v1.3.1 label set. This narrows, and does not retract, the original finding: "
    "the inspection result is unchanged, only its scope is now stated."
)

AUDIT_NOTE = (
    "Narrowed under operator ruling 9 (2026-09-19). The original claim stated an absence "
    "without naming the artefact the absence is an absence from, and so read as a claim "
    "about Channel Theory rather than about one file. Channel Theory v1.3-v1.6 deposited "
    "descriptions were fetched in CT-S26-CTV17-DRAFT and contain the string; v1.6 erratum "
    "(4) explains why prose and label set must be expected to differ. Label unchanged at "
    "INSPECTED: this is still a file-inspection result, now over two artefact sets instead "
    "of one. Not a retraction."
)


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load(path: Path):
    """Read claims.jsonl as (raw_line, parsed) pairs, preserving order."""
    raw = path.read_text(encoding="utf-8")
    if "\r" in raw:
        raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    rows = []
    for line in raw.split("\n"):
        if not line.strip():
            continue
        rows.append((line, json.loads(line)))
    return rows


def main() -> int:
    log = []

    def say(s=""):
        print(s)
        log.append(s)

    say("=" * 78)
    say("AMEND S3A-06 -- narrowing to the artefact actually inspected")
    say("=" * 78)
    say()

    if not TARGET.exists():
        say(f"FATAL: {TARGET} does not exist")
        return 2

    # ---------------------------------------------------------------- SECTION 1
    # Establish the PRESENCE side from the held deposited text before touching
    # the claim.  An amendment asserting presence must verify presence.
    say("SECTION 1 -- presence in the deposited descriptions (refs/, held bytes)")
    say("-" * 78)
    presence = []
    for fname, ver, doi in DEPOSITED:
        p = SESSION / "refs" / fname
        if not p.exists():
            say(f"FATAL: required source missing: {p}")
            return 2
        text = p.read_text(encoding="utf-8")
        n = text.count(NEEDLE)
        presence.append((ver, fname, n))
        say(f"  {ver:5s}  {doi:30s}  {NEEDLE!r} x {n:2d}   sha256 {sha256_file(p)[:16]}  {fname}")
    if any(n == 0 for _, _, n in presence):
        say()
        say("FATAL: the presence side does not hold in every deposited description.")
        say("The narrowing as ruled asserts presence in the deposited prose; if any")
        say("held description lacks the string, that assertion is wrong and this")
        say("script must not write it.")
        return 2
    say()
    say(f"  presence holds in all {len(presence)} held descriptions.")
    say()

    # Reader control: a defective read that returned the whole file as empty or
    # mis-decoded would report zero and be indistinguishable from real absence.
    # Assert a known-present sentinel unrelated to the needle.
    say("SECTION 2 -- reader integrity (a count of 0 must not be a broken read)")
    say("-" * 78)
    for fname, ver, _doi in DEPOSITED:
        text = (SESSION / "refs" / fname).read_text(encoding="utf-8")
        for sentinel in ("Newton-polygon", "Borel"):
            if sentinel not in text:
                say(f"FATAL: sentinel {sentinel!r} absent from {fname}: read is suspect")
                return 2
        say(f"  {ver:5s}  sentinels present, {len(text):6d} chars decoded  ok")
    say()

    # ---------------------------------------------------------------- SECTION 3
    say("SECTION 3 -- amend the claim in place, preserving the superseded text")
    say("-" * 78)
    before_hash = sha256_file(TARGET)
    say(f"  target        : {TARGET.relative_to(SESSIONS.parent)}")
    say(f"  sha256 before : {before_hash}")

    rows = load(TARGET)
    say(f"  claims in file: {len(rows)}")

    hits = [i for i, (_, c) in enumerate(rows) if c.get("claim_id") == CLAIM_ID]
    if len(hits) != 1:
        say(f"FATAL: expected exactly 1 row with claim_id {CLAIM_ID}, found {len(hits)}")
        return 2
    idx = hits[0]
    _, claim = rows[idx]

    if "claim_before_s26c" in claim:
        say(f"  {CLAIM_ID} already carries claim_before_s26c -- already amended.")
        say("  Refusing to amend twice; an amendment must not stack on itself.")
        return 1

    old_claim = claim["claim"]
    old_label = claim.get("label")
    say(f"  label before  : {old_label}")
    say(f"  claim before  : {len(old_claim)} chars")

    claim["claim_before_s26c"] = old_claim
    claim["claim"] = NEW_CLAIM
    claim["audit_s26c"] = AUDIT_NOTE
    claim["amended_in"] = f"{claim.get('amended_in', '')}; CT-S26-CTV17-DRAFT".lstrip("; ")
    claim["narrowed_not_retracted"] = True

    if claim.get("label") != old_label:
        say("FATAL: label moved; a narrowing must not change the label")
        return 2

    backup = SESSION / "outputs" / "CT-S3A-ZETA-AUDIT.claims.jsonl.pre-s26c-amend"
    if not backup.exists():
        shutil.copy2(TARGET, backup)
        say(f"  backup written: {backup.name}  (sha256 {sha256_file(backup)[:16]})")
    else:
        say(f"  backup exists : {backup.name} -- not overwritten")

    out_lines = []
    for i, (raw, parsed) in enumerate(rows):
        out_lines.append(json.dumps(parsed, ensure_ascii=False) if i == idx else raw)
    TARGET.write_text("\n".join(out_lines) + "\n", encoding="utf-8")

    after_hash = sha256_file(TARGET)
    say(f"  sha256 after  : {after_hash}")
    say()

    # ---------------------------------------------------------------- SECTION 4
    say("SECTION 4 -- read back from disk and re-assert")
    say("-" * 78)
    rows2 = load(TARGET)
    if len(rows2) != len(rows):
        say(f"FATAL: claim count changed {len(rows)} -> {len(rows2)}")
        return 2
    got = [c for _, c in rows2 if c.get("claim_id") == CLAIM_ID]
    if len(got) != 1:
        say("FATAL: read-back did not find exactly one amended claim")
        return 2
    g = got[0]
    checks = [
        ("claim text replaced", g["claim"] == NEW_CLAIM),
        ("superseded text preserved verbatim", g["claim_before_s26c"] == old_claim),
        ("label unchanged", g.get("label") == old_label),
        ("amending session named", "CT-S26-CTV17-DRAFT" in g.get("amended_in", "")),
        ("earlier amendment trail kept", "CT-R1-AUDIT/R2" in g.get("amended_in", "")),
        ("narrowing flagged", g.get("narrowed_not_retracted") is True),
        ("audit note present", len(g.get("audit_s26c", "")) > 100),
        ("no other claim_id lost", {c['claim_id'] for _, c in rows} == {c['claim_id'] for _, c in rows2}),
        ("file hash moved", before_hash != after_hash),
    ]
    bad = 0
    for name, ok in checks:
        say(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        bad += 0 if ok else 1
    say()
    say(f"  {len(checks)} checks, {bad} failed")
    say()
    say("VERDICT: " + ("OK" if bad == 0 else "FAILED"))
    say("=" * 78)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(log) + "\n", encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256 of output, from disk] {sha256_file(OUT)}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
