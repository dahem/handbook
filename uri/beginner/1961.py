import math
maxi, n = map(int, input().split())

arr = [int(x) for x in input().split()]

for i in range(1, n):
    if abs(arr[i] - arr[i-1]) > maxi:
        print("GAME OVER")
        exit()
print("YOU WIN")
