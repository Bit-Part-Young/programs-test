"""
VASP OUTCAR 文件转换为 extxyz 文件 测试
可获取 OUTCAR 中的所有离子步构型的原子位置、能量、受力、应力等信息
"""

# reference: https://gist.github.com/simonbatzner/c2b05d38789b67f6fe5d3c75a4f2223d
from ase.io import read, write

vasp_out_fn = "./OUTCAR"
extxyz_fn = "outcar.xyz"

all_confs = read(filename=vasp_out_fn, format="vasp-out", index=":")
print(len(all_confs))

write(filename=extxyz_fn, images=all_confs, format="extxyz", append=True)

"""
# output:
45
"""
