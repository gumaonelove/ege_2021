'''
(Е. Джобс) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди,
 первый ход делает Петя. За один ход игрок может
а) добавить в кучу сто камней или
б) увеличить количество камней в куче в два раза.
Победителем считается игрок, сделавший последний ход,
то есть первым получивший кучу, в которой будет 1000 или больше камней.
В начальный момент в куче было S камней, 1 ≤ S ≤ 999.
   Назовите минимальное и максимальное значения S, при которых Ваня выигрывает своим первым или вторым ходом,
   при этом для любого значения у Вани есть возможность выиграть своим первым ходом (в случае ошибки Пети).
'''


def f(s, p): # вася выйграет 1 или 2 ходом, с условием правильной игры Пети
    if s>=1000: return (p==3 or p==5)
    if s<1000 and p==5: return False
    if p>5: return False

    if p%2==0:
        return f(s+100, p+1) or f(2*s, p+1)
    else:
        return f(s+100, p+1) and f(2*s, p+1)


r = set()
for s in range(1, 1000):
    if f(s, 1):
        r.add(s)

def f1(s, p):
    if s>=1000: return p==3
    if p > 3: return False
    if s<1000 and p==3: return False

    return f1(s + 100, p + 1) or f1(s * 2, p + 1)

r1 = set()
for s in range(1, 1000):
    if f1(s, 1):
        r1.add(s)



def f2(s, p):
    if s>=1000: return p==3
    if p > 3: return False
    if s<1000 and p==3: return False

    if p==1:
        return f2(s+100, p+1) and f2(s*2, p+1)
    if p==2:
        return f2(s + 100, p + 1) or f2(s * 2, p + 1)

r2 = set()
for s in range(1, 1000):
    if f2(s, 1): r2.add(s)



l = list(r.intersection(r1).difference(r2))
l.sort()
print(l)