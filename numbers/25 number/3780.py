'''Найдите все натуральные числа, принадлежащие отрезку [63 000 000; 75 000 000], у которых ровно пять различных
нечётных делителей (количество чётных делителей может быть любым). В ответе перечислите найденные числа, справа от
каждого числа запишите его наибольший нечётный делитель.'''
import time
t0 = time.time()
from math import isqrt
def is_prime(z):
    if z <= 2 or z % 2 == 0: return False
    d = 3
    while d * d <= z:
        if z % d == 0: return False
        d += 2
    return True
# 65_000_000 75_000_000
print('start')
for x in range(1, 1000 + 1):
    # сбрасываю из x все двойки
    y = x
    while y % 2 == 0: y //= 2
    z = isqrt(isqrt(y))
    if z ** 4 == y and is_prime(z): print(x, y)
t1 = time.time()
print('Затрачено времени:', int(t1-t0), 'секунд')