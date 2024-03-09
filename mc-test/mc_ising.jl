t0 = time()
mev = 1.6e-22
kB = 1.38e-23
j = 2
J = j * mev / kB

N = 30
mcna = 100000
mcnb = 200000
#square_lattice

function neb(n, x, y)
    l = x - 1
    r = x + 1
    u = y + 1
    d = y - 1
    if x == 1
        l = n
    end
    if x == n
        r = 1
    end
    if y == 1
        d = n
    end
    if y == n
        u = 1
    end
    return [(r, y), (l, y), (x, u), (x, d)]
end


function dE(N, S, x, y, J)
    de = 0
    for (i, j) in neb(N, x, y)
        de = de + 2 * J * S[x, y] * S[i, j]
    end
    return de
end


function MCa(T, N)
    S = ones(N, N)
    for _ in 1:mcna
        x, y, r = rand(1:N), rand(1:N), rand()
        de = dE(N, S, x, y, J)
        if de < 0
            S[x, y] = -S[x, y]
        elseif r < exp(-de / T)
            S[x, y] = -S[x, y]
        else
            S[x, y] = S[x, y]
        end
    end
    return S
end


function MCb(T, N)
    AvM = 0
    S = ones(N, N)
    for _ in 1:mcnb
        x, y, r = rand(1:N), rand(1:N), rand()
        de = dE(N, S, x, y, J)
        if de < 0
            S[x, y] = -S[x, y]
        elseif r < exp(-de / T)
            S[x, y] = -S[x, y]
        end
        m = sum(S) / (N * N)
        AvM = AvM + abs(m)
    end
    AvM = AvM / mcnb
    return AvM, S
end

t0 = time()
tnum = 16
T = LinRange(80, 20, tnum)
mm = []

for i in 1:tnum
    if i == 0
        S = MCa(T[i], N)
    end
    m, S = MCb(T[i], N)
    append!(mm, m)
end
t1 = time()
t = t1 - t0
println(t)  # master 3~4 s

# using PyPlot
# grid("on")

# plot(T, mm)