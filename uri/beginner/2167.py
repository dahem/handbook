n = int(input())
arr = [int(x) for x in input().split()]
sol = 0
mini = arr[0]
for i in range(1, len(arr)):
    if mini <= arr[i]:
        mini = arr[i]
    else:
        sol = i
        break
if sol != 0:
    print(sol + 1)
else:
    print(0)
