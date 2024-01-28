from pyxtal import pyxtal
from pyxtal.lattice import Lattice

# TiB2
cell = Lattice.from_para(3.03, 3.03, 3.23, 90, 90, 120, ltype="hexagonal")
spg = 191
elements = ["Ti", "B"]
composition = [1, 2]

sites = [
    [{"1a": [0.0, 0.0, 0.0]}],
    [{"2d": [0.333, 0.667, 0.5]}],
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
structure_fn = "TiB2.vasp"
structure.to_file(structure_fn, fmt="poscar")
