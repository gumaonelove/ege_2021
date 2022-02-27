''' Необходимо найти наибольшую сумму такой группы, заканчивающуюся на 50. Программа должна вывести эту сумму.'''
file = open('27 number-61b.txt')
N, *data = map(int, file.readlines())
data.sort()
part = data[:20]

# trying for B task:
residual = (sum(data) - 50) % 100
from itertools import combinations
min_sum = 99999999999
for i in range(0, len(part)):
    for c in combinations(part, i):
        if sum(c) % 100 == residual:
            #print(c)  # DEBUG print
            if sum(c) < min_sum:
                min_sum = sum(c)
print(sum(data) - min_sum)
