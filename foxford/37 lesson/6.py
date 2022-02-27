def f(x):
    a = 0
    b = 0
    while x > 0:
        y = x % 10
        if y > 3:
            a = a + 1
        if y < 8:
            b = b + 1
        x = x // 10
    return (a, b)

for x in range(10**5, 10**4, -1):
    if f(x)==(4, 3):
        print(x)
        break