'''Для каждой пары вычисляется сумма и произведение составляющих пару чисел. Найдите максимальную
сумму пары, где произведение заканчивается на 4.'''

import sys
#sys.stdin = open('27_B.txt')
N = int(input()) # кол-во числе на вход
M = 10 # остаток на от деления на данное число закидываем в массив
s = [] * M # закидываем в этот массив
c_2 = 0 # второе по максимуму число дающее в отсатке 2
for lile in range(N): # начинаем считывание массива
    x = int(input()) # входное число последовательности
    s[x%M] = x if x > s[x%M] else s[x%M] # заполняем массив отностительно остатка от деления на 10
    if x%M==2 and x<s[x%M] and x>c_2: c=x # произведение чисел с остатком 2 дает на конце 4, значит нам нужно
    # # контролировать второе по величине числ с остатком 2


print(s) # debug print
suma = 0 # наша искомая сумма
'''
tup = [(1, 4), (2, 2), (2, 7), (3,8 number), (4, 6), (6,9)]
for t in tup:
    if s[t[0]] + s[t[1]] > suma:
        print(s[t[0]], s[t[1]], s[t[0]] + s[t[1]], s[t[0]] * s[t[1]])
        suma = s[t[0]] + s[t[1]]

'''
for i in range(M): # начиная лоховской перебор с помощью 2 циклов, знаю что хуйня идея
    for j in range(M): # осознаю что хуйня идея
        if (s[i]*s[j]) % 10 == 4 and s[i]+s[j] > suma and i!=j: # проверяю число ласт цифра произведения 4,
            # # сумма больше предыдуших и это не числа с остатком 2 и 2
            print(s[i],s[j], s[i]*s[j], s[i]+s[j]) # debug print
            suma = s[i]+s[j] # записываю подходящую сумма
        if i == 2 == j and s[i] + c_2 > suma and (s[i]*c_2) % 10 == 4: # рассматриваю ситуацияю с
            # # произведением двух чисел с остатком 2
            suma = s[i] + c_2
            print(s[i], c_2, s[i] * c_2, s[i] + c_2) # debug print


#print('-----------') # beautiful print
print(suma) # anwer