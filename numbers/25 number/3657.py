def f(n):
    s=0
    while n!=0:
        if n%10>=3:
            return False
        s+=n%10
        n=n//10
    if s%10==0:
        return True
    return False
def g(n):
    B=[1]
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            B.append(i)
            B.append(n//i)
    return len(B)
c=1

for i in range(1000000, 1300000):
    if f(i):
        if c%10==0:
            print(i, g(i))
        c+=1




