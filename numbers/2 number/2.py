for x in  (True, False):
    for y in  (True, False):
        for z in  (True, False):
            if (not(x) and y and z) or (not(x) and not(z)) == True:
                print(int(x),int(y),int(z))
