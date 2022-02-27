A = set()

def f(start, p):
    if p == 5: A.add(start)
    if p > 5: return
    f(start+4, p+1) or f(start*2, p+1)
f(2, 0)
print(len(A))

