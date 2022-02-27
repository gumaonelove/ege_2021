'''
(Е. Джобс) Женя составляет слова переставляя буквы З, А, П, И, С, Ь. Сколько слов может составить Женя, если известно,
 что Ь не может стоять на первом месте и после гласной?
'''
from itertools import permutations
count = 0
letters = ['З', 'А', 'П', 'И', 'С', 'Ь']
glass = ['А', 'И']
for word in permutations(letters):
    if word[0] != 'Ь' and not(word[word.index('Ь')-1] in glass):
        count += 1
print(count)