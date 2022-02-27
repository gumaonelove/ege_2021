'''
(№ 2686) Имеется набор данных, состоящий из пар положительных целых чисел. Необходимо выбрать из каждой пары ровно одно
число так, чтобы сумма всех выбранных чисел в шестнадцатеричной системе счисления оканчивалась на F и при этом была
минимально возможной. Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно число –
минимально возможную сумму, соответствующую условиям задачи.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество пар
N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит два натуральных числа, не превышающих 10 000.
Пример входного файла:
6
3 5
5 12
6 9
5 4
7 9
5 1
Для указанных входных данных значением искомой суммы должно быть число 31, которое в шестнадцатеричной системе
 счисления записывается как 1F16.
В ответе укажите два числа: сначала значение искомой суммы для файла А, затем для файла B.
'''

import sys
sys.stdin = open('27-26b.txt')
N = int(input())
s = [0] + [None]*15 # нам нужна 15 ячейка
for _ in range(N):
    numbers = [int(x) for x in input().split()]
    s_new = [None] * 16
    for k in range(16):
        variants = [x + s[(k-x)%16] for x in numbers if s[(k-x)%16] is not None]
        s_new[k] = min(variants) if variants else None
    s[:] = s_new

print(s[15])