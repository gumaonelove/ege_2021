A = [True, False]
print("x y z w ")
for x in A:
    for y in A:
        for z in A:
            for w in A:
                if ( (not(x) or not(y)) and (not( (not(x) and not(z)) or (x and z) ) ) and w ) == True:
                    print(int(x), int(y), int(z), int(w))
