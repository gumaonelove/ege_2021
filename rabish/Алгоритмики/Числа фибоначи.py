def fib1(n):
    F = [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            F.append(F[i-2] + F[i-1])
        return F[n]
    else:
        return F[n]
cache = {}

def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n-1) + fib2(n-2)
    return cache[n]
    
def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1
    
    
def main():
    n = int, input().split()
    print(fib1(n))


if __name__ == "__main__":
    main()
