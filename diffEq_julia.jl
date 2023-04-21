using DifferentialEquations

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

function differentialEquation(f, y, t)
    y0 = y[1]
    tstart = t[1]
    tstop = t[length(y)]
    tstep = t[2] - t[1]
    tspan = (tstart,tstop)
    prob = ODEProblem(f, y0, tspan)
    sol = solve(prob, saveat = tstart:tstep:tstop)
    return sol
end
