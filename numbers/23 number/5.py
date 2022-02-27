def f(s, f):
    if s == f :
        return 1
    if s > f:
        return 0

    k = f(s, f-2) + f(s, f-3)
    
    if f % 2 == 0:
        k+= f(s, f//2)

    return k

print()