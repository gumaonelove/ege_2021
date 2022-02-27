A = []
with open('24-5.txt', 'r') as f:
    for line in f:
        words = [len(str(word)) for word in line.split()]
        A += words
print('Среднее значение длины слова: ', int(sum(A)/len(A)))
print('Кол-во слов: ', len(A))
