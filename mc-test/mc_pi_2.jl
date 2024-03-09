N = 10000000

@time begin
    nc = count(x -> hypot(rand(), rand()) < 1, 1:N)
end

pi_estimate = nc / N * 4
println(pi_estimate)