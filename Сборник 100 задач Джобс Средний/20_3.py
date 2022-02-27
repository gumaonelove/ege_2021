from math import ceil
winning_positions_for_Vasya = []
lossing_positions_for_Vasya = []
def wiv_vas(now, p):
    if p % 2 == 1 and (now in winning_positions_for_Vasya): return True
    if p % 2 == 1 and (now in lossing_positions_for_Vasya): return False
    if p % 2 == 1 and now == 1: return True
    if p % 2 == 0 and now == 1: return False
    if p % 2 == 0:
        result = False
        for next_step in range(ceil(now/2), now):
            result += wiv_vas(next_step, p+1)
        return result
    else:
        result = True
        for next_step in range(ceil(now/2), now):
            result *= wiv_vas(next_step, p+1)
        return result
    
count = 0
for s in range(2, 1000):
    if wiv_vas(s, 1):
        winning_positions_for_Vasya.append(s)
        count += 1
        print(s)
    else:
        lossing_positions_for_Vasya.append(s)

print('answer =', count)        
print(winning_positions_for_Vasya)
print(lossing_positions_for_Vasya)
