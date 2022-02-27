def f(n):
    maxi = -1000
    mini = 1000
    while n!=0:
        if (n%10)>maxi: maxi = (n%10)
        if mini > (n%10): mini = (n%10)
        n//=10
    if maxi + mini == 12: return True
    return False


A = []
for n in range(123456, 654321+1):
    if f(n): A.append(n)

print(len(A), min(A))