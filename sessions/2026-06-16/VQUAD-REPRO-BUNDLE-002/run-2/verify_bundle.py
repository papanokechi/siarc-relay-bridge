#!/usr/bin/env python3
# VQUAD-REPRO-BUNDLE-001 integrity harness (lives in the slot, NOT in the bundle).
# Runs every essential script from its own directory, confirms exit 0, and
# compares the regenerated *_results.json against the reference copy in data/.
# Volatile fields (runtimes/timestamps) are ignored in the structural compare.
import json, os, subprocess, sys, hashlib

BUNDLE = r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-16\VQUAD-REPRO-BUNDLE-002\run-2\vquad-periodrep-bundle"
SCRIPTS = os.path.join(BUNDLE, "scripts")
DATA = os.path.join(BUNDLE, "data")

# (subdir, script, expected_results_json_or_None)
PLAN = [
    ("01-algebraicity", "holonomic_recognition_q3.py", "holonomic_recognition_q3_results.json"),
    ("01-algebraicity", "extract_verify_operators.py", "operator_verification_results.json"),
    ("01-algebraicity", "indicial_analysis.py",        "indicial_results.json"),
    ("01-algebraicity", "borel_pade_census.py",        "borel_pade_results.json"),
    ("02-galois",       "stage2_kovacic.py",           None),
    ("02-galois",       "stage2b_symsquare.py",        "stage2_kovacic_results.json"),
    ("02-galois",       "stage3_galois_LV.py",         "stage3_galois_LV_results.json"),
    ("02-galois",       "stage3b_frobenius_v2.py",     "stage3b_frobenius_results.json"),
    ("03-verification", "numcheck_period_rep.py",      "numcheck_period_rep_results.json"),
    ("03-verification", "stage4a_methodA_v2.py",       "stage4_methodA_results.json"),
    ("03-verification", "stage4_methods.py",           "stage4_methods_results.json"),
    ("03-verification", "stage0_residual_check.py",    "stage0_residual_results.json"),
    ("04-cycle",        "stage1_hankel_period.py",     "stage1_hankel_results.json"),
]

VOLATILE = ("runtime", "elapsed", "seconds", "timestamp", "date", "time_s",
            "wall", "generated", "utc")

def strip_volatile(obj):
    if isinstance(obj, dict):
        return {k: strip_volatile(v) for k, v in obj.items()
                if not any(t in k.lower() for t in VOLATILE)}
    if isinstance(obj, list):
        return [strip_volatile(x) for x in obj]
    return obj

def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]

rows = []
allgood = True
for sub, script, expect in PLAN:
    d = os.path.join(SCRIPTS, sub)
    gen = os.path.join(d, expect) if expect else None
    if gen and os.path.exists(gen):
        os.remove(gen)  # force regeneration
    p = subprocess.run([sys.executable, script], cwd=d,
                       capture_output=True, text=True, encoding="utf-8")
    code = p.returncode
    status = "ok" if code == 0 else f"EXIT{code}"
    cmp = "-"
    if code != 0:
        allgood = False
    elif expect:
        ref = os.path.join(DATA, expect)
        if not os.path.exists(gen):
            cmp = "NO-OUTPUT"; allgood = False
        elif not os.path.exists(ref):
            cmp = "NO-REF"; allgood = False
        elif sha(gen) == sha(ref):
            cmp = "exact"
        else:
            try:
                g = strip_volatile(json.load(open(gen, encoding="utf-8")))
                r = strip_volatile(json.load(open(ref, encoding="utf-8")))
                cmp = "match(modulo-volatile)" if g == r else "DIFF"
                if g != r:
                    allgood = False
            except Exception as e:
                cmp = f"ERR:{e}"; allgood = False
    rows.append((sub, script, status, expect or "(stdout)", cmp))

w1 = max(len(r[1]) for r in rows)
print(f"{'script'.ljust(w1)}  {'exit':5} {'compare-to-data/':22} output")
print("-" * (w1 + 50))
for sub, script, status, expect, cmp in rows:
    print(f"{script.ljust(w1)}  {status:5} {cmp:22} {expect}")
print("\nALL ESSENTIAL SCRIPTS PASS:", allgood)
