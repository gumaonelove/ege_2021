'''
В последовательности натуральных чисел рассматриваются все пары чисел, у которых произведение
кратно 6. Среди таких пар найдите пару, дающую максимальное произведение.
'''

import sys
#sys.stdin = open('27_B.txt')
N = int(input())
M = 6
s = [0]*M
for line in range(N):
    x = int(input())
    s[x % M] = x if x > s[x % M] else s[x % M]
max_ne_6 = max(s[1:])

if max_ne_6 * s[0] > max(s[2], s[4]) * s[3] and max_ne_6 * s[0] != 0:
    if max_ne_6 < s[0]:
        print(max_ne_6, s[0])
    else:
        print(s[0], max_ne_6)
elif max_ne_6 * s[0] <= max(s[2], s[4]) * s[3] and max(s[2], s[4]) * s[3] != 0:
    if max(s[2], s[4]) < s[3]:
        print(max(s[2], s[4]), s[3])
    else:
        print(s[3], max(s[2], s[4]))
else:
    print(0, 0)




#print(s)