def pseudo_list():
    for i in range(N):
        yield (i*9876+1024)%1000
N = 10**6 + 1
A = list(pseudo_list())
A.sort()
print(A[len(A)//2])