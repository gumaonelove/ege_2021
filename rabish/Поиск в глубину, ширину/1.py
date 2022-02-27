from functions import *


def adj(G, n, v1, v2):
    """Смежные ли вершины"""
    if G[v1*n + v2] == 1: return True
    else: return False

def dfs(G, n, visited, v1, final_vertice, way):
    '''
    Поиск в глубину
    :param G: Наш граф
    :param n: Число вершин
    :param visited: Массив вершин в которых мы были
    :param v1: Начинаем с v1
    :return: Ищем,,,
    '''
    visited[v1] = True
    if v1 == final_vertice:
        way.append(v1)
        return True
        
    for x in range(n):
        if not(visited[x]) and adj(G, n, v1, x):
            result = dfs(G, n, visited, x, final_vertice, way)
            if result:
                way.append(v1)
                return True
    return False




G = []
n = int(input())
visited = [False]*n

for i in range(n):
    s = input().split()
    for j in range(len(s)):
        G.append(int(s[j]))

counter = 0
for i in range(n):
    if visited[i] == False:
        counter += 1
        dfs(G, n, visited, i)
print(counter)

A = int(input())
Z = int(input())
way = []
dfs(G, n, visited, A, -1)
print(way[::-1])


A = int(input())
B = int(input())
line = [A]
print(bfs(G, n, A, B, line, visited))