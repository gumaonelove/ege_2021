for A in range (1, 10000):
    ok = 1
    for x in range(1, 1000):
        ok *= (x//50 > 3) or (x//13 <= 3) or (x//A > 6)
        if ok==0: break
    if ok==1: print(A)