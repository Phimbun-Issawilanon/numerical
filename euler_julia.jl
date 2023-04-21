# REF: https://docs.juliahub.com/CalculusWithJulia/AZHbv/0.0.5/ODEs/euler.html

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

function explicit_euler(F, ys, ts)
    for i in 1:length(ts)-1
        ys[i + 1] = ys[i] + (ts[i + 1] - ts[i]) * F(ys[i], ts[i])
    end
    return ys
end