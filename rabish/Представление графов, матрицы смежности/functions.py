def count_edges(V, E, m, n):
    '''Считаем кол-во ребер'''
    return m

def vertice_degree(V, E, m, n, i):
    '''Считаем степень вершины'''
    counter = 0
    for j in range(m): # пробегаемся по вершинам
        if E[2*j]==i or E[2*j+1]==i: # нашел ребро которые включает в себя i вершину
            counter += 1
    return counter

def adj(V, E, m, n, i,  j):
    '''Являются ли вершины i, j смежными?'''
    flag = False
    for k in range(m):
        if E[2*k] == i and E[2*i+1] == j:
            flag = True
        if E[2*k] == j and E[2*i+1] == i:
            flag = True
    return flag

def is_loop(V, E, m, n, i):
    '''Являются ли вершина петлей?'''
    for k in range(m):
        if E[2*k] == i and E[2*i+1] == i:
            return True
    return False

def adj_pro(V, E, m, n, i,  j):
    '''Кол-во смежных вершин'''
    flag = 0
    for k in range(m):
        if (E[2*k] == i and E[2*i+1] == j) or (E[2*k] == j and E[2*i+1] == i):
            flag += 1
    return flag

def find_dangling(V, E, m, n):
    '''Ищет висящую вершину'''
    # Ниже представлен говно код O(n*m)
    '''for i in range(n):
        if vertice_degree(V, E, m, n, i)==1:
            return i
    return -1'''
    # Вроде норм O(n+m)
    degree = [0]*n
    for k in range(m):
        degree[E[2 * k]] += 1
        degree[E[2 * k + 1]] += 1
    for i in range(n):
        if degree[i] == 1:
            return i
    return -1

def remove_edge(V, E, m, n, i, j):
    E = list(E)
    """Удаляем ребро"""
    for k in range(m):
        if (E[2*k]==i and E[2*k+1]==j) or (E[2*k]==j and E[2*k+1]==i):
            E.pop(2*k); E.pop(2*k +1)
    return E

# write me sir:

def shortest_route():
    '''Кратчайший маршрут в графе между двумя вершинами'''
    pass

def longest_route():
    '''Самый длинный маршрут, не повторяющийся'''
    pass

def contains_cycles():
    '''Существуют ли в шрафе цицлы'''

def is_connective():
    """Является ли граф связанным"""

def is_tree():
    '''Является ли граф деревом?'''

def count_routes():
    '''Кол-во маршрутов'''



