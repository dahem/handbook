n = int(input())
for x in range(n):
    a, b = map(int, input().split())
    sol = 0
    for y in range(min(a, b) + 1, max(a, b)):
        if y % 2 == 1:
            sol += y
    print(sol)
