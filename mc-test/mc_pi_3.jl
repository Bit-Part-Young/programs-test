N = 10000000

@time begin
    nc = count(_ -> begin
        x, y = rand(), rand()
        hypot(x, y) < 1
    end, 1:N)
end

pi_estimate = nc / N * 4
println(pi_estimate)
