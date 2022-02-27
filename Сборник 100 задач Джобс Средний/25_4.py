'''
Найдите 6 первых непростых чисел, больших 1200000 (1.2 млн), сумма делителей которых
(кроме 1 и самого числа) меньше, чем
n/555
В качестве ответа приведите найденные числа и сумму их делителей.
'''

def prime(n):
    if n <= 1: return False
    elif n == 2: return True
    elif n%2==0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True

def sumka(N):
    s = 0
    for n in N: s+= n
    return s

def f(n):
    # n is not prime
    devs = set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            devs.add(i)
            devs.add(n//i)
    s = sumka(devs)
    if s <n/555: return s
    else: return 0

def delit(n):
    devs = set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            devs.add(i)
            devs.add(n//i)
    return devs

count = 0

for n in range(1_200_000, 2*10**6):
    if prime(n): next
    else:
        F = f(n)
        if F!=0 and count<6:
            print(n, F)
            count += 1


