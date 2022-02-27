def suma(n):
    s = 0
    for i in str(n): s += int(i)
    return s

def f(n):
    n = str(bin(n)[2:]) + str(suma(n)%2)
    if n.count('1') > n.count('0'):
        n += '0'
    else:
        n += '1'
    return int(n, 2)


for n in range(20, 25):
    if f(n) > 80:
        print(f(n))


