with open('24_1.txt', 'r') as f:
    count=0
    maxi=0
    for i in str(f.read()):
        if i=='R':
            count+=1
        else:
            if count> maxi:
                maxi=count
            count=0
print(maxi)