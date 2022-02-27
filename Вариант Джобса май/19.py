def f(x, y, p):
    if x + y >= 45: return p==3
    if x+y<45 and p==3: return False
    return f(x, x+y, p+1) or f(x+y, y, p+1)


for y in range(1, 10000000000000):
    if f(7, y, 1):
        print(y)
        break