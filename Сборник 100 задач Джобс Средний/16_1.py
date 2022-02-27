A = [0, 5] + [None]*100
def f(n):
    if n==1: return 5
    if A[n-1]!=None: r = A[n-1]
    else:
        r = f(n-1)
        A[n-1] = r
    if r%2==0: return r + n//2
    else: return r+n*n-1

print(f(40))