import sympy as sp
import mpmath as mp
z=sp.symbols('z')
I=sp.I; rt3=sp.sqrt(3); rt11=sp.sqrt(11); rt33=sp.sqrt(33)
D=z*(z-1)
t=2*rt33*I/9
th=-2+rt3/9
p=5*(sp.Integer(156636384689044)*rt33 + sp.Integer(271939598721024)*rt11 + sp.Integer(46172647864885092)*I + sp.Integer(26659773733835227)*rt3*I)/(sp.Integer(371497152)*(sp.Integer(457937)*rt11 + sp.Integer(281700)*rt33 - sp.Integer(61204)*I))
q=sp.Rational(1,2)-sp.Rational(70425,30602)*rt33*I-sp.Rational(457937,122408)*rt11*I
K=(sp.Integer(1785871783)*rt11 + sp.Integer(1087554096)*rt33 - sp.Integer(559037336)*I + sp.Integer(48473568)*rt3*I)/(sp.Integer(19008)*(sp.Integer(457937)*rt11 + sp.Integer(281700)*rt33 - sp.Integer(61204)*I))
S0=p+sp.Rational(1,2)*q*((q-1)*t+th)
S1=p+sp.Rational(1,2)*(q-1)*(q*t+th)
th0sq=sp.simplify(4*(S0**2-K*q/(q-1)))
th1sq=sp.simplify(4*(S1**2-K))
aA=-t*z**2/2+(t-th)*z/2+S0
bA=-K
cA=(q-z)/(q-1)
A=sp.Matrix([[aA,bA],[cA,-aA]])
N=-A/D
def scalar(N, idx):
    a,b,c,d=N[0,0],N[0,1],N[1,0],N[1,1]
    if idx==1:
        P=-(a+d+sp.diff(b,z)/b)
        Q=-(sp.diff(a,z)+b*c-a*sp.diff(b,z)/b-a*d)
    else:
        P=-(a+d+sp.diff(c,z)/c)
        Q=-(sp.diff(d,z)+b*c-d*sp.diff(c,z)/c-a*d)
    return sp.cancel(P), sp.cancel(Q)
P1,Q1=scalar(N,1); P2,Q2=scalar(N,2)
s=I*rt11; x=(-1+s*(1-2*z))/6
PC=(2*z-1)/D; QC=-x**2/(3*D)
print('batch symbolic comparisons in=4')
rP1=sp.cancel(sp.together(P1-PC)); rQ1=sp.cancel(sp.together(Q1-QC)); rP2=sp.cancel(sp.together(P2-PC))
print('P1_minus_PC=', rP1)
print('Q1_minus_QC_cancel_is_zero=', rQ1==0)
print('Q1_minus_QC_radsimp_num_is_zero=', sp.radsimp(sp.together(rQ1).as_numer_denom()[0])==0)
print('P2_minus_PC=', sp.factor(rP2))
print('theta0_sq=', th0sq, 'theta1_sq=', th1sq)
print('batch symbolic comparisons out=4')
assert rP1==0 and sp.radsimp(sp.together(rQ1).as_numer_denom()[0])==0 and th0sq==0 and th1sq==0
wrong=sp.cancel(sp.together(Q1-(QC+sp.Rational(1,7))))
print('wrong_Q_shift_symbolic_zero=', wrong==0)
assert wrong != 0
print('batch numeric substitution in=6')
max_alg=0.0
for val in [sp.Rational(2,3), sp.Rational(3,2), 2, 3, -1, sp.Rational(5,4)]:
    rp=sp.N((P1-PC).subs(z,val),90)
    rq=sp.N((Q1-QC).subs(z,val),90)
    ap=abs(complex(rp)); aq=abs(complex(rq)); max_alg=max(max_alg,ap,aq)
    print('z=',val,'absP=',ap,'absQ=',aq)
print('batch numeric substitution out=6 max=',max_alg,'dps=90')
assert max_alg < 1e-60
pp,qq,tt,ttinf,theta0=sp.symbols('p q t th theta0')
S0good=pp+sp.Rational(1,2)*qq*((qq-1)*tt+ttinf)
S0bad=pp+sp.Rational(1,2)*qq*(qq-1)
det_good_plus=sp.factor(sp.det(sp.Matrix([[-S0good,(qq-1)/qq*(S0good**2-theta0**2/4)],[-qq/(qq-1),S0good]]))+theta0**2/4)
det_bad_plus=sp.factor(sp.det(sp.Matrix([[-S0good,(qq-1)/qq*(S0bad**2-theta0**2/4)],[-qq/(qq-1),S0good]]))+theta0**2/4)
print('detA0_good_plus_theta0sq_over4=',det_good_plus)
print('detA0_bad_plus_theta0sq_over4=',det_bad_plus)
assert det_good_plus==0 and det_bad_plus!=0
print('batch local-system residuals in=',9)
points=[sp.Rational(4,5), sp.Rational(13,10), sp.Rational(11,5)]
inits=[(1,0),(0,1),(1,-2)]
maxres=sp.Float(0,100)
Np=sp.diff(N,z)
for init in inits:
    Y=sp.Matrix([init[0],init[1]])
    for zz in points:
        Yp=N*Y
        Ypp=(Np+N*N)*Y
        res=sp.N((Ypp[0]+PC*Yp[0]+QC*Y[0]).subs(z,zz),100)
        absres=abs(complex(res))
        maxres=max(maxres, sp.Float(absres,80))
        print('Y_at_z=',init,'z=',zz,'res_abs=',absres)
print('batch local-system residuals out=9 max=',maxres,'dps=100')
assert maxres < sp.Float('1e-70',80)
wrongmax=sp.Float(0,80)
for zz in points:
    wrongmax=max(wrongmax, abs(sp.N((P2-PC).subs(z, zz),50)))
print('wrong_component_P_residual_sample_max=',wrongmax)
assert wrongmax > sp.Float('1e-3',50)
