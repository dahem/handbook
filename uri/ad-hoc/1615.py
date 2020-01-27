cases = int(input())
for cas in range(cases):
    n, m = map(int, input().split())
    arr = [int(x) for x in input().split()]
    ans = -1
    for i in range(1, n+1):
        if arr.count(i) * 2 > m:
            ans = i
            break
    print(ans)
