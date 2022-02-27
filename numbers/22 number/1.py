def f(x):
    a = 0
    b = 0
    while x > 0:
        c = x % 10
        a += c
        if c > b:
            b = c
        x //= 10
    return (a,b)

for x in range(0, 100):
    if f(x) == (11,7):
        print(x)
        break