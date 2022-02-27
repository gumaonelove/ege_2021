'''
Определите максимальное количество идущих
подряд символов, среди которых каждые два соседних различны.
'''


with open('zadanie24_1.txt', 'r') as f:
    '''
    count=0
    maxi=0
    last=''
    for i in str(f.read()):
    #for i in 'aabaaab':
        if i!=last:
            count+=1
        else:
            if count>maxi:
                maxi=count
            count=1
        last=i
    '''
    count = 0
    maxi = 0
    last = ''
    A = f.readline()
    for i in range(0, len(A)-1):
        # for i in 'aabaaab':
        if A[i+1] != A[i]:
            count += 1
        else:
            if count > maxi:
                maxi = count
            count = 1

    print(maxi)
