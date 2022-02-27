def f(n):
    raznost_dev = set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            raznost_dev.add(n//i - i)
    if len(raznost_dev) >= 2:
        if min(raznost_dev) > 4444:
            if min(raznost_dev)!=0:
                if max(raznost_dev) % min(raznost_dev) == 0:
                    return min(raznost_dev)
    return set()


for n in range(543210, 987654+1):
    F = f(n)
    if F:
        print(n, F)