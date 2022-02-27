'''
В последовательности натуральных чисел рассматриваются все пары чисел, у которых сумма элементов чётна. Среди таких пар
найдите пару, дающую максимальную сумму.

В первой строке дано число  — количество чисел в последовательности (). Далее в N строках подается по одному целому
числу — элементы последовательности. Каждое из чисел по модулю не превосходит .

Выведите одно число – максимальную чётную сумму двух элементов последовательности. Если таких пар нет, выведите ноль.
'''
import sys
#sys.stdin = open('1.txt')
N = int(input())
maxi_nechet_1 = 0
maxi_nechet_2 = 0
maxi_chet_1 = 0
maxi_chet_2 = 0
for i in range(N):
    x = int(input())

    if x % 2 == 0:
        if x > maxi_chet_2:
            if x > maxi_chet_1:
                maxi_chet_2 = maxi_chet_1
                maxi_chet_1 = x
            else:
                maxi_chet_2 = x
    else:
        if x > maxi_nechet_2:
            if x > maxi_nechet_1:
                maxi_nechet_2 = maxi_nechet_1
                maxi_nechet_1 = x
            else:
                maxi_nechet_2 = x
#print(maxi_chet_1+maxi_chet_2, maxi_nechet_1+maxi_nechet_2)

a = maxi_nechet_1; b = maxi_nechet_2
c = maxi_chet_1; d = maxi_chet_2

if (a + b > d + c) and a!=0 and b!=0:
    print(a+b)
elif (a +b <= d + c) and c!=0 and d!=0:
    print(c+d)
else:
    print(0)


