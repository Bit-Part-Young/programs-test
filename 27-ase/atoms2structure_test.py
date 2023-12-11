"""ASE Atoms object 与 pymatgen Structure object 互相转换 测试"""

from ase.build import bulk
from pymatgen.core.structure import Structure
from pymatgen.io.ase import AseAtomsAdaptor

atoms = bulk("Fe", "bcc", a=2.83, cubic=True)
structure = AseAtomsAdaptor.get_structure(atoms)

print("ASE Atoms object transfer to pymatgen Structure object:\n")
print(atoms)
print("---" * 20)
print(structure)
print("\n" + "---" * 20 + "\n")

print("pymatgen Structure object transfer to ASE Atoms object :\n")
structure_pmg = Structure.from_prototype(prototype="fcc", species=["Al"], a=4.05)
structure_ase = AseAtomsAdaptor.get_atoms(structure_pmg)

print(structure_pmg)
print("---" * 20)
print(structure_ase)


"""
# output:
ASE Atoms object transfer to pymatgen Structure object:

Atoms(symbols='Fe2', pbc=True, cell=[2.83, 2.83, 2.83])
------------------------------------------------------------
Full Formula (Fe2)
Reduced Formula: Fe
abc   :   2.830000   2.830000   2.830000
angles:  90.000000  90.000000  90.000000
pbc   :       True       True       True
Sites (2)
  #  SP      a    b    c
---  ----  ---  ---  ---
  0  Fe    0    0    0
  1  Fe    0.5  0.5  0.5

------------------------------------------------------------

pymatgen Structure object transfer to ASE Atoms object :

Full Formula (Al4)
Reduced Formula: Al
abc   :   4.050000   4.050000   4.050000
angles:  90.000000  90.000000  90.000000
pbc   :       True       True       True
Sites (4)
  #  SP      a    b    c
---  ----  ---  ---  ---
  0  Al    0    0    0
  1  Al    0.5  0.5  0
  2  Al    0.5  0    0.5
  3  Al    0    0.5  0.5
------------------------------------------------------------
Atoms(symbols='Al4', pbc=True, cell=[4.05, 4.05, 4.05])
"""
