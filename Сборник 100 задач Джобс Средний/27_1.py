'''
На вход программе поступает набор пар чисел. Нужно выбрать из каждой пары ровно одно
число таким образом, что сумма будет максимальной и будет оканчиваться на две
одинаковые цифры. Если такую сумму получить невозможно, вывести “NO” (без кавычек).
'''

import sys
from itertools import combinations
sys.stdin = open('27-1B.txt')
N = int(input())
raznost = [10**10]*11
suma = 0
for i in range(N):
    x, y = map(int, input().split())
    maxi = max(x, y); mini = min(x, y); r = maxi - mini
    suma+=maxi
    if raznost[r%11]>r: raznost[r%11] = r

print('Сумма без измения', suma)
print(raznost)
Q = []
for i in range(len(raznost)):
    for r in combinations(raznost, i):
        if ((suma-sum(r))%100)%11==0:
            Q.append(suma-sum(r))
print(max(Q))
