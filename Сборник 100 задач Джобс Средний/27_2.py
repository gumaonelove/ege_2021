import sys
sys.stdin = open('27-2B.txt')
N = int(input())
suma = 0
count_3 = 0
raznost = []
for i in range(N):
    numbers = [int(x) for x in input().split()]
    mini = min(numbers); maxi = max(numbers)
    suma += mini
    if mini%3==0: count_3 +=1
    if (maxi - mini)%3!=0 and mini!=maxi: raznost.append(maxi - mini)
raznost.sort()
print(suma)
print(raznost)
print('suma = ', suma+1+1)
print('Всего', N)
x = 2
print('кол-во кртных 3:', count_3-x)
print('Процент кратных 3:', str((count_3-x)/N)[:4])

# A = 412
# B = 3412945