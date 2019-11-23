
n = int(input())
maxi = 0
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
    maxi = max(maxi, x)
if maxi == arr[0]:
    print("S")
else:
    print("N")
