
A = [3, 8, 5, 4, 1, 2, 4, 1, 9, 3]
c = 0
for i in range(1, 10):
    if A[i-1] < A[i]:
        c = c + 1
        A[i-1], A[i] = A[i], A[i-1]
print(c)