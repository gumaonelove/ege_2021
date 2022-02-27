'''
В диапазоне [200800; 200950] найдите числа, являющиеся произведением трех различных
простых чисел, сумма которых меньше 1000.
В качестве ответа выведите пары чисел в порядке возрастания первых значений –
найденное число и сумма простых чисел, произведение которых образует данное число.
'''

def prime(n):
    if n <= 1: return False
    elif n == 2: return True
    elif n%2==0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True
def go_prime_list():
    A = []
    for n in range(1, 1500):
        if prime(n): A.append(n)
    return A
def sumka(N):
    s = 0
    for n in N: s+= n
    return s
def proz(N):
    p = 1
    for n in N: p*=n
    return p
def f(n):
    devs = []
    for i in go_prime_list():
        if n%i==0: devs.append(i)
    if len(devs)<3: return 0
    if len(devs)==3 and sumka(devs)<1000 and proz(devs)==n:
        return(sumka(devs))
    return 0


for n in range(200800, 200950+1):
    F = f(n)
    if F!=0:
        print(n, F)
    
