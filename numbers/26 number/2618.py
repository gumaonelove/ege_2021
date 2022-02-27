import time

t1 = time.time_ns()
with open('2618.txt', 'r') as f:
    storage_capacity, users_number = (int(x) for x in (f.readline().split()))
    A = [int(f.readline()) for i in range(users_number)]


def bubble_sort(A):
    '''this funs is bubble sort'''
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        i = 0
        while i < len(A) - 1:
            if not (A[i] <= A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i]
                is_sorted = False
            i += 1
    return A


# A = bubble_sort(A)
A.sort()
count = 0
used_capacity = 0

while used_capacity + A[count] <= storage_capacity:  # пока очередной не переполнит диск
    used_capacity += A[count]
    count += 1
print('Пользователей поместилось:', count)

used_capacity -= A[count - 1]  # выкинули последнего пометившегося
count -= 1  # отшагнули назад
delta = storage_capacity - used_capacity

while A[count + 1] <= delta:  # следующуий влезает перешагиваем на него
    count += 1
t2 = time.time_ns()
print('Максимальный размер данных пользователя:', A[count])
print('Времени задрачено:', str((t2 - t1) / (10 ** 9))[:4], 'секунд')

# with bubble_sotr: time  = 2.13 s
# with python_standart_sort: time = 0 s
