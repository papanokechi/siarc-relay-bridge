import sympy as sp

x = sp.symbols("x")
lam = sp.symbols("lambda")


def indicial_data(chi, c, s):
    p = sp.diff(chi, x) / chi
    q = c / chi
    p0 = sp.limit((x - s) * p, x, s)
    q0 = sp.limit((x - s) ** 2 * q, x, s)
    indicial = sp.expand(lam * (lam - 1) + p0 * lam + q0)
    return p0, q0, indicial


def operator(chi, c, y):
    return sp.simplify(chi * sp.diff(y, x, 2) + sp.diff(chi, x) * sp.diff(y, x) + c * y)


examples = [
    {
        "name": "E1: chi=x, c=0, s=0",
        "chi": x,
        "c": sp.Integer(0),
        "s": sp.Integer(0),
        "y1": sp.Integer(1),
        "y2": sp.log(x),
        "expected_log": "elementary second solution log(x)",
    },
    {
        "name": "E2: chi=x, c=x, s=0 (c(s)=0, q analytic)",
        "chi": x,
        "c": x,
        "s": sp.Integer(0),
        "y1": sp.besselj(0, x),
        "y2": sp.bessely(0, x),
        "expected_log": "BesselY(0,x) has a logarithmic term",
    },
    {
        "name": "E3: chi=x, c=1, s=0 (c(s)!=0)",
        "chi": x,
        "c": sp.Integer(1),
        "s": sp.Integer(0),
        "y1": sp.besselj(0, 2 * sp.sqrt(x)),
        "y2": None,
        "expected_log": "reduction-of-order integrand has nonzero residue",
    },
]

for ex in examples:
    chi, c, s, y1, y2 = ex["chi"], ex["c"], ex["s"], ex["y1"], ex["y2"]
    p0, q0, indicial = indicial_data(chi, c, s)
    residue = sp.limit((x - s) / (chi * y1**2), x, s)
    print(ex["name"])
    print(f"  p0 = {p0}")
    print(f"  q0 = {q0}")
    print(f"  indicial = {indicial}")
    print(f"  L[y1] = {operator(chi, c, y1)}")
    print(f"  residue of 1/(chi*y1^2) at s = {residue}")
    print(f"  log check = {ex['expected_log']}")
    if y2 is not None:
        print(f"  L[y2] = {operator(chi, c, y2)}")
    if ex["name"].startswith("E2"):
        print(f"  series(Y0) = {sp.series(y2, x, 0, 3)}")
    print()
