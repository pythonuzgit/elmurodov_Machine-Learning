import numpy as np

def rKF(f, t0, y0, tEnd, tau):
    """
    Solve the initial value problem y' = f(t,y)
    by 4th-order Runge-Kutta-Fehlberg method.
    t0, y0 are the initial conditions
    tEnd is the terminal value of t,
    tau is the step.
    """
    def increment(f, t, y, tau):
        k0 = tau * f(t, y)
        k1 = tau * f(t + tau/4., y + k0/4.)
        k2 = tau * f(t + 3./8. * tau, y + 3./32. * tau * k0 + 9./32.* tau * k1)
        k3 = tau * f(t + 12./13. * tau, y + 1932./2197. * tau * k0 -
                     7200./2197 * tau * k1 + 7296./2197. * tau * k2)
        k4 = tau * f(t + tau, y + 439./216. * tau * k0 -8. * tau * k1 +
                     3680./513. * tau * k2 - 845./4104. * tau * k3)
        k5 = tau * f(t + 1./2. * tau, y - 8./27. * tau * k0 + 2. * tau *k1 - 3544./2565. * tau * k2 +
                     1859./4104. * tau * k3 -11./40. * tau * k4)
        return 16./ 135. * k0 + 6656./ 12825. * k2 +28561./ 56430. * k3 -\
               9./50. * k4 + 2./55. * k5

    t = []
    y = []

    t.append(t0)
    y.append(y0)

    while t0 < tEnd:
        tau = min(tau, tEnd - t0)
        y0 = y0 + increment(f, t0, y0, tau)
        t0 = t0 + tau
        t.append(t0)
        y.append(y0)

    return np.array(t), np.array(y)


import numpy as np
import math as mt
import matplotlib.pyplot as plt

"""
Numerical solution of Didderential equation
by using Runge-Kutta- Fehlbeg: dy1/dt = y2,
dy2/dt= cos(y1), 0<t<4*phi 
"""



def f(t,y):
    f = np.zeros((2), 'float')
    f[0] = y[1]
    f[1] = mt.cos(y[0])
    return f

t0 = 0.
tEnd = 4. * np.pi
y0 = np.array([1., 0.])
tau = 0.25
t, y = rKF(f, t0, y0, tEnd, tau)
for n in range(0, 2):
    r = y[:, n]
    st = '$y$'
    sg = '-'
    if n == 1:
        st = '$\\frac{dy}{dt}$'
        sg = '--'
    plt.plot(t,r,sg,label = st)
    


plt.legend(loc=0)
plt.xlabel('$t$')
plt.grid(True)
plt.show()

