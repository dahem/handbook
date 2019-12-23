def check(a, b):
    return a[0] <= b[0] and a[1] <= b[1]


def run():
    x, y, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        if check([a, b], [x, y]) or check([b, a], [x, y]):
            print("Sim")
        else:
            print("Nao")


while True:
    try:
        run()
    except:
        break
