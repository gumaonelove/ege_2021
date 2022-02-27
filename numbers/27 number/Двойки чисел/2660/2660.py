'''
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех выбранных чисел не
делилась на 3 и при этом была максимально возможной.
'''
import sys
sys.stdin = open('2660-B.txt')
N = int(input())
sum_of_maximum = 0
min_distance = 10**5
for i in range(N):
    x, y = (int(word) for word in input().split())
    sum_of_maximum += max(x, y)
    if abs(x-y) < min_distance and abs(x-y) % 3 != 0:
        min_distance = abs(x-y)

if sum_of_maximum % 3 == 0:
    sum_of_maximum -= min_distance

print(sum_of_maximum)

# 32
# 127127
# 399762080