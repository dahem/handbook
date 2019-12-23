n = int(input())
m = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
arr.sort(reverse=True)

limit = arr[m-1]
ans = 0
for x in arr:
    if x >= limit:
        ans += 1
print(ans)
