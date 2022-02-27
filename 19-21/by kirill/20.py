main_answer = {}
s = 74 # sum for win
firt_group = 7

def main(x, y):
    '''number of moves for which Petya will win'''
    if (x, y) in main_answer:
        return main_answer[(x, y)]
    if x + y >= s:
        return 0
    start_recursion = [main(x + 2, y), main(x * 2, y), main(x, y+2), main(x, y*2)]

    moves_for_lose = [i for i in start_recursion if i <= 0] # generation

    if moves_for_lose:
        result = -max(moves_for_lose) + 1
    else:
        result = - max(start_recursion)
    main_answer[(x, y)] = result
    return result

for i in range(1, 66): # i = count in second group
    if main(firt_group,i) == 2: print(i)

