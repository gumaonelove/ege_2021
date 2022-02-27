A=list(range(1000, 0, -1))
N = len(A)

iterations_counters=0
is_sorted = False
# сортирующий проход конечной длины
while not is_sorted:
    # сортирующий проход
    is_sorted=True
    i = 0
    while i<N-1: # пока справа кто-то есть
        iterations_counters+=1
        if not(A[i] <= A[i+1]): # непорядок исправляем
            A[i], A[i+1] = A[i+1], A[i]
            is_sorted=False # запоминаем факт беспорядок
        i+=1 # всегда идем дальше


print(A)
print('iterations:', iterations_counters)


# n**2