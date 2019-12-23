import math
n = int(input())
h = w = 0
uh = uw = 0
for i in range(n):
    n, m = input().split()
    if n == 'chuva':
        if uh == 0:
            h += 1
            uw += 1
        else:
            uh -= 1
            uw += 1

    if m == 'chuva':
        if uw == 0:
            w += 1
            uh += 1
        else:
            uw -= 1
            uh += 1

print(h, w)
