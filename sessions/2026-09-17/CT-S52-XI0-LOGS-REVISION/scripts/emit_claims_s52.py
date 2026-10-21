#!/usr/bin/env python3
"""CT-S52 -- emit claims.jsonl.

Two rules this emitter exists to obey:

  * the buffer is validated BEFORE anything is written, so a refusal cannot
    leave a corrupt claims.jsonl on disk;
  * every figure is resolved against the SUMMARY LINE that reports it, by an
    anchored regex, never by searching the output for a digit string. A number
    that happens to appear elsewhere in the file (a line number, a page count,
    a denominator) must not be able to satisfy a check.

exit 0 written, 2 refusal, 3 crash.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
OUTD = SESS / "outputs"
DST = SESS / "claims.jsonl"

TASK = "CT-S52-XI0-LOGS-REVISION"

_cache: dict[str, str] = {}


def out(name: str) -> str:
    if name not in _cache:
        p = OUTD / name
        if not p.exists():
            refuse(f"cited output {name} does not exist")
        _cache[name] = p.read_text(encoding="utf-8", errors="replace")
    return _cache[name]


def sha(name: str) -> str:
    return hashlib.sha256((OUTD / name).read_bytes()).hexdigest()


PROBLEMS: list[str] = []


def refuse(why: str) -> None:
    print("REFUSED: " + why, file=sys.stderr)
    sys.exit(2)


CLAIMS: list[dict] = []


def claim(cid, label, text, evtype, script, outfile, anchor, dps=None,
          supersedes=None):
    """anchor: regex that must match EXACTLY ONE line of the cited output.

    The matched line is stored as the claim's evidence, so the record carries
    the summary line that reports the figure, not a free-floating number.
    """
    body = out(outfile)
    hits = [ln for ln in body.splitlines() if re.search(anchor, ln)]
    if len(hits) != 1:
        PROBLEMS.append(
            f"{cid}: anchor {anchor!r} matched {len(hits)} lines in "
            f"{outfile} (need exactly 1)")
        evidence = None
    else:
        evidence = hits[0].strip()
    CLAIMS.append({
        "claim_id": cid,
        "task_id": TASK,
        "label": label,
        "claim": text,
        "evidence_type": evtype,
        "evidence": evidence,
        "dps": dps,
        "reproducible": True,
        "script": script,
        "output_file": outfile,
        "output_hash": sha(outfile),
        **({"supersedes": supersedes} if supersedes else {}),
    })


XI = "scripts/xi0_logs.py"
XO = "xi0_logs.out.txt"
AR = "scripts/apply_revision.py"
AO = "apply_revision.out.txt"
DR = "scripts/diff_render.py"
DO = "diff_render.out.txt"
SW = "scripts/sweep.py"

# ---------------------------------------------------------------- PART A
claim("S52-01", "PROVEN",
      "The coefficients p_0..p_4 of L_V parsed from Appendix A.1 of the "
      "submitted source agree entry for entry with an independently typed "
      "hand transcription (12 entries).",
      "file_inspection", XI, XO,
      r"^  12 coefficient entries compared, parser vs independent hand table: AGREE$")

claim("S52-02", "PROVEN",
      "L_V applied to B-hat gives an exactly vanishing residual for every "
      "coefficient order N = 0..129, in exact Q(sqrt3) arithmetic. This "
      "reproduces the residual check the manuscript states in Appendix A.1.",
      "computation", XI, XO, r"^  nonzero residuals: 0$", dps="exact")

claim("S52-03", "PROVEN",
      "The indicial equation of L_V at xi = 0 has exactly the roots "
      "{-1, 0, 1, 2}, computed exactly.",
      "computation", XI, XO,
      r"^  exponents at xi = 0: \{-1, 0, 1, 2\}", dps="exact")

claim("S52-04", "PROVEN",
      "The first resonant step of the Frobenius recursion started from the "
      "lowest exponent s = -1 is obstructed by the nonzero element "
      "(38286 + 24984 sqrt3)/418501 of Q(sqrt3); hence no formal solution of "
      "L_V has leading exponent exactly -1.",
      "computation", XI, XO,
      r"^      n=1  constraint exponent 0: obstruction 38286/418501 \+ "
      r"24984/418501\*sqrt3 must vanish$", dps="exact")

claim("S52-05", "PROVEN",
      "The log-free local solution space of L_V at xi = 0 has dimension 3 "
      "(leading exponents 0, 1, 2) out of the 4 required, so exactly one "
      "local solution carries log xi. xi = 0 is a genuine regular singular "
      "point with unipotent local monodromy, NOT an apparent singularity.",
      "computation", XI, XO,
      r"^  a log-free local basis has dimension 3 of the 4 required$",
      dps="exact")

claim("S52-06", "VERIFIED",
      "Route 2, an independent Gaussian elimination on the truncated Laurent "
      "ansatz carrying no notion of indicial exponent or resonance, returns "
      "log-free dimension 3, agreeing with Route 1. This is a truncation "
      "argument (stable at M = 16 and M = 24), not a proof about the infinite "
      "system.",
      "computation", XI, XO, r"^  Route 2 log-free dimension: 3$", dps="exact")

claim("S52-07", "PROVEN",
      "Route 3 exhibits the logarithmic solution positively rather than "
      "inferring it from an absence: the total local solution dimension is 4, "
      "of which one carries a nonzero log part.",
      "computation", XI, XO,
      r"^      total local solution dimension found: 4$", dps="exact")

claim("S52-08", "PROVEN",
      "PART A VERDICT: LOGARITHMS FOUND. The manuscript's stated ground for "
      "apparency at xi = 0 -- that the four exponents are consecutive "
      "integers -- does not support the conclusion: consecutive integer "
      "exponents make the point resonant, which is precisely the case in "
      "which a logarithm can be forced, and here one is.",
      "computation", XI, XO,
      r"^  PART A VERDICT \(observable, before controls\): LOGARITHMS FOUND$",
      dps="exact")

claim("S52-09", "PROVEN",
      "Both controls fired: C-LOG, an operator with a known logarithm at an "
      "integer exponent, is detected; C-NOLOG, a known log-free operator with "
      "a consistent resonance, is not reported as logarithmic. The observable "
      "was evaluated before any vacuity pre-check, per the CT-S47 ordering "
      "rule.",
      "computation", XI, XO, r"^  controls: 2/2 FIRED$", dps="exact")

claim("S52-10", "VERIFIED",
      "Vacuity pre-check for the residual observable: perturbing the constant "
      "term of p_2 by +1/418501 produces 21 nonzero residuals in N = 0..20, "
      "so the residual check does move when the operator moves.",
      "computation", XI, XO,
      r"^  p_2 constant term perturbed by \+1/418501; nonzero residuals in "
      r"N=0\.\.20: 21$", dps="exact")

# ---------------------------------------------------------------- PART B
claim("S52-11", "VERIFIED",
      "The LaTeX source of the submitted PDF was identified by rebuilding "
      "every name-matching candidate and comparing text layers, not by "
      "filename. Exactly one byte-distinct source reproduces the submitted "
      "text layer.",
      "build", "scripts/identify_source.py", "identify_source.out.txt",
      r"^  SOURCE OF RECORD: sessions\\2026-06-16\\VQUAD-PAPER-LAYOUTFIX-001\\latex\\vquad-periodrep-paper\.tex$")

claim("S52-12", "VERIFIED",
      "Amendment-H sweep of the submitted source BEFORE editing, over the "
      "eight operator-named terms, returns 56 hits.",
      "file_inspection", SW, "sweep_before.out.txt",
      r"^TOTAL HITS ACROSS ALL TERMS: 56$")

claim("S52-13", "VERIFIED",
      "The revision consists of 18 tabled replacements, each of which had to "
      "match the submitted source exactly once or the script refuses. The "
      "submitted source is byte-unchanged afterwards.",
      "build", AR, AO, r"^  submitted source unchanged: YES$")

claim("S52-14", "VERIFIED",
      "The revised copy is byte-identical to the pristine submitted source "
      "with the 18 tabled replacements applied, reconstructed independently "
      "of the patch script's own run; nothing was edited out of band. The "
      "check was shown to fail on a planted one-word edit.",
      "build", DR, DO,
      r"^RECONSTRUCTION: byte-identical")

claim("S52-15", "VERIFIED",
      "Rendered comparison against the SUBMITTED PDF, identified by its "
      "published md5 rather than its filename: the revision grows the paper "
      "from 24 to 26 pages.",
      "build", DR, DO,
      r"^pages         : submitted 24  ->  revised 26   \(delta \+2\)$")

claim("S52-16", "VERIFIED",
      "Amendment-H sweep re-run on the revised copy returns 58 hits; every "
      "remaining hit is accounted for in CHANGES.md, including the ones "
      "deliberately left unedited.",
      "file_inspection", SW, "sweep_after.out.txt",
      r"^TOTAL HITS ACROSS ALL TERMS: 58$")


def main() -> int:
    # ---- validate the in-memory buffer BEFORE writing anything ----
    seen = set()
    for c in CLAIMS:
        if c["claim_id"] in seen:
            PROBLEMS.append(f"duplicate claim_id {c['claim_id']}")
        seen.add(c["claim_id"])
        if not c["evidence"] or not c["evidence"].strip():
            PROBLEMS.append(f"{c['claim_id']}: empty evidence")
        if c["label"] not in ("PROVEN", "VERIFIED", "STRUCTURAL",
                              "CONJECTURED"):
            PROBLEMS.append(f"{c['claim_id']}: bad label {c['label']}")
        if len(c["output_hash"]) != 64:
            PROBLEMS.append(f"{c['claim_id']}: bad output_hash")
        if not (SESS / c["script"]).exists():
            PROBLEMS.append(f"{c['claim_id']}: script {c['script']} missing")

    if PROBLEMS:
        print("REFUSED -- nothing written. Problems:", file=sys.stderr)
        for p in PROBLEMS:
            print("  " + p, file=sys.stderr)
        return 2

    buf = "\n".join(json.dumps(c, ensure_ascii=False) for c in CLAIMS) + "\n"
    # re-parse the buffer before it touches the disk
    for ln in buf.strip().split("\n"):
        json.loads(ln)
    DST.write_text(buf, encoding="utf-8")
    print(f"wrote {len(CLAIMS)} claims -> {DST}")
    print("claims.jsonl sha256: "
          + hashlib.sha256(DST.read_bytes()).hexdigest())
    for c in CLAIMS:
        print(f"  {c['claim_id']}  {c['label']:<10} {c['claim'][:58]}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        print(f"CRASH: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(3)
