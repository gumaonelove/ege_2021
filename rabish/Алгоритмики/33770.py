iter = 0
def f(n):
    count= 0
    Divs=set()
    for i in range (2, int(n**0.5)+1):
        count+=1
        if n%i ==0:
            if i%2==0: Divs.add(i)
            if (n//i)%2==0: Divs.add(n//i)
        if len(Divs)>2: break
    if len(Divs)==2: return (True, count)
    return (False, count)
print("число, кол- во чет дел, список чет дел")
for n in range (106_000_000, 107_000_000+1, 2):
    Q = f(n)
    if Q[0]:
        print(n)
        iter+=Q[1]
print('кол-во итераций:', iter)