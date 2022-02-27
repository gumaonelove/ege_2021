def f(a, b):
    if a ==b:
        return 1
    if a>b:
        return 0
    k = f(a, b-1)
    if b == 18:
        return 0
    if b % 2 ==0:
        k+= f(a, b//2)
    if b % 3 == 0:
        k+= f(a, b//3)
    return k

print(f(1,12)*f(12,39))