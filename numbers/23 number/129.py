def f(a, b):
    if a == b: return 1
    if a > b: return 0
    return f(a+3, b) + f(a+2, b) + f(int(str(a)+'1'), b)


print(f(3, 12)*f(12, 25))