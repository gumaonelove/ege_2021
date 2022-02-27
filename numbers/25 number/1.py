def f(n):
    A=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            A.append(i)
            A.append(n//i)
    if len(A)==4:
        A.sort()
        return A
    return set()

for n in range(194_400, 194_421):
    if f(n)!=set():
        print(*f(n))