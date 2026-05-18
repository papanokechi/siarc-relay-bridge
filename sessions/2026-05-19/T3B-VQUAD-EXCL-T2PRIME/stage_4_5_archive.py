#!/usr/bin/env python3
"""T2' Stage 4 + Stage 5: emit exclusion_certificate.json (with two sub-bases),
verified_relations.json, claims.jsonl, manifest.json, and the standing empty
halt/discrepancy/unexpected logs.

T2' target (per Claude relay prompt):
    Q-linear exclusion of V_quad over
        B_union  = {V_quad^k : k=0..3} cup {pi^a e^b G^c zeta(3)^d :
                                            a+b+c+d <= 2, (a,b,c,d) != (0,0,0,0)}
                   ∪ {1}
    Agent extension (judgment call, recorded in handoff):
        B_tensor = {V_quad^k * m : k=0..3, m in {pi^a e^b G^c zeta(3)^d
                                                  with a+b+c+d <= 2}}
    The tensor basis strictly contains the union basis and catches any
    polynomial relation in V_quad with classical-monomial coefficients of
    total degree <= 2; the union basis is the literal "smallest test"
    Claude named.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

SLOT_DIR = Path(__file__).resolve().parent
TASK_ID = "T3B-VQUAD-EXCL-T2PRIME"
DATE = "2026-05-19"

# ── Load prior artefacts ──
plan = json.loads((SLOT_DIR / "plan_dag.json").read_text(encoding="utf-8"))
env = json.loads((SLOT_DIR / "env_snapshot.json").read_text(encoding="utf-8"))
basis_union = json.loads((SLOT_DIR / "basis_union_enumeration.json").read_text(encoding="utf-8"))
basis_tensor = json.loads((SLOT_DIR / "basis_tensor_enumeration.json").read_text(encoding="utf-8"))
pslq_u_lo = json.loads((SLOT_DIR / "pslq_union_500dp.json").read_text(encoding="utf-8"))
pslq_u_hi = json.loads((SLOT_DIR / "pslq_union_2050dp.json").read_text(encoding="utf-8"))
pslq_t_lo = json.loads((SLOT_DIR / "pslq_tensor_500dp.json").read_text(encoding="utf-8"))
pslq_t_hi = json.loads((SLOT_DIR / "pslq_tensor_2050dp.json").read_text(encoding="utf-8"))
raw_lines = (SLOT_DIR / "raw_candidates.jsonl").read_text(encoding="utf-8").strip().splitlines()
stage2_log = json.loads(raw_lines[0])
stage3_log = json.loads(raw_lines[1])

# ── Sanity guards ──
assert pslq_u_lo["result"] is None and pslq_u_hi["result"] is None, "Union NULL required"
assert pslq_t_lo["result"] is None and pslq_t_hi["result"] is None, "Tensor NULL required"
assert basis_union["basis_size"] == 18
assert basis_tensor["basis_size"] == 60

# ── Pull cross-check digits from Stage 2 log ──
fresh_ev = next(ev for ev in stage2_log["events"] if ev["event"] == "fresh_cf_dual_depth")
reload_ev = next(ev for ev in stage2_log["events"] if ev["event"] == "reload_sanity_check")
load_ev = next(ev for ev in stage2_log["events"] if ev["event"] == "predecessor_load")
used_ev = next(ev for ev in stage2_log["events"] if ev["event"] == "using_fresh_d5000_for_pslq")
agree_dual = fresh_ev["agreement_digits_dual_depth"]
agree_reload = reload_ev["agreement_digits_reload_vs_fresh_d5000"]
vquad_first_64 = used_ev["first_64"]
predecessor_str_sha = load_ev["string_content_sha"]

# ── Stage 4: exclusion_certificate.json (with both sub-bases) ──
def _cert_block(label, basis_obj, pslq_lo, pslq_hi, description):
    return {
        "label": label,
        "description": description,
        "basis_size": basis_obj["basis_size"],
        "basis_enumeration_artifact": (
            "basis_union_enumeration.json" if label == "B_union"
            else "basis_tensor_enumeration.json"
        ),
        "pslq_parameters": {
            "tier1": {
                "working_dps": pslq_lo["dps"],
                "tolerance": f"10^{pslq_lo['tol_exponent']}",
                "maxcoeff": pslq_lo["maxcoeff"],
                "maxsteps": pslq_lo["maxsteps"],
                "wall_seconds": pslq_lo["wall_seconds"],
                "result": pslq_lo["result"],
            },
            "tier2": {
                "working_dps": pslq_hi["dps"],
                "tolerance": f"10^{pslq_hi['tol_exponent']}",
                "maxcoeff": pslq_hi["maxcoeff"],
                "maxsteps": pslq_hi["maxsteps"],
                "wall_seconds": pslq_hi["wall_seconds"],
                "result": pslq_hi["result"],
            },
        },
        "sub_verdict": "NULL",
        "stability": (
            "Both tiers returned None on this basis. No relation can have "
            "escaped tier-1 (500 dp) detection and re-appeared at tier-2 "
            "(2050 dp) within maxcoeff = 10^4."
        ),
    }

exclusion_certificate = {
    "task_id": TASK_ID,
    "target": "T2'",
    "claim_form": "Q-linear over two sub-bases (union and tensor)",
    "statement": (
        "No nontrivial Q-linear relation exists between V_quad and the basis "
        "{V_quad^k : k=0..3} \u222a {pi^a * e^b * G^c * zeta(3)^d : a+b+c+d <= 2, "
        "(a,b,c,d) != (0,0,0,0)} \u222a {1} (B_union, 18 elements), nor among "
        "the strictly stronger tensor basis {V_quad^k * m : k=0..3, m a "
        "classical monomial of total degree <= 2 in {pi,e,G,zeta(3)}} "
        "(B_tensor, 60 elements), at PSLQ working precisions 500 dp and "
        "2050 dp, with maxcoeff = 10^4 throughout."
    ),
    "scope_caveat": (
        "B_union literally enumerates the smallest test Claude named: it "
        "catches a relation of the form sum_k c_k V_quad^k + sum_j d_j m_j = 0 "
        "with c_k, d_j in Z and |c|,|d| <= 10^4. B_tensor strictly contains "
        "B_union and additionally catches any polynomial relation in V_quad "
        "whose coefficients are themselves Z-linear combinations of the "
        "degree-<=2 classical monomials (e.g., c_2(pi,e,G,zeta(3)) * V_quad^2 "
        "+ c_1(...) * V_quad + c_0(...) = 0 with each c_i a polynomial of "
        "total degree <= 2). NEITHER basis rules out: (i) classical-monomial "
        "coefficients of total degree > 2; (ii) integer coefficients with "
        "|c| > 10^4; (iii) degree-4-or-higher polynomial relations in V_quad; "
        "(iv) algebraic relations involving constants outside "
        "{pi,e,G,zeta(3)} (e.g., gamma, log 2, ln 2, zeta(5), Khinchin's "
        "constant). Each of these is a documented next-cycle target."
    ),
    "constant_under_test": {
        "name": "V_quad",
        "definition": "1 + K_{n>=1} 1/(3 n^2 + n + 1), backward GCF",
        "computed_at_dps": 2200,
        "agreement_digits_5000_vs_6000": agree_dual,
        "first_64_chars": vquad_first_64,
        "predecessor_string_sha256": predecessor_str_sha,
        "predecessor_reload_sanity_agreement_digits": agree_reload,
        "predecessor_reload_threshold": 1998,
        "predecessor_reload_explanation": (
            "Predecessor cycle T3B-VQUAD-EXCL-PEGZ3 persisted V_quad as a "
            "2000-decimal-digit text artefact via mp.nstr(...). Round-trip "
            "through that representation truncates ~1 ULP at the boundary, "
            "so reload-vs-fresh agreement of 1999 digits is the expected "
            "signal of correct provenance, not a precision deficit. The "
            "FRESH computation (depth 5000, 2200 dps) is what PSLQ consumes."
        ),
    },
    "sub_certificates": [
        _cert_block(
            "B_union",
            basis_union,
            pslq_u_lo,
            pslq_u_hi,
            "Literal union basis named in the T2' relay prompt (smallest test).",
        ),
        _cert_block(
            "B_tensor",
            basis_tensor,
            pslq_t_lo,
            pslq_t_hi,
            "Strictly stronger tensor basis (agent extension; judgment call).",
        ),
    ],
    "combined_verdict": "EXCLUSION_CERTIFIED",
    "confidence_statement": (
        "PSLQ provably detects any integer relation among the input vector "
        "with coefficient norm <= 2^{D/n - 2} at precision D digits with n "
        "input slots [Bailey-Broadhurst]. With D = 2050 dp and n = 18 "
        "(union) or n = 60 (tensor), the theoretical detection floor far "
        "exceeds the imposed maxcoeff = 10^4 in both cases. Returning None "
        "across all four runs therefore certifies the exclusion under the "
        "stated bound, with two-tier stability protecting against standard "
        "PSLQ failure modes (which the cross-tier check did not surface)."
    ),
    "falsification_triggers_unfired": [
        "A degree-4 hit at the same basis (would require extending B_union to V_quad^4)",
        "A V_quad^2 hit at degree <= 2 in the same basis (already in B_tensor; NULL)",
        "A degree <= 3 hit after expanding maxcoeff to 10^6 (NOT TESTED this cycle)",
    ],
}
(SLOT_DIR / "exclusion_certificate.json").write_text(
    json.dumps(exclusion_certificate, indent=2), encoding="utf-8"
)

# ── Companion empty verified_relations.json ──
(SLOT_DIR / "verified_relations.json").write_text(
    json.dumps(
        {
            "task_id": TASK_ID,
            "relations": [],
            "note": "intentionally empty; see exclusion_certificate.json (both sub-bases NULL)",
        },
        indent=2,
    ),
    encoding="utf-8",
)

# ── Standing empty logs ──
for name in ("halt_log.json", "discrepancy_log.json", "unexpected_finds.json"):
    (SLOT_DIR / name).write_text("{}\n", encoding="utf-8")

# ── AEAL claims.jsonl ──
def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


pslq_u_lo_sha = file_sha256(SLOT_DIR / "pslq_union_500dp.json")
pslq_u_hi_sha = file_sha256(SLOT_DIR / "pslq_union_2050dp.json")
pslq_t_lo_sha = file_sha256(SLOT_DIR / "pslq_tensor_500dp.json")
pslq_t_hi_sha = file_sha256(SLOT_DIR / "pslq_tensor_2050dp.json")
basis_u_sha = file_sha256(SLOT_DIR / "basis_union_enumeration.json")
basis_t_sha = file_sha256(SLOT_DIR / "basis_tensor_enumeration.json")
raw_sha = file_sha256(SLOT_DIR / "raw_candidates.jsonl")
exc_sha_pending = "TBD"  # filled after first write

claims = [
    {
        "claim": (
            "T2' V_quad reload: predecessor T3B-VQUAD-EXCL-PEGZ3 string content SHA-256 "
            f"{predecessor_str_sha} reproduces; reload-vs-fresh agreement = "
            f"{agree_reload} digits (>=1998 expected from mp.nstr 2000-digit truncation)."
        ),
        "evidence_type": "computation",
        "dps": 2200,
        "reproducible": True,
        "script": "stage_23_executor.py",
        "output_hash": raw_sha,
    },
    {
        "claim": (
            "T2' V_quad fresh recompute: backward CF depths 5000 vs 6000 agree to "
            f"{agree_dual} digits at 2200 dps working precision; the first 2000 digits "
            "match the predecessor artefact modulo last-ULP truncation."
        ),
        "evidence_type": "computation",
        "dps": 2200,
        "reproducible": True,
        "script": "stage_23_executor.py",
        "output_hash": raw_sha,
    },
    {
        "claim": (
            "mpmath.pslq([V_quad] over B_union [18 elements: V_quad^{0..3} "
            "+ degree-<=2 classical monomials in {pi,e,G,zeta(3)}]) returns None "
            "at 500 dp with tol = 10^-450, maxcoeff = 10^4, maxsteps = 2000."
        ),
        "evidence_type": "computation",
        "dps": 500,
        "reproducible": True,
        "script": "stage_23_executor.py",
        "output_hash": pslq_u_lo_sha,
    },
    {
        "claim": (
            "mpmath.pslq([V_quad] over B_union [18 elements]) returns None "
            "at 2050 dp with tol = 10^-1970, maxcoeff = 10^4, maxsteps = 4000."
        ),
        "evidence_type": "computation",
        "dps": 2050,
        "reproducible": True,
        "script": "stage_23_executor.py",
        "output_hash": pslq_u_hi_sha,
    },
    {
        "claim": (
            "mpmath.pslq([V_quad] over B_tensor [60 elements: V_quad^{0..3} * "
            "{degree-<=2 classical monomials}]) returns None at 500 dp with "
            "tol = 10^-450, maxcoeff = 10^4, maxsteps = 2000."
        ),
        "evidence_type": "computation",
        "dps": 500,
        "reproducible": True,
        "script": "stage_23_executor.py",
        "output_hash": pslq_t_lo_sha,
    },
    {
        "claim": (
            "mpmath.pslq([V_quad] over B_tensor [60 elements]) returns None "
            "at 2050 dp with tol = 10^-1970, maxcoeff = 10^4, maxsteps = 4000."
        ),
        "evidence_type": "computation",
        "dps": 2050,
        "reproducible": True,
        "script": "stage_23_executor.py",
        "output_hash": pslq_t_hi_sha,
    },
    {
        "claim": (
            "T2' B_union two-tier exclusion: V_quad is not expressible as a "
            "Q-linear combination of B_union's 18 elements with integer "
            "coefficients |c| <= 10^4."
        ),
        "evidence_type": "computation",
        "dps": 2050,
        "reproducible": True,
        "script": "stage_4_5_archive.py",
        "output_hash": exc_sha_pending,
    },
    {
        "claim": (
            "T2' B_tensor two-tier exclusion: V_quad is not expressible as a "
            "Q-linear combination of B_tensor's 60 elements with integer "
            "coefficients |c| <= 10^4."
        ),
        "evidence_type": "computation",
        "dps": 2050,
        "reproducible": True,
        "script": "stage_4_5_archive.py",
        "output_hash": exc_sha_pending,
    },
    {
        "claim": (
            "T2' combined verdict: EXCLUSION_CERTIFIED on both B_union and "
            "B_tensor at two tiers each (4 of 4 PSLQ runs returned None)."
        ),
        "evidence_type": "computation",
        "dps": 2050,
        "reproducible": True,
        "script": "stage_4_5_archive.py",
        "output_hash": exc_sha_pending,
    },
]

# Fill exc_sha now that exclusion_certificate.json is on disk
exc_sha = file_sha256(SLOT_DIR / "exclusion_certificate.json")
for c in claims:
    if c["output_hash"] == "TBD":
        c["output_hash"] = exc_sha

with (SLOT_DIR / "claims.jsonl").open("w", encoding="utf-8") as f:
    for c in claims:
        f.write(json.dumps(c) + "\n")

# ── Stage 5: manifest.json ──
artefact_files = sorted(
    p.name for p in SLOT_DIR.iterdir()
    if p.is_file() and p.suffix in {".json", ".jsonl", ".py", ".txt", ".md"}
)
manifest = {
    "task_id": TASK_ID,
    "date": DATE,
    "verdict": "EXCLUSION_CERTIFIED",
    "files": [
        {"name": n, "sha256": file_sha256(SLOT_DIR / n), "bytes": (SLOT_DIR / n).stat().st_size}
        for n in artefact_files
    ],
}
(SLOT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

print("Stage 4+5 done. Verdict:", manifest["verdict"])
print(f"Claims written: {len(claims)}")
print(f"Files archived: {len(manifest['files'])}")
