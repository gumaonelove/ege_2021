'''
(А.Н. Носкин) Петя составляет семибуквенные слова перестановкой букв слова ТРАТАТА.
Сколько всего различных слов может составить Петя?
'''

from itertools import permutations

letters = 'ТРАТАТА'

words = set()
for word in permutations(letters):
    words.add(word)

print(len(words))
