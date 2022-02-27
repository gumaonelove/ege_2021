def adj(v1, v2):
    '''
    Проверяем смежные вершиы или нет
    :param v1:
    :param v2:
    :return: Смежная или нет
    '''
    global w; global h
    if All[v1]!='.' or All[v2]!='.': return False
    x1, y1 = v1 % w, v1 // w
    x2, y2 = v2 % w, v2 // w
    #print(v1, '=', (x1, y1))
    #print(v2, '=', (x2, y2))
    if y1==y2 and abs(x1-x2)==1: return True
    if x1==x2 and abs(y1-y2)==1: return True
    return False
def ans_1(All, visited, v1, final_vert, way):
    '''
    Выведите карту с нарисованным путем прямо на экран
    :param All: Граф в виде матрицы смежности
    :param n: кол-во вершин графа
    :param visited: массив вершин в которых мы побывали
    :param start: вершина откуда начинаем
    :param finish: куда должны попасть
    :param way: наш путь
    :return: можем попасть или нет
    '''
    visited[v1] = True
    if v1 == final_vert:
        way.append(v1)
        return True
    for x in range(len(All)):
        if not(visited[x]) and adj(v1, x):
            result = ans_1(All, visited, x, final_vert, way)
            if result:
                way.append(v1)
                return True
    return False

import sys

sys.stdin = open('1.txt')
w, h = map(int, input().split())

All = []
visited = [False]*h*w
way = []

for y in range(h): All += str(input()).split()
start, finish = All.index('s'), All.index('e')
All[start]='.'; All[finish]='.'

for verb in range(w*h):
    if visited[verb]==False:
        ans_1(All, visited, start, finish, way)

for i in way: All[i]='*'
for line in range(h): print(*All[line*w:(line+1)*w])




