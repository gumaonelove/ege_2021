'''
В последовательности натуральных чисел рассматриваются все пары чисел.
Для каждой пары вычисляется сумма составляющих пару чисел. Определите количество пар, где сумма кратна 8 number.
'''

import sys
#sys.stdin = open('27_B.txt')
N = int(input())
M = 8 # остаток от деления на 10, для определения последней цифры обрабатываемого числа
s = [0]*M
for line in range(N):
    x = int(input())
    s[x % M] += 1
#print(*[i for i in range(M)]) # debug print
#print(*s) # debug print
count = (s[0]*(s[0]-1))/2 + (s[4]*(s[4]-1))/2
for i in range(1,M//2):
    #print(i) # debug print
    count += s[i]*s[8-i]
print(int(count))