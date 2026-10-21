import sympy as sp, random
z,p,q,t,thi=sp.symbols('z p q t theta_infinity')
I=sp.I; h=-I*sp.sqrt(11)/3
D=z*(z-1)
def R_family_expr():
    a = p + sp.Rational(1,2)*(-2*q*t+t-thi)*(z-q) - sp.Rational(1,2)*t*(z-q)**2
    c = -(z-q)/(q-1)
    s = p + sp.Rational(1,2)*(q-1)*q*t
    br = s**2 + (q-1)*(-q*thi**2/sp.Integer(4))
    f = p + sp.Rational(1,2)*((q-1)*q*t + q*thi)
    b = -z*br/q - (q-1)*f*f/q
    m11=a/D; m12=b/D; m21=c/D
    n21=-m21; n22=m11; n12=-m12
    P= -sp.diff(n21,z)/n21
    Q= -(sp.diff(n22,z)+n22**2+n21*n12 - (sp.diff(n21,z)/n21)*n22)
    return sp.together(Q-sp.diff(P,z)/2-P**2/4)
R=R_family_expr()
x0=(-sp.Rational(1,3)-h)/2
x=x0+h*z
Psys=(2*z-1)/D
Qsys=-x**2/(3*D)
Rsys=sp.together(Qsys-sp.diff(Psys,z)/2-Psys**2/4)
num=sp.together(R-Rsys).as_numer_denom()[0]
poly=sp.Poly(num,z)
coeffs=[sp.N(c,50) for c in poly.all_coeffs()]
# remove leading duplicate zeros? choose coeffs numerically
print('degree', poly.degree(), 'coeffs', len(coeffs))
for idx,c in enumerate(poly.all_coeffs()): print(idx, sp.factor(c))
# Use selected coefficients maybe all
for seed in range(30):
    guess=[complex(random.uniform(-2,2), random.uniform(-2,2)) for _ in range(4)]
    try:
        sol=sp.nsolve(poly.all_coeffs(), [p,q,t,thi], guess, tol=sp.Float('1e-40'), maxsteps=100, prec=80)
        print('SOL', [sp.N(s,30) for s in sol])
        break
    except Exception as e:
        pass
