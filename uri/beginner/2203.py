while True:
    try:
        x1, y1, x2, y2, v2, r1, r2 = map(float, input().split())
        dis = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
        if dis + v2 * 1.5 < r1 + r2:
            print("Y")
        else:
            print("N")
    except:
        break
