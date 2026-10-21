import sympy as sp
z,p,q,t,thi=sp.symbols('z p q t theta_infinity')
I=sp.I; s=sp.sqrt(11)
D=z*(z-1)
h=-I*s/3
x0=(-sp.Rational(1,3)-h)/2
x=x0+h*z
Psys=(2*z-1)/D; Qsys=-x**2/(3*D); Rsys=sp.together(Qsys-sp.diff(Psys,z)/2-Psys**2/4)
for component in [1,2]:
  print('component',component)
  a=p+sp.Rational(1,2)*(-2*q*t+t-thi)*(z-q)-sp.Rational(1,2)*t*(z-q)**2
  c=-(z-q)/(q-1)
  ss=p+sp.Rational(1,2)*(q-1)*q*t
  br=ss**2+(q-1)*(-q*thi**2/sp.Integer(4))
  f=p+sp.Rational(1,2)*((q-1)*q*t+q*thi)
  b=-z*br/q-(q-1)*f*f/q
  m11=a/D; m12=b/D; m21=c/D
  if component==1:
    n12=-m12; n11=-m11; n21=-m21
    P=-sp.diff(n12,z)/n12
    Q=-(sp.diff(n11,z)+n11**2+n12*n21-(sp.diff(n12,z)/n12)*n11)
  else:
    n21=-m21; n22=m11; n12=-m12
    P=-sp.diff(n21,z)/n21
    Q=-(sp.diff(n22,z)+n22**2+n21*n12-(sp.diff(n21,z)/n21)*n22)
  R=sp.together(Q-sp.diff(P,z)/2-P**2/4)
  for sign in [1,-1]:
    tv=sign*2*I*s/(3*sp.sqrt(3))
    # solve coefficients numerically for p,q,thi with t fixed using nsolve random
    num=sp.together((R-Rsys).subs(t,tv)).as_numer_denom()[0]
    coeffs=sp.Poly(num,z).all_coeffs()
    # maybe first coeff solve theta relation automatically
    print('sign',sign, 'degree', sp.Poly(num,z).degree())
    for seed in range(20):
      import random
      guess=[complex(random.uniform(-2,2),random.uniform(-2,2)) for _ in range(3)]
      try:
        sol=sp.nsolve(coeffs, [p,q,thi], guess, tol=1e-30, maxsteps=100, prec=60)
        print('SOL', [sp.N(v,30) for v in sol]); break
      except Exception: pass
