cases = int(input())
for x in range(cases):
    k, n = map(int, input().split())
    print(k % n + k // n)
