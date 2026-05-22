"""_refire_discovery.py — Hardened PSLQ discovery for M2-REFIRE.

Runs mpmath.pslq at a single SUFFICIENT dps against the M1-certified
ball midpoints. Redirects verbose stdout to a log file (line-buffered)
so the iteration counter K is checkpointed on disk continuously: even
if the process is killed mid-run, the last K reached is recoverable.

USAGE
-----
    python _refire_discovery.py --dps 8640  --P-bits 28712 --tag 8640@28712
    python _refire_discovery.py --dps 28712 --P-bits 28712 --tag 28712@28712

INVARIANTS (work order STEP 1)
------------------------------
- dps MUST be in {8640, 28712}. dps=2160 is BANNED (known spurious regime).
- Input vector is the M1 certified ball MIDPOINT (NOT mpmath.khinchin).
- maxsteps generously large (do not let mpmath hit a step cap).
- Any maxsteps-hit or exception => terminal_state=ERROR (not a result).

OUTPUTS
-------
- _refire_checkpoint_{tag}.log   (line-buffered verbose stdout from pslq)
- _refire_checkpoint_{tag}.json  (final checkpoint: K, relation, terminal state)
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import mpmath
from mpmath import mp, pslq
from flint import arb, ctx

sys.set_int_max_str_digits(1_000_000)

HERE = Path(__file__).parent
M1_OUTPUTS = HERE / "M1_outputs"

M1_BALL_SHA256 = {
    28712: "4729ea6cc4c2d433cbcb44c6f210ba82e22d77f51753c86aedce9562449a1ccf",
    14356: "378407d760627fd1dab5f3493d8e29037c63d76a4f92a066736b43238af03f54",
}

ALLOWED_DPS = (8640, 28712)
N_BASIS = 15
MAXCOEFF_EXP = 70
MAXSTEPS = 250_000  # generously above prior empirical K~29363

BASIS_LABELS = (
    "1", "K_0", "K_0^2", "K_0^3", "K_0^4", "K_0^5", "K_0^6",
    "log(K_0)",
    "K_0*pi", "K_0*e", "K_0*ln2", "K_0*gamma", "K_0*zeta(2)", "K_0*zeta(3)", "K_0*G",
)


_VERBOSE_ITER_LINE = re.compile(r"^\s*(\d+)/(\d+):\s+Error:\s+\S+\s+Norm:\s+(\d+)")
_VERBOSE_CANCEL_LINE = re.compile(r"^CANCELLING after step (\d+)/(\d+)")
_VERBOSE_FOUND_LINE = re.compile(r"^FOUND relation at iter (\d+)")
_VERBOSE_NORM_BOUND_LINE = re.compile(r"Norm bound:\s+(-?\d+)")


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 16), b""):
            h.update(blk)
    return h.hexdigest()


def load_m1_balls(P_bits: int):
    path = M1_OUTPUTS / f"balls_P{P_bits}.json"
    actual = file_sha256(path)
    expected = M1_BALL_SHA256[P_bits]
    if actual != expected:
        raise RuntimeError(
            f"M1 ball SHA mismatch at P={P_bits}: expected {expected}, got {actual}"
        )
    with open(path) as f:
        return json.load(f), actual


def arb_to_mpf_midpoint(a: arb, dps: int):
    s = a.str(dps + 5)
    if "+/-" in s:
        s = s.split(" +/-")[0]
    s = s.lstrip("[").rstrip("]").strip()
    return mp.mpf(s)


def reload_balls_as_arb(balls_json):
    saved_prec = ctx.prec
    try:
        # Use the M1 intrinsic precision for the reload to preserve full radius.
        ctx.prec = 32768
        arbs = []
        for entry in balls_json["basis"]:
            a = arb(entry["arb_repr"])
            arbs.append((entry["index"], entry["label"], a))
        if [t[1] for t in arbs] != list(BASIS_LABELS):
            raise RuntimeError("Label order mismatch in M1 balls")
        return [t[2] for t in arbs]
    finally:
        ctx.prec = saved_prec


def parse_log_for_terminal_state(log_path: Path, returned_relation):
    last_iter = -1
    last_norm = 0
    found_iter = None
    cancel_iter = None
    cancel_max = None
    norm_bound_value = None
    n_lines = 0
    with open(log_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            n_lines += 1
            m = _VERBOSE_ITER_LINE.match(line)
            if m:
                last_iter = int(m.group(1))
                last_norm = int(m.group(3))
                continue
            mc = _VERBOSE_CANCEL_LINE.match(line)
            if mc:
                cancel_iter = int(mc.group(1))
                cancel_max = int(mc.group(2))
                continue
            mf = _VERBOSE_FOUND_LINE.match(line)
            if mf:
                found_iter = int(mf.group(1))
                continue
            mnb = _VERBOSE_NORM_BOUND_LINE.search(line)
            if mnb:
                norm_bound_value = int(mnb.group(1))
                if norm_bound_value >= 0:
                    last_norm = norm_bound_value

    if returned_relation is not None and found_iter is not None:
        K = found_iter + 1
        terminal_state = "RELATION_CANDIDATE"
    elif cancel_iter is not None:
        K = cancel_iter + 1
        if cancel_max is not None and K >= cancel_max:
            terminal_state = "MAXSTEPS_HIT"
        else:
            terminal_state = "CONVERGED_NULL"
    elif last_iter < 0:
        K = 0
        terminal_state = "NO_OUTPUT"
    else:
        K = last_iter + 1
        terminal_state = "INDETERMINATE"

    return {
        "K": K,
        "last_iter_parsed": last_iter,
        "last_norm_for_comparison_only": last_norm,
        "found_iter": found_iter,
        "cancel_iter": cancel_iter,
        "cancel_max": cancel_max,
        "norm_bound_value_for_comparison_only": norm_bound_value,
        "verbose_lines": n_lines,
        "terminal_state": terminal_state,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dps", type=int, required=True)
    ap.add_argument("--P-bits", type=int, required=True,
                    choices=list(M1_BALL_SHA256.keys()))
    ap.add_argument("--tag", type=str, required=True,
                    help="checkpoint tag, e.g. 8640@28712")
    args = ap.parse_args()

    if args.dps not in ALLOWED_DPS:
        raise SystemExit(
            f"dps={args.dps} is NOT in the allowed set {ALLOWED_DPS}. "
            f"dps=2160 is BANNED for M2-REFIRE."
        )

    log_path = HERE / f"_refire_checkpoint_{args.tag}.log"
    ckpt_path = HERE / f"_refire_checkpoint_{args.tag}.json"

    # STEP 0b: SHA-check M1 ball.
    balls_json, ball_sha = load_m1_balls(args.P_bits)

    # Reload as Arb (for the midpoint extraction).
    arb_basis = reload_balls_as_arb(balls_json)

    # Prepare basis mpfs at the run dps from M1 ball midpoints.
    saved_dps = mp.dps
    try:
        mp.dps = args.dps
        basis_mpf = [arb_to_mpf_midpoint(a, args.dps) for a in arb_basis]

        # Write a header to the log so the run is self-describing.
        # Use unbuffered file with line buffering for crash safety.
        with open(log_path, "w", encoding="utf-8", buffering=1) as logf:
            logf.write(f"# M2-REFIRE discovery checkpoint log\n")
            logf.write(f"# tag={args.tag}\n")
            logf.write(f"# dps={args.dps}\n")
            logf.write(f"# P_bits={args.P_bits}\n")
            logf.write(f"# M1_ball_sha256={ball_sha}\n")
            logf.write(f"# maxsteps={MAXSTEPS}\n")
            logf.write(f"# maxcoeff_exp={MAXCOEFF_EXP}\n")
            logf.write(f"# input_source=M1_certified_ball_midpoint\n")
            logf.write(f"# N_basis={N_BASIS}\n")
            logf.write(f"# starting_at_unix={time.time():.3f}\n")
            logf.flush()

            t0 = time.perf_counter()
            relation = None
            exc_info = None
            interrupted = False
            try:
                with contextlib.redirect_stdout(logf):
                    relation = pslq(
                        basis_mpf,
                        maxcoeff=10 ** MAXCOEFF_EXP,
                        maxsteps=MAXSTEPS,
                        verbose=True,
                    )
            except KeyboardInterrupt:
                interrupted = True
                exc_info = {"type": "KeyboardInterrupt",
                            "msg": "external interrupt (Ctrl-C, terminal reset, or signal); PSLQ did NOT reach a natural terminal state"}
            except Exception as exc:
                exc_info = {"type": type(exc).__name__, "msg": str(exc)}
            except BaseException as exc:
                # Catch SystemExit and other BaseException subclasses too.
                exc_info = {"type": type(exc).__name__, "msg": str(exc), "base_exception": True}
            elapsed = time.perf_counter() - t0

            logf.write(f"# returned_relation={relation is not None}\n")
            logf.write(f"# interrupted={interrupted}\n")
            if exc_info:
                logf.write(f"# exception={exc_info}\n")
            logf.write(f"# elapsed_s={elapsed:.3f}\n")
            logf.write(f"# done_at_unix={time.time():.3f}\n")
            logf.flush()
    finally:
        mp.dps = saved_dps

    # Parse the log to recover terminal state.
    parsed = parse_log_for_terminal_state(log_path, relation)

    ckpt = {
        "tag": args.tag,
        "dps": args.dps,
        "P_bits": args.P_bits,
        "M1_ball_sha256": ball_sha,
        "input_source": "M1_certified_ball_midpoint",
        "maxsteps": MAXSTEPS,
        "maxcoeff_exp": MAXCOEFF_EXP,
        "n_basis": N_BASIS,
        "elapsed_s": elapsed,
        "exception": exc_info,
        "relation": list(relation) if relation else None,
        "log_path": str(log_path),
        **parsed,
    }

    with open(ckpt_path, "w", encoding="utf-8") as f:
        json.dump(ckpt, f, indent=2)

    print(json.dumps({
        "tag": args.tag,
        "dps": args.dps,
        "elapsed_s": elapsed,
        "terminal_state": parsed["terminal_state"],
        "K": parsed["K"],
        "has_candidate_relation": relation is not None,
        "candidate_relation_l2_norm_approx": (
            float(sum(int(x)**2 for x in relation)) ** 0.5
            if relation is not None else None
        ),
        "ckpt_path": str(ckpt_path),
        "log_path": str(log_path),
    }, indent=2))


if __name__ == "__main__":
    main()
