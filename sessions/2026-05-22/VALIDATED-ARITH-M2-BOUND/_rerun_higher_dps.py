"""Re-run mpmath.pslq at higher dps to escape the dps=2160 spurious termination.

For each rung, try dps = 4320 first; if mpmath still returns a relation that
fails M1 Arb verification, escalate to dps = 8640.
"""
from __future__ import annotations
import sys, json, time, contextlib, io, re
sys.set_int_max_str_digits(1_000_000)
from mpmath import mp, pslq
from flint import arb, ctx
from pathlib import Path

HERE = Path(__file__).parent

VERBOSE_ITER_RE = re.compile(r"^\s*(\d+)/(\d+):\s+Error:\s+\S+\s+Norm:\s+(\d+)")
CANCEL_RE = re.compile(r"^CANCELLING after step (\d+)/(\d+)")
FOUND_RE = re.compile(r"^FOUND relation at iter (\d+)")
NORM_BOUND_RE = re.compile(r"Norm bound:\s+(-?\d+)")


def arb_to_mpf_midpoint(a, dps):
    s = a.str(dps + 5)
    if "+/-" in s:
        s = s.split(" +/-")[0]
    s = s.lstrip("[").rstrip("]").strip()
    return mp.mpf(s)


def run_pslq(arb_basis, dps, maxcoeff_exp=70, maxsteps=100_000):
    saved = mp.dps
    try:
        mp.dps = dps
        basis_mpf = [arb_to_mpf_midpoint(a, dps) for a in arb_basis]
        buf = io.StringIO()
        t0 = time.perf_counter()
        try:
            with contextlib.redirect_stdout(buf):
                relation = pslq(basis_mpf, maxcoeff=10 ** maxcoeff_exp,
                                maxsteps=maxsteps, verbose=True)
        except Exception as exc:
            elapsed = time.perf_counter() - t0
            return {
                "relation": None, "K": -1, "error": str(exc),
                "elapsed_s": elapsed, "termination_reason": "exception",
            }
        elapsed = time.perf_counter() - t0
    finally:
        mp.dps = saved

    log_text = buf.getvalue()
    last_iter = -1
    last_norm = 0
    cancel_iter = None
    found_iter = None
    for line in log_text.splitlines():
        m = VERBOSE_ITER_RE.match(line)
        if m:
            last_iter = int(m.group(1))
            last_norm = int(m.group(3))
            continue
        mc = CANCEL_RE.match(line)
        if mc:
            cancel_iter = int(mc.group(1))
            continue
        mf = FOUND_RE.match(line)
        if mf:
            found_iter = int(mf.group(1))

    if relation is not None and found_iter is not None:
        K = found_iter + 1
        termination_reason = "relation_found"
    elif cancel_iter is not None:
        K = cancel_iter + 1
        termination_reason = "maxsteps_or_norm_break"
    else:
        K = last_iter + 1 if last_iter >= 0 else 0
        termination_reason = "indeterminate"

    return {
        "relation": list(relation) if relation else None,
        "K": K,
        "last_norm_seen": last_norm,
        "termination_reason": termination_reason,
        "elapsed_s": elapsed,
        "verbose_chars": len(log_text),
    }


def verify_candidate(arb_basis, candidate, verify_prec_bits=32768):
    """Verify whether a candidate integer relation is consistent with M1 balls."""
    saved = ctx.prec
    try:
        ctx.prec = verify_prec_bits
        S = arb(0)
        for m, x in zip(candidate, arb_basis):
            S = S + arb(m) * x
        contains_zero = S.contains(arb(0))
        # Propagated uncertainty (informational)
        prop_unc = arb(0)
        for m, x in zip(candidate, arb_basis):
            prop_unc = prop_unc + arb(abs(m)) * arb(0, x.rad())
        return {
            "contains_zero": contains_zero,
            "sum_arb_str": S.str(30),
            "propagated_uncertainty": prop_unc.str(15),
        }
    finally:
        ctx.prec = saved


def main():
    ctx.prec = 1024
    # Load top rung
    with open(HERE / "M1_outputs" / "balls_P28712.json") as f:
        balls_top = json.load(f)
    xs_top = [arb(e["arb_repr"]) for e in balls_top["basis"]]

    with open(HERE / "M1_outputs" / "balls_P14356.json") as f:
        balls_mid = json.load(f)
    xs_mid = [arb(e["arb_repr"]) for e in balls_mid["basis"]]

    results = {}
    # Run dps=8640 directly on both rungs (m32a-equivalent precision).
    # If spurious, escalate to 12960. Skip dps=4320 to save budget.
    for rung_name, xs in [("top_P28712", xs_top), ("mid_P14356", xs_mid)]:
        print(f"=== {rung_name} ===")
        for dps in (8640, 12960):
            print(f"-- dps={dps} --")
            r = run_pslq(xs, dps=dps)
            print(f"  K = {r['K']}  ({r['termination_reason']})")
            print(f"  relation = {'[len=15]' if r['relation'] else 'None'}")
            print(f"  elapsed = {r['elapsed_s']:.1f}s")
            if r["relation"] is not None:
                v = verify_candidate(xs, r["relation"])
                print(f"  candidate contains_zero: {v['contains_zero']}")
                print(f"  arb sum: {v['sum_arb_str']}")
                r["verification"] = v
                if v["contains_zero"]:
                    print(f"  >> candidate VERIFIES at high prec; this would be a TRUE relation! Halt.")
                else:
                    print(f"  >> candidate REJECTED as spurious; escalate dps")
            else:
                print(f"  >> no relation reported (termination via norm cancel) — usable K")
            results[(rung_name, dps)] = r
            # Stop escalating if we got a clean cancellation OR a verified-real relation
            if r["relation"] is None or (r.get("verification", {}).get("contains_zero")):
                break
        print()

    # Write summary
    out_summary = {}
    for k, v in results.items():
        out_summary[f"{k[0]}_dps{k[1]}"] = v
    (HERE / "_pslq_higher_dps_results.json").write_text(json.dumps(out_summary, indent=2))
    print(f"Summary written to _pslq_higher_dps_results.json")


if __name__ == "__main__":
    main()
