def prime(n):
    if n<=1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return False
    return True

def func_devs(n):
    devs = set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            devs.add(i)
            devs.add(n//i)
    return devs

def na_prosto(n):
    ans = ''
    power = 0
    while n%2==0 and n>0:
        n//=2
        power+=1
    if power != 0: ans += str(2) + '**' + str(power) + ' '
    d = 3
    power = 0
    while d <= n:
        if not(prime(d)): d+=2
        while n % d == 0:
            n //= d
            power+=1
        if power != 0: ans+= str(d)+'**'+str(power)+' '
        power = 0
        d += 2
    return ans

def sumka(n):
    s = 0
    while n!=0:
        s+=n%10
        n//=10
    return s

def proiz(N):
    p = 1
    for n in N: p*=n
    return p

def prosto_arr():
    A = []
    for i in range(100):
        if prime(i): A.append(i)
    return A

def ans_25_1(n):
    devs = set(); devs.add(n); devs.add(1)
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            devs.add(i)
            devs.add(n//i)
    l = len(devs)
    if l>=350: return True
    return False


def ans_25_2(n):
    count_3 = 0
    count_al = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i%3==0: count_3+=1
            else: count_al +=1
            if (n//i)%3==0: count_3+=1
            else: count_al+=1
    if count_3>count_al*2: return count_3 - count_al
    return 0


