'''
Функция f ищет, когда решения правильны для 1 или 2 хода Вани, а фу-ция f1 ищет, когда решения правильны только
для 1 хода Вани, значит из решений для f нужно убрать решения f1
'''
sum_for_win = 68
x = 6

def f(x,y,p):
    '''
    Функция f ищет, когда решения правильны для 1 или 2 хода Вани
        :param x: stones in first group
        :param y: stones in second group
        :param p: whose move
        :return: will p winn
    '''
    if x+y>=sum_for_win and (p==5 or p==3): # 1 or 2 Petya's step
        return True
    else:
        if x+y<sum_for_win and p==5: # 2 Petya's step
            return False
        else:
            if x+y>=sum_for_win:
                return False
    if p%2==0: # Ivan's step
        return f(x+1,y,p+1) or f(3*x,y,p+1) or f(x,y+1,p+1) or f(x,3*y,p+1)
    else:
        return f(x+1,y,p+1) and f(3*x,y,p+1) and f(x,y+1,p+1) and f(x,3*y,p+1)

def f1(x,y,p):
    '''
    фу-ция f1 ищет, когда решения правильны только для 1 хода Вани, значит из решений для f нужно убрать решения f1
        :param x: stones in first group
        :param y: stones in second group
        :param p: whose move
        :return: will p winn
    '''
    if x+y>=sum_for_win and (p==3): # 1 Petya's step
        return True
    else:
        if x+y<sum_for_win and p==3: # 1 Petya's step
            return False
        else:
            if x+y>=sum_for_win:
                return False
    if p%2==0: # Ivan's step
        return f1(x+1,y,p+1) or f1(3*x,y,p+1) or f1(x,y+1,p+1) or f1(x,3*y,p+1)
    else:
        return f1(x+1,y,p+1) and f1(3*x,y,p+1) and f1(x,y+1,p+1) and f1(x,3*y,p+1)


for i in range(1,100):
    if f(x,i,1):
        print(i)
print("==========")
for i in range(1,100):
    if f1(x,i,1):
        print(i)
        
