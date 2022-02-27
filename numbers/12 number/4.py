a = 16**1003 + 8**405 - 2**239 + 43
def f2(n):
    A = []
    while n!=0:
        A.append(n%2)
        n = n // 2
    return A
c = 0
for b in f2(a):
    if b == 0:
        c+=1
print(c)
