
while True:
    n = int(input())
    if n == 0:
        break
    sa = sb = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a > b:
            sa += 1
        elif b > a:
            sb += 1
    print(sa, sb)
