"""ASE io 模块 文件格式转换 测试"""

from ase.io import read, write
from ase.io.extxyz import write_xyz
from ase.io.lammpsdata import write_lammps_data
from ase.io.vasp import read_vasp, write_vasp

struct_fn = "Nb5Si3_alpha.vasp"
struct = read(filename=struct_fn, format="vasp")

output_vasp_fn = "POSCAR"
write_vasp(filename=output_vasp_fn, atoms=struct, direct=True, sort=True)

output_xyz_fn = "Nb5Si3_alpha.xyz"
output_extxyz_fn = "Nb5Si3_alpha_ext.xyz"
write(filename=output_xyz_fn, images=struct, format="xyz")
write(filename=output_extxyz_fn, images=struct, format="extxyz")
write_xyz(fileobj=output_extxyz_fn, images=struct)

output_lammps_data_fn = "Nb5Si3_alpha.lammps-data"
write_lammps_data(
    file=output_lammps_data_fn,
    atoms=struct,
    units="metal",
    atom_style="atomic",
)
