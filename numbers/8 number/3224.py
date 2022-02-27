'''
Сергей составляет 6-буквенные коды из букв Е, Л, Й. Буква Й может использоваться в коде не более одного раза, при
этом она не может стоять на первом месте, на последнем месте и рядом с буквой Е. Все остальные буквы могут встречаться
произвольное количество раз или не встречаться совсем. Сколько различных кодов может составить Сергей?
'''
letters = ['Е', 'Л', 'Й']
count = 0
for l1 in letters:
    for l2 in letters:
        for l3 in letters:
            for l4 in letters:
                for l5 in letters:
                    for l6 in letters:
                        word = l1+l2+l3+l4+l5+l6
                        if word.count('Й')<=1 and word[0]!='Й' and word[-1]!='Й' and word.count('ЙЕ')==0 and word.count('ЕЙ')==0:
                            count += 1
                            #print(word)

print(count)