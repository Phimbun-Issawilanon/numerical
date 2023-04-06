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


f(y,p,t) = 3.0*exp(-t)

y0 = 0.0
tspan = (0.0, 20)

prob = ODEProblem(f, y0, tspan)
sol = solve(prob)


plot(sol; label="")

#3

f(y,p,t) = -0.5*(t-1)*y

y0 = 1.0
tspan = (0.0, 20.0)

prob = ODEProblem(f, y0, tspan)
sol = solve(prob)


plot(sol; label="")

#tsit5()

f(y,p,t) = -0.3*y

y0 = 1.0
tspan = (0.0, 20)

prob = ODEProblem(f, y0, tspan)
num_sol = solve(prob, Tsit5(), reltol=1e-8, abstol=1e-8)
plot(num_sol,
    linewidth=1,
    label="numerical")

#euler
function euler(ivp,n)
    # Time discretization.
    a,b = ivp.tspan
    h = (b-a)/n
    t = [ a + i*h for i in 0:n ]

    # Initial condition and output setup.
    u = fill(float(ivp.u0),n+1)

    # The time stepping iteration.
    for i in 1:n
        u[i+1] = u[i] + h*ivp.f(u[i],ivp.p,t[i])
    end
    return t,u
end

f(u,p,t) = -0.3*u;
tspan = (0.0,20.0);
u0 = 1.0;
ivp = ODEProblem(f,u0,tspan)

t,u = euler(ivp,20)

plot(t,u, xaxis="Time t", title="Euler's")

#rk

function f_pend(y, t)
    return -0.3*y
end
y0 = [1.0; 0.0]
span = (0.0, 20.0)

function rungekutta1(f, y0, t)
    n = length(t)
    y = zeros((n, length(y0)))
    y[1,:] = y0
    for i in 1:n-1
        h = t[i+1] - t[i]
        y[i+1,:] = y[i,:] + h * f(y[i,:], t[i])
    end
    return y
end

t = range(0,stop=20,length=101);
sol = rungekutta1(f_pend, y0,t);
plot(t, sol[:, 1], xaxis="Time t", title="Runge-Kutta 1")
