for x in (False, True):
    for y in (False, True):
        for z in (False, True):
            for w in (False, True):
                if ((x and y and not(z)) == (y or z or not(w))) == True:
                    print(int(x), int(y), int(z), int(w))