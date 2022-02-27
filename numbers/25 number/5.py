from math import isqrt
a, b = 35_000_000, 40_000_000
#a, b = 63_000_000, 75_000_000


def prime(n):
    if n<=2: return True
    elif n%2==0: return False
    d = 3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True


def fast(n):
    while n%2==0: n //= 2
    if n == 1: return 0
    x = isqrt(isqrt(n))
    if x**4 == n and prime(x): return (n, x)
    return 0



for n in range(a, b+1):
    F = fast(n)
    if F!=0: print(n, F)



