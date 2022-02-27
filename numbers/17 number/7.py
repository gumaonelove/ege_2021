def nod(a,b):
    while b!=0:
        a, b=b, a%b
    return a
c=0
#print(nod(11, 13))
for i in range(100000, 10**6):
    if nod(70, i)==1:
        c+=1
print(c)


