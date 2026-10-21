"""CT-S47 - control arms for route_s5_qp.py.

Each arm mutates the SCRIPT and asserts the expected exit code:
    diff  (1) a figure must be reported as DIFFERing
    halt  (2) the script must refuse rather than compare
    clean (0) a semantically neutral edit must change nothing

Two rules carried from earlier sessions and both load-bearing here:

  * The arms run in a scratch directory (tempfile.TemporaryDirectory).  In
    CT-S46 the arms ran in the real session root and overwrote the very output
    file the claims cite; every gate exited 0 while the file on disk was the
    last arm's.  A control must not be able to write the artefact it controls.

  * A SyntaxError or NameError traceback echoes the mutated source line, so a
    'the reason appears in the output' test can score a script that never ran.
    `broke` guards that, and a crash is exit 3, distinct from both 1 and 2.
"""
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
SCRIPT = HERE / "route_s5_qp.py"
OUT = SESS / "outputs" / "mutants_route_s5_qp.out.txt"

SRC = SCRIPT.read_text(encoding="utf-8")

ARMS = [
    # (name, needle, replacement, expected kind, tex_sub)
    ("M1 coords blind to sqrt33 (the defect actually hit this session)",
     '        "sqrt33": e.coeff(_A3, 1).coeff(_B11, 1),',
     '        "sqrt33": sp.Integer(0),',
     "halt", None),
    ("M2 generators always vanish (route ALPHA cannot fail)",
     "        v = sp.expand(sp.radsimp(g.subs(sub)))",
     "        v = sp.Integer(0)",
     "halt", None),
    ("M3 source digest wrong (the file this was written against moved)",
     'SRC_SHA = "AF25048B9B62',
     'SRC_SHA = "AF25048B9B63',
     "halt", None),
    ("M4 parser silently drops a digit of q_A",
     'P["q_A"], P["q_A_sign"] = int(qA), sgn[qsA]',
     'P["q_A"], P["q_A_sign"] = int(str(qA)[:-1]), sgn[qsA]',
     "halt", None),
    ("M5 System C's s_+ corrupted (transport broken -> refuse, not report)",
     "s_p = sp.Rational(-1, 6) + r11 * sp.I / 6",
     "s_p = sp.Rational(-1, 5) + r11 * sp.I / 6",
     "halt", None),
    ("M6 approximation tolerance collapsed to zero",
     "    return sp.Float(5) * sp.Float(10) ** (-d - 1)",
     "    return sp.Float(0)",
     "diff", None),
    ("M7 branch pairing compared against its own branch (F4 vacuous)",
     "vals_cross = gen_values(p_parsed, q_parsed, t_of(2), theta_of(2))",
     "vals_cross = gen_values(p_parsed, q_parsed, t_of(1), theta_of(1))",
     "diff", None),
    ("M8 negative arm: a comment is not a defect",
     '"""CT-S47 - route S for section 5',
     '"""neutral edit for the negative control arm.\n\nCT-S47 - route S for section 5',
     "clean", None),
    # M9 is the arm the pass exists for: the PAGE carries a transposed digit.
    # It mutates section5.tex itself, so the source digest must be updated too
    # or the script would (correctly) refuse before ever comparing.
    ("M9 the PAGE carries a transposed digit (457937 -> 457973)",
     None, None, "diff", ("457937", "457973")),
]

EXPECT = {"diff": 1, "halt": 2, "clean": 0}


def run(src_text, tex_sub=None):
    """Run a version of the script in a throwaway tree.

    The scratch tree gets its own refs/ and outputs/, so neither the real
    section5.tex nor the real route_s5_qp.out.txt can be touched by any arm.
    """
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "scripts").mkdir()
        (root / "outputs").mkdir()
        (root / "refs").mkdir()
        tex = (SESS / "refs" / "section5.tex").read_bytes()
        if tex_sub is not None:
            old, new = tex_sub
            if tex.count(old.encode()) != 1:
                return None, f"tex needle {old!r} not unique"
            tex = tex.replace(old.encode(), new.encode())
            # the script resolves its source by hash; update it, or the arm
            # would only ever prove that the digest guard works (M3 does that)
            newsha = hashlib.sha256(tex).hexdigest().upper()
            src_text = re.sub(r'SRC_SHA = "[0-9A-Fa-f]{64}"',
                              f'SRC_SHA = "{newsha}"', src_text)
        (root / "refs" / "section5.tex").write_bytes(tex)
        tgt = root / "scripts" / "route_s5_qp.py"
        tgt.write_text(src_text, encoding="utf-8")
        pr = subprocess.run([sys.executable, str(tgt)], capture_output=True,
                            text=True, encoding="utf-8", errors="replace")
        return pr.returncode, (pr.stdout or "") + (pr.stderr or "")


lines = []


def say(s=""):
    lines.append(s)
    print(s)


say("=" * 74)
say("CONTROL ARMS for route_s5_qp.py   (each runs in a scratch tree)")
say("=" * 74)

# ---- baseline: the unmutated script must be clean --------------------------
rc, out = run(SRC)
say(f"baseline: exit {rc} (expected 0)")
if rc != 0:
    say("")
    say("REFUSED: baseline is not clean; no arm result would mean anything.")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    sys.exit(2)
if "36 checks, 0 DIFFER" not in out:
    say("")
    say("REFUSED: baseline did not report the expected 36 checks / 0 DIFFER.")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    sys.exit(2)
say("baseline: 36 checks, 0 DIFFER  -- arms are interpretable")
say("")

caught = missed = skipped = 0
for name, needle, repl, kind, tex_sub in ARMS:
    if needle is not None:
        if SRC.count(needle) == 0:
            say(f"[SKIPPED] {name}")
            say("          mutation site ABSENT -- this arm tested nothing")
            skipped += 1
            continue
        if SRC.count(needle) > 1:
            say(f"[SKIPPED] {name}")
            say(f"          needle not unique ({SRC.count(needle)} sites)")
            skipped += 1
            continue
        mutated = SRC.replace(needle, repl)
    else:
        mutated = SRC
    rc, out = run(mutated, tex_sub)
    if rc is None:
        say(f"[SKIPPED] {name}")
        say(f"          {out}")
        skipped += 1
        continue
    broke = ("SyntaxError" in out or "NameError" in out
             or "IndentationError" in out or rc == 3)
    want = EXPECT[kind]
    if broke:
        say(f"[MISSED ] {name}")
        say(f"          the mutant CRASHED (exit {rc}); a crash is not a detection")
        missed += 1
    elif rc == want:
        say(f"[CAUGHT ] {name}")
        say(f"          expected {kind} -> exit {want}, got {rc}")
        caught += 1
    else:
        say(f"[MISSED ] {name}")
        say(f"          expected {kind} -> exit {want}, got {rc}")
        missed += 1

say("")
say("=" * 74)
say(f"ARMS: {caught} CAUGHT, {missed} MISSED, {skipped} SKIPPED "
    f"(of {len(ARMS)})")
say("=" * 74)

# ---- the real artefact must be untouched -----------------------------------
real = SESS / "outputs" / "route_s5_qp.out.txt"
say(f"real output still reports: "
    f"{[l for l in real.read_text(encoding='utf-8').splitlines() if 'ROUTE S' in l]}")

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
sys.exit(1 if (missed or skipped) else 0)
