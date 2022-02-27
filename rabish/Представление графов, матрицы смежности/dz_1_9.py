from functions_for_dz import *


'''
N = int(input())
V = [x for x in range(N)] # Список вершин
E = [[0] for x in range(N)] # Матрица в структуре двумерного массива
for i in range(N): E[i] = [int(x) for x in input().split()]

#print(ans_1(E)) # Задача 1
#print(ans_2(E)) # Задача 2
#print(ans_3(N)) # Задача 3
#print(ans_4(E)) # Задача 4
#for rib in ans_5(E): print(rib) # Задача 5
#for rib in ans_7(E): print(rib) # Задача 7
'''

'''
n, m = map(int, input().split()) # n - колво вершин, m - колво ребер
V = [x for x in range(n)]
E = [0]*2*m # Список ребер
for i in range(m): # Считываем ребра
    E[2*i], E[2*i+1] = map(int, input().split())

# Задача 6
print(E)
print(ans_6(E, n))


print(ans_8(E, n, m)) # 8 number

'''

N = int(input())
E = [] # Список ребер
for i in range(N):
    m = [int(x) for x in input().split()]
    for x in m:
        E.append((i+1, x))

print(N)
for i in ans_9(E, N):
    print(*i)

