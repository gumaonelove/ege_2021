'''
В последовательности натуральных чисел рассматриваются все пары чисел. Для каждой пары вычисляется произведение
 составляющих пару чисел. Найдите максимальное произведение пары чисел, запись которого заканчивается на 3.
'''
# кол-во чсел с последней цифрой _
last_1=0; last_3=0; last_7=0; last_9=0
# массив из переменных, не знаю будет ли использоваться, просто как вариант
count_last=[0, last_1, 0, last_3, 0, 0, 0, last_7,0,last_9]

N = int(input())
for _ in range(N):
    x = int(input())
    if x > count_last[x%10]: count_last[x%10]=x
print(max(count_last[1]*count_last[3], count_last[7]*count_last[9]))
