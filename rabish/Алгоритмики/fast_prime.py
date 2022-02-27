def fast_prime(n):
    if n%2==0 and n!=2: return False
    elif n==2: return True
    d = 3
    if d*d<=n:
        if n%d==0: return False
        d+=2
    return True