def f(x, y, p):
    if x+y>=71 and (p==3 or p==5): return True
    if x+y>=71 and p!=5: return False
    if x+y<71 and p==5: return False
    if p%2==0:
        return f(x+3, y, p+1) or f(x*2, y, p+1) or f(x, y+3, p+1) or f(x, y*2, p+1)
    else:
        return f(x+3, y, p+1) and f(x*2, y, p+1) and f(x, y+3, p+1) and f(x, y*2, p+1)
def f1(x, y, p):
    if x+y>=71 and p==3: return True
    if x+y>=71 and p!=3: return False
    if x+y<71 and p==3: return False
    if p%2==0:
        return f1(x+3, y, p+1) or f1(x*2, y, p+1) or f1(x, y+3, p+1) or f1(x, y*2, p+1)
    else:
        return f1(x+3, y, p+1) and f1(x*2, y, p+1) and f1(x, y+3, p+1) and f1(x, y*2, p+1)


for y in range(1, 57):
    if f(13, y, 1):
        print(y)
print('=============')