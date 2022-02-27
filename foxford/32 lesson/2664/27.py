import sys
sys.stdin = open('1.txt') # Задача ЕГЭ №27 number  с сайта К.Ю.Полякова (#2664 в генераторе)
N = int(input())
M = 2 # на какое число должно делится
s = [0] + [None] * (M - 1) # табличка: возможные остатки от деления
for i in range(N):                      # print(*s, sep='\t')  # DEBUG PRINT
    numbers = [int(x) for x in input().split()]
    s_new = [None]*M # вычисляем новые макс.суммы для каждого остатка
    for k in range(M): # будем искать кол-во числе дающих определенный остаток
        variants = [x + s[(k - x) % M] for x in numbers if s[(k - x) % M] is not None]
        s_new[k] = max(variants) if variants else None
    s[:] = s_new
print(*s, sep='\t')
