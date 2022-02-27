import sys
sys.stdin = open('27-1B.txt')
N = int(input())
M = 100
S = [0] + [None]*(M-1)
R = [00, 11, 22, 33, 44, 55, 66, 77, 88, 99]
for i in range(N):
    numbers = [int(x) for x in input().split()]
    s_new = [None]*M
    for k in range(M):
        variants = [x + S[(k-x)%M] for x in numbers if S[(k-x)%M] is not None]
        s_new[k] = max(variants) if variants else None
    S[:] = s_new

Ans = []
for r in R:
    Ans.append(S[r])
print(max(Ans))

print(S[50])
# A = 1577
# B = 695111