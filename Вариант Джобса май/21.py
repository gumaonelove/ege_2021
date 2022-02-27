def f(x, y, p):
    if x+y >= 45 and (p==3 or p==5): return True
    if x+y < 45 and p==5: return False
    if x + y >=45 and p!=5: return False
    if p%2==0:
        return f(x, x+y, p+1) or f(x+y, y, p+1)
    else:
        return f(x, x+y, p+1) and f(x+y, y, p+1)

for y in range(1, 100):
    if f(y, y, 1):
        print(y)

print('===============================')
def f1(x, y, p):
    if x + y >= 45 and p==3 : return True
    if x + y >= 45 and p!=3: return False
    if x+y<45 and p==3: return False
    if p%2==0:
        return f1(x, x+y, p+1) or f1(x+y, y, p+1)
    else:
        return f1(x, x+y, p+1) and f1(x+y, y, p+1)

for y in range(1, 100):
    if f1(y, y, 1):
        print(y)