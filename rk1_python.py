#REF: https://perso.crans.org/besson/publis/notebooks/Runge-Kutta_methods_for_ODE_integration_in_Python.html

import numpy as np
import matplotlib.pyplot as plt
from time import time
import math

def func1(y,t):
    dydt = -0.3 * y
    return dydt
def func2(y,t):
    dydt = 3 * np.exp(-t)
    return dydt
def func3(y,t):
    dydt = -0.5 * (t-1) * y
    return dydt
def func4(y,t):
    dydt = (t**2)+y
    return dydt
def func5(y,t):
    dydt = (t**2 - y**2)/(t**2 + y**2)
    return dydt
def func6(y,t):
    dydt = y*(1-y)
    return dydt
def func7(y,t):
    dydt = 2*t + (y/t)
    return dydt
def func8(y,t):
    dydt = math.sqrt(t**2 + y**2)
    return dydt
def func9(y,t):
    dydt = math.sin(y) * np.exp(t)
    return dydt
def func10(y,t):
    dydt = math.sin(t) + math.cos(y)
    return dydt
"""y0 = 1.0
t = np.linspace(0,20,200)
y = np.zeros(len(t))
y[0] = y0"""

def rungekutta1(f, t, y):
    s_time = time()
    for i in range(len(t) - 1):
        y[i+1] = y[i] + (t[i+1] - t[i]) * f(y[i], t[i])
    e_time = time()
    return y, e_time-s_time

"""sol = rungekutta1(func1, y0, t)
plt.plot(t, sol)
#plt.plot(t, sol[:, 0], 'b', label=r'$\theta(t)$')
#plt.plot(t, sol[:, 1], 'g', label=r'$\omega(t)$')
plt.legend(loc='best')
plt.xlabel('t')
plt.show()"""