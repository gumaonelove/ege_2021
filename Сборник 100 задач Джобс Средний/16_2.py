A = [None]*10**7

def f(n):
    if n<5: return n%3
    if A[n-2]!=None:
        r = A[n-2]
    else:
        r = f(n-2)
        A[n-2] = r

    if n%2==0: return 2*r+2*n
    else: return r + n%4

for n in range(10**4):
    if f(n)<=1500: print(n)