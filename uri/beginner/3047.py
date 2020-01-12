n = int(input())
arr = [0, 0, 0]
arr[0] = int(input())
arr[1] = int(input())
arr[2] = n - sum(arr)

print(max(arr))
