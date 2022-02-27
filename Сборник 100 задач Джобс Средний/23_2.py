A = set()
def f(n):
    if n>=100: return
    elif n%2==0: A.add(n)
    f(n+3) or f(n*3)

f(10)

print(len(A))