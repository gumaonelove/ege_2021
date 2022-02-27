def f(n):

    m = 0
    while n > 0:
        d = n % 10
        if d % 3 == 0:
            if d > m:
                m = d
        n = n // 10
    if m == 0:
        return ('NO')
    else:
        return (m)
print(f(36))
# ошибки: