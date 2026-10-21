import sympy as sp
p,q=sp.symbols('p q')
I=sp.I; rt3=sp.sqrt(3); rt11=sp.sqrt(11)
z=sp.symbols('z')
# expressions copied/generated
# Use t=2 i sqrt(11)/(3 sqrt(3)); theta=sqrt(3)/9 (other sign is simultaneous negative)
for sign in [1,-1]:
    t=sign*2*I*rt11/(3*rt3)
    th=sign*rt3/9
    bpeq= -p**2 - p*q**2*t + p*q*t - q**4*t**2/4 + q**3*t**2/2 - q**2*t**2/4 + q**2*th**2/4 - q*th**2/4
    coef2=108*p*q*t - 108*p*t + 54*q**3*t**2 - 108*q**2*t**2 + 54*q**2*t*th + 27*q*t**2 - 27*q*th**2 + 54*q*th - 54*q - 6*rt11*I*q + 27*t**2 - 54*t*th + 27*th**2 - 54*th + 54 + 6*rt11*I
    coef3=-108*p**2 - 108*p*q**2*t - 216*p*q + 108*p*t + 216*p - 27*q**4*t**2 - 108*q**3*t + 81*q**2*t**2 - 54*q**2*t*th + 216*q**2*t + 27*q**2*th**2 - 108*q**2*th - 54*q*t**2 + 54*q*t*th - 108*q*t + 108*q*th + 10*q + 2*rt11*I*q - 27*th**2 - 10 - 2*rt11*I
    coef4=108*p**2 + 108*p*q**2*t - 108*p*q*t + 108*p*q - 108*p + 27*q**4*t**2 - 54*q**3*t**2 + 54*q**3*t + 27*q**2*t**2 - 108*q**2*t - 27*q**2*th**2 + 54*q**2*th + 54*q*t + 27*q*th**2 - 54*q*th
    eqs=[sp.simplify(e) for e in [bpeq,coef2,coef3,coef4]]
    print('sign',sign)
    for i,e in enumerate(eqs): print('eq',i, sp.factor(e))
    sol=sp.solve(eqs,[p,q],dict=True,simplify=True)
    print('solcount',len(sol))
    for so in sol: print({str(k):sp.simplify(v) for k,v in so.items()})
