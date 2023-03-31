# REF: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.03-The-Euler-Method.html
# sol1: dy/dt = -ky(t)
# sol2: dy/dt = 3e**-t
# sol3: dy/dt = -(t-1)y(t)/2

import numpy as np
import matplotlib.pyplot as plt

def function_1(t, y):
    k = 0.1
    return -k*y

def function_2(t, y):
    return 3*np.exp(-t)

def function_3(t, y):
    return -(t-1)*y/2

# Define parameters
ts = np.linspace(0,20,200) #(start, stop, num)
ys = np.zeros(len(ts))
ys[0] = 1.0 # Initial Condition

# Explicit Euler Method
def explicit_euler(f, ts, ys):
    for i in range(0, len(ts) - 1):
        ys[i + 1] = ys[i] + (ts[i+1]-ts[i])*f(ts[i], ys[i])

def plot_gaph(ts, ys):
    # plot graph
    plt.figure(figsize = (12, 8))
    plt.plot(ts, ys, '.-', label='Approximate')
    plt.title('Approximate ODE Solution with Explicit Euler Method')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.savefig("sol_euler_python")
    plt.show()

explicit_euler(function_1, ts, ys)
plot_gaph(ts, ys)
