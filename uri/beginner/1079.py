n = int(input().strip())
for x in range(n):
    a, b, c = map(float, input().split())
    print("%.1f" % ((a*2 + b*3 + c*5)/10.0))
