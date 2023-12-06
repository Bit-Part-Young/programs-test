
import matscipy.dislocation as sd

#from mpi4py import MPI
from ase.calculators.lammpslib import LAMMPSlib
from ase.optimize import FIRE
from ase.neb import NEB, NEBOptimizer
from ase.calculators.singlepoint import SinglePointCalculator
from ase.io import write, read
from ase.constraints import FixAtoms

import numpy as np

pot_path = "w_eam4.fs"
calculator = LAMMPSlib(lmpcmds=["pair_style eam/fs",
                           "pair_coeff * * %s W" % pot_path],
                           atom_types={'W': 1}, keep_alive=True)

disloc_ini, disloc_fin, _ = sd.make_barrier_configurations(calculator=calculator, hard_core=True)

disloc_ini.calc = calculator
disloc_fin.calc = calculator
fmax_relaxation = 1.0e-3
fmax_neb = 0.025
for index, disloc in enumerate(disloc_ini, disloc_fin):
    opt = FIRE(disloc)
    opt.run(fmax=fmax_relaxation)
n_knots = 5

np.testing.assert_almost_equal(disloc_ini.get_potential_energy(),
                               disloc_fin.get_potential_energy(),
                               decimal=3)

images = [disloc_ini] + \
         [disloc_ini.copy() for i in range(n_knots)] + \
         [disloc_fin]

for image in images:
    image.calc = calculator
glide_neb = NEB(images, allow_shared_calculator=True,
                        method="aseneb")
glide_neb.interpolate(apply_constraint=False)
opt = FIRE(glide_neb)
opt.run(fmax=fmax_neb, steps=250)

for image in glide_neb.images:
    energy = image.get_potential_energy()
    forces = image.get_forces()
    image.calc = SinglePointCalculator(image, energy=energy, forces=forces)

write("neb.xyz", glide_neb.images)
