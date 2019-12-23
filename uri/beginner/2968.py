import math

v, n = map(int, input().split())
ans = []
n *= v
for x in range(9):
    per = (x + 1) * 10 / 100
    ans.append(math.ceil(n * per))

print(" ".join(map(str, ans)))
