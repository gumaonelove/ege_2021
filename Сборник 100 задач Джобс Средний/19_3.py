from math import ceil
def f(now, p):
    if p == 6 and now == 1:return True
    if p == 6 and now != 1: return False
    if p != 6 and now == 1: return False
    if p > 6: return False
    if p % 2 == 1:
        result = False
        for next_step in range(ceil(now/2), now):
            result += f(next_step, p+1)
        return result
    else:
        result = True
        for next_step in range(ceil(now/2), now):
            result *= f(next_step, p+1)
        return result

for s in range(20, 1, -1):
    if f(s, 1):
        print(s)
        break
        
        
    
