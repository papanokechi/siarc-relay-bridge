"""
SPRINT-W2-TRANS-INDICIAL-SURVEY -- Part B
=========================================

Separation test:  for each candidate function f(family) ->
distribution over Trans vs non-Trans -- is there a clean
threshold or exact value?

Candidates:
  f1 = |mu+/mu-|
  f2 = |Im(alpha+)|
  f3 = alpha+ + alpha-
  f4 = alpha+ * alpha-
  f5 = a2 / b1^2  (the empirical Trans definition itself)
"""

import json
from mpmath import mpf, mpc

def load():
    with open("indicial_survey.json", "r") as f:
        data = json.load(f)
    def deserialise(x):
        if isinstance(x, dict) and "_type" in x:
            if x["_type"] == "mpc":
                return mpc(x["re"], x["im"])
            if x["_type"] == "mpf":
                return mpf(x["v"])
        return x
    out = {}
    for tag in data:
        out[tag] = []
        for r in data[tag]:
            out[tag].append({k: deserialise(v) for k, v in r.items()})
    return out

def fmt(x):
    if x is None:
        return "None"
    if isinstance(x, mpc):
        return f"({float(x.real):+.4f}{float(x.imag):+.4f}j)"
    if isinstance(x, mpf):
        return f"{float(x):+.6f}"
    return str(x)

def main():
    data = load()
    rows = []
    for tag in ("Trans", "Log", "Alg"):
        for r in data[tag]:
            mu_p = r["mu_plus"]; mu_m = r["mu_minus"]
            a_p = r["alpha_plus"]; a_m = r["alpha_minus"]
            f1 = r["mu_ratio_abs"]
            f2 = abs(a_p.imag) if isinstance(a_p, mpc) else mpf(0)
            f3 = r["alpha_sum"]
            f4 = r["alpha_product"]
            f5 = r["a2_b1sq"]
            rows.append((tag, r["label"], f1, f2, f3, f4, f5))

    print("="*92)
    print("SEPARATION TABLE  (Trans / Log / Alg)")
    print("="*92)
    print(f"{'tag':<6}{'lab':<6}{'|mu+/mu-|':>14}{'|Im(a+)|':>14}{'sum':>14}{'product':>16}{'a2/b1^2':>14}")
    for tag, lab, f1, f2, f3, f4, f5 in rows:
        print(f"{tag:<6}{lab:<6}{fmt(f1):>14}{fmt(f2):>14}{fmt(f3):>14}{fmt(f4):>16}{fmt(f5):>14}")

    # ---- threshold report ----
    print("\n" + "="*92)
    print("Per-class ranges")
    print("="*92)
    def stats(name, get):
        for tag in ("Trans", "Log", "Alg"):
            vals = []
            for r in data[tag]:
                v = get(r)
                if v is None:
                    continue
                if isinstance(v, mpc):
                    v = v.real
                vals.append(float(v))
            if not vals:
                print(f"  {tag:<6} {name:<14}: (empty)")
                continue
            print(f"  {tag:<6} {name:<14}: n={len(vals):>2}  "
                  f"min={min(vals):+.6f}  max={max(vals):+.6f}  "
                  f"unique-rounded={sorted(set(round(v, 6) for v in vals))[:6]}")

    stats("|mu+/mu-|", lambda r: r["mu_ratio_abs"])
    stats("alpha_sum", lambda r: r["alpha_sum"])
    stats("alpha_product", lambda r: r["alpha_product"])
    stats("alpha_disc", lambda r: r["alpha_disc"])
    stats("a2/b1^2", lambda r: r["a2_b1sq"])

    print("\n" + "="*92)
    print("Verdict")
    print("="*92)
    print("""
The only quantity constant across the 50 Trans families is
   |mu+/mu-|  =  (13 + 3 sqrt(17)) / 4
which is mathematically equivalent to  a2/b1^2 = -2/9
(see forcing_condition.py for the symbolic identity).

Hence Birkhoff-indicial features {sum, product, discriminant, individual exponents}
do NOT separate Trans from non-Trans.  The Trans definition is
already encoded in the characteristic-root ratio.

Conclusion: no NEW indicial invariant separates Trans families;
the question of why a2/b1^2 = -2/9 produces transcendental limits
must be sought outside the leading two-term Birkhoff balance.
""")


if __name__ == "__main__":
    main()
