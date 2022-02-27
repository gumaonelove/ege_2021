def f(x):
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 10)
        x = x // 10
    return (a, b)


for x in range(10**4, 1, -1):
    if f(x) == (3, 7):
        print(x)
        break