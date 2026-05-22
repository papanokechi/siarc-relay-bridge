"""Parse an existing _refire_checkpoint_*.log file and emit a PARTIAL
JSON checkpoint, for use after an external interrupt (KeyboardInterrupt,
terminal reset, etc.) where the discovery script did not reach its
normal checkpoint-write codepath.

This is a SALVAGE tool — it does NOT certify the run as complete.
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

sys.set_int_max_str_digits(1_000_000)

HERE = Path(__file__).parent

_VERBOSE_ITER_LINE = re.compile(r"^\s*(\d+)/(\d+):\s+Error:\s+(\S+)\s+Norm:\s+(\d+)")
_VERBOSE_CANCEL_LINE = re.compile(r"^CANCELLING after step (\d+)/(\d+)")
_VERBOSE_FOUND_LINE = re.compile(r"^FOUND relation at iter (\d+)")
_HEADER_LINE = re.compile(r"^#\s*(\w+)=(.+)$")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--interrupt-cause", required=True,
                    help="why the run did NOT complete (e.g. 'KeyboardInterrupt at iter 3229')")
    args = ap.parse_args()

    log_path = HERE / f"_refire_checkpoint_{args.tag}.log"
    ckpt_path = HERE / f"_refire_checkpoint_{args.tag}.json"

    if not log_path.exists():
        raise SystemExit(f"log {log_path} not found")

    header = {}
    last_iter = -1
    last_max = -1
    last_norm = 0
    last_err = None
    found_iter = None
    cancel_iter = None
    n_lines = 0
    iter_count = 0

    with open(log_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            n_lines += 1
            mh = _HEADER_LINE.match(line)
            if mh:
                header[mh.group(1)] = mh.group(2).strip()
                continue
            m = _VERBOSE_ITER_LINE.match(line)
            if m:
                last_iter = int(m.group(1))
                last_max = int(m.group(2))
                last_err = m.group(3)
                last_norm = int(m.group(4))
                iter_count += 1
                continue
            mf = _VERBOSE_FOUND_LINE.match(line)
            if mf:
                found_iter = int(mf.group(1))
                continue
            mc = _VERBOSE_CANCEL_LINE.match(line)
            if mc:
                cancel_iter = int(mc.group(1))
                continue

    K = last_iter + 1 if last_iter >= 0 else 0

    ckpt = {
        "tag": args.tag,
        "status": "INTERRUPTED_PARTIAL",
        "interrupt_cause": args.interrupt_cause,
        "header": header,
        "dps": int(header.get("dps", -1)),
        "P_bits": int(header.get("P_bits", -1)),
        "M1_ball_sha256": header.get("M1_ball_sha256", "unknown"),
        "maxsteps": int(header.get("maxsteps", -1)),
        "maxcoeff_exp": int(header.get("maxcoeff_exp", -1)),
        "input_source": header.get("input_source", "unknown"),
        "K": K,
        "last_iter_parsed": last_iter,
        "iter_count_in_log": iter_count,
        "last_norm_for_comparison_only": last_norm,
        "last_error_str": last_err,
        "found_iter": found_iter,
        "cancel_iter": cancel_iter,
        "terminal_state": "INTERRUPTED_PARTIAL",
        "log_lines": n_lines,
        "log_path": str(log_path),
        "salvage_note": (
            "This checkpoint is a PARTIAL salvage parsed from the verbose log "
            "after an external interrupt; the PSLQ search did NOT reach a "
            "natural terminal state. K is the last iteration counter seen in "
            "the log. terminal_state=INTERRUPTED_PARTIAL is NOT a result; "
            "it does NOT satisfy the M2-REFIRE K-stability gate. "
            "Deposit this with the partial-halt verdict in halt_log."
        ),
    }

    with open(ckpt_path, "w", encoding="utf-8") as f:
        json.dump(ckpt, f, indent=2)

    print(json.dumps({
        "tag": args.tag,
        "wrote": str(ckpt_path),
        "K_last_seen": K,
        "iter_count_in_log": iter_count,
        "terminal_state": "INTERRUPTED_PARTIAL",
        "log_lines": n_lines,
    }, indent=2))


if __name__ == "__main__":
    main()
