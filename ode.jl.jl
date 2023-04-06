#ODE.jl
#ode45
using ODE
using Plots

f(y,p,t) = -0.5*(t-1)*y
y0=1.0
tspan = (0.0, 1)
prob = ODEProblem(f,y0, tspan)
sol = solve(prob,ode45(),reltol=1e-8,abstol=1e-8)

plot(sol,xaxis="Time (t)") # legend=false


#ode23
using ODE
using Plots

f(y,p,t) = -0.5*(t-1)*y
y0=1.0
tspan = (0.0, 1)
prob = ODEProblem(f,y0, tspan)
sol = solve(prob,ode23(),reltol=1e-8,abstol=1e-8)

plot(sol,xaxis="Time (t)") # legend=false


