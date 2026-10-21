import sympy as sp
I=sp.I; rt3=sp.sqrt(3); rt11=sp.sqrt(11); rt33=sp.sqrt(33)
t=2*rt33*I/9; th=-2+rt3/9
p=5*(sp.Integer(156636384689044)*rt33 + sp.Integer(271939598721024)*rt11 + sp.Integer(46172647864885092)*I + sp.Integer(26659773733835227)*rt3*I)/(sp.Integer(371497152)*(sp.Integer(457937)*rt11 + sp.Integer(281700)*rt33 - sp.Integer(61204)*I))
q=sp.Rational(1,2)-sp.Rational(70425,30602)*rt33*I-sp.Rational(457937,122408)*rt11*I
K=(sp.Integer(1785871783)*rt11 + sp.Integer(1087554096)*rt33 - sp.Integer(559037336)*I + sp.Integer(48473568)*rt3*I)/(sp.Integer(19008)*(sp.Integer(457937)*rt11 + sp.Integer(281700)*rt33 - sp.Integer(61204)*I))
S0=p+sp.Rational(1,2)*q*((q-1)*t+th)
S1=p+sp.Rational(1,2)*(q-1)*(q*t+th)
th0sq=sp.simplify(4*(S0**2-K*q/(q-1)))
th1sq=sp.simplify(4*(S1**2-K))
for name,val in [('t',t),('theta_inf',th),('p',p),('q',q),('K',K),('theta0_sq',th0sq),('theta1_sq',th1sq)]:
    print(name,'exact=',val)
    print(name,'numeric=',sp.N(val,50))
