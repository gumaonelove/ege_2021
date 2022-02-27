def f(x):
    L, M = 0, 0
    while x > 0:
        L += 1
        if x % 16 % 2 == 0:
            M += 1
        else:
            M -= 1
        x //= 16
    return (L, M)

count = 0
x = 8
for x in range(10**x, 10**(x+1)):
    if f(x) == (6, 0): count += 1

print(count)


# 2799744 (10^6 10^7)
# 2115456 (10^7 10^8)
