F = open('24.txt', 'r')
ln=1
mxln=1
st=F.read()
n=len(st)
for i in range (1,n):
    if st[i]==st[i-1]:
        ln=ln+1
        if ln>mxln:
            mxln=ln
    else:
        ln=1
print (mxln)
F.close()