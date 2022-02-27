def f(a, b, p):
    if a+b>=57 and p==5: return True
    if a + b >= 57 and p != 5: return False
    if a + b < 57 and p == 5: return False
    if p%2==0:
        return f(a+b, b, p+1) or f(a, a+b, p+1)
    else:
        return f(a + b, b, p + 1) and f(a, a + b, p + 1)

for b in range(1, 100):
    if f(b, b, 1):
        print(b)
        break

