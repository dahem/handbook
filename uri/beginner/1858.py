n = int(input())
mini = 100
ind = -1
arr = [int(x) for x in input().split()]
for x in range(n):
    if arr[x] < mini:
        mini = arr[x]
        ind = x
print(ind+1)
