from sympy.solvers.ode import dsolve
import sympy
t = sympy.symbols('t')
y = sympy.Function('y')

dydt = y(t).diff(t)

def func1():
    return -0.3*y(t)
def func2():
    return 3*sympy.exp(-t)
def func3():
    return -0.5*(t-1)*y(t)

# result 
eqn = sympy.Eq(dydt, func2())
sol = dsolve(eqn, y(t), ics={y(0):1})
print(sol)
sympy.plot(sol.rhs,(t,0,20))


