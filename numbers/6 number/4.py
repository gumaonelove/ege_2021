def f(s):
    n = 11
    while s < 224:
        s = s + 15
        n = n + 8
    return(n)

for s in range(1, 100000):
    if f(s) == 115:
        print(s)
        break