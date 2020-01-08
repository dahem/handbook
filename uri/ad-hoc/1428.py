n = int(input())
for x in range(n):
    n, m = map(int, input().split())
    print((n//3) * (m // 3))
