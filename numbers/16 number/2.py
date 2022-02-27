def f(n):
    print(n)
    if n < 4:
        f(n + 1)
        f(n + 2)
        f(n + 3)

print(f(1))