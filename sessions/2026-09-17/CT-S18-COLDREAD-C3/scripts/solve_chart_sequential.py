import sympy as sp
z,p,q=sp.symbols('z p q')
I=sp.I; s=sp.sqrt(11)
for sign in [1,-1]:
    t=sign*2*I*s/(3*sp.sqrt(3))
    thi=sp.simplify(1+2*s*I/(27*t))
    print('sign', sign, 't=', sp.simplify(t), 'theta_inf=', sp.simplify(thi))
    # paste coeffs? recompute quickly
    D=z*(z-1)
    a=p+sp.Rational(1,2)*(-2*q*t+t-thi)*(z-q)-sp.Rational(1,2)*t*(z-q)**2
    c=-(z-q)/(q-1)
    ss=p+sp.Rational(1,2)*(q-1)*q*t
    br=ss**2+(q-1)*(-q*thi**2/sp.Integer(4))
    f=p+sp.Rational(1,2)*((q-1)*q*t+q*thi)
    b=-z*br/q-(q-1)*f*f/q
    m11=a/D; m12=b/D; m21=c/D
    n21=-m21; n22=m11; n12=-m12
    P=-sp.diff(n21,z)/n21
    Q=-(sp.diff(n22,z)+n22**2+n21*n12-(sp.diff(n21,z)/n21)*n22)
    R=sp.together(Q-sp.diff(P,z)/2-P**2/4)
    h=-I*s/3
    x0=(-sp.Rational(1,3)-h)/2
    x=x0+h*z
    Psys=(2*z-1)/D; Qsys=-x**2/(3*D); Rsys=sp.together(Qsys-sp.diff(Psys,z)/2-Psys**2/4)
    num=sp.factor(sp.together(R-Rsys).as_numer_denom()[0])
    poly=sp.Poly(num,z)
    coeffs=[sp.factor(c0) for c0 in poly.all_coeffs() if c0!=0]
    for i,c0 in enumerate(coeffs): print(i, c0)
    sol=sp.solve(coeffs, [p,q], dict=True, simplify=True)
    print('sol', sol)
