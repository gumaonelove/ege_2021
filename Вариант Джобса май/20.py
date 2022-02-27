def f(x, y, p):
    if x + y >= 45: return p==4
    if x+y<45 and p==4: return False
    if p%2==1:
        return f(x, x+y, p+1) or f(x+y, y, p+1)
    else:
        return f(x, x+y, p+1) and f(x+y, y, p+1)

for y in range(1, 100):
    if f(6, y, 1):
        print(y)