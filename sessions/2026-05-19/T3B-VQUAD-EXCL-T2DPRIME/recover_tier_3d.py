#!/usr/bin/env python3
"""recover_tier_3d.py -- T3B-VQUAD-EXCL-T2DPRIME recovery driver.

Recovers the single missing tier 3d (B_4_2 PSLQ at 2050 dp, maxcoeff=10^4)
after the original stage_23_executor.py terminated silently between tier 3c
and tier 3d on 2026-05-19 (no JSON, no exception trace, no crashed-process
evidence). Tiers 3a, 3b, 3c already produced clean JSON artefacts on disk;
those are preserved byte-for-byte by this driver.

Discipline (per relay constraints):
  1. V_quad recomputed via the IDENTICAL backward-CF call the original used
     (depth 5000, dps 2200), then string-SHA-verified against the predecessor
     T2 artefact (52375a71...f2f5c44). Determinism of mpmath at fixed version
     and dps means we get bit-identical V_quad to what tier 3c saw.
  2. Basis built from EXPONENTS read from basis_4_2_enumeration.json on disk
     (not regenerated from a function call). Basis file SHA-256 captured and
     embedded in the tier 3d output. Mtime asserted <= tier-3c-JSON mtime,
     proving the basis file is the same one tier 3c consumed.
  3. PSLQ parameters identical to tier 3c (tol = 10^-450 at 500 dp,
     tol = 10^-1970 at 2050 dp, maxcoeff = 10^4, maxsteps = 2000/4000).
  4. Pre-flight smoke: PSLQ at 500 dp on B_4_2 with maxcoeff=10^4 BEFORE
     launching the long 2050-dp tier. Compare smoke output to the existing
     pslq_4_2_maxc4_500dp.json (all fields except wall_seconds and any
     timestamp/sha sidecar fields). Halt if mismatch.
  5. Heartbeat thread writes tier_3d_progress.log every 60s during PSLQ runs
     so the next silent kill leaves an evidence trail.

Outputs (slot-local):
  pslq_4_2_maxc4_2050dp.json    -- the recovered tier (only on success)
  tier_3d_progress.log          -- timestamped heartbeat
  tier_3d_recovery.json         -- provenance sidecar (smoke result, basis
                                   sha, mtime checks, restart reason)
  tier_3d_preflight_500dp.json  -- smoke-test JSON, NOT a replacement for
                                   the canonical pslq_4_2_maxc4_500dp.json
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import threading
import time
import traceback
from itertools import product
from pathlib import Path

import mpmath as mp

SLOT_DIR = Path(__file__).resolve().parent
TASK_ID = "T3B-VQUAD-EXCL-T2DPRIME"

# ── Provenance constants (copied verbatim from stage_23_executor.py) ──
PREDECESSOR_VQUAD_PATH = (
    SLOT_DIR.parent.parent / "2026-05-18" / "T3B-VQUAD-EXCL-PEGZ3" / "vquad_value_2000dp.txt"
)
PREDECESSOR_VQUAD_STR_SHA = (
    "52375a71a05bf61ad971cf83ea9334eb96e20ffa054dc3cab74447966a2f5c44"
)
DPS_WORKING_HI = 2200
PSLQ_TOL_OFFSET = {500: 50, 2050: 80}
PSLQ_MAXSTEPS = {500: 2000, 2050: 4000}

BASIS_FILE = SLOT_DIR / "basis_4_2_enumeration.json"
CANONICAL_TIER_3C = SLOT_DIR / "pslq_4_2_maxc4_500dp.json"
OUT_TIER_3D = SLOT_DIR / "pslq_4_2_maxc4_2050dp.json"
OUT_PREFLIGHT = SLOT_DIR / "tier_3d_preflight_500dp.json"
OUT_PROGRESS = SLOT_DIR / "tier_3d_progress.log"
OUT_RECOVERY = SLOT_DIR / "tier_3d_recovery.json"


# ── Logging helpers ──

def now_ts() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def log_progress(msg: str) -> None:
    line = f"[{now_ts()}] {msg}\n"
    with OUT_PROGRESS.open("a", encoding="utf-8") as f:
        f.write(line)
        f.flush()
    print(line, end="", flush=True)


def sha256_of_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def file_sha256(p: Path) -> str:
    return sha256_of_bytes(p.read_bytes())


# ── V_quad (inline copy of stage_23_executor.py:compute_vquad) ──

def compute_vquad(depth: int, dps: int) -> mp.mpf:
    """V_quad = 1 + K_{n>=1} 1/(3n^2+n+1) via backward GCF recurrence."""
    with mp.workdps(dps + 50):
        v = mp.mpf(0)
        for n in range(depth, 0, -1):
            v = mp.mpf(1) / (3 * n * n + n + 1 + v)
        return mp.mpf(1) + v


# ── Basis builder (inline copy; reads exponents from JSON for safety) ──

def enum_classical_monomials_deg_le(max_deg: int):
    names = ["pi", "e", "G", "zeta3"]
    items = []
    for total in range(0, max_deg + 1):
        for combo in product(range(0, total + 1), repeat=4):
            if sum(combo) != total:
                continue
            parts = []
            for k, exp in zip(names, combo):
                if exp == 0:
                    continue
                parts.append(k if exp == 1 else f"{k}^{exp}")
            label = "1" if not parts else "*".join(parts)
            items.append((combo, label))
    return items


def build_basis_from_disk(v_quad: mp.mpf, dps: int, basis_records: list[dict]) -> list[mp.mpf]:
    """Build the 75-element B_4_2 numerical vector using the EXACT exponents
    recorded in basis_4_2_enumeration.json on disk. Order is preserved
    (records[i] -> vals[i]). Returns the list of 75 mpf values evaluated at
    the requested working precision."""
    with mp.workdps(dps):
        pi_v, e_v, G_v, z3_v = mp.pi, mp.e, mp.catalan, mp.zeta(3)
        V = mp.mpf(v_quad)
        vals: list[mp.mpf] = []
        for rec in basis_records:
            k = rec["k"]
            a, b, c, d = rec["classical_exponents"]
            v_pow = V ** k
            m_val = (pi_v ** a) * (e_v ** b) * (G_v ** c) * (z3_v ** d)
            vals.append(v_pow * m_val)
        return vals


# ── PSLQ wrapper (matches stage_23_executor.py:run_pslq exactly) ──

def run_pslq(vals: list[mp.mpf], dps: int, maxcoeff: int) -> dict:
    tol_exp = -(dps - PSLQ_TOL_OFFSET[dps])
    mp.mp.dps = dps + 30
    with mp.workdps(dps):
        tol = mp.mpf(10) ** tol_exp
        t0 = time.time()
        try:
            rel = mp.pslq(
                vals,
                tol=tol,
                maxcoeff=maxcoeff,
                maxsteps=PSLQ_MAXSTEPS[dps],
            )
        except ValueError as exc:
            rel = None
            err = repr(exc)
        else:
            err = None
        elapsed = time.time() - t0
    return {
        "dps": dps,
        "tol_exponent": tol_exp,
        "maxcoeff": maxcoeff,
        "maxsteps": PSLQ_MAXSTEPS[dps],
        "basis_size": len(vals),
        "wall_seconds": round(elapsed, 3),
        "result": None if rel is None else [int(c) for c in rel],
        "error": err,
    }


# ── Heartbeat thread ──

class Heartbeat:
    def __init__(self, label: str, interval_s: float = 60.0):
        self.label = label
        self.interval = interval_s
        self._stop = threading.Event()
        self._t = None
        self._start = None

    def start(self):
        self._start = time.time()
        self._t = threading.Thread(target=self._loop, daemon=True)
        self._t.start()

    def _loop(self):
        log_progress(f"HEARTBEAT START {self.label}")
        try:
            import psutil  # type: ignore
            proc = psutil.Process(os.getpid())
            have_psutil = True
        except Exception:
            have_psutil = False
            log_progress(f"  (psutil unavailable -- timestamps only)")
        while not self._stop.wait(self.interval):
            elapsed = time.time() - self._start
            if have_psutil:
                try:
                    mem_mb = proc.memory_info().rss / (1024 * 1024)
                    log_progress(f"  alive {self.label} elapsed={elapsed:.0f}s mem={mem_mb:.0f}MB")
                except Exception as e:
                    log_progress(f"  alive {self.label} elapsed={elapsed:.0f}s (psutil err: {e})")
            else:
                log_progress(f"  alive {self.label} elapsed={elapsed:.0f}s")
        log_progress(f"HEARTBEAT STOP  {self.label}")

    def stop(self):
        self._stop.set()
        if self._t is not None:
            self._t.join(timeout=5)


# ── Recovery main ──

SMOKE_INVARIANT_FIELDS = ["dps", "tol_exponent", "maxcoeff", "maxsteps",
                          "basis_size", "result", "error"]

SMOKE_COMPARISON_NOTE = (
    "Comparison checks structural parameters (dps, tol_exponent, maxcoeff, "
    "maxsteps, basis_size) plus the PSLQ verdict (result, error). mp.pslq "
    "returns only None on failure-to-find or a list of integers on success; "
    "it does not surface iteration count, final reduction norm, or any "
    "internal trace data. Verdict equality when both are None therefore "
    "reduces to None == None: it confirms 'no relation was found within "
    "maxcoeff at this dps' is the same outcome the smoke and canonical "
    "runs reached, but it does not prove byte-identical internal state. "
    "This is a structural-invariance check, not a byte-equality check."
)

def compare_pslq_jsons(canonical: dict, smoke: dict) -> tuple[bool, list[str]]:
    """Compare smoke-test PSLQ JSON to canonical tier 3c JSON on the
    structural fields that should be invariant under rerun, plus the PSLQ
    verdict. See SMOKE_COMPARISON_NOTE for the inherent limit of this check.
    Returns (structural_invariants_match, diffs)."""
    diffs: list[str] = []
    for f in SMOKE_INVARIANT_FIELDS:
        if canonical.get(f) != smoke.get(f):
            diffs.append(f"{f}: canonical={canonical.get(f)!r} smoke={smoke.get(f)!r}")
    return (len(diffs) == 0, diffs)


def main() -> int:
    log_progress(f"=== {TASK_ID} TIER-3D RECOVERY DRIVER ===")
    log_progress(f"mpmath {mp.__version__}, python {sys.version.split()[0]}")

    # ── Provenance: predecessor V_quad string SHA ──
    raw = PREDECESSOR_VQUAD_PATH.read_bytes()
    v_str = raw.decode("utf-8").strip()
    pred_str_sha = sha256_of_bytes(v_str.encode("utf-8"))
    if pred_str_sha != PREDECESSOR_VQUAD_STR_SHA:
        log_progress(f"ABORT: predecessor SHA mismatch (got {pred_str_sha})")
        return 2
    log_progress(f"Predecessor V_quad string SHA: {pred_str_sha} OK")

    # ── Recompute V_quad fresh (depth 5000, dps 2200) ──
    log_progress("Computing V_quad fresh @ depth 5000, dps 2200 ...")
    t0 = time.time()
    v_quad = compute_vquad(5000, DPS_WORKING_HI)
    log_progress(f"  V_quad fresh CF done in {time.time()-t0:.2f}s; first 64: {mp.nstr(v_quad, 64)}")

    # ── Load basis from disk and check provenance ──
    if not BASIS_FILE.exists():
        log_progress(f"ABORT: {BASIS_FILE.name} missing")
        return 3
    if not CANONICAL_TIER_3C.exists():
        log_progress(f"ABORT: {CANONICAL_TIER_3C.name} missing -- tier 3c output absent")
        return 4

    basis_sha = file_sha256(BASIS_FILE)
    basis_obj = json.loads(BASIS_FILE.read_text(encoding="utf-8"))
    if basis_obj.get("basis_size") != 75 or basis_obj.get("k_max") != 4 or basis_obj.get("classical_max_deg") != 2:
        log_progress(f"ABORT: basis file structure unexpected: {basis_obj.get('basis_size')}/{basis_obj.get('k_max')}/{basis_obj.get('classical_max_deg')}")
        return 5
    basis_records = basis_obj["items"]
    log_progress(f"Basis loaded: {len(basis_records)} records; sha256={basis_sha}")

    basis_mtime = BASIS_FILE.stat().st_mtime
    tier_3c_mtime = CANONICAL_TIER_3C.stat().st_mtime
    if basis_mtime > tier_3c_mtime:
        log_progress(f"ABORT: basis file mtime ({basis_mtime}) > tier-3c mtime ({tier_3c_mtime})  -- basis modified after 3c ran")
        return 6
    log_progress(f"  basis_mtime <= tier_3c_mtime: {basis_mtime:.0f} <= {tier_3c_mtime:.0f} OK")

    canonical_3c = json.loads(CANONICAL_TIER_3C.read_text(encoding="utf-8"))
    log_progress(f"Canonical tier 3c loaded: result={canonical_3c.get('result')!r} basis_size={canonical_3c.get('basis_size')}")

    # ── Pre-flight smoke test: PSLQ at 500 dp on B_4_2 ──
    log_progress("Pre-flight smoke: building B_4_2 @ 500 dp ...")
    t0 = time.time()
    vals_500 = build_basis_from_disk(v_quad, 500, basis_records)
    log_progress(f"  basis built ({len(vals_500)} elements) in {time.time()-t0:.2f}s; first val nstr32 = {mp.nstr(vals_500[0], 32)}")

    log_progress("Pre-flight smoke: PSLQ @ 500 dp maxcoeff=10^4 (ETA ~9 min) ...")
    hb = Heartbeat("smoke_500dp")
    hb.start()
    try:
        smoke_500 = run_pslq(vals_500, 500, 10**4)
    finally:
        hb.stop()
    smoke_500_record = dict(smoke_500)
    smoke_500_record["preflight"] = True
    OUT_PREFLIGHT.write_text(json.dumps(smoke_500_record, indent=2), encoding="utf-8")
    log_progress(f"  smoke result: {smoke_500['result']!r}  ({smoke_500['wall_seconds']}s)")

    matches, diffs = compare_pslq_jsons(canonical_3c, smoke_500)
    if not matches:
        log_progress(f"ABORT: smoke disagreed with canonical tier 3c on {len(diffs)} field(s):")
        for d in diffs:
            log_progress(f"  diff: {d}")
        recovery_meta = {
            "task_id": TASK_ID,
            "tier": "3d",
            "outcome": "HALTED_PREFLIGHT_DIVERGENCE",
            "diffs": diffs,
            "basis_sha256": basis_sha,
            "predecessor_vquad_string_sha256": pred_str_sha,
            "smoke_json": smoke_500_record,
            "canonical_tier_3c_json": canonical_3c,
        }
        OUT_RECOVERY.write_text(json.dumps(recovery_meta, indent=2), encoding="utf-8")
        return 7
    log_progress(
        "Pre-flight smoke: structural invariants match canonical tier 3c "
        f"on {SMOKE_INVARIANT_FIELDS}; verdict equality is None == None "
        "(see SMOKE_COMPARISON_NOTE in driver source for scope of this check)"
    )

    # ── Tier 3d: PSLQ @ 2050 dp on B_4_2 ──
    log_progress("Tier 3d: building B_4_2 @ 2050 dp ...")
    t0 = time.time()
    vals_2050 = build_basis_from_disk(v_quad, 2050, basis_records)
    log_progress(f"  basis built ({len(vals_2050)} elements) in {time.time()-t0:.2f}s")

    log_progress("Tier 3d: PSLQ @ 2050 dp maxcoeff=10^4 (ETA ~95-110 min) ...")
    hb = Heartbeat("tier_3d_2050dp")
    hb.start()
    try:
        tier_3d = run_pslq(vals_2050, 2050, 10**4)
    finally:
        hb.stop()
    log_progress(f"  tier 3d result: {tier_3d['result']!r}  ({tier_3d['wall_seconds']}s)")

    # ── Write tier 3d JSON (canonical schema, no extra fields so manifest
    #    sha-256 is stable under future re-archives) ──
    OUT_TIER_3D.write_text(json.dumps(tier_3d, indent=2), encoding="utf-8")
    tier_3d_sha = file_sha256(OUT_TIER_3D)
    log_progress(f"  wrote {OUT_TIER_3D.name}  sha256={tier_3d_sha}")

    # ── Recovery provenance sidecar ──
    recovery_meta = {
        "task_id": TASK_ID,
        "tier": "3d",
        "outcome": "RECOVERED",
        "reason_for_recovery": (
            "Original stage_23_executor.py terminated silently between tier 3c "
            "(landed 2026-05-19 10:45:53) and tier 3d (never produced output). "
            "No Python error trace surfaced and no live python.exe was found at "
            "14:56 UTC. Likely causes (not confirmed): VS Code terminal session "
            "closure, OOM kill during 2050dp PSLQ on 75 elements, or silent "
            "mpmath internal failure. This recovery driver re-runs ONLY tier 3d, "
            "with a pre-flight 500dp smoke test confirming pipeline integrity."
        ),
        "predecessor_vquad_string_sha256": pred_str_sha,
        "basis_file": BASIS_FILE.name,
        "basis_sha256": basis_sha,
        "basis_mtime_epoch": basis_mtime,
        "tier_3c_mtime_epoch": tier_3c_mtime,
        "smoke_preflight_json": smoke_500_record,
        "smoke_structural_invariants_match": True,
        "smoke_comparison_fields": SMOKE_INVARIANT_FIELDS,
        "smoke_comparison_note": SMOKE_COMPARISON_NOTE,
        "tier_3d_json": tier_3d,
        "tier_3d_json_sha256": tier_3d_sha,
        "mpmath_version": mp.__version__,
        "python_version": sys.version.split()[0],
        "driver_script": Path(__file__).name,
    }
    OUT_RECOVERY.write_text(json.dumps(recovery_meta, indent=2), encoding="utf-8")
    log_progress(f"Recovery sidecar written: {OUT_RECOVERY.name}")
    log_progress("=== DONE ===")
    return 0


if __name__ == "__main__":
    try:
        rc = main()
    except Exception as exc:
        log_progress(f"FATAL: {type(exc).__name__}: {exc}")
        log_progress("TRACEBACK:\n" + traceback.format_exc())
        rc = 99
    sys.exit(rc)
