'''(№ 2673) Имеется набор данных, состоящий из положительных целых чисел. Необходимо определить количество пар элементов
(ai, aj) этого набора, в которых 1 ≤ i + 7 ≤ j ≤ N и произведение элементов кратно 14.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество чисел
 N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно натуральное число, не превышающее 10 000.
Пример входного файла:
9
7
5
6
12
5
11
8
16
14
Для указанных входных данных количество подходящих пар должно быть равно 3. В приведённом наборе имеются три подходящие
пары (7, 16), (7, 14), (5, 14), произведение элементов которых кратно 14, а индексы элементов последовательности
различаются не меньше, чем на 7.
В ответе укажите два числа: сначала количество подходящих пар для файла А, затем для файла B.
'''
import sys
sys.stdin = open('27-13b.txt')
M = 14
N = int(input())
A = [int(input()) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(i+7, N):
        if (A[i] * A[j]) % 14 == 0:
            count += 1

print(count)

# a 30
# b