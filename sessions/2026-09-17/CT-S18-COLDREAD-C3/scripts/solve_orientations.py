import sympy as sp
z,p,q=sp.symbols('z p q')
I=sp.I; s=sp.sqrt(11)
for h in [-I*s/3, I*s/3]:
  for sign in [1,-1]:
    t=sign*2*I*s/(3*sp.sqrt(3))
    thi=sp.simplify(1+2*s*I/(27*t)) # for h=-. For h plus maybe coeff term changes sign; derive via solve below instead.
    # recompute coefficient1 solve thi from leading series rather than use formula
    tv=t
    D=z*(z-1)
    qsym=q; psym=p; thisym=sp.symbols('thi')
    a=psym+sp.Rational(1,2)*(-2*qsym*tv+tv-thisym)*(z-qsym)-sp.Rational(1,2)*tv*(z-qsym)**2
    c=-(z-qsym)/(qsym-1)
    ss=psym+sp.Rational(1,2)*(qsym-1)*qsym*tv
    br=ss**2+(qsym-1)*(-qsym*thisym**2/sp.Integer(4))
    f=psym+sp.Rational(1,2)*((qsym-1)*qsym*tv+qsym*thisym)
    b=-z*br/qsym-(qsym-1)*f*f/qsym
    m11=a/D; m12=b/D; m21=c/D
    n21=-m21; n22=m11; n12=-m12
    P=-sp.diff(n21,z)/n21
    Q=-(sp.diff(n22,z)+n22**2+n21*n12-(sp.diff(n21,z)/n21)*n22)
    R=sp.together(Q-sp.diff(P,z)/2-P**2/4)
    x0=(-sp.Rational(1,3)-h)/2
    x=x0+h*z
    Psys=(2*z-1)/D; Qsys=-x**2/(3*D); Rsys=sp.together(Qsys-sp.diff(Psys,z)/2-Psys**2/4)
    poly=sp.Poly(sp.together(R-Rsys).as_numer_denom()[0],z)
    coeffs=poly.all_coeffs()
    solthi=sp.solve(sp.factor(coeffs[1]/(2*q*(q-1))), thisym)
    print('h',h,'tsign',sign,'thi_solutions',solthi)
    for thiv in solthi:
      cs=[sp.factor(c0.subs(thisym,thiv)) for c0 in coeffs[2:6]]
      sol=sp.solve(cs,[p,q],dict=True,simplify=True)
      print('  thi',sp.simplify(thiv),'solpq',sol)
