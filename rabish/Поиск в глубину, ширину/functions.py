def adj(G, n, v1, v2):
    """Смежные ли вершины"""
    if G[v1*n + v2] == 1: return True
    else: return False

def dfs(G, n, visited, v1, prev):
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
            if visited[x] and x!= prev: return True
            else:
                result = dfs(G, n, visited, x, v1)
                if result: return True
    return False


def bfs(G, n, start, goal_node, line, visited):
    '''Есть ли путь от а до б поиском в ширину'''
    while len(line)>0:
        x = line.pop(0)
        visited[x] = True
        for i in range(n):
            if i == goal_node: return True
            if G[i*n+x]==1:
                if not(visited[i]): line.append(i)

    return False