'''
Есть набор данных, состоящий из  пар положительных целых чисел. Необходимо выбрать из каждой пары ровно одно число так,
 чтобы сумма всех выбранных чисел не делилась на 4 и при этом была максимально возможной. Если получить требуемую сумму
 невозможно, в качестве ответа нужно выдать 0.
'''
N = int(input())
min_raznost = 10**10
suma=0
for _ in range(N):
    x, y = map(int, input().split())
    maxi=max(x, y); mini=min(x, y); suma+=maxi
    if maxi-mini<min_raznost and maxi!=mini:min_raznost=maxi-mini
if suma%4==0: suma-=min_raznost
if suma%4==0: suma=0
print(suma)