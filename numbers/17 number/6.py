c=0
m=0
for i in range(924, 9433):
    if i%7==0 and i%11!=0 and i%13!=0 and i%15!=0 and i%24!=0:
        c+=1
        if i>m:
            m=i

print(c, m)