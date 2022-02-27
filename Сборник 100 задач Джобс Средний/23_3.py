count = 0
def f(a, b):
    global count
    if a>b or a == 50: return
    if a == b: count+=1
    f(a+3, b) or f(2*a+1, b) or (a+(3-a%3), b)


f(5, 23)
c1 = count

f(23, 89)
print(c1*(count-c1))