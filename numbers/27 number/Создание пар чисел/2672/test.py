import sys
sys.stdin = open('27-12a.txt')
N = int(input())
M = 6
All = [int(input()) for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if i!=j:
            if (All[i] * All[j])%M==0:
                count += 1

print(count//2)