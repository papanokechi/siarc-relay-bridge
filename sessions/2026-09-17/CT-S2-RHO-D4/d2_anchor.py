import json
import s_exponent as S
from mpmath import mpf, nstr

d = json.load(open("s_table.json"))
print("label                        signchg r_inf_digits r_inf_nonzero")
for r in d["representatives"]:
    dig = str(r["r_inf_halfN_vs_N_agreement_digits"])[:8]
    print("{:28s} {:>5} {:>10} {}".format(
        r["label"], r["b_sign_changes"], dig, r["r_inf_nonzero"]))

print()
# d = 2 anchor: V_quad b(n) = 3n^2 + n + 1 -> beta low->high [1, 1, 3]
r = S.analyse("V_quad_d2", [1, 1, 3])
print("V_quad d=2  s_measured :", r["s_measured"])
print("            s_predicted:", r["s_predicted"])
print("            residual   :", r["residual"])
print("            r_inf      :", r["r_inf"])
print("            signchg    :", r["b_sign_changes"])
rho = -mpf(r["s_measured"]) - 1
print("  rho_d = -s-1        =", nstr(rho, 25))
print("  stored rho (CC-G)   = -1.833333333333333333333333333333")
print("  |diff|              =", nstr(abs(rho - mpf("-1.8333333333333333333333333333333333")), 6))
json.dump(r, open("d2_anchor.json", "w"), indent=2)
