arr = [int(x) for x in input().split()]
arr.sort()
if arr[0] + arr[1] <= arr[2] and arr[1] + arr[2] <= arr[3]:
    print("N")
else:
    print("S")
