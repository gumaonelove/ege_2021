import sys
#sys.stdin = open('3.txt')
N = int(input())
s = [0 for x in range(0, 10)]
for line in range(N):
    x = int(input())
    s[x%10] += 1

#print(s) # debag print
"""
не получается определить кол-во пар все остальное заебись
!!!
"""
count = 0
count += (s[0]*s[8])
count += s[1]*s[7]
count += s[2]*s[6]
count += s[3]*s[5]
count += (s[4]*(s[4]-1))/2
count += (s[9]*(s[9]-1))/2

print(int(count))