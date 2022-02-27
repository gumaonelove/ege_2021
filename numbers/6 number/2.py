
def f(d):
    n = 1
    s = 32
    while s <= 2019:
        s += d
        n += 3
    return (n)

for d in range(1, 1000):
    print(d, f(d))
    if f(d)==88:
        print(d)
        break