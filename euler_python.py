# REF: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.03-The-Euler-Method.html
# sol1: dy/dt = -ky(t)
# sol2: dy/dt = 3e**-t
# sol3: dy/dt = -(t-1)y(t)/2

import numpy as np
import matplotlib.pyplot as plt
import time
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


# Explicit Euler Method
def explicit_euler(f, ts, ys):
    start_time = time.time()
    for i in range(0, len(ts) - 1):
        ys[i + 1] = ys[i] + (ts[i+1]-ts[i])*f(ys[i], ts[i])
    end_time = time.time()
    return end_time - start_time

def plot_gaph(ts, ys):
    plt.figure(figsize = (12, 8))
    plt.plot(ts, ys, '.-', label='Approximate')
    plt.title('Approximate ODE Solution with Explicit Euler Method')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.grid()
    plt.savefig("sol_euler_python")
    plt.show()
