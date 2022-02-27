R = set()
def f(a, p):
    if p == 5: R.add(a)
    if p > 5: return
    return f(a+2, p+1) or f(a+3, p+1) or f(a*2, p+1)

f(10, 0)
print(len(R))


