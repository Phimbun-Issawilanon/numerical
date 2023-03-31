#1
using DifferentialEquations
using Plots

f(y,p,t) = -0.3*y

y0 = 1.0
tspan = (0.0, 20)

prob = ODEProblem(f, y0, tspan)
sol = solve(prob)


plot(sol; label="")

#2
using DifferentialEquations
using Plots

f(y,p,t) = 3.0*exp(-t)

y0 = 0.0
tspan = (0.0, 20)

prob = ODEProblem(f, y0, tspan)
sol = solve(prob)


plot(sol; label="")

#3
using DifferentialEquations
using Plots

f(y,p,t) = -0.5*(t-1)*y

y0 = 1.0
tspan = (0.0, 20)

prob = ODEProblem(f, y0, tspan)
sol = solve(prob)


plot(sol; label="")
