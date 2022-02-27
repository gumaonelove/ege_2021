import sys
sys.stdin = open('27-1b.txt')
N = int(input())
raznosts = set()
summa = 0
for _ in range(N):
    para = list(map(int, input().split()))
    summa += min(para)
    raznost = max(para) - min(para)
    if raznost%3!=0:
        raznosts.add(raznost)

if summa%3==0:
    summa += min(raznosts)

print(summa)