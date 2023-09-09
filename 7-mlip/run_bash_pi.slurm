#!/bin/bash

#SBATCH -J bash
#SBATCH -p small
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -o %j.out
#SBATCH -e %j.err

module purge

module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load intel-oneapi-tbb/2021.4.0

./install.sh ../mylammps intel_cpu_intelmpi

