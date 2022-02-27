import sys
sys.stdin = open('b.txt')
N = int(input())
A_50men = [0]*51
B_51bol = [0]*80
for _ in range(N):
    x = int(input())
    if x <= 50: A_50men[x%80] += 1
    if x > 50: B_51bol[x%80] += 1
count = 0
for i in range(1, 51): count += A_50men[i] * B_51bol[80 - i]
for i in range(1, 40): count += B_51bol[i] * B_51bol[80 - i]
count += B_51bol[0]*(B_51bol[0]-1)//2
count += B_51bol[40]*(B_51bol[40]-1)//2
print(count)