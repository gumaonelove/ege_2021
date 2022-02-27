def g(line:str):
    main_list = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}
    last = line[0]
    line = line[1:]
    count = 1
    for now in line:
        if now == last:
            count += 1
        else:
            if count > main_list[last]:
                main_list[last] = count
            count = 1
        last = now
    return main_list



M = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}
with open('24.txt') as f:
    for line in f.readlines():
        G = g(line.replace('\n', ''))
        for key in G:
            if G[key] == max(G.values()):
                M[key] += 1



print(M)










