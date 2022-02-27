import sys
sys.stdin = open('b.txt')
N = int(input())

A = [int(input()) for _ in range(N)]; A.sort()
#print(A)
maxi_len = 1
elem = A[0]
now_len = 0
for dif in range(1, 101):
    now_len = 1
    i = -1
    while i < len(A)-2:
        i += 1
        if elem + dif in A[i+1:i+dif+1]:
            now_len += 1
            elem = A[i] + dif
            i = i + A[i+1:i+dif+1].index(elem)
        else:
            elem = A[i+1]
            if maxi_len < now_len:
                maxi_len = now_len
            now_len = 1

if maxi_len < now_len:
    maxi_len = now_len
now_len = 1
print(maxi_len)

