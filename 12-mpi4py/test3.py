import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# passing MPI datatypes explicitly
if rank == 0:
    data = numpy.arange(10, dtype="i")
    comm.Send([data, MPI.INT], dest=1, tag=77)
    print(f"process {rank} send buffer-like array {data}...")
elif rank == 1:
    data = numpy.empty(10, dtype="i")
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print(f"process {rank} recv buffer-like array {data}...")


# result:
# process 0 send buffer-like array [0 1 2 3 4 5 6 7 8 9]...
# process 1 recv buffer-like array [0 1 2 3 4 5 6 7 8 9]...
