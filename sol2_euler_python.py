# REF: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.03-The-Euler-Method.html
# dy/dt = 3e**-t

import numpy as np
import matplotlib.pyplot as plt

#plt.style.use('seaborn-poster')

# Define parameters
f = lambda x, y: 3*np.exp(-x) # ODE
h = 0.1 # Step size
xs = np.arange(0, 1 + h, h) # Numerical grid
y0 = 1.0 # Initial Condition

# Explicit Euler Method
ys = np.zeros(len(xs))
ys[0] = y0

for i in range(0, len(xs) - 1):
    ys[i + 1] = ys[i] + h*f(xs[i], ys[i])

plt.figure(figsize = (12, 8))
# calculate ds/st
plt.plot(xs, ys, 'o-', label='Approximate')
# calculate s(t)
#plt.plot(t, -np.exp(-3*t), 'g', label='Exact')
plt.title('Approximate ODE Solution with Explicit Euler Method')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.savefig("sol2_euler_python")
plt.show()