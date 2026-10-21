# Cold read report: PACKET-A-remark22-lemma

Initial repository check: branch `log-pv-01`, HEAD `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.

Final repository check: branch `log-pv-01`, HEAD `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.

Isolation statement: I read only the specified packet file under `sessions/2026-09-17/` and did not read any other file in that tree. I wrote artifacts only in `sessions/2026-09-17/CT-S11-COLDREAD3/`.

## Step-by-step review

1. **Step 1: CORRECT.** With `t = x-s` and `chi = t h`, `h(s) != 0`,
   `chi' = h + t h'`, so
   `(x-s) chi'/chi = chi'/h -> h(s)/h(s) = 1`. Thus `p = chi'/chi`
   has a simple pole with residue exactly `1`.

2. **Step 2: CORRECT.** Since `c` is polynomial and `chi` has a simple
   zero at `s`, `q = c/chi` has at most a simple pole. Therefore
   `(x-s)^2 q -> 0`. If `c(s)=0`, then `q` may even be analytic at `s`,
   but the stated limit remains true.

3. **Step 3: CORRECT.** The regular-singular conditions hold because
   `(x-s)p` and `(x-s)^2 q` are analytic at `s`. The indicial polynomial is
   `lambda(lambda-1) + p0 lambda + q0` with `p0=1`, `q0=0`, hence
   `lambda^2`.

4. **Step 4: CORRECT.** For a second-order regular singular point with a
   repeated indicial root, the second independent local solution has a
   logarithmic term. In this particular equation the nonzero coefficient can
   be seen directly by reduction of order. A Frobenius solution for exponent
   `0` has the form `y1 = a(t)` with `a(0) != 0`. Since `p = chi'/chi`,
   `exp(-integral p dx) = const/chi = const/(t h(t))`, and
   `1/(chi y1^2) = const/(t h(t) a(t)^2)` has a simple pole with nonzero
   residue. Thus
   `y2 = y1 integral dx/(chi y1^2)` contains a nonzero multiple of
   `y1 log(t)`. The logarithm gives nontrivial local monodromy, so the
   singularity is not apparent.

5. **Step 5: CORRECT.** The conclusion is independent of `c`. Dropping the
   older hypothesis `c(s) != 0` is legitimate: `c(s)=0` can remove the pole
   of `q`, but it cannot remove the pole of `p=chi'/chi` when `s` is a simple
   root of `chi`. The packet's phrase "assume `s` is a genuine singular point"
   is harmless here; for a simple root of `chi`, the standard-form coefficient
   `p` is singular regardless of `c`.

## SymPy checks

I wrote `verify_examples.py` and saved its output in `verify_examples.out`.
The output SHA-256 is
`E8E1A9128587293B3C765A438C47C6FE242B1C6D6DCFDF659A1D0712C26A0D5D`.

The script checks three examples exactly:

- `chi=x, c=0`: indicial polynomial `lambda**2`, solutions `1` and `log(x)`.
- `chi=x, c=x`: this has `c(0)=0` and analytic `q`; SymPy verifies
  `J_0(x)` and `Y_0(x)` solve the equation, and the displayed series for
  `Y_0(x)` contains `2*log(x)/pi`.
- `chi=x, c=1`: this has `c(0)!=0`; SymPy verifies the Frobenius solution
  `J_0(2 sqrt(x))`, and the reduction-of-order integrand has residue `1`,
  forcing a logarithm.

## Final verdict

**SOUND.**
