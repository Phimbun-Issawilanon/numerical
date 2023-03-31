# REF: https://docs.juliahub.com/CalculusWithJulia/AZHbv/0.0.5/ODEs/euler.html

using Plots

function function_1(y, t)
    k = 0.1
    return -k*y
end

function function_2(y, t)
    return 3*exp(-t)
end

function function_3(y, t)
    return -(t-1)*y/2
end

# Define parameters
num = 200
t0,tend = 0, 20
h = (tend-t0)/(num-1)
ts = zeros(num)

y0 = 1
ys = zeros(num)

ts[1] = t0
ys[1] = y0

function explicit_euler(F, ts, ys, h)
    for i in 1:num-1
        ts[i + 1] = ts[i] + h
        ys[i + 1] = ys[i] + h * F(ys[i], ts[i])
    end
end

function plot_graph(ts, ys)
    plot(ts, ys)
    savefig("sol_euler_julia")
end

explicit_euler(function_1, ts, ys, h)
plot_graph(ts, ys)