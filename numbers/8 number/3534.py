'''
(Е. Джобс) Вася составляет 4-буквенные слова, в которых есть только буквы С, Ч, И, Т, А, Й, причём буква А может
встретиться в каждом слове не более 1 раза. Каждая из других допустимых букв может встречаться в слове любое количество
раз или не встречаться совсем. Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько различных слов может написать Вася?
'''

letters = ['С', 'Ч', 'И', 'Т', 'А', 'Й']
count = 0
for l1 in letters:
    for l2 in letters:
        for l3 in letters:
            for l4 in letters:
                word = l1+l2+l3+l4
                if word.count('А')<=1 :
                    count += 1


print(count)