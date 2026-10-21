import sympy as sp, random
z,p,q,t,thi=sp.symbols('z p q t theta_infinity')
I=sp.I; s=sp.sqrt(11)
D=z*(z-1)
def family_R(component=2):
    a=p+sp.Rational(1,2)*(-2*q*t+t-thi)*(z-q)-sp.Rational(1,2)*t*(z-q)**2
    c=-(z-q)/(q-1)
    ss=p+sp.Rational(1,2)*(q-1)*q*t
    br=ss**2+(q-1)*(-q*thi**2/sp.Integer(4))
    f=p+sp.Rational(1,2)*((q-1)*q*t+q*thi)
    b=-z*br/q-(q-1)*f*f/q
    m11=a/D; m12=b/D; m21=c/D
    if component==2:
        n21=-m21; n22=m11; n12=-m12
        P=-sp.diff(n21,z)/n21
        Q=-(sp.diff(n22,z)+n22**2+n21*n12-(sp.diff(n21,z)/n21)*n22)
    else:
        n12=-m12; n11=-m11; n21=-m21
        P=-sp.diff(n12,z)/n12
        Q=-(sp.diff(n11,z)+n11**2+n12*n21-(sp.diff(n12,z)/n12)*n11)
    return sp.together(Q-sp.diff(P,z)/2-P**2/4), P, Q
for hsign in [-1,1]:
  h=hsign*I*s/3
  x0=(-sp.Rational(1,3)-h)/2
  x=x0+h*z
  Psys=(2*z-1)/D; Qsys=-x**2/(3*D); Rsys=sp.together(Qsys-sp.diff(Psys,z)/2-Psys**2/4)
  print('h', h)
  for component in [1,2]:
    R,Pf,Qf=family_R(component)
    for sign in [-1,1]:
      tv=sign*2*I*s/(3*sp.sqrt(3)) # independent? t^2 fixed
      num=sp.together((R-Rsys).subs(t,tv)).as_numer_denom()[0]
      coeffs=sp.Poly(num,z).all_coeffs()
      sols=[]
      for seed in range(50):
        guess=[complex(random.uniform(-3,3),random.uniform(-3,3)) for _ in range(3)]
        try:
          sol=sp.nsolve(coeffs, [p,q,thi], guess, tol=1e-30, maxsteps=100, prec=70)
          rounded=tuple(complex(sp.N(v,20)) for v in sol)
          if all(abs(rounded[i]-r[i])>1e-8 for r in sols for i in [1]): sols.append(rounded)
        except Exception: pass
      print(' component',component,'tsign',sign,'solutions',sols[:4])
