with open('list.txt', 'r') as f:
    A = sorted((int(x) for x in f.readline().split()))


print(A[len(A)//2])