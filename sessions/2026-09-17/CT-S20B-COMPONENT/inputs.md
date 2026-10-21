# Inputs

Exact expressions. Variable z. Symbols p, q, t, th0, th1, thi.

## 1. Rank-2 system

D(z) = z*(z-1)

Matrix A(z) has entries a, b, c, and d = -a (trace-free):

  a = p + (1/2)*(-2*q*t + t - thi)*(z - q) - (1/2)*t*(z - q)**2

  b = -(z*((p + (1/2)*(q-1)*q*t)**2 - th1**2/4
        + (q-1)*(th0**2/4 - th1**2/4 - q*thi**2/4)))/q
      - ((q-1)*(p + (1/2)*((q-1)*q*t - th0 + q*thi))
        *(p + (1/2)*((q-1)*q*t + th0 + q*thi)))/q

  c = -(z - q)/(q - 1)

Convention, given and not to be re-derived here:
  N11 = -a/D,  N12 = -b/D,  N21 = -c/D,  N22 = a/D
and the system is  y' = N y,  y = (y1, y2).

## 2. System C, scalar form

  s_plus = (-1 + I*sqrt(11))/6
  delta  = -I*sqrt(11)/3
  x(z)   = s_plus + delta*z

  P_C = delta*(6*x + 1)/(3*x**2 + x + 1)
  Q_C = delta**2*(-x**2)/(3*x**2 + x + 1)

System C is  y'' + P_C*y' + Q_C*y = 0.

## 3. The point

  p  = 5*I*(-28151758571*sqrt(33) + 48874838016*sqrt(11))/4086468672
  q  = 1/2 + (-457937*sqrt(11)*I + 281700*sqrt(33)*I)/122408
  t  = -2*sqrt(33)*I/9
  thi = -2 - sqrt(3)/9
  th0 = 0
  th1 = 0

## 4. Conventions

  b-route: scalar reduction via the first component (eliminate y2).
  c-route: scalar reduction via the second component (eliminate y1).