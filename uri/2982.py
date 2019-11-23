import math
n = int(input())

ans = 0

for i in range(n):
    [a, b] = input().split()
    b = int(b)
    if a == 'G':
        ans -= b
    else:
        ans += b
if ans >= 0:
    print("A greve vai parar.")
else:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
