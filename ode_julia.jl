#ODE.jl
#ode45
using ODE

function func1(y, p, t)
    return -0.3*y
end
function func2(y, p, t)
    return 3.0*exp(-t)
end
function func3(y, p, t)
    return -(t-1)*y/2
end
function func4(y, p, t)
    return (t^2)+y
end
function func5(y, p, t)
    return (t^2 - y^2)/(t^2 + y^2)
end
function func6(y, p, t)
    return y*(1-y)
end
function func7(y, p, t)
    return 2*t + (y/t)
end
function func8(y, p, t)
    return sqrt(t^2 + y^2)
end
function func9(y, p, t)
    return sin(y) * exp(t)
end
function func10(y, p, t)
    return sin(t) + cos(y)
end

function ode_45(f, y, t)
    y0 = y[1]
    tstart = t[1]
    tstop = t[length(y)]
    tstep = t[2] - t[1]
    tspan = (t[1],t[length(y)])
    prob = ODEProblem(f, y0, tspan)
    sol = solve(prob, ode45(), reltol=1e-8, abstol=1e-8, saveat=tstart:tstep:tstop)
    return sol
end

function ode_23(f, y, t)
    y0 = y[1]
    tstart = t[1]
    tstop = t[length(y)]
    tstep = t[2] - t[1]
    tspan = (t[1],t[length(y)])
    prob = ODEProblem(f, y0, tspan)
    sol = solve(prob, ode23(), reltol=1e-8, abstol=1e-8, saveat=tstart:tstep:tstop)
    return sol
end
