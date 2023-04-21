# REF: https://perso.crans.org/besson/publis/notebooks/Runge-Kutta_methods_for_ODE_integration_in_Julia.html

function func1(y, t)
    return -0.3*y
end
function func2(y, t)
    return 3.0*exp(-t)
end
function func3(y, t)
    return -(t-1)*y/2
end
function func4(y, t)
    return (t^2)+y
end
function func5(y, t)
    return (t^2 - y^2)/(t^2 + y^2)
end
function func6(y, t)
    return y*(1-y)
end
function func7(y,t)
    return 2*t + (y/t)
end
function func8(y,t)
    return sqrt(t^2 + y^2)
end
function func9(y,t)
    return sin(y) * exp(t)
end
function func10(y,t)
    return sin(t) + cos(y)
end

function rungekutta2(f, y, t)
    for i in 1:length(t)-1
        h = t[i+1] - t[i]
        y[i+1] = y[i] + h * f(y[i] + f(y[i], t[i]) * h/2, t[i] + h/2)
    end
    return y
end