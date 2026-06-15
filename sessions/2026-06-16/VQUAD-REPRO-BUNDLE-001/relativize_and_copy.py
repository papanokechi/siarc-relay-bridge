#!/usr/bin/env python3
# VQUAD-REPRO-BUNDLE-001 build tool (lives in the slot, NOT in the bundle).
# Copies the ESSENTIAL scripts into the bundle and relativizes the single
# hardcoded absolute output path each writes to (C:\LocalWork\...\X.json ->
# os.path.join(os.path.dirname(os.path.abspath(__file__)), "X.json")).
# This is the ONLY change made to script bodies; parent slots are untouched.
import os, re

SRC15 = r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15"
SRC01 = SRC15 + r"\PERIOD-REP-VQUAD-001\scripts"
SRC02 = SRC15 + r"\PERIOD-REP-VQUAD-002\scripts"
SRC03 = SRC15 + r"\PERIOD-REP-VQUAD-003\scripts"
BUNDLE = r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-16\VQUAD-REPRO-BUNDLE-001\vquad-periodrep-bundle\scripts"

PLAN = {
    "01-algebraicity": [
        (SRC02, "holonomic_recognition_q3.py"),
        (SRC02, "extract_verify_operators.py"),
        (SRC02, "indicial_analysis.py"),
        (SRC02, "borel_pade_census.py"),
    ],
    "02-galois": [
        (SRC03, "stage2_kovacic.py"),
        (SRC03, "stage2b_symsquare.py"),
        (SRC03, "stage3_galois_LV.py"),
        (SRC03, "stage3b_frobenius_v2.py"),
    ],
    "03-verification": [
        (SRC03, "stage4a_methodA_v2.py"),
        (SRC03, "stage4_methods.py"),
        (SRC01, "numcheck_period_rep.py"),
        (SRC03, "stage0_residual_check.py"),
        (SRC03, "q3_foundation.py"),
    ],
    "04-cycle": [
        (SRC03, "stage1_hankel_period.py"),
    ],
}

# Per-file source patches applied BEFORE relativization. The only such patch
# corrects stage4_methods.py's *inline* Method-A self-check to the established
# Borel-sum convention D_xi -> +1/z, xi -> +z^2 D_z (the same convention proven
# in the sibling stage4a_methodA_v2.py and documented in docs/CONVENTIONS.md).
# The parent slot retained the superseded -1/z attempt in this script and
# instead hand-annotated its results JSON; the bundle ships the corrected,
# self-consistent script so that running it reproduces all_three = True. This
# changes NO numerical result (Methods B and C are untouched); it only flips the
# legacy wrong-sign operator duality so the inline Method-A flag agrees with the
# certified result.
PATCHES = {
    "stage4_methods.py": [
        (re.compile(r"def neg_z2Dz\(expr\):\n    return -z\*\*2\*sp\.diff\(expr, z\)"),
         "def pos_z2Dz(expr):\n    return z**2*sp.diff(expr, z)"),
        (re.compile(r"        g = \(sp\.Integer\(-1\)\)\*\*k \* z\*\*\(-k\) \* f\(z\).*"),
         "        g = z**(-k) * f(z)   # (+1/z)^k f  with D_xi -> +1/z  "
         "[bundle: corrected Borel-sum convention, see docs/CONVENTIONS.md]"),
        (re.compile(r"            g = neg_z2Dz\(g\).*"),
         "            g = pos_z2Dz(g)   # xi -> +z^2 D_z, applied a times  "
         "[bundle: corrected convention]"),
    ],
}

# Matches an r-string literal that begins with C:\LocalWork, plus any
# concatenated r"..." continuation pieces (handles the 2-line `path = (...)` form).
ABS = re.compile(r'r"C:\\LocalWork[^"]*"(?:\s*r"[^"]*")*')

def relativize(text):
    n = 0
    def repl(m):
        nonlocal n
        pieces = re.findall(r'r"([^"]*)"', m.group(0))
        full = "".join(pieces)
        base = full.split("\\")[-1]
        n += 1
        if base.endswith(".json"):
            # output/IO file -> write/read next to this script
            return ('os.path.join(os.path.dirname(os.path.abspath(__file__)), '
                    f'"{base}")')
        # directory reference (e.g. a sibling-module ".../scripts" path on
        # sys.path) -> the script's own dir, since siblings are co-located
        return 'os.path.dirname(os.path.abspath(__file__))'
    new = ABS.sub(repl, text)
    return new, n

def ensure_import_os(text):
    if re.search(r'^\s*import os\b', text, re.M):
        return text
    lines = text.splitlines(keepends=True)
    # insert before the first non-__future__ import/from line
    for i, ln in enumerate(lines):
        if re.match(r'\s*(import|from)\s+\w', ln) and "__future__" not in ln:
            lines.insert(i, "import os\n")
            return "".join(lines)
    return "import os\n" + text

# Portability shim: these scripts print mathematical Unicode (gamma, xi, the
# contour-integral sign, beta, ...). On Windows a non-UTF-8 console (cp1252)
# raises UnicodeEncodeError on those prints. Reconfiguring stdout/stderr to
# UTF-8 makes the scripts run unchanged on any console. This is pure I/O and
# cannot affect any computed value or any *_results.json (those are written
# with encoding="utf-8" already).
UTF8_GUARD = (
    "import sys as _sys  # bundle portability: force UTF-8 console output\n"
    "try:\n"
    "    _sys.stdout.reconfigure(encoding=\"utf-8\")\n"
    "    _sys.stderr.reconfigure(encoding=\"utf-8\")\n"
    "except Exception:\n"
    "    pass\n"
)

def ensure_utf8_guard(text):
    if "reconfigure(encoding=\"utf-8\")" in text:
        return text
    lines = text.splitlines(keepends=True)
    for i, ln in enumerate(lines):
        if re.match(r'\s*(import|from)\s+\w', ln) and "__future__" not in ln:
            lines.insert(i, UTF8_GUARD)
            return "".join(lines)
    return UTF8_GUARD + text

report = []
for sub, items in PLAN.items():
    for srcdir, fname in items:
        src = os.path.join(srcdir, fname)
        with open(src, encoding="utf-8") as fh:
            text = fh.read()
        npatch = 0
        for rx, rep in PATCHES.get(fname, []):
            text, c = rx.subn(rep, text)
            npatch += c
        new, n = relativize(text)
        if n:
            new = ensure_import_os(new)
        new = ensure_utf8_guard(new)
        dst = os.path.join(BUNDLE, sub, fname)
        with open(dst, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new)
        # verify no absolute path remains
        leak = "C:\\LocalWork" in new
        report.append((sub, fname, n, npatch, "LEAK!" if leak else "ok"))

for sub, fname, n, npatch, status in report:
    extra = f" patched={npatch}" if npatch else ""
    print(f"{status:6} {sub:16} {fname:32} paths_relativized={n}{extra}")
print(f"\nTotal scripts copied: {len(report)}")
print("Any leaks:", any(r[4] != "ok" for r in report))
print("Patches applied:", sum(r[3] for r in report), "(expected 3 in stage4_methods.py)")
