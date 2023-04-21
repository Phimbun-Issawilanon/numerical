# https://docs.scipy.org/doc/scipy/reference/integrate.html
# equation 1) y' = -0.3*y, y0=1
# equation 2) y' = 3*e^(-t), y0 = 0
# equation 3) y' = 0.5*(t-1)y, y0 = 1
# def function(t,y):

import numpy as np
import matplotlib.pyplot as plt
import time
import math

from scipy.integrate import solve_ivp

def func1(t,y):
    dydt = -0.3 * y
    return dydt
def func2(t,y):
    dydt = 3 * np.exp(-t)
    return dydt
def func3(t,y):
    dydt = -0.5 * (t-1) * y
    return dydt
def func4(t,y):
    dydt = (t**2)+y
    return dydt
def func5(t,y):
    dydt = (t**2 - y**2)/(t**2 + y**2)
    return dydt
def func6(t,y):
    dydt = y*(1-y)
    return dydt
def func7(t,y):
    dydt = 2*t + (y/t)
    return dydt
def func8(t,y):
    dydt = math.sqrt(t**2 + y**2)
    return dydt
def func9(t,y):
    dydt = math.sin(y) * np.exp(t)
    return dydt
def func10(t,y):
    dydt = math.sin(t) + math.cos(y)
    return dydt

def plot_graph(t_space, solve):
    plt.plot(t_space, solve)
    plt.xlabel("time")
    plt.ylabel('y(t)')
    plt.show()
    plt.title("y' = -0.3*y")

#t_begin = 0
#t_nsamples = 200
#t_span = [t_begin, t_end]
#t_space = np.linspace(t_begin, t_end, t_nsamples)
#y0 = 1
def solve_ode(func, t_space, y0):
    start_time = time.time()
    t_span = [t_space[0],t_space[-1]]
    sol = solve_ivp(func, t_span, [y0], dense_output=True)
    # methods: 'RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA'
    #sol = solve_ivp(func1, t_span, y0, method="RK23", dense_output=True) # explicit Runge-Kuttanethod of order 3(2)
    #sol = solve_ivp(func1, t_span, y0, method="RK45", dense_output=True) # explicit Runge-Kuttanethod of order 5(4)
    #sol = solve_ivp(func1, t_span, y0, method="BDF", dense_output=True)  # implicit

    # result
    sol = sol.sol(t_space).T
    end_time = time.time()
    return sol, end_time-start_time