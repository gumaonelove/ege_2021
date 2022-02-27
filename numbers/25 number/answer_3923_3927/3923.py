from functions import *
import time
t0 = time.time()
n = int(input())

primes = set_prosto(30)
s = ''
ans = 1
c = []
k = 0

for d in primes:
    if n%d==0:
        k += power_of_num(n, d)
        s+= str(d) + '**' + str(power_of_num(n, d)) + "\n"

        for j in range(power_of_num(n, d)):
            c.append(d)
c.sort(reverse=True)

print(primes)
print(c)
for i in range(k):
    ans *= primes[i]**(c[i]-1)
print(s)
print(ans)

t1 = time.time()
print('Времени затрачено =', int(t1-t0), 'секунд')