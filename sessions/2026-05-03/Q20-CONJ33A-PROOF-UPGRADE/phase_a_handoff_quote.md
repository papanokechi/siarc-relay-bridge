# Phase A.1 — Quote of the Newton-polygon argument from XI0-D3-DIRECT

Source: `siarc-relay-bridge/sessions/2026-05-02/XI0-D3-DIRECT/handoff.md`
and `xi0_d3_runner.py` (verbatim, with line ranges).

---

## A.1.a — Conjecture statement quoted from `xi0_d3_runner.py` lines 1–17

> XI0-D3-DIRECT  --  Newton-polygon / Borel-singularity test of the
> cross-degree universality conjecture
>     xi_0(b) = d / beta_d^{1/d}
> at d = 3, per Galois bin.
>
> Conjecture origin:
>   CHANNEL-THEORY v1.3  Conj 3.3.A* (D2-NOTE-DRAFT)
>   PROVEN  at d = 2  (Newton-polygon proof, CT v1.3 Sec 3.3.A)
>   EMPIRICAL at d = 4 (PCF2-SESSION-Q1, ~80 digits)
>   DEFERRED at d = 3 (this prompt closes that gap)

## A.1.b — The algebraic Newton-polygon argument quoted from
`xi0_d3_runner.py` lines 23–34

> (A) ALGEBRAIC NEWTON-POLYGON
>     Build  L f = (poly in z),  L = 1 - z B(theta+1) - z^2,
>     B(t) = sum_{k} alpha_k t^k.
>     Newton polygon edge at z = 0:  (0,0) -- (1, 3)  slope 1/3.
>     Ansatz f ~ exp(c / u),  z = u^3:
>       chi(c) = 1 + alpha_3 c^3 / 27 = 0
>       c^3 = -27 / alpha_3,  |c| = 3 / alpha_3^{1/3}.
>     Compare |c_root| to xi_0_conj = 3 / alpha_3^{1/3} to >=60 digits.

## A.1.c — Q20 STRUCTURAL OBSERVATION quoted from `handoff.md`
(Anomalies section, "W1 (structural triviality)")

> the algebraic test depends only on alpha_3.  The 80-digit per-bin
> agreement is uniformity evidence, not independent verification of
> bin-specific behaviour.  The d=4 framework (PCF2-SESSION-Q1) has
> the same property and was accepted as EMPIRICAL evidence; the
> prompt explicitly directs us to mirror that framework.  Claude may
> want to consider whether the operator-level derivation in this
> script is in fact a **proof** (modulo standard Newton-polygon /
> irregular-singular-point theorems), not merely empirical.  If so,
> D2-NOTE Conj 3.3.A*'s d=3 row could be upgraded from DEFERRED to
> PROVEN, not just EMPIRICAL.  This is an upgrade *beyond* the
> prompt's PASS criterion -- I have written the verdict at the
> empirical level the prompt requested, and surfaced the proof
> question here.

This is the structural observation Q20 arbitrates: is the operator
derivation a **proof at all d ≥ 2** modulo Newton-polygon / ISP
machinery (per Wasow §X.3, Adams 1928, Birkhoff 1930, B–T 1933), or
is it empirical-at-d=3-only?

## A.1.d — Algebraic test code quoted from `xi0_d3_runner.py`
lines 110–149 (`operator_points`, `newton_edge_vertices`,
`char_poly_along_edge`)

```python
def operator_points(coeffs):
    """L = 1 - z B(theta+1) - z^2 with B(t) = a3 t^3 + a2 t^2 + a1 t + a0."""
    a3, a2, a1, a0 = coeffs
    t = sp.symbols("_t")
    B_shift = (sp.Integer(a3) * (t + 1) ** 3
               + sp.Integer(a2) * (t + 1) ** 2
               + sp.Integer(a1) * (t + 1)
               + sp.Integer(a0))
    poly = sp.Poly(sp.expand(B_shift), t)
    coeffs_t = poly.all_coeffs()
    deg = poly.degree()
    pts = {(0, 0): sp.Integer(1)}
    for power_t, c in zip(range(deg, -1, -1), coeffs_t):
        cR = sp.Rational(c)
        if cR != 0:
            pts[(1, power_t)] = -cR
    pts[(2, 0)] = pts.get((2, 0), sp.Integer(0)) - sp.Integer(1)
    return pts

def newton_edge_vertices(pts):
    by_i = {}
    for (i, j), c in pts.items():
        if c == 0: continue
        by_i.setdefault(i, []).append(j)
    js_at_1 = max(by_i.get(1, [-1]))
    return [(0, 0), (1, js_at_1)]

def char_poly_along_edge(pts, vertices):
    (_, j_top) = vertices[1]
    d = j_top
    c = sp.symbols("c")
    chi = pts[(0, 0)] * sp.Integer(1)
    if (1, d) in pts:
        chi += pts[(1, d)] * (-c / sp.Integer(d)) ** d
    chi = sp.expand(chi)
    return chi, c, d
```

This builds the Newton polygon vertices of `L_d`, identifies the
slope-`1/d` edge as `(0,0) → (1, d)`, and writes the characteristic
polynomial `χ(c)` along that edge, in a manner that is uniform
in `d` (the runner's `d=3` is just an instantiation; `d` is the
edge-degree variable in the code, not a hard-coded constant).
