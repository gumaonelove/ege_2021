s = '>' + '1'*10 + '2'*20 + '3'*30

while s.find('>1') != -1 or s.find('>2') != -1 or s.find('>3') != -1:
    if s.find('>1') != -1:
        s = s.replace('>1', '22>', 1)
    if s.find('>2') != -1:
        s = s.replace('>2', '2>', 1)
    if s.find('>3') != -1:
        s = s.replace('>3', '1>', 1)
q=0
s=s[::]
for i in s:
    q+=int(i)
print(q)