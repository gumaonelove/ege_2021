'''
(№ 2677) (А. Жуков) Имеется набор данных, состоящий из положительных целых чисел. Необходимо определить количество
пар элементов (ai, aj) этого набора, в которых 1 ≤ i+5 ≤ j ≤ N, сумма элементов нечётна, а произведение делится на 13.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество
 чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно натуральное число, не превышающее 10 000.
Пример входного файла:
7
4
14
27
39
7
2
13
Для указанных входных данных количество подходящих пар должно быть равно 2. В приведённом наборе имеются две пары
(4, 13) и (14, 13), сумма элементов которых нечётна, произведение кратно 13 и индексы элементов последовательности
отличаются не менее, чем на 5.
В ответе укажите два числа: сначала количество подходящих пар для файла А, затем для файла B.
'''

import sys
sys.stdin = open('b.txt')
N = int(input())
M = 5
Q = [int(input()) for _ in range(M)]
k_13_1 = k_13_2 = k_2 = k_1 = 0
pn = 0
for i in range(N-M):
    y = Q[i%M]
    if y%13 == 0:
        if y%2==0:
            k_13_2 += 1
        else:
            k_13_1 += 1
    else:
        if y%2==0:
            k_2 += 1
        else:
            k_1 += 1

    x = int(input())

    if x%13==0:
        if x%2==0: # четное кратное 13
            pn += k_13_1 + k_1
        else: # не четное кратное 13
            pn += k_13_2 + k_2
    else:
        if x%2==0: # четное не кратное 13
            pn += k_13_1
        else: # не четное не кратное 13
            pn += k_13_2
    Q[i%M] = x
print(pn)