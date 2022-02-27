def f(a, b):
    if a==b: return 1
    if a>b or b== 10: return 0
    k=f(a, b-1)
    if b%2==0: k+=f(a, b//2)
    return k
print(f(1, 25)*f(25, 28))
