from functions import *
'''
Напишем представление графа в виде списка ребер
В входных данных получим граф в виде списка ребер, сохраним в памяти
Первая строка содержит n, m - число вершин и ребер, затем
m строк содержат пары чисел от 0 до n-1  - например, 3 7 означает 
что между вершинами 3 и 7 есть ребро
'''

n, m = map(int, input().split())

V = [x for x in range(n)] # массив вершин
E = [0]*2*m # массив ребер

for i in range(m):
    a, b = map(int, input().split()) # считываем ребро a, b
    E[2*i], E[2*i+1] = a, b # начало вершины, конец вершины

s = 0

for i in range(n):
    s += vertice_degree(V, E, m, n, i)
print(s, m)


flag = False
for i in range(n): # Алгоритм по поиску петель O(m*n)
    if is_loop(V, E, m, n, i):
        flag = True


flag = False
for i in range(m): # Алгоритм по поиску петель O(m)
    if E[2*i] == E[2*i+1]:
        flag = True
        print('Петля: ', E[2*i+1])
print(flag)