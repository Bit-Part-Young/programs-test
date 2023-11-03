# Import pylibxc and numpy
import numpy as np
import pylibxc

# Build functional
func = pylibxc.LibXCFunctional("gga_c_pbe", "unpolarized")

# Create input
inp = {}
inp["rho"] = np.random.random((3))
inp["sigma"] = np.random.random((3))

# Compute
ret = func.compute(inp)
for k, v in ret.items():
    print(k, v)


# output
"""
zk [[-0.00088269]
 [-0.063585  ]
 [-0.06505307]]
vrho [[-0.00506666]
 [-0.08236324]
 [-0.08354652]]
vsigma [[0.00047753]
 [0.00557631]
 [0.0045402 ]]
"""
