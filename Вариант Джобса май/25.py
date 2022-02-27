def is_prime(n):
    if n == 2: return True
    if n%2==0: return False
    if n == 1: return False
    for i in range(3, int(n**0.5)+2, 2):
        if n%i==0: return False
    return True


count = 0
d = 1
while count != 5:
    if is_prime(10000000 + d):
        count += 1
        print(d, 10000000 + d)
    d += 1

count = 0
d = 1
while count != 5:
    if is_prime(10000000 - d):
        count += 1
        print(d, 10000000 - d)
    d += 1
'''
19 number 10000019
79 10000079
103 10000103
121 10000121
139 10000139
9 9999991
27 9999973
29 9999971
57 9999943
63 9999937

'''