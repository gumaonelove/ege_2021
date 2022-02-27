'''В файле 24-4 записана строка, состоящая из букв английского алфавита. Укажите
максимальную длину подстроки, в записи которой только 2 различных символа.
Например, в строке acbcbbbbaabaabccbab такая подстрока bbbbaabaab = 10'''

A = open('24-4.txt', 'r').read()
print(A)
max_len = 0
for i in range(len(A)):
    now_str = set(); now_str.add(A[i])
    j = i+1; count = 0
    while len(now_str)<=2 and j<len(A):
        now_str.add(A[j])
        j += 1; count += 1
    if count > max_len: max_len = count
print(max_len)

