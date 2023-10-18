from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {"a": 7, "b": 3.14}
    comm.isend(data, dest=1, tag=11)
    print(f"process {rank} send {data}...")
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    # data = comm.irecv(source=0, tag=11)
    print(f"process {rank} recv {data}...")


# result:
# comm.recv()
# process 0 send {'a': 7, 'b': 3.14}...
# process 1 recv {'a': 7, 'b': 3.14}...

# comm.irecv()
# process 1 recv <mpi4py.MPI.Request object at 0x7f56c6812a80>...
# process 0 send {'a': 7, 'b': 3.14}...
