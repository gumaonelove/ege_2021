A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

def binary_search(n):
    mid = len(A) // 2 # среднее значение
    low = 0 # минимальное значение
    high = len(A) - 1 # типо максимальное значение

    while A[mid] != n and low <= high:
        if n > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return -1
    else:
        return mid

for b in B:
    print(binary_search(b))