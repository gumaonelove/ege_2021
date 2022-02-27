import sys
sys.setrecursionlimit(50000)
def f(a, b):
    if a == b:
        return 1
    if a>b:
        return 0
    k = f(a, b+1)

    if float(int(b**0.5)) == float(b**0.5):
        k+=f(a, b**0.5)
    return k
print(f(5, 225))