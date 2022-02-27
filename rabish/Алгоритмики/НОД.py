def gcd1(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd1(a % b, b)
    elif b >= a:
        return gcd1(a, b % a)

def gcd2(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)

def gcd3(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a>= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)

def gcd4(a, b):
    assert a >= 0 or b >= 0
    if a == 0 or b == 0:
        return max(a,b)
    return gcd4(b % a, a)


def main():
    a, b = map(int, input().split())
    print(gcd1(a, b))


if __name__ == "__main__":
    main()