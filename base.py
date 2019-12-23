import math
n = int(input())
n, m = map(int, input().split())
arr = [int(x) for x in input().split()]
dp = [[0 for y in range(m)] for x in range(n)]

while True:
    try:
        run()
    except:
        break
