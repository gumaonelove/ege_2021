'''
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех выбранных чисел  делилась
на 3 и при этом была максимально возможной.
'''
import sys
sys.stdin = open('Zadanie_27-B-kyrs.txt')
N = int(input())
M = 3
s = [0] + [None]*(M-1)
for line in range(N):
    numbers = [int(x) for x in input().split()]
    s_new = [None] * M
    for k in range(M):
        variants = [x + s[(k-x) % M] for x in numbers if s[(k-x)% M] is not None]
        s_new[k] = max(variants) if variants else None
    s[:] = s_new
for i in s:
    try:
        if i%3==0: print(i)
    except:
        pass