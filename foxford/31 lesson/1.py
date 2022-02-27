def sign(x):
    if x >= 0: return 1
    return -1

a, b, c, d = map(float, input().split())

q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)
p = (3 * a * c - b**2)/(3*a**2)
Q = (p/3)**3+(q/2)**2
A = sign(-q/2+Q**0.5)*((abs(-q/2+Q**0.5))**(1/3))
B = sign(-q/2-Q**0.5)*((abs(-q/2-Q**0.5))**(1/3))

print(A+B-b/(3*a))