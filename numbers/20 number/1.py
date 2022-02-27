'''
(Е. Джобс) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди,
первый ход делает Петя. За один ход игрок может
а) добавить в кучу сто камней или
б) увеличить количество камней в куче в два раза.
Игра завершается в тот момент,
когда количество камней в куче становится не менее 1000. Победителем считается игрок, сделавший последний ход,
то есть первым получивший кучу, в которой будет 1000 или больше камней.
В начальный момент в куче было S камней, 1 ≤ S ≤ 999.
   Сколько существует значений S, при которых Петя выигрывает вторым ходом?
'''

def f(s, p):
    if s>=1000: return p==4
    if p > 4: return False
    if s<1000 and p==4: return False

    if p==2:
        return f(s+100, p+1) and f(s*2, p+1)
    else:
        return f(s + 100, p + 1) or f(s * 2, p + 1)

count = 0
for s in range(1, 1000):
    if f(s, 1):
        count += 1
        if count<20: print(s)
print('==========')
print(count)