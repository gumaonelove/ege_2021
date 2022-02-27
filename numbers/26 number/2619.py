with open('2619.txt', 'r') as f:
    capacity, N = (int(x) for x in f.readline().split())
    A = sorted(list(int(x) for x in f))

used_capacity = 0
i = 0
while used_capacity + A[i] <= capacity:
    used_capacity += A[i]
    i += 1

print('count:', i)

used_capacity -= A[i - 1]  # выкинули последнего пометившегося
i -= 1  # отшагнули назад
delta = capacity - used_capacity

while A[i + 1] <= delta:  # следующуий влезает перешагиваем на него
    i += 1

print('Максимальный размер данных пользователя:', A[i])