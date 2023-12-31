"""Atoms object 常用 method 和 attribute 测试"""

from ase.io import read

struct_fn = "Nb5Si3_alpha.vasp"
struct = read(filename=struct_fn, format="vasp")

print("Total number of atoms:")
print(len(struct))
print(struct.get_global_number_of_atoms())
print("---" * 25)

print("Atomic symbols:")
print(list(struct.symbols))
print(struct.get_chemical_symbols())
print("---" * 25)

print("Chemical formula:")
print(struct.symbols)
print(struct.get_chemical_formula())
print("---" * 25)

print("Atomic numbers:")
print(struct.numbers)
print(struct.get_atomic_numbers())
print("---" * 25)

print("Structure cell:")
print(struct.cell)
print(struct.get_cell())
print("---" * 25)

print("Structure cell parameters:")
print(struct.cell.cellpar())
# deprecated 写法
# print(struct.get_cell_lengths_and_angles())
print("---" * 25)

print("Structure volume:")
print(struct.get_volume())
print("---" * 25)

print("Structure mass:")
print(struct.get_masses())
print("---" * 25)

print("Structure positions:")
print(struct.positions)
print(struct.get_positions())
print("---" * 25)

print("Structure pbc condition:")
print(struct.pbc)
print(struct.get_pbc())
print("---" * 25)

print(struct.todict())


"""
# 以下 method 需要设置 calculator
struct.get_potential_energy()
struct.get_potential_energies()
struct.get_total_energy()
struct.get_properties()
struct.get_forces()
struct.get_stress()
struct.get_stresses()
"""


"""
# output:
Total number of atoms:
32
32
---------------------------------------------------------------------------
Atomic symbols:
['Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si']
['Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Nb', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si', 'Si']
---------------------------------------------------------------------------
Chemical formula:
Nb20Si12
Nb20Si12
---------------------------------------------------------------------------
Atomic numbers:
[41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 14 14 14 14
 14 14 14 14 14 14 14 14]
[41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 14 14 14 14
 14 14 14 14 14 14 14 14]
---------------------------------------------------------------------------
Structure cell:
Cell([6.57, 6.57, 11.88])
Cell([6.57, 6.57, 11.88])
---------------------------------------------------------------------------
Structure cell parameters:
[ 6.57  6.57 11.88 90.   90.   90.  ]
---------------------------------------------------------------------------
Structure volume:
512.799012
---------------------------------------------------------------------------
Structure mass:
[92.90637 92.90637 92.90637 92.90637 92.90637 92.90637 92.90637 92.90637
 92.90637 92.90637 92.90637 92.90637 92.90637 92.90637 92.90637 92.90637
 92.90637 92.90637 92.90637 92.90637 28.085   28.085   28.085   28.085
 28.085   28.085   28.085   28.085   28.085   28.085   28.085   28.085  ]
---------------------------------------------------------------------------
Structure positions:
[[ 1.09062  4.37562 10.098  ]
 [ 2.19438  1.09062 10.098  ]
 [ 5.47938  4.37562  7.722  ]
 [ 4.37562  5.47938  1.782  ]
 [ 1.09062  2.19438  4.158  ]
 [ 2.19438  1.09062  1.782  ]
 [ 5.47938  2.19438  1.782  ]
 [ 1.09062  4.37562  1.782  ]
 [ 4.37562  1.09062  4.158  ]
 [ 5.47938  4.37562  4.158  ]
 [ 2.19438  5.47938  4.158  ]
 [ 5.47938  2.19438 10.098  ]
 [ 4.37562  5.47938 10.098  ]
 [ 2.19438  5.47938  7.722  ]
 [ 1.09062  2.19438  7.722  ]
 [ 4.37562  1.09062  7.722  ]
 [ 0.       0.       0.     ]
 [ 0.       0.       5.94   ]
 [ 3.285    3.285    0.     ]
 [ 3.285    3.285    5.94   ]
 [ 4.10625  0.82125  0.     ]
 [ 5.74875  4.10625  0.     ]
 [ 2.46375  0.82125  5.94   ]
 [ 0.82125  2.46375  0.     ]
 [ 4.10625  5.74875  5.94   ]
 [ 2.46375  5.74875  0.     ]
 [ 0.82125  4.10625  5.94   ]
 [ 5.74875  2.46375  5.94   ]
 [ 0.       0.       8.91   ]
 [ 0.       0.       2.97   ]
 [ 3.285    3.285    2.97   ]
 [ 3.285    3.285    8.91   ]]
---------------------------------------------------------------------------
Structure pbc condition:
[ True  True  True]
[ True  True  True]
---------------------------------------------------------------------------
{'numbers': array([41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41,
       41, 41, 41, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]), 'positions': array([[ 1.09062,  4.37562, 10.098  ],
       [ 2.19438,  1.09062, 10.098  ],
       [ 5.47938,  4.37562,  7.722  ],
       [ 4.37562,  5.47938,  1.782  ],
       [ 1.09062,  2.19438,  4.158  ],
       [ 2.19438,  1.09062,  1.782  ],
       [ 5.47938,  2.19438,  1.782  ],
       [ 1.09062,  4.37562,  1.782  ],
       [ 4.37562,  1.09062,  4.158  ],
       [ 5.47938,  4.37562,  4.158  ],
       [ 2.19438,  5.47938,  4.158  ],
       [ 5.47938,  2.19438, 10.098  ],
       [ 4.37562,  5.47938, 10.098  ],
       [ 2.19438,  5.47938,  7.722  ],
       [ 1.09062,  2.19438,  7.722  ],
       [ 4.37562,  1.09062,  7.722  ],
       [ 0.     ,  0.     ,  0.     ],
       [ 0.     ,  0.     ,  5.94   ],
       [ 3.285  ,  3.285  ,  0.     ],
       [ 3.285  ,  3.285  ,  5.94   ],
       [ 4.10625,  0.82125,  0.     ],
       [ 5.74875,  4.10625,  0.     ],
       [ 2.46375,  0.82125,  5.94   ],
       [ 0.82125,  2.46375,  0.     ],
       [ 4.10625,  5.74875,  5.94   ],
       [ 2.46375,  5.74875,  0.     ],
       [ 0.82125,  4.10625,  5.94   ],
       [ 5.74875,  2.46375,  5.94   ],
       [ 0.     ,  0.     ,  8.91   ],
       [ 0.     ,  0.     ,  2.97   ],
       [ 3.285  ,  3.285  ,  2.97   ],
       [ 3.285  ,  3.285  ,  8.91   ]]), 'cell': array([[ 6.57,  0.  ,  0.  ],
       [ 0.  ,  6.57,  0.  ],
       [ 0.  ,  0.  , 11.88]]), 'pbc': array([ True,  True,  True])}
"""
