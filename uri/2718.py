import math
n = int(input())
for i in range(n):
    x = bin(int(input()))[2:]
    arr = [0 for j in range(len(x))]
    maxi = 0
    if x[0] == '1':
        arr[0] = 1
        maxi = 1

    for j in range(1, len(x)):
        if x[j] == '1':
            arr[j] = arr[j-1] + 1
            maxi = max(maxi, arr[j])
        else:
            arr[j] = 0
    print(maxi)
