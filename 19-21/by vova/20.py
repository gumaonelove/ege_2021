sum_for_win = 68
x = 6


def f(x, y, p):
    '''
        :param x: stones in first group
        :param y: stones in second group
        :param p: whose move
        :return: will p winn
    '''
    if x + y >= sum_for_win and p == 4:
        return True
    else:
        if x + y < sum_for_win and p == 4:
            return False
        else:
            if x + y >= sum_for_win:
                return False
    if p % 2 == 1:
        return f(x + 1, y, p + 1) or f(3 * x, y, p + 1) or f(x, y + 1, p + 1) or f(x, 3 * y, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(3 * x, y, p + 1) and f(x, y + 1, p + 1) and f(x, 3 * y, p + 1)


for i in range(1, 100):
    if f(x, i, 1):
        print(i)

