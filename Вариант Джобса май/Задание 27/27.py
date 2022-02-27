import sys
sys.stdin = open('27-0.txt')
N = int(input())
big = []
little = []
middle = [[], []]
for _ in range(N):
    pair = list(map(int, input().split()))
    if sum(pair)%2==0:
        little.append(min(pair))
        big.append(max(pair))
    else:
        middle[pair[0]%2] += [pair[0]]
        middle[pair[1] % 2] += [pair[1]]


print(big)
print(little)
print(middle)
