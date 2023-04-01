# https://docs.scipy.org/doc/scipy/reference/integrate.html
import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func1(y,t):
    k = 0.3
    dydt = -k * y
    return dydt

def func2(y,t):
    k = 3
    dydt = k * np.exp(-t)
    return dydt

def func3(y,t):
    k = -0.5
    dydt = k * (t-1) * y
    return dydt

# result 
y0 = 1
t = np.linspace(0,20,200)
print(len(t), t)
y = odeint(func1, y0, t)
print(len(y), y)

plt.plot(t,y)
plt.xlabel("time")
plt.ylabel('y(t)')
plt.show()