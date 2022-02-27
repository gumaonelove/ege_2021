def count_edges(a, n):
    '''Считаем кол-во ребер O(n**2)'''
    counter = 0
    for i in range(n):
        for j in range(i, n):
            if [a[i*n+j]] == 1:
                counter += 1
    return counter

def vertice_degree(a, n, i):
    '''Считаем степень вершины O(n)'''
    counter = 0
    for j in range(n): # пробегаемся по вершинам
        if a[i*n+j] == 1: # нашел ребро которые включает в себя i вершину
            counter += 1
    return counter

def adj(a, n, i, j):
    '''Являются ли вершины i, j смежными?'''
    return bool(a[i*n+j])

def is_loop(a, n, i, j):
    '''Являются ли вершина петлей?'''
    return bool(a[i*n+j])


def find_dangling(a, n):
    '''Ищет висящую вершину O(n**2)'''
    for i in range(n):
        if vertice_degree(a, n, i) == 1: return i
    return -1

def remove_edge(a, n, i, j):
    """Удаляем ребро"""
    a[i*n+j] = 0
    a[j*n+i] = 0