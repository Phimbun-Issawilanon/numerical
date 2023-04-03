# https://docs.scipy.org/doc/scipy/reference/integrate.html
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def func1(t,y):
    dydt = -0.3 * y
    return dydt

def func2(t,y):
    dydt = 3 * np.exp(-t)
    return dydt

def func3(t,y):
    dydt = -0.5 * (t-1) * y
    return dydt

# equation 1) y' = -0.3*y, y0=1
# equation 2) y' = 3*e^(-t), y0 = 0
# equation 3) y' = 0.5*(t-1)y, y0 = 1

def plot_graph(t_space, solve):
    plt.plot(t_space, solve)
    plt.xlabel("time")
    plt.ylabel('y(t)')
    plt.show()
    plt.title("y' = -0.3*y")
    #plt.savefig("xxx")

t_begin = 0
t_end = 20
t_nsamples = 200
t_span = [t_begin, t_end]
t_space = np.linspace(t_begin, t_end, t_nsamples)
y0 = 1

sol = solve_ivp(func1, t_span, [y0], dense_output=True)
# methods: 'RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA'
#sol = solve_ivp(func1, t_span, y0, method="RK23", dense_output=True) # explicit Runge-Kuttanethod of order 3(2)
#sol = solve_ivp(func1, t_span, y0, method="RK45", dense_output=True) # explicit Runge-Kuttanethod of order 5(4)
#sol = solve_ivp(func1, t_span, y0, method="BDF", dense_output=True)  # implicit

# result
sol = sol.sol(t_space).T
print(len(sol), sol)
plot_graph(t_space, sol)