'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [194465; 194550],
 числа, имеющие ровно 4 различных делителя.
'''

def f(n):
    A = set()
    for i in range(1, int(n*0.5)+1):
        if n%i==0: A.add(i); A.add(n//i)
        if len(A)>4: return set()
    if len(A)!=4: return set()
    B = list(A)
    B.sort()
    return B

for n in range(194_465, 194_550+1):
    U = f(n)
    if U!=set():
        print(n, U)