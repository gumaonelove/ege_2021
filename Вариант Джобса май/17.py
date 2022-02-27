def go7(n):
    while n!=0:
        if n%7==0: return False
        n //=7
    return True
count = 0
maxi = 0
for n in range (3399, 225599+1):
    if n%5==3 and go7(n):
        count += 1
        if n > maxi: maxi = n

print(count, maxi)