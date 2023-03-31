# REF: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.03-The-Euler-Method.html
# dy/dt = -ky(t)

import numpy as np
import matplotlib.pyplot as plt

#plt.style.use('seaborn-poster')

# Define parameters
k = 0.1
#h = 0.1 # Step size
#t = np.arange(0, 1 + h, h) # Numerical grid
xs = np.linspace(0,20,200) #(start, stop, num)
y0 = 1.0 # Initial Condition

f = lambda x, y: -k*y # ODE

'''def model(y,t,k):
    dydt = -k * y
    return dydt'''

# Explicit Euler Method
ys = np.zeros(len(xs))
ys[0] = y0

for i in range(0, len(xs) - 1):
    #s[i + 1] = s[i] + h*model(s[i],t[i],k=0.1)
    ys[i + 1] = ys[i] + (xs[i+1]-xs[i])*f(xs[i], ys[i])

plt.figure(figsize = (12, 8))
# calculate ds/st
plt.plot(xs, ys, '.-', label='Approximate')
# calculate s(t)
#plt.plot(t, -np.exp(-3*t), 'g', label='Exact')
plt.title('Approximate ODE Solution with Explicit Euler Method')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.savefig("sol1_euler_python")
plt.show()