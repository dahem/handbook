n = int(input())
for x in range(n):
    a, b = map(float, input().split())
    if b == 0:
        print("divisao impossivel")
        continue
    print("%.1f" % (a/b))
