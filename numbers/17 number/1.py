A = []
for i in range(4668, 10415):
    if (i % 3 == 0 or i % 11 == 0) and i % 2 !=0 and i % 13 !=0 and i % 22 !=0 and i % 33 !=0:
        A.append(i)
print(len(A))
print(min(A))