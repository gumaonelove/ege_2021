A=input()
count=0
B=A.split()
for b in B:
    b=int(b)
    if b>0:
        count+=1
print(count)
