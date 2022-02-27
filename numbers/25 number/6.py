'''
Рассматриваются целые числа, принадлежащих числовому отрезку [356738; 404321],
которые представляют собой произведение двух различных простых делителей.
В ответе запишите количество таких чисел и такое из них, простые делители которого отличаются друг от друга больше всего.
'''

def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3, int(n**0.5)+2, 2):
        if n%i==0: return False
    return True

def f(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            if is_prime(i) and is_prime(n//i): return (n//i - i)
    return False

count = 0
m = 0
this = 0
for n in range(356_738, 404_321+1):
    F = f(n)
    if F != False:
        count += 1
        if F > m:
            m = F
            this = n

print(count, this)
