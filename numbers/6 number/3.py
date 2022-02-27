def f(s):
    n=1
    while s<31:
        s+=3
        n*=2
    return n

for s in range(1, 100000):
    if f(s) == 128:
        print(s)
        break