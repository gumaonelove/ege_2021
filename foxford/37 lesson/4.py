def f(x, y, p):
    if x+y>=71 and p==4: return True
    if x+y>=71 and p!=4: return False
    if x+y<71 and p==4: return False
    if p%2==1:
        return f(x+3, y, p+1) or f(x*2, y, p+1) or f(x, y+3, p+1) or f(x, y*2, p+1)
    else:
        return f(x+3, y, p+1) and f(x*2, y, p+1) and f(x, y+3, p+1) and f(x, y*2, p+1)


for y in range(1, 57):
    if f(13, y, 1):
        print(y)
