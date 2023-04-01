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

def plot_graph(sol):
    plt.plot(sol.t, sol.y[0])
    plt.xlabel("time")
    plt.ylabel('y(t)')
    plt.show()
    plt.title("y' = -0.3*y")
    #plt.savefig("xxx")

t_span = [0,20]
y0 = [1]
sol = solve_ivp(func1, t_span, y0, t_eval=np.arange(0,20,0.1))
#sol = solve_ivp(func1, t_span, y0, t_eval=np.arange(0,20,0.1), method="RK23") # explicit Runge-Kuttanethod of order 3(2)
#sol = solve_ivp(func1, t_span, y0, t_eval=np.arange(0,20,0.1), method="RK45") # explicit Runge-Kuttanethod of order 5(4)
#sol = solve_ivp(func1, t_span, y0, t_eval=np.arange(0,20,0.1), method="BDF") # implicit
# result
print(len(sol.y[0]), sol.y)
print(len(sol.t), sol.t)
plot_graph(sol)