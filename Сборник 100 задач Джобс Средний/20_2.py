def f(a, b, p):
    if a+b>=57 and p==4: return True
    if a + b >= 57 and p != 4: return False
    if a + b < 57 and p == 4: return False
    if p%2==1:
        return f(a+b, b, p+1) or f(a, a+b, p+1)
    else:
        return f(a + b, b, p + 1) and f(a, a + b, p + 1)
W = []
for b in range(1, 100):
    if f(9, b, 1):
        W.append(b)

print(min(W), max(W))
