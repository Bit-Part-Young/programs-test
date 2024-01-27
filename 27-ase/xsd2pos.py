import sys

from ase.io.xsd import read_xsd
from pymatgen.io.ase import AseAtomsAdaptor


def xsd_to_pos(xsd_file: str):
    atoms = read_xsd(f"2-ms-format/{xsd_file}")
    # print(atoms)

    struct = AseAtomsAdaptor.get_structure(atoms)
    print(struct)

    struct.to(filename=f"1-vasp-format/{xsd_file[:-4]}.vasp", fmt="poscar")


if __name__ == "__main__":
    xsd_file = sys.argv[1]

    xsd_to_pos(xsd_file=xsd_file)
