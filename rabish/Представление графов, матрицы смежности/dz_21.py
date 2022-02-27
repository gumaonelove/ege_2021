from functions_for_dz import *

n, m = map(int, input().split()) # n - колво вершин, m - колво ребер
V = [x for x in range(n)] # список вершин
E = [[0]*m, [0]*m] # Список ребер первый вложмас = старт, второй финиш
for i in range(m): # Считываем ребра
    E[0][i], E[1][i] = map(int, input().split())


print(ans_21(E, V, n, m))