import math
n = int(input())
for i in range(n):
    name = input()
    m = float(input())
    arr = [float(x) for x in input().split()]
    arr.sort()
    print("%s %.2f" % (name, sum(arr[1:-1]) * m))
