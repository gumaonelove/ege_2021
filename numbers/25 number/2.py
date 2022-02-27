def f(n):
    A=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            A.append(i)
            A.append(n//i)
    if len(A)==6:
        A.sort()
        return A
    return set()

for n in range(174352, 174398):
    if f(n)!=set():
        print(*f(n))