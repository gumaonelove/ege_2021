A = [1, 3] + [0]*50
for n in range(2, 50):
    A[n] = A[n-1] - A[n-2] + 3*n
print(A[40])


def f(n):
    if n==0: return 1
    if n==1: return 3
    return f(n-1) + f(n-2) + 3*n


print(f(40))