M_size=int(input())
M=set(map(int,input().split()))
N_size=int(input())
N=set(map(int,input().split()))
O=set()
M,N=M.difference(N),N.difference(M)
O.update(M,N)
O=sorted(O)
for i in O:
    print(i)
