def prime(n):
    '''Проверяем является ли входное число простым'''
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return False
    return True

def go_next_prost(n):
    '''Ищем для входного числа ближайшее большее простое, тупым перебором'''
    d = 1
    while True:
        if prime(n+d): return (n+d)
        d+=1

def f(a, b):
    if a == b: return 1
    if a > b: return 0
    if a == 33: return 0
    k = f(a + 2, b) + f(go_next_prost(a), b)
    return k


print(f(2, 14)*f(14, 45))

