# https://docs.scipy.org/doc/scipy/reference/integrate.html
import numpy as np 
import matplotlib.pyplot as plt
import time
import math

from scipy.integrate import odeint

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

def solve_ode(func, t, y0):
    stat_time = time.time()
    sol = odeint(func, y0, t)
    end_time = time.time()
    return sol, end_time-stat_time
