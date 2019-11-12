n = int(input())
arr = [int(x) for x in input().split()]
mini = 100000000000000000
ind = -1
for x in range(len(arr)):
    if arr[x] < mini:
        mini = arr[x]
        ind = x

print("Menor valor:", mini)
print("Posicao:", ind)
