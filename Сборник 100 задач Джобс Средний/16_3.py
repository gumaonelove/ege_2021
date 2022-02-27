F = [x for x in range(10)] + [None]*100
G = [x for x in range(10)] + [None]*100
print(F)
print(G)

for n in range(10, 100):
    if n%2==0:
        G[n] = G[n - 1] - F[n - 1]
        F[n] = G[n] - F[n - 1]
    else:
        F[n] = F[n - 1] + G[n - 1]
        G[n] = F[n] + G[n - 1]

print(F[40])