c=0
m=0
for i in range(1043, 7238):
    if i%4==0 and i%12!=0 and i%16!=0 and i%25!=0:
        c+=1
        if i>m:
            m=i

print(c, m)