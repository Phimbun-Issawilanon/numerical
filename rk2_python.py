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

'''y0 = 1.0
t = np.linspace(0,20,200)
y = np.zeros(len(t))
y[0] = y0'''

def rungekutta2(f, y, t):
    for i in range(len(t) - 1):
        h = t[i+1] - t[i]
        y[i+1] = y[i] + h * f(y[i] + f(y[i], t[i]) * h / 2., t[i] + h / 2.)
    return y

def plot_gaph(ts, ys):
    #plt.figure(figsize = (12, 8))
    plt.plot(ts, ys, label='Approximate')
    plt.title('Approximate ODE Solution with Explicit RK2 Method')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.show()

'''y = rungekutta2(func1, y0, t)
plot_gaph(t, y)'''