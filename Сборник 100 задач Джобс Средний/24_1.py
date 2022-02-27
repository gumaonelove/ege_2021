A = open('24-1.txt', 'r').readline()
start_pos = ''
last_pos = ''
steps = ''
Buk = {}
maxi = 0
count = 1
for i in range(len(A)-1):
    start_pos = A[i]
    if A[i+1] != start_pos:
        steps = A[i+1]
        for j in range(i+2, len(A)):
            if A[j] == steps: count += 1
            else:
                last_pos = A[j]
                break
        if start_pos == last_pos and last_pos != steps:
            if count > maxi:
                if Buk.get(steps)==None: Buk[steps] = count
                else:
                    if Buk[steps] < count: Buk[steps] = count
    count = 1

print(Buk)
print(A.rfind('BBBBB'))
print(A.rfind('CCCCC'))

