from functions_1 import *
'''
Напишем представление графа в виде матрицы смежности
Что такое двумерный массив?
-таблица n*m n - строчек, m - столбцов
'''
n = int(input())
a = [0]*n*n
for i in range(n):
    for j in range(i, n):
        a[i*n+j] = 0 # FIX ME!!!