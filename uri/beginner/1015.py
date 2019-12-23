x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

print("%0.4f" % (((x1-x2)**2 + (y2-y1)**2)**0.5))
