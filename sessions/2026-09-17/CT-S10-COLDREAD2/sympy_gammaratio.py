import sympy as sp
x, r = sp.symbols('x r')
expr = (1-r*x)*(1-x)**(-r)
series = sp.series(expr, x, 0, 5)
print('expr=(1-r*x)*(1-x)**(-r), x=1/n')
print(series)
for k in range(1,5):
    print(f'coeff x^{k}:', sp.simplify(series.removeO().coeff(x,k)))
print('log series:', sp.series(sp.log(expr), x, 0, 5))
