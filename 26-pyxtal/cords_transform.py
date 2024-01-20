import numpy as np

basis = np.array(
    [[10.224, 0.000, 0.000], [0.000, 10.224, 0.000], [0.000, 0.000, 5.189]]
)

direct = np.array(
    [
        [0.1653000000000002, 0.6524999999999999, 0.7185000000000001],
        [0.3346999999999998, -0.1524999999999999, 0.7185000000000001],
        [-0.6524999999999999, 0.6653000000000002, 1.2185000000000001],
    ]
)

cartesian: np.ndarray = np.dot(direct, basis)
print(cartesian)

direct_new = np.linalg.solve(basis, cartesian.T).T
print(direct_new)
