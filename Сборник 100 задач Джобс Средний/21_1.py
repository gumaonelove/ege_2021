def f(a, b, X, p):
    if a + b >= X and p==5: return True
    if a + b >= X and p != 5: return False
    if a + b < X and p == 5: return False
    if p%2==0:
        return f(a + 2, b, X, p + 1) or f(a * 2, b, X,  p + 1) or f(a, b * 2, X,  p + 1) or f(a, b + 2, X,  p + 1)
    else:
        return f(a + 2, b, X, p + 1) and f(a * 2, b, X, p + 1) and f(a, b * 2, X, p + 1) and f(a, b + 2, X, p + 1)



for X in range(1, 100):
    if f(8, 8, X, 1):
        print(X)

