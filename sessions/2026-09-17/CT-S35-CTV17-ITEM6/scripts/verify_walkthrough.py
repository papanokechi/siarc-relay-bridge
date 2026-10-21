"""verify_walkthrough.py -- gate the DEPOSIT INSTRUCTIONS, not the description.

CT-S35-CTV17-ITEM6.

Why this file exists
--------------------
Both existing gates verify DESCRIPTION-v1.7-rev3.html.  Neither can see
WALKTHROUGH.md, so every statement in the walkthrough was unchecked, and five
of them were false while both gates were green (claim S35-19):

  * a check count that had not been updated when checks were added;
  * a character count belonging to a superseded revision;
  * an instruction to compare a hash against a constant printed in the file,
    left behind when S2a superseded that procedure;
  * a settled question still described as open, with the opposite answer;
  * a command that truncates the very counts the surrounding prose tells the
    reader to check.

The first four are readable defects.  The fifth is not: it can only be found
by RUNNING the block.  So this gate executes the walkthrough's own commands
and asserts that what they print contains what the walkthrough claims it does.

Read-only.  Makes no network call.  Writes nothing outside outputs/.
"""

import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)

WALK = os.environ.get("VW_WALK_OVERRIDE") or os.path.join(SESSION, "WALKTHROUGH.md")
# The override exists so the mutant harness can point this gate at a mutated
# COPY without copying the gate itself.  A harness copied into a temp dir keeps
# HERE/SESSION resolving to that temp dir and dies before judging anything;
# overriding the one input under test leaves every other path correct.
DESC = os.path.join(SESSION, "DESCRIPTION-v1.7-rev3.html")
FORM = os.path.join(SESSION, "DEPOSIT-FORM.md")

# Amendment C: a check that reads a file must assert a known-present feature,
# including a non-ASCII one where the file has one, BEFORE evaluating any
# absence.  An ASCII-only sentinel cannot detect a latin-1 read, because ASCII
# survives it.
WALK_SENTINEL_TEXT = "New version"
WALK_SENTINEL_NONASCII = "\u2192"          # the arrow in "1.6 -> 1.7"
DESC_SENTINEL_NONASCII = "\u2080"          # subscript zero, 42 raw occurrences
# NOT xi (U+03BE): the description escapes it as &xi; 35 times, so the raw
# codepoint is genuinely absent.  Picking it as a sentinel made this gate
# refuse a sound file on its first run -- a reader defect, not a file defect,
# and confirmed as such by a second, differently-implemented read of the raw
# bytes before anything was changed.


def read_text(path, sentinel, nonascii):
    """Read a file and prove the read worked before anything is judged absent."""
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8").replace("\r\n", "\n")
    if sentinel not in text:
        raise AssertionError(
            "READER INTEGRITY: sentinel %r absent from %s -- the read is "
            "suspect; no absence may be evaluated" % (sentinel, path))
    if nonascii and nonascii not in text:
        raise AssertionError(
            "READER INTEGRITY: non-ASCII sentinel %r absent from %s -- a "
            "latin-1 or truncated read would pass an ASCII-only sentinel"
            % (nonascii, path))
    return text


def code_lines(text):
    """Every line inside a fenced block, with blockquote markers stripped."""
    out, inside = [], False
    for line in text.split("\n"):
        bare = re.sub(r"^\s*>\s?", "", line)
        if bare.strip().startswith("```"):
            inside = not inside
            continue
        if inside:
            out.append(bare)
    return out


def run_gate(script):
    """Run a gate and return its stdout, so counts come from the gate itself."""
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    proc = subprocess.run(
        [sys.executable, os.path.join(HERE, script)],
        capture_output=True, text=True, encoding="utf-8", env=env, cwd=SESSION)
    return proc.stdout or ""


def checks_run(stdout):
    m = re.search(r"^checks run\s*:\s*(\d+)", stdout, re.M)
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------------------
# the checks
# ---------------------------------------------------------------------------

def build_checks(W, D, F, gate_out):
    """Each check returns (ok, detail).  Truth comes from the artefacts."""

    desc_bytes = os.path.getsize(DESC)
    desc_chars = len(D)
    real = {name: checks_run(out) for name, out in gate_out.items()}

    def w1():
        """Every check count the walkthrough states matches the gate's own."""
        bad = []
        for name, n in real.items():
            if n is None:
                bad.append("%s printed no 'checks run' line" % name)
                continue
            stem = name.replace(".py", "")
            for m in re.finditer(
                    re.escape(stem) + r"[^\n]{0,80}?\*{0,2}(\d+)\s*/\s*(\d+)\*{0,2}",
                    W):
                if int(m.group(1)) != n:
                    bad.append("%s quoted as %s/%s, actually runs %d"
                               % (name, m.group(1), m.group(2), n))
        for m in re.finditer(r"\*{0,2}(\d+) checks, 0 failed", W):
            if int(m.group(1)) not in [v for v in real.values() if v]:
                bad.append("'%s checks, 0 failed' matches no gate (%s)"
                           % (m.group(1), real))
        return (not bad, "; ".join(bad) or
                "every quoted check count equals the gate's own output %s" % real)

    def w2():
        """Every character/byte count quoted for the description is current."""
        bad = []
        for m in re.finditer(r"([\d][\d ,]{3,})\s*(?:chars|characters)", W):
            n = int(re.sub(r"[ ,]", "", m.group(1)))
            if n != desc_chars:
                bad.append("char count %d quoted, file has %d" % (n, desc_chars))
        for m in re.finditer(r"([\d][\d ,]{3,})\s*(?:bytes|B)\b", W):
            n = int(re.sub(r"[ ,]", "", m.group(1)))
            if n not in (desc_bytes, CARRIED_BYTES):
                bad.append("byte count %d quoted, matches neither the "
                           "description (%d) nor the carried file (%d)"
                           % (n, desc_bytes, CARRIED_BYTES))
        return (not bad, "; ".join(bad) or
                "all quoted sizes match: description %d chars / %d bytes, "
                "carried file %d bytes" % (desc_chars, desc_bytes, CARRIED_BYTES))

    def w3():
        """No instruction to compare a hash against a constant by eye."""
        bad = [ln.strip() for ln in W.split("\n")
               if re.search(r"^\s*(?:>\s*)?Expected\s*:\s*`?[0-9a-f]{64}", ln)]
        return (not bad, "; ".join(bad) or
                "no 'Expected: <64 hex>' eye-comparison instruction remains "
                "(S35-18 standing form (i))")

    def w4():
        """Every cd in a runnable block points at THIS session."""
        bad = []
        for ln in code_lines(W):
            m = re.match(r"\s*cd\s+(.+?)\s*$", ln)
            if m:
                target = m.group(1).strip().strip('"').rstrip("\\")
                if os.path.normcase(target) != os.path.normcase(SESSION):
                    bad.append("cd %s" % target)
        return (not bad, "; ".join(bad) or
                "every cd in a runnable block targets this session")

    def w5():
        """Every file a runnable block READS exists here.

        Redirect targets are excluded: `*> outputs\\x.txt` names a file the
        command creates.  Requiring it to pre-exist confused 'the instructions
        point at a missing input' with 'this step has not been run yet', and
        failed on outputs\\postpublish_readback.out.txt, which by definition
        cannot exist before publishing.
        """
        bad, seen = [], set()
        lines = code_lines(W)
        written = set()
        for ln in lines:
            for t in re.findall(r"\*?>\s*([\w.\\-]+)", ln):
                written.add(os.path.normcase(t.lstrip(".\\")))
        for ln in lines:
            for m in re.finditer(r"(?:\.\\|scripts\\|outputs\\)[\w.\\-]+", ln):
                rel = m.group(0).lstrip(".\\")
                if rel in seen or "<" in rel:
                    continue
                if os.path.normcase(rel) in written:
                    continue                      # created by the block itself
                seen.add(rel)
                if not os.path.exists(os.path.join(SESSION, rel)):
                    bad.append(rel)
        return (not bad, "; ".join("missing: " + b for b in bad) or
                "all %d input file(s) named in runnable blocks exist; "
                "redirect targets excluded" % len(seen))

    def w6():
        """The walkthrough's claim about the excluded table is true."""
        claimed = "zero" in W and "refs/" in W
        hits = (len(re.findall(r"refs/", D)) + len(re.findall(r"outputs/", D))
                + len(re.findall(r"CT-S\d+", D)))
        if not claimed:
            return (False, "section 6 no longer states the exclusion claim")
        return (hits == 0,
                "description contains %d internal-path occurrence(s); the "
                "walkthrough claims zero" % hits)

    def w7():
        """The carried file's size and md5 agree with DEPOSIT-FORM."""
        bad = []
        if str(CARRIED_BYTES) not in W.replace(",", "").replace("\u00a0", " ") \
                and "609 300" not in W:
            bad.append("carried-file byte count %d not stated" % CARRIED_BYTES)
        if CARRIED_MD5[:8] not in W:
            bad.append("carried-file md5 %s... not stated" % CARRIED_MD5[:8])
        if CARRIED_KEY not in W:
            bad.append("carried-file key %s not stated" % CARRIED_KEY)
        return (not bad, "; ".join(bad) or
                "carried file stated as %s, %d bytes, md5 %s..."
                % (CARRIED_KEY, CARRIED_BYTES, CARRIED_MD5[:8]))

    def w8():
        """EXECUTABLE: the display commands surface the counts they promise.

        This is the one check that cannot be satisfied by reading.  It takes
        each 'Select-Object -Last N' as the walkthrough writes it, applies it
        to the gate's real output, and asserts the counts survive the cut.
        """
        bad = []
        for ln in code_lines(W):
            m = re.search(r"(\w[\w.]*\.py)\s*\|\s*Select-Object\s+-Last\s+(\d+)",
                          ln)
            if not m:
                continue
            script, n = m.group(1), int(m.group(2))
            out = gate_out.get(script)
            if out is None:
                bad.append("%s named in a display command but not run" % script)
                continue
            tail = "\n".join(out.rstrip("\n").split("\n")[-n:])
            missing = [w for w in ("checks run", "checks failed")
                       if w not in tail]
            if missing:
                bad.append("%s | -Last %d hides %s"
                           % (script, n, " and ".join(missing)))
        return (not bad, "; ".join(bad) or
                "every 'Select-Object -Last N' still shows 'checks run' and "
                "'checks failed' when applied to the real gate output")

    return [
        ("W1 quoted check counts equal the gates' own output", w1),
        ("W2 quoted sizes are the current revision's", w2),
        ("W3 no eye-compared hash constant remains", w3),
        ("W4 every cd targets this session, not the packet's origin", w4),
        ("W5 every file a runnable block READS exists", w5),
        ("W6 the stated exclusion of internal paths is true of the description", w6),
        ("W7 the carried file agrees with DEPOSIT-FORM", w7),
        ("W8 EXECUTED: display commands do not hide the counts they promise", w8),
    ]


def form_value(F, key, pattern=r"(.+)"):
    m = re.search(r"^%s:\s*%s\s*$" % (re.escape(key), pattern), F, re.M)
    if not m:
        raise AssertionError("DEPOSIT-FORM.md has no %s line" % key)
    return m.group(1).strip()


def main():
    W = read_text(WALK, WALK_SENTINEL_TEXT, WALK_SENTINEL_NONASCII)
    D = read_text(DESC, "Channel Theory", DESC_SENTINEL_NONASCII)
    F = read_text(FORM, "concept_doi", None)

    global CARRIED_BYTES, CARRIED_MD5, CARRIED_KEY
    CARRIED_BYTES = int(form_value(F, "carried_file_bytes", r"(\d+)"))
    CARRIED_MD5 = form_value(F, "carried_file_md5", r"([0-9a-f]{32})")
    CARRIED_KEY = form_value(F, "carried_file_key")

    print("=" * 76)
    print("verify_walkthrough.py -- gating the deposit INSTRUCTIONS")
    print("  walkthrough : %s (%d chars)" % (os.path.basename(WALK), len(W)))
    print("  reader      : text and non-ASCII sentinels present in both files")
    print("=" * 76)

    print("\nrunning the gates, so every count comes from the gate itself ...")
    gate_out = {}
    for script in ("verify_description.py", "preflight_deposit_rev2.py"):
        gate_out[script] = run_gate(script)
        print("  %-28s checks run: %s" % (script, checks_run(gate_out[script])))
    print()

    failed = broken = 0
    for name, fn in build_checks(W, D, F, gate_out):
        try:
            ok, detail = fn()
        except Exception as exc:                       # a check that cannot run
            broken += 1
            print("  [BROKEN] %s\n           %s: %s"
                  % (name, type(exc).__name__, exc))
            continue
        if not ok:
            failed += 1
        print("  [%s] %s\n           %s" % ("PASS" if ok else "FAIL", name, detail))

    # Reader-integrity controls: prove the reader would have refused a bad read.
    print("\n" + "-" * 76)
    controls, caught = [
        ("truncated read", lambda: read_text_from(W[:200])),
        ("latin-1 read (ASCII survives it)",
         lambda: read_text_from(W.encode("utf-8").decode("latin-1"), ascii_only=True)),
        ("empty read", lambda: read_text_from("")),
    ], 0
    for label, fn in controls:
        try:
            fn()
            print("  [BROKEN CONTROL] %s -- not caught" % label)
        except AssertionError as exc:
            caught += 1
            print("  [PASS] %s -- caught: %s" % (label, str(exc).split(" -- ")[0]))

    print("\n" + "=" * 76)
    print("checks run     : %d" % len(build_checks(W, D, F, gate_out)))
    print("checks failed  : %d" % failed)
    print("broken checks  : %d" % broken)
    print("reader controls: %d of %d caught" % (caught, len(controls)))
    print()
    if failed or broken:
        print("WALKTHROUGH GATE: FAILED")
        print("=" * 76)
        return 1
    print("WALKTHROUGH GATE: PASSED -- the instructions agree with the")
    print("  artefacts they describe, and their display commands were run,")
    print("  not read.  This gate cannot make the deposit correct; it only")
    print("  removes the class where correct bytes meet stale instructions.")
    print("=" * 76)
    return 0


def read_text_from(text, ascii_only=False):
    """The sentinel logic alone, for the controls -- same rule, no file."""
    if ascii_only:
        # a latin-1 decode of utf-8 mangles non-ASCII but leaves ASCII intact
        if WALK_SENTINEL_NONASCII not in text:
            raise AssertionError(
                "READER INTEGRITY: non-ASCII sentinel absent -- a latin-1 read "
                "would pass an ASCII-only sentinel")
        return text
    if WALK_SENTINEL_TEXT not in text:
        raise AssertionError("READER INTEGRITY: sentinel absent -- the read is suspect")
    if WALK_SENTINEL_NONASCII not in text:
        raise AssertionError("READER INTEGRITY: non-ASCII sentinel absent")
    return text


if __name__ == "__main__":
    sys.exit(main())
