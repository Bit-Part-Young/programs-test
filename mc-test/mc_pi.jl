function estimate_pi(N::Int)
    nc = 0
    for _ in 1:N
        x, y = rand(), rand()
        if hypot(x, y) < 1
            nc += 1
        end
    end
    return nc / N * 4
end

t0 = time()
N = 10000000
pi_estimate = estimate_pi(N)
t1 = time()

println(pi_estimate, "\t", t1 - t0)
