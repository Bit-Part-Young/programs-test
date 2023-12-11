"""ASE 简单 bulk 模型构建测试"""

from ase.build import bulk
from ase.io import write

# 原胞
primCell = bulk(name="Al", crystalstructure="fcc", a=4.05)
# 单胞
unitCell = bulk(name="Al", crystalstructure="fcc", a=4.05, cubic=True)
# 超胞
superCell = unitCell * (2, 2, 2)
# 构型原子数
print(len(primCell))
print(superCell.get_global_number_of_atoms())

# 保存成 VASP 格式文件
write(filename="Al222.vasp", images=superCell, format="vasp", direct=True)

"""
# output:
1
32
"""
