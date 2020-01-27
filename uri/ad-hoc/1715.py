
n, m = map(int, input().split())
ans = 0
for x in range(n):
    arr = [int(x) for x in input().split()]
    ans += int(arr.count(0) == 0)
print(ans)
