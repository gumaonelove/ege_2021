# выбрать из каждой пары ровно одно число так,
# чтобы сумма всех выбранных чисел не делилась на 3
# и при этом была максимально возможной.
import sys
sys.stdin = open("2663-A.txt")
N = int(input())
sum_of_maximums = 0
# массив минимальных разностей в парах, сгруппированных по остатку
min_deltas = [[10001]*2 for residual in range(3)]
for i in range(N):
    x, y = (int(word) for word in input().split())
    sum_of_maximums += max(x, y)
    delta = abs(x - y)
    if delta < min_deltas[delta % 3][-1]:  # победил в "поддавки" наибольший мин
        min_deltas[delta % 3][-1] = delta  # занимаю его место
        min_deltas[delta % 3].sort()  # "перетряхиваем" минимальные

delta = 0
if sum_of_maximums % 3 == 1:
    delta = min(min_deltas[1][0], min_deltas[2][0] + min_deltas[2][1])
elif sum_of_maximums % 3 == 2:
    delta = min(min_deltas[2][0], min_deltas[1][0] + min_deltas[1][1])
sum_of_maximums -= delta
print(sum_of_maximums)
