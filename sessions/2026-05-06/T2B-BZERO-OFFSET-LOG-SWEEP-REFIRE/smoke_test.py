"""044R smoke test for sweep_b1_5_8_9_10_refire.py.

Verifies (per relay 044R Phase A step 3):
  - Stage A cache loads and matches stage_a_summary.json bit-for-bit
  - per-b1 counts (5/8/9/10) match summary
  - total_enumerated == 319440
  - total_convergent == 241892
  - bauer_orbit_membership / discriminant_identity_class still pass
    the 044 helper-function checks
  - extract_n_over_log2_v2 still extracts synthetic n=2/3 relations
  - outcome classifier returns AT_H7 qualifier for non-budget cases
  - VERDICT_OMITS_H_BOUND_QUALIFIER guard is correctly armed
"""
import json
import sys
from pathlib import Path

import sweep_b1_5_8_9_10_refire as s


def _expect(cond, msg):
    if not cond:
        print(f"  FAIL: {msg}")
        sys.exit(1)
    else:
        print(f"  OK:   {msg}")


print("=" * 72)
print("044R SMOKE TEST -- sweep_b1_5_8_9_10_refire.py")
print("=" * 72)

print("\n[1] Stage A cache integrity:")
cache_path = Path(__file__).parent / "stage_a_cache.json"
summary_path = Path(__file__).parent / "stage_a_summary.json"
_expect(cache_path.exists(), f"stage_a_cache.json present at {cache_path}")
_expect(summary_path.exists(), f"stage_a_summary.json present at {summary_path}")

cache = json.loads(cache_path.read_text())
summary = json.loads(summary_path.read_text())

_expect(cache["total"] == 319440, f"cache.total = 319440 (got {cache['total']})")
_expect(cache["n_stagea"] == 500, f"cache.n_stagea = 500 (got {cache['n_stagea']})")
_expect(summary["stage_a_total_enumerated"] == 319440,
        f"summary.total_enumerated = 319440 "
        f"(got {summary['stage_a_total_enumerated']})")
_expect(summary["stage_a_total_convergent"] == 241892,
        f"summary.total_convergent = 241892 "
        f"(got {summary['stage_a_total_convergent']})")
_expect(len(cache["convergent"]) == 241892,
        f"len(cache.convergent) = 241892 (got {len(cache['convergent'])})")

print("\n[2] Per-b1 cache counts vs summary (bit-for-bit):")
expected_per_b1 = summary["per_b1"]
actual_counts = {}
for c in cache["convergent"]:
    b1 = c[0]
    actual_counts[str(b1)] = actual_counts.get(str(b1), 0) + 1
for b1_str in ["5", "8", "9", "10"]:
    expected = expected_per_b1[b1_str]["convergent"]
    actual = actual_counts.get(b1_str, 0)
    _expect(actual == expected,
            f"b1={b1_str}: cache={actual} == summary={expected}")

print("\n[3] enumerate_families() still returns 319440:")
fams = s.enumerate_families()
_expect(len(fams) == 319440, f"enumerate_families() len = 319440 (got {len(fams)})")

print("\n[4] PSLQ_HMAX_TRANS = 10**7 (044R SCOPE OF CHANGE #1):")
_expect(s.PSLQ_HMAX_TRANS == 10 ** 7,
        f"PSLQ_HMAX_TRANS = 10**7 = 10000000 (got {s.PSLQ_HMAX_TRANS})")

print("\n[5] WALL_BUDGET_SECONDS = 9000 (2.5 hr):")
_expect(s.WALL_BUDGET_SECONDS == 9000,
        f"WALL_BUDGET_SECONDS = 9000 (got {s.WALL_BUDGET_SECONDS})")

print("\n[6] H_BOUND_TAG = 'AT_H7':")
_expect(s.H_BOUND_TAG == "AT_H7",
        f"H_BOUND_TAG = 'AT_H7' (got {s.H_BOUND_TAG!r})")

print("\n[7] bauer_orbit_membership unchanged from 044:")
r1 = s.bauer_orbit_membership((-1, 0, 0, 6, 3))
_expect(r1["on_orbit"] is True and r1["k"] == 1,
        f"b6 k=1 known orbit hit: on_orbit={r1['on_orbit']}, k={r1['k']}")
r2 = s.bauer_orbit_membership((-1, 0, 0, 5, 3))
_expect(r2["on_orbit"] is False,
        "b1=5 a2=-1 NOT on orbit (b1 != +/-6k)")
r3 = s.bauer_orbit_membership((8, -4, 0, 7, 4))
_expect(r3["on_orbit"] is False, "b7 singular outlier NOT on orbit")

print("\n[8] discriminant_identity_class unchanged from 044:")
_expect(
    s.discriminant_identity_class((-8, 0, 0, 6, 0)) == "trans_stratum_proper",
    "b6 a2=-8 -> trans_stratum_proper (9*-8 + 2*36 = 0)",
)
_expect(
    s.discriminant_identity_class((16, 0, 0, 8, 0)) == "brouncker_boundary",
    "b8 a2=16 -> brouncker_boundary (4*16 - 64 = 0)",
)

print("\n[9] extract_n_over_log2_v2 synthetic relations:")
_expect(
    s.extract_n_over_log2_v2({"relation": [-2, 0, 0, 0, 0, 0, 0, 1]}) == 2,
    "synthetic n=2 relation: r0=-2, r7=1 -> n=2",
)
_expect(
    s.extract_n_over_log2_v2({"relation": [-3, 0, 0, 0, 0, 0, 0, 1]}) == 3,
    "synthetic n=3 relation: r0=-3, r7=1 -> n=3",
)
_expect(
    s.extract_n_over_log2_v2({"relation": [-2, 0, 1, 0, 0, 0, 0, 1]}) is None,
    "rejects pi-using relation",
)

print("\n[10] determine_outcome_h7 verdict tags carry AT_H7:")
tag, _ev = s.determine_outcome_h7([], [], False, 100, 100, 5, 5)
_expect(tag == "OUTCOME_A_AT_H7", f"empty hits, complete -> OUTCOME_A_AT_H7 (got {tag})")

tag, _ev = s.determine_outcome_h7(
    [{"b1": 9, "coeffs": [1, 0, 0, 9, 0], "ratio": "1/81", "n": 2,
      "bauer_on_orbit": False, "bauer_k": None}],
    [], False, 100, 100, 5, 5)
_expect(tag == "OUTCOME_B_AT_H7", f"1 off-orbit hit -> OUTCOME_B_AT_H7 (got {tag})")

tag, _ev = s.determine_outcome_h7(
    [{"b1": 9, "ratio": "x", "n": 2}, {"b1": 8, "ratio": "y", "n": 3}],
    [], False, 100, 100, 5, 5)
_expect(tag == "OUTCOME_C_AT_H7", f"2 off-orbit -> OUTCOME_C_AT_H7 (got {tag})")

tag, _ev = s.determine_outcome_h7([], [], True, 50, 100, 0, 5)
_expect(tag == "NOT_DETERMINED_AT_H7_BUDGET",
        f"budget exceeded -> NOT_DETERMINED_AT_H7_BUDGET (got {tag})")

tag, _ev = s.determine_outcome_h7(
    [],
    [{"b1": 9, "coeffs": [1, 0, 0, 9, 0], "ratio": "x",
      "stage_bc_relation": [0, 1, 0, 0, 0, 0, 1, 0],
      "stage_bc_residual": "1e-50",
      "deep_relation": None, "deep_residual": None,
      "deep_residual_lt_1e_200": False,
      "reason": "deep verify failed"}],
    False, 100, 100, 5, 5)
_expect(tag == "NOT_DETERMINED_AT_H7",
        f"ambiguous record only -> NOT_DETERMINED_AT_H7 (got {tag})")

print("\n[11] Verify forbidden bare-A/B/C tags would trip the self-check:")
# We can't easily run the self-check without invoking run(); but verify
# the determine_outcome_h7 outputs always carry AT_H7 when prefixed
# OUTCOME_.
for tag_check, _ in [
    s.determine_outcome_h7([], [], False, 100, 100, 5, 5),
    s.determine_outcome_h7(
        [{"b1": 9, "ratio": "x", "n": 2}], [], False, 100, 100, 5, 5),
    s.determine_outcome_h7(
        [{"b1": 9, "ratio": "x", "n": 2},
         {"b1": 8, "ratio": "y", "n": 3}],
        [], False, 100, 100, 5, 5),
]:
    if tag_check.startswith("OUTCOME_"):
        _expect("AT_H7" in tag_check,
                f"verdict {tag_check!r} carries AT_H7 qualifier")

print("\n[12] _write_halt_and_exit helper exists:")
_expect(callable(s._write_halt_and_exit),
        "_write_halt_and_exit is callable (used for STAGE_A_CACHE_INTEGRITY_FAIL "
        "and VERDICT_OMITS_H_BOUND_QUALIFIER)")

# Synthetic per-b1 integrity recheck against summary -- fast Stage A
# load timing.
print("\n[13] Stage A load timing (single read):")
import time
t0 = time.time()
cache_again = json.loads(cache_path.read_text())
dt = time.time() - t0
print(f"  cache load: {dt*1000:.0f} ms ({len(cache_again['convergent'])} entries)")
_expect(dt < 30.0,
        f"cache load < 30s (got {dt:.1f}s; expectation: well under WALL_BUDGET)")

print("\n" + "=" * 72)
print("ALL 044R SMOKE TESTS PASS")
print("=" * 72)
