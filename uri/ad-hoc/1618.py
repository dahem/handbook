cases = int(input())
for cas in range(cases):
    arr = [int(x) for x in input().split()]
    x = arr[-2]
    y = arr[-1]
    if arr[0] <= x <= arr[2] and arr[1] <= y <= arr[-3]:
        print(1)
    else:
        print(0)
