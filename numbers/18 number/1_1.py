with open('1_1.txt', 'r') as f:
    rows = f.readlines()
A = []
S = []
for row in rows:
    try:
        ind = row.index('\n')
        b = row[:ind].replace(',', '.')
    except:
        b = row.replace(',', '.')
    A.append(float(b))
suma = A[0]
for i in range(len(A)-1):
    if A[i+1] > A[i]:
        suma += A[i+1]
    else:
        S.append(suma)
        suma = A[i+1]
else:
    S.append(suma)
print(int(max(S)))