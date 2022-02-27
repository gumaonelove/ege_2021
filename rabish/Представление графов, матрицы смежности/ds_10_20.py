from functions_for_dz import *

n, m = map(int, input().split()) # n - колво вершин, m - колво ребер
V = [x for x in range(n)]
E = [0]*2*m # Список ребер
for i in range(m): # Считываем ребра
    E[2*i], E[2*i+1] = map(int, input().split())

#print(ans_10(E, m)) #10
#print(ans_11(E, m)) #11
#print(*ans_13(E, n)) # 13

# for a in ans_15(E, n, m): print(*a) # 15

#print(ans_17(E, n, m)) # 17


#print(ans_18(E, n, m)) # 18



#print(ans_19(E, n, m)) # 19 number


#print(ans_20(E, n, m)) # 20