"""Example to use get_symmetry_dataset with Wurtzite structure input (P6_3mc)."""
from spglib import get_symmetry_dataset

lattice = [[3.111, 0, 0], [-1.5555, 2.6942050311733885, 0], [0, 0, 4.988]]
position = [
    [1.0 / 3, 2.0 / 3, 0.0],
    [2.0 / 3, 1.0 / 3, 0.5],
    [1.0 / 3, 2.0 / 3, 0.6181],
    [2.0 / 3, 1.0 / 3, 0.1181],
]
types = [1, 1, 2, 2]
symprec = 1e-5

cell = (lattice, position, types)
dataset = get_symmetry_dataset(cell, symprec=symprec)

print(f'International symbol: {dataset["international"]} ({dataset["number"]})')
print(f'Hall symbol: {dataset["hall"]}')
print("Wyckoff letters: ", end="")
print(" ".join([f"{w}" for w in dataset["wyckoffs"]]))
print("Equivalent atoms:")
for i, equiv_atom in enumerate(dataset["equivalent_atoms"]):
    print(f"{i} -> {equiv_atom}")
print("Space group operations:")
for i, (r, t) in enumerate(zip(dataset["rotations"], dataset["translations"])):
    print(f"--- {i + 1} ---")
    for vec in r:
        print(f"{vec[0]:2d} {vec[1]:2d} {vec[2]:2d}")
    print(f"{t[0]:.5f} {t[1]:.5f} {t[2]:.5f}")


# output:
"""
International symbol: P6_3mc (186)
Hall symbol: P 6c -2c
Wyckoff letters: b b b b
Equivalent atoms:
0 -> 0
1 -> 0
2 -> 2
3 -> 2
Space group operations:
--- 1 ---
 1  0  0
 0  1  0
 0  0  1
0.00000 0.00000 0.00000
--- 2 ---
 1 -1  0
 1  0  0
 0  0  1
0.00000 -0.00000 0.50000
--- 3 ---
 0 -1  0
 1 -1  0
 0  0  1
0.00000 -0.00000 0.00000
--- 4 ---
-1  0  0
 0 -1  0
 0  0  1
0.00000 0.00000 0.50000
--- 5 ---
-1  1  0
-1  0  0
 0  0  1
0.00000 0.00000 0.00000
--- 6 ---
 0  1  0
-1  1  0
 0  0  1
0.00000 0.00000 0.50000
--- 7 ---
 0  1  0
 1  0  0
 0  0  1
0.00000 -0.00000 0.50000
--- 8 ---
 1  0  0
 1 -1  0
 0  0  1
0.00000 -0.00000 0.00000
--- 9 ---
 1 -1  0
 0 -1  0
 0  0  1
0.00000 0.00000 0.50000
--- 10 ---
 0 -1  0
-1  0  0
 0  0  1
0.00000 0.00000 0.00000
--- 11 ---
-1  0  0
-1  1  0
 0  0  1
0.00000 0.00000 0.50000
--- 12 ---
-1  1  0
 0  1  0
 0  0  1
0.00000 0.00000 0.00000
"""
