with open('input.txt', 'r') as f:
    All = f.read()
All = All.replace('\n', ' ')
suma=0; l=''
for i in All:
    if i!=' ':
        l+=i
    else:
        suma+=int(l)
        l=''

print(suma, file=open('output.txt', 'w'))