def f(a, b, p):
    if a+b>=57 and p==3: return True
    if a + b >= 57 and p != 3: return False
    if a + b < 57 and p == 3: return False
    return f(a+b, b, p+1) or f(a, a+b, p+1)

for b in range(1, 100):
    if f(10, b, 1):
        print(b)
        break