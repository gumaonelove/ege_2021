import math

w, h, n = [int(x) for x in input().split()]
l = 0
r = math.ceil(math.sqrt(w * h * n)) * max(h, n)
m = r // 2

def ok(g, h, w, n):
    if (g // h) * (g // w) >= n: return True
    else: return False
    
while r - l > 1:
    if ok(m, h, w, n):
        r = m
    else: l = m
    m = (r - l) // 2 + l

print(r)