from random import random
from time import time

import numpy as np

t0 = time()
N = 10000000
nc = 0
for i in range(N):
    x, y = random(), random()
    if np.hypot(x, y) < 1:
        nc = nc + 1
pi_estimate = nc / N * 4
t1 = time()
t = t1 - t0
print(pi_estimate, "\t", t)
