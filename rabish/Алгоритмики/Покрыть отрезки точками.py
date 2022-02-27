n = int(input())
maps_tuples = []
maps_set = set()

for i in range(n):
    x1, x2 = map(int, input().split())
    maps_tuples.append((x1, x2))
    maps_set.add(x1); maps_set.add(x2)


def PointsCover(mt, ma):
    count = 0
    A = []
    for x in ma:
        for y in mt:
            if y[0] <= x <= y[1]:
                count += 1
        else:
            if count == len(mt):
                A.append(x)
            count = 0
    return A


print(PointsCover(maps_tuples, maps_set))
print(maps_set)