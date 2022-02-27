c=0
m=0
for i in range(1033, 7738):
    if i%5==0 and i%11!=0 and i%17!=0 and i%19!=0 and i%23!=0:
        c+=1
        if i>m:
            m=i

print(c, m)