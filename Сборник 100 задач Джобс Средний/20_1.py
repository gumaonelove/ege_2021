def f(a, b, X, p):
    if a + b >= X and p == 4: return True
    if a + b >= X and p != 4: return False
    if a + b < X and p == 4: return False
    if p%2==1:
        return f(a + 2, b, X, p + 1) or f(a * 2, b, X,  p + 1) or f(a, b * 2, X,  p + 1) or f(a, b + 2, X,  p + 1)
    else:
        return f(a + 2, b, X, p + 1) and f(a * 2, b, X, p + 1) and f(a, b * 2, X, p + 1) and f(a, b + 2, X, p + 1)

count = 0
for X in range(1, 1000):
    if f(10, 15, X, 1):
        count += 1

print(count)

