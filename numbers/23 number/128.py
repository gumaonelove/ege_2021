def f(a, b):
    if a == b: return 1
    if a > b: return 0
    if a == 43: return 0
    return f(a+2, b) + f(a+a+1, b) + f(a+a-1, b)

print(f(7, 63))