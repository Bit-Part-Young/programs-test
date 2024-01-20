from ase import Atoms

a = 5.387
crystal = Atoms(
    "Zn4S4",
    scaled_positions=[
        [0.0, 0.0, 0.0],
        [0.0, 0.5, 0.5],
        [0.5, 0.0, 0.5],
        [0.5, 0.5, 0.0],
        [0.25, 0.75, 0.75],
        [0.25, 0.25, 0.25],
        [0.75, 0.75, 0.25],
        [0.75, 0.25, 0.75],
    ],
    cell=[a, a, a],
    pbc=True,
)

print(crystal)
print(crystal.info)
