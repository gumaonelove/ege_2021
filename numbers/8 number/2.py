'''
Миша составляет 5-буквенные коды из букв С, А, К, У, Р. Каждая допустимая гласная буква может входить в код не более
одного раза. Сколько кодов может составить Миша?
'''
count = 0

c = ["С", "К", "Р"]
w = ["А", "У"]
for w1 in c+w:
    for w2 in c + w:
        for w3 in c + w:
            for w4 in c+w:
                for w5 in c + w:
                    word = w1+w2+w3+w4+w5
                    if word.count(w[0]) <= 1 and word.count(w[1]) <= 1:
                        if count <= 20:
                            print(word)
                        count += 1


print(count)

