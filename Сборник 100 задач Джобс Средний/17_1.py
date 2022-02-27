def f(n):
    last = n%10; n//=10
    last_chet = (last%2==0)
    while n!=0:
        now = n%10; n//=10
        now_chet = (now%2==0)
        if now_chet == last_chet: return False
        last_chet = now_chet
    return True



count = 0
for n in range(123456, 654321+1):
    if f(n): count +=1

print(count)
