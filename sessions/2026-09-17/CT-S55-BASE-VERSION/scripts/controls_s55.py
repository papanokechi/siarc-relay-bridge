#!/usr/bin/env python3
"""CT-S55 -- control harness for emit_claims_s55.py.

Every arm runs in a fresh scratch directory. An arm run in the real session
directory would overwrite the very claims.jsonl the claims cite.

A0 is a positive baseline that must WRITE. A harness in which every arm refuses
is indistinguishable from one in which every arm works.

An arm that provokes a SyntaxError or NameError does not count as CAUGHT: a
traceback echoes the offending source line, so the reason string can appear in
the output of a script that never ran a single check.
"""
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
OUT = SESSION / "outputs" / "controls.out.txt"
REAL_CLAIMS = SESSION / "claims.jsonl"

BV = "outputs/base_version.out.txt"
HS = "outputs/submitted_file_hash.out.txt"
SW = "outputs/sweep_h.out.txt"
EMIT = "scripts/emit_claims_s55.py"

LINES: list[str] = []


def say(s: str = "") -> None:
    print(s)
    LINES.append(s)


def sub(rel: str, old: str, new: str):
    def f(root: Path) -> None:
        p = root / rel
        t = p.read_text(encoding="utf-8")
        if t.count(old) != 1:
            raise AssertionError(f"arm setup: {rel}: {old!r} occurs {t.count(old)} times, need 1")
        p.write_text(t.replace(old, new), encoding="utf-8")
    return f


def dup_line(rel: str, needle: str):
    def f(root: Path) -> None:
        p = root / rel
        ls = p.read_text(encoding="utf-8").split("\n")
        idx = [i for i, l in enumerate(ls) if l.strip().startswith(needle)]
        if len(idx) != 1:
            raise AssertionError(f"arm setup: {rel}: {needle!r} occurs {len(idx)} times, need 1")
        ls.insert(idx[0] + 1, ls[idx[0]])
        p.write_text("\n".join(ls), encoding="utf-8")
    return f


def del_line(rel: str, needle: str):
    def f(root: Path) -> None:
        p = root / rel
        ls = p.read_text(encoding="utf-8").split("\n")
        idx = [i for i, l in enumerate(ls) if l.strip().startswith(needle)]
        if len(idx) != 1:
            raise AssertionError(f"arm setup: {rel}: {needle!r} occurs {len(idx)} times, need 1")
        del ls[idx[0]]
        p.write_text("\n".join(ls), encoding="utf-8")
    return f


# name, mutation (None = pristine), expected rc, reason substring
ARMS = [
    ("A0 pristine (positive baseline: must WRITE)", None, 0, None),
    ("M1 the two routes disagree on the version",
     sub(HS, "S55H submitted version: v1.2", "S55H submitted version: v1.1"),
     2, "the two routes disagree"),
    ("M2 rebase flag flipped to NO",
     sub(BV, "S55 rebase required: YES", "S55 rebase required: NO"),
     2, "but the output does not say YES"),
    ("M3 unstripped match no longer zero",
     sub(BV, "S55 unstripped page match: 0 of 25", "S55 unstripped page match: 25 of 25"),
     2, "0 unstripped matches"),
    ("M4 a falsifier is recorded as fired",
     sub(BV, "S55 falsifiers fired: none", "S55 falsifiers fired: F1"),
     2, "a falsifier fired"),
    ("M5 stamped build recorded as matching a version",
     sub(HS, "S55H stamped matches: 0 of 4", "S55H stamped matches: 1 of 4"),
     2, "matches nothing, but the output disagrees"),
    ("M6 anchor line duplicated",
     dup_line(BV, "S55 LMP holds version:"),
     2, "matched 2 lines, expected exactly 1"),
    ("M7 anchor line deleted",
     del_line(BV, "S55 CT-S52 base pages:"),
     2, "matched 0 lines, expected exactly 1"),
    ("M8 output_hash attributed to the wrong script",
     sub(EMIT, '"output_hash": hs_hash,\n        },\n        {\n            "claim_id": "S55-02"',
         '"output_hash": bv_hash,\n        },\n        {\n            "claim_id": "S55-02"'),
     2, "output_hash does not belong to"),
    ("M9 a claim emptied of its text",
     sub(EMIT, 'c["task_id"] = TASK', 'c["claim"] = "   "\n        c["task_id"] = TASK'),
     2, "empty or too short"),
    ("M10 a label outside the permitted set",
     sub(EMIT, '"label": "VERIFIED",\n            "evidence_type": "computation",',
         '"label": "PROBABLY",\n            "evidence_type": "computation",'),
     2, "unknown label"),
    ("M11 sweep reported as empty",
     sub(SW, "S55S sweep empty: NO", "S55S sweep empty: YES"),
     2, "asserts the sweep is not empty"),
    ("M12 second instance unconfirmed",
     sub(SW, "S55S second instance confirmed: YES", "S55S second instance confirmed: NO"),
     2, "did not confirm one"),
    ("M13 sweep split no longer sums to the census",
     sub(SW, "S55S actionable stale figures: 28", "S55S actionable stale figures: 27"),
     2, "does not sum to the census"),
]


def main() -> int:
    say("=" * 74)
    say("CT-S55 -- CONTROL HARNESS for emit_claims_s55.py")
    say("=" * 74)
    say("")

    before = REAL_CLAIMS.read_bytes() if REAL_CLAIMS.exists() else None
    before_h = hashlib.sha256(before).hexdigest() if before else "(absent)"
    say(f"real claims.jsonl before: sha256 {before_h}")
    if before is None:
        say("ERROR: no real claims.jsonl to compare A0 against")
        return 1
    expect_claims = len([l for l in before.decode("utf-8").split("\n") if l.strip()])
    say(f"A0 must write {expect_claims} claims "
        f"(derived from the real artefact, not transcribed)")
    say("")

    results = []
    for name, mut, want_rc, want_reason in ARMS:
        with tempfile.TemporaryDirectory(prefix="s55ctl-") as td:
            root = Path(td) / "session"
            root.mkdir()
            shutil.copytree(SESSION / "scripts", root / "scripts",
                            ignore=shutil.ignore_patterns("__pycache__"))
            shutil.copytree(SESSION / "outputs", root / "outputs")
            (root / "claims.jsonl").unlink(missing_ok=True)

            setup_err = None
            if mut is not None:
                try:
                    mut(root)
                except AssertionError as e:
                    setup_err = str(e)

            if setup_err:
                say(f"  {name}")
                say(f"     SETUP FAILED: {setup_err}")
                results.append((name, False, "setup"))
                continue

            pr = subprocess.run(
                [sys.executable, "scripts/emit_claims_s55.py"],
                cwd=root, capture_output=True, text=True, encoding="utf-8",
            )
            out = (pr.stdout or "") + (pr.stderr or "")
            wrote = (root / "claims.jsonl").exists()
            n_claims = 0
            if wrote:
                n_claims = len([l for l in (root / "claims.jsonl").read_text(
                    encoding="utf-8").split("\n") if l.strip()])

            broke = ("SyntaxError" in out) or ("NameError" in out) or ("CRASH" in out)
            rc_ok = pr.returncode == want_rc
            if want_reason is None:
                # A0: must write, must write all six, must not have broken
                ok = rc_ok and wrote and n_claims == expect_claims and not broke
                detail = f"rc={pr.returncode} wrote={wrote} claims={n_claims}/{expect_claims}"
            else:
                reason_ok = want_reason in out
                ok = rc_ok and reason_ok and not wrote and not broke
                detail = (f"rc={pr.returncode} refused_for_its_own_reason={reason_ok} "
                          f"wrote={wrote}")
            if broke:
                detail += "  [REJECTED: script failed to parse/run]"

            say(f"  {name}")
            say(f"     expected rc {want_rc}"
                + (f", reason {want_reason!r}" if want_reason else ", and a written file"))
            say(f"     {detail}")
            first = next((l for l in out.split("\n")
                          if l.startswith("REFUSED") or l.startswith("[wrote")), "(no verdict line)")
            say(f"     {first.strip()[:150]}")
            say(f"     -> {'CAUGHT' if ok else 'MISSED'}")
            results.append((name, ok, detail))

    caught = sum(1 for _, ok, _ in results if ok)
    say("")
    say(f"ARMS: {caught}/{len(results)} CAUGHT")

    after = REAL_CLAIMS.read_bytes() if REAL_CLAIMS.exists() else None
    after_h = hashlib.sha256(after).hexdigest() if after else "(absent)"
    say(f"real claims.jsonl after : sha256 {after_h}")
    say(f"real claims.jsonl unchanged: {before == after}")
    if before != after:
        say("  ERROR: the harness modified the artefact its claims cite")
    say("")
    say(f"S55C arms caught: {caught} of {len(results)}")
    say(f"S55C artefact unchanged: {before == after}")
    return 0 if (caught == len(results) and before == after) else 1


if __name__ == "__main__":
    rc = main()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256 ] {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    print(f"[exit   ] {rc}")
    sys.exit(rc)
