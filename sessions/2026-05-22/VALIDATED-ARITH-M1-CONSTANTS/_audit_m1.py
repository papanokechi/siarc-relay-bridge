"""Compute SHA-256 of M1_outputs JSON files and report radius decimals for AEAL claims."""
import hashlib
import json
import math
import re
from pathlib import Path

OUT_DIR = Path("M1_outputs")


def file_sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def parse_arb_radius_log10(s: str) -> float:
    """From an arb radius string, extract approx log10 of the radius.

    The string is `str(x.rad())` where x.rad() is itself an Arb ball whose
    CENTRE is the actual radius. For tiny radii Arb prints in the form
        [LEADING_DIGITS e-EXPONENT +/- TINY e-LARGER_EXPONENT]
    For huge values (radius near 1) it may print plain decimal form.

    We need log10 of the radius itself (the mantissa-side value), which can
    underflow Python `float` for exponents below -300. Solution: parse the
    leading digits + the explicit exponent token separately.
    """
    s = s.strip()
    if s == "0":
        return -math.inf
    if s.startswith("["):
        inner = s.lstrip("[").split("+/-")[0].strip()
    else:
        inner = s
    # inner is now like "2.10560358...e-8690" (very long mantissa with explicit exponent)
    # or "0.00012..." (plain decimal) or "1.234".
    # Try to find scientific exponent token first.
    m = re.search(r"[eE]([-+]?[0-9]+)\s*$", inner)
    if m:
        exp = int(m.group(1))
        # The mantissa before 'e' contributes log10(mantissa) which is in [0,1).
        mantissa_part = inner[: m.start()].strip()
        # Just take the first significant digit to get rough log10 contribution.
        m2 = re.match(r"\s*([-+]?)([0-9]+)(?:\.([0-9]+))?", mantissa_part)
        if m2:
            int_part = m2.group(2)
            # Number of integer digits not counting leading zeros
            n_int = len(int_part.lstrip("0"))
            if n_int == 0 and m2.group(3):
                # Number is 0.0...0xxx
                frac = m2.group(3)
                leading_zeros = len(frac) - len(frac.lstrip("0"))
                return exp - leading_zeros - 1
            return exp + (n_int - 1)
        return float(exp)
    # No exponent token: plain decimal
    try:
        v = float(inner)
        if v == 0:
            return -math.inf
        return math.log10(abs(v))
    except Exception:
        return float("nan")


def main():
    print("M1_outputs file hashes:")
    for p in sorted(OUT_DIR.glob("*.json")):
        h = file_sha256(p)
        print(f"  {p.name:35s}  sha256={h}")

    print()
    print("Radius (log10) per basis entry, per precision rung:")
    for P in (7178, 14356, 28712):
        path = OUT_DIR / f"balls_P{P}.json"
        with open(path) as f:
            data = json.load(f)
        print(f"  P_bits={P}:")
        for e in data["basis"]:
            lr = parse_arb_radius_log10(e["radius_str"])
            print(f"    [{e['index']:2d}] {e['label']:12s}  log10(rad) ~= {lr:.2f}")


if __name__ == "__main__":
    main()
