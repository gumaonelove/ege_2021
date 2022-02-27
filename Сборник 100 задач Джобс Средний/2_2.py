print('a b c d F')
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                F = int((a==d) or (c and not(d)))
                print(a, b, c, d, F)
