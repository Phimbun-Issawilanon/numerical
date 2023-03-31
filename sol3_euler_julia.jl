# REF: https://docs.juliahub.com/CalculusWithJulia/AZHbv/0.0.5/ODEs/euler.html

using Plots

x0, y0 = 0, 1
F(y,x) = -(x-1)*y/2 

# create array of x
start_x = x0
stop_x = 1.1
num = 12
h = (stop_x-start_x)/(num-1)
xs = zeros(num)
ys = zeros(num)

xs[1] = x0   # index is off by 1
ys[1] = y0

for i in 1:num-1
  xs[i + 1] = xs[i] + h
  ys[i + 1] = ys[i] + h * F(ys[i], xs[i])
end

plot(xs, ys)
savefig("sol3_euler_julia")