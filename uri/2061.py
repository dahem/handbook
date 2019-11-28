import math
n, m = map(int, input().split())
ans = n
for i in range(m):
    x = input()
    if x == 'fechou':
        ans += 1
    else:
        ans -= 1
print(ans)
