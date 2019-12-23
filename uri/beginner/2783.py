t, n, m = map(int, input().split())

arr1 = [int(x) for x in input().split()]

arr2 = [int(x) for x in input().split()]
sol = 0
for x in arr1:
    if x in arr2:
        sol += 1
print(len(arr1) - sol)
