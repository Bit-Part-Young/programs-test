from ase import Atoms

d = 1.10
molecule = Atoms(["N", "N"], positions=[(0.0, 0.0, 0.0), (0.0, 0.0, d)])

print(molecule)
