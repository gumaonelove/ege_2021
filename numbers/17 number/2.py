A=[]
for i in range(1030, 7731):
    if i%4==0 and i%12!=0 and i%15!=0 and i%17!=0 and i%21!=0:
        A.append(i)

print(len(A), max(A))