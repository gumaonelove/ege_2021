from functions import *
def dfs(G, n, visited, v1, final_vertice, way, cycle_starter):
    #global way
    '''
    Поиск в глубинв проверка на циклы
    :param G: Наш граф
    :param n: Число вершин
    :param visited: Массив вершин в которых мы были
    :param v1: Начинаем с v1
    :return: Ищем,,,
    '''
    visited[v1] = True
    for x in range(n):
        if adj(G, n, v1, x):
            if visited[x]:
                cycle_starter = x
                way.append(v1)
                return  True
            else:
                result = dfs(G, n, visited, x, final_vertice, way, cycle_starter)
                if result:
                    way.append(v1)
                    if v1 == x:
                        FINISH = True
                        return True
    return False
