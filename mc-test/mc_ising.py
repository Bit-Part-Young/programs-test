from time import time

import matplotlib.pyplot as plt
import numpy as np

mev = 1.6e-22
kB = 1.38e-23
j = 2
J = j * mev / kB
N = 30
mcna = 100000
mcnb = 200000
# square_lattice


def neb(n, x, y):
    l = x - 1
    r = x + 1
    u = y + 1
    d = y - 1
    if x == 0:
        l = n - 1
    if x == n - 1:
        r = 0
    if y == 0:
        d = n - 1
    if y == n - 1:
        u = 0
    return [(r, y), (l, y), (x, u), (x, d)]


def dE(N, S, x, y, J):
    de = 0
    for i, j in neb(N, x, y):
        de = de + 2 * J * S[x, y] * S[i, j]
    return de


def MCa(T, N):
    S = np.ones((N, N), dtype=int)
    for _ in range(mcna):
        x = np.random.randint(0, N)
        y = np.random.randint(0, N)
        de = dE(N, S, x, y, J)
        if de < 0:
            S[x, y] = -S[x, y]
        elif np.random.rand() < np.exp(-de / T):
            S[x, y] = -S[x, y]
    return S


def MCb(T, N):
    AvM = 0
    for _ in range(mcnb):
        x = np.random.randint(0, N)
        y = np.random.randint(0, N)
        de = dE(N, S, x, y, J)
        if de < 0:
            S[x, y] = -S[x, y]
        elif np.random.rand() < np.exp(-de / T):
            S[x, y] = -S[x, y]
        m = np.sum(S) / (N**2)
        AvM = AvM + np.abs(m)
    AvM = AvM / mcnb
    return AvM, S


tnum = 16
T = np.linspace(80, 20, tnum)
mm = []
t0 = time()
for i in range(tnum):
    if i == 0:
        S = MCa(T[i], N)
    m, S = MCb(T[i], N)
    mm.append(m)
t1 = time()
t = t1 - t0
print(t)  # master 140 s
plt.plot(T, mm, "v-.", c="blue", label="y1", markersize=12, linewidth=2)
plt.savefig("mc_ising_python.png")
