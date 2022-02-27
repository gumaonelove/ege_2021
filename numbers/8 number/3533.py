'''
(Е. Джобс) Вася составляет 4-буквенные слова из букв И, Н, С, Т, А, В, К и упорядочивает их по алфавиту.
При этом на первом месте может быть только согласная, на последнем - гласная. Вот начало списка:
1. ВААА
2. ВААИ
3. ВАВА
...
Укажите номер слова НИКА в этом списке.
'''

letters = ['И', 'Н', 'С', 'Т', 'А', 'В', 'К']
letters.sort()
cogl = ['Н', 'С', 'Т','В', 'К']
glas = ['И', 'А']
words = []
for l1 in letters:
    for l2 in letters:
        for l3 in letters:
            for l4 in letters:
                word = l1+l2+l3+l4
                if word[0] in cogl and word[-1] in glas:
                    words.append(word)
print(words.index('НИКА')+1)