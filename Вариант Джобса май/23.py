def f(a, b):
    if a == b: return 1
    if a > b: return 0

    k = f(a+1, b) + f(a*2, b)
    if a%2==0:
        k += f(a+1, b)
    if a%2==1:
        k += f(a+2, b)

    return k


print(f(3, 9)*f(9, 17)*f(17, 25))