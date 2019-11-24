import math
n = int(input())
arr = [int(x) for x in input().split()]
sol = 0


def is_stepladder(i, j):
    diff = arr[i + 1] - arr[i]
    for k in range(i + 1, j + 1):
        if arr[k] - arr[k-1] != diff:
            return False
    return True


if len(arr) == 1:
    print(1)
    exit()
last = 0
i = 1
while(i < len(arr)):
    if is_stepladder(last, i):
        if i == len(arr) - 1:
            sol += 1
        i += 1
    else:
        i -= 1
        last = i
        sol += 1


print(sol)
