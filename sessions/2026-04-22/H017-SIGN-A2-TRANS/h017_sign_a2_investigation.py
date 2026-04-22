#!/usr/bin/env python3
"""
H017-SIGN-A2-TRANS: Investigate sign(a2) anomaly in Trans families.

22/24 Trans families have a2 < 0. The 2 exceptions have a=[1,2,1].
Determine whether this is structural or an artifact.

Tasks:
  1. Characterize the 2 exceptions (b poly, K value, PSLQ relation, disc_a)
  2. Compare convergence rates (positive vs negative a2 Trans families)
  3. disc_a distribution across all 24 Trans families
  4. Enrichment analysis: sign(a2)=-1 among Trans vs full non-Rat space
"""

import json
import hashlib
import itertools
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import mpmath
from mpmath import mpf, mp
from scipy.stats import fisher_exact

# ── Configuration ──────────────────────────────────────────────────
COEFF_RANGE = list(range(-4, 5))  # [-4, 4]
DPS_WORK = 50
N_WORK = 500
SCRIPT_NAME = "h017_sign_a2_investigation.py"
OUT_DIR = Path(__file__).parent
CLAIMS_FILE = OUT_DIR / "claims.jsonl"

def sha256_of(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

def aeal_claim(claim, dps, output_hash=""):
    with open(CLAIMS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "claim": claim, "evidence_type": "computation",
            "dps": dps, "reproducible": True,
            "script": SCRIPT_NAME, "output_hash": output_hash
        }) + "\n")

def halt(reason, details=None):
    with open(OUT_DIR / "halt_log.json", "w") as f:
        json.dump({"reason": reason, "details": details,
                    "time": datetime.now(timezone.utc).isoformat()}, f, indent=2)
    print(f"HALT: {reason}")
    sys.exit(1)

def eval_pcf(a_coeffs, b_coeffs, N, dps):
    """Evaluate PCF limit. Coefficients are [a2, a1, a0], [b2, b1, b0]."""
    mp.dps = dps + 50
    a2, a1, a0 = mpf(a_coeffs[0]), mpf(a_coeffs[1]), mpf(a_coeffs[2])
    b2, b1, b0 = mpf(b_coeffs[0]), mpf(b_coeffs[1]), mpf(b_coeffs[2])
    Pp, Pc = mpf(1), b0
    Qp, Qc = mpf(0), mpf(1)
    for n in range(1, N + 1):
        an = a2*n*n + a1*n + a0
        bn = b2*n*n + b1*n + b0
        Pn = bn*Pc + an*Pp
        Qn = bn*Qc + an*Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if n % 50 == 0 and Qc != 0:
            s = abs(Qc)
            if s > mpf(10)**20:
                Pc /= s; Pp /= s; Qc /= s; Qp /= s
    if Qc == 0:
        return None
    mp.dps = dps
    return +(Pc / Qc)

def eval_pcf_at_N(a_coeffs, b_coeffs, N, dps):
    """Evaluate PCF at exactly N terms (for convergence comparison)."""
    return eval_pcf(a_coeffs, b_coeffs, N, dps)


# ── Load data ──────────────────────────────────────────────────────
print("Loading Trans families...")
with open(OUT_DIR / "trans_families.json") as f:
    trans_families = json.load(f)

with open(OUT_DIR / "f1_base_certificate.json") as f:
    cert = json.load(f)

print(f"  {len(trans_families)} Trans families loaded")
print(f"  Total convergent: {cert['convergent']}")
print(f"  Rat count: {cert['strata']['Rat']['count']}")


# ══════════════════════════════════════════════════════════════════
# TASK 1: Characterize the 2 exceptions
# ══════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("TASK 1: Characterize the 2 exceptions (a2 > 0)")
print("="*60)

exceptions = []
for fam in trans_families:
    a = fam["family"]["a"]
    if a[0] > 0:  # a2 > 0 (leading coefficient)
        b = fam["family"]["b"]
        idx = fam["index"]
        disc_a = a[1]**2 - 4*a[0]*a[2]  # a1^2 - 4*a2*a0

        # Compute K at dps=50
        K = eval_pcf(a, b, N_WORK, DPS_WORK)
        K_str = mpmath.nstr(K, 50) if K is not None else "FAILED"

        exc = {
            "index": idx,
            "a": a,
            "b": b,
            "K": K_str,
            "disc_a": disc_a,
            "relation": fam["relation"],
            "basis": fam["basis"],
            "a_factored": f"a(n) = (n+1)^2" if a == [1, 2, 1] else "not perfect square",
            "a_roots": "double root at n=-1 (negative integer)"
        }
        exceptions.append(exc)
        print(f"\n  Index {idx}: a={a}, b={b}")
        print(f"    disc_a = {disc_a} (double root)")
        print(f"    K = {K_str}")
        print(f"    relation = {fam['relation']}")
        print(f"    a(n) = n^2 + 2n + 1 = (n+1)^2")

if len(exceptions) != 2:
    halt("Expected exactly 2 exceptions with a2>0",
         {"found": len(exceptions)})

# Verify both have a=[1,2,1]
for exc in exceptions:
    if exc["a"] != [1, 2, 1]:
        halt("Exception has unexpected a coefficients", exc)

print(f"\n  Both exceptions have a=[1,2,1], disc_a=0, double root at n=-1")
print(f"  This negative integer root is NOT caught by structural Rat screen")
print(f"  (Rat screen checks a(k)=0 for k>=1, not k<=-1)")


# ══════════════════════════════════════════════════════════════════
# TASK 2: Compare convergence rates
# ══════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("TASK 2: Compare convergence rates")
print("="*60)

# Select 3 negative-a2 Trans families for comparison
neg_a2_fams = [f for f in trans_families if f["family"]["a"][0] < 0]
pos_a2_fams = [f for f in trans_families if f["family"]["a"][0] > 0]

# Pick 3 negative-a2 families with different a coefficients
seen_a = set()
neg_a2_samples = []
for f in neg_a2_fams:
    key = tuple(f["family"]["a"])
    if key not in seen_a:
        neg_a2_samples.append(f)
        seen_a.add(key)
    if len(neg_a2_samples) == 3:
        break

test_fams = neg_a2_samples + pos_a2_fams
N_values = [100, 200, 300, 400]
N_ref = 500

convergence_results = []
print(f"\n  Computing K_500 reference values at dps={DPS_WORK}...")

for fam in test_fams:
    a = fam["family"]["a"]
    b = fam["family"]["b"]
    idx = fam["index"]
    sign_label = "a2>0" if a[0] > 0 else "a2<0"

    K_ref = eval_pcf(a, b, N_ref, DPS_WORK)
    if K_ref is None:
        print(f"  WARNING: K_500 failed for index {idx}")
        continue

    errors = {}
    for N in N_values:
        K_N = eval_pcf(a, b, N, DPS_WORK)
        if K_N is not None:
            err = float(abs(K_N - K_ref))
            errors[N] = err

    entry = {
        "index": idx,
        "a": a,
        "b": b,
        "sign_a2": sign_label,
        "K_500": mpmath.nstr(K_ref, 30),
        "convergence_errors": {str(n): e for n, e in errors.items()}
    }
    convergence_results.append(entry)

    print(f"\n  Index {idx} ({sign_label}): a={a}, b={b}")
    for N in N_values:
        if N in errors:
            print(f"    |K_{N} - K_500| = {errors[N]:.6e}")

# Summarize: average error for positive vs negative a2
pos_errors = {N: [] for N in N_values}
neg_errors = {N: [] for N in N_values}
for r in convergence_results:
    bucket = pos_errors if ">" in r["sign_a2"] else neg_errors
    for N in N_values:
        key = str(N)
        if key in r["convergence_errors"]:
            bucket[N].append(r["convergence_errors"][key])

print("\n  Average |K_N - K_500|:")
print(f"  {'N':>5}  {'a2<0 (avg)':>14}  {'a2>0 (avg)':>14}")
convergence_summary = {}
for N in N_values:
    avg_neg = np.mean(neg_errors[N]) if neg_errors[N] else float('nan')
    avg_pos = np.mean(pos_errors[N]) if pos_errors[N] else float('nan')
    print(f"  {N:>5}  {avg_neg:>14.6e}  {avg_pos:>14.6e}")
    convergence_summary[str(N)] = {"a2_neg_avg": avg_neg, "a2_pos_avg": avg_pos}


# ══════════════════════════════════════════════════════════════════
# TASK 3: disc_a distribution across all 24 Trans families
# ══════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("TASK 3: disc_a distribution in Trans families")
print("="*60)

disc_neg = 0
disc_zero = 0
disc_pos = 0
disc_details = []

for fam in trans_families:
    a = fam["family"]["a"]
    a2, a1, a0 = a[0], a[1], a[2]
    disc = a1**2 - 4*a2*a0
    sign_a2 = "positive" if a2 > 0 else ("zero" if a2 == 0 else "negative")

    if disc < 0:
        disc_neg += 1
    elif disc == 0:
        disc_zero += 1
    else:
        disc_pos += 1

    disc_details.append({
        "index": fam["index"],
        "a": a,
        "disc_a": disc,
        "sign_a2": sign_a2
    })

print(f"  disc_a < 0: {disc_neg}")
print(f"  disc_a = 0: {disc_zero}")
print(f"  disc_a > 0: {disc_pos}")

# Check: all disc_a >= 0 as expected from DISC-A-DESERT-CHECK
if disc_neg > 0:
    halt("Found disc_a < 0 in Trans families — contradicts prior result",
         {"count": disc_neg})

print(f"\n  Detailed distribution:")
unique_a = {}
for d in disc_details:
    key = tuple(d["a"])
    if key not in unique_a:
        unique_a[key] = {"a": d["a"], "disc_a": d["disc_a"],
                         "sign_a2": d["sign_a2"], "count": 0}
    unique_a[key]["count"] += 1

for key, info in sorted(unique_a.items()):
    print(f"    a={info['a']}, disc_a={info['disc_a']}, "
          f"sign_a2={info['sign_a2']}, count={info['count']}")


# ══════════════════════════════════════════════════════════════════
# TASK 4: Enrichment analysis
# ══════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("TASK 4: Enrichment of sign(a2)=-1 in Trans")
print("="*60)

# Count non-Rat families with a2 < 0 in the full F(2,4) space
# We enumerate all convergent non-Rat families and count sign(a2)
# Non-Rat = Trans + Des = 400093 + 24 = 400117
# Total convergent = 513387, Rat = 113270

total_convergent = cert["convergent"]  # 513387
n_rat = cert["strata"]["Rat"]["count"]  # 113270
n_non_rat = total_convergent - n_rat  # 400117

# To get the fraction of non-Rat families with a2<0, we need to enumerate
# We can compute this analytically from the coefficient range
# OR enumerate. Let's enumerate for exactness.

print(f"  Enumerating all {total_convergent} convergent families to count a2<0...")
print(f"  (Using numpy vectorized approach for speed)")

# Generate all coefficient combinations
coeffs = np.array(list(itertools.product(COEFF_RANGE, repeat=6)))
print(f"  Total families: {len(coeffs)}")

a_coeffs = coeffs[:, :3]  # [a2, a1, a0]
b_coeffs = coeffs[:, 3:]  # [b2, b1, b0]

# Quick convergence check: use the same vectorized approach as f1_base
# A family converges if |a(n)| << |b(n)|^2 asymptotically
# The leading coefficient determines: need b2 != 0 or specific conditions
# Actually, let's just count from the known partition structure.

# We know structural Rat families have a(k)=0 for some k in [1, 100].
# For the enrichment, we need the sign(a2) distribution among non-Rat
# convergent families. Let me enumerate properly.

# Since the Rat screen is structural (a(k)=0 for integer k>=1), we can:
# 1) Check convergence via numpy vectorized
# 2) Subtract structural Rat
# 3) Count a2 < 0 among the rest

# Convergence: evaluate |K_N| for moderate N using numpy
print("  Checking convergence with vectorized evaluation...")
N_conv = 200  # sufficient for convergence check

# Vectorized PCF evaluation at float precision
a2v = a_coeffs[:, 0].astype(np.float64)
a1v = a_coeffs[:, 1].astype(np.float64)
a0v = a_coeffs[:, 2].astype(np.float64)
b2v = b_coeffs[:, 0].astype(np.float64)
b1v = b_coeffs[:, 1].astype(np.float64)
b0v = b_coeffs[:, 2].astype(np.float64)

M = len(coeffs)
Pp = np.ones(M)
Pc = b0v.copy()
Qp = np.zeros(M)
Qc = np.ones(M)
alive = np.ones(M, dtype=bool)

for n in range(1, N_conv + 1):
    nf = float(n)
    an = a2v * nf * nf + a1v * nf + a0v
    bn = b2v * nf * nf + b1v * nf + b0v

    Pn = bn * Pc + an * Pp
    Qn = bn * Qc + an * Qp
    Pp[:] = Pc; Pc[:] = Pn
    Qp[:] = Qc; Qc[:] = Qn

    # Rescale periodically
    if n % 20 == 0:
        scale = np.abs(Qc)
        big = (scale > 1e100) & alive
        if np.any(big):
            Pc[big] /= scale[big]
            Pp[big] /= scale[big]
            Qc[big] /= scale[big]
            Qp[big] /= scale[big]

        # Mark diverged
        bad = (np.abs(Pc) > 1e300) | (np.abs(Qc) > 1e300) | np.isnan(Pc) | np.isnan(Qc)
        alive &= ~bad

# Convergent = alive and Qc != 0
convergent_mask = alive & (np.abs(Qc) > 1e-300)
K_vals = np.where(convergent_mask, Pc / Qc, np.nan)
convergent_mask &= np.isfinite(K_vals)

n_convergent_approx = np.sum(convergent_mask)
print(f"  Approximate convergent count: {n_convergent_approx}")
print(f"  (Certificate says: {total_convergent})")

# Structural Rat check: a(k)=0 for some integer k in [1, 100]
struct_rat = np.zeros(M, dtype=bool)
for k in range(1, 101):
    kf = float(k)
    val = a2v * kf * kf + a1v * kf + a0v
    struct_rat |= (np.abs(val) < 0.5)  # integer coefficients, so exact

# Non-Rat convergent families
non_rat_conv = convergent_mask & ~struct_rat
n_non_rat_approx = np.sum(non_rat_conv)
print(f"  Non-Rat convergent (approx): {n_non_rat_approx}")
print(f"  (Certificate says: {n_non_rat})")

# Count a2 < 0 among non-Rat convergent
a2_neg_non_rat = np.sum(non_rat_conv & (a2v < 0))
a2_zero_non_rat = np.sum(non_rat_conv & (a2v == 0))
a2_pos_non_rat = np.sum(non_rat_conv & (a2v > 0))
total_non_rat_check = int(a2_neg_non_rat + a2_zero_non_rat + a2_pos_non_rat)

print(f"\n  Among non-Rat convergent families:")
print(f"    a2 < 0: {a2_neg_non_rat} ({100*a2_neg_non_rat/total_non_rat_check:.1f}%)")
print(f"    a2 = 0: {a2_zero_non_rat} ({100*a2_zero_non_rat/total_non_rat_check:.1f}%)")
print(f"    a2 > 0: {a2_pos_non_rat} ({100*a2_pos_non_rat/total_non_rat_check:.1f}%)")

# Trans a2 distribution
n_trans_a2_neg = sum(1 for f in trans_families if f["family"]["a"][0] < 0)
n_trans_a2_zero = sum(1 for f in trans_families if f["family"]["a"][0] == 0)
n_trans_a2_pos = sum(1 for f in trans_families if f["family"]["a"][0] > 0)
n_trans = len(trans_families)

frac_trans_a2_neg = n_trans_a2_neg / n_trans
frac_nonrat_a2_neg = float(a2_neg_non_rat) / total_non_rat_check

print(f"\n  Trans a2<0 fraction: {n_trans_a2_neg}/{n_trans} = {frac_trans_a2_neg:.4f}")
print(f"  Non-Rat a2<0 fraction: {int(a2_neg_non_rat)}/{total_non_rat_check} = {frac_nonrat_a2_neg:.4f}")

enrichment_ratio = frac_trans_a2_neg / frac_nonrat_a2_neg if frac_nonrat_a2_neg > 0 else float('inf')
print(f"  Enrichment ratio: {enrichment_ratio:.4f}")

# Fisher exact test
# Contingency table:
#                 a2<0    a2>=0
# Trans           22      2
# Non-Rat other   a2_neg  (total - a2_neg - 22)
# We use non-Rat minus Trans as the background
bg_a2_neg = int(a2_neg_non_rat) - n_trans_a2_neg
bg_a2_nonneg = total_non_rat_check - int(a2_neg_non_rat) - (n_trans - n_trans_a2_neg)

table = [[n_trans_a2_neg, n_trans - n_trans_a2_neg],
         [bg_a2_neg, bg_a2_nonneg]]
print(f"\n  Fisher exact test contingency table:")
print(f"               a2<0    a2>=0")
print(f"    Trans      {table[0][0]:>6}  {table[0][1]:>6}")
print(f"    Other      {table[1][0]:>6}  {table[1][1]:>6}")

odds_ratio, p_value = fisher_exact(table, alternative='greater')
print(f"  Odds ratio: {odds_ratio:.4f}")
print(f"  p-value (one-sided, greater): {p_value:.6e}")


# ══════════════════════════════════════════════════════════════════
# Determine hypothesis status
# ══════════════════════════════════════════════════════════════════
if p_value < 0.01 and enrichment_ratio > 1.5:
    hypothesis_status = "ASSOCIATION"
    structural_note = (
        "sign(a2)<0 is significantly enriched in Trans families "
        f"(enrichment {enrichment_ratio:.2f}x, p={p_value:.2e}). "
        "The 2 exceptions with a2>0 share a=[1,2,1] => a(n)=(n+1)^2, "
        "which has disc_a=0 (double root at n=-1). This degenerate "
        "quadratic behaves structurally differently from generic a2>0 "
        "families. The association is genuine but not an implication: "
        "a2<0 is necessary-ish but disc_a=0 provides the escape route."
    )
elif p_value < 0.05:
    hypothesis_status = "WEAK_ASSOCIATION"
    structural_note = "Marginal statistical significance."
else:
    hypothesis_status = "ARTIFACT"
    structural_note = "No significant enrichment detected."

print(f"\n  Hypothesis status: {hypothesis_status}")
print(f"  {structural_note}")


# ══════════════════════════════════════════════════════════════════
# Build report
# ══════════════════════════════════════════════════════════════════
report = {
    "task_id": "H017-SIGN-A2-TRANS",
    "date": datetime.now(timezone.utc).isoformat(),
    "n_trans_a2_neg": n_trans_a2_neg,
    "n_trans_a2_zero": n_trans_a2_zero,
    "n_trans_a2_pos": n_trans_a2_pos,
    "exceptions": exceptions,
    "disc_a_distribution": {
        "negative": disc_neg,
        "zero": disc_zero,
        "positive": disc_pos
    },
    "disc_a_details": [
        {"a": info["a"], "disc_a": info["disc_a"],
         "sign_a2": info["sign_a2"], "family_count": info["count"]}
        for info in sorted(unique_a.values(), key=lambda x: tuple(x["a"]))
    ],
    "convergence_comparison": {
        "test_families": convergence_results,
        "summary": {
            str(N): {"a2_neg_avg": float(convergence_summary[str(N)]["a2_neg_avg"]),
                      "a2_pos_avg": float(convergence_summary[str(N)]["a2_pos_avg"])}
            for N in N_values
        }
    },
    "enrichment_analysis": {
        "non_rat_total": total_non_rat_check,
        "non_rat_a2_neg": int(a2_neg_non_rat),
        "non_rat_a2_zero": int(a2_zero_non_rat),
        "non_rat_a2_pos": int(a2_pos_non_rat),
        "frac_trans_a2_neg": frac_trans_a2_neg,
        "frac_nonrat_a2_neg": frac_nonrat_a2_neg,
        "enrichment_ratio": float(enrichment_ratio),
        "fisher_table": table,
        "odds_ratio": float(odds_ratio),
        "p_value": float(p_value)
    },
    "hypothesis_status": hypothesis_status,
    "structural_note": structural_note
}

out_path = OUT_DIR / "h017_sign_a2_report.json"
with open(out_path, "w") as f:
    json.dump(report, f, indent=2)
print(f"\nReport written to {out_path}")

# ── AEAL claims ──────────────────────────────────────────────────
h = sha256_of(report)
aeal_claim(
    f"H017-SIGN-A2: 22/24 Trans have a2<0, 2 exceptions a=[1,2,1] disc_a=0. "
    f"Enrichment ratio={enrichment_ratio:.2f}x, Fisher p={p_value:.2e}",
    dps=DPS_WORK, output_hash=h
)
aeal_claim(
    f"H017-SIGN-A2: disc_a distribution in Trans: neg={disc_neg}, zero={disc_zero}, pos={disc_pos}. "
    f"All disc_a >= 0 (confirmed, no disc_a<0 in Trans).",
    dps=0, output_hash=h
)
aeal_claim(
    f"H017-SIGN-A2: Exceptions a=[1,2,1] have a(n)=(n+1)^2 with double root at n=-1. "
    f"Status: {hypothesis_status}",
    dps=DPS_WORK, output_hash=h
)

print("\n3 AEAL claims written.")
print("Done.")
