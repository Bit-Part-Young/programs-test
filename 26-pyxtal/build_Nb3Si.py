from pyxtal import pyxtal
from pyxtal.lattice import Lattice

# Nb3Si
cell = Lattice.from_para(10.224, 10.224, 5.189, 90, 90, 90, ltype="tetragonal")
spg = 86
elements = ["Nb", "Nb", "Nb", "Si"]
composition = [8, 8, 8, 8]

sites = [
    [{"8g": [0.1653, 0.6525, 0.7185]}],
    [{"8g": [0.1043, 0.2665, 0.5230]}],
    [{"8g": [0.0603, 0.5364, 0.2370]}],
    [{"8g": [0.0442, 0.2782, 0.0293]}],
]

structure = pyxtal()
structure.build(
    group=spg, species=elements, numIons=composition, lattice=cell, sites=sites
)

structure_pmg = structure.to_pymatgen()
structure_ase = structure.to_ase()

print(structure)
print("---" * 25)
print(structure_pmg)

structure_fn = "Nb3Si.vasp"
structure.to_file(structure_fn, fmt="poscar")
