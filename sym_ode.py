from sympy.solvers.ode import dsolve
import sympy
import time
import math

t = sympy.symbols('t')
y = sympy.Function('y')

dydt = y(t).diff(t)

def func1():
    return -0.3*y(t)
def func2():
    return 3*sympy.exp(-t)
def func3():
    return -0.5*(t-1)*y(t)
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
    dydt = sympy.sqrt(t**2 + y**2)
    return dydt
def func9(y,t):
    dydt = sympy.sin(y) * sympy.exp(t)
    return dydt
def func10(y,t):
    dydt = sympy.sin(t) + sympy.cos(y)
    return dydt

# result 
def solve_ode(func, y0):
    start_time = time.time()
    eqn = sympy.Eq(dydt, func())
    sol = dsolve(eqn, y(t), ics={y(0):y0})
    end_time = time.time()
    return sol.rhs, end_time-start_time
#sympy.plot(sol.rhs,(t,0,20))


