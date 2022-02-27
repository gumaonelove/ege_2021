#A= [int(word) for word in input().split()]
A=list(range(500, 0, -1))
N = len(A)
i=0
iterations_counters=0
while i<N-1: # пока справа кто-то есть
    iterations_counters+=1
    if not(A[i] <= A[i+1]):
        A[i], A[i+1] = A[i+1], A[i]
        i=0
    else: # порядок, идем дальше к концу
        i+=1


print(A)
print('iterations:', iterations_counters)

# n**3