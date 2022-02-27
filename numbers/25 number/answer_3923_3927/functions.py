def prime(n):
    '''Проверяем простое число или нет'''
    if (n <= 1 or n % 2 == 0) and n != 2: return False
    if n == 2: return True
    d = 3
    while d * d <= n:
        if n % d == 0: return False
        d += 2
    return True

def set_prosto(n):
    '''Возвращает массив простых чиссел из диапазона 2...n+1'''
    ans = []
    for i in range(2, n+1):
        if prime(i): ans.append(i)
    return ans

def delim(n): # на 10**6 итераций затрачено 33 секунды
    '''
    Ищем все делители числа
    :param n:
    :return: Все делители числа включая 1 и n
    '''
    devs = set()
    pros = set()
    for i in range(1, int(n**0.5)+1, 1):
        if n%i==0:
            devs.add(i)
            devs.add(n//i)
            if prime(i): pros.add(i)
            if prime(n//i): pros.add(n//i)
    return (devs, pros)

def proiz(A):
    '''
    Произведение всех элементов
    :param A: Множество которое надо перемножить
    :return: произведение всех элементов
    '''
    ans = 1
    for a in A: ans *= a
    return ans

def power_of_num(n, d):
    power = 0
    while n % d == 0:
        power+=1
        n//=d
    return power






