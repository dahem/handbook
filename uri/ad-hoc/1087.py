def run():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 0:
        raise Exception()
    if x1 == x2 and y1 == y2:
        print(0)
        return
    if x1 == x2 or y1 == y2:
        print(1)
        return
    if abs(x2 - x1) == abs(y2 - y1):
        print(1)
        return
    print(2)


while True:
    try:
        run()
    except:
        break
