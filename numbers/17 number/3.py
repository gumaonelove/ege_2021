A=[]
for i in range(1045, 8964):
    if (i%5==0 or i%7==0) and i%11!=0 and i%13!=0 and i%17!=0 and i%19!=0:
        A.append(i)

print(len(A), min(A))