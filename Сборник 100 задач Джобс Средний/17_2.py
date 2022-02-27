def sums(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s


def proz(n):
    p = 1
    while n != 0:
        p *= n % 10
        n //= 10
    return p

A = []
for n in range(123456, 654321 + 1):
    if sums(n)>proz(n): A.append(n)
print(len(A), max(A))