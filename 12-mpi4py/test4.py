"""广播"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = list(range(10))
    print(f"process {rank} bcast data {data} to other processes")
else:
    data = None
data = comm.bcast(data, root=0)

print(f"process {rank} recv {data}...")

# result:
# process 0 bcast data [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] to other processes
# process 0 recv [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]...
# process 1 recv [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]...
# process 2 recv [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]...
# process 3 recv [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]...
# process 4 recv [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]...
