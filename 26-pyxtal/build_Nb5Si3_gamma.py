from pyxtal import pyxtal
from pyxtal.lattice import Lattice

# gamma Nb5Si3
# pyxtal 中显示的 composition 有点问题，实际内容没问题
cell = Lattice.from_para(7.536, 7.536, 5.248, 90, 90, 120, ltype="hexagonal")
spg = 193
elements = ["Nb", "Nb", "Si"]
composition = [4, 6, 6]

sites = [
    [{"4d": [0.333, 0.667, 0.0]}],
    [{"6g": [0.2473, 0.0, 0.25]}],
    [{"6g": [0.6063, 0.0, 0.25]}],
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
structure_fn = "Nb5Si3_gamma.vasp"
structure.to_file(structure_fn, fmt="poscar")
