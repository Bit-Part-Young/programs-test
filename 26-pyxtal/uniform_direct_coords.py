import sys

import numpy as np
from ase.io.vasp import read_vasp, write_vasp
from pymatgen.core.structure import Structure


def uniform_direct_coords(structure_fn: str):
    structure = read_vasp(structure_fn)
    # scale_positions 坐标值范围在 0-1 之间
    scale_positions = structure.get_scaled_positions()

    structure.set_scaled_positions(scale_positions)
    write_vasp(structure_fn, structure, direct=True, sort=False)

    print("The direct coordinates range have been uniformed to 0-1.")


if __name__ == "__main__":
    strcutre_fn = sys.argv[1]
    uniform_direct_coords(sys.argv[1])
