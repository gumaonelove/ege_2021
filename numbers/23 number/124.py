def f(a, b):
    if a == b: return 1
    if a > b: return 0
    if b == 32: return 0
    k = f(a, b-3)
    if b%2==0: k+=f(a, b//2)
    return k

print(f(1, 16)*f(16, 41))