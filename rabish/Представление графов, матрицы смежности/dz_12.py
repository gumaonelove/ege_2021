from functions_for_dz import *
N = int(input())
V = [x for x in range(N)] # Список вершин
E = [[0] for x in range(N)] # Матрица в структуре двумерного массива
for i in range(N): E[i] = [int(x) for x in input().split()]

# print(ans_12(E)) # 12


#for a in ans_14(E): print(*a) # 14

#for a in ans_16(E): print(*a) # 16

print(ans_22(E))