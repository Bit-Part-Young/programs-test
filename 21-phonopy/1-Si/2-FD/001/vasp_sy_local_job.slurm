#!/bin/bash

#SBATCH -J vasp
#SBATCH -p 64c512g
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH -o %j.out
#SBATCH -e %j.err

module purge

module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0

ulimit -s unlimited

export OMP_NUM_THREADS=1
export I_MPI_ADJUST_REDUCE=3

mpirun $HOME/yangsl/bin/vasp_std
