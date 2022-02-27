'''
(№ 2679) (А. Жуков) Имеется набор данных, состоящий из целых чисел. Необходимо определить максимальное произведение
подпоследовательности, состоящей из одного или более идущих подряд элементов.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество
чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно натуральное число, не превышающее по модулю 100.
Пример входного файла:
7
2
3
-2
-3
-1
4
6
Для указанных входных данных наибольшее произведение равно 72. Его можно получить для последовательности -3 -1 4 6.
В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.
'''

def list_list_count_otr(*args):
    ind_otr = []
    for i in range(len(args)):
        if args[i] <0:
            ind_otr += [i]
    return ind_otr

def list_proz(*args):
    p = 1
    for a in args:
        p *= a
    return p

import sys
sys.stdin = open('b.txt')
N = int(input())
p = []
Proiz = []
for _ in range(N):
    x = int(input())
    if x !=0:
        p += [x]
    else:
        Proiz.append(p)
        p = []

Proiz.append(p)
PPPP = []
for p in Proiz:
    if len(list_list_count_otr(*p)) == 1:
        p.pop(list_list_count_otr(*p)[0])
        PPPP.append(list_proz(*p))
    elif len(list_list_count_otr(*p))%2==0 and len(list_list_count_otr(*p))!=0:
        PPPP.append(list_proz(*p))
    elif len(list_list_count_otr(*p))%2==1:
        ind_otr = list_list_count_otr(*p)
        #print(ind_otr)
        otr = []
        for i in ind_otr:
            otr.append(p[i])
        min_otr = max(otr)
        p.remove(min_otr)
        PPPP.append(list_proz(*p))
    elif len(list_list_count_otr(*p))==0:
        PPPP.append(list_proz(*p))

print(max(PPPP))





