def run():
    n = int(input())
    x = 0.0
    y = 0.0
    for i in range(n):
        a, b = map(float, input().split())
        x += a * b
        y += 100.0 * b
    print("%.4f" % (x/y))


while True:
    try:
        run()
    except:
        break
