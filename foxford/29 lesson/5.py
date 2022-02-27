'''Текстовый файл состоит более чем из 100 символов A, B и C. Определите максимальное количество идущих подряд символов,
среди которых каждые два соседних одинаковы. Для выполнения этого задания следует написать программу.'''

with open('24.txt', 'r') as f:
    count=0
    maxi=0
    last=''
    for i in str(f.read()):
    #for i in 'aabaaab':
        if i==last:
            count+=1
        else:
            if count>maxi:
                maxi=count
            count=1
        last=i
    print(maxi)