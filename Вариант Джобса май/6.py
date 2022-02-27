def f(s):
    n = 1
    while s > n:
        s = s - 15
        n = n * 5
    return(n)

count = 0
for s in range (0, 10000):

    if f(s) == 125:
        count += 1

print(count)