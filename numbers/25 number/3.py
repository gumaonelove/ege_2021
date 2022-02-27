def f(n):
    A=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            if i%2==0:
                A.append(i)
            if (n//i)%2==0:
                A.append(n//i)
    if len(A)==4:
        A.sort()
        return A
    return set()

for n in range(174350, 174395+1):
    if f(n)!=set():
        print(*f(n))