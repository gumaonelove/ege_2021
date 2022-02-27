'''
В файле 24-3 записана строка, состоящая из букв a и b. Найдите максимальную длину
подстроки из пересекающихся комбинаций abba.
Например, в строке bbbaaababbabbabbaaabab длиной искомой последовательности будет
10 (abbabbabba).
'''

A = open('24-3.txt', 'r').readline()
#A = 'abbabbabba'
A = A.replace('bb', '1')
count = 0
max_len = 0
print(A)
for i in range(0, len(A), 2):
    #print(A[i:i+2])
    if A[i:i+2] == 'a1': count += 1
    else:
        if max_len<count: max_len = count
        count = 0
print(max_len*3+1)

